# Nervos Talk 社区简报

- 统计窗口: 2026-10-01 05:33:14 CST 到 2026-10-02 05:33:14 CST
- 生成时间: 2026-10-02 05:33:21 CST
- 话题数: 4
- 帖子数: 4
- 作者数: 4
- 总结模式: ai:openai-compatible

## 社区总结

## 今日发生了什么

按给定材料，Nervos Talk 在 2026-10-01 有 4 条可见更新，分别落在 did:ckb 声誉扩展、Spark Program 钱包行为研究、CKBA 会员流程和 LS-IDL。[S01, S02, S03, S04] 其中，Vellum 话题有人认领具体组件并计划测试网发行后回报，CKBA 公布了贡献会员投票结果。[S01, S03] 研究和技术侧，Spark Program 回复了研究结论边界，LS-IDL 继续讲 CKB IDL 的实践路径。[S02, S04] 从给定材料看，今天社区整体较平静，材料中仅见这 4 条更新；S02、S04 原文在关键处截断，完整讨论无法确认。[S01, S02, S03, S04]

## 重点话题

- **Vellum / did:ckb 声誉扩展有推进**：Ayoub_Lesfer 表示愿意负责 `crowdcell.campaign-funded.v1`。[S01] 他正在私信里与对方整理 payload，并计划等测试网开始发行后再到论坛发帖。[S01]
- **Spark Program 钱包行为研究给出结论边界**：mulinya 回复 xingtianchunyan，明确该研究没有建立经过验证的人类/机器人/交易所身份分类器。[S02] 它建立的是可复现的 CKB 原生行为分析流程、冻结观察队列，以及有证据支持的结构模式，原文在此截断。[S02]
- **CKBA 贡献会员投票结果公布**：CKBA Membership 发帖称，大会已完成对 10 月 GA 前收到的贡献会员申请投票。[S03] 本轮审议 5 份申请，1 名申请人获准加入，并欢迎 Yukang Chen。[S03]
- **LS-IDL 实践说明继续更新**：OWK50GA 的帖子以“从 Rust Witness 到可验证 CKB 接口”为题，介绍 CKB IDL 的实践 walkthrough。[S04] 帖中指出 CKB 脚本是可执行程序，钱包和交易构建者也需要知道如何构造这些程序期望的数据，CKB IDL 0.1 则给这个外部接口提供 canonical 描述，原文在此截断。[S04]

## 值得继续跟进

- 看 `crowdcell.campaign-funded.v1` 是否按计划在测试网发行，以及 Ayoub_Lesfer 是否会回到论坛公布 payload 和发行进展。[S01]
- 看 Spark Program 这条研究结论之后，社区是否会继续追问身份分类器边界、方法可复现性和观察队列的后续使用。[S02]
- 看 LS-IDL 0.1 的完整接口设计，以及 derive、validate、commit 相关讨论是否继续推进；材料截断，后续尚不明确。[S04]

## 来源索引

- `S01` [[DIS] Vellum: Reputation Extension on did:ckb](https://talk.nervos.org/t/dis-vellum-reputation-extension-on-did-ckb/10613/13) | Ayoub_Lesfer | 2026-10-02 04:53:00 CST | Sounds good, I’ll own crowdcell.campaign-funded.v1 then. Sorting out the payload with you in DM and I’ll post here once it’s issuing on testnet.
- `S02` [Spark Program | CKB Wallet Behaviour Intelligence](https://talk.nervos.org/t/spark-program-ckb-wallet-behaviour-intelligence/10338/28) | mulinya | 2026-10-02 00:59:25 CST | Hi xingtianchunyan, Research conclusion The study does not establish a verified human/bot/exchange identity classifier. It establishes a reproducible CKB-native behavioural-analysis workflow, a frozen observational cohort, and evidence-supported structural patterns whose...
- `S03` [CKBA Membership Process](https://talk.nervos.org/t/ckba-membership-process/10340/12) | CKBAMembership | 2026-10-01 23:09:19 CST | CKBA Contributing Member: Cycle 2 (Q3 2026) Outcome The General Assembly has completed its vote on the Contributing Member applications received ahead of the October GA. 5 applications were considered, and 1 applicant has been admitted. Please join us in welcoming Yukang Chen...
- `S04` [LS-IDL: a Lock Script Interface Description Language for CKB (derive, validate, commit)](https://talk.nervos.org/t/ls-idl-a-lock-script-interface-description-language-for-ckb-derive-validate-commit/10596/7) | OWK50GA | 2026-10-01 20:20:43 CST | From Rust Witness to Verifiable CKB Interface: A Practical CKB IDL Walkthrough CKB scripts are executable programs, but wallets and transaction builders also need to know how to construct the data those programs expect. CKB IDL 0.1 gives that external interface a canonical,...

## 活跃话题

1. [[DIS] Vellum: Reputation Extension on did:ckb](https://talk.nervos.org/t/dis-vellum-reputation-extension-on-did-ckb/10613) | 1 条近窗帖子 | 最新活动 2026-10-02 04:53:00 CST
2. [Spark Program | CKB Wallet Behaviour Intelligence](https://talk.nervos.org/t/spark-program-ckb-wallet-behaviour-intelligence/10338) | 1 条近窗帖子 | 最新活动 2026-10-02 00:59:25 CST | tags: In-Progress
3. [CKBA Membership Process](https://talk.nervos.org/t/ckba-membership-process/10340) | 1 条近窗帖子 | 最新活动 2026-10-01 23:09:19 CST | tags: CKBA, Membership, lang-en
4. [LS-IDL: a Lock Script Interface Description Language for CKB (derive, validate, commit)](https://talk.nervos.org/t/ls-idl-a-lock-script-interface-description-language-for-ckb-derive-validate-commit/10596) | 1 条近窗帖子 | 最新活动 2026-10-01 20:20:43 CST | tags: CKB

## 最近帖子摘录

- 2026-10-02 04:53:00 CST | Ayoub_Lesfer | [[DIS] Vellum: Reputation Extension on did:ckb](https://talk.nervos.org/t/dis-vellum-reputation-extension-on-did-ckb/10613/13) | Sounds good, I’ll own crowdcell.campaign-funded.v1 then. Sorting out the payload with you in DM and I’ll post here once it’s issuing on testnet.
- 2026-10-02 00:59:25 CST | mulinya | [Spark Program | CKB Wallet Behaviour Intelligence](https://talk.nervos.org/t/spark-program-ckb-wallet-behaviour-intelligence/10338/28) | Hi xingtianchunyan, Research conclusion The study does not establish a verified human/bot/exchange identity classifier. It establishes a reproducible CKB-native behavioural-...
- 2026-10-01 23:09:19 CST | CKBAMembership | [CKBA Membership Process](https://talk.nervos.org/t/ckba-membership-process/10340/12) | CKBA Contributing Member: Cycle 2 (Q3 2026) Outcome The General Assembly has completed its vote on the Contributing Member applications received ahead of the October GA. 5...
- 2026-10-01 20:20:43 CST | OWK50GA | [LS-IDL: a Lock Script Interface Description Language for CKB (derive, validate, commit)](https://talk.nervos.org/t/ls-idl-a-lock-script-interface-description-language-for-ckb-derive-validate-commit/10596/7) | From Rust Witness to Verifiable CKB Interface: A Practical CKB IDL Walkthrough CKB scripts are executable programs, but wallets and transaction builders also need to know how to...
