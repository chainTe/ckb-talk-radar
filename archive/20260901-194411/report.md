# Nervos Talk 社区简报

- 统计窗口: 2026-09-01 03:44:11 CST 到 2026-09-02 03:44:11 CST
- 生成时间: 2026-09-02 03:44:15 CST
- 话题数: 4
- 帖子数: 5
- 作者数: 4
- 总结模式: ai:openai-compatible

## 社区总结

## 今日发生了什么

过去 24 小时，Nervos Talk 整体讨论量不算多，但话题比较集中：社区主要围绕挖矿去中心化、共识机制设计和治理流程展开 [S01, S02, S03, S04, S05]。一位成员提出新的挖矿去中心化奖励提案，并得到 DAO 协调员的流程反馈 [S03, S04]；同时有成员发出头部矿池算力集中的警告 [S05]。此外，CKBA 会员申请截止日期因 GA 延期而更新 [S01]。

## 重点话题

- **挖矿去中心化奖励提案**：knmo 提出“CKB mining Decentralization Rewarder”方案，并表示开发前提是 Spark 计划的 NNCBN 项目获得批准，否则缺少必要硬件 [S03]。DAO 协调员 zz_tovarishch 随即回应，按照 CKB Community Fund DAO 规则指出提案在流程和完整性上还有待补充，以帮助其推进下一步 [S04]。

- **头部矿池算力集中警告**：knmo 在算力集中讨论帖中报告，f2 矿池刚刚新增了 15 PH/s 的算力，头部矿池合计占比已接近 49% [S05]。

- **“Proof of Buy”共识机制技术讨论**：在关于为 Layer1 设计的 Layer2 共识方案帖中，Lawliet_Chan 讨论了矿工延迟广播以获取优势的潜在攻击问题，并提出对策：矿工必须在计算 VRF 随机值前，事先指定为该区块支付多少 L1 token [S02]。

- **CKBA 会员申请截止日更新**：由于即将到来的 GA 已推迟到 9 月底，Contributing Member 的申请截止日期相应调整为 9 月 15 日（AOE）[S01]。

## 值得继续跟进

- knmo 的挖矿去中心化奖励提案能否按 DAO 规则补齐材料并进入正式流程，值得观察 [S03, S04]。
- 头部矿池算力已接近 49%，后续是否继续增长、社区和项目方是否会就此提出应对讨论，需要留意 [S05]。
- “Proof of Buy”方案中“先支付、后出块”的设计是否能有效解决延迟广播问题，有待进一步讨论验证 [S02]。

## 来源索引

- `S01` [CKBA Membership Process](https://talk.nervos.org/t/ckba-membership-process/10340/9) | CKBAMembership | 2026-09-01 22:00:45 CST | Update Since the upcoming GA has been changed to the end of September, the application deadline for Contributing Member is now September 15 (AOE).
- `S02` [Proof of Buy，一种专为Layer1设计的Layer2共识](https://talk.nervos.org/t/proof-of-buy-layer1-layer2/9752/31) | Lawliet_Chan | 2026-09-01 15:09:16 CST | 至此，我们会迎来一个新的问题。 如果， 此时我先使用VRF计算随机值，然后等待其他矿工广播他的goal，当我发现这些goal之后，我本地做计算，看看我需要为本区块支付多少L1 token才能比他的goal更高，从而抢得出块权。 如此， 几乎所有矿工都会偏好延迟广播自己的区块，要求先看到别人的goal再计算并广播自己的goal，后广播的矿工具备了天然优势。 这显然是不行的。 所以，我们需要将为本高度的区块支付L1 token的行为在时间上往前移——你必须事先指定你要为该区块支付多少L1 token，然后再计算VRF输出值。而事先支付L1...
- `S03` [CKB mining Decentralization Rewarder](https://talk.nervos.org/t/ckb-mining-decentralization-rewarder/10672/1) | knmo | 2026-09-01 09:11:37 CST | CKB mining Decentralization Rewarder Let me say this right off the bat: I would make the development and implementation contingent on the approval of the Spark program NNCBN, since otherwise I won’t have the necessary hardware. Nevertheless, I make a clear distinction between...
- `S04` [CKB mining Decentralization Rewarder](https://talk.nervos.org/t/ckb-mining-decentralization-rewarder/10672/2) | zz_tovarishch | 2026-09-01 09:32:54 CST | Hi @knmo , Thank you for bringing this proposal idea to the community. As a DAO coordinator, I would like to share some feedback regarding the process rules and proposal completeness to help guide your next steps: 1.Current Post Status Under the CKB Community Fund DAO Rules...
- `S05` [49% pools hashrate 62qw704s93hhsj](https://talk.nervos.org/t/49-pools-hashrate-62qw704s93hhsj/8691/3) | knmo | 2026-09-01 07:04:53 CST | Someone just added 15 PH/s to f2. Sad.

## 活跃话题

1. [CKBA Membership Process](https://talk.nervos.org/t/ckba-membership-process/10340) | 1 条近窗帖子 | 最新活动 2026-09-01 22:00:45 CST | tags: CKBA, Membership, lang-en
2. [Proof of Buy，一种专为Layer1设计的Layer2共识](https://talk.nervos.org/t/proof-of-buy-layer1-layer2/9752) | 1 条近窗帖子 | 最新活动 2026-09-01 15:09:16 CST | tags: lang-zh, 共识协议
3. [CKB mining Decentralization Rewarder](https://talk.nervos.org/t/ckb-mining-decentralization-rewarder/10672) | 2 条近窗帖子 | 最新活动 2026-09-01 09:32:54 CST | tags: coinbase, decentralisation, mining
4. [49% pools hashrate 62qw704s93hhsj](https://talk.nervos.org/t/49-pools-hashrate-62qw704s93hhsj/8691) | 1 条近窗帖子 | 最新活动 2026-09-01 07:04:53 CST | tags: lang-en

## 最近帖子摘录

- 2026-09-01 22:00:45 CST | CKBAMembership | [CKBA Membership Process](https://talk.nervos.org/t/ckba-membership-process/10340/9) | Update Since the upcoming GA has been changed to the end of September, the application deadline for Contributing Member is now September 15 (AOE).
- 2026-09-01 15:09:16 CST | Lawliet_Chan | [Proof of Buy，一种专为Layer1设计的Layer2共识](https://talk.nervos.org/t/proof-of-buy-layer1-layer2/9752/31) | 至此，我们会迎来一个新的问题。 如果， 此时我先使用VRF计算随机值，然后等待其他矿工广播他的goal，当我发现这些goal之后，我本地做计算，看看我需要为本区块支付多少L1 token才能比他的goal更高，从而抢得出块权。 如此，...
- 2026-09-01 09:32:54 CST | zz_tovarishch | [CKB mining Decentralization Rewarder](https://talk.nervos.org/t/ckb-mining-decentralization-rewarder/10672/2) | Hi @knmo , Thank you for bringing this proposal idea to the community. As a DAO coordinator, I would like to share some feedback regarding the process rules and proposal...
- 2026-09-01 09:11:37 CST | knmo | [CKB mining Decentralization Rewarder](https://talk.nervos.org/t/ckb-mining-decentralization-rewarder/10672/1) | CKB mining Decentralization Rewarder Let me say this right off the bat: I would make the development and implementation contingent on the approval of the Spark program NNCBN,...
- 2026-09-01 07:04:53 CST | knmo | [49% pools hashrate 62qw704s93hhsj](https://talk.nervos.org/t/49-pools-hashrate-62qw704s93hhsj/8691/3) | Someone just added 15 PH/s to f2. Sad.
