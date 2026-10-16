# Nervos Talk 社区简报

- 统计窗口: 2026-10-16 03:48:13 CST 到 2026-10-17 03:48:13 CST
- 生成时间: 2026-10-17 03:48:18 CST
- 话题数: 6
- 帖子数: 8
- 作者数: 7
- 总结模式: ai:openai-compatible

## 社区总结

## 今日发生了什么

今天 Nervos Talk 的主要活动是多个 CKB 生态项目更新：Corven 发布第 1 周进展报告 [S02]，QuotaCell 与 CellRoute / FiberPay 分别发出新帖 [S03, S04]。测试与讨论方面，CrowdCell 在推进 keeper 拆分计划 [S05]，RIVET 围绕 GitHub 备份的删除场景和恢复模式继续技术讨论 [S06, S07]。POI 游戏也有合作任务说明 [S01]。整体看，今天不是单一热点爆发，而是开发工具、众筹测试、备份工具和游戏帖子分散更新 [S01, S02, S03, S04, S05, S06, S07, S08]。

## 重点话题

- **Corven 第 1 周进展**：Corven 在 Spark Program 下发布 Week 1 进展报告，报告期为 2026 年 10 月 12–16 日 [S02]。项目定位是为 CKB 和 Fiber Network 构建的浏览器 IDE，并给出项目网站和 GitHub [S02]。
- **QuotaCell 与 CellRoute / FiberPay 新帖**：QuotaCell 提出让团队无需交出 treasury 也能支出的方案，开场以小型团队需要付款但无法逐笔审批、又不想开放全部 treasury 权限为场景 [S03]。CellRoute / FiberPay 则介绍一个把 CKB 开发实验室和支付实验整合到同一门户的应用，作者分享当前进展并邀请开发者反馈 [S04]。
- **CrowdCell 测试推进**：作者回应测试称，让用户从自己的节点运行第二个 keeper 正是测试需要的“不由项目方控制”的运营者 [S05]。目前 keeper 运行在 indexer 内，计划在 tip 落地前拆分出来并补一个简短 readme [S05]。
- **RIVET 技术讨论**：评论者认可 RIVET 测试网 demo 与恢复路径，认为把恢复拆成 Exact 和 Attribution 模式是正确的，并提出 GitHub 删除仓库时锚定是关键问题 [S06]。作者回应称当前用 Merkle tree 记录所有 commit hashes，但同意 refs 和 tip commits 需要补充，并会加入排序后的 refs 哈希和 bundle 本身的 SHA-256 [S07]。另有回复表达对 VeriCell 产品概念的喜欢 [S08]。
- **POI 合作任务**：POI 作者说明该任务为 co-op mission，不能单人完成，需要与另一名玩家组队 [S01]。

## 值得继续跟进

- Corven 第 1 周报告目前只称活动正在进行中，后续是否披露具体完成项和里程碑值得观察 [S02]。QuotaCell 与 CellRoute / FiberPay 刚发帖，社区反馈和机制细节也尚待展开 [S03, S04]。
- CrowdCell 计划把 keeper 从 indexer 拆出并补 readme，能否在 tip 落地前完成、外部运营者测试如何进行，值得继续跟进 [S05]。
- RIVET 对删除仓库场景的锚定改进，包括 sorted refs hash 和 bundle SHA-256，以及 Exact / Attribution 恢复模式的实际效果，需要后续观察 [S06, S07]。

## 来源索引

