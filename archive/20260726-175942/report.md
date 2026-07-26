# Nervos Talk 社区简报

- 统计窗口: 2026-07-26 01:59:42 CST 到 2026-07-27 01:59:42 CST
- 生成时间: 2026-07-27 01:59:53 CST
- 话题数: 10
- 帖子数: 17
- 作者数: 11
- 总结模式: ai:openrouter

## 社区总结

## 今日发生了什么

今天论坛整体较为活跃，多个 Spark 项目持续推进，开发者工具 ckb-viz 上线了交互式入门教程，帮助新人理解 CKB 的 Cell 模型。[S01] 同时，围绕 Myelin 这一链下 Cell 会话运行时的讨论升温，社区成员就"链下执行+链上验证"是否等同于 GameFi 展开了观点交锋。[S13, S14]

## 重点话题

- **ckb-viz 新增交互式入门教程**：开发者 truthixify 在 /learn 页面推出了面向 CKB 新手的可视化教程，用"存钱罐作钱包、硬币作 Cell"的比喻讲解余额模型，这一需求来自上次 CKBuilder 会议中 neon 的反馈。[S01] 同时 knmo 提供了一则难以解析的交易哈希，供工具测试改进。[S02]

- **Fiber 生态两个项目更新**：Spark 项目"Fiber Submarine Swap Service"团队根据 xingtianchunyan 的详细反馈全面修订了提案，补充了项目类型说明和核心团队成员信息。[S03] 另一项目 FiberLatch Access 发布了获批后的首份双周进度报告，目前处于可复用访问包的设计阶段，尚未进入代码实现。[S04]

- **Cellar 容量租赁市场重构设计**：Carlos_Bunny 在收到反馈后承认此前技术表述过度设计，提出将 Cellar 的逻辑从"自定义 Lock + 自定义 Type"双脚本方案改为更简洁的 Type-only 架构，以避免跨脚本协调问题。[S07, S08]

- **论坛工具讨论**：ArthurZhang 回应了 Mermaid 图表插件与 Babel 翻译层的兼容性问题，初步判断两者在 Markdown 层面可共存，但指出 Mermaid 节点标签内的文本会被 Babel 当作不透明代码块原样保留，无法自动翻译。[S10, S11]

- **Myelin 定位之争**：xxuejie 明确表态自己只做游戏基础设施，"区块链只是数据库"，拒绝被归入 GameFi；ArthurZhang 则区分了"协议层"与"应用层"，认为链下游戏+链上验证的架构本身不等于 GameFi，并强调 Myelin 与 ZK 方案的核心差异在于保留原生 CKB 语义而非电路表示。[S13, S14, S15]

## 值得继续跟进

- **Cellar 技术方案的最终落地**：Carlos_Bunny 已承诺会更谨慎地修订提案，但 Type-only 重构是否会影响安全假设或审计范围，有待下一版提案确认。[S07, S08]

- **FiberLatch Access 从设计转入实现的节奏**：目前仅完成 Weeks 1–2 的设计阶段，后续开发进度和代码开源时间值得关注。[S04]

- **Mermaid 插件的翻译体验**：若部署后中文社区的技术图表出现大量未翻译英文标签，可能需要额外的本地化方案或社区协作流程。[S11]

## 来源索引

