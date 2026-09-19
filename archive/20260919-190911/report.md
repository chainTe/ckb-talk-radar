# Nervos Talk 社区简报

- 统计窗口: 2026-09-19 03:09:11 CST 到 2026-09-20 03:09:11 CST
- 生成时间: 2026-09-20 03:09:18 CST
- 话题数: 7
- 帖子数: 8
- 作者数: 8
- 总结模式: ai:openai-compatible

## 社区总结

## 今日发生了什么

从这批帖子看，论坛今天的更新集中在 9 月 19 日，内容以 Spark Program 项目动态和 CKB/Fiber 技术讨论为主 [S01, S03, S04, S05, S06, S07, S08]。新项目方面，RIVET 和 Proof-of-Inquiry Gateway for CKB 分别在论坛亮相 [S01, S06]。Spark Program 相关帖子较活跃，Fiber Weir、NNCBN 和 CKB Builder Lab 都有新进展或回应 [S03, S04, S05]。技术侧，Proof of Buy 继续讨论 L1 对 L2 的审查攻击，Fiber 自动流动性再平衡 RFC 也在等待 Fiber 团队回应 [S07, S08]。

## 重点话题

- RIVET 新帖由 Jedi_dtechmaker 发布，介绍用 CKB、IPFS、RGB++ 备份、时间戳和恢复完整 GitHub 历史 [S01]；帖下有一条“very impressive”的回复 [S02]。Proof-of-Inquiry Gateway for CKB 也作为新帖出现，作者为 Axel_Domingo_Padilla，团队是 RadhikaChain / RadhikaChain Research [S06]；项目定位为独立开源工程，关注可验证 agent 基础设施、区块链互操作性、隐私保护证据和机器对机器服务 [S06]。

- Fiber Weir 以 Spark Program 项目帖形式出现，项目名是 Fiber Weir，一句话总结为实现 Fiber Network 路线图中的“programmable conditional payment”，也就是条件门控支付流 [S03]。

- NNCBN 话题下有更新，发帖人称可以在论坛发布第一份简报，计划在 9 月 29 日发布，并以后每周二发布 [S04]。硬件采购过程比原先预期更长，且正在把硬件采购与出国行程合并处理 [S04]。

- CKB Builder Lab 话题下，devnash 回应了最终评估和建议 [S05]；其表示理解主要差距不是 CKB Builder Lab 的技术实现，而是缺少结构化、量化证据来证明教育效果 [S05]。

- Proof of Buy 讨论继续，提出一种来自 L1 的审查攻击及防御手段 [S07]；具体场景是 L1 出块矿工若同时参与 L2 挖矿，可以拒绝接收 goal 更高的 L2 block，只打包自己在 L2 出的块 [S07]。Fiber 自动通道流动性再平衡 RFC 中，ILE_LABS 请 @quake 和 Fiber 团队查看上面的问题，并告知 Fiber 侧如何推进 [S08]；其还提出需要先确定该缺口是否与当前开发相关、已被覆盖或不是优先事项，再决定是否进一步投入 [S08]。

## 值得继续跟进

- RIVET 和 Proof-of-Inquiry Gateway for CKB 目前都只有介绍性内容或早期反馈 [S01, S02, S06]；后续可观察是否发布原型、技术细节或更多社区讨论 [S01, S02, S06]。

- Spark Program 项目推进值得看：Fiber Weir 是否能从提案继续落地 [S03]；CKB Builder Lab 如何补足教育效果的量化证据 [S05]；NNCBN 的 9 月 29 日首份简报以及硬件采购延迟是否影响启动节点计划 [S04]。

- 技术风险方面，Proof of Buy 中 L1 矿工审查 L2 block 的攻击场景是否有后续防御方案值得观察 [S07]；Fiber 团队是否会回应自动通道流动性再平衡的问题，也将决定该方向是否继续投入 [S08]。

## 来源索引

