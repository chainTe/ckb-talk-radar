# CKB Talk Radar

每日抓取 `https://talk.nervos.org/latest` 最近 24 小时社区动态，生成一份可以直接发布到 GitHub Pages 的社区简报站点。

输出内容包括：

- `snapshot.json`: 结构化原始数据
- `report.md`: Markdown 版日报
- `index.html`: 前端日报页
- `rss.xml`: RSS 订阅源
- 可选的 OpenAI 中文分析总结

## What It Does

- 通过 Discourse JSON 接口抓取 `latest` 和话题详情
- 过滤最近 `N` 小时内的新主题、新回复和活跃讨论
- 清洗 HTML 正文，生成可读文本
- 汇总活跃话题、作者、关键词、主题分布
- 生成稳定的 `outputs/latest/` 发布目录
- 支持本地静态服务和 RSS
- 支持 GitHub Actions 每日构建并部署到 GitHub Pages
- 支持 AI 总结和本地规则回退

## Quick Start

安装：

```bash
pip3 install -e .
```

本地生成一份最近 24 小时日报：

```bash
python3 -m ckb_talk_radar --hours 24 --skip-ai
```

如果要启用 AI 总结：

```bash
pip3 install -e '.[ai]'
cp .env.example .env
export OPENAI_API_KEY=your_key
python3 -m ckb_talk_radar --hours 24 --model gpt-4.1-mini
```

也可以直接用快捷命令：

```bash
make run
make test
make serve
```

## Local Preview

生成后直接启动本地服务：

```bash
python3 -m ckb_talk_radar --hours 24 --skip-ai --serve
```

如果只想服务已经生成的最新结果：

```bash
python3 -m ckb_talk_radar --serve-only --output-dir outputs --port 8000
```

默认访问地址：

- `http://127.0.0.1:8000/`
- `http://127.0.0.1:8000/rss.xml`

## GitHub Pages

项目已内置工作流 [daily-pages.yml](/Users/guopenglin/ckb-talk-radar/.github/workflows/daily-pages.yml)。

默认行为：

- 推送到 `main` 后立即重新发布
- 每天 `Asia/Shanghai 01:00` 定时更新
- 支持手动触发 `workflow_dispatch`
- 自动将 `outputs/latest/` 发布为 Pages 根目录
- 有 `OPENAI_API_KEY` 时使用 AI 总结，没有则回退到本地总结

启用步骤：

1. 把项目推到 GitHub。
2. 在 `Settings -> Pages` 中把 `Source` 设置为 `GitHub Actions`。
3. 可选：在 `Settings -> Secrets and variables -> Actions` 中添加 `OPENAI_API_KEY`。
4. 可选：在 `Settings -> Secrets and variables -> Actions -> Variables` 中添加：

```text
PAGES_SITE_URL=https://yourname.github.io/ckb-talk-radar
PAGES_SITE_TITLE=CKB Talk Radar Daily Brief
PAGES_CUSTOM_DOMAIN=radar.example.com
```

发布后：

- 首页是日报页 `/`
- RSS 是 `/rss.xml`
- 如果设置了 `PAGES_CUSTOM_DOMAIN`，会自动生成 `CNAME`

## CLI Options

- `--hours`: 统计窗口，默认 `24`
- `--output-dir`: 输出目录，默认 `outputs`
- `--timezone`: 展示时区，默认 `Asia/Shanghai`
- `--max-pages`: 扫描 `latest.json` 的最大分页数，默认 `5`
- `--model`: OpenAI 模型名，默认 `gpt-4.1-mini`
- `--skip-ai`: 强制禁用 AI 总结
- `--site-url`: 公开站点地址，用于 RSS 和 canonical
- `--site-title`: 页面和 RSS 标题
- `--custom-domain`: 生成 GitHub Pages `CNAME`
- `--serve`: 生成后立即启动本地服务
- `--serve-only`: 不抓取，只服务 `outputs/latest/`
- `--host`: 服务监听地址，默认 `127.0.0.1`
- `--port`: 服务端口，默认 `8000`

## Project Layout

```text
ckb_talk_radar/
  cli.py
  discourse.py
  publishing.py
  reporting.py
  server.py
.github/workflows/
  daily-pages.yml
outputs/latest/
  index.html
  report.md
  rss.xml
  snapshot.json
```

## Output Layout

每次运行都会生成一个带时间戳的归档目录，同时刷新稳定发布目录：

```text
outputs/20260426-173000/
  index.html
  snapshot.json
  report.md
  rss.xml
outputs/latest/
  index.html
  snapshot.json
  report.md
  rss.xml
```

## Development

运行测试：

```bash
python3 -m unittest discover -s tests -v
```

或：

```bash
make test
```

## Notes

- 目标站点是 Discourse 社区，优先调用 JSON 接口而不是解析 HTML。
- 当前策略抓取最近 `N` 小时内有活动的话题，只保留窗口内帖子。
- 如果网络环境受限，抓取会失败，需要在可访问外网的环境中运行。
- 本地服务首页默认映射到 `outputs/latest/index.html`，RSS 默认映射到 `/rss.xml`。
- GitHub Actions 的定时任务运行在默认分支上；如果公开仓库 60 天没有活动，GitHub 可能自动暂停调度。
