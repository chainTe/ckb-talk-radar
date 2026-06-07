# Nervos Talk 社区简报

- 统计窗口: 2026-06-07 02:02:25 CST 到 2026-06-08 02:02:25 CST
- 生成时间: 2026-06-08 02:02:30 CST
- 话题数: 6
- 帖子数: 7
- 作者数: 6
- 总结模式: ai:openrouter

## 社区总结

## 今日发生了什么

Fiber Desktop v1 重建提案的 DAO 投票正在进行中，目前参与度约 40%，距离周三截止还需约 900 万 CKB 才能达到法定人数 [S01, S06]。同时，社区成员 IrisNeko 发起招募，邀请 10-15 位社区成员参与 Nervos Brain 问答 Agent 的最终验收测试 [S03]。

## 重点话题

- **Fiber Desktop 投票冲刺**：ebubedev 更新称 v1 重建提案已在 Metaforo 开启投票，当前投票量约 597 万 CKB，距离 1500 万的法定人数还差约 900 万，"赞成"和"反对"均计入法定人数，呼吁社区参与 [S06]。该原型帖此前已展示了中继、通道和支付等用户需求，反馈直接塑造了 v1 计划 [S01]。

- **Nervos Brain 招募测试者**：IrisNeko 发起招募，计划邀请 10-15 位社区成员对 Nervos Brain 问答 Agent 进行最终验收测试，覆盖 CCC、CKB、Fiber、Spore、xUDT、SDK 等专业领域，面向开发者和普通 Web3 用户两类人群 [S03]。

- **Fiber 流动性方案探讨**：Ckroamer 调研闪电网络生态项目 Amboss 后，提出 CKB 可让 Fiber 拥有更好的"类 Amboss"解决方案，分析了 JIT 通道等入向流动性解决思路，将闪电网络的协议限制转化为流动性市场机会 [S04]。

- **DIS 隐私订单簿项目进展**：Lawliet_Chan 更新周报，团队本周开会并讨论重新撰写 invisibook 论文大纲，准备投递 NDSS Fall Cycle [S05]。

- **CKBadger 概念澄清**：janx 回应社区提问，解释 CKBadger 中"Pure CKB"指完全上链、零链下依赖；"Decentralized Mixture"指部分上链、带有 IPFS 等去中心化链下依赖；"Centralized Mixture"则指其他中心化混合模式 [S07]。

## 值得继续跟进

- **Fiber Desktop 投票结果**：周三投票截止前能否达到 1500 万 CKB 法定人数将直接决定 v1 重建能否获得资助，需关注最后两天的社区动员情况 [S06]。

- **Nervos Brain 测试反馈**：验收测试的参与者质量和反馈深度将影响该问答 Agent 上线后的实际可用性，尤其是 Fiber、Spore 等复杂技术问题的回答准确度 [S03]。

- **DIS 论文投递结果**：invisibook 论文若能在 NDSS Fall Cycle 中获得学术认可，将为 CKB L1 隐私订单簿方案增加技术公信力 [S05]。

## 来源索引

