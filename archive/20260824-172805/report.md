# Nervos Talk 社区简报

- 统计窗口: 2026-08-24 01:28:05 CST 到 2026-08-25 01:28:05 CST
- 生成时间: 2026-08-25 01:28:08 CST
- 话题数: 6
- 帖子数: 8
- 作者数: 6
- 总结模式: ai:openai-compatible

## 社区总结

## 今日发生了什么

过去 24 小时，Nervos Talk 上主要围绕几个技术方向展开讨论：Spark 委员会拒绝了一个 CKB NFT 市场提案、Myelin 发布了新的功能进展、Fiber 在探索接入 Light Client，同时有一个 ZK 双人文字游戏上线邀请社区试玩。[S01, S03, S04, S07] 整体来看，社区不算平静，但也没有重大突发消息，更多是开发者层面的迭代与讨论。[S01, S03, S04, S05, S06, S07, S08]

## 重点话题

- **Spark 委员会拒绝了 CKB NFT 市场提案**：申请者 SamChain 提交的 NFT 市场平台方案未通过评审，委员会表示经过仔细考虑后暂时无法通过该申请。[S01]
- **Fiber 开始探索摆脱全节点 RPC 依赖**：joii2020 发布了把 Fiber 与 CKB Light Client 集成的方案，目的是让第三方产品不必依赖公共 RPC 服务；ArthurZhang 肯定了方向，但也提醒需要区分“验证创建 Cell 的交易”和“确认该 Cell 之后没有被花费”这两件事。[S07, S08]
- **Myelin 从有界会话走向持续运行**：帖子介绍了 epoch 生产、创世绑定终结性、持久恢复等能力，并用 Veloren 作为集成实验场景，让 off-chain Cell 会话运行时能更接近连续运行。[S03]
- **社区开发者做了一个双人 ZK 单词游戏**：原型叫 Mastermind on CKB，双方各自在链上提交一个四字母单词，然后轮流猜测对方的词，欢迎社区试玩。[S04]
- **共享锁和游戏场景的讨论在继续**：关于 COMP Shared Lock，有观点认为它可以降低使用门槛，让没有 CKB 钱包的用户也能参与链上留言或接收 UDT 空投；另一边，关于把 Counter Strike 移植到 Fiber 的讨论中，作者认为实时游戏更适合 offchain 路线，5v5 的通道流动性仍是挑战，且尚未开始实际尝试。[S05, S06]

## 值得继续跟进

- **Fiber + Light Client 的验证盲区**：ArthurZhang 指出的“Cell 创建”与“Cell 未被后续花费”之间的验证差异，是这套方案后续需要重点解决的技术问题。[S08]
- **Myelin 的 Veloren 集成实验**：从有界会话过渡到持续运行后，实际应用中的稳定性和持久恢复能力还需要更多测试来验证。[S03]
- **被拒的 NFT 市场提案是否会调整或重新提交**：目前委员会只回复了“暂时拒绝”，没有更多信息，需要继续关注申请者是否会带来修改版本。[S01]

## 来源索引

