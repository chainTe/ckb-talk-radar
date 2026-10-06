# Nervos Talk 社区简报

- 统计窗口: 2026-10-06 05:26:03 CST 到 2026-10-07 05:26:03 CST
- 生成时间: 2026-10-07 05:26:14 CST
- 话题数: 11
- 帖子数: 14
- 作者数: 11
- 总结模式: ai:openai-compatible

## 社区总结

## 今日发生了什么

今天论坛最集中的动态是 Spark 相关：Corven 提交新资助提案 [S10]，zk-Lock 合并关键 PR [S08]，Spark Verify 的审议被委员会排到 10 月 8 日 [S12]。同时，Kirea Finance 发布 CKB 原生 RWA 借贷的 [DIS] 讨论帖 [S02]，Tranfr 和 Myelin 等开发项目也有进展或提问 [S07, S14]。社区侧则发布了 CKBA Reddit AMA 回顾和 Aba 线下活动回顾 [S03, S04]。整体看，今天项目提案、开发讨论和社区活动都有动静，不算平静 [S10, S02, S04]。

## 重点话题

- Spark 审议与提案集中：Corven 请求 600 美元、4 周，为现有浏览器 CKB IDE 添加 Fiber Network 工具，并在肯尼亚 Web3 开发者俱乐部测试 [S10]；zk-Lock 作者称已合并 PR #4，zk-lock-bound 进入主代码库 [S08]；Spark Verify 申请人询问委员会是否已审阅最新更新 [S11]，委员会回复因中国国庆假期将本周 Spark 审议安排在 10 月 8 日 [S12]。
- Kirea Finance 发布 [DIS] 讨论帖：它定位为 CKB 上原生 RWA 借贷模式 [S02]，将现实世界资产债权表示为独特、可拥有的链上资产，可持有、转移或用作贷款抵押 [S02]，全生命周期从资产发行和 KYC 开始 [S02]。
- 开发基础设施继续推进：Tranfr 更新称已完成数据布局和状态表示，并实现、测试 deadline-check 逻辑 [S07]；Myelin 帖下有人问会话能否运行 L1 不支持的增强“Cell Model v1.5”，允许修改交易形状或规则 [S14]；FNN Safeguard 讨论中有人质疑恢复节点用复制身份材料连接 Fiber 网络后，安全假设是否过时，并将其类比为“可复现构建”方法 [S13]；Khie 帖下有人赞赏把钱包连接作为一次配置、无需中心化 relay 或浏览器注入的 P2P 层 [S09]。
- CKB Off Chain Aba 活动获正面反馈：活动回顾称 10 月 3 日在 Abia State Aba 与 Abia Web3 Network 合作举办，尽管大雨仍有人参加 [S04]；回帖表示高兴看到 CKB 聚会 [S05]，并称赞写得好 [S06]。
- CKBA 相关动态：NNCBN 在周报中称其申请 CKBA Contributing Member 的投票决定此时不接纳 [S01]，他会继续推进实现，让未来决定更可能通过 [S01]；同日 CKBA Reddit AMA 回顾发布，Stefan 作为 CKBA 内容与传播团队负责人参与，讨论涵盖提升 CKB 可见度等 [S03]。

## 值得继续跟进

- 10 月 8 日 Spark 审议结果：委员会已说明本周 Spark 审议安排在 10 月 8 日 [S12]，Spark Verify 正在等待 [S11]，Corven 新提案也在流程中 [S10]；这些项目的后续决定值得观察 [S12, S11, S10]。
- Kirea Finance 的 RWA 借贷讨论：该 [DIS] 把现实世界资产债权做成可持有、转移和抵押的链上资产，并涉及发行和 KYC 生命周期 [S02]；后续社区对这类原生 RWA 模式的讨论细节值得跟进 [S02]。
- Fiber 与底层扩展相关风险：Corven 计划为 CKB IDE 加 Fiber Network 工具 [S10]，FNN Safeguard 正在讨论恢复节点和升级前资格的安全假设 [S13]，Myelin 也被问能否支持 L1 不支持的增强 Cell Model v1.5 [S14]；这些方向都还需要更多技术反馈 [S10, S13, S14]。

## 来源索引

