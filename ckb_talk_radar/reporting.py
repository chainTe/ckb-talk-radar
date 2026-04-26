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


def ensure_output_dir(base_dir: str | Path, run_at: datetime) -> Path:
    run_dir = Path(base_dir) / run_at.strftime("%Y%m%d-%H%M%S")
    run_dir.mkdir(parents=True, exist_ok=True)
    return run_dir


def save_snapshot(snapshot: CrawlSnapshot, path: str | Path) -> None:
    with Path(path).open("w", encoding="utf-8") as handle:
        json.dump(snapshot.to_dict(), handle, ensure_ascii=False, indent=2)


def build_summary(snapshot: CrawlSnapshot, *, model: str, skip_ai: bool) -> SummaryResult:
    if not skip_ai:
        ai_summary = try_openai_summary(snapshot=snapshot, model=model)
        if ai_summary is not None:
            return ai_summary
    return SummaryResult(mode="heuristic", body=build_heuristic_summary(snapshot))


def try_openai_summary(snapshot: CrawlSnapshot, *, model: str) -> SummaryResult | None:
    api_key, base_url, provider_name = resolve_llm_credentials()
    if not api_key:
        return None

    try:
        from openai import OpenAI
    except ImportError:
        return SummaryResult(
            mode="heuristic",
            body=build_heuristic_summary(snapshot),
            note="检测到 OPENAI_API_KEY，但当前环境未安装 `openai` 包，已回退到本地规则总结。",
        )

    client_kwargs = {"api_key": api_key}
    if base_url:
        client_kwargs["base_url"] = base_url
    client = OpenAI(**client_kwargs)
    prompt = build_ai_prompt(snapshot)
    try:
        response = client.chat.completions.create(
            model=model,
            messages=[
                {
                    "role": "system",
                    "content": (
                        "你是 Nervos 社区研究员。请基于提供的最近社区帖子，输出中文分析。"
                        "不要编造未出现的信息；如果信息不足，要明确指出。"
                    ),
                },
                {"role": "user", "content": prompt},
            ],
            max_tokens=1400,
        )
        text = extract_chat_completion_text(response)
        if not text:
            return None
        return SummaryResult(mode=f"ai:{provider_name}", body=text)
    except Exception as exc:
        return SummaryResult(
            mode="heuristic",
            body=build_heuristic_summary(snapshot),
            note=f"AI 总结调用失败，已回退到本地规则总结：{exc}",
        )


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


def build_ai_prompt(snapshot: CrawlSnapshot) -> str:
    topic_blocks: list[str] = []
    for topic in snapshot.topics[:30]:
        header = (
            f"话题: {topic.title}\n"
            f"链接: {topic.url}\n"
            f"最近24小时帖子数: {len(topic.recent_posts)}\n"
        )
        post_blocks: list[str] = []
        for post in topic.recent_posts[:10]:
            post_blocks.append(
                "\n".join(
                    [
                        f"- 作者: {post.author}",
                        f"  时间: {post.created_at.isoformat()}",
                        f"  内容: {shorten(post.content_text, width=500, placeholder='...')}",
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


def build_heuristic_summary(snapshot: CrawlSnapshot) -> str:
    posts = snapshot.posts
    topics = snapshot.topics
    unique_authors = sorted({post.author for post in posts})
    keyword_counts = extract_keywords(posts)
    theme_counts = extract_themes(posts)
    active_topics = sorted(topics, key=lambda item: len(item.recent_posts), reverse=True)[:5]

    lines: list[str] = [
        "### 今日发生了什么",
    ]

    if not topics:
        lines.append("- 最近 24 小时论坛整体比较平静，没有抓到新的活跃讨论。")
    else:
        overview = (
            f"- 最近 {snapshot.window_hours} 小时论坛里共有 {len(topics)} 个活跃话题、"
            f"{len(posts)} 条帖子、{len(unique_authors)} 位参与作者。"
        )
        lines.append(overview)
        if active_topics:
            top_topic = active_topics[0]
            lines.append(
                f"- 今天最集中的讨论围绕“{top_topic.title}”展开，共有 {len(top_topic.recent_posts)} 条近窗帖子。"
            )

    lines.extend(["", "### 重点话题"])

    if active_topics:
        for topic in active_topics[:5]:
            excerpt = shorten(
                " ".join(post.content_text.replace("\n", " ") for post in topic.recent_posts[:2]),
                width=140,
                placeholder="...",
            )
            lines.append(
                f"- {topic.title}：近 24 小时有 {len(topic.recent_posts)} 条新帖/回复。"
                f" 讨论主要围绕 {excerpt or '该话题暂无更多可提取内容'}"
            )
    else:
        lines.append("- 今天没有形成明显的重点讨论话题。")

    lines.extend(["", "### 值得继续跟进"])
    if theme_counts:
        dominant = "、".join(f"{theme}（{count}）" for theme, count in theme_counts.most_common(3))
        lines.append(f"- 当前讨论重心主要落在：{dominant}。")
    if keyword_counts:
        lines.append("- 可以继续跟踪这些高频线索：" + "、".join(word for word, _ in keyword_counts[:8]) + "。")

    lines.append("- 优先查看高回复话题中的最新回复，它们通常最能代表社区当下真实关注点。")
    return "\n".join(lines)


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
