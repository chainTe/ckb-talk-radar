from __future__ import annotations

from dataclasses import asdict, dataclass
from datetime import datetime
from typing import Any


@dataclass(slots=True)
class ForumPost:
    post_id: int
    post_number: int
    topic_id: int
    topic_title: str
    topic_slug: str
    author: str
    created_at: datetime
    updated_at: datetime | None
    reply_to_post_number: int | None
    url: str
    content_text: str
    content_html: str
    like_count: int
    quote_count: int


@dataclass(slots=True)
class TopicActivity:
    topic_id: int
    title: str
    slug: str
    url: str
    created_at: datetime
    last_posted_at: datetime | None
    category_id: int | None
    tags: list[str]
    posters: list[str]
    recent_posts: list[ForumPost]


@dataclass(slots=True)
class CrawlSnapshot:
    base_url: str
    generated_at: datetime
    since: datetime
    until: datetime
    window_hours: int
    topics: list[TopicActivity]

    @property
    def posts(self) -> list[ForumPost]:
        items: list[ForumPost] = []
        for topic in self.topics:
            items.extend(topic.recent_posts)
        return items

    def to_dict(self) -> dict[str, Any]:
        return _serialize(asdict(self))


def _serialize(value: Any) -> Any:
    if isinstance(value, datetime):
        return value.isoformat()
    if isinstance(value, list):
        return [_serialize(item) for item in value]
    if isinstance(value, dict):
        return {key: _serialize(item) for key, item in value.items()}
    return value
