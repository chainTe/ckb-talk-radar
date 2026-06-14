# Nervos Talk 社区简报

- 统计窗口: 2026-06-14 02:10:55 CST 到 2026-06-15 02:10:55 CST
- 生成时间: 2026-06-15 02:11:03 CST
- 话题数: 9
- 帖子数: 10
- 作者数: 8
- 总结模式: ai:openrouter

## 社区总结

## 今日发生了什么

今天 Nervos Talk 整体较平静，新帖数量不多。[S02, S03, S07, S08, S09, S06] 社区关注焦点分散在开发者工具、Layer 2 技术讨论和生态项目进展上，没有出现引发广泛讨论的重大事件。[S02, S03, S07, S08, S09, S06]

## 重点话题

- **开发者教育工具新提案**：团队 Zuhudev & Charles 提交了一份预算 1,950 美元、为期 8 周的提案，计划为 CKB 生态构建交互式开发者入门与模拟基础设施，属于开发者工具和教育方向。[S02]

- **CellScript 编译器升级**：ArthurZhang 发布 CellScript 0.16 版本，主要改进是编译器不再只输出产物和元数据，而是提供更清晰的合约预期视图，重点提升了保障性和工具链体验。[S07]

- **Morph Channel 技术讨论继续**：ArthurZhang 在 Morph Channel 议题下回应了社区成员 Jan 的评论，表示对方指出的正是后续细化需要关注的压力点，并提及与 CKB 上 Perun 及早期通用支付通道构造的比较。[S09]

- **隐私订单簿项目 Invisibook 推进**：Lawliet_Chan 报告本周开发进展，包括完成 "proof of buying" 模块的 PR 定义，并继续讨论和撰写 Invisibook 论文。[S03]

- **Fiber 流动性方案讨论**：Crybaby 详细解释 Amboss 并非简单的 Splicing 或 Loop，而是通过经济学手段实现流动性杠杆，强调其在闪电网络生态中的独特价值。[S08]

## 值得继续跟进

- **CellScript 后续版本**：0.16 是"较大升级"，开发者对新编译器输出格式的实际体验反馈值得观察，这将影响 CKB 合约开发的易用性。[S07]

- **Morph Channel 与现有通道方案的比较**：ArthurZhang 已承认需要进一步细化，其与 Perun 及早期通用支付通道构造的技术差异和优劣可能成为后续讨论焦点。[S09]

- **论坛分类优化实验**：knmo 继续推进论坛分类精简工作，涉及多语言 FAQ 和开发者/用户分区的角色定位调整，长期影响社区信息获取效率。[S06]

## 来源索引

