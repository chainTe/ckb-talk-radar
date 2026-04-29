from __future__ import annotations

import json
import os
import re
from collections import Counter
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from textwrap import shorten
from typing import Iterable
from zoneinfo import ZoneInfo

from .models import CrawlSnapshot, ForumPost, TopicActivity


STOPWORDS = {
    "the",
    "and",
    "that",
    "with",
    "this",
    "have",
    "from",
    "your",
    "about",
    "there",
    "their",
    "they",
    "will",
    "would",
    "what",
    "when",
    "where",
    "which",
    "while",
    "into",
    "just",
    "also",
    "than",
    "then",
    "them",
    "been",
    "being",
    "more",
    "some",
    "could",
    "should",
    "because",
    "very",
    "much",
    "make",
    "made",
    "here",
    "only",
    "over",
    "after",
    "before",
    "these",
    "those",
    "using",
    "used",
    "like",
    "still",
    "even",
    "for",
    "not",
    "local",
    "week",
    "weeks",
    "status",
    "report",
    "update",
    "notes",
    "thanks",
    "thank",
    "hello",
    "please",
    "into",
    "from",
    "community",
    "nervos",
    "talk",
    "https",
    "http",
    "com",
    "org",
}

AI_TOPIC_LIMIT = 12
AI_POSTS_PER_TOPIC = 6
AI_POST_EXCERPT_WIDTH = 280
AI_MAX_COMPLETION_TOKENS = 6400

THEME_KEYWORDS = {
    "技术开发": {
        "sdk",
        "fiber",
        "ckb",
        "script",
        "contract",
        "protocol",
        "transaction",
        "node",
        "rpc",
        "testnet",
        "mainnet",
        "wallet",
        "integration",
    },
    "生态进展": {
        "launch",
        "product",
        "project",
        "tool",
        "platform",
        "app",
        "release",
        "partnership",
        "grant",
        "ecosystem",
    },
    "社区互动": {
        "ama",
        "event",
        "meetup",
        "discussion",
        "feedback",
        "question",
        "tutorial",
        "guide",
        "share",
        "community",
    },
    "市场与传播": {
        "market",
        "trading",
        "listing",
        "price",
        "campaign",
        "media",
        "twitter",
        "x.com",
        "growth",
    },
}


@dataclass(slots=True)
class SummaryResult:
    mode: str
    body: str
    note: str | None = None


class SummaryGenerationError(RuntimeError):
    """Raised when AI summary generation is requested but does not succeed."""


def ensure_output_dir(base_dir: str | Path, run_at: datetime) -> Path:
    run_dir = Path(base_dir) / run_at.strftime("%Y%m%d-%H%M%S")
    run_dir.mkdir(parents=True, exist_ok=True)
    return run_dir


def save_snapshot(snapshot: CrawlSnapshot, path: str | Path) -> None:
    with Path(path).open("w", encoding="utf-8") as handle:
        json.dump(snapshot.to_dict(), handle, ensure_ascii=False, indent=2)


def build_summary(snapshot: CrawlSnapshot, *, model: str) -> SummaryResult:
    return try_openai_summary(snapshot=snapshot, model=model)


def try_openai_summary(snapshot: CrawlSnapshot, *, model: str) -> SummaryResult:
    api_key, base_url, provider_name = resolve_llm_credentials()
    if not api_key:
        raise SummaryGenerationError(
            "AI summary requested but no API key is configured. "
            "Set OPENROUTER_API_KEY / MOONSHOT_API_KEY / OPENAI_API_KEY."
        )

    try:
        from openai import OpenAI
    except ImportError:
        raise SummaryGenerationError(
            "AI summary requested but the `openai` package is not installed."
        )

    client_kwargs = {"api_key": api_key}
    if base_url:
        client_kwargs["base_url"] = base_url
    client = OpenAI(**client_kwargs)
    prompt = build_ai_prompt(snapshot)
    request_kwargs: dict[str, object] = {
        "model": model,
        "messages": [
            {
                "role": "system",
                "content": (
                    "你是 Nervos 社区研究员。请基于提供的最近社区帖子，输出中文分析。"
                    "不要编造未出现的信息；如果信息不足，要明确指出。"
                ),
            },
            {"role": "user", "content": prompt},
        ],
        "max_completion_tokens": AI_MAX_COMPLETION_TOKENS,
    }
    if provider_name == "openrouter":
        # Reasoning tokens count toward output budget on OpenRouter, so keep them
        # out of the visible response and request no extra reasoning budget.
        request_kwargs["reasoning"] = {"exclude": True, "effort": "none"}
    try:
        response = client.chat.completions.create(**request_kwargs)
        text = extract_chat_completion_text(response)
        if not text:
            raise SummaryGenerationError(describe_empty_chat_completion(response))
        return SummaryResult(mode=f"ai:{provider_name}", body=text)
    except Exception as exc:
        if isinstance(exc, SummaryGenerationError):
            raise
        raise SummaryGenerationError(f"AI summary request failed: {exc}") from exc


