# Nervos Talk 社区简报

- 统计窗口: 2026-06-12 03:03:19 CST 到 2026-06-13 03:03:19 CST
- 生成时间: 2026-06-13 03:03:27 CST
- 话题数: 10
- 帖子数: 18
- 作者数: 13
- 总结模式: ai:openrouter

## 社区总结

## 今日发生了什么

社区今天围绕 Nervos 生态的技术进展展开活跃讨论，Fiber 支付通道方案 [S07, S08]、跨链互操作协议 [S13, S14, S15, S16] 和开发者工具 [S12] 均有新动态。同时，一位社区成员发现官网 /ckbpage 页面存在专业性问题 [S03]，已获官方团队回应 [S05] 并转交维护团队处理 [S05]。

## 重点话题

- **Fiber 流动性方案引发深度讨论**：quake 解释了 Fiber 计划引入类似 LND Loop 的流动性管理功能，结合 MPP（多路径支付）降低对 Splicing 的需求，从而简化 Amboss 等流动性市场的角色定位 [S07]；Ckroamer 则提出不同视角，认为 Amboss 的核心价值不仅在于撮合流动性，更在于提供"质押收入"这类 DeFi 属性，闪电网络生态对此存在真实需求 [S08]。

- **Morph Channel 新方案发布**：ArthurZhang 发布了面向公众的 Morph Channel 解释文章，该方案旨在 CKB 上将价值、状态证据和费用责任分离，并提供了对应的中文草案 [S09]。

- **Chiral 跨链协议获核心开发者关注**：janx 与 T_Silva 就 Chiral 对称同构绑定协议展开多轮技术对话，确认该协议用双向链上轻客户端验证替代客户端验证，CKB 将通过 Mithril 证书验证器验证 Cardano 状态，用户可在 CKB 和 Cardano 之间无桥铸造和转移资产 [S13, S14, S15, S16]。

- **开发者工具 CellKit Actions 亮相**：Fidelcoder 团队发布 CellKit Actions，提供可复用的 CKB 交易操作组件，以降低应用开发中重复处理底层 Cell 逻辑的门槛 [S12]。

- **Fiber Desktop 资助进入拨款流程**：ebubedev 的 V1 重建提案投票通过后，询问 25% 启动款支付时间；zz_tovarishch 确认已通知委员会拨款，通常需 1-2 周处理 [S10, S11]。

## 值得继续跟进

- **官网 /ckbpage 页面的整改结果**：knmo 指出该页面搜索排名靠前但显得不专业 [S03]，zz_tovarishch 已转交维护团队 [S05]，需观察后续是否重定向至 Rewards 页面 [S06] 及 typo 修复 [S06]。

- **Pocket Node Android 轻客户端的下一版发布**：Jnr6 表示同步问题已修复并将包含在下次发布中，已在 devnet 和 testnet 完成长历史钱包测试，正在收集用户反馈 [S02]。

- **Spark 激励计划与 Holdem Bulls 的关联**：Hbulls 询问扑克项目与 Spark 激励计划的关系，目前尚未获得明确回复 [S01]。

## 来源索引

