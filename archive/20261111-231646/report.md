# Nervos Talk 社区简报

- 统计窗口: 2026-11-11 07:16:46 CST 到 2026-11-12 07:16:46 CST
- 生成时间: 2026-11-12 07:16:57 CST
- 话题数: 8
- 帖子数: 9
- 作者数: 8
- 总结模式: ai:openai-compatible

## 社区总结

## 今日发生了什么

今天论坛的主要动态是项目进展更新 [S01, S03, S05]：zk-Lock 的交互式前端已经上线 [S01]；CrowdCell 宣布 M1 仪表盘和发现功能在测试网上线 [S05]；ckbup 以早期版本公开征集反馈 [S03]。此外，iCKB 合约审计复盘称约三分之一合约代码从未运行 [S07]，官网更新讨论也在继续 [S08]。整体看，今天的帖子以开发进展和项目状态更新为主 [S01, S03, S05, S07]。

## 重点话题

- zk-Lock 前端上线：项目方称交互式前端已上线，约一分钟、无需钱包和安装，用户输入秘密词后由浏览器生成证明 [S01]；社区成员祝贺交付，并提到 zk-lock-bound 是对 mempool proof-copy 问题的回应 [S02]。
- CrowdCell 发布 M1 状态：CrowdCell 称 M1 已完成并在测试网 crowdcell.vercel.app 上线，包含钱包感知索引器端点和“My campaigns”等功能 [S05]；CellGuard × CrowdCell 试点帖中，回复提到测试网部署文件与评审 pledge profile 的事项 [S06]。
- ckbup 早期安装器征集反馈：作者开始构建类似 rustup 的开源安装器和版本管理器，用于 CKB 命令行工具，并公开分享以获取实际搭机用户的反馈 [S03]。
- iCKB 合约审计发现未运行代码：phroi 表示这次追踪链上代码哪些部分从未运行，结果发现每个合约约三分之一代码从未运行 [S07]。
- 官网与生态更新：官网更新讨论中，发帖人感谢整理并称 Nervos 网站很多内容过时，列表与团队正在处理的内容接近 [S08]；CKB 生态双周报 #28 汇总了基础设施与工具等进展，包括将 c-kzg-4844 移植到 CKB-VM [S09]。

## 值得继续跟进

- zk-Lock 前端已可用，后续可观察真实使用情况，以及 zk-lock-bound 对 proof-copy 防护的实际效果和安全边界 [S01, S02]。
- CrowdCell M1 已上线测试网，后续可跟进 CellGuard × CrowdCell 试点中的 pledge profile 评审与集成进展 [S05, S06]。
- iCKB 审计发现约三分之一合约代码从未运行，后续值得关注这些未覆盖路径是否会补测试、补审计或调整上线策略 [S07]。

## 来源索引