- `S01` [[DIS] Rypto — CKB Content & Advocacy Campaign](https://talk.nervos.org/t/dis-rypto-ckb-content-advocacy-campaign/10364/4) | Lawliet_Chan | 2026-06-14 22:44:54 CST | 时间会证明CKB是L1目前的最优解， 从最早声称L2是扩容到 指出POS的问题。 CKB一直在做正确的事情， 做正确的事情很重要。 我们需要有更多的人了解CKB， 投了赞成票！ 会持续关注您的后续~
- `S02` [Interactive Developer Onboarding & Simulation Infrastructure for the CKB Ecosystem](https://talk.nervos.org/t/interactive-developer-onboarding-simulation-infrastructure-for-the-ckb-ecosystem/10385/1) | devnash | 2026-06-14 22:01:40 CST | Project Category Developer Tooling · Ecosystem Infrastructure · Interactive Education Funding Requested $1,950 Estimated Completion Time 8 Weeks Team Members Zuhudev & Charles We are full-stack blockchain developers focused on building developer tooling, decentralized...
- `S03` [[DIS] Decentralized privacy order-book appchain based on CKB L1 - 2026.phase-1](https://talk.nervos.org/t/dis-decentralized-privacy-order-book-appchain-based-on-ckb-l1-2026-phase-1/10015/31) | Lawliet_Chan | 2026-06-14 21:31:36 CST | 周报 2026.6.14 开发 proof of buying 模块： define proof of buy by Lawliet-Chan · Pull Request #8 · invisibook-lab/invisibook · GitHub 继续讨论和撰写invisibook论文
- `S04` [Local-first sovereign somatic lattice on CKB that gives users personalized Z-zero alignment steps for less stress while building consented data for health research and AI training](https://talk.nervos.org/t/local-first-sovereign-somatic-lattice-on-ckb-that-gives-users-personalized-z-zero-alignment-steps-for-less-stress-while-building-consented-data-for-health-research-and-ai-training/10379/2) | discourse_ai_spam | 2026-06-14 17:02:19 CST | 
- `S05` [Local-first sovereign somatic lattice on CKB that gives users personalized Z-zero alignment steps for less stress while building consented data for health research and AI training](https://talk.nervos.org/t/local-first-sovereign-somatic-lattice-on-ckb-that-gives-users-personalized-z-zero-alignment-steps-for-less-stress-while-building-consented-data-for-health-research-and-ai-training/10379/3) | system | 2026-06-14 19:57:45 CST | 
- `S06` [Streamlining the forum categories needs your testing and feedback](https://talk.nervos.org/t/streamlining-the-forum-categories-needs-your-testing-and-feedback/10216/15) | knmo | 2026-06-14 18:22:06 CST | Answers about development Answers about usage Respuestas sobre el desarrollo Respuestas sobre el uso 關於開發的常見問題 關於使用的常見問題 terrytai: Perhaps it just needs better category descriptions and guidance. Developers and users with a touch of role-playing. 開發者聚落 Barrio de los...
- `S07` [CellScript - A DSL for Cell-Based Contracts](https://talk.nervos.org/t/cellscript-a-dsl-for-cell-based-contracts/10193/25) | ArthurZhang | 2026-06-14 15:33:48 CST | CellScript 0.16 Release Notes CellScript 0.16 is a rather large upgrade focused on assurance and tooling. For users, the main change is that the compiler is no longer just producing an artefact and a metadata sidecar. It now gives you a clearer view of what a contract expects...
- `S08` [[Fiber] CKB 能让 Fiber 拥有更好的 Amboss](https://talk.nervos.org/t/fiber-ckb-fiber-amboss/10353/4) | Crybaby | 2026-06-14 13:22:59 CST | Amboss 其实是个流动性杠杆平台，并不是简单的 Splicing，不管是 Splicing 还是 Loop，你想要有 1000 CKB 的流动性就必须在链上有等额的 CKB 代币转移到 Fiber 网络中，但 Amboss 通过经济学手段，让你只需要提供 10 CKB 就能撬动 1000 CKB 的流动性，区别在于你只能用 30 天而已。 所以 Amboss 给闪电网络生态带来的意义肯定是 Splicing 和 Loop 给不了的，它有它的独特性和存在价值。
- `S09` [Morph Channel Explained: Separating Value, State Evidence, and Fee Responsibility on CKB](https://talk.nervos.org/t/morph-channel-explained-separating-value-state-evidence-and-fee-responsibility-on-ckb/10378/3) | ArthurZhang | 2026-06-14 11:36:39 CST | Hi Jan, Thanks for the thoughtful comment. I think you pointed at exactly the right pressure points, and this is very close to what any further refinement of Morph now needs. The comparison with Perun on CKB and the earlier Generic Payment Channel Construction is especially...
- `S10` [Vellum: a reference dashboard and SDK for did:ckb](https://talk.nervos.org/t/vellum-a-reference-dashboard-and-sdk-for-did-ckb/10274/7) | truthixify | 2026-06-14 07:39:55 CST | @Hanssen I’ve made a PR, please check it out here: feat(did-ckb): identifier helpers, resolver, history walk, did:plc migration by truthixify · Pull Request #376 · ckb-devrel/ccc · GitHub

## 活跃话题

1. [[DIS] Rypto — CKB Content & Advocacy Campaign](https://talk.nervos.org/t/dis-rypto-ckb-content-advocacy-campaign/10364) | 1 条近窗帖子 | 最新活动 2026-06-14 22:44:54 CST
2. [Interactive Developer Onboarding & Simulation Infrastructure for the CKB Ecosystem](https://talk.nervos.org/t/interactive-developer-onboarding-simulation-infrastructure-for-the-ckb-ecosystem/10385) | 1 条近窗帖子 | 最新活动 2026-06-14 22:01:40 CST | tags: Spark-Program
3. [[DIS] Decentralized privacy order-book appchain based on CKB L1 - 2026.phase-1](https://talk.nervos.org/t/dis-decentralized-privacy-order-book-appchain-based-on-ckb-l1-2026-phase-1/10015) | 1 条近窗帖子 | 最新活动 2026-06-14 21:31:36 CST | tags: appchain
4. [Local-first sovereign somatic lattice on CKB that gives users personalized Z-zero alignment steps for less stress while building consented data for health research and AI training](https://talk.nervos.org/t/local-first-sovereign-somatic-lattice-on-ckb-that-gives-users-personalized-z-zero-alignment-steps-for-less-stress-while-building-consented-data-for-health-research-and-ai-training/10379) | 2 条近窗帖子 | 最新活动 2026-06-14 19:57:45 CST | tags: CKB, Spark-Program, appchain, dapp
5. [Streamlining the forum categories needs your testing and feedback](https://talk.nervos.org/t/streamlining-the-forum-categories-needs-your-testing-and-feedback/10216) | 1 条近窗帖子 | 最新活动 2026-06-14 18:22:06 CST
6. [CellScript - A DSL for Cell-Based Contracts](https://talk.nervos.org/t/cellscript-a-dsl-for-cell-based-contracts/10193) | 1 条近窗帖子 | 最新活动 2026-06-14 15:33:48 CST | tags: CKB-VM, CellScript, DSL
7. [[Fiber] CKB 能让 Fiber 拥有更好的 Amboss](https://talk.nervos.org/t/fiber-ckb-fiber-amboss/10353) | 1 条近窗帖子 | 最新活动 2026-06-14 13:22:59 CST
8. [Morph Channel Explained: Separating Value, State Evidence, and Fee Responsibility on CKB](https://talk.nervos.org/t/morph-channel-explained-separating-value-state-evidence-and-fee-responsibility-on-ckb/10378) | 1 条近窗帖子 | 最新活动 2026-06-14 11:36:39 CST
9. [Vellum: a reference dashboard and SDK for did:ckb](https://talk.nervos.org/t/vellum-a-reference-dashboard-and-sdk-for-did-ckb/10274) | 1 条近窗帖子 | 最新活动 2026-06-14 07:39:55 CST | tags: CKB, NFT, QA, dapp, testnet

## 最近帖子摘录

- 2026-06-14 22:44:54 CST | Lawliet_Chan | [[DIS] Rypto — CKB Content & Advocacy Campaign](https://talk.nervos.org/t/dis-rypto-ckb-content-advocacy-campaign/10364/4) | 时间会证明CKB是L1目前的最优解， 从最早声称L2是扩容到 指出POS的问题。 CKB一直在做正确的事情， 做正确的事情很重要。 我们需要有更多的人了解CKB， 投了赞成票！ 会持续关注您的后续~
- 2026-06-14 22:01:40 CST | devnash | [Interactive Developer Onboarding & Simulation Infrastructure for the CKB Ecosystem](https://talk.nervos.org/t/interactive-developer-onboarding-simulation-infrastructure-for-the-ckb-ecosystem/10385/1) | Project Category Developer Tooling · Ecosystem Infrastructure · Interactive Education Funding Requested $1,950 Estimated Completion Time 8 Weeks Team Members Zuhudev & Charles...
- 2026-06-14 21:31:36 CST | Lawliet_Chan | [[DIS] Decentralized privacy order-book appchain based on CKB L1 - 2026.phase-1](https://talk.nervos.org/t/dis-decentralized-privacy-order-book-appchain-based-on-ckb-l1-2026-phase-1/10015/31) | 周报 2026.6.14 开发 proof of buying 模块： define proof of buy by Lawliet-Chan · Pull Request #8 · invisibook-lab/invisibook · GitHub 继续讨论和撰写invisibook论文
- 2026-06-14 19:57:45 CST | system | [Local-first sovereign somatic lattice on CKB that gives users personalized Z-zero alignment steps for less stress while building consented data for health research and AI training](https://talk.nervos.org/t/local-first-sovereign-somatic-lattice-on-ckb-that-gives-users-personalized-z-zero-alignment-steps-for-less-stress-while-building-consented-data-for-health-research-and-ai-training/10379/3) | 
- 2026-06-14 18:22:06 CST | knmo | [Streamlining the forum categories needs your testing and feedback](https://talk.nervos.org/t/streamlining-the-forum-categories-needs-your-testing-and-feedback/10216/15) | Answers about development Answers about usage Respuestas sobre el desarrollo Respuestas sobre el uso 關於開發的常見問題 關於使用的常見問題 terrytai: Perhaps it just needs better category...
- 2026-06-14 17:02:19 CST | discourse_ai_spam | [Local-first sovereign somatic lattice on CKB that gives users personalized Z-zero alignment steps for less stress while building consented data for health research and AI training](https://talk.nervos.org/t/local-first-sovereign-somatic-lattice-on-ckb-that-gives-users-personalized-z-zero-alignment-steps-for-less-stress-while-building-consented-data-for-health-research-and-ai-training/10379/2) | 
- 2026-06-14 15:33:48 CST | ArthurZhang | [CellScript - A DSL for Cell-Based Contracts](https://talk.nervos.org/t/cellscript-a-dsl-for-cell-based-contracts/10193/25) | CellScript 0.16 Release Notes CellScript 0.16 is a rather large upgrade focused on assurance and tooling. For users, the main change is that the compiler is no longer just...
- 2026-06-14 13:22:59 CST | Crybaby | [[Fiber] CKB 能让 Fiber 拥有更好的 Amboss](https://talk.nervos.org/t/fiber-ckb-fiber-amboss/10353/4) | Amboss 其实是个流动性杠杆平台，并不是简单的 Splicing，不管是 Splicing 还是 Loop，你想要有 1000 CKB 的流动性就必须在链上有等额的 CKB 代币转移到 Fiber 网络中，但 Amboss 通过经济学手段，让你只需要提供 10 CKB 就能撬动 1000 CKB 的流动性，区别在于你只能用 30 天而已。 所以...
- 2026-06-14 11:36:39 CST | ArthurZhang | [Morph Channel Explained: Separating Value, State Evidence, and Fee Responsibility on CKB](https://talk.nervos.org/t/morph-channel-explained-separating-value-state-evidence-and-fee-responsibility-on-ckb/10378/3) | Hi Jan, Thanks for the thoughtful comment. I think you pointed at exactly the right pressure points, and this is very close to what any further refinement of Morph now needs....
- 2026-06-14 07:39:55 CST | truthixify | [Vellum: a reference dashboard and SDK for did:ckb](https://talk.nervos.org/t/vellum-a-reference-dashboard-and-sdk-for-did-ckb/10274/7) | @Hanssen I’ve made a PR, please check it out here: feat(did-ckb): identifier helpers, resolver, history walk, did:plc migration by truthixify · Pull Request #376 · ckb-...