- `S01` [Fiber Desktop — run Fiber (FNN) on your laptop without the “public node” headache](https://talk.nervos.org/t/fiber-desktop-run-fiber-fnn-on-your-laptop-without-the-public-node-headache/10247/9) | ebubedev | 2026-06-07 09:00:01 CST | DAO vote open — closes Wednesday Quick update: the v1 rebuild proposal is in Metaforo voting until Wednesday. This prototype thread showed the demand — users on relays, channels, and payments; feedback that shaped the v1 plan. The grant funds the real product: new UX, cross-...
- `S02` [Fiber Desktop — run Fiber (FNN) on your laptop without the “public node” headache](https://talk.nervos.org/t/fiber-desktop-run-fiber-fnn-on-your-laptop-without-the-public-node-headache/10247/10) | knmo | 2026-06-07 23:06:48 CST | OT: Delegated DAO voting could become an important democratic mechanism if @CKBA plays a decisive role in its implementation. CKB can remain locked for years (and soon decades) without requiring active management by its owners. If the “stake”—the weight of my DAO-staked,...
- `S03` [招募 Nervos 社区成员参与 Nervos Brain最终验收测试](https://talk.nervos.org/t/nervos-nervos-brain/10354/1) | IrisNeko | 2026-06-07 22:58:35 CST | 大家好，我这边准备对 Nervos Brain做最终验收测试，想邀请 10-15 位 Nervos 社区成员一起帮忙试用和反馈。 Nervos Brain 是一个面向 CKB / Nervos 生态的问答Agent，会基于官方文档、Nervos Talk、GitHub docs/code 等资料进行检索和回答。 这次希望招募几类测试成员： 3-5 位熟悉 Nervos / CKB 的开发者或深度社区成员 主要测试 CCC、CKB、Fiber、Spore、xUDT、Nervos Talk、SDK、生态架构等专业问题。 3-5 位普通 Web3 /...
- `S04` [[Fiber] CKB 能让 Fiber 拥有更好的 Amboss](https://talk.nervos.org/t/fiber-ckb-fiber-amboss/10353/1) | Ckroamer | 2026-06-07 16:16:06 CST | 我在调研闪电网络的生态应用时，惊讶的发现了 Amboss 这个项目，它的核心功能就是为闪电网络节点提供 “入向” 流动性，简单地说，就是为商家提供更大的收款额度。 在此基础之上，Amboss 将因为闪电网络固有的协议特性而带来的限制，转化为流动性市场，成为了闪电网络生态中为数不多的 Defi 项目，着实令人眼前一亮。 收款额度 这个问题目前主要有两种解决思路: JIT (Just-In-Time Channel，即时通道) 思路。也就是透过 LSP 服务商，在检测到要为某个钱包节点转账但对方却没有足够入金额度时，即时建立一条有足够额度的通道。...
- `S05` [[DIS] Decentralized privacy order-book appchain based on CKB L1 - 2026.phase-1](https://talk.nervos.org/t/dis-decentralized-privacy-order-book-appchain-based-on-ckb-l1-2026-phase-1/10015/30) | Lawliet_Chan | 2026-06-07 13:34:32 CST | 周报 2026.6.7 开会并讨论重新撰写invisibook论文大纲（备投NDSS Fall Cycle）
- `S06` [[DIS] Fiber Desktop v1 ground-up rebuild and launch — fnn desktop app](https://talk.nervos.org/t/dis-fiber-desktop-v1-ground-up-rebuild-and-launch-fnn-desktop-app/10317/12) | ebubedev | 2026-06-07 08:56:56 CST | Voting update — 3 days left (closes Wednesday) The [VOT] poll is live on Metaforo. Current turnout: 5,970,865 / 15,000,000 CKB (~40% of quorum) We still need ~9M CKB in participation for the vote to count. Yes and No both count toward quorum. Vote:...
- `S07` [CKBadger: a local-first CKB-native explorer, and a vibe-coding experiment](https://talk.nervos.org/t/ckbadger-a-local-first-ckb-native-explorer-and-a-vibe-coding-experiment/10276/7) | janx | 2026-06-07 08:51:53 CST | Good question! TLDR; “Pure CKB” means the object is fully on the CKB blockchain, zero off-chain dependencies. “Decentralized Mixture” means the object is partially on-chain, with some off-chain but decentralized dependencies like IPFS. In contrast, “Centralized Mixture” refers...

## 活跃话题

1. [Fiber Desktop — run Fiber (FNN) on your laptop without the “public node” headache](https://talk.nervos.org/t/fiber-desktop-run-fiber-fnn-on-your-laptop-without-the-public-node-headache/10247) | 2 条近窗帖子 | 最新活动 2026-06-07 23:06:48 CST | tags: fiber, testnet
2. [招募 Nervos 社区成员参与 Nervos Brain最终验收测试](https://talk.nervos.org/t/nervos-nervos-brain/10354) | 1 条近窗帖子 | 最新活动 2026-06-07 22:58:35 CST
3. [[Fiber] CKB 能让 Fiber 拥有更好的 Amboss](https://talk.nervos.org/t/fiber-ckb-fiber-amboss/10353) | 1 条近窗帖子 | 最新活动 2026-06-07 16:16:06 CST
4. [[DIS] Decentralized privacy order-book appchain based on CKB L1 - 2026.phase-1](https://talk.nervos.org/t/dis-decentralized-privacy-order-book-appchain-based-on-ckb-l1-2026-phase-1/10015) | 1 条近窗帖子 | 最新活动 2026-06-07 13:34:32 CST | tags: appchain
5. [[DIS] Fiber Desktop v1 ground-up rebuild and launch — fnn desktop app](https://talk.nervos.org/t/dis-fiber-desktop-v1-ground-up-rebuild-and-launch-fnn-desktop-app/10317) | 1 条近窗帖子 | 最新活动 2026-06-07 08:56:56 CST | tags: fiber
6. [CKBadger: a local-first CKB-native explorer, and a vibe-coding experiment](https://talk.nervos.org/t/ckbadger-a-local-first-ckb-native-explorer-and-a-vibe-coding-experiment/10276) | 1 条近窗帖子 | 最新活动 2026-06-07 08:51:53 CST | tags: app

## 最近帖子摘录

- 2026-06-07 23:06:48 CST | knmo | [Fiber Desktop — run Fiber (FNN) on your laptop without the “public node” headache](https://talk.nervos.org/t/fiber-desktop-run-fiber-fnn-on-your-laptop-without-the-public-node-headache/10247/10) | OT: Delegated DAO voting could become an important democratic mechanism if @CKBA plays a decisive role in its implementation. CKB can remain locked for years (and soon decades)...
- 2026-06-07 22:58:35 CST | IrisNeko | [招募 Nervos 社区成员参与 Nervos Brain最终验收测试](https://talk.nervos.org/t/nervos-nervos-brain/10354/1) | 大家好，我这边准备对 Nervos Brain做最终验收测试，想邀请 10-15 位 Nervos 社区成员一起帮忙试用和反馈。 Nervos Brain 是一个面向 CKB / Nervos 生态的问答Agent，会基于官方文档、Nervos Talk、GitHub docs/code 等资料进行检索和回答。 这次希望招募几类测试成员： 3-5...
- 2026-06-07 16:16:06 CST | Ckroamer | [[Fiber] CKB 能让 Fiber 拥有更好的 Amboss](https://talk.nervos.org/t/fiber-ckb-fiber-amboss/10353/1) | 我在调研闪电网络的生态应用时，惊讶的发现了 Amboss 这个项目，它的核心功能就是为闪电网络节点提供 “入向” 流动性，简单地说，就是为商家提供更大的收款额度。 在此基础之上，Amboss 将因为闪电网络固有的协议特性而带来的限制，转化为流动性市场，成为了闪电网络生态中为数不多的 Defi 项目，着实令人眼前一亮。 收款额度...
- 2026-06-07 13:34:32 CST | Lawliet_Chan | [[DIS] Decentralized privacy order-book appchain based on CKB L1 - 2026.phase-1](https://talk.nervos.org/t/dis-decentralized-privacy-order-book-appchain-based-on-ckb-l1-2026-phase-1/10015/30) | 周报 2026.6.7 开会并讨论重新撰写invisibook论文大纲（备投NDSS Fall Cycle）
- 2026-06-07 09:00:01 CST | ebubedev | [Fiber Desktop — run Fiber (FNN) on your laptop without the “public node” headache](https://talk.nervos.org/t/fiber-desktop-run-fiber-fnn-on-your-laptop-without-the-public-node-headache/10247/9) | DAO vote open — closes Wednesday Quick update: the v1 rebuild proposal is in Metaforo voting until Wednesday. This prototype thread showed the demand — users on relays,...
- 2026-06-07 08:56:56 CST | ebubedev | [[DIS] Fiber Desktop v1 ground-up rebuild and launch — fnn desktop app](https://talk.nervos.org/t/dis-fiber-desktop-v1-ground-up-rebuild-and-launch-fnn-desktop-app/10317/12) | Voting update — 3 days left (closes Wednesday) The [VOT] poll is live on Metaforo. Current turnout: 5,970,865 / 15,000,000 CKB (~40% of quorum) We still need ~9M CKB in...
- 2026-06-07 08:51:53 CST | janx | [CKBadger: a local-first CKB-native explorer, and a vibe-coding experiment](https://talk.nervos.org/t/ckbadger-a-local-first-ckb-native-explorer-and-a-vibe-coding-experiment/10276/7) | Good question! TLDR; “Pure CKB” means the object is fully on the CKB blockchain, zero off-chain dependencies. “Decentralized Mixture” means the object is partially on-chain,...