- `S01` [Spark Program | NNCBN - Nervos Network Community Boot Nodes](https://talk.nervos.org/t/spark-program-nncbn-nervos-network-community-boot-nodes/10653/12) | NNCBN | 2026-10-07 01:17:17 CST | 2026 October 06, Second Weekly Report I received a response to my application to become a CKBA Contributing Member. The vote resulted in a decision against admission at this time. I will continue to work on the implementation so that a future decision will be more likely to be...
- `S02` [[DIS] Hardening Kirea Finance (Native RWA Lending on CKB)](https://talk.nervos.org/t/dis-hardening-kirea-finance-native-rwa-lending-on-ckb/10809/1) | SalmanDev | 2026-10-07 00:14:27 CST | Summary Kirea Finance is a native Real-World Asset (RWA) pattern built on CKB, which represents real-world asset claims as unique, ownable on-chain assets that owners can hold, transfer, or use as collateral for loans. The full lifecycle, from asset issuance and KYC...
- `S03` [AMA with Stefan, CKBA’s Content & Communications Team Lead](https://talk.nervos.org/t/ama-with-stefan-ckba-s-content-communications-team-lead/10733/3) | zz_tovarishch | 2026-10-06 22:29:04 CST | image1920×2213 448 KB The CKBA Reddit AMA Recap Cheers everyone, Thanks to everyone who joined our Reddit AMA with Stefan, who leads CKBA’s Content & Communications team. As part of our series introducing CKBA’s team leaders, the discussion covered growing CKB’s visibility,...
- `S04` [CKB Off Chain Aba: Event Overview](https://talk.nervos.org/t/ckb-off-chain-aba-event-overview/10808/1) | Jedi_dtechmaker | 2026-10-06 16:23:52 CST | On October 3, 2026, we brought CKB Off Chain to Aba, Abia State. We worked closely with Abia Web3 Network to make this happen. The weather was terrible, it rained heavily for most of the day, but the people who showed up were exactly the right ones....
- `S05` [CKB Off Chain Aba: Event Overview](https://talk.nervos.org/t/ckb-off-chain-aba-event-overview/10808/2) | Code3ks | 2026-10-06 21:27:04 CST | Happy to see a CKB gathering like this.
- `S06` [CKB Off Chain Aba: Event Overview](https://talk.nervos.org/t/ckb-off-chain-aba-event-overview/10808/3) | Birdmannn | 2026-10-06 22:28:19 CST | Nice work, and nice write up. Well done, my boss.
- `S07` [Tranfr — Programmable Recovery for CKB](https://talk.nervos.org/t/tranfr-programmable-recovery-for-ckb/10644/16) | SalmanDev | 2026-10-06 16:17:39 CST | Tranfr — Progress Update I’ve made solid progress on the core Tranfr implementation and have now completed several of the key technical foundations. Completed so far Finalized the Tranfr data layout and state representation. Implemented and tested the deadline-check logic in...
- `S08` [Spark Program | zk-Lock for CKB](https://talk.nervos.org/t/spark-program-zk-lock-for-ckb/10448/21) | Mulandi_Cecilia | 2026-10-06 16:10:22 CST | gm gm @xingtianchunyan and the committee, Thank you for being direct. I think I had read the previous post and interpreted it narrowly. First, I have merged PR #4, so zk-lock-bound is now part of the main codebase. I believe it gives the project a rounder feel and also extends...
- `S09` [Khie，「契」。](https://talk.nervos.org/t/khie/10726/4) | Code3ks | 2026-10-06 15:33:01 CST | Love the idea of making wallet connection a P2P layer you set up once and forget. Not needing a centralized relay or browser injection makes cross-device flows, like a phone wallet driving an AI tool on desktop, feel much more realistic. The CCC App module is a smart bridge...
- `S10` [Spark Program Proposal: Corven](https://talk.nervos.org/t/spark-program-proposal-corven/10807/1) | lestonEth | 2026-10-06 14:37:49 CST | English Version Corven requests $600 over 4 weeks to add Fiber Network tooling to its working browser-based CKB IDE and test it with Web3 developer clubs across Kenya. Project Name Corven: a browser-based IDE for building on CKB and Fiber Network Team / Individual Profile...
- `S11` [Spark Program | Spark Verify - Reproducible Acceptance Checks for CKB Projects](https://talk.nervos.org/t/spark-program-spark-verify-reproducible-acceptance-checks-for-ckb-projects/10598/12) | Akane | 2026-10-06 05:37:51 CST | Hi @zz_tovarishch, just following up on my latest update—has the committee had a chance to review it?
- `S12` [Spark Program | Spark Verify - Reproducible Acceptance Checks for CKB Projects](https://talk.nervos.org/t/spark-program-spark-verify-reproducible-acceptance-checks-for-ckb-projects/10598/13) | zz_tovarishch | 2026-10-06 13:51:32 CST | 你好Akane, 因为这周是中国的国庆假期，委员会将这周的Spark审议安排在了10.8号 我们会在审议后尽快通知到各个项目，感谢您的理解和耐心
- `S13` [[DIS] FNN Safeguard — Recovery Verification and Pre-Upgrade Qualification for Fiber Nodes](https://talk.nervos.org/t/dis-fnn-safeguard-recovery-verification-and-pre-upgrade-qualification-for-fiber-nodes/10712/9) | knmo | 2026-10-06 12:56:01 CST | Dappsoverapps: A recovered node connects to the Fiber network using copied identity material. Isn’t it true that once files have been copied or extracted, security assumptions become obsolete anyway? To me, this sounds like a “reproducible build” approach. If even Quake...
- `S14` [Introducing Myelin: a CKB-aligned off-chain Cell session runtime](https://talk.nervos.org/t/introducing-myelin-a-ckb-aligned-off-chain-cell-session-runtime/10498/11) | jm9k | 2026-10-06 11:08:24 CST | Hey @ArthurZhang, great work on this. One question: Could a Myelin session run an enhanced “Cell Model v1.5” with modified transaction shapes or rules that L1 does not support?

## 活跃话题

1. [Spark Program | NNCBN - Nervos Network Community Boot Nodes](https://talk.nervos.org/t/spark-program-nncbn-nervos-network-community-boot-nodes/10653) | 1 条近窗帖子 | 最新活动 2026-10-07 01:17:17 CST | tags: In-Progress, Node, Spark-Program, bootnode
2. [[DIS] Hardening Kirea Finance (Native RWA Lending on CKB)](https://talk.nervos.org/t/dis-hardening-kirea-finance-native-rwa-lending-on-ckb/10809) | 1 条近窗帖子 | 最新活动 2026-10-07 00:14:27 CST
3. [AMA with Stefan, CKBA’s Content & Communications Team Lead](https://talk.nervos.org/t/ama-with-stefan-ckba-s-content-communications-team-lead/10733) | 1 条近窗帖子 | 最新活动 2026-10-06 22:29:04 CST | tags: AMA
4. [CKB Off Chain Aba: Event Overview](https://talk.nervos.org/t/ckb-off-chain-aba-event-overview/10808) | 3 条近窗帖子 | 最新活动 2026-10-06 22:28:19 CST
5. [Tranfr — Programmable Recovery for CKB](https://talk.nervos.org/t/tranfr-programmable-recovery-for-ckb/10644) | 1 条近窗帖子 | 最新活动 2026-10-06 16:17:39 CST | tags: In-Progress
6. [Spark Program | zk-Lock for CKB](https://talk.nervos.org/t/spark-program-zk-lock-for-ckb/10448) | 1 条近窗帖子 | 最新活动 2026-10-06 16:10:22 CST | tags: In-Progress
7. [Khie，「契」。](https://talk.nervos.org/t/khie/10726) | 1 条近窗帖子 | 最新活动 2026-10-06 15:33:01 CST | tags: CKB, dapp
8. [Spark Program Proposal: Corven](https://talk.nervos.org/t/spark-program-proposal-corven/10807) | 1 条近窗帖子 | 最新活动 2026-10-06 14:37:49 CST | tags: CKB, Grant, Spark-Program
9. [Spark Program | Spark Verify - Reproducible Acceptance Checks for CKB Projects](https://talk.nervos.org/t/spark-program-spark-verify-reproducible-acceptance-checks-for-ckb-projects/10598) | 2 条近窗帖子 | 最新活动 2026-10-06 13:51:32 CST | tags: Pending
10. [[DIS] FNN Safeguard — Recovery Verification and Pre-Upgrade Qualification for Fiber Nodes](https://talk.nervos.org/t/dis-fnn-safeguard-recovery-verification-and-pre-upgrade-qualification-for-fiber-nodes/10712) | 1 条近窗帖子 | 最新活动 2026-10-06 12:56:01 CST
11. [Introducing Myelin: a CKB-aligned off-chain Cell session runtime](https://talk.nervos.org/t/introducing-myelin-a-ckb-aligned-off-chain-cell-session-runtime/10498) | 1 条近窗帖子 | 最新活动 2026-10-06 11:08:24 CST | tags: CKB-VM, CellScript, Myelin, lang-en

## 最近帖子摘录

- 2026-10-07 01:17:17 CST | NNCBN | [Spark Program | NNCBN - Nervos Network Community Boot Nodes](https://talk.nervos.org/t/spark-program-nncbn-nervos-network-community-boot-nodes/10653/12) | 2026 October 06, Second Weekly Report I received a response to my application to become a CKBA Contributing Member. The vote resulted in a decision against admission at this...
- 2026-10-07 00:14:27 CST | SalmanDev | [[DIS] Hardening Kirea Finance (Native RWA Lending on CKB)](https://talk.nervos.org/t/dis-hardening-kirea-finance-native-rwa-lending-on-ckb/10809/1) | Summary Kirea Finance is a native Real-World Asset (RWA) pattern built on CKB, which represents real-world asset claims as unique, ownable on-chain assets that owners can hold,...
- 2026-10-06 22:29:04 CST | zz_tovarishch | [AMA with Stefan, CKBA’s Content & Communications Team Lead](https://talk.nervos.org/t/ama-with-stefan-ckba-s-content-communications-team-lead/10733/3) | image1920×2213 448 KB The CKBA Reddit AMA Recap Cheers everyone, Thanks to everyone who joined our Reddit AMA with Stefan, who leads CKBA’s Content & Communications team. As...
- 2026-10-06 22:28:19 CST | Birdmannn | [CKB Off Chain Aba: Event Overview](https://talk.nervos.org/t/ckb-off-chain-aba-event-overview/10808/3) | Nice work, and nice write up. Well done, my boss.
- 2026-10-06 21:27:04 CST | Code3ks | [CKB Off Chain Aba: Event Overview](https://talk.nervos.org/t/ckb-off-chain-aba-event-overview/10808/2) | Happy to see a CKB gathering like this.
- 2026-10-06 16:23:52 CST | Jedi_dtechmaker | [CKB Off Chain Aba: Event Overview](https://talk.nervos.org/t/ckb-off-chain-aba-event-overview/10808/1) | On October 3, 2026, we brought CKB Off Chain to Aba, Abia State. We worked closely with Abia Web3 Network to make this happen. The weather was terrible, it rained heavily for...
- 2026-10-06 16:17:39 CST | SalmanDev | [Tranfr — Programmable Recovery for CKB](https://talk.nervos.org/t/tranfr-programmable-recovery-for-ckb/10644/16) | Tranfr — Progress Update I’ve made solid progress on the core Tranfr implementation and have now completed several of the key technical foundations. Completed so far Finalized...
- 2026-10-06 16:10:22 CST | Mulandi_Cecilia | [Spark Program | zk-Lock for CKB](https://talk.nervos.org/t/spark-program-zk-lock-for-ckb/10448/21) | gm gm @xingtianchunyan and the committee, Thank you for being direct. I think I had read the previous post and interpreted it narrowly. First, I have merged PR #4, so zk-lock-...
- 2026-10-06 15:33:01 CST | Code3ks | [Khie，「契」。](https://talk.nervos.org/t/khie/10726/4) | Love the idea of making wallet connection a P2P layer you set up once and forget. Not needing a centralized relay or browser injection makes cross-device flows, like a phone...
- 2026-10-06 14:37:49 CST | lestonEth | [Spark Program Proposal: Corven](https://talk.nervos.org/t/spark-program-proposal-corven/10807/1) | English Version Corven requests $600 over 4 weeks to add Fiber Network tooling to its working browser-based CKB IDE and test it with Web3 developer clubs across Kenya. Project...
- 2026-10-06 13:51:32 CST | zz_tovarishch | [Spark Program | Spark Verify - Reproducible Acceptance Checks for CKB Projects](https://talk.nervos.org/t/spark-program-spark-verify-reproducible-acceptance-checks-for-ckb-projects/10598/13) | 你好Akane, 因为这周是中国的国庆假期，委员会将这周的Spark审议安排在了10.8号 我们会在审议后尽快通知到各个项目，感谢您的理解和耐心
- 2026-10-06 12:56:01 CST | knmo | [[DIS] FNN Safeguard — Recovery Verification and Pre-Upgrade Qualification for Fiber Nodes](https://talk.nervos.org/t/dis-fnn-safeguard-recovery-verification-and-pre-upgrade-qualification-for-fiber-nodes/10712/9) | Dappsoverapps: A recovered node connects to the Fiber network using copied identity material. Isn’t it true that once files have been copied or extracted, security assumptions...
- 2026-10-06 11:08:24 CST | jm9k | [Introducing Myelin: a CKB-aligned off-chain Cell session runtime](https://talk.nervos.org/t/introducing-myelin-a-ckb-aligned-off-chain-cell-session-runtime/10498/11) | Hey @ArthurZhang, great work on this. One question: Could a Myelin session run an enhanced “Cell Model v1.5” with modified transaction shapes or rules that L1 does not support?
- 2026-10-06 05:37:51 CST | Akane | [Spark Program | Spark Verify - Reproducible Acceptance Checks for CKB Projects](https://talk.nervos.org/t/spark-program-spark-verify-reproducible-acceptance-checks-for-ckb-projects/10598/12) | Hi @zz_tovarishch, just following up on my latest update—has the committee had a chance to review it?