- `S01` [Spark Program | zk-Lock for CKB](https://talk.nervos.org/t/spark-program-zk-lock-for-ckb/10448/26) | Mulandi_Cecilia | 2026-11-11 23:28:33 CST | Hi @xingtianchunyan and the committee, Thank you for your patience. The interactive frontend asked for in post #22 is live: https://zk-lock.vercel.app/ It takes about a minute, with no wallet and nothing to install. You type a secret word, your browser produces the proof, and...
- `S02` [Spark Program | zk-Lock for CKB](https://talk.nervos.org/t/spark-program-zk-lock-for-ckb/10448/27) | psawyerberlin | 2026-11-12 03:37:56 CST | Hi Cecilia, Congratulations on delivering zk-Lock! Going from a Groth16 verifier on CKB-VM to a reusable primitive with an SDK, a CLI, a reproducible circuit and a tutorial in a few weeks is impressive. And zk-lock-bound is a great answer to the mempool proof-copy problem....
- `S03` [Ckbup: one installer for CKB command-line tools (early progress, feedback welcome)](https://talk.nervos.org/t/ckbup-one-installer-for-ckb-command-line-tools-early-progress-feedback-welcome/11188/1) | Steven_Hert | 2026-11-12 03:01:14 CST | I’ve started building ckbup, a small open-source installer and version manager for CKB’s command-line tools, in the spirit of rustup. It’s free and I’m not asking for anything; I’m sharing it early to get feedback from people who actually set up CKB machines. Why Getting the...
- `S04` [[DIS] FiberNuts: Reliable Cashu-over-Fiber Payments with Hosted-LSP Onboarding](https://talk.nervos.org/t/dis-fibernuts-reliable-cashu-over-fiber-payments-with-hosted-lsp-onboarding/11051/7) | Code3ks | 2026-11-12 01:21:39 CST | Gm @zz_tovarishch please can you update the metaforo success in this thread?. Thank you.
- `S05` [[DIS] CrowdCell: From Testnet Demo to a Crowdfunding Product on CKB | CrowdCell：把 CKB 测试网上的免信任众筹做成产品](https://talk.nervos.org/t/dis-crowdcell-from-testnet-demo-to-a-crowdfunding-product-on-ckb-crowdcell-ckb/10937/13) | Ayoub_Lesfer | 2026-11-12 01:19:24 CST | [Status Update] M1: dashboards and discovery are live M1 is done and live on testnet at crowdcell.vercel.app. What shipped: Wallet-aware indexer endpoints, so the app knows which campaigns and pledges belong to the connected wallet. “My campaigns”...
- `S06` [Spark Program | CellGuard × CrowdCell — Real Transaction Policy Integration Pilot](https://talk.nervos.org/t/spark-program-cellguard-x-crowdcell-real-transaction-policy-integration-pilot/11161/2) | Ayoub_Lesfer | 2026-11-12 01:18:49 CST | Hey Dang, nice to see this, and happy to review the pledge profile once you’ve pinned it. A few things that should save you time. The live deployment is the one in deployment/deployed-contracts-testnet.json (redeployed Oct 31), that’s what crowdcell.vercel.app runs. The...
- `S07` [iCKB Contracts Revisited: Old Code, New Audit](https://talk.nervos.org/t/ickb-contracts-revisited-old-code-new-audit/10225/5) | phroi | 2026-11-11 23:57:39 CST | Last time I asked if the contracts accept something they shouldn’t. This time I asked what all those tests never even touched: which parts of the code on chain had never run? So I traced it, instruction by instruction. About a third of each contract had never run. Most of that...
- `S08` [Web page www.nervos.org - Discussion for new pull request](https://talk.nervos.org/t/web-page-www-nervos-org-discussion-for-new-pull-request/11133/8) | excitedsashimi | 2026-11-11 13:22:24 CST | Hi @psawyerberlin, thank you for pulling this together and thanks to @Thinker and @silenceport for the discussion. Really appreciate everyone taking the time to contribute. A lot of Nervos site is out of date and your list lines up closely with what we’ve been working through....
- `S09` [CKB Ecosystem Biweekly Update](https://talk.nervos.org/t/ckb-ecosystem-biweekly-update/9821/34) | zz_tovarishch | 2026-11-11 09:35:24 CST | image690×388 97.6 KB CKB Ecosystem Biweekly Update #28 Welcome to the latest CKB Ecosystem Biweekly Update. Here’s a quick summary of key dev and ecosystem progress from the past two weeks. Infrastructure & Tooling @CKBdev ported c-kzg-4844 to CKB-VM. Other works include...

## 活跃话题

1. [Spark Program | zk-Lock for CKB](https://talk.nervos.org/t/spark-program-zk-lock-for-ckb/10448) | 2 条近窗帖子 | 最新活动 2026-11-12 03:37:56 CST | tags: In-Progress
2. [Ckbup: one installer for CKB command-line tools (early progress, feedback welcome)](https://talk.nervos.org/t/ckbup-one-installer-for-ckb-command-line-tools-early-progress-feedback-welcome/11188) | 1 条近窗帖子 | 最新活动 2026-11-12 03:01:14 CST | tags: CKB, Infrastructure, dev-tool, fiber, rust
3. [[DIS] FiberNuts: Reliable Cashu-over-Fiber Payments with Hosted-LSP Onboarding](https://talk.nervos.org/t/dis-fibernuts-reliable-cashu-over-fiber-payments-with-hosted-lsp-onboarding/11051) | 1 条近窗帖子 | 最新活动 2026-11-12 01:21:39 CST
4. [[DIS] CrowdCell: From Testnet Demo to a Crowdfunding Product on CKB | CrowdCell：把 CKB 测试网上的免信任众筹做成产品](https://talk.nervos.org/t/dis-crowdcell-from-testnet-demo-to-a-crowdfunding-product-on-ckb-crowdcell-ckb/10937) | 1 条近窗帖子 | 最新活动 2026-11-12 01:19:24 CST | tags: lang-en
5. [Spark Program | CellGuard × CrowdCell — Real Transaction Policy Integration Pilot](https://talk.nervos.org/t/spark-program-cellguard-x-crowdcell-real-transaction-policy-integration-pilot/11161) | 1 条近窗帖子 | 最新活动 2026-11-12 01:18:49 CST
6. [iCKB Contracts Revisited: Old Code, New Audit](https://talk.nervos.org/t/ickb-contracts-revisited-old-code-new-audit/10225) | 1 条近窗帖子 | 最新活动 2026-11-11 23:57:39 CST | tags: lang-en
7. [Web page www.nervos.org - Discussion for new pull request](https://talk.nervos.org/t/web-page-www-nervos-org-discussion-for-new-pull-request/11133) | 1 条近窗帖子 | 最新活动 2026-11-11 13:22:24 CST
8. [CKB Ecosystem Biweekly Update](https://talk.nervos.org/t/ckb-ecosystem-biweekly-update/9821) | 1 条近窗帖子 | 最新活动 2026-11-11 09:35:24 CST | tags: Ecosystem-Update, lang-en

## 最近帖子摘录

- 2026-11-12 03:37:56 CST | psawyerberlin | [Spark Program | zk-Lock for CKB](https://talk.nervos.org/t/spark-program-zk-lock-for-ckb/10448/27) | Hi Cecilia, Congratulations on delivering zk-Lock! Going from a Groth16 verifier on CKB-VM to a reusable primitive with an SDK, a CLI, a reproducible circuit and a tutorial in a...
- 2026-11-12 03:01:14 CST | Steven_Hert | [Ckbup: one installer for CKB command-line tools (early progress, feedback welcome)](https://talk.nervos.org/t/ckbup-one-installer-for-ckb-command-line-tools-early-progress-feedback-welcome/11188/1) | I’ve started building ckbup, a small open-source installer and version manager for CKB’s command-line tools, in the spirit of rustup. It’s free and I’m not asking for anything;...
- 2026-11-12 01:21:39 CST | Code3ks | [[DIS] FiberNuts: Reliable Cashu-over-Fiber Payments with Hosted-LSP Onboarding](https://talk.nervos.org/t/dis-fibernuts-reliable-cashu-over-fiber-payments-with-hosted-lsp-onboarding/11051/7) | Gm @zz_tovarishch please can you update the metaforo success in this thread?. Thank you.
- 2026-11-12 01:19:24 CST | Ayoub_Lesfer | [[DIS] CrowdCell: From Testnet Demo to a Crowdfunding Product on CKB | CrowdCell：把 CKB 测试网上的免信任众筹做成产品](https://talk.nervos.org/t/dis-crowdcell-from-testnet-demo-to-a-crowdfunding-product-on-ckb-crowdcell-ckb/10937/13) | [Status Update] M1: dashboards and discovery are live M1 is done and live on testnet at crowdcell.vercel.app. What shipped: Wallet-aware indexer endpoints, so the app knows...
- 2026-11-12 01:18:49 CST | Ayoub_Lesfer | [Spark Program | CellGuard × CrowdCell — Real Transaction Policy Integration Pilot](https://talk.nervos.org/t/spark-program-cellguard-x-crowdcell-real-transaction-policy-integration-pilot/11161/2) | Hey Dang, nice to see this, and happy to review the pledge profile once you’ve pinned it. A few things that should save you time. The live deployment is the one in...
- 2026-11-11 23:57:39 CST | phroi | [iCKB Contracts Revisited: Old Code, New Audit](https://talk.nervos.org/t/ickb-contracts-revisited-old-code-new-audit/10225/5) | Last time I asked if the contracts accept something they shouldn’t. This time I asked what all those tests never even touched: which parts of the code on chain had never run? So...
- 2026-11-11 23:28:33 CST | Mulandi_Cecilia | [Spark Program | zk-Lock for CKB](https://talk.nervos.org/t/spark-program-zk-lock-for-ckb/10448/26) | Hi @xingtianchunyan and the committee, Thank you for your patience. The interactive frontend asked for in post #22 is live: https://zk-lock.vercel.app/ It takes about a minute,...
- 2026-11-11 13:22:24 CST | excitedsashimi | [Web page www.nervos.org - Discussion for new pull request](https://talk.nervos.org/t/web-page-www-nervos-org-discussion-for-new-pull-request/11133/8) | Hi @psawyerberlin, thank you for pulling this together and thanks to @Thinker and @silenceport for the discussion. Really appreciate everyone taking the time to contribute. A...
- 2026-11-11 09:35:24 CST | zz_tovarishch | [CKB Ecosystem Biweekly Update](https://talk.nervos.org/t/ckb-ecosystem-biweekly-update/9821/34) | image690×388 97.6 KB CKB Ecosystem Biweekly Update #28 Welcome to the latest CKB Ecosystem Biweekly Update. Here’s a quick summary of key dev and ecosystem progress from the...
