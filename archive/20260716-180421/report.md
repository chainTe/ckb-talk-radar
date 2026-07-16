# Nervos Talk 社区简报

- 统计窗口: 2026-07-16 02:04:21 CST 到 2026-07-17 02:04:21 CST
- 生成时间: 2026-07-17 02:04:28 CST
- 话题数: 8
- 帖子数: 14
- 作者数: 8
- 总结模式: ai:openrouter

## 社区总结

## 今日发生了什么

Nervos Talk 社区今日围绕 Fiber 网络生态展开密集技术讨论，核心议题包括支付流架构、RGB++ 交换机制与流动性市场建设。[S01, S04, S10] 开发者们就链下通道的即时性与原子性、Bitcoin 侧的单次使用封锁承诺，以及 Opticrum 去中心化流动性市场的实际操作展开深度互动。[S02, S06, S10]

## 重点话题

- **Visa 自托管支付平台架构探讨**：BuildUnion 团队正在敲定基于 Nervos 的自托管 Visa 支付平台架构，用户刷卡后由钱包提示确认付款。[S01] matt_ckb 建议采用 Fiber 通道实现即时性与原子性，指出链上结算无法满足需求，BuildUnion 确认收到建议。[S02, S03]

- **Spark Program | Fiber RGB++ Swap 机制澄清**：Carl 回应 matt_ckb 的提问，确认 Bitcoin 侧通道内并非每次更新都广播 OP_RETURN 承诺，而是每个新通道状态生成新的签名单次使用封锁承诺，避免每笔支付都产生 Bitcoin 交易。[S06] matt_ckb 此前对此表示关注，认为这是 RGB++/Fiber 长期缺失的组件。[S04]

- **Trickle 流式微支付设计确认**：T_Silva 回应 ArthurZhang 的疑问，明确 Trickle 并非新会计原语，而是在重复通道更新之上封装"预算上限+速率+到期时间"的本地支出许可，实现无需逐笔确认的流式支付。[S08, S09]

- **Opticrum 流动性市场中文操作手册发布**：Ckroamer 发布 Fiber Opticrum 流动性提供者操作手册，涵盖节点前提、市场机制与实操步骤，连接需要 Fiber 通道流动性的买家与提供方。[S10]

- **Fiber Desktop 中期更新**：ebubedev 发布 Fiber Studio v0.1.9 进度更新，非 M3 里程碑完成报告，但呼吁用户升级至最新构建。[S12]

## 值得继续跟进

- **RGB++/Fiber 与 Lightning Liquidity Ads 的融合路径**：ArthurZhang 指出该项目结构接近 Lightning Liquidity Ads，且 RGB Lightning 社区因资产传输原语复杂度而停滞，需观察 Nervos 生态能否突破类似瓶颈。[S05, S07]

- **PactAgent 争议解决机制**：ArthurZhang 追问 PactAgent 在里程碑验收分歧时的处理机制，该问题尚未得到开发者回应，关系到 DAO/Bounty 工作流的实际可信度。[S11]

- **Nervos Community Catalyst Q2 2026 报告后续影响**：neon.bit 发布的季度报告显示 Community Keeps Building 增至 70 名 CKBuilders，Build on CKB 引入约 40 名新开发者，需观察 Q3 实际交付转化。[S13]

## 来源索引

