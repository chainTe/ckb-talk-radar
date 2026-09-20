# Nervos Talk 社区简报

- 统计窗口: 2026-09-20 03:15:32 CST 到 2026-09-21 03:15:32 CST
- 生成时间: 2026-09-21 03:15:37 CST
- 话题数: 7
- 帖子数: 7
- 作者数: 7
- 总结模式: ai:openai-compatible

## 社区总结

## 今日发生了什么

今天论坛的主要事情是几个 CKB 新应用和工具进展集中出现：Khie 钱包连接协议发布 [S02]，CKB Fly 把果蝇头方向回路搬上 CKB [S04]，Pocket Node for iOS 报告 Milestone 1 完成 [S03]。同时，Spark CRT 作者回应审查意见并编辑原帖 [S01]，Fiber 流动性再平衡研究收到核心团队反馈 [S06]。社区还出现了重启 utxo stack 的询问，以及 RIVET 后续讨论 [S05, S07]。整体看，今天社区不算平静，新项目展示和项目反馈都有动静 [S01, S02, S03, S04, S05, S06, S07]。

## 重点话题

- **Khie 钱包连接协议发布**：Khie 基于 libp2p，是构建在端到端通道上的钱包连接协议 [S02]。作者说它像 CCC 一样，打开、连接钱包，然后忘掉它 [S02]。作者认为 CKB 适合孵化新钱包形态，包括邮箱 DKIM、抗量子、手机到桌面等方向 [S02]。
- **CKB Fly 把果蝇神经回路放上 CKB**：项目把果蝇大脑中管头方向的环吸引子放到 CKB，包含 155 个神经元、6,522 条连接、45,961 个突触，连接组来自 FlyWire release 783 [S04]。整个神经系统是一个 cell，1,213 字节 [S04]。它是 MidTermDev/immortal-fruit-fly 的移植，要求逐位一致，并称已用主网真实轨迹在 CKB-VM 重放验证 [S04]。项目明确没有代币、没有服务器 [S04]。
- **Pocket Node for iOS 完成 Milestone 1**：帖子报告 iOS grant 的“Shared core, iOS bridge, app skeleton”已完成，并在 main 上标记为 ios-m1 [S03]。帖子列出交付内容、验证方式和下一步 [S03]。
- **Spark CRT 与 Fiber 流动性收到反馈**：Spark CRT 发帖人感谢 xingtian 和委员会认真阅读，称两点意见公平，并表示已相应编辑原帖 [S01]。他还提到重新阅读时，对第 2 点的一个回答被埋在底部 bullet 里 [S01]。Fiber 流动性再平衡研究方面，quake 感谢研究和原型，但表示额外路由提示和图循环查询目前不是核心团队高优先级 [S06]。当前工作提到 Loop，材料在这里截断 [S06]。
- **社区询问与后续讨论**：有用户发帖问如何才能重启，或者重新搞一个之前关闭的 utxo stack 项目 [S05]。RIVET 帖子下有人赞同，认为除 Git 外还有很多领域需要类似功能，并追问当前链上脚本是否满足需求，还是需要开发新的链上脚本 [S07]。

## 值得继续跟进

- Khie 作为钱包连接协议能否真正落地、被钱包或应用采用，是后续观察点；目前材料只看到发布介绍，没有采用情况 [S02]。
- Pocket Node for iOS 的下一步值得跟进，因为 M1 已完成，帖子本身也提到 what comes next [S03]。
- Spark CRT 原帖编辑后的委员会反馈、Fiber 流动性提案的优先级、utxo stack 是否有人回应重启、RIVET 是否要开发新链上脚本，都是尚未看到结论的方向 [S01, S05, S06, S07]。

## 来源索引

