from __future__ import annotations

import tempfile
import unittest
from datetime import datetime, timezone
from pathlib import Path
from types import SimpleNamespace
from unittest import mock

from ckb_talk_radar.discourse import clean_cooked_html
from ckb_talk_radar.models import CrawlSnapshot, ForumPost, TopicActivity
from ckb_talk_radar.publishing import (
    publish_latest_artifacts,
    render_history_index,
    render_html_report,
    render_rss_feed,
)
from ckb_talk_radar.reporting import (
    build_heuristic_summary,
    extract_chat_completion_text,
    extract_keywords,
    resolve_llm_credentials,
    try_openai_summary,
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

    def test_build_heuristic_summary(self) -> None:
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
        snapshot = CrawlSnapshot(
            base_url="https://example.com",
            generated_at=datetime(2026, 4, 26, 9, 0, tzinfo=timezone.utc),
            since=datetime(2026, 4, 25, 9, 0, tzinfo=timezone.utc),
            until=datetime(2026, 4, 26, 9, 0, tzinfo=timezone.utc),
            window_hours=24,
            topics=[topic],
        )

        summary = build_heuristic_summary(snapshot)
        self.assertIn("1 个活跃话题", summary)
        self.assertIn("Fiber update", summary)

    def test_render_html_report(self) -> None:
        snapshot = make_snapshot()
        html = render_html_report(
            snapshot,
            type("Summary", (), {"mode": "heuristic", "body": "### 核心结论\n- Fiber 很活跃", "note": None})(),
            timezone_name="Asia/Shanghai",
            site_url="https://example.github.io/ckb-talk-radar",
        )
        self.assertIn("Daily community pulse.", html)
        self.assertIn("./rss.xml", html)
        self.assertIn("Fiber update", html)
        self.assertIn("canonical", html)

    def test_render_rss_feed(self) -> None:
        snapshot = make_snapshot()
        rss = render_rss_feed(
            snapshot,
            type("Summary", (), {"mode": "heuristic", "body": "### 核心结论\n- Fiber 很活跃", "note": None})(),
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

    def test_try_openai_summary_falls_back_on_provider_error(self) -> None:
        snapshot = make_snapshot()
        fake_client = mock.Mock()
        fake_client.chat.completions.create.side_effect = RuntimeError("Invalid Authentication")
        fake_openai_module = SimpleNamespace(OpenAI=mock.Mock(return_value=fake_client))
        with mock.patch.dict("os.environ", {"MOONSHOT_API_KEY": "moonshot-key"}, clear=False):
            with mock.patch.dict("sys.modules", {"openai": fake_openai_module}):
                summary = try_openai_summary(snapshot=snapshot, model="kimi-for-coding")
        self.assertIsNotNone(summary)
        assert summary is not None
        self.assertEqual(summary.mode, "heuristic")
        self.assertIn("调用失败", summary.note or "")


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
