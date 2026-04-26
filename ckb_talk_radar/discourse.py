from __future__ import annotations

import json
import re
from dataclasses import dataclass
from datetime import datetime, timezone
from html import unescape
from typing import Any, Iterable
from urllib.error import HTTPError, URLError
from urllib.parse import urlencode, urljoin
from urllib.request import Request, urlopen

from .models import CrawlSnapshot, ForumPost, TopicActivity


TAG_BREAKS = re.compile(r"(?i)<\s*(br|/p|/div|/li|/h[1-6])\s*/?>")
TAG_STRIP = re.compile(r"<[^>]+>")
WHITESPACE = re.compile(r"[ \t\r\f\v]+")
BLANK_LINES = re.compile(r"\n{3,}")


class CrawlError(RuntimeError):
    """Raised when a crawl request fails."""


@dataclass(slots=True)
class TopicSeed:
    topic_id: int
    title: str
    slug: str
    created_at: datetime
    last_posted_at: datetime | None
    category_id: int | None
    tags: list[str]
    posters: list[str]


class DiscourseClient:
    def __init__(self, base_url: str, timeout: int = 20) -> None:
        self.base_url = base_url.rstrip("/")
        self.timeout = timeout

    def crawl_recent_activity(
        self,
        *,
        since: datetime,
        until: datetime,
        window_hours: int,
        max_pages: int = 5,
    ) -> CrawlSnapshot:
        seeds = list(self.iter_recent_topics(since=since, max_pages=max_pages))
        topics: list[TopicActivity] = []

        for seed in seeds:
            topic = self.fetch_topic_activity(seed=seed, since=since)
            if topic.recent_posts:
                topics.append(topic)

        topics.sort(
            key=lambda item: item.last_posted_at or item.created_at,
            reverse=True,
        )
        return CrawlSnapshot(
            base_url=self.base_url,
            generated_at=datetime.now(timezone.utc),
            since=since,
            until=until,
            window_hours=window_hours,
            topics=topics,
        )

    def iter_recent_topics(self, *, since: datetime, max_pages: int) -> Iterable[TopicSeed]:
        seen_topic_ids: set[int] = set()

        for page in range(max_pages):
            params = {"page": page} if page else None
            payload = self.fetch_json("/latest.json", params=params)
            topics = payload.get("topic_list", {}).get("topics", [])
            if not topics:
                return

            oldest_activity: datetime | None = None
            any_recent = False

            for raw_topic in topics:
                topic_id = int(raw_topic["id"])
                if topic_id in seen_topic_ids:
                    continue

                seen_topic_ids.add(topic_id)
                created_at = parse_timestamp(raw_topic["created_at"])
                last_posted_at = parse_timestamp_nullable(
                    raw_topic.get("last_posted_at") or raw_topic.get("bumped_at")
                )
                activity_at = last_posted_at or created_at

                if oldest_activity is None or activity_at < oldest_activity:
                    oldest_activity = activity_at

                if activity_at < since and created_at < since:
                    continue

                any_recent = True
                yield TopicSeed(
                    topic_id=topic_id,
                    title=raw_topic["title"],
                    slug=raw_topic["slug"],
                    created_at=created_at,
                    last_posted_at=last_posted_at,
                    category_id=raw_topic.get("category_id"),
                    tags=list(raw_topic.get("tags", [])),
                    posters=extract_poster_names(raw_topic.get("posters", [])),
                )

            if oldest_activity is not None and oldest_activity < since and not any_recent:
                return

    def fetch_topic_activity(self, *, seed: TopicSeed, since: datetime) -> TopicActivity:
        payload = self.fetch_topic_json(topic_id=seed.topic_id, slug=seed.slug)
        posts = self._fetch_all_posts(seed.topic_id, payload)

        recent_posts = [
            to_forum_post(self.base_url, payload, post)
            for post in posts
            if parse_timestamp(post["created_at"]) >= since
        ]
        recent_posts.sort(key=lambda item: item.created_at)

        return TopicActivity(
            topic_id=seed.topic_id,
            title=seed.title,
            slug=seed.slug,
            url=build_topic_url(self.base_url, seed.slug, seed.topic_id),
            created_at=seed.created_at,
            last_posted_at=seed.last_posted_at,
            category_id=seed.category_id,
            tags=seed.tags,
            posters=seed.posters,
            recent_posts=recent_posts,
        )

    def fetch_topic_json(self, *, topic_id: int, slug: str) -> dict[str, Any]:
        candidates = [f"/t/{topic_id}.json", f"/t/{slug}/{topic_id}.json"]
        errors: list[Exception] = []

        for path in candidates:
            try:
                return self.fetch_json(path)
            except CrawlError as exc:
                errors.append(exc)

        detail = "; ".join(str(item) for item in errors)
        raise CrawlError(f"Unable to fetch topic {topic_id}: {detail}")

    def fetch_json(self, path: str, params: dict[str, Any] | None = None) -> dict[str, Any]:
        url = urljoin(f"{self.base_url}/", path.lstrip("/"))
        if params:
            url = f"{url}?{urlencode(params, doseq=True)}"

        request = Request(
            url,
            headers={
                "Accept": "application/json",
                "User-Agent": "ckb-talk-radar/0.1",
            },
        )
        try:
            with urlopen(request, timeout=self.timeout) as response:
                return json.load(response)
        except HTTPError as exc:
            raise CrawlError(f"{url} returned HTTP {exc.code}") from exc
        except URLError as exc:
            raise CrawlError(f"{url} failed: {exc.reason}") from exc

    def _fetch_all_posts(self, topic_id: int, payload: dict[str, Any]) -> list[dict[str, Any]]:
        post_stream = payload.get("post_stream", {})
        loaded_posts = {int(post["id"]): post for post in post_stream.get("posts", [])}
        stream_ids = [int(post_id) for post_id in post_stream.get("stream", [])]
        missing_ids = [post_id for post_id in stream_ids if post_id not in loaded_posts]

        for batch in chunked(missing_ids, 50):
            extra_payload = self.fetch_json(
                f"/t/{topic_id}/posts.json",
                params={"post_ids[]": batch},
            )
            for post in extract_posts(extra_payload):
                loaded_posts[int(post["id"])] = post

        if stream_ids:
            return [loaded_posts[post_id] for post_id in stream_ids if post_id in loaded_posts]
        return list(loaded_posts.values())