def resolve_llm_credentials() -> tuple[str | None, str | None, str]:
    openrouter_api_key = os.getenv("OPENROUTER_API_KEY")
    openrouter_base_url = os.getenv("OPENROUTER_BASE_URL")
    moonshot_api_key = os.getenv("MOONSHOT_API_KEY")
    moonshot_base_url = os.getenv("MOONSHOT_BASE_URL")
    openai_api_key = os.getenv("OPENAI_API_KEY")
    openai_base_url = os.getenv("OPENAI_BASE_URL")

    if openrouter_api_key:
        return (
            openrouter_api_key,
            openrouter_base_url or "https://openrouter.ai/api/v1",
            "openrouter",
        )
    if moonshot_api_key:
        return (
            moonshot_api_key,
            moonshot_base_url or "https://api.kimi.com/coding/v1",
            "kimi",
        )
    if openai_api_key:
        provider_name = "openai-compatible" if openai_base_url else "openai"
        return (openai_api_key, openai_base_url, provider_name)
    return (None, openai_base_url, "openai")


def extract_chat_completion_text(response: object) -> str:
    choices = getattr(response, "choices", None) or []
    if not choices:
        return ""
    message = getattr(choices[0], "message", None)
    if message is None:
        return ""
    content = getattr(message, "content", "")
    if content is None:
        return ""
    if isinstance(content, str):
        return content.strip()
    if isinstance(content, list):
        parts: list[str] = []
        for item in content:
            text = getattr(item, "text", None)
            if text:
                parts.append(str(text))
            elif isinstance(item, dict) and item.get("text"):
                parts.append(str(item["text"]))
        return "\n".join(part.strip() for part in parts if part.strip()).strip()
    return str(content).strip()


def describe_empty_chat_completion(response: object) -> str:
    choices = getattr(response, "choices", None) or []
    if not choices:
        return "AI summary returned no choices."
    choice = choices[0]
    message = getattr(choice, "message", None)
    finish_reason = getattr(choice, "finish_reason", None)
    details: list[str] = []
    if finish_reason:
        details.append(f"finish_reason={finish_reason}")
    if message is not None:
        refusal = getattr(message, "refusal", None)
        reasoning = getattr(message, "reasoning", None)
        tool_calls = getattr(message, "tool_calls", None)
        if refusal:
            details.append(f"refusal={str(refusal).strip()[:160]}")
        if reasoning:
            details.append("reasoning_present=true")
        if tool_calls:
            details.append("tool_calls_present=true")
    if details:
        return "AI summary returned empty content. " + "; ".join(details)
    return "AI summary returned empty content."


def build_ai_prompt(snapshot: CrawlSnapshot) -> str:
    topic_blocks: list[str] = []
    for topic in snapshot.topics[:AI_TOPIC_LIMIT]:
        header = (
            f"话题: {topic.title}\n"
            f"链接: {topic.url}\n"
            f"最近24小时帖子数: {len(topic.recent_posts)}\n"
        )
        post_blocks: list[str] = []
        for post in topic.recent_posts[:AI_POSTS_PER_TOPIC]:
            post_blocks.append(
                "\n".join(
                    [
                        f"- 作者: {post.author}",
                        f"  时间: {post.created_at.isoformat()}",
                        f"  内容: {shorten(post.content_text, width=AI_POST_EXCERPT_WIDTH, placeholder='...')}",
                    ]
                )
            )
        topic_blocks.append(f"{header}\n" + "\n".join(post_blocks))

    return "\n\n".join(
        [
            f"请总结 Nervos Talk 最近 {snapshot.window_hours} 小时发生了什么。",
            "请把结果写成面向读者的一份中文日报，不要写成学术分析。",
            "请按下面结构输出，并尽量像人在写社区晨报：",
            "## 今日发生了什么",
            "用 2 到 4 句话先讲清楚今天论坛最主要的事情。",
            "## 重点话题",
            "用 3 到 5 条 bullet 概括今天最值得关注的话题，每条都说明发生了什么。",
            "## 值得继续跟进",
            "列出 2 到 3 条值得后续观察的方向或风险。",
            "要求：",
            "- 使用简洁中文",
            "- 优先总结“发生了什么”，不要只是罗列关键词",
            "- 不要编造帖子里没有出现的信息",
            "- 如果今天内容很少，要明确说社区今天整体较平静",
            "",
            "原始材料：",
            *topic_blocks,
        ]
    )
