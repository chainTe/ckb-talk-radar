from __future__ import annotations

import io
import tempfile
import unittest
from datetime import datetime, timezone
from pathlib import Path
from types import SimpleNamespace
from unittest import mock
from urllib import error

from ckb_talk_radar.discord import (
    DEFAULT_DISCORD_USER_AGENT,
    DiscordPayload,
    build_discord_request,
    compose_discord_brief,
    parse_summary_sections,
    read_retry_after_seconds,
    split_discord_message,
    strip_summary_citations,
)
from ckb_talk_radar.discourse import clean_cooked_html
from ckb_talk_radar.models import CrawlSnapshot, ForumPost, TopicActivity
from ckb_talk_radar.publishing import (
    markdownish_to_html,
    publish_latest_artifacts,
    render_history_index,
    render_html_report,
    render_rss_feed,
)
from ckb_talk_radar.reporting import (
    SummaryGenerationError,
    build_summary,
    build_chat_request_kwargs,
    build_summary_sources,
    build_citation_repair_prompt,
    describe_empty_chat_completion,
    extract_citation_ids,
    extract_chat_completion_text,
    extract_keywords,
    repair_summary_citations,
    render_report,
    request_summary_text,
    resolve_llm_credentials,
    split_summary_sentences,
    try_openai_summary,
    validate_summary_citations,
)


class CleaningTests(unittest.TestCase):
    def test_clean_cooked_html(self) -> None:
        raw = "<p>Hello <strong>Fiber</strong><br>world &amp; friends</p>"
        cleaned = clean_cooked_html(raw)
        self.assertEqual(cleaned, "Hello Fiber\nworld & friends")


