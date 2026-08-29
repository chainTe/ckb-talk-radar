# Nervos Talk 社区简报

- 统计窗口: 2026-08-28 08:51:10 CST 到 2026-08-29 08:51:10 CST
- 生成时间: 2026-08-29 08:51:18 CST
- 话题数: 5
- 帖子数: 7
- 作者数: 3
- 总结模式: ai:openai-compatible

## 社区总结

## 今日发生了什么

Nervos Talk 今天算不上平静，多个技术话题在同一天更新[S01, S02, S03, S04, S05, S06, S07]。核心看点集中在 ZK 游戏设计、Fiber 生态工具和 CellScript 项目进展上[S01, S05, S07]：有开发者展示了一款基于 CKB 的双人 ZK 单词游戏并引发安全性讨论[S01, S02, S03]；另一侧，Fiber 网络的 GUI 客户端和隐私资金方案也在社区里获得了推进[S05, S06]。此外，CellScript 发布了从 0.12 到 0.24 的四个月项目报告[S07]。

## 重点话题

- **ZK 单词游戏引发机制讨论**：ArthurZhang 指出这个游戏类似 commit–reveal 机制，通过给双方相同尝试次数来消除先手优势，但同时提出 create/join 时也应该证明每个 commitment 对应有效的词典单词，否则可能有问题[S01]。随后开发者 truthixify 承认这些问题是真实的，并补充说 mastermind circuit 已经将 commitment 绑定到单词并证明词典成员资格，但如果有人提交垃圾 commitment，玩家会进入一个永远无法完成的游戏[S02, S03]。

- **CellScript 发布四个月项目报告**：ArthurZhang 在 CellScript 帖子中介绍了从 0.12 到 0.24 的变化，提到最初在四月发布 0.12 时主要把它看作一个终于有了清晰发布边界的编译器，并总结了 Q2 和 Q3 至今的相关工作[S07]。

- **Fiber 桌面客户端 Opticrum Desktop 介绍**：Ckroamer 发帖介绍了基于 Opticrum 协议开发的 Fiber 客户端项目，用户可以通过它方便地接入 Fiber 网络，还能通过向流动性市场发布订单解决入金流动性问题；项目内置 Fiber 节点，需要 Rust 和 Node.js 环境[S05]。

- **Fiber 通道协作出资隐私方案讨论**：在 fiber-payjoin-kit 的讨论中，ILE_LABS 表示 Tier 1 不需要修改 FNN，协作构建完全移到通道打开流程之外，通过一个单独的普通支付交易来为通道提供资金[S06]。

- **研究笔记获深入回复**：ArthurZhang 回复了 Mulandi_Cecilia 关于 groth16-ckb 威胁模型、Molecule schema 和 zk-Lock M1 实现的内容，认为 zk-Lock 提供了创建时由 proof 门控的 Lock 配置，VK 和 public-input commitment 固定在锁定 Cell 的 args 中[S04]。

## 值得继续跟进

- **ZK 单词游戏的承诺有效性**：虽然开发者声称电路已经绑定词典成员资格，但 truthixify 补充的“垃圾 commitment 导致无法完成游戏”以及 ArthurZhang 提出的应在 create/join 时验证承诺有效性的问题，仍需要进一步观察作者是否会调整合约逻辑[S01, S03]。

- **Fiber 生态工具的实际落地**：Opticrum Desktop 和 fiber-payjoin-kit 今天都有新讨论，但前者还停留在安装和功能说明阶段，后者关于 tier 结构和外部资金通道的细节也仍需后续验证[S05, S06]。

- **CellScript 0.24 之后的路线**：ArthurZhang 的四个月报告提到了从编译器定位出发的演变，但今天只发布了阶段性总结，后续能否继续保持更新节奏、以及捆绑合约有哪些新能力，值得继续关注[S07]。

## 来源索引

