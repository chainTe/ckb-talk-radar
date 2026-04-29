from __future__ import annotations

import json
import re
import shutil
from collections import Counter
from dataclasses import dataclass
from datetime import datetime
from email.utils import format_datetime
from html import escape
from pathlib import Path
from textwrap import shorten
from typing import Any
from xml.sax.saxutils import escape as xml_escape
from zoneinfo import ZoneInfo

from .models import CrawlSnapshot, ForumPost, TopicActivity
from .reporting import SummaryResult, build_summary_sources, extract_keywords, extract_themes, format_dt


RUN_DIR_PATTERN = re.compile(r"^\d{8}-\d{6}$")


@dataclass(slots=True)
class ArchiveEntry:
    run_id: str
    generated_at: datetime
    topics: int
    posts: int
    window_hours: int
    title: str
    href: str


def render_html_report(
    snapshot: CrawlSnapshot,
    summary: SummaryResult,
    *,
    timezone_name: str,
    site_url: str | None = None,
    site_title: str = "CKB Talk Radar Daily Brief",
) -> str:
    zone = ZoneInfo(timezone_name)
    posts = sorted(snapshot.posts, key=lambda item: item.created_at, reverse=True)
    topics = sorted(snapshot.topics, key=lambda item: len(item.recent_posts), reverse=True)
    keywords = extract_keywords(posts, limit=8)
    themes = extract_themes(posts)
    authors = Counter(post.author for post in posts).most_common(6)
    summary_sources = build_summary_sources(snapshot)
    stats = [
        ("Active Topics", str(len(topics))),
        ("Posts", str(len(posts))),
        ("Authors", str(len({post.author for post in posts}))),
        ("Window", f"{snapshot.window_hours}h"),
    ]

    summary_html = markdownish_to_html(summary.body)
    source_rows = render_summary_source_rows(summary_sources, zone)
    stat_cards = "\n".join(
        (
            "<article class=\"stat-card\">"
            f"<span class=\"stat-label\">{escape(label)}</span>"
            f"<strong class=\"stat-value\">{escape(value)}</strong>"
            "</article>"
        )
        for label, value in stats
    )
    keyword_chips = "".join(
        f"<li>{escape(word)}<span>{count}</span></li>" for word, count in keywords
    ) or "<li>暂无关键词<span>0</span></li>"
    theme_rows = "".join(
        (
            "<li>"
            f"<span>{escape(theme)}</span>"
            f"<strong>{count}</strong>"
            "</li>"
        )
        for theme, count in themes.most_common(5)
    ) or "<li><span>其他</span><strong>0</strong></li>"
    author_rows = "".join(
        (
            "<li>"
            f"<span>@{escape(author)}</span>"
            f"<strong>{count}</strong>"
            "</li>"
        )
        for author, count in authors
    ) or "<li><span>暂无作者</span><strong>0</strong></li>"
    topic_cards = "\n".join(render_topic_card(topic, zone) for topic in topics) or (
        "<article class=\"topic-card empty\"><p>最近 24 小时没有抓到活跃话题。</p></article>"
    )
    timeline_rows = "\n".join(render_post_row(post, zone) for post in posts[:18]) or (
        "<article class=\"timeline-row empty\"><p>暂无帖子。</p></article>"
    )

    canonical_tags = ""
    if site_url:
        site_root = site_url.rstrip("/")
        canonical_tags = (
            f'  <link rel="canonical" href="{escape(site_root + "/")}">\n'
            f'  <link rel="alternate" type="application/rss+xml" title="CKB Talk Radar RSS" href="{escape(site_root + "/rss.xml")}">\n'
        )

    return f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{escape(site_title)}</title>
{canonical_tags}  <meta name="description" content="Nervos Talk 最近 24 小时社区日报、活跃话题和 RSS 订阅。">
  <style>
    :root {{
      --bg: #f2eee6;
      --paper: rgba(255, 251, 244, 0.78);
      --ink: #1b160f;
      --muted: #6a5d4b;
      --accent: #b84d1a;
      --accent-soft: rgba(184, 77, 26, 0.14);
      --line: rgba(27, 22, 15, 0.12);
      --shadow: 0 28px 60px rgba(71, 47, 22, 0.12);
    }}
    * {{ box-sizing: border-box; }}
    body {{
      margin: 0;
      color: var(--ink);
      background:
        radial-gradient(circle at top left, rgba(184, 77, 26, 0.18), transparent 30%),
        radial-gradient(circle at 80% 20%, rgba(33, 119, 101, 0.15), transparent 25%),
        linear-gradient(180deg, #f8f2e8 0%, var(--bg) 100%);
      font-family: "Avenir Next", "Segoe UI", sans-serif;
    }}
    body::before {{
      content: "";
      position: fixed;
      inset: 0;
      pointer-events: none;
      background-image:
        linear-gradient(rgba(27, 22, 15, 0.03) 1px, transparent 1px),
        linear-gradient(90deg, rgba(27, 22, 15, 0.03) 1px, transparent 1px);
      background-size: 26px 26px;
      mask-image: linear-gradient(180deg, rgba(0, 0, 0, 0.38), transparent 78%);
    }}
    a {{ color: inherit; }}
    .shell {{
      width: min(1180px, calc(100vw - 32px));
      margin: 0 auto;
      padding: 28px 0 56px;
      position: relative;
    }}
    .hero {{
      display: grid;
      grid-template-columns: 1.35fr 0.9fr;
      gap: 20px;
      align-items: stretch;
    }}
    .hero-panel, .side-panel, .section {{
      background: var(--paper);
      backdrop-filter: blur(16px);
      border: 1px solid rgba(255, 255, 255, 0.45);
      box-shadow: var(--shadow);
      border-radius: 28px;
    }}
    .hero-panel {{
      padding: 34px;
      min-height: 340px;
      position: relative;
      overflow: hidden;
    }}
    .hero-panel::after {{
      content: "Daily Brief";
      position: absolute;
      right: -12px;
      bottom: 6px;
      font-family: "Iowan Old Style", "Palatino Linotype", serif;
      font-size: clamp(52px, 10vw, 120px);
      color: rgba(27, 22, 15, 0.06);
      letter-spacing: -0.06em;
    }}
    .eyebrow {{
      display: inline-flex;
      align-items: center;
      gap: 10px;
      text-transform: uppercase;
      letter-spacing: 0.18em;
      font-size: 12px;
      color: var(--accent);
    }}
    .eyebrow::before {{
      content: "";
      width: 32px;
      height: 1px;
      background: currentColor;
    }}
    h1 {{
      margin: 18px 0 14px;
      font-family: "Iowan Old Style", "Palatino Linotype", serif;
      font-size: clamp(44px, 5vw, 76px);
      line-height: 0.94;
      letter-spacing: -0.05em;
      max-width: 8ch;
    }}
    .lede {{
      margin: 0;
      max-width: 54ch;
      font-size: 17px;
      line-height: 1.75;
      color: var(--muted);
    }}
    .hero-meta {{
      display: flex;
      flex-wrap: wrap;
      gap: 10px;
      margin-top: 26px;
    }}
    .hero-meta span {{
      padding: 10px 14px;
      border-radius: 999px;
      background: rgba(255, 255, 255, 0.72);
      border: 1px solid var(--line);
      font-size: 13px;
      color: var(--muted);
    }}
    .side-panel {{
      padding: 24px;
      display: grid;
      gap: 16px;
    }}
    .stat-grid {{
      display: grid;
      grid-template-columns: repeat(2, minmax(0, 1fr));
      gap: 12px;
    }}
    .stat-card {{
      border-radius: 22px;
      padding: 18px;
      background: rgba(255, 255, 255, 0.84);
      border: 1px solid var(--line);
      min-height: 116px;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
    }}
    .stat-label {{
      color: var(--muted);
      text-transform: uppercase;
      letter-spacing: 0.12em;
      font-size: 11px;
    }}
    .stat-value {{
      font-size: clamp(28px, 4vw, 42px);
      line-height: 1;
      font-family: "Iowan Old Style", "Palatino Linotype", serif;
    }}
    .feed-box {{
      border-radius: 22px;
      background: linear-gradient(135deg, #1d3d38, #28554c 62%, #17312c);
      color: #f6f0e5;
      padding: 18px 20px;
    }}
    .feed-box p {{
      margin: 0 0 14px;
      line-height: 1.6;
      color: rgba(246, 240, 229, 0.78);
    }}
    .feed-links {{
      display: flex;
      flex-wrap: wrap;
      gap: 10px;
    }}
    .feed-links a {{
      text-decoration: none;
      border-radius: 999px;
      padding: 9px 14px;
      background: rgba(255, 255, 255, 0.1);
      border: 1px solid rgba(255, 255, 255, 0.14);
    }}
    .main-grid {{
      display: grid;
      grid-template-columns: 1.18fr 0.82fr;
      gap: 20px;
      margin-top: 20px;
    }}
    .section {{
      padding: 24px;
    }}
    .section-header {{
      display: flex;
      justify-content: space-between;
      gap: 14px;
      align-items: baseline;
      margin-bottom: 18px;
    }}
    .section-header h2 {{
      margin: 0;
      font-family: "Iowan Old Style", "Palatino Linotype", serif;
      font-size: 30px;
      letter-spacing: -0.04em;
    }}
    .section-header span {{
      color: var(--muted);
      font-size: 13px;
    }}
    .summary-panel {{
      line-height: 1.72;
      color: #2f281f;
    }}
    .summary-panel h3 {{
      margin: 18px 0 10px;
      font-size: 18px;
    }}
    .summary-panel ul {{
      margin: 0;
      padding-left: 18px;
    }}
    .summary-panel ol {{
      margin: 0;
      padding-left: 18px;
    }}
    .summary-panel p {{
      margin: 0 0 10px;
    }}
    .summary-panel code {{
      padding: 2px 6px;
      border-radius: 6px;
      background: rgba(27, 22, 15, 0.08);
      font-size: 0.95em;
    }}
    .summary-panel .citations {{
      font-size: 0.92em;
      color: var(--muted);
      white-space: nowrap;
    }}
    .summary-panel .citations a {{
      color: var(--accent);
      text-decoration: none;
    }}
    .source-index {{
      margin-top: 18px;
      padding-top: 14px;
      border-top: 1px solid var(--line);
    }}
    .source-index h3 {{
      margin: 0 0 10px;
      font-size: 16px;
    }}
    .source-list {{
      list-style: none;
      margin: 0;
      padding: 0;
      display: grid;
      gap: 10px;
    }}
    .source-list li {{
      padding: 10px 12px;
      border-radius: 14px;
      border: 1px solid var(--line);
      background: rgba(255, 255, 255, 0.58);
      font-size: 14px;
      line-height: 1.55;
    }}
    .source-list code {{
      font-size: 12px;
      margin-right: 6px;
    }}
    .source-meta {{
      color: var(--muted);
      font-size: 12px;
    }}
    .topic-list {{
      display: grid;
      gap: 14px;
    }}
    .topic-card {{
      padding: 18px;
      border-radius: 22px;
      border: 1px solid var(--line);
      background: linear-gradient(180deg, rgba(255,255,255,0.8), rgba(255,255,255,0.58));
      display: grid;
      gap: 10px;
    }}
    .topic-card header {{
      display: flex;
      justify-content: space-between;
      gap: 12px;
      align-items: start;
    }}
    .topic-card h3 {{
      margin: 0;
      font-size: 20px;
      line-height: 1.2;
    }}
    .count-pill {{
      flex: 0 0 auto;
      border-radius: 999px;
      padding: 8px 12px;
      background: var(--accent-soft);
      color: var(--accent);
      font-size: 12px;
      font-weight: 600;
    }}
    .meta-line {{
      display: flex;
      flex-wrap: wrap;
      gap: 10px;
      color: var(--muted);
      font-size: 13px;
    }}
    .excerpt {{
      margin: 0;
      color: #463a2c;
      line-height: 1.68;
    }}
    .tag-row {{
      display: flex;
      flex-wrap: wrap;
      gap: 8px;
    }}
    .tag-row span {{
      padding: 6px 10px;
      border-radius: 999px;
      background: rgba(29, 61, 56, 0.08);
      color: #28554c;
      font-size: 12px;
    }}
    .side-stack {{
      display: grid;
      gap: 20px;
    }}
    .mini-list {{
      list-style: none;
      padding: 0;
      margin: 0;
      display: grid;
      gap: 12px;
    }}
    .mini-list li {{
      display: flex;
      justify-content: space-between;
      gap: 14px;
      align-items: center;
      padding-bottom: 12px;
      border-bottom: 1px solid var(--line);
      color: #43372a;
    }}
    .mini-list li:last-child {{ border-bottom: 0; padding-bottom: 0; }}
    .mini-list span {{
      color: var(--muted);
    }}
    .mini-list strong {{
      font-size: 14px;
    }}
    .keyword-cloud {{
      list-style: none;
      padding: 0;
      margin: 0;
      display: flex;
      flex-wrap: wrap;
      gap: 10px;
    }}
    .keyword-cloud li {{
      display: inline-flex;
      align-items: center;
      gap: 8px;
      padding: 8px 12px;
      border-radius: 999px;
      background: rgba(184, 77, 26, 0.08);
      color: #6b2c11;
      font-size: 13px;
    }}
    .keyword-cloud span {{
      display: inline-grid;
      place-items: center;
      width: 22px;
      height: 22px;
      border-radius: 50%;
      background: rgba(184, 77, 26, 0.14);
      font-size: 11px;
    }}
    .timeline {{
      display: grid;
      gap: 12px;
    }}
    .timeline-row {{
      padding: 16px 18px;
      border-radius: 18px;
      border: 1px solid var(--line);
      background: rgba(255,255,255,0.7);
    }}
    .timeline-row time {{
      display: block;
      color: var(--muted);
      font-size: 12px;
      margin-bottom: 6px;
    }}
    .timeline-row strong {{
      display: block;
      font-size: 16px;
      margin-bottom: 6px;
    }}
    .timeline-row p {{
      margin: 0;
      color: #473c2f;
      line-height: 1.66;
    }}
    .footer {{
      padding: 20px 2px 0;
      color: var(--muted);
      font-size: 13px;
    }}
    @media (max-width: 980px) {{
      .hero, .main-grid {{
        grid-template-columns: 1fr;
      }}
    }}
    @media (max-width: 640px) {{
      .shell {{
        width: min(100vw - 20px, 1180px);
        padding-top: 12px;
      }}
      .hero-panel, .side-panel, .section {{
        border-radius: 24px;
      }}
      .hero-panel {{
        padding: 24px;
      }}
      .stat-grid {{
        grid-template-columns: 1fr 1fr;
      }}
    }}
  </style>
</head>
<body>
  <main class="shell">
    <section class="hero">
      <article class="hero-panel">
        <div class="eyebrow">CKB Talk Radar</div>
        <h1>Daily community pulse.</h1>
        <p class="lede">把 Nervos Talk 最近 {snapshot.window_hours} 小时的讨论浓缩成一页日报。左手看 AI 总结，右手看主题热度、关键词和作者活跃度，底部顺手订阅 RSS。</p>
        <div class="hero-meta">
          <span>统计窗口 {escape(format_dt(snapshot.since, zone))} - {escape(format_dt(snapshot.until, zone))}</span>
          <span>生成时间 {escape(format_dt(snapshot.generated_at, zone))}</span>
          <span>总结模式 {escape(summary.mode)}</span>
        </div>
      </article>
      <aside class="side-panel">
        <div class="stat-grid">
          {stat_cards}
        </div>
        <section class="feed-box">
          <p>稳定入口已经写到 <code>outputs/latest/</code>。本地服务启动后，首页会指向这份最新日报，RSS 也会同步刷新。</p>
          <div class="feed-links">
            <a href="./rss.xml">订阅 RSS</a>
            <a href="./history/">历史归档</a>
            <a href="./report.md">查看 Markdown</a>
            <a href="./snapshot.json">查看 JSON</a>
          </div>
        </section>
      </aside>
    </section>

    <section class="main-grid">
      <article class="section">
        <div class="section-header">
          <h2>今天发生了什么</h2>
          <span>{escape(summary.mode)}</span>
        </div>
        <div class="summary-panel">
          {summary_html}
          <div class="source-index">
            <h3>来源索引</h3>
            <ul class="source-list">{source_rows}</ul>
          </div>
        </div>
      </article>

      <aside class="side-stack">
        <section class="section">
          <div class="section-header">
            <h2>Theme Split</h2>
            <span>topic intent</span>
          </div>
          <ul class="mini-list">{theme_rows}</ul>
        </section>

        <section class="section">
          <div class="section-header">
            <h2>Top Authors</h2>
            <span>recent participants</span>
          </div>
          <ul class="mini-list">{author_rows}</ul>
        </section>

        <section class="section">
          <div class="section-header">
            <h2>Keywords</h2>
            <span>conversation texture</span>
          </div>
          <ul class="keyword-cloud">{keyword_chips}</ul>
        </section>
      </aside>
    </section>

    <section class="section" style="margin-top:20px;">
      <div class="section-header">
        <h2>Active Topics</h2>
        <span>sorted by recent post volume</span>
      </div>
      <div class="topic-list">{topic_cards}</div>
    </section>

    <section class="section" style="margin-top:20px;">
      <div class="section-header">
        <h2>Recent Timeline</h2>
        <span>latest 18 posts</span>
      </div>
      <div class="timeline">{timeline_rows}</div>
    </section>

    <footer class="footer">
      Built from Discourse JSON endpoints on {escape(snapshot.base_url)}.
    </footer>
  </main>
</body>
</html>
"""


def render_rss_feed(
    snapshot: CrawlSnapshot,
    summary: SummaryResult,
    *,
    timezone_name: str,
    site_url: str | None = None,
    site_title: str = "CKB Talk Radar",
) -> str:
    zone = ZoneInfo(timezone_name)
    posts = sorted(snapshot.posts, key=lambda item: item.created_at, reverse=True)
    latest_pub_date = posts[0].created_at if posts else snapshot.generated_at
    summary_excerpt = shorten(
        " ".join(line.strip("- ").strip() for line in summary.body.splitlines() if line.strip()),
        width=700,
        placeholder="...",
    )
    channel_link = f"{site_url.rstrip('/')}/" if site_url else f"{snapshot.base_url}/latest"
    atom_link = ""
    if site_url:
        atom_link = (
            f"  <atom:link href=\"{xml_escape(site_url.rstrip('/') + '/rss.xml')}\" "
            "rel=\"self\" type=\"application/rss+xml\" />\n"
        )
    items = [
        render_rss_item(
            title=f"CKB Talk Daily Brief - {snapshot.generated_at.astimezone(zone):%Y-%m-%d}",
            link=channel_link,
            guid=f"tag:ckb-talk-radar,{snapshot.generated_at.date()}:daily-brief",
            pub_date=snapshot.generated_at,
            description=summary_excerpt,
        )
    ]
    for topic in sorted(snapshot.topics, key=lambda item: item.last_posted_at or item.created_at, reverse=True):
        items.append(render_rss_topic_item(topic))

    return (
        "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n"
        "<rss version=\"2.0\" xmlns:atom=\"http://www.w3.org/2005/Atom\">\n"
        "<channel>\n"
        f"  <title>{xml_escape(site_title)}</title>\n"
        f"  <link>{xml_escape(channel_link)}</link>\n"
        "  <description>Daily Nervos Talk community briefing and latest active topics.</description>\n"
        f"  <language>zh-cn</language>\n"
        f"  <lastBuildDate>{format_datetime(latest_pub_date)}</lastBuildDate>\n"
        f"{atom_link}"
        + "".join(items)
        + "</channel>\n"
        "</rss>\n"
    )


def render_history_index(
    entries: list[ArchiveEntry],
    *,
    timezone_name: str,
    site_url: str | None = None,
    site_title: str = "CKB Talk Radar Daily Brief",
) -> str:
    zone = ZoneInfo(timezone_name)
    canonical = ""
    if site_url:
        canonical = f'  <link rel="canonical" href="{escape(site_url.rstrip("/") + "/history/")}">\n'

    cards = "\n".join(
        (
            "<article class=\"archive-card\">"
            f"<time>{escape(format_dt(entry.generated_at, zone))}</time>"
            f"<h2><a href=\"{escape(entry.href)}\">{escape(entry.title)}</a></h2>"
            f"<p>{entry.topics} 个话题 · {entry.posts} 条帖子 · {entry.window_hours}h 窗口</p>"
            f"<a class=\"open-link\" href=\"{escape(entry.href)}\">查看日报</a>"
            "</article>"
        )
        for entry in entries
    ) or "<article class=\"archive-card\"><p>暂无历史归档。</p></article>"

    return f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{escape(site_title)} Archive</title>
{canonical}  <style>
    :root {{
      --bg: #f7f1e8;
      --ink: #1f1810;
      --muted: #6d604f;
      --card: rgba(255, 252, 247, 0.84);
      --line: rgba(31, 24, 16, 0.1);
      --accent: #235a4d;
    }}
    * {{ box-sizing: border-box; }}
    body {{
      margin: 0;
      color: var(--ink);
      background:
        radial-gradient(circle at top right, rgba(35, 90, 77, 0.16), transparent 24%),
        radial-gradient(circle at 10% 10%, rgba(184, 77, 26, 0.12), transparent 22%),
        linear-gradient(180deg, #fbf7ef 0%, var(--bg) 100%);
      font-family: "Avenir Next", "Segoe UI", sans-serif;
    }}
    .wrap {{
      width: min(1100px, calc(100vw - 28px));
      margin: 0 auto;
      padding: 32px 0 56px;
    }}
    .hero {{
      padding: 28px;
      border-radius: 28px;
      background: rgba(255, 252, 247, 0.82);
      border: 1px solid rgba(255,255,255,0.56);
      box-shadow: 0 26px 48px rgba(58, 40, 19, 0.1);
    }}
    .hero h1 {{
      margin: 10px 0 8px;
      font-family: "Iowan Old Style", "Palatino Linotype", serif;
      font-size: clamp(34px, 5vw, 58px);
      letter-spacing: -0.05em;
    }}
    .hero p {{
      margin: 0;
      color: var(--muted);
      line-height: 1.7;
      max-width: 60ch;
    }}
    .hero a {{
      display: inline-block;
      margin-top: 18px;
      color: var(--accent);
    }}
    .grid {{
      margin-top: 18px;
      display: grid;
      gap: 14px;
    }}
    .archive-card {{
      padding: 20px 22px;
      border-radius: 22px;
      background: var(--card);
      border: 1px solid var(--line);
      box-shadow: 0 16px 32px rgba(58, 40, 19, 0.08);
    }}
    .archive-card time {{
      color: var(--muted);
      font-size: 13px;
    }}
    .archive-card h2 {{
      margin: 6px 0 8px;
      font-size: 24px;
      line-height: 1.15;
    }}
    .archive-card p {{
      margin: 0 0 12px;
      color: var(--muted);
    }}
    .open-link {{
      color: var(--accent);
      text-decoration: none;
    }}
  </style>
</head>
<body>
  <main class="wrap">
    <section class="hero">
      <p>CKB Talk Radar</p>
      <h1>Archive</h1>
      <p>这里保留每天生成的社区简报历史版本。首页始终展示最新结果，这里则用来回看过去几天的话题脉络。</p>
      <a href="../">返回最新日报</a>
    </section>
    <section class="grid">
      {cards}
    </section>
  </main>
</body>
</html>
"""


def render_rss_item(
    *,
    title: str,
    link: str,
    guid: str,
    pub_date: datetime,
    description: str,
) -> str:
    return (
        "  <item>\n"
        f"    <title>{xml_escape(title)}</title>\n"
        f"    <link>{xml_escape(link)}</link>\n"
        f"    <guid>{xml_escape(guid)}</guid>\n"
        f"    <pubDate>{format_datetime(pub_date)}</pubDate>\n"
        f"    <description>{xml_escape(description)}</description>\n"
        "  </item>\n"
    )


def render_rss_topic_item(topic: TopicActivity) -> str:
    latest = topic.last_posted_at or topic.created_at
    description = shorten(
        " ".join(post.content_text.replace("\n", " ") for post in topic.recent_posts),
        width=700,
        placeholder="...",
    )
    return render_rss_item(
        title=f"{topic.title} ({len(topic.recent_posts)} posts)",
        link=topic.url,
        guid=f"{topic.url}#recent-{len(topic.recent_posts)}",
        pub_date=latest,
        description=description or f"Recent activity in topic {topic.title}",
    )


def render_topic_card(topic: TopicActivity, zone: ZoneInfo) -> str:
    latest = topic.last_posted_at or topic.created_at
    excerpt = shorten(
        " ".join(post.content_text.replace("\n", " ") for post in topic.recent_posts[:2]),
        width=260,
        placeholder="...",
    )
    tags = "".join(f"<span>{escape(tag)}</span>" for tag in topic.tags[:6])
    if not tags:
        tags = "<span>untagged</span>"
    return (
        "<article class=\"topic-card\">"
        "<header>"
        f"<h3><a href=\"{escape(topic.url)}\">{escape(topic.title)}</a></h3>"
        f"<span class=\"count-pill\">{len(topic.recent_posts)} posts</span>"
        "</header>"
        "<div class=\"meta-line\">"
        f"<span>Latest {escape(format_dt(latest, zone))}</span>"
        f"<span>{escape(', '.join(sorted({post.author for post in topic.recent_posts})) or 'unknown')}</span>"
        "</div>"
        f"<p class=\"excerpt\">{escape(excerpt or 'No excerpt available.')}</p>"
        f"<div class=\"tag-row\">{tags}</div>"
        "</article>"
    )


def render_post_row(post: ForumPost, zone: ZoneInfo) -> str:
    preview = shorten(post.content_text.replace("\n", " "), width=220, placeholder="...")
    return (
        "<article class=\"timeline-row\">"
        f"<time>{escape(format_dt(post.created_at, zone))}</time>"
        f"<strong><a href=\"{escape(post.url)}\">{escape(post.topic_title)}</a> · @{escape(post.author)}</strong>"
        f"<p>{escape(preview)}</p>"
        "</article>"
    )


def render_summary_source_rows(sources: list[object], zone: ZoneInfo) -> str:
    rows = []
    for source in sources:
        rows.append(
            (
                f'<li id="source-{escape(str(source.citation_id).lower())}">'
                f"<div><code>{escape(str(source.citation_id))}</code>"
                f'<a href="{escape(str(source.url))}">{escape(str(source.topic_title))}</a></div>'
                f'<div class="source-meta">{escape(str(source.author))} · {escape(format_dt(source.created_at, zone))}</div>'
                f"<div>{escape(str(source.excerpt))}</div>"
                "</li>"
            )
        )
    return "".join(rows) or "<li>暂无来源索引。</li>"


def markdownish_to_html(markdown_text: str) -> str:
    blocks: list[str] = []
    list_type: str | None = None
    for raw_line in markdown_text.splitlines():
        line = raw_line.strip()
        if not line:
            if list_type is not None:
                blocks.append(f"</{list_type}>")
                list_type = None
            continue
        if line.startswith("### "):
            if list_type is not None:
                blocks.append(f"</{list_type}>")
                list_type = None
            blocks.append(f"<h3>{render_inline_markdown(line[4:])}</h3>")
            continue
        if line.startswith("## "):
            if list_type is not None:
                blocks.append(f"</{list_type}>")
                list_type = None
            blocks.append(f"<h2>{render_inline_markdown(line[3:])}</h2>")
            continue
        if line.startswith("- "):
            if list_type != "ul":
                if list_type is not None:
                    blocks.append(f"</{list_type}>")
                blocks.append("<ul>")
                list_type = "ul"
            blocks.append(f"<li>{render_inline_markdown(line[2:])}</li>")
            continue
        ordered_match = re.match(r"^\d+\.\s+(.*)$", line)
        if ordered_match:
            if list_type != "ol":
                if list_type is not None:
                    blocks.append(f"</{list_type}>")
                blocks.append("<ol>")
                list_type = "ol"
            blocks.append(f"<li>{render_inline_markdown(ordered_match.group(1))}</li>")
            continue
        if list_type is not None:
            blocks.append(f"</{list_type}>")
            list_type = None
        blocks.append(f"<p>{render_inline_markdown(line)}</p>")
    if list_type is not None:
        blocks.append(f"</{list_type}>")
    return "\n".join(blocks)


def render_inline_markdown(text: str) -> str:
    parts = re.split(r"(`[^`]+`)", text)
    rendered: list[str] = []
    for part in parts:
        if not part:
            continue
        if part.startswith("`") and part.endswith("`") and len(part) >= 2:
            rendered.append(f"<code>{escape(part[1:-1])}</code>")
            continue
        rendered.append(render_inline_markdown_without_code(part))
    return "".join(rendered)


def render_inline_markdown_without_code(text: str) -> str:
    pattern = re.compile(r"\[(S\d+(?:\s*,\s*S\d+)*)\]|\[([^\]]+)\]\(([^)]+)\)|\*\*([^*]+?)\*\*|\*([^*]+?)\*")
    pieces: list[str] = []
    cursor = 0
    for match in pattern.finditer(text):
        pieces.append(escape(text[cursor:match.start()]))
        citation_group, link_text, link_url, bold_text, italic_text = match.groups()
        if citation_group is not None:
            citation_links = ", ".join(
                f'<a href="#source-{escape(citation_id.lower())}">{escape(citation_id)}</a>'
                for citation_id in (item.strip() for item in citation_group.split(","))
            )
            pieces.append(f'<span class="citations">[{citation_links}]</span>')
        elif link_text is not None and link_url is not None:
            safe_url = sanitize_href(link_url)
            pieces.append(
                f'<a href="{escape(safe_url)}" target="_blank" rel="noreferrer">{escape(link_text)}</a>'
            )
        elif bold_text is not None:
            pieces.append(f"<strong>{escape(bold_text)}</strong>")
        elif italic_text is not None:
            pieces.append(f"<em>{escape(italic_text)}</em>")
        cursor = match.end()
    pieces.append(escape(text[cursor:]))
    return "".join(pieces)


def sanitize_href(url: str) -> str:
    candidate = url.strip()
    if candidate.startswith(("http://", "https://", "mailto:")):
        return candidate
    return "#"


def publish_latest_artifacts(
    run_dir: str | Path,
    output_root: str | Path,
    *,
    custom_domain: str | None = None,
    timezone_name: str = "Asia/Shanghai",
    site_url: str | None = None,
    site_title: str = "CKB Talk Radar Daily Brief",
    history_source: str | Path | None = None,
) -> Path:
    latest_dir = Path(output_root) / "latest"
    latest_dir.mkdir(parents=True, exist_ok=True)
    for filename in ("snapshot.json", "report.md", "index.html", "rss.xml"):
        source = Path(run_dir) / filename
        if source.exists():
            shutil.copy2(source, latest_dir / filename)
    archive_dir = latest_dir / "archive"
    history_dir = latest_dir / "history"
    shutil.rmtree(archive_dir, ignore_errors=True)
    shutil.rmtree(history_dir, ignore_errors=True)
    archive_dir.mkdir(parents=True, exist_ok=True)
    history_dir.mkdir(parents=True, exist_ok=True)

    entries = collect_archive_entries(output_root, archive_dir, history_source)
    history_html = render_history_index(
        entries,
        timezone_name=timezone_name,
        site_url=site_url,
        site_title=site_title,
    )
    (history_dir / "index.html").write_text(history_html, encoding="utf-8")
    (latest_dir / ".nojekyll").write_text("", encoding="utf-8")
    if custom_domain:
        (latest_dir / "CNAME").write_text(f"{custom_domain.strip()}\n", encoding="utf-8")
    return latest_dir


def collect_archive_entries(
    output_root: str | Path,
    archive_dir: Path,
    history_source: str | Path | None,
) -> list[ArchiveEntry]:
    entries: dict[str, ArchiveEntry] = {}

    if history_source:
        seed_archive_dir = Path(history_source) / "archive"
        if seed_archive_dir.exists():
            for source_dir in sorted(seed_archive_dir.iterdir()):
                if not source_dir.is_dir():
                    continue
                target_dir = archive_dir / source_dir.name
                shutil.copytree(source_dir, target_dir, dirs_exist_ok=True)
                entry = build_archive_entry(target_dir, source_dir.name)
                if entry is not None:
                    entries[entry.run_id] = entry

    for source_dir in iter_local_run_dirs(output_root):
        target_dir = archive_dir / source_dir.name
        target_dir.mkdir(parents=True, exist_ok=True)
        for filename in ("snapshot.json", "report.md", "index.html", "rss.xml"):
            source = source_dir / filename
            if source.exists():
                shutil.copy2(source, target_dir / filename)
        entry = build_archive_entry(target_dir, source_dir.name)
        if entry is not None:
            entries[entry.run_id] = entry

    return sorted(entries.values(), key=lambda item: item.run_id, reverse=True)


def iter_local_run_dirs(output_root: str | Path) -> list[Path]:
    root = Path(output_root)
    dirs: list[Path] = []
    for item in root.iterdir():
        if not item.is_dir():
            continue
        if item.name in {"latest", ".site-history"}:
            continue
        if RUN_DIR_PATTERN.match(item.name) and (item / "snapshot.json").exists():
            dirs.append(item)
    return sorted(dirs)


def build_archive_entry(run_dir: Path, run_id: str) -> ArchiveEntry | None:
    snapshot_path = run_dir / "snapshot.json"
    index_path = run_dir / "index.html"
    if not snapshot_path.exists() or not index_path.exists():
        return None
    data = json.loads(snapshot_path.read_text(encoding="utf-8"))
    topics = data.get("topics", [])
    posts = sum(len(topic.get("recent_posts", [])) for topic in topics)
    title = f"{run_id} Daily Brief"
    return ArchiveEntry(
        run_id=run_id,
        generated_at=datetime.fromisoformat(data["generated_at"]),
        topics=len(topics),
        posts=posts,
        window_hours=int(data.get("window_hours", 24)),
        title=title,
        href=f"../archive/{run_id}/",
    )