def render_report(
    snapshot: CrawlSnapshot,
    summary: SummaryResult,
    *,
    timezone_name: str,
) -> str:
    zone = ZoneInfo(timezone_name)
    posts = snapshot.posts
    authors = sorted({post.author for post in posts})
    topic_lines = render_topic_lines(snapshot.topics, zone)
    recent_post_lines = render_recent_post_lines(posts, zone)

    lines: list[str] = [
        "# Nervos Talk 社区简报",
        "",
        f"- 统计窗口: {format_dt(snapshot.since, zone)} 到 {format_dt(snapshot.until, zone)}",
        f"- 生成时间: {format_dt(snapshot.generated_at, zone)}",
        f"- 话题数: {len(snapshot.topics)}",
        f"- 帖子数: {len(posts)}",
        f"- 作者数: {len(authors)}",
        f"- 总结模式: {summary.mode}",
    ]

    if summary.note:
        lines.append(f"- 备注: {summary.note}")

    lines.extend(
        [
            "",
            "## 社区总结",
            "",
            summary.body.strip(),
            "",
            "## 活跃话题",
            "",
            *topic_lines,
            "",
            "## 最近帖子摘录",
            "",
            *recent_post_lines,
        ]
    )
    return "\n".join(lines).strip() + "\n"


def render_topic_lines(topics: Iterable[TopicActivity], zone: ZoneInfo) -> list[str]:
    lines: list[str] = []
    for index, topic in enumerate(topics, start=1):
        latest = format_dt(topic.last_posted_at or topic.created_at, zone)
        tags = f" | tags: {', '.join(topic.tags)}" if topic.tags else ""
        lines.append(
            f"{index}. [{topic.title}]({topic.url}) | {len(topic.recent_posts)} 条近窗帖子 | 最新活动 {latest}{tags}"
        )
    if not lines:
        return ["暂无最近 24 小时内容。"]
    return lines


def render_recent_post_lines(posts: list[ForumPost], zone: ZoneInfo) -> list[str]:
    lines: list[str] = []
    for post in sorted(posts, key=lambda item: item.created_at, reverse=True)[:20]:
        preview = shorten(post.content_text.replace("\n", " "), width=180, placeholder="...")
        lines.append(
            f"- {format_dt(post.created_at, zone)} | {post.author} | [{post.topic_title}]({post.url}) | {preview}"
        )
    if not lines:
        return ["暂无帖子。"]
    return lines


def format_dt(value: datetime, zone: ZoneInfo) -> str:
    return value.astimezone(zone).strftime("%Y-%m-%d %H:%M:%S %Z")


def extract_keywords(posts: Iterable[ForumPost], limit: int = 15) -> list[tuple[str, int]]:
    counter: Counter[str] = Counter()
    for post in posts:
        tokens = re.findall(r"[a-zA-Z][a-zA-Z0-9_.-]{2,}", post.content_text.lower())
        for token in tokens:
            if token in STOPWORDS:
                continue
            if token.startswith("www."):
                continue
            counter[token] += 1
    return counter.most_common(limit)


def extract_themes(posts: Iterable[ForumPost]) -> Counter[str]:
    counter: Counter[str] = Counter()
    for post in posts:
        lowered = post.content_text.lower()
        best_theme: str | None = None
        best_score = 0
        for theme, keywords in THEME_KEYWORDS.items():
            score = sum(1 for keyword in keywords if keyword in lowered)
            if score > best_score:
                best_theme = theme
                best_score = score
        if best_theme is None:
            counter["其他"] += 1
        else:
            counter[best_theme] += 1
    return counter