- `S01` [POI: Proof of Identity, a platformer on CKB testnet that teaches .cell names by using them](https://talk.nervos.org/t/poi-proof-of-identity-a-platformer-on-ckb-testnet-that-teaches-cell-names-by-using-them/10967/5) | LusoCryptoLabs | 2026-10-17 02:58:32 CST | This is a co-op mission, so it can’t be completed solo. You’ll need to team up with another player in the game to finish it. Looks like you’re really liking the game, that’s great, thanks for participating
- `S02` [Spark Program Proposal: Corven cloud-native IDE](https://talk.nervos.org/t/spark-program-proposal-corven-cloud-native-ide/10807/4) | lestonEth | 2026-10-17 02:10:26 CST | Corven Spark Program — Week 1 Progress Report Project: Corven: A Browser-Based IDE for Building on CKB and Fiber Network Reporting Period: 12–16 October 2026 Status: Week 1 activities underway Project Website: https://corvanide.space/ GitHub: GitHub - corvenide/corven-fronted:...
- `S03` [QuotaCell: Let your team spend without handing over the treasury](https://talk.nervos.org/t/quotacell-let-your-team-spend-without-handing-over-the-treasury/11002/1) | Ticoworld | 2026-10-17 00:07:20 CST | Imagine you’re running a project with a small team. There are expenses to handle, suppliers to pay, and people who need to get things done. You can’t be available to approve every single payment. But you also don’t want to give everyone unrestricted access to the treasury. So...
- `S04` [CellRoute / FiberPay — CKB development tools with live asset inspection](https://talk.nervos.org/t/cellroute-fiberpay-ckb-development-tools-with-live-asset-inspection/11000/1) | Dat_Nguyen_Tu | 2026-10-16 23:46:12 CST | Hi Nervos community, I am building CellRoute / FiberPay, a CKB application that brings development labs and payment experiments into one portal. I would like to share the current progress and get feedback from developers in the ecosystem. Live app:...
- `S05` [[DIS] CrowdCell: From Testnet Demo to a Crowdfunding Product on CKB | CrowdCell：把 CKB 测试网上的免信任众筹做成产品](https://talk.nervos.org/t/dis-crowdcell-from-testnet-demo-to-a-crowdfunding-product-on-ckb-crowdcell-ckb/10937/6) | Ayoub_Lesfer | 2026-10-16 23:34:01 CST | Thanks for testing it and for reposting here. Having you run the second keeper from your own node is exactly what that test needs, an operator I don’t control. Right now the keeper runs inside the indexer, so I’ll split it out with a short readme before the tip lands so it’s...
- `S06` [[DIS] RIVET: Decentralized GitHub Backup, Timestamping and Restore on CKB](https://talk.nervos.org/t/dis-rivet-decentralized-github-backup-timestamping-and-restore-on-ckb/10739/10) | psawyerberlin | 2026-10-16 04:09:18 CST | Nice work getting a working demo on testnet. Backup with a restore path is a real gap, and splitting restore into Exact and Attribution modes is the right call. Two technical points: 1. Anchoring for the deletion case. If GitHub deletes the repo, the anchor is the only...
- `S07` [[DIS] RIVET: Decentralized GitHub Backup, Timestamping and Restore on CKB](https://talk.nervos.org/t/dis-rivet-decentralized-github-backup-timestamping-and-restore-on-ckb/10739/11) | Jedi_dtechmaker | 2026-10-16 06:45:03 CST | Thanks for the feedback and the vote! To answer your questions. Anchoring & deletion case: Great point. Right now we Merkle-tree all commit hashes (git log --all), but you’re spot on about refs and tip commits. Adding the sorted refs hash + a SHA-256 of the bundle itself makes...
- `S08` [[DIS] RIVET: Decentralized GitHub Backup, Timestamping and Restore on CKB](https://talk.nervos.org/t/dis-rivet-decentralized-github-backup-timestamping-and-restore-on-ckb/10739/12) | Jedi_dtechmaker | 2026-10-16 06:49:36 CST | And i really love the idea and concept behind your product VeriCell.

## 活跃话题

1. [POI: Proof of Identity, a platformer on CKB testnet that teaches .cell names by using them](https://talk.nervos.org/t/poi-proof-of-identity-a-platformer-on-ckb-testnet-that-teaches-cell-names-by-using-them/10967) | 1 条近窗帖子 | 最新活动 2026-10-17 02:58:32 CST
2. [Spark Program Proposal: Corven cloud-native IDE](https://talk.nervos.org/t/spark-program-proposal-corven-cloud-native-ide/10807) | 1 条近窗帖子 | 最新活动 2026-10-17 02:10:26 CST | tags: CKB, Grant, Pending, Spark-Program
3. [QuotaCell: Let your team spend without handing over the treasury](https://talk.nervos.org/t/quotacell-let-your-team-spend-without-handing-over-the-treasury/11002) | 1 条近窗帖子 | 最新活动 2026-10-17 00:07:20 CST | tags: CKB, CKB-VM, lang-en
4. [CellRoute / FiberPay — CKB development tools with live asset inspection](https://talk.nervos.org/t/cellroute-fiberpay-ckb-development-tools-with-live-asset-inspection/11000) | 1 条近窗帖子 | 最新活动 2026-10-16 23:46:12 CST
5. [[DIS] CrowdCell: From Testnet Demo to a Crowdfunding Product on CKB | CrowdCell：把 CKB 测试网上的免信任众筹做成产品](https://talk.nervos.org/t/dis-crowdcell-from-testnet-demo-to-a-crowdfunding-product-on-ckb-crowdcell-ckb/10937) | 1 条近窗帖子 | 最新活动 2026-10-16 23:34:01 CST | tags: lang-en
6. [[DIS] RIVET: Decentralized GitHub Backup, Timestamping and Restore on CKB](https://talk.nervos.org/t/dis-rivet-decentralized-github-backup-timestamping-and-restore-on-ckb/10739) | 3 条近窗帖子 | 最新活动 2026-10-16 06:49:36 CST | tags: CKB

## 最近帖子摘录

- 2026-10-17 02:58:32 CST | LusoCryptoLabs | [POI: Proof of Identity, a platformer on CKB testnet that teaches .cell names by using them](https://talk.nervos.org/t/poi-proof-of-identity-a-platformer-on-ckb-testnet-that-teaches-cell-names-by-using-them/10967/5) | This is a co-op mission, so it can’t be completed solo. You’ll need to team up with another player in the game to finish it. Looks like you’re really liking the game, that’s...
- 2026-10-17 02:10:26 CST | lestonEth | [Spark Program Proposal: Corven cloud-native IDE](https://talk.nervos.org/t/spark-program-proposal-corven-cloud-native-ide/10807/4) | Corven Spark Program — Week 1 Progress Report Project: Corven: A Browser-Based IDE for Building on CKB and Fiber Network Reporting Period: 12–16 October 2026 Status: Week 1...
- 2026-10-17 00:07:20 CST | Ticoworld | [QuotaCell: Let your team spend without handing over the treasury](https://talk.nervos.org/t/quotacell-let-your-team-spend-without-handing-over-the-treasury/11002/1) | Imagine you’re running a project with a small team. There are expenses to handle, suppliers to pay, and people who need to get things done. You can’t be available to approve...
- 2026-10-16 23:46:12 CST | Dat_Nguyen_Tu | [CellRoute / FiberPay — CKB development tools with live asset inspection](https://talk.nervos.org/t/cellroute-fiberpay-ckb-development-tools-with-live-asset-inspection/11000/1) | Hi Nervos community, I am building CellRoute / FiberPay, a CKB application that brings development labs and payment experiments into one portal. I would like to share the...
- 2026-10-16 23:34:01 CST | Ayoub_Lesfer | [[DIS] CrowdCell: From Testnet Demo to a Crowdfunding Product on CKB | CrowdCell：把 CKB 测试网上的免信任众筹做成产品](https://talk.nervos.org/t/dis-crowdcell-from-testnet-demo-to-a-crowdfunding-product-on-ckb-crowdcell-ckb/10937/6) | Thanks for testing it and for reposting here. Having you run the second keeper from your own node is exactly what that test needs, an operator I don’t control. Right now the...
- 2026-10-16 06:49:36 CST | Jedi_dtechmaker | [[DIS] RIVET: Decentralized GitHub Backup, Timestamping and Restore on CKB](https://talk.nervos.org/t/dis-rivet-decentralized-github-backup-timestamping-and-restore-on-ckb/10739/12) | And i really love the idea and concept behind your product VeriCell.
- 2026-10-16 06:45:03 CST | Jedi_dtechmaker | [[DIS] RIVET: Decentralized GitHub Backup, Timestamping and Restore on CKB](https://talk.nervos.org/t/dis-rivet-decentralized-github-backup-timestamping-and-restore-on-ckb/10739/11) | Thanks for the feedback and the vote! To answer your questions. Anchoring & deletion case: Great point. Right now we Merkle-tree all commit hashes (git log --all), but you’re...
- 2026-10-16 04:09:18 CST | psawyerberlin | [[DIS] RIVET: Decentralized GitHub Backup, Timestamping and Restore on CKB](https://talk.nervos.org/t/dis-rivet-decentralized-github-backup-timestamping-and-restore-on-ckb/10739/10) | Nice work getting a working demo on testnet. Backup with a restore path is a real gap, and splitting restore into Exact and Attribution modes is the right call. Two technical...
