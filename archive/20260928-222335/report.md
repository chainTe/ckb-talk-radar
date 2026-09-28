# Nervos Talk 社区简报

- 统计窗口: 2026-09-28 06:23:35 CST 到 2026-09-29 06:23:35 CST
- 生成时间: 2026-09-29 06:23:42 CST
- 话题数: 5
- 帖子数: 7
- 作者数: 6
- 总结模式: ai:openai-compatible

## 社区总结

## 今日发生了什么

今天 Nervos Talk 可见的新内容主要集中在几个既有方向的进展：Cellula.id 集成、CKB Community Fund DAO Dashboard、LS-IDL、CKB 节点收入层，以及隐私订单簿 appchain 周报 [S01, S02, S05, S06, S07]。其中 DAO Dashboard 帖从工具介绍转出了实际问题反馈，有用户报告落地页被重定向到错误页，并随后出现了相关 GitHub PR [S02, S03, S04]。整体看，今天不是大量新主题爆发的一天，更多是已有讨论帖的推进和问题暴露 [S01, S03, S04, S05, S06, S07]。

## 重点话题

- CKB Community Fund DAO Dashboard 上线后遇到 bug 反馈：JackyLHH 介绍了一个用 AI 工具制作的 Dashboard，用于集中查看 DAO 规则、提案、投票结果、执行进展与资金使用情况，并支持中英文 [S02]；随后 ebubedev 反馈网站落地页会被重定向到错误页 [S03]；之后又出现一个相关 GitHub PR，标题指向保留已审阅的双语里程碑概览、不再重新解析到 MyMemory [S04]。
- Cellula.id 计划集成进 Pocket Node：Jnr6 表示会把 Cellula.id 集成进 Pocket Node，时间可能在 M5 或之后 [S01]；开发者已在 Pocket Node 仓库开 PR 跟踪进度 [S01]。
- LS-IDL 更新到 0.1.0，并走向版本化接口协议：OWK50GA 说项目已从 flat lock-witness 原型成长为带可用工具的版本化接口协议 [S05]；IDL 0.1.0 现在有独立规范、JSON Schema、canonical fixtures 和 conformance vectors [S05]。
- CKB 节点收入层应不应该是单独项目：janx 认为应该作为单独项目，收集和排名全节点并与奖励关联，这超出 CKBadger 的范围 [S06]。
- 隐私订单簿 appchain 发布周报：Lawliet_Chan 在 2026.9.28 周报中称开发了 proof of buy 的 CKB 合约和前端部分功能 [S07]；并附上 invisibook 仓库 PR #8 链接 [S07]。

## 值得继续跟进

- DAO Dashboard 的错误页问题是否解决、相关 PR 是否合并，以及双语里程碑概览处理是否落地 [S03, S04]。
- Cellula.id 集成 Pocket Node 目前只是“M5 或之后”的计划，后续要看跟踪 PR 的实际进展 [S01]。
- LS-IDL 0.1.0 的规范、fixtures 和 conformance vectors 如何被工具链采用 [S05]；节点收入层是否独立成项目、如何收集排名全节点并关联奖励，仍值得观察 [S06]。

## 来源索引

