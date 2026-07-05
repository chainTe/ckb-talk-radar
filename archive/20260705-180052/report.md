# Nervos Talk 社区简报

- 统计窗口: 2026-07-05 02:00:52 CST 到 2026-07-06 02:00:52 CST
- 生成时间: 2026-07-06 02:00:58 CST
- 话题数: 6
- 帖子数: 8
- 作者数: 6
- 总结模式: ai:openrouter

## 社区总结

## 今日发生了什么

今天 Nervos Talk 论坛以 Fiber 生态建设为主线，多个项目同时推进：桌面端钱包完成关键里程碑，非洲移动支付项目 Dular 澄清了架构争议，隐私订单簿项目继续引入闪电网络共识机制。[S01, S04, S06]

## 重点话题

- **Fiber Desktop v1 完成 Milestone 2**：ebubedev 宣布钱包、节点通道和网络功能从占位界面变为完全接入官方 fnn 节点的可用模块，桌面重建项目取得实质进展。[S06]

- **Dular 回应架构质疑并解释延迟**：项目负责人 duongja 明确当前阶段采用运营商托管模式，普通移动/USSD 用户无需独立运行 Fiber 节点；同时坦承周报延迟是因为下一里程碑依赖非洲当地生产级 USSD 接入，正在解决中。[S03, S04]

- **隐私订单簿引入 Fiber 闪电网络**：Lawliet_Chan 的 Invisibook 项目继续实现"proof of buy"机制，尝试通过 Fiber 闪电网络协助共识。[S01]

- **Luxvoid 跨链方案遭技术性质疑**：有回复指出该协议仅能验证比特币交易在 CKB 上的合法性，但并未真正在 BTC 链上完成资产转移，"桥接"说法存疑。[S02]

- **Fiber Python SDK 明确托管支付设计**：SalmanDev 解释 SDK 将封装 settle_invoice 接口，支持"hold-invoice"模式，使 PactAgent 等场景的里程碑释放无需第三方托管资金。[S07]

## 值得继续跟进

- Dular 的生产级 USSD 接入能否落实，将直接影响其下一里程碑交付和非洲试点可信度。[S04]

- Luxvoid 的 BTC→CKB 桥接方案需要回应"只验证、不转移"的技术质疑，否则 DAO 支持申请可能面临更多挑战。[S02]

- Fiber 桌面端 Milestone 2 虽已完成功能接线，但实际节点稳定性与用户体验仍需观察后续测试反馈。[S06]

## 来源索引