- `S01` [Ckb-viz: read any CKB transaction as a flow of cells](https://talk.nervos.org/t/ckb-viz-read-any-ckb-transaction-as-a-flow-of-cells/10482/8) | truthixify | 2026-07-26 22:44:13 CST | Quick update: ckb-viz now has an interactive primer at /learn for folks new to CKB. It came out of a request from neon at the last CKBuilder meeting. It walks through the cell model using a piggy bank for a wallet and coins for cells: a balance as a set of coins, what a lock...
- `S02` [Ckb-viz: read any CKB transaction as a flow of cells](https://talk.nervos.org/t/ckb-viz-read-any-ckb-transaction-as-a-flow-of-cells/10482/9) | knmo | 2026-07-26 23:58:43 CST | truthixify: hard-to-decode transaction hashes very welcome. 0x1166ca65353a5cdd3379229280e2805d9065c9b39f3e11d4cf3352542aeef996
- `S03` [Spark Program | Fiber Submarine Swap Service](https://talk.nervos.org/t/spark-program-fiber-submarine-swap-service/10516/3) | George_Liam | 2026-07-26 21:58:27 CST | Hi @xingtianchunyan, Thank you for the detailed feedback — we’ve revised the proposal in full. The updated version addresses all points raised: The project type is now explicitly stated in the overview. The team section includes all core members with names, roles, background,...
- `S04` [[DIS] FiberLatch Access - Open-Source Access Control for Fiber Payments](https://talk.nervos.org/t/dis-fiberlatch-access-open-source-access-control-for-fiber-payments/10414/4) | Ticoworld | 2026-07-26 20:12:05 CST | FiberLatch Access — Weeks 1–2 Progress Update Hi everyone, Here is the first progress update for FiberLatch Access since the proposal was approved. The work for Weeks 1–2 focused on defining how the reusable access package should work before implementation begins. That phase...
- `S05` [CKB DevLaunch Kit](https://talk.nervos.org/t/ckb-devlaunch-kit/10476/5) | CrptoHead | 2026-07-26 17:24:18 CST | hello @xingtianchunyan The changes have been intergrated as requested. Regards Cryptogead
- `S06` [[DIS] Decentralized privacy order-book appchain based on CKB L1 - 2026.phase-1](https://talk.nervos.org/t/dis-decentralized-privacy-order-book-appchain-based-on-ckb-l1-2026-phase-1/10015/37) | Lawliet_Chan | 2026-07-26 17:12:47 CST | 周报 2026.7.26 使用renegade的mpc-jelly和ark-mpc的 co-zk库 来开发： cozk2p: complete 2-party collaborative-ZK settlement e2e by dreamATD · Pull Request #9 · invisibook-lab/invisibook · GitHub
- `S07` [Spark Program | Cellar — A Capacity Leasing Market for CKB Cells](https://talk.nervos.org/t/spark-program-cellar-a-capacity-leasing-market-for-ckb-cells/10492/8) | Carlos_Bunny | 2026-07-26 16:15:13 CST | Hi , thanks for the direct feedback. Point taken on both the technical accuracy and the formatting. That is on me, and I’ll be more careful before posting a revision. You’re right that I overstated the need for both a custom CellarLeaseLock and CellarLeaseType. The cleaner...
- `S08` [Spark Program | Cellar — A Capacity Leasing Market for CKB Cells](https://talk.nervos.org/t/spark-program-cellar-a-capacity-leasing-market-for-ckb-cells/10492/9) | Carlos_Bunny | 2026-07-26 16:17:34 CST | My previous framing split Cellar-specific logic across a custom lock and custom type script, which creates the coordination problem you described: mode, witness format, identities, and transition classification all have to line up across two scripts. A cleaner design is type-...
- `S09` [Forum tooling suggestion: Mermaid diagram support for technical posts](https://talk.nervos.org/t/forum-tooling-suggestion-mermaid-diagram-support-for-technical-posts/10391/3) | phroi | 2026-07-26 07:42:15 CST | I support this, just I wonder how it would interplay with Babel our translation layer, which if you notice already disable some Discourse-native features: [ANN]The Babel Reunited translation plugin has started public beta testing in the DAO category CKB Community Fund DAO...
- `S10` [Forum tooling suggestion: Mermaid diagram support for technical posts](https://talk.nervos.org/t/forum-tooling-suggestion-mermaid-diagram-support-for-technical-posts/10391/4) | ArthurZhang | 2026-07-26 12:05:27 CST | Hey Phroi, thank you for bringing up this, I actually had gone through both repos earlier this week and i think so far the two plugins are generally compatible at the markdown layer (Mermaid blocks should survive translation end-to-end), though they share a real client-side...
- `S11` [Forum tooling suggestion: Mermaid diagram support for technical posts](https://talk.nervos.org/t/forum-tooling-suggestion-mermaid-diagram-support-for-technical-posts/10391/5) | ArthurZhang | 2026-07-26 12:09:07 CST | And just mentioning this, it seems mermaid labels will not be translated if both plugins are deployed in a vanilla manner, because Babel Reunited seems to treat ```mermaid as an opaque code block, the text inside Mermaid node labels (e.g. A[用户点击发送]) is passed through verbatim,...
- `S12` [Introducing Myelin: a CKB-aligned off-chain Cell session runtime](https://talk.nervos.org/t/introducing-myelin-a-ckb-aligned-off-chain-cell-session-runtime/10498/5) | phroi | 2026-07-26 07:37:35 CST | Hey @ArthurZhang, thank you for building on top of @xxuejie original work, I find all this fascinating and it showcases the real strengths of CKB. Feels like quite a few protocols had to reinvent this very piece of logic, thinking for example about WarSpore: [DIS] WarSpore ·...
- `S13` [Introducing Myelin: a CKB-aligned off-chain Cell session runtime](https://talk.nervos.org/t/introducing-myelin-a-ckb-aligned-off-chain-cell-session-runtime/10498/6) | xxuejie | 2026-07-26 10:06:52 CST | I’m sorry, you can treat this as a rant, but I want to clearify one thing: I’m experimenting infrastructure for games, games only, nothing but games. I want to go back old school where blockchains are just databases. I actually thought hard on this (someone I deeply respect...
- `S14` [Introducing Myelin: a CKB-aligned off-chain Cell session runtime](https://talk.nervos.org/t/introducing-myelin-a-ckb-aligned-off-chain-cell-session-runtime/10498/7) | ArthurZhang | 2026-07-26 11:32:20 CST | I think a distinction is worth preserving here. An off-chain game whose execution is verified on-chain does not, merely by virtue of that architecture, become GameFi. GameFi is an application-level economic category, not a property of the protocol beneath it. As a protocol...
- `S15` [Introducing Myelin: a CKB-aligned off-chain Cell session runtime](https://talk.nervos.org/t/introducing-myelin-a-ckb-aligned-off-chain-cell-session-runtime/10498/8) | ArthurZhang | 2026-07-26 11:49:17 CST | @phroi, the main distinction from ZK, as I see it, is that Myelin preserves native CKB semantics rather than proving a circuit representation of them. A disputed transition remains a CKB-shaped chunk executed by CKB-VM, which makes integration with existing programmes...
- `S16` [PactAgent: From Application to Infrastructure](https://talk.nervos.org/t/pactagent-from-application-to-infrastructure/10352/5) | Ajay | 2026-07-26 06:19:59 CST | Hi everyone, I’d like to share a new developer update on PactAgent and get feedback from the Nervos CKB community. PactAgent has moved from being a single end-user agreement/payment app to a reusable, app-scoped agreement and escrow infrastructure layer, exposed via a...
- `S17` [Jan Xie：区块链抽象与演进](https://talk.nervos.org/t/jan-xie/6241/11) | knmo | 2026-07-26 02:43:49 CST | yixiu.ckbfans.bit: 不得不说，这是具有超前远见的分享。 0xshushu: 到了24年中，这篇文章似乎还是不过时。 預計在2026年或隨後的幾年裡，上述內容的重要性將在公眾中更加顯現。

## 活跃话题

1. [Ckb-viz: read any CKB transaction as a flow of cells](https://talk.nervos.org/t/ckb-viz-read-any-ckb-transaction-as-a-flow-of-cells/10482) | 2 条近窗帖子 | 最新活动 2026-07-26 23:58:43 CST | tags: CKB, CKB-VM, dapp, lang-en
2. [Spark Program | Fiber Submarine Swap Service](https://talk.nervos.org/t/spark-program-fiber-submarine-swap-service/10516) | 1 条近窗帖子 | 最新活动 2026-07-26 21:58:27 CST | tags: Spark-Program
3. [[DIS] FiberLatch Access - Open-Source Access Control for Fiber Payments](https://talk.nervos.org/t/dis-fiberlatch-access-open-source-access-control-for-fiber-payments/10414) | 1 条近窗帖子 | 最新活动 2026-07-26 20:12:05 CST | tags: CKB, dapp, testnet
4. [CKB DevLaunch Kit](https://talk.nervos.org/t/ckb-devlaunch-kit/10476) | 1 条近窗帖子 | 最新活动 2026-07-26 17:24:18 CST | tags: Spark-Program, Submitted
5. [[DIS] Decentralized privacy order-book appchain based on CKB L1 - 2026.phase-1](https://talk.nervos.org/t/dis-decentralized-privacy-order-book-appchain-based-on-ckb-l1-2026-phase-1/10015) | 1 条近窗帖子 | 最新活动 2026-07-26 17:12:47 CST | tags: appchain
6. [Spark Program | Cellar — A Capacity Leasing Market for CKB Cells](https://talk.nervos.org/t/spark-program-cellar-a-capacity-leasing-market-for-ckb-cells/10492) | 2 条近窗帖子 | 最新活动 2026-07-26 16:17:34 CST | tags: Spark-Program, Submitted
7. [Forum tooling suggestion: Mermaid diagram support for technical posts](https://talk.nervos.org/t/forum-tooling-suggestion-mermaid-diagram-support-for-technical-posts/10391) | 3 条近窗帖子 | 最新活动 2026-07-26 12:09:07 CST
8. [Introducing Myelin: a CKB-aligned off-chain Cell session runtime](https://talk.nervos.org/t/introducing-myelin-a-ckb-aligned-off-chain-cell-session-runtime/10498) | 4 条近窗帖子 | 最新活动 2026-07-26 11:49:17 CST | tags: CKB-VM, CellScript, lang-en
9. [PactAgent: From Application to Infrastructure](https://talk.nervos.org/t/pactagent-from-application-to-infrastructure/10352) | 1 条近窗帖子 | 最新活动 2026-07-26 06:19:59 CST | tags: CKB, CKB-VM, dapp, lang-en
10. [Jan Xie：区块链抽象与演进](https://talk.nervos.org/t/jan-xie/6241) | 1 条近窗帖子 | 最新活动 2026-07-26 02:43:49 CST | tags: lang-zh

## 最近帖子摘录

- 2026-07-26 23:58:43 CST | knmo | [Ckb-viz: read any CKB transaction as a flow of cells](https://talk.nervos.org/t/ckb-viz-read-any-ckb-transaction-as-a-flow-of-cells/10482/9) | truthixify: hard-to-decode transaction hashes very welcome. 0x1166ca65353a5cdd3379229280e2805d9065c9b39f3e11d4cf3352542aeef996
- 2026-07-26 22:44:13 CST | truthixify | [Ckb-viz: read any CKB transaction as a flow of cells](https://talk.nervos.org/t/ckb-viz-read-any-ckb-transaction-as-a-flow-of-cells/10482/8) | Quick update: ckb-viz now has an interactive primer at /learn for folks new to CKB. It came out of a request from neon at the last CKBuilder meeting. It walks through the cell...
- 2026-07-26 21:58:27 CST | George_Liam | [Spark Program | Fiber Submarine Swap Service](https://talk.nervos.org/t/spark-program-fiber-submarine-swap-service/10516/3) | Hi @xingtianchunyan, Thank you for the detailed feedback — we’ve revised the proposal in full. The updated version addresses all points raised: The project type is now...
- 2026-07-26 20:12:05 CST | Ticoworld | [[DIS] FiberLatch Access - Open-Source Access Control for Fiber Payments](https://talk.nervos.org/t/dis-fiberlatch-access-open-source-access-control-for-fiber-payments/10414/4) | FiberLatch Access — Weeks 1–2 Progress Update Hi everyone, Here is the first progress update for FiberLatch Access since the proposal was approved. The work for Weeks 1–2...
- 2026-07-26 17:24:18 CST | CrptoHead | [CKB DevLaunch Kit](https://talk.nervos.org/t/ckb-devlaunch-kit/10476/5) | hello @xingtianchunyan The changes have been intergrated as requested. Regards Cryptogead
- 2026-07-26 17:12:47 CST | Lawliet_Chan | [[DIS] Decentralized privacy order-book appchain based on CKB L1 - 2026.phase-1](https://talk.nervos.org/t/dis-decentralized-privacy-order-book-appchain-based-on-ckb-l1-2026-phase-1/10015/37) | 周报 2026.7.26 使用renegade的mpc-jelly和ark-mpc的 co-zk库 来开发： cozk2p: complete 2-party collaborative-ZK settlement e2e by dreamATD · Pull Request #9 · invisibook-lab/invisibook · GitHub
- 2026-07-26 16:17:34 CST | Carlos_Bunny | [Spark Program | Cellar — A Capacity Leasing Market for CKB Cells](https://talk.nervos.org/t/spark-program-cellar-a-capacity-leasing-market-for-ckb-cells/10492/9) | My previous framing split Cellar-specific logic across a custom lock and custom type script, which creates the coordination problem you described: mode, witness format,...
- 2026-07-26 16:15:13 CST | Carlos_Bunny | [Spark Program | Cellar — A Capacity Leasing Market for CKB Cells](https://talk.nervos.org/t/spark-program-cellar-a-capacity-leasing-market-for-ckb-cells/10492/8) | Hi , thanks for the direct feedback. Point taken on both the technical accuracy and the formatting. That is on me, and I’ll be more careful before posting a revision. You’re...
- 2026-07-26 12:09:07 CST | ArthurZhang | [Forum tooling suggestion: Mermaid diagram support for technical posts](https://talk.nervos.org/t/forum-tooling-suggestion-mermaid-diagram-support-for-technical-posts/10391/5) | And just mentioning this, it seems mermaid labels will not be translated if both plugins are deployed in a vanilla manner, because Babel Reunited seems to treat ```mermaid as an...
- 2026-07-26 12:05:27 CST | ArthurZhang | [Forum tooling suggestion: Mermaid diagram support for technical posts](https://talk.nervos.org/t/forum-tooling-suggestion-mermaid-diagram-support-for-technical-posts/10391/4) | Hey Phroi, thank you for bringing up this, I actually had gone through both repos earlier this week and i think so far the two plugins are generally compatible at the markdown...
- 2026-07-26 11:49:17 CST | ArthurZhang | [Introducing Myelin: a CKB-aligned off-chain Cell session runtime](https://talk.nervos.org/t/introducing-myelin-a-ckb-aligned-off-chain-cell-session-runtime/10498/8) | @phroi, the main distinction from ZK, as I see it, is that Myelin preserves native CKB semantics rather than proving a circuit representation of them. A disputed transition...
- 2026-07-26 11:32:20 CST | ArthurZhang | [Introducing Myelin: a CKB-aligned off-chain Cell session runtime](https://talk.nervos.org/t/introducing-myelin-a-ckb-aligned-off-chain-cell-session-runtime/10498/7) | I think a distinction is worth preserving here. An off-chain game whose execution is verified on-chain does not, merely by virtue of that architecture, become GameFi. GameFi is...
- 2026-07-26 10:06:52 CST | xxuejie | [Introducing Myelin: a CKB-aligned off-chain Cell session runtime](https://talk.nervos.org/t/introducing-myelin-a-ckb-aligned-off-chain-cell-session-runtime/10498/6) | I’m sorry, you can treat this as a rant, but I want to clearify one thing: I’m experimenting infrastructure for games, games only, nothing but games. I want to go back old...
- 2026-07-26 07:42:15 CST | phroi | [Forum tooling suggestion: Mermaid diagram support for technical posts](https://talk.nervos.org/t/forum-tooling-suggestion-mermaid-diagram-support-for-technical-posts/10391/3) | I support this, just I wonder how it would interplay with Babel our translation layer, which if you notice already disable some Discourse-native features: [ANN]The Babel...
- 2026-07-26 07:37:35 CST | phroi | [Introducing Myelin: a CKB-aligned off-chain Cell session runtime](https://talk.nervos.org/t/introducing-myelin-a-ckb-aligned-off-chain-cell-session-runtime/10498/5) | Hey @ArthurZhang, thank you for building on top of @xxuejie original work, I find all this fascinating and it showcases the real strengths of CKB. Feels like quite a few...
- 2026-07-26 06:19:59 CST | Ajay | [PactAgent: From Application to Infrastructure](https://talk.nervos.org/t/pactagent-from-application-to-infrastructure/10352/5) | Hi everyone, I’d like to share a new developer update on PactAgent and get feedback from the Nervos CKB community. PactAgent has moved from being a single end-user...
- 2026-07-26 02:43:49 CST | knmo | [Jan Xie：区块链抽象与演进](https://talk.nervos.org/t/jan-xie/6241/11) | yixiu.ckbfans.bit: 不得不说，这是具有超前远见的分享。 0xshushu: 到了24年中，这篇文章似乎还是不过时。 預計在2026年或隨後的幾年裡，上述內容的重要性將在公眾中更加顯現。
