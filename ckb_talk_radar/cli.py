from __future__ import annotations

import argparse
import os
from datetime import datetime, timedelta, timezone

from .discord import DiscordPublishError, compose_discord_brief, publish_to_discord
from .discourse import CrawlError, DiscourseClient
from .publishing import publish_latest_artifacts, render_html_report, render_rss_feed
from .reporting import build_summary, ensure_output_dir, render_report, save_snapshot
from .server import serve_output_dir


def default_model() -> str:
    env_model = os.getenv("CKB_TALK_RADAR_MODEL")
    if env_model:
        return env_model
    if os.getenv("OPENROUTER_API_KEY"):
        return "moonshotai/kimi-k2.6"
    if os.getenv("MOONSHOT_API_KEY"):
        return "kimi-for-coding"
    return "gpt-4.1-mini"


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Crawl recent Nervos Talk activity and generate a summary report."
    )
    parser.add_argument("--base-url", default="https://talk.nervos.org")
    parser.add_argument("--hours", type=int, default=24)
    parser.add_argument("--output-dir", default="outputs")
    parser.add_argument("--timezone", default="Asia/Shanghai")
    parser.add_argument("--max-pages", type=int, default=5)
    parser.add_argument("--timeout", type=int, default=20)
    parser.add_argument("--model", default=default_model())
    parser.add_argument("--skip-ai", action="store_true")
    parser.add_argument("--site-url", default=os.getenv("CKB_TALK_RADAR_SITE_URL") or None)
    parser.add_argument(
        "--site-title",
        default=os.getenv("CKB_TALK_RADAR_SITE_TITLE") or "CKB Talk Radar Daily Brief",
    )
    parser.add_argument(
        "--custom-domain",
        default=os.getenv("CKB_TALK_RADAR_CUSTOM_DOMAIN") or None,
    )
    parser.add_argument(
        "--history-source",
        default=os.getenv("CKB_TALK_RADAR_HISTORY_SOURCE") or None,
    )
    parser.add_argument(
        "--discord-webhook-url",
        default=os.getenv("CKB_TALK_RADAR_DISCORD_WEBHOOK_URL")
        or os.getenv("DISCORD_WEBHOOK_URL")
        or None,
    )
    parser.add_argument(
        "--discord-username",
        default=os.getenv("CKB_TALK_RADAR_DISCORD_USERNAME") or "CKB Talk Radar",
    )
    parser.add_argument(
        "--discord-avatar-url",
        default=os.getenv("CKB_TALK_RADAR_DISCORD_AVATAR_URL") or None,
    )
    parser.add_argument("--serve", action="store_true")
    parser.add_argument("--serve-only", action="store_true")
    parser.add_argument("--host", default="127.0.0.1")
    parser.add_argument("--port", type=int, default=8000)
    return parser


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()

    if args.serve_only:
        serve_output_dir(args.output_dir, host=args.host, port=args.port)
        return 0

    now = datetime.now(timezone.utc)
    since = now - timedelta(hours=args.hours)
    client = DiscourseClient(base_url=args.base_url, timeout=args.timeout)

    try:
        snapshot = client.crawl_recent_activity(
            since=since,
            until=now,
            window_hours=args.hours,
            max_pages=args.max_pages,
        )
    except CrawlError as exc:
        parser.exit(1, f"Crawl failed: {exc}\n")

    output_dir = ensure_output_dir(args.output_dir, run_at=now)
    snapshot_path = output_dir / "snapshot.json"
    report_path = output_dir / "report.md"
    html_path = output_dir / "index.html"
    rss_path = output_dir / "rss.xml"

    save_snapshot(snapshot, snapshot_path)
    summary = build_summary(snapshot, model=args.model, skip_ai=args.skip_ai)
    report = render_report(snapshot, summary, timezone_name=args.timezone)
    report_path.write_text(report, encoding="utf-8")
    html_report = render_html_report(
        snapshot,
        summary,
        timezone_name=args.timezone,
        site_url=args.site_url,
        site_title=args.site_title,
    )
    html_path.write_text(html_report, encoding="utf-8")
    rss_feed = render_rss_feed(
        snapshot,
        summary,
        timezone_name=args.timezone,
        site_url=args.site_url,
        site_title=args.site_title,
    )
    rss_path.write_text(rss_feed, encoding="utf-8")
    latest_dir = publish_latest_artifacts(
        output_dir,
        args.output_dir,
        custom_domain=args.custom_domain,
        timezone_name=args.timezone,
        site_url=args.site_url,
        site_title=args.site_title,
        history_source=args.history_source,
    )

    print(f"Snapshot saved to {snapshot_path}")
    print(f"Report saved to {report_path}")
    print(f"Dashboard saved to {html_path}")
    print(f"RSS saved to {rss_path}")
    print(f"Latest artifacts published to {latest_dir}")

    if args.discord_webhook_url:
        discord_messages = compose_discord_brief(snapshot, summary, site_url=args.site_url)
        try:
            publish_to_discord(
                args.discord_webhook_url,
                discord_messages,
                username=args.discord_username,
                avatar_url=args.discord_avatar_url,
                timeout=args.timeout,
            )
        except DiscordPublishError as exc:
            parser.exit(1, f"Discord publish failed: {exc}\n")
        print(f"Discord brief sent in {len(discord_messages)} message(s)")

    if args.serve:
        serve_output_dir(args.output_dir, host=args.host, port=args.port)
    return 0