class SummaryTests(unittest.TestCase):
    def test_extract_keywords(self) -> None:
        post = ForumPost(
            post_id=1,
            post_number=1,
            topic_id=10,
            topic_title="Fiber update",
            topic_slug="fiber-update",
            author="alice",
            created_at=datetime(2026, 4, 26, 8, 0, tzinfo=timezone.utc),
            updated_at=None,
            reply_to_post_number=None,
            url="https://example.com/t/fiber-update/10/1",
            content_text="Fiber SDK release for CKB wallet integration",
            content_html="",
            like_count=1,
            quote_count=0,
        )
        keywords = dict(extract_keywords([post], limit=10))
        self.assertIn("fiber", keywords)
        self.assertIn("sdk", keywords)

    def test_render_html_report(self) -> None:
        snapshot = make_snapshot()
        html = render_html_report(
            snapshot,
            type("Summary", (), {"mode": "ai:openrouter", "body": "### 核心结论\n- Fiber 很活跃。[S01]", "note": None})(),
            timezone_name="Asia/Shanghai",
            site_url="https://example.github.io/ckb-talk-radar",
        )
        self.assertIn("Daily community pulse.", html)
        self.assertIn("./rss.xml", html)
        self.assertIn("Fiber update", html)
        self.assertIn("canonical", html)
        self.assertIn("来源索引", html)
        self.assertIn("#source-s01", html)

    def test_markdownish_to_html_supports_inline_markdown(self) -> None:
        html = markdownish_to_html(
            "\n".join(
                [
                    "## 重点话题",
                    "- **Bold** with `code` and [link](https://example.com) [S01]",
                    "1. *Italic* item [S02]",
                ]
            )
        )
        self.assertIn("<strong>Bold</strong>", html)
        self.assertIn("<code>code</code>", html)
        self.assertIn('href="https://example.com"', html)
        self.assertIn('href="#source-s01"', html)
        self.assertIn("<ol>", html)
        self.assertIn("<em>Italic</em>", html)

    def test_render_rss_feed(self) -> None:
        snapshot = make_snapshot()
        rss = render_rss_feed(
            snapshot,
            type("Summary", (), {"mode": "ai:openrouter", "body": "### 核心结论\n- Fiber 很活跃。[S01]", "note": None})(),
            timezone_name="Asia/Shanghai",
            site_url="https://example.github.io/ckb-talk-radar",
        )
        self.assertIn("<rss version=\"2.0\"", rss)
        self.assertIn("Fiber update", rss)
        self.assertIn("CKB Talk Radar", rss)
        self.assertIn("atom:link", rss)

    def test_render_history_index(self) -> None:
        snapshot = make_snapshot()
        html = render_history_index(
            entries=[
                type(
                    "Entry",
                    (),
                    {
                        "run_id": "20260426-090000",
                        "generated_at": snapshot.generated_at,
                        "topics": 1,
                        "posts": 1,
                        "window_hours": 24,
                        "title": "20260426-090000 Daily Brief",
                        "href": "../archive/20260426-090000/",
                    },
                )()
            ],
            timezone_name="Asia/Shanghai",
            site_url="https://example.github.io/ckb-talk-radar",
        )
        self.assertIn("Archive", html)
        self.assertIn("../archive/20260426-090000/", html)

    def test_publish_latest_artifacts_includes_archive(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            run_dir = root / "20260426-090000"
            run_dir.mkdir()
            (run_dir / "snapshot.json").write_text(
                (
                    '{"generated_at":"2026-04-26T09:00:00+00:00","window_hours":24,'
                    '"topics":[{"recent_posts":[{"author":"alice"}]}]}'
                ),
                encoding="utf-8",
            )
            (run_dir / "report.md").write_text("# report", encoding="utf-8")
            (run_dir / "index.html").write_text("<html></html>", encoding="utf-8")
            (run_dir / "rss.xml").write_text("<rss></rss>", encoding="utf-8")

            latest_dir = publish_latest_artifacts(
                run_dir,
                root,
                timezone_name="Asia/Shanghai",
                site_url="https://example.github.io/ckb-talk-radar",
            )

            self.assertTrue((latest_dir / "history" / "index.html").exists())
            self.assertTrue((latest_dir / "archive" / "20260426-090000" / "index.html").exists())

    def test_resolve_llm_credentials_prefers_openrouter(self) -> None:
        with mock.patch.dict(
            "os.environ",
            {
                "OPENROUTER_API_KEY": "openrouter-key",
                "MOONSHOT_API_KEY": "moonshot-key",
                "OPENAI_API_KEY": "openai-key",
            },
            clear=False,
        ):
            api_key, base_url, provider_name = resolve_llm_credentials()
        self.assertEqual(api_key, "openrouter-key")
        self.assertEqual(base_url, "https://openrouter.ai/api/v1")
        self.assertEqual(provider_name, "openrouter")

    def test_resolve_llm_credentials_prefers_moonshot(self) -> None:
        with mock.patch.dict(
            "os.environ",
            {"MOONSHOT_API_KEY": "moonshot-key", "OPENAI_API_KEY": "openai-key"},
            clear=False,
        ):
            api_key, base_url, provider_name = resolve_llm_credentials()
        self.assertEqual(api_key, "moonshot-key")
        self.assertEqual(base_url, "https://api.kimi.com/coding/v1")
        self.assertEqual(provider_name, "kimi")

    def test_extract_chat_completion_text(self) -> None:
        response = type(
            "Resp",
            (),
            {
                "choices": [
                    type(
                        "Choice",
                        (),
                        {"message": type("Msg", (), {"content": "hello"})()},
                    )()
                ]
            },
        )()
        self.assertEqual(extract_chat_completion_text(response), "hello")

    def test_extract_chat_completion_text_returns_empty_when_content_is_none(self) -> None:
        response = type(
            "Resp",
            (),
            {
                "choices": [
                    type(
                        "Choice",
                        (),
                        {"message": type("Msg", (), {"content": None})()},
                    )()
                ]
            },
        )()
        self.assertEqual(extract_chat_completion_text(response), "")

    def test_build_summary_sources_creates_stable_ids(self) -> None:
        snapshot = make_snapshot()
        sources = build_summary_sources(snapshot)
        self.assertTrue(sources)
        self.assertEqual(sources[0].citation_id, "S01")
        self.assertIn("Fiber update", sources[0].topic_title)

    def test_validate_summary_citations_accepts_known_ids(self) -> None:
        snapshot = make_snapshot()
        sources = build_summary_sources(snapshot)
        validate_summary_citations("## 今日发生了什么\n- Fiber 很活跃。[S01]", sources)

    def test_validate_summary_citations_rejects_missing_id(self) -> None:
        snapshot = make_snapshot()
        sources = build_summary_sources(snapshot)
        with self.assertRaises(SummaryGenerationError):
            validate_summary_citations("## 今日发生了什么\n- Fiber 很活跃。", sources)

    def test_build_citation_repair_prompt_mentions_validation_error(self) -> None:
        snapshot = make_snapshot()
        sources = build_summary_sources(snapshot)
        prompt = build_citation_repair_prompt(
            summary_text="## 今日发生了什么\n- Fiber 很活跃。",
            sources=sources,
            validation_error="missing citation",
        )
        self.assertIn("missing citation", prompt)
        self.assertIn("[S01]", prompt)

    def test_split_summary_sentences_and_extract_citation_ids(self) -> None:
        sentences = split_summary_sentences("一句话。[S01] 第二句话。[S02, S03]")
        self.assertEqual(len(sentences), 2)
        self.assertEqual(extract_citation_ids(sentences[1]), ["S02", "S03"])

    def test_render_report_includes_source_index(self) -> None:
        snapshot = make_snapshot()
        report = render_report(
            snapshot,
            type("Summary", (), {"mode": "ai:openrouter", "body": "## 今日发生了什么\n- Fiber 很活跃。[S01]", "note": None})(),
            timezone_name="Asia/Shanghai",
        )
        self.assertIn("## 来源索引", report)
        self.assertIn("`S01`", report)

    def test_describe_empty_chat_completion_includes_finish_reason_and_reasoning(self) -> None:
        response = type(
            "Resp",
            (),
            {
                "choices": [
                    type(
                        "Choice",
                        (),
                        {
                            "finish_reason": "length",
                            "message": type(
                                "Msg",
                                (),
                                {"content": None, "reasoning": "hidden chain", "tool_calls": None},
                            )(),
                        },
                    )()
                ]
            },
        )()
        message = describe_empty_chat_completion(response)
        self.assertIn("finish_reason=length", message)
        self.assertIn("reasoning_present=true", message)

    def test_try_openai_summary_raises_on_provider_error(self) -> None:
        snapshot = make_snapshot()
        fake_client = mock.Mock()
        fake_client.chat.completions.create.side_effect = RuntimeError("Invalid Authentication")
        fake_openai_module = SimpleNamespace(OpenAI=mock.Mock(return_value=fake_client))
        with mock.patch.dict("os.environ", {"MOONSHOT_API_KEY": "moonshot-key"}, clear=False):
            with mock.patch.dict("sys.modules", {"openai": fake_openai_module}):
                with self.assertRaises(SummaryGenerationError) as ctx:
                    try_openai_summary(snapshot=snapshot, model="kimi-for-coding")
        self.assertIn("AI summary request failed", str(ctx.exception))

    def test_build_summary_repairs_missing_citations_once(self) -> None:
        snapshot = make_snapshot()
        first_response = type(
            "Resp",
            (),
            {"choices": [type("Choice", (), {"message": type("Msg", (), {"content": "## 今日发生了什么\n- Fiber 很活跃。"})(), "finish_reason": "stop"})()]},
        )()
        second_response = type(
            "Resp",
            (),
            {"choices": [type("Choice", (), {"message": type("Msg", (), {"content": "## 今日发生了什么\n- Fiber 很活跃。[S01]"})(), "finish_reason": "stop"})()]},
        )()
        fake_client = mock.Mock()
        fake_client.chat.completions.create.side_effect = [first_response, second_response]
        fake_openai_module = SimpleNamespace(OpenAI=mock.Mock(return_value=fake_client))
        with mock.patch.dict("os.environ", {"OPENROUTER_API_KEY": "openrouter-key"}, clear=False):
            with mock.patch.dict("sys.modules", {"openai": fake_openai_module}):
                summary = build_summary(snapshot=snapshot, model="moonshotai/kimi-k2.6")
        self.assertEqual(summary.body, "## 今日发生了什么\n- Fiber 很活跃。[S01]")
        self.assertEqual(fake_client.chat.completions.create.call_count, 2)

    def test_build_summary_raises_when_ai_returns_empty_content(self) -> None:
        snapshot = make_snapshot()
        fake_response = type(
            "Resp",
            (),
            {
                "choices": [
                    type(
                        "Choice",
                        (),
                        {"message": type("Msg", (), {"content": None})()},
                    )()
                ]
            },
        )()
        fake_client = mock.Mock()
        fake_client.chat.completions.create.return_value = fake_response
        fake_openai_module = SimpleNamespace(OpenAI=mock.Mock(return_value=fake_client))
        with mock.patch.dict("os.environ", {"OPENROUTER_API_KEY": "openrouter-key"}, clear=False):
            with mock.patch.dict("sys.modules", {"openai": fake_openai_module}):
                with self.assertRaises(SummaryGenerationError) as ctx:
                    build_summary(snapshot=snapshot, model="moonshotai/kimi-k2.6")
        self.assertIn("empty content", str(ctx.exception))
        fake_client.chat.completions.create.assert_called_once()
        self.assertEqual(
            fake_client.chat.completions.create.call_args.kwargs["extra_body"],
            {"reasoning": {"exclude": True, "effort": "none"}},
        )
        self.assertEqual(
            fake_client.chat.completions.create.call_args.kwargs["max_completion_tokens"],
            6400,
        )

    def test_build_chat_request_kwargs_keeps_openrouter_extra_body(self) -> None:
        kwargs = build_chat_request_kwargs(
            model="moonshotai/kimi-k2.6",
            provider_name="openrouter",
            user_prompt="hello",
        )
        self.assertEqual(
            kwargs["extra_body"],
            {"reasoning": {"exclude": True, "effort": "none"}},
        )

    def test_parse_summary_sections_supports_markdown_headings(self) -> None:
        sections = parse_summary_sections(
            "\n".join(
                [
                    "## 今日发生了什么",
                    "- 社区今天比较热闹",
                    "",
                    "### 重点话题",
                    "- Fiber SDK",
                    "",
                    "## 值得继续跟进：",
                    "- 继续看后续集成进展",
                ]
            )
        )
        self.assertEqual(sections["今日发生了什么"], "- 社区今天比较热闹")
        self.assertEqual(sections["重点话题"], "- Fiber SDK")
        self.assertEqual(sections["值得继续跟进"], "- 继续看后续集成进展")

    def test_compose_discord_brief_includes_expected_sections(self) -> None:
        snapshot = make_snapshot()
        summary = type(
            "Summary",
            (),
            {
                "mode": "ai:openrouter",
                "body": "\n".join(
                    [
                        "## 今日发生了什么",
                        "- 今天主要在聊 Fiber 更新。[S01]",
                        "",
                        "## 重点话题",
                        "- Fiber update：有新的 SDK 进展。[S01]",
                        "",
                        "## 值得继续跟进",
                        "- 继续看 wallet integration 的落地节奏。[S01]",
                    ]
                ),
                "note": None,
            },
        )()
        messages = compose_discord_brief(
            snapshot,
            summary,
            site_url="https://chainte.github.io/ckb-talk-radar",
            message_limit=2000,
        )
        self.assertEqual(len(messages), 1)
        self.assertIn("# Nervos Talk 社区简报", messages[0])
        self.assertIn("## 社区总结", messages[0])
        self.assertIn("## 今日发生了什么", messages[0])
        self.assertIn("link: https://chainte.github.io/ckb-talk-radar", messages[0])
        self.assertNotIn("[S01]", messages[0])

    def test_strip_summary_citations_removes_source_markers(self) -> None:
        cleaned = strip_summary_citations("- Fiber 很活跃。[S01, S02]\n- 继续观察。[S03]")
        self.assertEqual(cleaned, "- Fiber 很活跃。\n- 继续观察。")

    def test_split_discord_message_respects_limit(self) -> None:
        chunks = split_discord_message(("A" * 1500) + "\n" + ("B" * 1500), limit=1800)
        self.assertGreater(len(chunks), 1)
        self.assertTrue(all(len(chunk) <= 1800 for chunk in chunks))

    def test_read_retry_after_seconds_defaults_when_payload_is_invalid(self) -> None:
        http_error = error.HTTPError(
            url="https://discord.example/webhook",
            code=429,
            msg="Too Many Requests",
            hdrs=None,
            fp=io.BytesIO(b"not-json"),
        )
        self.assertEqual(read_retry_after_seconds(http_error), 1.0)
        http_error.close()

    def test_discord_payload_includes_optional_fields(self) -> None:
        payload = DiscordPayload(
            content="hello",
            username="CKB Talk Radar",
            avatar_url="https://example.com/avatar.png",
        )
        self.assertEqual(
            payload.to_dict(),
            {
                "content": "hello",
                "username": "CKB Talk Radar",
                "avatar_url": "https://example.com/avatar.png",
            },
        )

    def test_build_discord_request_sets_expected_headers(self) -> None:
        http_request = build_discord_request("https://discord.example/webhook", b"{}")
        self.assertEqual(http_request.get_method(), "POST")
        self.assertEqual(http_request.headers["Content-type"], "application/json")
        self.assertEqual(http_request.headers["Accept"], "application/json")
        self.assertEqual(http_request.headers["User-agent"], DEFAULT_DISCORD_USER_AGENT)


def make_snapshot() -> CrawlSnapshot:
    post = ForumPost(
        post_id=1,
        post_number=1,
        topic_id=10,
        topic_title="Fiber update",
        topic_slug="fiber-update",
        author="alice",
        created_at=datetime(2026, 4, 26, 8, 0, tzinfo=timezone.utc),
        updated_at=None,
        reply_to_post_number=None,
        url="https://example.com/t/fiber-update/10/1",
        content_text="Fiber SDK release for CKB wallet integration",
        content_html="",
        like_count=1,
        quote_count=0,
    )
    topic = TopicActivity(
        topic_id=10,
        title="Fiber update",
        slug="fiber-update",
        url="https://example.com/t/fiber-update/10",
        created_at=datetime(2026, 4, 26, 7, 0, tzinfo=timezone.utc),
        last_posted_at=datetime(2026, 4, 26, 8, 0, tzinfo=timezone.utc),
        category_id=None,
        tags=["fiber"],
        posters=["alice"],
        recent_posts=[post],
    )
    return CrawlSnapshot(
        base_url="https://example.com",
        generated_at=datetime(2026, 4, 26, 9, 0, tzinfo=timezone.utc),
        since=datetime(2026, 4, 25, 9, 0, tzinfo=timezone.utc),
        until=datetime(2026, 4, 26, 9, 0, tzinfo=timezone.utc),
        window_hours=24,
        topics=[topic],
    )


if __name__ == "__main__":
    unittest.main()
