# Nervos Talk 社区简报

- 统计窗口: 2026-09-04 03:16:46 CST 到 2026-09-05 03:16:46 CST
- 生成时间: 2026-09-05 03:16:50 CST
- 话题数: 6
- 帖子数: 9
- 作者数: 6
- 总结模式: ai:openai-compatible

## 社区总结

## 今日发生了什么

过去 24 小时论坛有不少实质性进展 [S01, S02, S03, S04, S07, S09]。最突出的是两件事：Vellum（did:ckb 上的信誉扩展）治理投票正式通过，支持率 64.37% [S04]；CellScript 发布 0.25 版本，为基于 Cell 的合约带来更丰富的语言能力 [S07]。此外，Fiber 生态也出现了一个新项目 ChannelForge，定位为“流动性就绪引擎” [S01]。

## 重点话题

- Vellum 投票通过并完成核验：Metaforo 收盘统计显示支持率 64.37%，总投票权重 242,742,014 CKB，之后又用 CKB DAO Watchdog 和人工检查做了交叉核验 [S04]。有社区成员表示很高兴看到 Vellum 通过，因为在某些场景下信誉机制是必不可少的 [S05]。

- CellScript 0.25 发布：这个版本为合约作者增加了有界非 Cell 泛型、Option<T>、泛型定长数组、全范围 u128 字面量以及 checked 除法等能力 [S07]。作者也提醒，0.25 中 value generics 的设计和公共接口尚未最终确定，目前正在考虑简化公共泛型接口，或者把用户自定义泛型限制在包内 [S08]。

- ChannelForge 项目亮相：这是一个开源 Fiber 基础设施层，目的是帮助支付应用判断某笔支付能否成功被接收，并帮助识别流动性 [S01]。目前该项目的公开介绍还处于项目概述阶段 [S01]。

- NNCBN Spark Program 更新：社区 Boot Nodes 项目公开了已创建的 GitHub 组织与仓库链接，包括 NT-Spark 和 Qubes，并表示之后会每周固定时间用文字同步进度 [S02]。

- 其他进展：Pocket Node for iOS 公布了 kickoff 支付的链上交易链接 [S03]；Tranfr 获得委员会拨款批准，但金额从原申请的 $1,600 降至 $700，同时 Tianji 的反馈暴露了 commit-bound 两阶段设计中的缺口 [S09]。

## 值得继续跟进

- CellScript 0.25 的 value generics 公共接口还没有定稿，后续 stable 版本如何取舍会影响合约作者的使用方式 [S08]。

- ChannelForge 刚发布总体介绍，需要观察它如何与 Fiber 的流动性体系对接，以及后续是否会进入具体讨论或开发 [S01]。

- Tranfr 虽然拿到拨款，但金额缩减且设计存在缺口，值得留意团队如何用更少的预算调整 commit-bound 两阶段方案 [S09]。

## 来源索引

