# Nervos Talk 社区简报

- 统计窗口: 2026-10-07 05:45:37 CST 到 2026-10-08 05:45:37 CST
- 生成时间: 2026-10-08 05:45:42 CST
- 话题数: 3
- 帖子数: 4
- 作者数: 4
- 总结模式: ai:openai-compatible

## 社区总结

## 今日发生了什么

从提供的帖子看，今天 Nervos Talk 整体更新量不大，共有三条讨论线，分别涉及 DAO Treasury、Kirea Finance 和 Pocket Node for iOS [S01, S02, S04]。讨论较集中的是 Kirea Finance：社区成员追问它和作者正在进行的 Tranfr Spark grant 如何并行 [S02]，项目方随后回应称 Tranfr 已推进中，并将在两周内完成并准备验收 [S03]。Nervos DAO Treasury 激活 Pre-RFC 继续细化 Optimistic Tally 的投票机制 [S01]，Pocket Node for iOS 帖则更新了 M1 付款为 1,968,504 CKB [S04]。

## 重点话题

- Nervos DAO Treasury 的 Pre-RFC 讨论继续，@phroi 感谢 @chenyukang 分享 Optimistic Tally，并概述提案是持有保证金的 Type ID cell，投票 cell 引用必须早于提案的 DAO 存款，权重按存款 capacity 计算，计数 cell 分片认证 YES 票 [S01]。
- Kirea Finance 的 DIS 帖收到质疑：社区成员问该提案如何与作者活跃的 Tranfr — Programmable Recovery for CKB Spark grant 并存，并指出 Tranfr 已收到初始付款，但 recovery path、SDK、前端和文档仍未完成 [S02]。
- SalmanDev 在同一帖回应称，Tranfr 是其 Spark program 下的第二个项目，已在进行中，将在两周内完全完成、收尾并准备验收，并以 Proven Execution Capacity 作为回应方向 [S03]。
- Pocket Node for iOS 帖更新 M1 付款信息：金额为 $2,500，按 0.00127 换算为 1,968,504 CKB，并附上链上交易链接 [S04]。
- 从这些帖子看，今天更新都来自已有话题的回复，更多是问答、机制细化和里程碑付款披露，而不是全新话题发布 [S01, S02, S03, S04]。

## 值得继续跟进

- Kirea Finance 与 Tranfr 的时间/资源冲突如何收尾：社区是否接受“两周内完成 Tranfr”的时间线，以及 Kirea 后续是否会补充执行安排，目前材料中还没有结论 [S02, S03]。
- Nervos DAO Treasury 的 Optimistic Tally 细节：当前材料只概述到提案、存款权重和 YES 票分片认证，后续机制如何继续细化仍需等论坛更新 [S01]。
- Pocket Node for iOS 的 M1 付款之后是否进入下一阶段：目前只有付款金额和交易链接，交付进展与下一步计划在材料中未展开 [S04]。

## 来源索引

