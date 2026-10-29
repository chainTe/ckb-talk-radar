# Nervos Talk 社区简报

- 统计窗口: 2026-10-29 05:30:36 CST 到 2026-10-30 05:30:36 CST
- 生成时间: 2026-10-30 05:30:42 CST
- 话题数: 6
- 帖子数: 16
- 作者数: 9
- 总结模式: ai:openai-compatible

## 社区总结

## 今日发生了什么

过去24小时，论坛讨论主要集中在 Fiber LSP 的容量压测、Kaze X CKB Unitour 的拨款支付节奏，以及 Spark Program 下的新申请上。[S02, S04, S10, S14] 有人把单个 Fiber LSP 在本地 CKB dev chain 上填到 11,496 个频道，但两个钱包之间的支付仍要 4 到 5 秒，和 350 个频道时一样。[S02] Kaze 团队与社区围绕“先拨款再执行”还是“完成 milestone 后付款”出现明显分歧。[S04, S05, S06, S08] 同时，CellFlow 申请 500 美元做 CCC 交易恢复 PoC，Light dApp Kit 申请 1,000 美元推进浏览器轻客户端的主网与 DAO 功能。[S10, S14]

## 重点话题

- **Fiber LSP 容量压测**：LusoCryptoLabs 报告单个 Fiber LSP 填到 11,496 个频道，使用的是当天测试网 LSP（Cellula 钱包背后那个）的 build 和配置，在本地 CKB dev chain 上完成。[S02] 支付延迟没有随频道数增加而变化，两个钱包之间仍为 4 到 5 秒，与 350 个频道时相同。[S02] ArthurZhang 认为 11.5k 频道很鼓舞，并建议下一步做跨独立 LSP 的持续并发支付测试，以更好判断真实世界扩展性。[S03]

- **Kaze Unitour 拨款时点争议**：Dorex45 表示 Metaforo 阶段后双方已对齐进入执行阶段，并理解 grant 会在一周内发放，因此来询问预计放款日期。[S04] zz_tovarishch 澄清获批 proposal 是三个各 1,000 美元的 milestone，不包含预付款，将按完成 milestone 后付款的流程走。[S05] Dorex45 则称资金是为了支持活动执行，不只是完成后报销。[S06] ebubedev 指出 proposal 没写活动前需要 payout，milestone 写的是 event completed。[S08] Dorex45 又强调 proposal 从未要求在活动完成后才收款，资金用于每个 Unitour 的筹划和执行。[S09]

- **Tranfr 的 Cheque 技术疑问**：有用户在 Tranfr 帖中对 Time Lock + Cheque 方案提问，指出按 RFC 0039 rule 1.b.ii，接收方 claim Cheque cell 时 capacity 必须回到发送方，因此 plain CKB 下接收方什么也拿不到。[S01] 该用户还表示已用测试确认，得到 error 8。[S01]

- **Spark Program：CellFlow 申请**：Dangbaty2004 提交 CellFlow 申请，请求 500 美元等值 CKB、周期 4 周，定位为 CKB Developer Infrastructure / PoC。[S10] 有回复认为它看起来有助于部署。[S11] 作者随后表示感谢。[S12] 另有一条同题帖子被作者删除。[S13]

- **Spark Program：Light dApp Kit 申请**：Akane 提交 Light dApp Kit 申请，请求 1,000 美元。[S14] 项目要基于已完成真实 testnet transfer 的浏览器轻客户端原型，提升稳定性、实现主网转账和完整 Nervos DAO 存取，并交付可复用 kit。[S14]

## 值得继续跟进

- Fiber 的下一步是跨独立 LSP 的持续并发支付测试，这被提出来用于判断真实世界扩展性。[S03] 单 LSP 11,496 频道下支付仍为 4 到 5 秒、与 350 频道相同，容量提升是否带来延迟收益还需继续观察。[S02]

- Kaze 拨款争议的关键是付款时点：社区按三个 milestone 完成后再付来理解流程，团队则强调活动执行前需要资金分配。[S05, S07, S08] 双方目前对 proposal 的理解仍不一致，后续要看能否就支付安排达成一致。[S06, S09]

- Tranfr 帖中的 Cheque 回收规则是一个明确技术约束：接收方 claim 时 capacity 回发送方，plain CKB 接收方拿不到，且测试出现 error 8。[S01] 后续需要看 Time Lock + Cheque 方案如何回应这一限制。[S01]

## 来源索引