- `S01` [ChannelForge](https://talk.nervos.org/t/channelforge/10684/1) | Okeyo | 2026-09-05 02:54:22 CST | 1. Project Overview Project Name ChannelForge — Fiber Liquidity Readiness Engine One-Sentence Summary ChannelForge is an open-source Fiber infrastructure layer that helps payment applications determine whether a specific payment can be successfully received, identify liquidity...
- `S02` [Spark Program | NNCBN - Nervos Network Community Boot Nodes](https://talk.nervos.org/t/spark-program-nncbn-nervos-network-community-boot-nodes/10653/5) | NNCBN | 2026-09-04 23:00:06 CST | xingtianchunyan: provide a link to a GitHub repository already created https:// github .com/NNCBN/ https:// github .com/NNCBN/NT-Spark https:// github .com/NNCBN/Qubes Text-based updates in this post, with progress updates at a fixed time each week. This is more formal than...
- `S03` [[DIS] Pocket Node for iOS: a self-custody CKB light client for Apple and Identity/Signer for CCC web apps](https://talk.nervos.org/t/dis-pocket-node-for-ios-a-self-custody-ckb-light-client-for-apple-and-identity-signer-for-ccc-web-apps/10583/18) | zz_tovarishch | 2026-09-04 17:43:46 CST | Kick off payment: https://explorer.nervos.org/transaction/0x63a7f3a52fc91c52939186ca9c1064238ccdfe498d3398f25707537f591bbaa4
- `S04` [[DIS] Vellum: Reputation Extension on did:ckb](https://talk.nervos.org/t/dis-vellum-reputation-extension-on-did-ckb/10613/4) | zz_tovarishch | 2026-09-04 12:15:17 CST | Based on the Metaforo tally at close, the outcome is PASSED. Approval is 64.37% with total voting weight 242,742,014 CKB. Post-close verification has been completed using CKB DAO Watchdog, together with a manual sanity check. The verification cross-checks Metaforo-recorded...
- `S05` [[DIS] Vellum: Reputation Extension on did:ckb](https://talk.nervos.org/t/dis-vellum-reputation-extension-on-did-ckb/10613/5) | ArthurZhang | 2026-09-04 12:28:16 CST | very glad to see Vellum make it through this time as reputation is indispensable in some contexts.
- `S06` [[DIS] Vellum: Reputation Extension on did:ckb](https://talk.nervos.org/t/dis-vellum-reputation-extension-on-did-ckb/10613/6) | truthixify | 2026-09-04 14:58:57 CST | zz_tovarishch: Based on the Metaforo tally at close, the outcome is PASSED. Approval is 64.37% with total voting weight 242,742,014 CKB. Post-close verification has been completed using CKB DAO Watchdog, together with a manual sanity check. The verification cross-checks...
- `S07` [CellScript - A DSL for Cell-Based Contracts](https://talk.nervos.org/t/cellscript-a-dsl-for-cell-based-contracts/10193/32) | ArthurZhang | 2026-09-04 11:58:19 CST | CellScript 0.25: More Expressive Contracts, Safer Upgrades, Stronger Verification Short Announcement CellScript 0.25 is out. For contract authors, this release adds bounded non-Cell generics, Option<T>, generic fixed arrays, full-range u128 literals, checked division and...
- `S08` [CellScript - A DSL for Cell-Based Contracts](https://talk.nervos.org/t/cellscript-a-dsl-for-cell-based-contracts/10193/33) | ArthurZhang | 2026-09-04 12:11:07 CST | One note on the 0.25 language work: the design and public interface for value generics are not final yet. i am currently considering two bounded options—simplifying the public generic surface, or keeping user-defined generics package-local for the 0.25 stable line. suggestions...
- `S09` [Tranfr — Programmable Recovery for CKB](https://talk.nervos.org/t/tranfr-programmable-recovery-for-ckb/10644/10) | SalmanDev | 2026-09-04 04:59:09 CST | Thank you to the committee for approving the grant. One thing before starting: the reduced funding of $700 (down from the original $1,600 request) lands at the same time the valuable feedback from Tianji surfaced a real gap in the design. The commit-bound two-phase...

## 活跃话题

1. [ChannelForge](https://talk.nervos.org/t/channelforge/10684) | 1 条近窗帖子 | 最新活动 2026-09-05 02:54:22 CST
2. [Spark Program | NNCBN - Nervos Network Community Boot Nodes](https://talk.nervos.org/t/spark-program-nncbn-nervos-network-community-boot-nodes/10653) | 1 条近窗帖子 | 最新活动 2026-09-04 23:00:06 CST | tags: Node, Pending, Spark-Program, bootnode
3. [[DIS] Pocket Node for iOS: a self-custody CKB light client for Apple and Identity/Signer for CCC web apps](https://talk.nervos.org/t/dis-pocket-node-for-ios-a-self-custody-ckb-light-client-for-apple-and-identity-signer-for-ccc-web-apps/10583) | 1 条近窗帖子 | 最新活动 2026-09-04 17:43:46 CST | tags: Pocket-Node, light-client
4. [[DIS] Vellum: Reputation Extension on did:ckb](https://talk.nervos.org/t/dis-vellum-reputation-extension-on-did-ckb/10613) | 3 条近窗帖子 | 最新活动 2026-09-04 14:58:57 CST
5. [CellScript - A DSL for Cell-Based Contracts](https://talk.nervos.org/t/cellscript-a-dsl-for-cell-based-contracts/10193) | 2 条近窗帖子 | 最新活动 2026-09-04 12:11:07 CST | tags: CKB-VM, CellScript, DSL, lang-en
6. [Tranfr — Programmable Recovery for CKB](https://talk.nervos.org/t/tranfr-programmable-recovery-for-ckb/10644) | 1 条近窗帖子 | 最新活动 2026-09-04 04:59:09 CST | tags: Pending

## 最近帖子摘录

- 2026-09-05 02:54:22 CST | Okeyo | [ChannelForge](https://talk.nervos.org/t/channelforge/10684/1) | 1. Project Overview Project Name ChannelForge — Fiber Liquidity Readiness Engine One-Sentence Summary ChannelForge is an open-source Fiber infrastructure layer that helps...
- 2026-09-04 23:00:06 CST | NNCBN | [Spark Program | NNCBN - Nervos Network Community Boot Nodes](https://talk.nervos.org/t/spark-program-nncbn-nervos-network-community-boot-nodes/10653/5) | xingtianchunyan: provide a link to a GitHub repository already created https:// github .com/NNCBN/ https:// github .com/NNCBN/NT-Spark https:// github .com/NNCBN/Qubes Text-...
- 2026-09-04 17:43:46 CST | zz_tovarishch | [[DIS] Pocket Node for iOS: a self-custody CKB light client for Apple and Identity/Signer for CCC web apps](https://talk.nervos.org/t/dis-pocket-node-for-ios-a-self-custody-ckb-light-client-for-apple-and-identity-signer-for-ccc-web-apps/10583/18) | Kick off payment: https://explorer.nervos.org/transaction/0x63a7f3a52fc91c52939186ca9c1064238ccdfe498d3398f25707537f591bbaa4
- 2026-09-04 14:58:57 CST | truthixify | [[DIS] Vellum: Reputation Extension on did:ckb](https://talk.nervos.org/t/dis-vellum-reputation-extension-on-did-ckb/10613/6) | zz_tovarishch: Based on the Metaforo tally at close, the outcome is PASSED. Approval is 64.37% with total voting weight 242,742,014 CKB. Post-close verification has been...
- 2026-09-04 12:28:16 CST | ArthurZhang | [[DIS] Vellum: Reputation Extension on did:ckb](https://talk.nervos.org/t/dis-vellum-reputation-extension-on-did-ckb/10613/5) | very glad to see Vellum make it through this time as reputation is indispensable in some contexts.
- 2026-09-04 12:15:17 CST | zz_tovarishch | [[DIS] Vellum: Reputation Extension on did:ckb](https://talk.nervos.org/t/dis-vellum-reputation-extension-on-did-ckb/10613/4) | Based on the Metaforo tally at close, the outcome is PASSED. Approval is 64.37% with total voting weight 242,742,014 CKB. Post-close verification has been completed using CKB...
- 2026-09-04 12:11:07 CST | ArthurZhang | [CellScript - A DSL for Cell-Based Contracts](https://talk.nervos.org/t/cellscript-a-dsl-for-cell-based-contracts/10193/33) | One note on the 0.25 language work: the design and public interface for value generics are not final yet. i am currently considering two bounded options—simplifying the public...
- 2026-09-04 11:58:19 CST | ArthurZhang | [CellScript - A DSL for Cell-Based Contracts](https://talk.nervos.org/t/cellscript-a-dsl-for-cell-based-contracts/10193/32) | CellScript 0.25: More Expressive Contracts, Safer Upgrades, Stronger Verification Short Announcement CellScript 0.25 is out. For contract authors, this release adds bounded non-...
- 2026-09-04 04:59:09 CST | SalmanDev | [Tranfr — Programmable Recovery for CKB](https://talk.nervos.org/t/tranfr-programmable-recovery-for-ckb/10644/10) | Thank you to the committee for approving the grant. One thing before starting: the reduced funding of $700 (down from the original $1,600 request) lands at the same time the...