- `S01` [Bringing poker back to Nervos - introducing Holdem Bulls V1](https://talk.nervos.org/t/bringing-poker-back-to-nervos-introducing-holdem-bulls-v1/10310/17) | Hbulls | 2026-06-13 02:12:27 CST | hi and thank you for the reply. how does this apply to spark incentive program? regards
- `S02` [[DIS] Mobile-Ready CKB Light Client (Pocket Node) for Android](https://talk.nervos.org/t/dis-mobile-ready-ckb-light-client-pocket-node-for-android/9879/56) | Jnr6 | 2026-06-13 02:05:12 CST | By the way, this is fixed and will be part of the next release. I did a lot of work on the syncing too and tested it with devnet and testnet and synced a wallet with a very long history, and it worked fine. I’d like your feedback on the issue you encountered. Also, can you...
- `S03` [/ckbpage](https://talk.nervos.org/t/ckbpage/10377/1) | knmo | 2026-06-12 22:01:37 CST | That looks unprofessional. Should this really remain on the official Nervos.Org website? /ckbpage This website appeared as the top search result when I typed “ckb Secondary Issuance” into Startpage.com search. https://www.nervos.org/ckbpage “The base issuance is 33.6 billion...
- `S04` [/ckbpage](https://talk.nervos.org/t/ckbpage/10377/2) | knmo | 2026-06-12 22:25:59 CST | @pph janewuco janecryptoto cryptoto (jane) · GitHub X (formerly Twitter) Jane Wu (@janewuco) on X common knowledge base @nervosnetwork
- `S05` [/ckbpage](https://talk.nervos.org/t/ckbpage/10377/3) | zz_tovarishch | 2026-06-12 22:44:52 CST | Hi Knmo 感谢您发现的问题，已经将问题转给维护团队
- `S06` [/ckbpage](https://talk.nervos.org/t/ckbpage/10377/4) | knmo | 2026-06-13 00:32:34 CST | Perhaps you might decide to redirect to this excellent website: Rewards | Nervos CKB In any case, there’s also a small typo there: “This a two-step confirmation process […]” Delete letter ”a”
- `S07` [[Fiber] CKB 能让 Fiber 拥有更好的 Amboss](https://talk.nervos.org/t/fiber-ckb-fiber-amboss/10353/2) | quake | 2026-06-12 10:26:01 CST | Fiber 目前的计划是引入类似 LND Loop 的流动性管理功能，使节点运营者能够在不修改 Channel 结构的情况下灵活调整入站和出站流动性，因为在有 MPP 支持的情况下，针对一个通道做 Splicing 其实并不是高需求的场景。对于大多数实际场景，Loop 加 MPP 已经能够满足流动性管理需求，因此像 Amboss 或者 Magma 这类流动性市场所需要承担的职责会大幅简化。它们更多只需要扮演流动性提供者发现和撮合的平台角色，而不再需要围绕复杂的 Channel...
- `S08` [[Fiber] CKB 能让 Fiber 拥有更好的 Amboss](https://talk.nervos.org/t/fiber-ckb-fiber-amboss/10353/3) | Ckroamer | 2026-06-12 22:47:13 CST | Amboss 的意义更多的在于提供流动性撮合的同时，给生态提供金融性质的 “质押收入”，并不只是简单的解决流动性问题 LND 是使用最多的闪电网络节点，但 Amboss 仍然能在闪电网络生态中占有一定席位，足以说明大家对于闪电网络 Defi 其实是有需求的
- `S09` [Morph Channel Explained: Separating Value, State Evidence, and Fee Responsibility on CKB](https://talk.nervos.org/t/morph-channel-explained-separating-value-state-evidence-and-fee-responsibility-on-ckb/10378/1) | ArthurZhang | 2026-06-12 22:10:42 CST | (This is a general-public-facing companion to the June 2026 Morph Channel paper. The paper is the canonical specification; this article is an audience-friendly explainer. Also there is an original draft proposal written in Chinese ) The one-line summary: Morph Channel is a...
- `S10` [[DIS] Fiber Desktop v1 ground-up rebuild and launch — fnn desktop app](https://talk.nervos.org/t/dis-fiber-desktop-v1-ground-up-rebuild-and-launch-fnn-desktop-app/10317/14) | ebubedev | 2026-06-12 17:38:53 CST | The [VOT] proposal has passed (thank you @zz_tovarishch for verification). I’m ready to begin the 3-month v1 build on the agreed schedule. Could the DAO Funds Management Committee confirm the timeline for the grant commencement payment (25%)?
- `S11` [[DIS] Fiber Desktop v1 ground-up rebuild and launch — fnn desktop app](https://talk.nervos.org/t/dis-fiber-desktop-v1-ground-up-rebuild-and-launch-fnn-desktop-app/10317/15) | zz_tovarishch | 2026-06-12 20:26:26 CST | Hi Edbubedev, 在投票确认通过时，就已经通知委员会进行启动款项拨款，一般需要等待1-2周的处理时间，感谢您的耐心等待
- `S12` [CellKit Actions — Reusable Transaction Actions for CKB Apps](https://talk.nervos.org/t/cellkit-actions-reusable-transaction-actions-for-ckb-apps/10375/1) | Fidelcoder | 2026-06-12 16:39:22 CST | Team Profile & Contact Applicant: Fidelcoder GitHub: FidelCoder (Fidel) · GitHub Role: Blockchain Engineer Telegram: @GriffinsOduol Email: griffinesonyango@gmail.com ** Project Description** Problem Building CKB applications requires developers to repeatedly handle low-level...
- `S13` [Chiral - Symmetric isomorphic binding: a committee-free, anchor-agnostic protocol where each chain verifies the other with a succinct on-chain light client](https://talk.nervos.org/t/chiral-symmetric-isomorphic-binding-a-committee-free-anchor-agnostic-protocol-where-each-chain-verifies-the-other-with-a-succinct-on-chain-light-client/10360/4) | T_Silva | 2026-06-12 03:37:42 CST | Thanks sharp catch, and you’re right that we’re overloading “leap” relative to RGB++. Let me answer your direct question first, then the terminology. Does ownership ever come to CKB? Yes, the leap is symmetric. The bound cell hosted on CKB toggles its controlling seal between...
- `S14` [Chiral - Symmetric isomorphic binding: a committee-free, anchor-agnostic protocol where each chain verifies the other with a succinct on-chain light client](https://talk.nervos.org/t/chiral-symmetric-isomorphic-binding-a-committee-free-anchor-agnostic-protocol-where-each-chain-verifies-the-other-with-a-succinct-on-chain-light-client/10360/5) | janx | 2026-06-12 09:51:51 CST | @T_Silva Thanks, I’m starting to get the gist now. What I find interesting and new (correct me if I’m wrong): The “RGB++ like path” is for user-defined tokens. Users can mint Chiral assets - whose seals and values are split on CKB and Cardano - and transfer them bridgelessly...
- `S15` [Chiral - Symmetric isomorphic binding: a committee-free, anchor-agnostic protocol where each chain verifies the other with a succinct on-chain light client](https://talk.nervos.org/t/chiral-symmetric-isomorphic-binding-a-committee-free-anchor-agnostic-protocol-where-each-chain-verifies-the-other-with-a-succinct-on-chain-light-client/10360/6) | T_Silva | 2026-06-12 10:17:13 CST | Thanks, this is a really good read of it, and you have the most important piece exactly right. The part you nailed, Chiral replaces client-side validation with mutual on-chain light-client verification. CKB verifies Cardano by running a Mithril certificate verifier inside CKB-...
- `S16` [Chiral - Symmetric isomorphic binding: a committee-free, anchor-agnostic protocol where each chain verifies the other with a succinct on-chain light client](https://talk.nervos.org/t/chiral-symmetric-isomorphic-binding-a-committee-free-anchor-agnostic-protocol-where-each-chain-verifies-the-other-with-a-succinct-on-chain-light-client/10360/7) | janx | 2026-06-12 10:38:56 CST | Thanks that’s clear and informative.
- `S17` [Deep Dive into CKB-VM Snapshot V1: Architecture and Design Principles](https://talk.nervos.org/t/deep-dive-into-ckb-vm-snapshot-v1-architecture-and-design-principles/10366/2) | Ebube | 2026-06-12 06:00:32 CST | Informative
- `S18` [Spark Program | Dular](https://talk.nervos.org/t/spark-program-dular/10212/13) | duongja | 2026-06-12 04:04:38 CST | Milestone 2 Report: USSD Interface Milestone 2 focused on making Dular usable from feature phones through a USSD interface. This is important because the target users are mobile money users, not only smartphone or browser wallet users. The USSD implementation is now built and...

## 活跃话题

1. [Bringing poker back to Nervos - introducing Holdem Bulls V1](https://talk.nervos.org/t/bringing-poker-back-to-nervos-introducing-holdem-bulls-v1/10310) | 1 条近窗帖子 | 最新活动 2026-06-13 02:12:27 CST | tags: CKB, QA, Spark-Program, dapp, partnership, testnet
2. [[DIS] Mobile-Ready CKB Light Client (Pocket Node) for Android](https://talk.nervos.org/t/dis-mobile-ready-ckb-light-client-pocket-node-for-android/9879) | 1 条近窗帖子 | 最新活动 2026-06-13 02:05:12 CST | tags: CKB, light-client
3. [/ckbpage](https://talk.nervos.org/t/ckbpage/10377) | 4 条近窗帖子 | 最新活动 2026-06-13 00:32:34 CST
4. [[Fiber] CKB 能让 Fiber 拥有更好的 Amboss](https://talk.nervos.org/t/fiber-ckb-fiber-amboss/10353) | 2 条近窗帖子 | 最新活动 2026-06-12 22:47:13 CST
5. [Morph Channel Explained: Separating Value, State Evidence, and Fee Responsibility on CKB](https://talk.nervos.org/t/morph-channel-explained-separating-value-state-evidence-and-fee-responsibility-on-ckb/10378) | 1 条近窗帖子 | 最新活动 2026-06-12 22:10:42 CST
6. [[DIS] Fiber Desktop v1 ground-up rebuild and launch — fnn desktop app](https://talk.nervos.org/t/dis-fiber-desktop-v1-ground-up-rebuild-and-launch-fnn-desktop-app/10317) | 2 条近窗帖子 | 最新活动 2026-06-12 20:26:26 CST | tags: fiber
7. [CellKit Actions — Reusable Transaction Actions for CKB Apps](https://talk.nervos.org/t/cellkit-actions-reusable-transaction-actions-for-ckb-apps/10375) | 1 条近窗帖子 | 最新活动 2026-06-12 16:39:22 CST | tags: Spark-Program
8. [Chiral - Symmetric isomorphic binding: a committee-free, anchor-agnostic protocol where each chain verifies the other with a succinct on-chain light client](https://talk.nervos.org/t/chiral-symmetric-isomorphic-binding-a-committee-free-anchor-agnostic-protocol-where-each-chain-verifies-the-other-with-a-succinct-on-chain-light-client/10360) | 4 条近窗帖子 | 最新活动 2026-06-12 10:38:56 CST | tags: CKB, Spark-Program, partnership, testnet
9. [Deep Dive into CKB-VM Snapshot V1: Architecture and Design Principles](https://talk.nervos.org/t/deep-dive-into-ckb-vm-snapshot-v1-architecture-and-design-principles/10366) | 1 条近窗帖子 | 最新活动 2026-06-12 06:00:32 CST | tags: CKB-VM
10. [Spark Program | Dular](https://talk.nervos.org/t/spark-program-dular/10212) | 1 条近窗帖子 | 最新活动 2026-06-12 04:04:38 CST | tags: In-Progress, Spark-Program

## 最近帖子摘录

- 2026-06-13 02:12:27 CST | Hbulls | [Bringing poker back to Nervos - introducing Holdem Bulls V1](https://talk.nervos.org/t/bringing-poker-back-to-nervos-introducing-holdem-bulls-v1/10310/17) | hi and thank you for the reply. how does this apply to spark incentive program? regards
- 2026-06-13 02:05:12 CST | Jnr6 | [[DIS] Mobile-Ready CKB Light Client (Pocket Node) for Android](https://talk.nervos.org/t/dis-mobile-ready-ckb-light-client-pocket-node-for-android/9879/56) | By the way, this is fixed and will be part of the next release. I did a lot of work on the syncing too and tested it with devnet and testnet and synced a wallet with a very long...
- 2026-06-13 00:32:34 CST | knmo | [/ckbpage](https://talk.nervos.org/t/ckbpage/10377/4) | Perhaps you might decide to redirect to this excellent website: Rewards | Nervos CKB In any case, there’s also a small typo there: “This a two-step confirmation process […]”...
- 2026-06-12 22:47:13 CST | Ckroamer | [[Fiber] CKB 能让 Fiber 拥有更好的 Amboss](https://talk.nervos.org/t/fiber-ckb-fiber-amboss/10353/3) | Amboss 的意义更多的在于提供流动性撮合的同时，给生态提供金融性质的 “质押收入”，并不只是简单的解决流动性问题 LND 是使用最多的闪电网络节点，但 Amboss 仍然能在闪电网络生态中占有一定席位，足以说明大家对于闪电网络 Defi 其实是有需求的
- 2026-06-12 22:44:52 CST | zz_tovarishch | [/ckbpage](https://talk.nervos.org/t/ckbpage/10377/3) | Hi Knmo 感谢您发现的问题，已经将问题转给维护团队
- 2026-06-12 22:25:59 CST | knmo | [/ckbpage](https://talk.nervos.org/t/ckbpage/10377/2) | @pph janewuco janecryptoto cryptoto (jane) · GitHub X (formerly Twitter) Jane Wu (@janewuco) on X common knowledge base @nervosnetwork
- 2026-06-12 22:10:42 CST | ArthurZhang | [Morph Channel Explained: Separating Value, State Evidence, and Fee Responsibility on CKB](https://talk.nervos.org/t/morph-channel-explained-separating-value-state-evidence-and-fee-responsibility-on-ckb/10378/1) | (This is a general-public-facing companion to the June 2026 Morph Channel paper. The paper is the canonical specification; this article is an audience-friendly explainer. Also...
- 2026-06-12 22:01:37 CST | knmo | [/ckbpage](https://talk.nervos.org/t/ckbpage/10377/1) | That looks unprofessional. Should this really remain on the official Nervos.Org website? /ckbpage This website appeared as the top search result when I typed “ckb Secondary...
- 2026-06-12 20:26:26 CST | zz_tovarishch | [[DIS] Fiber Desktop v1 ground-up rebuild and launch — fnn desktop app](https://talk.nervos.org/t/dis-fiber-desktop-v1-ground-up-rebuild-and-launch-fnn-desktop-app/10317/15) | Hi Edbubedev, 在投票确认通过时，就已经通知委员会进行启动款项拨款，一般需要等待1-2周的处理时间，感谢您的耐心等待
- 2026-06-12 17:38:53 CST | ebubedev | [[DIS] Fiber Desktop v1 ground-up rebuild and launch — fnn desktop app](https://talk.nervos.org/t/dis-fiber-desktop-v1-ground-up-rebuild-and-launch-fnn-desktop-app/10317/14) | The [VOT] proposal has passed (thank you @zz_tovarishch for verification). I’m ready to begin the 3-month v1 build on the agreed schedule. Could the DAO Funds Management...
- 2026-06-12 16:39:22 CST | Fidelcoder | [CellKit Actions — Reusable Transaction Actions for CKB Apps](https://talk.nervos.org/t/cellkit-actions-reusable-transaction-actions-for-ckb-apps/10375/1) | Team Profile & Contact Applicant: Fidelcoder GitHub: FidelCoder (Fidel) · GitHub Role: Blockchain Engineer Telegram: @GriffinsOduol Email: griffinesonyango@gmail.com ** Project...
- 2026-06-12 10:38:56 CST | janx | [Chiral - Symmetric isomorphic binding: a committee-free, anchor-agnostic protocol where each chain verifies the other with a succinct on-chain light client](https://talk.nervos.org/t/chiral-symmetric-isomorphic-binding-a-committee-free-anchor-agnostic-protocol-where-each-chain-verifies-the-other-with-a-succinct-on-chain-light-client/10360/7) | Thanks that’s clear and informative.
- 2026-06-12 10:26:01 CST | quake | [[Fiber] CKB 能让 Fiber 拥有更好的 Amboss](https://talk.nervos.org/t/fiber-ckb-fiber-amboss/10353/2) | Fiber 目前的计划是引入类似 LND Loop 的流动性管理功能，使节点运营者能够在不修改 Channel 结构的情况下灵活调整入站和出站流动性，因为在有 MPP 支持的情况下，针对一个通道做 Splicing 其实并不是高需求的场景。对于大多数实际场景，Loop 加 MPP 已经能够满足流动性管理需求，因此像 Amboss 或者 Magma...
- 2026-06-12 10:17:13 CST | T_Silva | [Chiral - Symmetric isomorphic binding: a committee-free, anchor-agnostic protocol where each chain verifies the other with a succinct on-chain light client](https://talk.nervos.org/t/chiral-symmetric-isomorphic-binding-a-committee-free-anchor-agnostic-protocol-where-each-chain-verifies-the-other-with-a-succinct-on-chain-light-client/10360/6) | Thanks, this is a really good read of it, and you have the most important piece exactly right. The part you nailed, Chiral replaces client-side validation with mutual on-chain...
- 2026-06-12 09:51:51 CST | janx | [Chiral - Symmetric isomorphic binding: a committee-free, anchor-agnostic protocol where each chain verifies the other with a succinct on-chain light client](https://talk.nervos.org/t/chiral-symmetric-isomorphic-binding-a-committee-free-anchor-agnostic-protocol-where-each-chain-verifies-the-other-with-a-succinct-on-chain-light-client/10360/5) | @T_Silva Thanks, I’m starting to get the gist now. What I find interesting and new (correct me if I’m wrong): The “RGB++ like path” is for user-defined tokens. Users can mint...
- 2026-06-12 06:00:32 CST | Ebube | [Deep Dive into CKB-VM Snapshot V1: Architecture and Design Principles](https://talk.nervos.org/t/deep-dive-into-ckb-vm-snapshot-v1-architecture-and-design-principles/10366/2) | Informative
- 2026-06-12 04:04:38 CST | duongja | [Spark Program | Dular](https://talk.nervos.org/t/spark-program-dular/10212/13) | Milestone 2 Report: USSD Interface Milestone 2 focused on making Dular usable from feature phones through a USSD interface. This is important because the target users are mobile...
- 2026-06-12 03:37:42 CST | T_Silva | [Chiral - Symmetric isomorphic binding: a committee-free, anchor-agnostic protocol where each chain verifies the other with a succinct on-chain light client](https://talk.nervos.org/t/chiral-symmetric-isomorphic-binding-a-committee-free-anchor-agnostic-protocol-where-each-chain-verifies-the-other-with-a-succinct-on-chain-light-client/10360/4) | Thanks sharp catch, and you’re right that we’re overloading “leap” relative to RGB++. Let me answer your direct question first, then the terminology. Does ownership ever come to...