- `S01` [Spark Program | CKB Revocable Timelock (CRT) — Timelock Encryption You Can Cancel](https://talk.nervos.org/t/spark-program-ckb-revocable-timelock-crt-timelock-encryption-you-can-cancel/10698/3) | psawyerberlin | 2026-09-20 23:31:01 CST | Thanks xingtian, and thanks to the committee for reading it carefully. Both points are fair and I’d rather answer them bluntly than well. I’ve edited the original post accordingly. Re-reading it, one of my answers to point 2 was buried in a bullet at the bottom and another was...
- `S02` [Khie，「契」。](https://talk.nervos.org/t/khie/10726/1) | Hanssen | 2026-09-20 20:59:38 CST | 本文同时发表于我的个人博客。 khie.svg945×945 6.36 KB Khie /kʰje/，客家語，意为契。 准备钱包，打开应用，扫码，结契。Khie 基于 libp2p，是构建在端到端通道上的钱包连接协议。 我很难给 Khie 再下更复杂的定义，它就像 CCC 一样，你打开，连接钱包，然后忘掉它。虽然如此，Khie 想解决的问题却要棘手许多。 很难被人注意到的一点是，CKB 或许比任何区块链都更适合孵化新的钱包形态。邮箱 DKIM 或抗量子，手机到桌面，各式钱包在 CKB 上钻出。 并不只是因为自由的签名算法这种显而易见的原因，更因为...
- `S03` [[DIS] Pocket Node for iOS: a self-custody CKB light client for Apple and Identity/Signer for CCC web apps](https://talk.nervos.org/t/dis-pocket-node-for-ios-a-self-custody-ckb-light-client-for-apple-and-identity-signer-for-ccc-web-apps/10583/22) | Jnr6 | 2026-09-20 20:15:19 CST | Pocket Node for iOS: Milestone 1 completion report Milestone 1 of the iOS grant (“Shared core, iOS bridge, app skeleton”) is complete and tagged as ios-m1 on main. This post lists what shipped, how it was verified, and what comes next. Acceptance criteria, as written in the...
- `S04` [CKB Fly ｜一只活在CKB上的果蝇](https://talk.nervos.org/t/ckb-fly-ckb/10725/1) | tianlitao | 2026-09-20 17:33:03 CST | 简介 CKB Fly 把果蝇大脑里管「面朝哪个方向」的回路（头方向环吸引子）放到了 CKB 上：155 个神经元、6,522 条连接、45,961 个突触，连接组来自 FlyWire release 783。整个神经系统就是一个 cell，1,213 字节。 它是 MidTermDev/immortal-fruit-fly 的移植（原版跑在 BSC 的 EVM 上），要求逐位一致：同样的动作序列，产生同样的膜电位、同样的放电、同样的朝向。这条是拿主网真实轨迹在 CKB-VM 里重放验证的，不是「看着像」。 没有代币。 没有服务器。 玩法 看：打开...
- `S05` [重启utxo stack](https://talk.nervos.org/t/utxo-stack/10724/1) | ckbbkc | 2026-09-20 15:46:40 CST | 如何才能重启，或者重新搞一个 之前关闭的utxo stack项目？
- `S06` [[RFC & Research] Automated Channel Liquidity Rebalancing on Fiber Network](https://talk.nervos.org/t/rfc-research-automated-channel-liquidity-rebalancing-on-fiber-network/10691/6) | quake | 2026-09-20 14:35:41 CST | Thanks for sharing the research and prototype, we really appreciate the effort to improve liquidity management for Fiber node operators. Additional routing hints and graph cycle queries aren’t high-priority items for the core team right now. We’re currently working on Loop...
- `S07` [RIVET: CKB-native GitHub backup using IPFS, RGB++, and CCC](https://talk.nervos.org/t/rivet-ckb-native-github-backup-using-ipfs-rgb-and-ccc/10722/3) | joii2020 | 2026-09-20 09:31:20 CST | Good Idea! I think that besides Git, there are many other areas where similar functionality is needed. Do you think the current on-chain script fully meets your needs, or does the ideal scenario require developing an new on-chain script?

## 活跃话题

1. [Spark Program | CKB Revocable Timelock (CRT) — Timelock Encryption You Can Cancel](https://talk.nervos.org/t/spark-program-ckb-revocable-timelock-crt-timelock-encryption-you-can-cancel/10698) | 1 条近窗帖子 | 最新活动 2026-09-20 23:31:01 CST | tags: Pending
2. [Khie，「契」。](https://talk.nervos.org/t/khie/10726) | 1 条近窗帖子 | 最新活动 2026-09-20 20:59:38 CST | tags: CKB, dapp
3. [[DIS] Pocket Node for iOS: a self-custody CKB light client for Apple and Identity/Signer for CCC web apps](https://talk.nervos.org/t/dis-pocket-node-for-ios-a-self-custody-ckb-light-client-for-apple-and-identity-signer-for-ccc-web-apps/10583) | 1 条近窗帖子 | 最新活动 2026-09-20 20:15:19 CST | tags: Pocket-Node, light-client
4. [CKB Fly ｜一只活在CKB上的果蝇](https://talk.nervos.org/t/ckb-fly-ckb/10725) | 1 条近窗帖子 | 最新活动 2026-09-20 17:33:03 CST | tags: dapp
5. [重启utxo stack](https://talk.nervos.org/t/utxo-stack/10724) | 1 条近窗帖子 | 最新活动 2026-09-20 15:46:40 CST
6. [[RFC & Research] Automated Channel Liquidity Rebalancing on Fiber Network](https://talk.nervos.org/t/rfc-research-automated-channel-liquidity-rebalancing-on-fiber-network/10691) | 1 条近窗帖子 | 最新活动 2026-09-20 14:35:41 CST
7. [RIVET: CKB-native GitHub backup using IPFS, RGB++, and CCC](https://talk.nervos.org/t/rivet-ckb-native-github-backup-using-ipfs-rgb-and-ccc/10722) | 1 条近窗帖子 | 最新活动 2026-09-20 09:31:20 CST | tags: CKB, RGB, appchain, dapp, ipfs, lang-en

## 最近帖子摘录

- 2026-09-20 23:31:01 CST | psawyerberlin | [Spark Program | CKB Revocable Timelock (CRT) — Timelock Encryption You Can Cancel](https://talk.nervos.org/t/spark-program-ckb-revocable-timelock-crt-timelock-encryption-you-can-cancel/10698/3) | Thanks xingtian, and thanks to the committee for reading it carefully. Both points are fair and I’d rather answer them bluntly than well. I’ve edited the original post...
- 2026-09-20 20:59:38 CST | Hanssen | [Khie，「契」。](https://talk.nervos.org/t/khie/10726/1) | 本文同时发表于我的个人博客。 khie.svg945×945 6.36 KB Khie /kʰje/，客家語，意为契。 准备钱包，打开应用，扫码，结契。Khie 基于 libp2p，是构建在端到端通道上的钱包连接协议。 我很难给 Khie 再下更复杂的定义，它就像 CCC 一样，你打开，连接钱包，然后忘掉它。虽然如此，Khie...
- 2026-09-20 20:15:19 CST | Jnr6 | [[DIS] Pocket Node for iOS: a self-custody CKB light client for Apple and Identity/Signer for CCC web apps](https://talk.nervos.org/t/dis-pocket-node-for-ios-a-self-custody-ckb-light-client-for-apple-and-identity-signer-for-ccc-web-apps/10583/22) | Pocket Node for iOS: Milestone 1 completion report Milestone 1 of the iOS grant (“Shared core, iOS bridge, app skeleton”) is complete and tagged as ios-m1 on main. This post...
- 2026-09-20 17:33:03 CST | tianlitao | [CKB Fly ｜一只活在CKB上的果蝇](https://talk.nervos.org/t/ckb-fly-ckb/10725/1) | 简介 CKB Fly 把果蝇大脑里管「面朝哪个方向」的回路（头方向环吸引子）放到了 CKB 上：155 个神经元、6,522 条连接、45,961 个突触，连接组来自 FlyWire release 783。整个神经系统就是一个 cell，1,213 字节。 它是 MidTermDev/immortal-fruit-fly 的移植（原版跑在 BSC 的...
- 2026-09-20 15:46:40 CST | ckbbkc | [重启utxo stack](https://talk.nervos.org/t/utxo-stack/10724/1) | 如何才能重启，或者重新搞一个 之前关闭的utxo stack项目？
- 2026-09-20 14:35:41 CST | quake | [[RFC & Research] Automated Channel Liquidity Rebalancing on Fiber Network](https://talk.nervos.org/t/rfc-research-automated-channel-liquidity-rebalancing-on-fiber-network/10691/6) | Thanks for sharing the research and prototype, we really appreciate the effort to improve liquidity management for Fiber node operators. Additional routing hints and graph cycle...
- 2026-09-20 09:31:20 CST | joii2020 | [RIVET: CKB-native GitHub backup using IPFS, RGB++, and CCC](https://talk.nervos.org/t/rivet-ckb-native-github-backup-using-ipfs-rgb-and-ccc/10722/3) | Good Idea! I think that besides Git, there are many other areas where similar functionality is needed. Do you think the current on-chain script fully meets your needs, or does...