- `S01` [Tranfr — Programmable Recovery for CKB](https://talk.nervos.org/t/tranfr-programmable-recovery-for-ckb/10644/20) | SalmanDev | 2026-10-30 05:20:25 CST | @Hanssen I have a question on the Time Lock + Cheque suggestion. Per RFC 0039 (rule 1.b.ii), when the receiver claims a Cheque cell, the cell’s capacity must go back to the sender, so for plain CKB the recipient would receive nothing. I also confirmed it with a test (error 8)....
- `S02` [One Fiber LSP, 11,496 channels](https://talk.nervos.org/t/one-fiber-lsp-11-496-channels/11068/1) | LusoCryptoLabs | 2026-10-29 22:08:16 CST | We filled one Fiber LSP to 11,496 channels on a local CKB dev chain, with the build and config that our testnet LSP, the one behind the Cellula wallet, ran that day. A payment between two wallets still took 4 to 5 s, as it did with 350 channels. The channel count turned out...
- `S03` [One Fiber LSP, 11,496 channels](https://talk.nervos.org/t/one-fiber-lsp-11-496-channels/11068/2) | ArthurZhang | 2026-10-30 03:36:47 CST | Great work! 11.5k channels on a single LSP is pretty encouraging, especially with the optimisations you found along the way. Would be interesting to see some sustained concurrent payment tests across separate LSPs next, just to get a better feel for real-world scaling. Also i...
- `S04` [[DIS] Kaze X CKB Unitour Continuation Proposal](https://talk.nervos.org/t/dis-kaze-x-ckb-unitour-continuation-proposal/10736/6) | Dorex45 | 2026-10-29 17:45:29 CST | GM Team Following the Metaforo stage, we aligned on moving into the execution phase, with the understanding that grant funds would be disbursed within one week. Since we’ve now reached that timeline, I wanted to kindly check in on the expected release date. We’re actively...
- `S05` [[DIS] Kaze X CKB Unitour Continuation Proposal](https://talk.nervos.org/t/dis-kaze-x-ckb-unitour-continuation-proposal/10736/7) | zz_tovarishch | 2026-10-29 23:13:50 CST | Hi @Dorex45, thanks for checking in. To clarify the payment schedule, the approved proposal lists three milestones at $1,000 each and does not include a request for an upfront payment. We will follow the milestone-based payment process: once a milestone is completed, please...
- `S06` [[DIS] Kaze X CKB Unitour Continuation Proposal](https://talk.nervos.org/t/dis-kaze-x-ckb-unitour-continuation-proposal/10736/8) | Dorex45 | 2026-10-30 00:48:27 CST | Thanks for the clarification. We understand that the grant is structured around three milestones of $1,000 each. However, our understanding is that the funding is intended to facilitate the execution of these activities, not simply reimburse them after completion. Each...
- `S07` [[DIS] Kaze X CKB Unitour Continuation Proposal](https://talk.nervos.org/t/dis-kaze-x-ckb-unitour-continuation-proposal/10736/9) | Dorex45 | 2026-10-30 00:58:10 CST | Event Planning & Execution Of Each Milestone from our end was bound to happen only after allocation of grant requested to run each particular milestone.
- `S08` [[DIS] Kaze X CKB Unitour Continuation Proposal](https://talk.nervos.org/t/dis-kaze-x-ckb-unitour-continuation-proposal/10736/10) | ebubedev | 2026-10-30 01:09:41 CST | the problem is you did not state that u needed the payout before the event, instead the milestone for event completed check your proposal and see
- `S09` [[DIS] Kaze X CKB Unitour Continuation Proposal](https://talk.nervos.org/t/dis-kaze-x-ckb-unitour-continuation-proposal/10736/11) | Dorex45 | 2026-10-30 01:31:59 CST | Our proposal clearly outlined a total grant request of $3,000, capped at $1,000 per Unitour. At no point did we request to receive the grant after the events had been completed. The funding is intended to facilitate the planning and execution of each Unitour, ensuring the...
- `S10` [Spark Program | CellFlow — Durable CCC Transaction Recovery PoC](https://talk.nervos.org/t/spark-program-cellflow-durable-ccc-transaction-recovery-poc/11067/1) | Dangbaty2004 | 2026-10-29 12:32:21 CST | Capture1906×878 147 KB Applicant: Dang Ba Ty Discord: tyforwork Email: dangbaty.work@gmail.com GitHub: tydeptrai21042004 (Dang Ba Ty) · GitHub Funding requested: $500 USD, payable in equivalent CKB Duration: 4 weeks Project type: CKB Developer Infrastructure / Proof of Concept...
- `S11` [Spark Program | CellFlow — Durable CCC Transaction Recovery PoC](https://talk.nervos.org/t/spark-program-cellflow-durable-ccc-transaction-recovery-poc/11067/2) | Tu_Tran_thanh | 2026-10-29 12:46:23 CST | it looks helpful to deploy.
- `S12` [Spark Program | CellFlow — Durable CCC Transaction Recovery PoC](https://talk.nervos.org/t/spark-program-cellflow-durable-ccc-transaction-recovery-poc/11067/3) | Dangbaty2004 | 2026-10-29 18:13:32 CST | Thanks you very much !!!
- `S13` [Spark Program | CellFlow — Durable CCC Transaction Recovery PoC](https://talk.nervos.org/t/spark-program-cellflow-durable-ccc-transaction-recovery-poc/11066/1) | Dangbaty2004 | 2026-10-29 12:23:59 CST | (topic deleted by author)
- `S14` [Spark Program | Light dApp Kit](https://talk.nervos.org/t/spark-program-light-dapp-kit/11062/1) | Akane | 2026-10-29 05:36:42 CST | 1. Project overview Purpose: Build on a browser light-client prototype that has completed a real testnet transfer to improve stability, implement mainnet transfers and full Nervos DAO deposits and withdrawals, and deliver a reusable kit for other dApps. Request: USD 1,000...

## 活跃话题

1. [Tranfr — Programmable Recovery for CKB](https://talk.nervos.org/t/tranfr-programmable-recovery-for-ckb/10644) | 1 条近窗帖子 | 最新活动 2026-10-30 05:20:25 CST | tags: In-Progress
2. [One Fiber LSP, 11,496 channels](https://talk.nervos.org/t/one-fiber-lsp-11-496-channels/11068) | 2 条近窗帖子 | 最新活动 2026-10-30 03:36:47 CST | tags: CKB, fiber
3. [[DIS] Kaze X CKB Unitour Continuation Proposal](https://talk.nervos.org/t/dis-kaze-x-ckb-unitour-continuation-proposal/10736) | 8 条近窗帖子 | 最新活动 2026-10-30 03:25:30 CST | tags: CKB, CKB-VM, Grant, Nervos-项目动态, appchain, dapp
4. [Spark Program | CellFlow — Durable CCC Transaction Recovery PoC](https://talk.nervos.org/t/spark-program-cellflow-durable-ccc-transaction-recovery-poc/11067) | 3 条近窗帖子 | 最新活动 2026-10-29 18:13:32 CST
5. [Spark Program | CellFlow — Durable CCC Transaction Recovery PoC](https://talk.nervos.org/t/spark-program-cellflow-durable-ccc-transaction-recovery-poc/11066) | 1 条近窗帖子 | 最新活动 2026-10-29 12:23:59 CST
6. [Spark Program | Light dApp Kit](https://talk.nervos.org/t/spark-program-light-dapp-kit/11062) | 1 条近窗帖子 | 最新活动 2026-10-29 05:36:42 CST

## 最近帖子摘录

- 2026-10-30 05:20:25 CST | SalmanDev | [Tranfr — Programmable Recovery for CKB](https://talk.nervos.org/t/tranfr-programmable-recovery-for-ckb/10644/20) | @Hanssen I have a question on the Time Lock + Cheque suggestion. Per RFC 0039 (rule 1.b.ii), when the receiver claims a Cheque cell, the cell’s capacity must go back to the...
- 2026-10-30 03:36:47 CST | ArthurZhang | [One Fiber LSP, 11,496 channels](https://talk.nervos.org/t/one-fiber-lsp-11-496-channels/11068/2) | Great work! 11.5k channels on a single LSP is pretty encouraging, especially with the optimisations you found along the way. Would be interesting to see some sustained...
- 2026-10-30 03:25:30 CST | ebubedev | [[DIS] Kaze X CKB Unitour Continuation Proposal](https://talk.nervos.org/t/dis-kaze-x-ckb-unitour-continuation-proposal/10736/13) | check here Dorex45: . Detailed Deliverables & Milestones Milestone University Deliverable(s) ETA Budget Milestone 1 Machakos University, Main Campus 3-hour tour: teaching, live...
- 2026-10-30 01:40:52 CST | Dorex45 | [[DIS] Kaze X CKB Unitour Continuation Proposal](https://talk.nervos.org/t/dis-kaze-x-ckb-unitour-continuation-proposal/10736/12) | For Reference on Section 2. Summary The Proposal Clearly Requests a Grant of $3000 to run the Unitours.
- 2026-10-30 01:31:59 CST | Dorex45 | [[DIS] Kaze X CKB Unitour Continuation Proposal](https://talk.nervos.org/t/dis-kaze-x-ckb-unitour-continuation-proposal/10736/11) | Our proposal clearly outlined a total grant request of $3,000, capped at $1,000 per Unitour. At no point did we request to receive the grant after the events had been completed....
- 2026-10-30 01:09:41 CST | ebubedev | [[DIS] Kaze X CKB Unitour Continuation Proposal](https://talk.nervos.org/t/dis-kaze-x-ckb-unitour-continuation-proposal/10736/10) | the problem is you did not state that u needed the payout before the event, instead the milestone for event completed check your proposal and see
- 2026-10-30 00:58:10 CST | Dorex45 | [[DIS] Kaze X CKB Unitour Continuation Proposal](https://talk.nervos.org/t/dis-kaze-x-ckb-unitour-continuation-proposal/10736/9) | Event Planning & Execution Of Each Milestone from our end was bound to happen only after allocation of grant requested to run each particular milestone.
- 2026-10-30 00:48:27 CST | Dorex45 | [[DIS] Kaze X CKB Unitour Continuation Proposal](https://talk.nervos.org/t/dis-kaze-x-ckb-unitour-continuation-proposal/10736/8) | Thanks for the clarification. We understand that the grant is structured around three milestones of $1,000 each. However, our understanding is that the funding is intended to...
- 2026-10-29 23:13:50 CST | zz_tovarishch | [[DIS] Kaze X CKB Unitour Continuation Proposal](https://talk.nervos.org/t/dis-kaze-x-ckb-unitour-continuation-proposal/10736/7) | Hi @Dorex45, thanks for checking in. To clarify the payment schedule, the approved proposal lists three milestones at $1,000 each and does not include a request for an upfront...
- 2026-10-29 22:08:16 CST | LusoCryptoLabs | [One Fiber LSP, 11,496 channels](https://talk.nervos.org/t/one-fiber-lsp-11-496-channels/11068/1) | We filled one Fiber LSP to 11,496 channels on a local CKB dev chain, with the build and config that our testnet LSP, the one behind the Cellula wallet, ran that day. A payment...
- 2026-10-29 18:13:32 CST | Dangbaty2004 | [Spark Program | CellFlow — Durable CCC Transaction Recovery PoC](https://talk.nervos.org/t/spark-program-cellflow-durable-ccc-transaction-recovery-poc/11067/3) | Thanks you very much !!!
- 2026-10-29 17:45:29 CST | Dorex45 | [[DIS] Kaze X CKB Unitour Continuation Proposal](https://talk.nervos.org/t/dis-kaze-x-ckb-unitour-continuation-proposal/10736/6) | GM Team Following the Metaforo stage, we aligned on moving into the execution phase, with the understanding that grant funds would be disbursed within one week. Since we’ve now...
- 2026-10-29 12:46:23 CST | Tu_Tran_thanh | [Spark Program | CellFlow — Durable CCC Transaction Recovery PoC](https://talk.nervos.org/t/spark-program-cellflow-durable-ccc-transaction-recovery-poc/11067/2) | it looks helpful to deploy.
- 2026-10-29 12:32:21 CST | Dangbaty2004 | [Spark Program | CellFlow — Durable CCC Transaction Recovery PoC](https://talk.nervos.org/t/spark-program-cellflow-durable-ccc-transaction-recovery-poc/11067/1) | Capture1906×878 147 KB Applicant: Dang Ba Ty Discord: tyforwork Email: dangbaty.work@gmail.com GitHub: tydeptrai21042004 (Dang Ba Ty) · GitHub Funding requested: $500 USD,...
- 2026-10-29 12:23:59 CST | Dangbaty2004 | [Spark Program | CellFlow — Durable CCC Transaction Recovery PoC](https://talk.nervos.org/t/spark-program-cellflow-durable-ccc-transaction-recovery-poc/11066/1) | (topic deleted by author)
- 2026-10-29 05:36:42 CST | Akane | [Spark Program | Light dApp Kit](https://talk.nervos.org/t/spark-program-light-dapp-kit/11062/1) | 1. Project overview Purpose: Build on a browser light-client prototype that has completed a real testnet transfer to improve stability, implement mainnet transfers and full...