- `S01` [[DIS] Decentralized privacy order-book appchain based on CKB L1 - 2026.phase-1](https://talk.nervos.org/t/dis-decentralized-privacy-order-book-appchain-based-on-ckb-l1-2026-phase-1/10015/34) | Lawliet_Chan | 2026-07-05 23:06:32 CST | 周报 2026.7.5 继续实现proof of buy，尝试引入fiber闪电网络协助共识： define proof of buy by Lawliet-Chan · Pull Request #8 · invisibook-lab/invisibook · GitHub
- `S02` [[DIS] Luxvoid Protocol: The First Working BTC→CKB→EVM Pipeline — Seeking DAO Support/collab for Production Scaling](https://talk.nervos.org/t/dis-luxvoid-protocol-the-first-working-btc-ckb-evm-pipeline-seeking-dao-support-collab-for-production-scaling/10400/18) | Crybaby | 2026-07-05 21:46:50 CST | Sorry, it’s just verifying a Bitcoin transaction on CKB, letting CKB know the transaction is legal on BTC, but this isn’t the way to bridge assets from BTC to CKB, because nothing changed on BTC blockchain. Otherwise, assuming the Bitcoin transaction you mentioned here is...
- `S03` [Spark Program | Dular](https://talk.nervos.org/t/spark-program-dular/10212/21) | duongja | 2026-07-05 18:42:45 CST | Hi @Hanssen, thanks for pushing on this. I agree this needs to be very explicit. For the current milestone scope, Dular is not trying to make every mobile/USSD pilot user run an independent Fiber node. The current architecture is operator-managed, because the target users are...
- `S04` [Spark Program | Dular](https://talk.nervos.org/t/spark-program-dular/10212/22) | duongja | 2026-07-05 18:51:24 CST | Hello, thank you for the reminder. Apologies for the delay in weekly updates. The main reason is that our next milestone depends heavily on production USSD access, and we have been trying to resolve that before giving a substantive update. Our original plan was to use Africa’s...
- `S05` [Spark Program | Dular](https://talk.nervos.org/t/spark-program-dular/10212/23) | ebubedev | 2026-07-05 21:04:24 CST | Hi @duongja — thanks for the architecture clarifications in post #15. I reviewed the public repo to understand how Fiber fits in practice, and I have a few follow-up questions on the final milestone scope. 1. How do users access and spend funds without running their own Fiber...
- `S06` [[DIS] Fiber Desktop v1 ground-up rebuild and launch — fnn desktop app](https://talk.nervos.org/t/dis-fiber-desktop-v1-ground-up-rebuild-and-launch-fnn-desktop-app/10317/19) | ebubedev | 2026-07-05 20:14:38 CST | Milestone 2 complete: Wallet, Peers & Channels are live Hi everyone, Following up on the Milestone 1 update — Milestone 2 is done. Since that post, the Wallet, Channels, and Network sections moved from placeholders to fully wired screens backed by the official fnn node. This...
- `S07` [[DIS] Fiber Python SDK — Native Python Library for Fiber Network Payments](https://talk.nervos.org/t/dis-fiber-python-sdk-native-python-library-for-fiber-network-payments/10462/2) | SalmanDev | 2026-07-05 07:11:38 CST | One design decision worth clarifying: The SDK will wrap settle_invoice, which enables hold-invoice patterns — pay now, release on condition. This is what makes escrow flows like PactAgent’s milestone releases possible without a third party custodying funds.
- `S08` [[DIS] Mobile-Ready CKB Light Client (Pocket Node) for Android](https://talk.nervos.org/t/dis-mobile-ready-ckb-light-client-pocket-node-for-android/9879/68) | Jnr6 | 2026-07-05 03:56:29 CST | Good question, and you have actually put your finger on exactly what is happening. Both behaviors come from the same root cause, and it was just written up in detail by another user: Funds become invisible (balance 0 + large negative outflow) when mnemonic was previously used...

## 活跃话题

1. [[DIS] Decentralized privacy order-book appchain based on CKB L1 - 2026.phase-1](https://talk.nervos.org/t/dis-decentralized-privacy-order-book-appchain-based-on-ckb-l1-2026-phase-1/10015) | 1 条近窗帖子 | 最新活动 2026-07-05 23:06:32 CST | tags: appchain
2. [[DIS] Luxvoid Protocol: The First Working BTC→CKB→EVM Pipeline — Seeking DAO Support/collab for Production Scaling](https://talk.nervos.org/t/dis-luxvoid-protocol-the-first-working-btc-ckb-evm-pipeline-seeking-dao-support-collab-for-production-scaling/10400) | 1 条近窗帖子 | 最新活动 2026-07-05 21:46:50 CST | tags: CKB, RGBpp, testnet
3. [Spark Program | Dular](https://talk.nervos.org/t/spark-program-dular/10212) | 3 条近窗帖子 | 最新活动 2026-07-05 21:04:24 CST | tags: In-Progress, Spark-Program
4. [[DIS] Fiber Desktop v1 ground-up rebuild and launch — fnn desktop app](https://talk.nervos.org/t/dis-fiber-desktop-v1-ground-up-rebuild-and-launch-fnn-desktop-app/10317) | 1 条近窗帖子 | 最新活动 2026-07-05 20:14:38 CST | tags: fiber
5. [[DIS] Fiber Python SDK — Native Python Library for Fiber Network Payments](https://talk.nervos.org/t/dis-fiber-python-sdk-native-python-library-for-fiber-network-payments/10462) | 1 条近窗帖子 | 最新活动 2026-07-05 07:11:38 CST | tags: fiber
6. [[DIS] Mobile-Ready CKB Light Client (Pocket Node) for Android](https://talk.nervos.org/t/dis-mobile-ready-ckb-light-client-pocket-node-for-android/9879) | 1 条近窗帖子 | 最新活动 2026-07-05 03:56:29 CST | tags: CKB, light-client

## 最近帖子摘录

- 2026-07-05 23:06:32 CST | Lawliet_Chan | [[DIS] Decentralized privacy order-book appchain based on CKB L1 - 2026.phase-1](https://talk.nervos.org/t/dis-decentralized-privacy-order-book-appchain-based-on-ckb-l1-2026-phase-1/10015/34) | 周报 2026.7.5 继续实现proof of buy，尝试引入fiber闪电网络协助共识： define proof of buy by Lawliet-Chan · Pull Request #8 · invisibook-lab/invisibook · GitHub
- 2026-07-05 21:46:50 CST | Crybaby | [[DIS] Luxvoid Protocol: The First Working BTC→CKB→EVM Pipeline — Seeking DAO Support/collab for Production Scaling](https://talk.nervos.org/t/dis-luxvoid-protocol-the-first-working-btc-ckb-evm-pipeline-seeking-dao-support-collab-for-production-scaling/10400/18) | Sorry, it’s just verifying a Bitcoin transaction on CKB, letting CKB know the transaction is legal on BTC, but this isn’t the way to bridge assets from BTC to CKB, because...
- 2026-07-05 21:04:24 CST | ebubedev | [Spark Program | Dular](https://talk.nervos.org/t/spark-program-dular/10212/23) | Hi @duongja — thanks for the architecture clarifications in post #15. I reviewed the public repo to understand how Fiber fits in practice, and I have a few follow-up questions...
- 2026-07-05 20:14:38 CST | ebubedev | [[DIS] Fiber Desktop v1 ground-up rebuild and launch — fnn desktop app](https://talk.nervos.org/t/dis-fiber-desktop-v1-ground-up-rebuild-and-launch-fnn-desktop-app/10317/19) | Milestone 2 complete: Wallet, Peers & Channels are live Hi everyone, Following up on the Milestone 1 update — Milestone 2 is done. Since that post, the Wallet, Channels, and...
- 2026-07-05 18:51:24 CST | duongja | [Spark Program | Dular](https://talk.nervos.org/t/spark-program-dular/10212/22) | Hello, thank you for the reminder. Apologies for the delay in weekly updates. The main reason is that our next milestone depends heavily on production USSD access, and we have...
- 2026-07-05 18:42:45 CST | duongja | [Spark Program | Dular](https://talk.nervos.org/t/spark-program-dular/10212/21) | Hi @Hanssen, thanks for pushing on this. I agree this needs to be very explicit. For the current milestone scope, Dular is not trying to make every mobile/USSD pilot user run an...
- 2026-07-05 07:11:38 CST | SalmanDev | [[DIS] Fiber Python SDK — Native Python Library for Fiber Network Payments](https://talk.nervos.org/t/dis-fiber-python-sdk-native-python-library-for-fiber-network-payments/10462/2) | One design decision worth clarifying: The SDK will wrap settle_invoice, which enables hold-invoice patterns — pay now, release on condition. This is what makes escrow flows like...
- 2026-07-05 03:56:29 CST | Jnr6 | [[DIS] Mobile-Ready CKB Light Client (Pocket Node) for Android](https://talk.nervos.org/t/dis-mobile-ready-ckb-light-client-pocket-node-for-android/9879/68) | Good question, and you have actually put your finger on exactly what is happening. Both behaviors come from the same root cause, and it was just written up in detail by another...
