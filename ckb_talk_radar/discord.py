from __future__ import annotations

import json
import re
import time
from collections.abc import Iterable
from dataclasses import dataclass
from textwrap import shorten
from typing import Any
from urllib import error, request

from .models import CrawlSnapshot, TopicActivity
from .reporting import SummaryResult, extract_keywords, extract_themes


DISCORD_MESSAGE_LIMIT = 2000
SECTION_TITLES = ("今日发生了什么", "重点话题", "值得继续跟进")
SECTION_HEADING_RE = re.compile(r"^\s*#{2,6}\s*(.+?)\s*$")


class DiscordPublishError(RuntimeError):
    """Raised when the Discord webhook publish flow fails."""


@dataclass(slots=True)
class DiscordPayload:
    content: str
    username: str | None = None
    avatar_url: str | None = None

    def to_dict(self) -> dict[str, Any]:
        payload: dict[str, Any] = {"content": self.content}
        if self.username:
            payload["username"] = self.username
        if self.avatar_url:
            payload["avatar_url"] = self.avatar_url
        return payload


def compose_discord_brief(
    snapshot: CrawlSnapshot,
    summary: SummaryResult,
    *,
    site_url: str | None = None,
    message_limit: int = DISCORD_MESSAGE_LIMIT,
) -> list[str]:
    sections = parse_summary_sections(summary.body)
    lines: list[str] = [
        "# Nervos Talk 社区简报",
        "",
        "## 社区总结",
        build_community_summary(snapshot),
        "",
        "## 今日发生了什么",
        sections.get("今日发生了什么") or build_today_section(snapshot),
        "",
        "## 重点话题",
        sections.get("重点话题") or build_topic_section(snapshot),
        "",
        "## 值得继续跟进",
        sections.get("值得继续跟进") or build_followup_section(snapshot),
    ]

    if site_url:
        lines.extend(["", f"link: {site_url.rstrip('/')}"])

    message = "\n".join(lines).strip()
    return split_discord_message(message, limit=message_limit)


def parse_summary_sections(markdown: str) -> dict[str, str]:
    sections: dict[str, list[str]] = {}
    current_title: str | None = None

    for raw_line in markdown.splitlines():
        line = raw_line.rstrip()
        match = SECTION_HEADING_RE.match(line)
        if match:
            title = normalize_heading(match.group(1))
            current_title = title if title in SECTION_TITLES else None
            if current_title:
                sections.setdefault(current_title, [])
            continue
        if current_title:
            sections[current_title].append(line)

    cleaned: dict[str, str] = {}
    for title, content in sections.items():
        trimmed = trim_empty_lines(content)
        if trimmed:
            cleaned[title] = "\n".join(trimmed)
    return cleaned


def normalize_heading(heading: str) -> str:
    return heading.strip().rstrip("：:")


def trim_empty_lines(lines: Iterable[str]) -> list[str]:
    items = list(lines)
    while items and not items[0].strip():
        items.pop(0)
    while items and not items[-1].strip():
        items.pop()
    return items


def build_community_summary(snapshot: CrawlSnapshot) -> str:
    posts = snapshot.posts
    topics = snapshot.topics
    unique_authors = {post.author for post in posts}
    if not topics:
        return f"最近 {snapshot.window_hours} 小时社区整体比较平静，暂未捕获到新的活跃讨论。"

    hottest = max(topics, key=lambda item: len(item.recent_posts))
    return (
        f"最近 {snapshot.window_hours} 小时共捕获 {len(topics)} 个活跃话题、"
        f"{len(posts)} 条帖子、{len(unique_authors)} 位作者。"
        f" 当前热度最高的话题是《{hottest.title}》，窗口内新增 {len(hottest.recent_posts)} 条帖子/回复。"
    )


def build_today_section(snapshot: CrawlSnapshot) -> str:
    posts = snapshot.posts
    topics = snapshot.topics
    if not topics:
        return f"- 最近 {snapshot.window_hours} 小时论坛整体较平静，没有形成明显的新讨论波峰。"

    unique_authors = len({post.author for post in posts})
    hottest = max(topics, key=lambda item: len(item.recent_posts))
    return "\n".join(
        [
            f"- 最近 {snapshot.window_hours} 小时论坛共有 {len(topics)} 个活跃话题、{len(posts)} 条帖子、{unique_authors} 位参与者。",
            f"- 讨论最集中在《{hottest.title}》，该话题在统计窗口内出现了 {len(hottest.recent_posts)} 条新帖或回复。",
        ]
    )