- `S01` [RIVET: CKB-native GitHub backup using IPFS, RGB++, and CCC](https://talk.nervos.org/t/rivet-ckb-native-github-backup-using-ipfs-rgb-and-ccc/10722/1) | Jedi_dtechmaker | 2026-09-19 17:16:47 CST | Hello everyone, I am building RIVET, a decentralized developer platform that backs up, timestamps, and restores your entire GitHub history using CKB, IPFS, and RGB++. Developers currently build their entire careers and reputations on platforms they do not actually control....
- `S02` [RIVET: CKB-native GitHub backup using IPFS, RGB++, and CCC](https://talk.nervos.org/t/rivet-ckb-native-github-backup-using-ipfs-rgb-and-ccc/10722/2) | Dangbaty2004 | 2026-09-19 23:58:48 CST | very impressive !
- `S03` [Spark Program | Fiber Weir — Condition-Gated Payment Streams for Fiber Network](https://talk.nervos.org/t/spark-program-fiber-weir-condition-gated-payment-streams-for-fiber-network/10723/1) | Carl | 2026-09-19 19:35:12 CST | Spark Program | Fiber Weir — Condition-Gated Payment Streams for Fiber Network 1. Project Overview Project name: Fiber Weir One-sentence summary: A working implementation of a piece of Fiber Network’s own named roadmap item — “programmable conditional payment” — letting a...
- `S04` [Spark Program | NNCBN - Nervos Network Community Boot Nodes](https://talk.nervos.org/t/spark-program-nncbn-nervos-network-community-boot-nodes/10653/10) | NNCBN | 2026-09-19 18:50:00 CST | NNCBN: I can post the first brief report here on the forum—which will be posted every Tuesday—on September 29 The procurement process is taking longer than originally expected. I’m combining the hardware procurement with a trip abroad, since local suppliers don’t offer the...
- `S05` [Spark Program | CKB Builder Lab: Interactive Developer Onboarding Infrastructure for the CKB Ecosystem](https://talk.nervos.org/t/spark-program-ckb-builder-lab-interactive-developer-onboarding-infrastructure-for-the-ckb-ecosystem/10385/32) | devnash | 2026-09-19 18:19:23 CST | Thank you for the detailed final evaluation and recommendations. I understand that the main gap identified is not the technical implementation of CKB Builder Lab, but the lack of structured and quantitative evidence demonstrating its educational effectiveness. I agree with the...
- `S06` [Proof-of-Inquiry Gateway for CKB](https://talk.nervos.org/t/proof-of-inquiry-gateway-for-ckb/10720/1) | Axel_Domingo_Padilla | 2026-09-19 16:17:12 CST | Proof-of-Inquiry Gateway for CKB Developer / Team RadhikaChain / RadhikaChain Research Independent open-source engineering project focused on verifiable agent infrastructure, blockchain interoperability, privacy-preserving evidence, and machine-to-machine services. Project...
- `S07` [Proof of Buy，一种专为Layer1设计的Layer2共识](https://talk.nervos.org/t/proof-of-buy-layer1-layer2/9752/33) | Lawliet_Chan | 2026-09-19 16:11:20 CST | 一种来自L1的审查攻击 及 防御手段 前文提到，在proof of buy中，我们在finalize L2 block的时候，会将这些L2 block header上传到L1上去。 但这迎来一个问题， 不管L1有多去中心化， 但具体在某个高度出块的时候， 一般而言总是只有一个矿池出的块最终被采纳的。 在这种情况下， 此刻出块的L1矿工，就具备对L2 block审查的权力， 具体而言，他自己可能就是既是L1的矿工也参与L2的挖矿，此时恰逢他自己在L1出块，他可以选择拒绝接收 那些goal比他还高的L2 block， 只打包他自己在L2出的块。...
- `S08` [[RFC & Research] Automated Channel Liquidity Rebalancing on Fiber Network](https://talk.nervos.org/t/rfc-research-automated-channel-liquidity-rebalancing-on-fiber-network/10691/5) | ILE_LABS | 2026-09-19 15:28:06 CST | Understood. @quake and the Fiber team, please take a look at the questions above and let us know how we should proceed from the Fiber side. We need to determine whether this gap is relevant to current development, already covered, or not a priority before investing further in...

## 活跃话题

1. [RIVET: CKB-native GitHub backup using IPFS, RGB++, and CCC](https://talk.nervos.org/t/rivet-ckb-native-github-backup-using-ipfs-rgb-and-ccc/10722) | 2 条近窗帖子 | 最新活动 2026-09-19 23:58:48 CST | tags: CKB, RGB, appchain, dapp, ipfs, lang-en
2. [Spark Program | Fiber Weir — Condition-Gated Payment Streams for Fiber Network](https://talk.nervos.org/t/spark-program-fiber-weir-condition-gated-payment-streams-for-fiber-network/10723) | 1 条近窗帖子 | 最新活动 2026-09-19 19:35:12 CST | tags: Spark-Program
3. [Spark Program | NNCBN - Nervos Network Community Boot Nodes](https://talk.nervos.org/t/spark-program-nncbn-nervos-network-community-boot-nodes/10653) | 1 条近窗帖子 | 最新活动 2026-09-19 18:50:00 CST | tags: In-Progress, Node, Spark-Program, bootnode
4. [Spark Program | CKB Builder Lab: Interactive Developer Onboarding Infrastructure for the CKB Ecosystem](https://talk.nervos.org/t/spark-program-ckb-builder-lab-interactive-developer-onboarding-infrastructure-for-the-ckb-ecosystem/10385) | 1 条近窗帖子 | 最新活动 2026-09-19 18:19:23 CST | tags: In-Progress
5. [Proof-of-Inquiry Gateway for CKB](https://talk.nervos.org/t/proof-of-inquiry-gateway-for-ckb/10720) | 1 条近窗帖子 | 最新活动 2026-09-19 16:17:12 CST
6. [Proof of Buy，一种专为Layer1设计的Layer2共识](https://talk.nervos.org/t/proof-of-buy-layer1-layer2/9752) | 1 条近窗帖子 | 最新活动 2026-09-19 16:11:20 CST | tags: lang-zh, 共识协议
7. [[RFC & Research] Automated Channel Liquidity Rebalancing on Fiber Network](https://talk.nervos.org/t/rfc-research-automated-channel-liquidity-rebalancing-on-fiber-network/10691) | 1 条近窗帖子 | 最新活动 2026-09-19 15:28:06 CST

## 最近帖子摘录

- 2026-09-19 23:58:48 CST | Dangbaty2004 | [RIVET: CKB-native GitHub backup using IPFS, RGB++, and CCC](https://talk.nervos.org/t/rivet-ckb-native-github-backup-using-ipfs-rgb-and-ccc/10722/2) | very impressive !
- 2026-09-19 19:35:12 CST | Carl | [Spark Program | Fiber Weir — Condition-Gated Payment Streams for Fiber Network](https://talk.nervos.org/t/spark-program-fiber-weir-condition-gated-payment-streams-for-fiber-network/10723/1) | Spark Program | Fiber Weir — Condition-Gated Payment Streams for Fiber Network 1. Project Overview Project name: Fiber Weir One-sentence summary: A working implementation of a...
- 2026-09-19 18:50:00 CST | NNCBN | [Spark Program | NNCBN - Nervos Network Community Boot Nodes](https://talk.nervos.org/t/spark-program-nncbn-nervos-network-community-boot-nodes/10653/10) | NNCBN: I can post the first brief report here on the forum—which will be posted every Tuesday—on September 29 The procurement process is taking longer than originally expected....
- 2026-09-19 18:19:23 CST | devnash | [Spark Program | CKB Builder Lab: Interactive Developer Onboarding Infrastructure for the CKB Ecosystem](https://talk.nervos.org/t/spark-program-ckb-builder-lab-interactive-developer-onboarding-infrastructure-for-the-ckb-ecosystem/10385/32) | Thank you for the detailed final evaluation and recommendations. I understand that the main gap identified is not the technical implementation of CKB Builder Lab, but the lack...
- 2026-09-19 17:16:47 CST | Jedi_dtechmaker | [RIVET: CKB-native GitHub backup using IPFS, RGB++, and CCC](https://talk.nervos.org/t/rivet-ckb-native-github-backup-using-ipfs-rgb-and-ccc/10722/1) | Hello everyone, I am building RIVET, a decentralized developer platform that backs up, timestamps, and restores your entire GitHub history using CKB, IPFS, and RGB++. Developers...
- 2026-09-19 16:17:12 CST | Axel_Domingo_Padilla | [Proof-of-Inquiry Gateway for CKB](https://talk.nervos.org/t/proof-of-inquiry-gateway-for-ckb/10720/1) | Proof-of-Inquiry Gateway for CKB Developer / Team RadhikaChain / RadhikaChain Research Independent open-source engineering project focused on verifiable agent infrastructure,...
- 2026-09-19 16:11:20 CST | Lawliet_Chan | [Proof of Buy，一种专为Layer1设计的Layer2共识](https://talk.nervos.org/t/proof-of-buy-layer1-layer2/9752/33) | 一种来自L1的审查攻击 及 防御手段 前文提到，在proof of buy中，我们在finalize L2 block的时候，会将这些L2 block header上传到L1上去。 但这迎来一个问题， 不管L1有多去中心化， 但具体在某个高度出块的时候， 一般而言总是只有一个矿池出的块最终被采纳的。 在这种情况下， 此刻出块的L1矿工，就具备对L2...
- 2026-09-19 15:28:06 CST | ILE_LABS | [[RFC & Research] Automated Channel Liquidity Rebalancing on Fiber Network](https://talk.nervos.org/t/rfc-research-automated-channel-liquidity-rebalancing-on-fiber-network/10691/5) | Understood. @quake and the Fiber team, please take a look at the questions above and let us know how we should proceed from the Fiber side. We need to determine whether this gap...