- `S01` [Spark Program | CKB NFT Marketplace - On-Chain Digital Object Trading Platform](https://talk.nervos.org/t/spark-program-ckb-nft-marketplace-on-chain-digital-object-trading-platform/10544/2) | xingtianchunyan | 2026-08-24 21:46:39 CST | Hi, @SamChain, Thank you for taking the time to submit a proposal for a CKB NFT marketplace platform. The committee has completed its review process. After careful consideration, it regrets to inform you that the application for this CKB NFT marketplace has been temporarily...
- `S02` [Spark Program | CKB NFT Marketplace - On-Chain Digital Object Trading Platform](https://talk.nervos.org/t/spark-program-ckb-nft-marketplace-on-chain-digital-object-trading-platform/10544/3) | zz_tovarishch | 2026-08-24 21:49:53 CST | 
- `S03` [From bounded sessions to continuous operation: pluggable chain modules in Myelin](https://talk.nervos.org/t/from-bounded-sessions-to-continuous-operation-pluggable-chain-modules-in-myelin/10658/1) | ArthurZhang | 2026-08-24 21:28:37 CST | Epoch production, genesis-bound finality, durable recovery, and a Veloren integration experiment. The previous post, ‘Introducing Myelin: a CKB-aligned off-chain Cell session runtime’describes the core proposition: run finite Cell transitions off-chain, preserve CKB...
- `S04` [I built a two-player ZK word game on CKB. Come play it](https://talk.nervos.org/t/i-built-a-two-player-zk-word-game-on-ckb-come-play-it/10657/1) | truthixify | 2026-08-24 18:15:22 CST | ckb-mastermind-app.vercel.app Mastermind on CKB It is Mastermind, except with words, and both people are playing at the same time. You each pick a secret four-letter word and commit to it on chain. Then you take turns guessing at each other’s word, and when someone guesses at...
- `S05` [COMP Shared Lock: From Gas Pool to Open Message Spaces](https://talk.nervos.org/t/comp-shared-lock-from-gas-pool-to-open-message-spaces/10654/2) | RetricSu | 2026-08-24 16:52:00 CST | 这是一个很简单的想法，但是非常有趣。没有准入门槛可以让用户不需要有ckb钱包就能去使用应用，比如留言。但它让我想到，也许设置一定的门槛，也能很好的发挥这个 shared lock 的想法。比如某些项目lauch 的时候，他们可能会希望让一些用户去试用自己的应用，它们可以通过自己的服务器去设置一定的门槛，让满足的用户去享受这些链上的shared cells来体验产品。一个例子可能是，我们之前考虑解决的 air-drop 某个 udt 的接收问题：用户没有ckb 钱包，也就没办法去接收 udt 空投，要么项目方自己去付出这些成本，每空投一个...
- `S06` [Porting Couter Strike to Fiber network](https://talk.nervos.org/t/porting-couter-strike-to-fiber-network/10647/5) | RetricSu | 2026-08-24 16:40:36 CST | 感谢你这么细致的回复。你对这个 demo 技术上用到的东西的理解完全正确。我感觉游戏确实是个不错的用例，至少我能看到在 CKB 上对游戏讨论的热情是很高的。 针对 CS 这个 kill/match 数的调研很有意思，给了我很多的启发。反过来想，要移植这样的游戏，做full on-chain game几乎是不可能的，offchain显然是更合适的路线。 对于这种实时游戏，确实5 vs 5 player 之间的流动性会是通道网络上一个不小的挑战。我还没有开始往这个方向去做一些尝试，这个 demo...
- `S07` [Integrating Fiber with CKB Light Client: An Exploration in Reducing Reliance on Full-Node RPC ServicesFiber+LightClient](https://talk.nervos.org/t/integrating-fiber-with-ckb-light-client-an-exploration-in-reducing-reliance-on-full-node-rpc-servicesfiber-lightclient/10656/1) | joii2020 | 2026-08-24 10:40:25 CST | Background Fiber currently retrieves on-chain data through the RPC interface of a CKB full node. The default testnet configuration uses a public RPC, which makes Fiber easy to deploy and try. For third parties that want to integrate Fiber into their own products, however, this...
- `S08` [Integrating Fiber with CKB Light Client: An Exploration in Reducing Reliance on Full-Node RPC ServicesFiber+LightClient](https://talk.nervos.org/t/integrating-fiber-with-ckb-light-client-an-exploration-in-reducing-reliance-on-full-node-rpc-servicesfiber-lightclient/10656/2) | ArthurZhang | 2026-08-24 11:54:34 CST | Nice work. I think this is a meaningful step towards making Fiber clients much less dependent on trusted full-node RPCs. The main thing I would still keep an eye on is the distinction between verifying the transaction that created a Cell and knowing that the Cell has not since...

## 活跃话题

1. [Spark Program | CKB NFT Marketplace - On-Chain Digital Object Trading Platform](https://talk.nervos.org/t/spark-program-ckb-nft-marketplace-on-chain-digital-object-trading-platform/10544) | 2 条近窗帖子 | 最新活动 2026-08-24 21:46:39 CST | tags: Rejection
2. [From bounded sessions to continuous operation: pluggable chain modules in Myelin](https://talk.nervos.org/t/from-bounded-sessions-to-continuous-operation-pluggable-chain-modules-in-myelin/10658) | 1 条近窗帖子 | 最新活动 2026-08-24 21:28:37 CST | tags: CellScript, Myelin
3. [I built a two-player ZK word game on CKB. Come play it](https://talk.nervos.org/t/i-built-a-two-player-zk-word-game-on-ckb-come-play-it/10657) | 1 条近窗帖子 | 最新活动 2026-08-24 18:15:22 CST | tags: CKB, testnet
4. [COMP Shared Lock: From Gas Pool to Open Message Spaces](https://talk.nervos.org/t/comp-shared-lock-from-gas-pool-to-open-message-spaces/10654) | 1 条近窗帖子 | 最新活动 2026-08-24 16:52:00 CST
5. [Porting Couter Strike to Fiber network](https://talk.nervos.org/t/porting-couter-strike-to-fiber-network/10647) | 1 条近窗帖子 | 最新活动 2026-08-24 16:40:36 CST | tags: fiber, game
6. [Integrating Fiber with CKB Light Client: An Exploration in Reducing Reliance on Full-Node RPC ServicesFiber+LightClient](https://talk.nervos.org/t/integrating-fiber-with-ckb-light-client-an-exploration-in-reducing-reliance-on-full-node-rpc-servicesfiber-lightclient/10656) | 2 条近窗帖子 | 最新活动 2026-08-24 11:54:34 CST | tags: fiber

## 最近帖子摘录

- 2026-08-24 21:49:53 CST | zz_tovarishch | [Spark Program | CKB NFT Marketplace - On-Chain Digital Object Trading Platform](https://talk.nervos.org/t/spark-program-ckb-nft-marketplace-on-chain-digital-object-trading-platform/10544/3) | 
- 2026-08-24 21:46:39 CST | xingtianchunyan | [Spark Program | CKB NFT Marketplace - On-Chain Digital Object Trading Platform](https://talk.nervos.org/t/spark-program-ckb-nft-marketplace-on-chain-digital-object-trading-platform/10544/2) | Hi, @SamChain, Thank you for taking the time to submit a proposal for a CKB NFT marketplace platform. The committee has completed its review process. After careful...
- 2026-08-24 21:28:37 CST | ArthurZhang | [From bounded sessions to continuous operation: pluggable chain modules in Myelin](https://talk.nervos.org/t/from-bounded-sessions-to-continuous-operation-pluggable-chain-modules-in-myelin/10658/1) | Epoch production, genesis-bound finality, durable recovery, and a Veloren integration experiment. The previous post, ‘Introducing Myelin: a CKB-aligned off-chain Cell session...
- 2026-08-24 18:15:22 CST | truthixify | [I built a two-player ZK word game on CKB. Come play it](https://talk.nervos.org/t/i-built-a-two-player-zk-word-game-on-ckb-come-play-it/10657/1) | ckb-mastermind-app.vercel.app Mastermind on CKB It is Mastermind, except with words, and both people are playing at the same time. You each pick a secret four-letter word and...
- 2026-08-24 16:52:00 CST | RetricSu | [COMP Shared Lock: From Gas Pool to Open Message Spaces](https://talk.nervos.org/t/comp-shared-lock-from-gas-pool-to-open-message-spaces/10654/2) | 这是一个很简单的想法，但是非常有趣。没有准入门槛可以让用户不需要有ckb钱包就能去使用应用，比如留言。但它让我想到，也许设置一定的门槛，也能很好的发挥这个 shared lock 的想法。比如某些项目lauch 的时候，他们可能会希望让一些用户去试用自己的应用，它们可以通过自己的服务器去设置一定的门槛，让满足的用户去享受这些链上的shared...
- 2026-08-24 16:40:36 CST | RetricSu | [Porting Couter Strike to Fiber network](https://talk.nervos.org/t/porting-couter-strike-to-fiber-network/10647/5) | 感谢你这么细致的回复。你对这个 demo 技术上用到的东西的理解完全正确。我感觉游戏确实是个不错的用例，至少我能看到在 CKB 上对游戏讨论的热情是很高的。 针对 CS 这个 kill/match 数的调研很有意思，给了我很多的启发。反过来想，要移植这样的游戏，做full on-chain game几乎是不可能的，offchain显然是更合适的路线。...
- 2026-08-24 11:54:34 CST | ArthurZhang | [Integrating Fiber with CKB Light Client: An Exploration in Reducing Reliance on Full-Node RPC ServicesFiber+LightClient](https://talk.nervos.org/t/integrating-fiber-with-ckb-light-client-an-exploration-in-reducing-reliance-on-full-node-rpc-servicesfiber-lightclient/10656/2) | Nice work. I think this is a meaningful step towards making Fiber clients much less dependent on trusted full-node RPCs. The main thing I would still keep an eye on is the...
- 2026-08-24 10:40:25 CST | joii2020 | [Integrating Fiber with CKB Light Client: An Exploration in Reducing Reliance on Full-Node RPC ServicesFiber+LightClient](https://talk.nervos.org/t/integrating-fiber-with-ckb-light-client-an-exploration-in-reducing-reliance-on-full-node-rpc-servicesfiber-lightclient/10656/1) | Background Fiber currently retrieves on-chain data through the RPC interface of a CKB full node. The default testnet configuration uses a public RPC, which makes Fiber easy to...
