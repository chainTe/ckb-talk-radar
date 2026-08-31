# Nervos Talk 社区简报

- 统计窗口: 2026-08-31 05:43:44 CST 到 2026-09-01 05:43:44 CST
- 生成时间: 2026-09-01 05:43:53 CST
- 话题数: 7
- 帖子数: 9
- 作者数: 8
- 总结模式: ai:openai-compatible

## 社区总结

## 今日发生了什么

今天论坛的主旋律是 Fiber 生态与共识机制讨论：Fiber 基础设施黑客松“Gone in 60ms”正式公布最终结果，社区反响热烈 [S07, S08]。Rosen Bridge 的 CKB 集成审查继续推进，新合约提交后审查者提醒先理清版本对应关系 [S03]。中文社区这边，基于 CKB L1 的隐私订单簿项目更新周报，提出用 VRF 替代 VDF 的共识设计调整 [S04]。

## 重点话题

- **Fiber 黑客松结果落地**：neon.bit 发布了“Gone in 60ms: Fiber Network Infrastructure Hackathon”的最终结果，该黑客松在 2026 年 7 月期间举办 [S07]，Ajay 等社区成员向获奖者表示祝贺 [S08]。

- **Rosen Bridge 审查进入新阶段**：tianji 指出此前评论 #147–#149 对应的是 3 月 9 日修订版（6312fdf9），而 8 月 31 日的新合约（b62254b2）可能修正、澄清或取代旧版，审查时间线需要先理清 [S03]。phroi 引用 tianji 的观点称，删除 ACP 解决了共享可变状态与并发问题 [S02]。

- **Proof of Buy 方案调整**：Lawliet_Chan 在周报中表示补充了 proof of buy 细节，考虑用 VRF 代替 VDF [S04]；具体机制是用 VRF 输出与 L1 支付金额联合计算 goal 值（goal = f(L1_payment, vrf_output)），避免资金雄厚方垄断出块权 [S05]。

- **fiber-payjoin-kit 完成主网测量**：ILE_LABS 表示团队对 CKB 主网数据做了更深测量，在 6.5 年链历史中仅识别出 8 笔真正协作交易 [S09]，这一数据对提案的影响值得关注。

- **Spark Program 仍在推进**：项目方回应社区询问，表示项目仍在继续，只是主网数据收集与分析需要更多时间，详细进度报告会在数据充分后发布 [S06]。

## 值得继续跟进

- **Rosen Bridge 新合约审查**：新提交的 b62254b2 与 3 月 9 日版本的具体差异，以及旧注释哪些仍然有效，需要审查者进一步澄清 [S03]。

- **Proof of Buy 从 VDF 转向 VRF**：新的加权公式已提出，但还没有测试或模拟数据，后续是否有实现与验证值得关注 [S04, S05]。

- **Spark Program 正式报告**：项目方表示主网数据还需更多时间，社区都在等这份详细进度报告，留意后续发布 [S06]。

## 来源索引

