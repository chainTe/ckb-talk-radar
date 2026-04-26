from __future__ import annotations

import unittest
from datetime import datetime, timezone

from ckb_talk_radar.discourse import clean_cooked_html
from ckb_talk_radar.models import CrawlSnapshot, ForumPost, TopicActivity
from ckb_talk_radar.publishing import render_html_report, render_rss_feed
from ckb_talk_radar.reporting import build_heuristic_summary, extract_keywords


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