- `S01` [Pre-RFC Discussion: Activating the Nervos DAO Treasury](https://talk.nervos.org/t/pre-rfc-discussion-activating-the-nervos-dao-treasury/10143/22) | phroi | 2026-10-08 05:00:14 CST | Thanks @chenyukang for sharing the Optimistic Tally!! An overview: A proposal is a Type ID cell holding a bond. Vote cells reference the voter’s DAO deposits, which must be older than the proposal. Weight is the deposits’ capacity. Counting cells certify YES votes in slices of...
- `S02` [[DIS] Hardening Kirea Finance (Native RWA Lending on CKB)](https://talk.nervos.org/t/dis-hardening-kirea-finance-native-rwa-lending-on-ckb/10809/2) | truthixify | 2026-10-07 21:12:45 CST | Can you clarify how this proposal fits alongside your active Tranfr — Programmable Recovery for CKB - #6 by tianji Spark grant? Tranfr has received its initial payment and still has the recovery path, SDK, frontend, and documentation outstanding, while Kirea is another solo...
- `S03` [[DIS] Hardening Kirea Finance (Native RWA Lending on CKB)](https://talk.nervos.org/t/dis-hardening-kirea-finance-native-rwa-lending-on-ckb/10809/3) | SalmanDev | 2026-10-07 22:08:03 CST | Thank you for raising this important question. To clarify: Tranfr Timeline: Tranfr (my second project under the Spark program) is already well underway and will be fully completed, wrapped up, and ready for acceptance within the next two weeks. Proven Execution Capacity: In...
- `S04` [[DIS] Pocket Node for iOS: a self-custody CKB light client for Apple and Identity/Signer for CCC web apps](https://talk.nervos.org/t/dis-pocket-node-for-ios-a-self-custody-ckb-light-client-for-apple-and-identity-signer-for-ccc-web-apps/10583/24) | zz_tovarishch | 2026-10-07 16:05:32 CST | M1 Payment $2,500/0.00127=1,968,504 CKB https://explorer.nervos.org/transaction/0xa86b7915ce458cd338aeb86e5a20c4ac4373c45420b798fb3537d4aad7936498

## 活跃话题

1. [Pre-RFC Discussion: Activating the Nervos DAO Treasury](https://talk.nervos.org/t/pre-rfc-discussion-activating-the-nervos-dao-treasury/10143) | 1 条近窗帖子 | 最新活动 2026-10-08 05:00:14 CST | tags: CKB, lang-en
2. [[DIS] Hardening Kirea Finance (Native RWA Lending on CKB)](https://talk.nervos.org/t/dis-hardening-kirea-finance-native-rwa-lending-on-ckb/10809) | 2 条近窗帖子 | 最新活动 2026-10-07 22:08:03 CST
3. [[DIS] Pocket Node for iOS: a self-custody CKB light client for Apple and Identity/Signer for CCC web apps](https://talk.nervos.org/t/dis-pocket-node-for-ios-a-self-custody-ckb-light-client-for-apple-and-identity-signer-for-ccc-web-apps/10583) | 1 条近窗帖子 | 最新活动 2026-10-07 16:05:32 CST | tags: Pocket-Node, light-client

## 最近帖子摘录

- 2026-10-08 05:00:14 CST | phroi | [Pre-RFC Discussion: Activating the Nervos DAO Treasury](https://talk.nervos.org/t/pre-rfc-discussion-activating-the-nervos-dao-treasury/10143/22) | Thanks @chenyukang for sharing the Optimistic Tally!! An overview: A proposal is a Type ID cell holding a bond. Vote cells reference the voter’s DAO deposits, which must be...
- 2026-10-07 22:08:03 CST | SalmanDev | [[DIS] Hardening Kirea Finance (Native RWA Lending on CKB)](https://talk.nervos.org/t/dis-hardening-kirea-finance-native-rwa-lending-on-ckb/10809/3) | Thank you for raising this important question. To clarify: Tranfr Timeline: Tranfr (my second project under the Spark program) is already well underway and will be fully...
- 2026-10-07 21:12:45 CST | truthixify | [[DIS] Hardening Kirea Finance (Native RWA Lending on CKB)](https://talk.nervos.org/t/dis-hardening-kirea-finance-native-rwa-lending-on-ckb/10809/2) | Can you clarify how this proposal fits alongside your active Tranfr — Programmable Recovery for CKB - #6 by tianji Spark grant? Tranfr has received its initial payment and still...
- 2026-10-07 16:05:32 CST | zz_tovarishch | [[DIS] Pocket Node for iOS: a self-custody CKB light client for Apple and Identity/Signer for CCC web apps](https://talk.nervos.org/t/dis-pocket-node-for-ios-a-self-custody-ckb-light-client-for-apple-and-identity-signer-for-ccc-web-apps/10583/24) | M1 Payment $2,500/0.00127=1,968,504 CKB https://explorer.nervos.org/transaction/0xa86b7915ce458cd338aeb86e5a20c4ac4373c45420b798fb3537d4aad7936498