- `S01` [[Fiber] Opticrum Desktop: A Fiber GUI with in-bound liquidity capacity](https://talk.nervos.org/t/fiber-opticrum-desktop-a-fiber-gui-with-in-bound-liquidity-capacity/10669/3) | Ckroamer | 2026-08-31 23:35:45 CST | 谢谢你贴了我之前写的服务端的文档
- `S02` [[DIS] CKB Integration for Rosen Bridge](https://talk.nervos.org/t/dis-ckb-integration-for-rosen-bridge/9756/150) | phroi | 2026-08-31 11:18:45 CST | tianji: Dropping ACP removes the shared mutable-state and concurrency surface I was referring to. One user-created cell per request, signed metadata, and confirmed-only custody inputs are all correct moves. The original CKB-local shared-state problem is resolved. Correct....
- `S03` [[DIS] CKB Integration for Rosen Bridge](https://talk.nervos.org/t/dis-ckb-integration-for-rosen-bridge/9756/151) | tianji | 2026-08-31 21:14:15 CST | Re: #150 — Frozen-revision review Appreciate the update. One chronology point needs to be fixed first: comments #147–#149 (Aug 18–23) referred to the Mar 9 revision (6312fdf9…). The new contract (commit b62254b2…, Aug 31) may legitimately fix, clarify, supersede, or make parts...
- `S04` [[DIS] Decentralized privacy order-book appchain based on CKB L1 - 2026.phase-1](https://talk.nervos.org/t/dis-decentralized-privacy-order-book-appchain-based-on-ckb-l1-2026-phase-1/10015/42) | Lawliet_Chan | 2026-08-31 15:30:48 CST | 周报 2026.8.31 补充 proof of buy细节，考虑使用VRF代替VDF
- `S05` [Proof of Buy，一种专为Layer1设计的Layer2共识](https://talk.nervos.org/t/proof-of-buy-layer1-layer2/9752/30) | Lawliet_Chan | 2026-08-31 15:26:29 CST | VRF加权 为了防止富者（比如上述的L2项目方自己）垄断出块权和攻击网络，我们需要使用随机数对L1支付金额进行加权，以让出块权的选举不能单纯只靠支付金额大小。 我们引入VRF，并让VRF的输出结果与支付的L1 token金额结合在一起进行计算，我们用数学式来表达为： goal = f(L1_payment, vrf_output) 每个出块节点想竞争出块权的话必须在出块时广播自己的goal 并连同L2 block header一起 上传到L1 block，只有goal最大的才会成为该高度的区块。 fork choice...
- `S06` [Spark Program | CKB Wallet Behaviour Intelligence](https://talk.nervos.org/t/spark-program-ckb-wallet-behaviour-intelligence/10338/21) | mulinya | 2026-08-31 12:54:24 CST | Hello xingtianchunyan, Thank you for checking in. The project is still progressing. More time has been needed for mainnet data collection and analysis to ensure we have enough meaningful data before reporting the results. The work is ongoing, and I’ll share a detailed progress...
- `S07` [Gone in 60ms: Fiber Network Infrastructure Hackathon Results](https://talk.nervos.org/t/gone-in-60ms-fiber-network-infrastructure-hackathon-results/10671/1) | neon.bit | 2026-08-31 07:11:26 CST | Gone in 60ms: Fiber Network Infrastructure Hackathon Results After weeks of building and careful deliberation, we’re ready to share the final results of the Gone in 60ms: Fiber Network Infrastructure Hackathon! The hackathon ran through July 2026, with builders tasked with...
- `S08` [Gone in 60ms: Fiber Network Infrastructure Hackathon Results](https://talk.nervos.org/t/gone-in-60ms-fiber-network-infrastructure-hackathon-results/10671/2) | Ajay | 2026-08-31 11:15:56 CST | Congratulations to all the winners
- `S09` [[DIS] fiber-payjoin-kit: Collaborative Channel Funding Privacy for the Nervos Fiber Network RES](https://talk.nervos.org/t/dis-fiber-payjoin-kit-collaborative-channel-funding-privacy-for-the-nervos-fiber-network-res/10604/5) | ILE_LABS | 2026-08-31 06:20:55 CST | Thank you all for your attention to details on our proposal. Since posting the tiered restructure, our team completed a deeper measurement pass against CKB mainnet data. We identified only 8 genuinely collaborative transactions across 6.5 years of chain history, and 98 Fiber...

## 活跃话题

1. [[Fiber] Opticrum Desktop: A Fiber GUI with in-bound liquidity capacity](https://talk.nervos.org/t/fiber-opticrum-desktop-a-fiber-gui-with-in-bound-liquidity-capacity/10669) | 1 条近窗帖子 | 最新活动 2026-08-31 23:35:45 CST
2. [[DIS] CKB Integration for Rosen Bridge](https://talk.nervos.org/t/dis-ckb-integration-for-rosen-bridge/9756) | 2 条近窗帖子 | 最新活动 2026-08-31 21:14:15 CST
3. [[DIS] Decentralized privacy order-book appchain based on CKB L1 - 2026.phase-1](https://talk.nervos.org/t/dis-decentralized-privacy-order-book-appchain-based-on-ckb-l1-2026-phase-1/10015) | 1 条近窗帖子 | 最新活动 2026-08-31 15:30:48 CST | tags: appchain
4. [Proof of Buy，一种专为Layer1设计的Layer2共识](https://talk.nervos.org/t/proof-of-buy-layer1-layer2/9752) | 1 条近窗帖子 | 最新活动 2026-08-31 15:26:29 CST | tags: lang-zh, 共识协议
5. [Spark Program | CKB Wallet Behaviour Intelligence](https://talk.nervos.org/t/spark-program-ckb-wallet-behaviour-intelligence/10338) | 1 条近窗帖子 | 最新活动 2026-08-31 12:54:24 CST | tags: In-Progress
6. [Gone in 60ms: Fiber Network Infrastructure Hackathon Results](https://talk.nervos.org/t/gone-in-60ms-fiber-network-infrastructure-hackathon-results/10671) | 2 条近窗帖子 | 最新活动 2026-08-31 11:15:56 CST | tags: CKB, Hackathon, fiber
7. [[DIS] fiber-payjoin-kit: Collaborative Channel Funding Privacy for the Nervos Fiber Network RES](https://talk.nervos.org/t/dis-fiber-payjoin-kit-collaborative-channel-funding-privacy-for-the-nervos-fiber-network-res/10604) | 1 条近窗帖子 | 最新活动 2026-08-31 06:20:55 CST

## 最近帖子摘录

- 2026-08-31 23:35:45 CST | Ckroamer | [[Fiber] Opticrum Desktop: A Fiber GUI with in-bound liquidity capacity](https://talk.nervos.org/t/fiber-opticrum-desktop-a-fiber-gui-with-in-bound-liquidity-capacity/10669/3) | 谢谢你贴了我之前写的服务端的文档
- 2026-08-31 21:14:15 CST | tianji | [[DIS] CKB Integration for Rosen Bridge](https://talk.nervos.org/t/dis-ckb-integration-for-rosen-bridge/9756/151) | Re: #150 — Frozen-revision review Appreciate the update. One chronology point needs to be fixed first: comments #147–#149 (Aug 18–23) referred to the Mar 9 revision (6312fdf9…)....
- 2026-08-31 15:30:48 CST | Lawliet_Chan | [[DIS] Decentralized privacy order-book appchain based on CKB L1 - 2026.phase-1](https://talk.nervos.org/t/dis-decentralized-privacy-order-book-appchain-based-on-ckb-l1-2026-phase-1/10015/42) | 周报 2026.8.31 补充 proof of buy细节，考虑使用VRF代替VDF
- 2026-08-31 15:26:29 CST | Lawliet_Chan | [Proof of Buy，一种专为Layer1设计的Layer2共识](https://talk.nervos.org/t/proof-of-buy-layer1-layer2/9752/30) | VRF加权 为了防止富者（比如上述的L2项目方自己）垄断出块权和攻击网络，我们需要使用随机数对L1支付金额进行加权，以让出块权的选举不能单纯只靠支付金额大小。 我们引入VRF，并让VRF的输出结果与支付的L1 token金额结合在一起进行计算，我们用数学式来表达为： goal = f(L1_payment, vrf_output)...
- 2026-08-31 12:54:24 CST | mulinya | [Spark Program | CKB Wallet Behaviour Intelligence](https://talk.nervos.org/t/spark-program-ckb-wallet-behaviour-intelligence/10338/21) | Hello xingtianchunyan, Thank you for checking in. The project is still progressing. More time has been needed for mainnet data collection and analysis to ensure we have enough...
- 2026-08-31 11:18:45 CST | phroi | [[DIS] CKB Integration for Rosen Bridge](https://talk.nervos.org/t/dis-ckb-integration-for-rosen-bridge/9756/150) | tianji: Dropping ACP removes the shared mutable-state and concurrency surface I was referring to. One user-created cell per request, signed metadata, and confirmed-only custody...
- 2026-08-31 11:15:56 CST | Ajay | [Gone in 60ms: Fiber Network Infrastructure Hackathon Results](https://talk.nervos.org/t/gone-in-60ms-fiber-network-infrastructure-hackathon-results/10671/2) | Congratulations to all the winners
- 2026-08-31 07:11:26 CST | neon.bit | [Gone in 60ms: Fiber Network Infrastructure Hackathon Results](https://talk.nervos.org/t/gone-in-60ms-fiber-network-infrastructure-hackathon-results/10671/1) | Gone in 60ms: Fiber Network Infrastructure Hackathon Results After weeks of building and careful deliberation, we’re ready to share the final results of the Gone in 60ms: Fiber...
- 2026-08-31 06:20:55 CST | ILE_LABS | [[DIS] fiber-payjoin-kit: Collaborative Channel Funding Privacy for the Nervos Fiber Network RES](https://talk.nervos.org/t/dis-fiber-payjoin-kit-collaborative-channel-funding-privacy-for-the-nervos-fiber-network-res/10604/5) | Thank you all for your attention to details on our proposal. Since posting the tiered restructure, our team completed a deeper measurement pass against CKB mainnet data. We...