- `S01` [I built a two-player ZK word game on CKB. Come play it](https://talk.nervos.org/t/i-built-a-two-player-zk-word-game-on-ckb-come-play-it/10657/2) | ArthurZhang | 2026-08-28 17:17:22 CST | this is much like a commit–reveal game, and it neutralizes first-mover advantage by deciding the outcome only after both players receive an equal number of attempts. however, create/join should also prove that each commitment represents a valid dictionary word, otherwise a...
- `S02` [I built a two-player ZK word game on CKB. Come play it](https://talk.nervos.org/t/i-built-a-two-player-zk-word-game-on-ckb-come-play-it/10657/3) | truthixify | 2026-08-28 23:32:24 CST | These issues are real, thank you @ArthurZhang
- `S03` [I built a two-player ZK word game on CKB. Come play it](https://talk.nervos.org/t/i-built-a-two-player-zk-word-game-on-ckb-come-play-it/10657/4) | truthixify | 2026-08-28 23:36:52 CST | Although the mastermind circuit binds the commitment to the word and proves dictionary membership, so a junk commitment means you can never answer at all. A player will enter a game they can’t finish.
- `S04` [Research Notes: What Zero-Knowledge Proofs Enable on CKB](https://talk.nervos.org/t/research-notes-what-zero-knowledge-proofs-enable-on-ckb/10368/8) | ArthurZhang | 2026-08-28 23:21:21 CST | @Mulandi_Cecilia I went through your groth16-ckb threat model, Molecule schema, and the zk-Lock M1 implementation. Your zk-Lock gives us a concrete creation-time proof-gated Lock profile, with the VK and public-input commitment fixed in the locked Cell’s args. This materially...
- `S05` [[Fiber] Opticrum Desktop: A Fiber GUI with in-bound liquidity capacity](https://talk.nervos.org/t/fiber-opticrum-desktop-a-fiber-gui-with-in-bound-liquidity-capacity/10669/1) | Ckroamer | 2026-08-28 22:47:54 CST | Q1：这是个什么项目？ 基于 Opticrum 协议进行开发的 Fiber 客户端项目，用户能使用它便利地接入 Fiber 网络，同时还能通过向流动性市场发布订单来解决入金流动性问题。 Q2：如何使用该项目？ 需要提前安装 Rust 和 NodeJs。 $ git clone https://github.com/Opticrum/desktop-wallet && cd desktop-wallet $ npm i $ npm run tauri:dev Q3：项目有哪些特点？ 内置节点：内置了 Fiber 节点，表单化了 Fiber...
- `S06` [[DIS] fiber-payjoin-kit: Collaborative Channel Funding Privacy for the Nervos Fiber Network RES](https://talk.nervos.org/t/dis-fiber-payjoin-kit-collaborative-channel-funding-privacy-for-the-nervos-fiber-network-res/10604/4) | Ckroamer | 2026-08-28 22:29:22 CST | ILE_LABS: Tier 1 requires no fnn changes. The collaborative construction moves entirely outside the channel open, into a separate ordinary payment transaction whose output then funds the channel through open_channel_with_external_funding / submit_signed_funding_tx, which...
- `S07` [CellScript - A DSL for Cell-Based Contracts](https://talk.nervos.org/t/cellscript-a-dsl-for-cell-based-contracts/10193/31) | ArthurZhang | 2026-08-28 11:28:55 CST | Four Months of CellScript: What Changed from 0.12 to 0.24 A Q2 and Q3-to-date 2026 project report for the Nervos community When I posted CellScript 0.12 in April, I thought of it mainly as a compiler that had finally earned a clear release boundary. The bundled contracts...

## 活跃话题

1. [I built a two-player ZK word game on CKB. Come play it](https://talk.nervos.org/t/i-built-a-two-player-zk-word-game-on-ckb-come-play-it/10657) | 3 条近窗帖子 | 最新活动 2026-08-28 23:36:52 CST | tags: CKB, testnet
2. [Research Notes: What Zero-Knowledge Proofs Enable on CKB](https://talk.nervos.org/t/research-notes-what-zero-knowledge-proofs-enable-on-ckb/10368) | 1 条近窗帖子 | 最新活动 2026-08-28 23:21:21 CST | tags: CKB-VM, architecture, groth16, lang-en, sp1, zero-knowledge, zkvm
3. [[Fiber] Opticrum Desktop: A Fiber GUI with in-bound liquidity capacity](https://talk.nervos.org/t/fiber-opticrum-desktop-a-fiber-gui-with-in-bound-liquidity-capacity/10669) | 1 条近窗帖子 | 最新活动 2026-08-28 22:47:54 CST
4. [[DIS] fiber-payjoin-kit: Collaborative Channel Funding Privacy for the Nervos Fiber Network RES](https://talk.nervos.org/t/dis-fiber-payjoin-kit-collaborative-channel-funding-privacy-for-the-nervos-fiber-network-res/10604) | 1 条近窗帖子 | 最新活动 2026-08-28 22:29:22 CST
5. [CellScript - A DSL for Cell-Based Contracts](https://talk.nervos.org/t/cellscript-a-dsl-for-cell-based-contracts/10193) | 1 条近窗帖子 | 最新活动 2026-08-28 11:28:55 CST | tags: CKB-VM, CellScript, DSL, lang-en

## 最近帖子摘录

- 2026-08-28 23:36:52 CST | truthixify | [I built a two-player ZK word game on CKB. Come play it](https://talk.nervos.org/t/i-built-a-two-player-zk-word-game-on-ckb-come-play-it/10657/4) | Although the mastermind circuit binds the commitment to the word and proves dictionary membership, so a junk commitment means you can never answer at all. A player will enter a...
- 2026-08-28 23:32:24 CST | truthixify | [I built a two-player ZK word game on CKB. Come play it](https://talk.nervos.org/t/i-built-a-two-player-zk-word-game-on-ckb-come-play-it/10657/3) | These issues are real, thank you @ArthurZhang
- 2026-08-28 23:21:21 CST | ArthurZhang | [Research Notes: What Zero-Knowledge Proofs Enable on CKB](https://talk.nervos.org/t/research-notes-what-zero-knowledge-proofs-enable-on-ckb/10368/8) | @Mulandi_Cecilia I went through your groth16-ckb threat model, Molecule schema, and the zk-Lock M1 implementation. Your zk-Lock gives us a concrete creation-time proof-gated...
- 2026-08-28 22:47:54 CST | Ckroamer | [[Fiber] Opticrum Desktop: A Fiber GUI with in-bound liquidity capacity](https://talk.nervos.org/t/fiber-opticrum-desktop-a-fiber-gui-with-in-bound-liquidity-capacity/10669/1) | Q1：这是个什么项目？ 基于 Opticrum 协议进行开发的 Fiber 客户端项目，用户能使用它便利地接入 Fiber 网络，同时还能通过向流动性市场发布订单来解决入金流动性问题。 Q2：如何使用该项目？ 需要提前安装 Rust 和 NodeJs。 $ git clone https://github.com/Opticrum/desktop-...
- 2026-08-28 22:29:22 CST | Ckroamer | [[DIS] fiber-payjoin-kit: Collaborative Channel Funding Privacy for the Nervos Fiber Network RES](https://talk.nervos.org/t/dis-fiber-payjoin-kit-collaborative-channel-funding-privacy-for-the-nervos-fiber-network-res/10604/4) | ILE_LABS: Tier 1 requires no fnn changes. The collaborative construction moves entirely outside the channel open, into a separate ordinary payment transaction whose output then...
- 2026-08-28 17:17:22 CST | ArthurZhang | [I built a two-player ZK word game on CKB. Come play it](https://talk.nervos.org/t/i-built-a-two-player-zk-word-game-on-ckb-come-play-it/10657/2) | this is much like a commit–reveal game, and it neutralizes first-mover advantage by deciding the outcome only after both players receive an equal number of attempts. however,...
- 2026-08-28 11:28:55 CST | ArthurZhang | [CellScript - A DSL for Cell-Based Contracts](https://talk.nervos.org/t/cellscript-a-dsl-for-cell-based-contracts/10193/31) | Four Months of CellScript: What Changed from 0.12 to 0.24 A Q2 and Q3-to-date 2026 project report for the Nervos community When I posted CellScript 0.12 in April, I thought of...