def extract_posts(payload: dict[str, Any]) -> list[dict[str, Any]]:
    if "post_stream" in payload:
        return list(payload["post_stream"].get("posts", []))
    if "posts" in payload:
        return list(payload.get("posts", []))
    return []


def parse_timestamp(value: str) -> datetime:
    return datetime.fromisoformat(value.replace("Z", "+00:00"))


def parse_timestamp_nullable(value: str | None) -> datetime | None:
    if not value:
        return None
    return parse_timestamp(value)


def extract_poster_names(raw_posters: list[dict[str, Any]]) -> list[str]:
    names: list[str] = []
    for item in raw_posters:
        description = item.get("description") or ""
        user_id = item.get("user_id")
        if description:
            names.append(description)
        elif user_id is not None:
            names.append(str(user_id))
    return names


def build_topic_url(base_url: str, slug: str, topic_id: int, post_number: int | None = None) -> str:
    path = f"/t/{slug}/{topic_id}"
    if post_number:
        path = f"{path}/{post_number}"
    return urljoin(f"{base_url}/", path.lstrip("/"))


def clean_cooked_html(cooked_html: str) -> str:
    text = TAG_BREAKS.sub("\n", cooked_html)
    text = TAG_STRIP.sub("", text)
    text = unescape(text)
    text = WHITESPACE.sub(" ", text)
    text = re.sub(r"\s*\n\s*", "\n", text)
    text = BLANK_LINES.sub("\n\n", text)
    return text.strip()


def to_forum_post(base_url: str, topic_payload: dict[str, Any], post: dict[str, Any]) -> ForumPost:
    topic_id = int(topic_payload["id"])
    slug = topic_payload["slug"]
    title = topic_payload["title"]
    post_number = int(post["post_number"])
    return ForumPost(
        post_id=int(post["id"]),
        post_number=post_number,
        topic_id=topic_id,
        topic_title=title,
        topic_slug=slug,
        author=post.get("username", "unknown"),
        created_at=parse_timestamp(post["created_at"]),
        updated_at=parse_timestamp_nullable(post.get("updated_at")),
        reply_to_post_number=post.get("reply_to_post_number"),
        url=build_topic_url(base_url, slug, topic_id, post_number),
        content_text=clean_cooked_html(post.get("cooked", "")),
        content_html=post.get("cooked", ""),
        like_count=int(post.get("like_count", 0)),
        quote_count=int(post.get("quote_count", 0)),
    )


def chunked(items: list[int], size: int) -> Iterable[list[int]]:
    for index in range(0, len(items), size):
        yield items[index : index + size]