- `S01` [Architectural recommended for a payment flow on Nervos](https://talk.nervos.org/t/architectural-recommended-for-a-payment-flow-on-nervos/10496/1) | BuildUnion | 2026-07-16 16:01:05 CST | Hey everyone, We’re finalizing the architecture for a self-custodial Visa payment platform on Nervos and would appreciate some architectural clarity. The intended payment flow is: User taps their Visa card. Their Nervos wallet prompts them to approve the payment. Once they...
- `S02` [Architectural recommended for a payment flow on Nervos](https://talk.nervos.org/t/architectural-recommended-for-a-payment-flow-on-nervos/10496/2) | matt_ckb | 2026-07-16 18:37:18 CST | I suggest looking into Fiber, channels can offer this immediacy and atomicity, but on-chain settlement will not
- `S03` [Architectural recommended for a payment flow on Nervos](https://talk.nervos.org/t/architectural-recommended-for-a-payment-flow-on-nervos/10496/3) | BuildUnion | 2026-07-16 20:43:18 CST | Roger that, thanks.
- `S04` [Spark Program | Fiber RGB++ Swap](https://talk.nervos.org/t/spark-program-fiber-rgb-swap/10487/2) | matt_ckb | 2026-07-16 02:27:33 CST | On the BTC side, (inside the channel) are users iterating on a OP_RETURN commitment that could be pushed to the chain to settle the channel balances? Really glad to see you looking at this, it has been a missing component of RGB++/Fiber for some time now.
- `S05` [Spark Program | Fiber RGB++ Swap](https://talk.nervos.org/t/spark-program-fiber-rgb-swap/10487/3) | ArthurZhang | 2026-07-16 11:50:42 CST | Nice one, this kind of reminds me a bit of Lightning Liquidity Ads. There have actually been similar discussions in the RGB Lightning community as well, but they have been largely caught up with the complexity of getting the asset transport primitive itself right. I think you...
- `S06` [Spark Program | Fiber RGB++ Swap](https://talk.nervos.org/t/spark-program-fiber-rgb-swap/10487/4) | Carl | 2026-07-16 20:02:03 CST | Hi Matt, exactly the right question — and yes, that’s the mechanism. Users aren’t broadcasting an OP_RETURN commitment per update; that would mean a Bitcoin tx per payment, which defeats the point of a channel. Instead each new channel state produces a new signed single-use-...
- `S07` [Spark Program | Fiber RGB++ Swap](https://talk.nervos.org/t/spark-program-fiber-rgb-swap/10487/5) | Carl | 2026-07-16 20:05:48 CST | Hi Arthur, good parallel — structurally this is close to Liquidity Ads: a gossip-broadcast offer that lets peers discover terms before committing, rather than negotiating out of band. I think the reason RGB Lightning discussions stalled on the asset transport primitive is that...
- `S08` [Trickle: Budget-Capped Streaming Micropayments for Fiber Network](https://talk.nervos.org/t/trickle-budget-capped-streaming-micropayments-for-fiber-network/10493/2) | ArthurZhang | 2026-07-16 11:57:30 CST | Really interesting direction, one question I have: would each stream essentially be a higher-level abstraction over repeated channel updates, or are you envisioning some new accounting primitive that allows the stream state to accumulate off-chain and only settle against the...
- `S09` [Trickle: Budget-Capped Streaming Micropayments for Fiber Network](https://talk.nervos.org/t/trickle-budget-capped-streaming-micropayments-for-fiber-network/10493/3) | T_Silva | 2026-07-16 17:12:10 CST | Good question, appreciate you digging into it. It’s the first one, not a new primitive: each stream really is repeated channel updates under a thin allowance wrapper. The “grant” is a local spend cap the payer signs once (budget + rate + expiry) so nothing needs approving per-...
- `S10` [[Fiber] Opticrum 流动性提供者操作手册](https://talk.nervos.org/t/fiber-opticrum/10495/1) | Ckroamer | 2026-07-16 13:05:43 CST | 本文假设你已有一个运行中的 Fiber 节点—— 如果没有，请先参照 Fiber Network 官方文档 搭好节点，记下 fiber_rpc_url（默认 http://localhost:8227），再继续往下走。 什么是 Opticrum Opticrum 是运行在 CKB（Nervos Network）上的去中心化流动性市场。它连接两类参与者： 买家（Order 发布者）：需要 Fiber 通道流动性的人。他们在链上发布 Order，锁定资金并声明 “我需要一个容量为 X 的通道，每区块付 Y shannons 作为租金”...
- `S11` [PactAgent Developer Update: UI Redesign, DAO/Bounty Workflow Focus, and Agreement Operations Improvements](https://talk.nervos.org/t/pactagent-developer-update-ui-redesign-dao-bounty-workflow-focus-and-agreement-operations-improvements/10352/3) | ArthurZhang | 2026-07-16 12:19:06 CST | hi ajay, great work, just one question I was curious about, how does PactAgent handle cases where there is a disagreement on milestone completion? for example, a builder submits proof and considers the milestone completed, but the reviewer disagrees and rejects it. Is there an...
- `S12` [[DIS] Fiber Desktop v1 ground-up rebuild and launch — fnn desktop app](https://talk.nervos.org/t/dis-fiber-desktop-v1-ground-up-rebuild-and-launch-fnn-desktop-app/10317/22) | ebubedev | 2026-07-16 09:40:14 CST | Progress update: Fiber Studio v0.1.9 — upgrade when you can Hi everyone, Following the Milestone 2 post and the smaller fix release — this is not an M3 completion report. It’s a mid-milestone update on what shipped since then, and a nudge to move to the latest build. Latest...
- `S13` [Nervos Community Catalyst: Quarterly Reports](https://talk.nervos.org/t/nervos-community-catalyst-quarterly-reports/8822/6) | neon.bit | 2026-07-16 06:43:47 CST | Q2 2026 report Executive Summary Q2 2026 was defined by expansion and consolidation across all of NCC’s core programmes. The Community Keeps Building initiative grew to 70 CKBuilders, while the launch of the Build on CKB initiative brought a further estimated 40 new developers...
- `S14` [Spark Program | Cellar — A Capacity Leasing Market for CKB Cells](https://talk.nervos.org/t/spark-program-cellar-a-capacity-leasing-market-for-ckb-cells/10492/2) | matt_ckb | 2026-07-16 02:07:10 CST | really glad to see your interest in this use case! one thing I wanted to clarify is that since is a property of a transaction, not the cell itself. If you use since to enforce the timelock you are bound to a single signed transaction, the leased capacity can’t actually be used...

## 活跃话题

1. [Architectural recommended for a payment flow on Nervos](https://talk.nervos.org/t/architectural-recommended-for-a-payment-flow-on-nervos/10496) | 3 条近窗帖子 | 最新活动 2026-07-16 20:43:18 CST
2. [Spark Program | Fiber RGB++ Swap](https://talk.nervos.org/t/spark-program-fiber-rgb-swap/10487) | 4 条近窗帖子 | 最新活动 2026-07-16 20:05:48 CST | tags: Spark-Program
3. [Trickle: Budget-Capped Streaming Micropayments for Fiber Network](https://talk.nervos.org/t/trickle-budget-capped-streaming-micropayments-for-fiber-network/10493) | 2 条近窗帖子 | 最新活动 2026-07-16 17:12:10 CST | tags: CKB, Hackathlon, fiber
4. [[Fiber] Opticrum 流动性提供者操作手册](https://talk.nervos.org/t/fiber-opticrum/10495) | 1 条近窗帖子 | 最新活动 2026-07-16 13:05:43 CST
5. [PactAgent Developer Update: UI Redesign, DAO/Bounty Workflow Focus, and Agreement Operations Improvements](https://talk.nervos.org/t/pactagent-developer-update-ui-redesign-dao-bounty-workflow-focus-and-agreement-operations-improvements/10352) | 1 条近窗帖子 | 最新活动 2026-07-16 12:19:06 CST | tags: CKB, CKB-VM, dapp
6. [[DIS] Fiber Desktop v1 ground-up rebuild and launch — fnn desktop app](https://talk.nervos.org/t/dis-fiber-desktop-v1-ground-up-rebuild-and-launch-fnn-desktop-app/10317) | 1 条近窗帖子 | 最新活动 2026-07-16 09:40:14 CST | tags: fiber
7. [Nervos Community Catalyst: Quarterly Reports](https://talk.nervos.org/t/nervos-community-catalyst-quarterly-reports/8822) | 1 条近窗帖子 | 最新活动 2026-07-16 06:43:47 CST
8. [Spark Program | Cellar — A Capacity Leasing Market for CKB Cells](https://talk.nervos.org/t/spark-program-cellar-a-capacity-leasing-market-for-ckb-cells/10492) | 1 条近窗帖子 | 最新活动 2026-07-16 02:07:10 CST | tags: Spark-Program

## 最近帖子摘录

- 2026-07-16 20:43:18 CST | BuildUnion | [Architectural recommended for a payment flow on Nervos](https://talk.nervos.org/t/architectural-recommended-for-a-payment-flow-on-nervos/10496/3) | Roger that, thanks.
- 2026-07-16 20:05:48 CST | Carl | [Spark Program | Fiber RGB++ Swap](https://talk.nervos.org/t/spark-program-fiber-rgb-swap/10487/5) | Hi Arthur, good parallel — structurally this is close to Liquidity Ads: a gossip-broadcast offer that lets peers discover terms before committing, rather than negotiating out of...
- 2026-07-16 20:02:03 CST | Carl | [Spark Program | Fiber RGB++ Swap](https://talk.nervos.org/t/spark-program-fiber-rgb-swap/10487/4) | Hi Matt, exactly the right question — and yes, that’s the mechanism. Users aren’t broadcasting an OP_RETURN commitment per update; that would mean a Bitcoin tx per payment,...
- 2026-07-16 18:37:18 CST | matt_ckb | [Architectural recommended for a payment flow on Nervos](https://talk.nervos.org/t/architectural-recommended-for-a-payment-flow-on-nervos/10496/2) | I suggest looking into Fiber, channels can offer this immediacy and atomicity, but on-chain settlement will not
- 2026-07-16 17:12:10 CST | T_Silva | [Trickle: Budget-Capped Streaming Micropayments for Fiber Network](https://talk.nervos.org/t/trickle-budget-capped-streaming-micropayments-for-fiber-network/10493/3) | Good question, appreciate you digging into it. It’s the first one, not a new primitive: each stream really is repeated channel updates under a thin allowance wrapper. The...
- 2026-07-16 16:01:05 CST | BuildUnion | [Architectural recommended for a payment flow on Nervos](https://talk.nervos.org/t/architectural-recommended-for-a-payment-flow-on-nervos/10496/1) | Hey everyone, We’re finalizing the architecture for a self-custodial Visa payment platform on Nervos and would appreciate some architectural clarity. The intended payment flow...
- 2026-07-16 13:05:43 CST | Ckroamer | [[Fiber] Opticrum 流动性提供者操作手册](https://talk.nervos.org/t/fiber-opticrum/10495/1) | 本文假设你已有一个运行中的 Fiber 节点—— 如果没有，请先参照 Fiber Network 官方文档 搭好节点，记下 fiber_rpc_url（默认 http://localhost:8227），再继续往下走。 什么是 Opticrum Opticrum 是运行在 CKB（Nervos Network）上的去中心化流动性市场。它连接两类参与者：...
- 2026-07-16 12:19:06 CST | ArthurZhang | [PactAgent Developer Update: UI Redesign, DAO/Bounty Workflow Focus, and Agreement Operations Improvements](https://talk.nervos.org/t/pactagent-developer-update-ui-redesign-dao-bounty-workflow-focus-and-agreement-operations-improvements/10352/3) | hi ajay, great work, just one question I was curious about, how does PactAgent handle cases where there is a disagreement on milestone completion? for example, a builder submits...
- 2026-07-16 11:57:30 CST | ArthurZhang | [Trickle: Budget-Capped Streaming Micropayments for Fiber Network](https://talk.nervos.org/t/trickle-budget-capped-streaming-micropayments-for-fiber-network/10493/2) | Really interesting direction, one question I have: would each stream essentially be a higher-level abstraction over repeated channel updates, or are you envisioning some new...
- 2026-07-16 11:50:42 CST | ArthurZhang | [Spark Program | Fiber RGB++ Swap](https://talk.nervos.org/t/spark-program-fiber-rgb-swap/10487/3) | Nice one, this kind of reminds me a bit of Lightning Liquidity Ads. There have actually been similar discussions in the RGB Lightning community as well, but they have been...
- 2026-07-16 09:40:14 CST | ebubedev | [[DIS] Fiber Desktop v1 ground-up rebuild and launch — fnn desktop app](https://talk.nervos.org/t/dis-fiber-desktop-v1-ground-up-rebuild-and-launch-fnn-desktop-app/10317/22) | Progress update: Fiber Studio v0.1.9 — upgrade when you can Hi everyone, Following the Milestone 2 post and the smaller fix release — this is not an M3 completion report. It’s a...
- 2026-07-16 06:43:47 CST | neon.bit | [Nervos Community Catalyst: Quarterly Reports](https://talk.nervos.org/t/nervos-community-catalyst-quarterly-reports/8822/6) | Q2 2026 report Executive Summary Q2 2026 was defined by expansion and consolidation across all of NCC’s core programmes. The Community Keeps Building initiative grew to 70...
- 2026-07-16 02:27:33 CST | matt_ckb | [Spark Program | Fiber RGB++ Swap](https://talk.nervos.org/t/spark-program-fiber-rgb-swap/10487/2) | On the BTC side, (inside the channel) are users iterating on a OP_RETURN commitment that could be pushed to the chain to settle the channel balances? Really glad to see you...
- 2026-07-16 02:07:10 CST | matt_ckb | [Spark Program | Cellar — A Capacity Leasing Market for CKB Cells](https://talk.nervos.org/t/spark-program-cellar-a-capacity-leasing-market-for-ckb-cells/10492/2) | really glad to see your interest in this use case! one thing I wanted to clarify is that since is a property of a transaction, not the cell itself. If you use since to enforce...