def build_topic_section(snapshot: CrawlSnapshot) -> str:
    topics = sorted(snapshot.topics, key=lambda item: len(item.recent_posts), reverse=True)[:5]
    if not topics:
        return "- 今天没有形成明显的重点话题。"

    return "\n".join(render_topic_bullet(topic, window_hours=snapshot.window_hours) for topic in topics)


def render_topic_bullet(topic: TopicActivity, *, window_hours: int) -> str:
    preview = shorten(
        " ".join(post.content_text.replace("\n", " ") for post in topic.recent_posts[:2]),
        width=140,
        placeholder="...",
    )
    detail = preview or "该话题暂未提取到更多正文线索。"
    return (
        f"- [{topic.title}]({topic.url})：近 {window_hours} 小时有 {len(topic.recent_posts)} 条新帖/回复。"
        f" 讨论主要围绕 {detail}"
    )


def build_followup_section(snapshot: CrawlSnapshot) -> str:
    posts = snapshot.posts
    theme_counts = extract_themes(posts)
    keyword_counts = extract_keywords(posts, limit=8)
    lines: list[str] = []

    if theme_counts:
        dominant = "、".join(f"{theme}（{count}）" for theme, count in theme_counts.most_common(3))
        lines.append(f"- 当前讨论重心主要落在：{dominant}。")
    if keyword_counts:
        lines.append("- 可以继续跟踪这些高频线索：" + "、".join(word for word, _ in keyword_counts) + "。")
    lines.append("- 建议继续关注高回复话题中的新增回复，它们通常最能反映社区下一步的实际关注点。")
    return "\n".join(lines)


def split_discord_message(message: str, *, limit: int = DISCORD_MESSAGE_LIMIT) -> list[str]:
    if len(message) <= limit:
        return [message]

    chunks: list[str] = []
    current = ""
    for line in message.splitlines():
        candidate = f"{current}\n{line}".strip("\n") if current else line
        if len(candidate) <= limit:
            current = candidate
            continue
        if current:
            chunks.append(current)
            current = ""
        if len(line) <= limit:
            current = line
            continue
        chunks.extend(split_long_line(line, limit=limit))

    if current:
        chunks.append(current)
    return chunks


def split_long_line(line: str, *, limit: int) -> list[str]:
    pieces: list[str] = []
    remainder = line.strip()
    while remainder:
        if len(remainder) <= limit:
            pieces.append(remainder)
            break
        split_at = remainder.rfind(" ", 0, limit)
        if split_at <= 0:
            split_at = limit
        pieces.append(remainder[:split_at].rstrip())
        remainder = remainder[split_at:].lstrip()
    return pieces


def publish_to_discord(
    webhook_url: str,
    messages: Iterable[str],
    *,
    username: str | None = None,
    avatar_url: str | None = None,
    timeout: int = 20,
) -> None:
    for content in messages:
        send_webhook_message(
            webhook_url,
            DiscordPayload(content=content, username=username, avatar_url=avatar_url),
            timeout=timeout,
        )


def send_webhook_message(webhook_url: str, payload: DiscordPayload, *, timeout: int = 20) -> None:
    body = json.dumps(payload.to_dict(), ensure_ascii=False).encode("utf-8")
    http_request = request.Request(
        webhook_url,
        data=body,
        headers={"Content-Type": "application/json"},
        method="POST",
    )

    for attempt in range(2):
        try:
            with request.urlopen(http_request, timeout=timeout) as response:
                status = getattr(response, "status", None) or response.getcode()
                if 200 <= status < 300:
                    return
                raise DiscordPublishError(f"Discord webhook returned unexpected status {status}.")
        except error.HTTPError as exc:
            if exc.code == 429 and attempt == 0:
                retry_after = read_retry_after_seconds(exc)
                time.sleep(retry_after)
                continue
            detail = exc.read().decode("utf-8", errors="replace")
            raise DiscordPublishError(
                f"Discord webhook request failed with status {exc.code}: {detail}"
            ) from exc
        except error.URLError as exc:
            raise DiscordPublishError(f"Discord webhook request failed: {exc}") from exc


def read_retry_after_seconds(exc: error.HTTPError) -> float:
    try:
        data = json.loads(exc.read().decode("utf-8"))
    except (OSError, ValueError, json.JSONDecodeError):
        return 1.0
    retry_after = data.get("retry_after", 1)
    try:
        return max(float(retry_after), 0.0)
    except (TypeError, ValueError):
        return 1.0
