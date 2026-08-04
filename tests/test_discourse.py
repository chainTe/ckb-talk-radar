from __future__ import annotations

import unittest
from datetime import datetime, timezone
from unittest import mock

from ckb_talk_radar.discourse import DiscourseClient, extract_tag_names


class TagParsingTests(unittest.TestCase):
    def test_iter_recent_topics_normalizes_tag_objects(self) -> None:
        payload = {
            "topic_list": {
                "topics": [
                    {
                        "id": 123,
                        "title": "CKB topic",
                        "slug": "ckb-topic",
                        "created_at": "2026-08-04T01:00:00Z",
                        "last_posted_at": "2026-08-04T02:00:00Z",
                        "category_id": 1,
                        "tags": [
                            {"id": 52, "name": "CKB", "slug": "52-tag"},
                            {"id": 17, "name": "CKB-VM", "slug": "ckb-vm"},
                        ],
                        "posters": [],
                    }
                ]
            }
        }
        client = DiscourseClient("https://talk.nervos.org")

        with mock.patch.object(client, "fetch_json", return_value=payload):
            topics = list(
                client.iter_recent_topics(
                    since=datetime(2026, 8, 3, tzinfo=timezone.utc),
                    max_pages=1,
                )
            )

        self.assertEqual(topics[0].tags, ["CKB", "CKB-VM"])

    def test_extract_tag_names_supports_discourse_tag_objects(self) -> None:
        raw_tags = [
            {"id": 52, "name": "CKB", "slug": "52-tag"},
            {"id": 17, "name": "CKB-VM", "slug": "ckb-vm"},
        ]

        self.assertEqual(extract_tag_names(raw_tags), ["CKB", "CKB-VM"])

    def test_extract_tag_names_preserves_strings_and_uses_slug_fallback(self) -> None:
        raw_tags = [
            "fiber",
            {"slug": "lang-en"},
            {"name": " fiber "},
            {"id": 99},
            None,
        ]

        self.assertEqual(extract_tag_names(raw_tags), ["fiber", "lang-en"])

    def test_extract_tag_names_rejects_non_list_payloads(self) -> None:
        self.assertEqual(extract_tag_names({"name": "CKB"}), [])


if __name__ == "__main__":
    unittest.main()