- `S01` [Cellula.id: `.cell` names on CKB, with the contracts public and reproducible](https://talk.nervos.org/t/cellula-id-cell-names-on-ckb-with-the-contracts-public-and-reproducible/10753/6) | Jnr6 | 2026-09-29 04:22:32 CST | i will be integrating this into Pocket Node, probably around M5 or after, the developer opened a Pr on PN repo to track the progress, if you’re interested to see how it progress. Check here
- `S02` [一站式查看 CKB Community Fund DAO 提案、投票与执行进展](https://talk.nervos.org/t/ckb-community-fund-dao/10793/1) | JackyLHH | 2026-09-28 15:38:27 CST | 我想介绍一下用 AI 工具制作的 CKB Community Fund DAO Dashboard。构建这个网站主要是为了方便大家集中查看 DAO 的规则、提案、投票结果、执行进展与资金使用情况。 网址： https://ckbcommunityfunddao.xyz 主要功能 实时抓取并整理 Nervos Talk、Metaforo 等公开来源的数据 浏览 DAO 提案及其当前状态 查看某个提案的概览、路线图、申请预算、投票结果和进展 追踪提案人发布的周报、里程碑报告与结项报告 按状态和提案类型搜索、筛选 支持中文和英文 提供邮件与...
- `S03` [一站式查看 CKB Community Fund DAO 提案、投票与执行进展](https://talk.nervos.org/t/ckb-community-fund-dao/10793/2) | ebubedev | 2026-09-28 20:07:07 CST | pls check the website theres is bug that redirect the landing page to this error page Screenshot 2026-09-28 at 13.05.282916×1898 156 KB
- `S04` [一站式查看 CKB Community Fund DAO 提案、投票与执行进展](https://talk.nervos.org/t/ckb-community-fund-dao/10793/3) | ebubedev | 2026-09-29 01:32:46 CST | github.com/JackyLHH/ckb-community-fund-dao-dashboard Keep reviewed bilingual overviews instead of re-parsing them into MyMemory (#2) main ← chukwuma619:fix/keep-reviewed-milestone-overview opened 05:32PM - 28 Sep 26 UTC chukwuma619 +561 -823 ## Summary Production...
- `S05` [LS-IDL: a Lock Script Interface Description Language for CKB (derive, validate, commit)](https://talk.nervos.org/t/ls-idl-a-lock-script-interface-description-language-for-ckb-derive-validate-commit/10596/5) | OWK50GA | 2026-09-28 20:12:21 CST | TL;DR Since my original CKB IDL post, the project has grown from a flat lock-witness prototype into a versioned interface protocol with working tooling: IDL 0.1.0 now has a standalone specification, JSON Schema, canonical fixtures and conformance vectors. The Rust derive...
- `S06` [A Revenue Layer for CKB Nodes](https://talk.nervos.org/t/a-revenue-layer-for-ckb-nodes/10734/15) | janx | 2026-09-28 13:44:49 CST | I believe it should be a separate project. Collecting and ranking full nodes (possibly with daemons running alongside the CKB node), and linking these to rewards is beyond CKBadger’s scope.
- `S07` [[DIS] Decentralized privacy order-book appchain based on CKB L1 - 2026.phase-1](https://talk.nervos.org/t/dis-decentralized-privacy-order-book-appchain-based-on-ckb-l1-2026-phase-1/10015/46) | Lawliet_Chan | 2026-09-28 10:38:29 CST | 周报 2026.9.28 开发proof of buy的CKB合约和前端部分功能： define proof of buy by Lawliet-Chan · Pull Request #8 · invisibook-lab/invisibook · GitHub

## 活跃话题

1. [Cellula.id: `.cell` names on CKB, with the contracts public and reproducible](https://talk.nervos.org/t/cellula-id-cell-names-on-ckb-with-the-contracts-public-and-reproducible/10753) | 1 条近窗帖子 | 最新活动 2026-09-29 04:22:32 CST | tags: CKB, dapp
2. [一站式查看 CKB Community Fund DAO 提案、投票与执行进展](https://talk.nervos.org/t/ckb-community-fund-dao/10793) | 3 条近窗帖子 | 最新活动 2026-09-29 01:32:46 CST
3. [LS-IDL: a Lock Script Interface Description Language for CKB (derive, validate, commit)](https://talk.nervos.org/t/ls-idl-a-lock-script-interface-description-language-for-ckb-derive-validate-commit/10596) | 1 条近窗帖子 | 最新活动 2026-09-28 20:12:21 CST | tags: CKB
4. [A Revenue Layer for CKB Nodes](https://talk.nervos.org/t/a-revenue-layer-for-ckb-nodes/10734) | 1 条近窗帖子 | 最新活动 2026-09-28 13:44:49 CST | tags: CKB, CKB-VM
5. [[DIS] Decentralized privacy order-book appchain based on CKB L1 - 2026.phase-1](https://talk.nervos.org/t/dis-decentralized-privacy-order-book-appchain-based-on-ckb-l1-2026-phase-1/10015) | 1 条近窗帖子 | 最新活动 2026-09-28 10:38:29 CST | tags: appchain

## 最近帖子摘录

- 2026-09-29 04:22:32 CST | Jnr6 | [Cellula.id: `.cell` names on CKB, with the contracts public and reproducible](https://talk.nervos.org/t/cellula-id-cell-names-on-ckb-with-the-contracts-public-and-reproducible/10753/6) | i will be integrating this into Pocket Node, probably around M5 or after, the developer opened a Pr on PN repo to track the progress, if you’re interested to see how it...
- 2026-09-29 01:32:46 CST | ebubedev | [一站式查看 CKB Community Fund DAO 提案、投票与执行进展](https://talk.nervos.org/t/ckb-community-fund-dao/10793/3) | github.com/JackyLHH/ckb-community-fund-dao-dashboard Keep reviewed bilingual overviews instead of re-parsing them into MyMemory (#2) main ← chukwuma619:fix/keep-reviewed-...
- 2026-09-28 20:12:21 CST | OWK50GA | [LS-IDL: a Lock Script Interface Description Language for CKB (derive, validate, commit)](https://talk.nervos.org/t/ls-idl-a-lock-script-interface-description-language-for-ckb-derive-validate-commit/10596/5) | TL;DR Since my original CKB IDL post, the project has grown from a flat lock-witness prototype into a versioned interface protocol with working tooling: IDL 0.1.0 now has a...
- 2026-09-28 20:07:07 CST | ebubedev | [一站式查看 CKB Community Fund DAO 提案、投票与执行进展](https://talk.nervos.org/t/ckb-community-fund-dao/10793/2) | pls check the website theres is bug that redirect the landing page to this error page Screenshot 2026-09-28 at 13.05.282916×1898 156 KB
- 2026-09-28 15:38:27 CST | JackyLHH | [一站式查看 CKB Community Fund DAO 提案、投票与执行进展](https://talk.nervos.org/t/ckb-community-fund-dao/10793/1) | 我想介绍一下用 AI 工具制作的 CKB Community Fund DAO Dashboard。构建这个网站主要是为了方便大家集中查看 DAO 的规则、提案、投票结果、执行进展与资金使用情况。 网址： https://ckbcommunityfunddao.xyz 主要功能 实时抓取并整理 Nervos Talk、Metaforo 等公开来源的数据...
- 2026-09-28 13:44:49 CST | janx | [A Revenue Layer for CKB Nodes](https://talk.nervos.org/t/a-revenue-layer-for-ckb-nodes/10734/15) | I believe it should be a separate project. Collecting and ranking full nodes (possibly with daemons running alongside the CKB node), and linking these to rewards is beyond...
- 2026-09-28 10:38:29 CST | Lawliet_Chan | [[DIS] Decentralized privacy order-book appchain based on CKB L1 - 2026.phase-1](https://talk.nervos.org/t/dis-decentralized-privacy-order-book-appchain-based-on-ckb-l1-2026-phase-1/10015/46) | 周报 2026.9.28 开发proof of buy的CKB合约和前端部分功能： define proof of buy by Lawliet-Chan · Pull Request #8 · invisibook-lab/invisibook · GitHub
