# Nervos Talk 社区简报

- 统计窗口: 2026-10-25 03:26:18 CST 到 2026-10-26 03:26:18 CST
- 生成时间: 2026-10-26 03:26:26 CST
- 话题数: 7
- 帖子数: 12
- 作者数: 8
- 总结模式: ai:openai-compatible

## 社区总结

## 今日发生了什么

从这批帖子看，过去一天论坛有多条测试网产品和基础设施提案更新，整体不算完全安静[S01,S03,S05,S09,S10]。讨论主线之一是 Kirea Finance 的 RWA 借贷争议：有人质疑链上无法强制执行现实世界义务，项目方随后连续回应并补充链下与链上两层思路[S05,S06,S07]。另一条主线是开发者工具和测试网应用：CKB IDL 作者回应反馈，Nine Cells、Cellula Wallet、FiberNuts 等都在征集测试或迭代[S03,S04,S01,S09,S10]。此外，Twine 帖子有简短正面反馈，Nervlith 发布了品牌更名与平台介绍[S11,S12]。

## 重点话题

- Kirea Finance 继续围绕 RWA 强制执行展开讨论：社区成员指出 CKB 能约束链上合约，但不能直接约束现实世界义务[S05]；项目方回应称 RWA 需要链下与链上两层配合，并提到 Centrifuge、Goldfinch、Maple 等协议也不是仅靠智能合约执行现实义务[S06,S07]。项目方还把部分回答放到 metaforo 链接中，邀请继续提问[S08]。

- CKB IDL 提案作者回应开发者体验关切：作者表示目标是让 IDL 生成和消费自然融入现有开发流程，而不是增加另一套复杂流程[S03]；同时认同应补充现有工具而非重复造轮子，并感谢此前对 CellScript registry 集成探索的帮助[S04]。

- Nine Cells 测试网游戏分享后引发实现讨论：作者介绍这是一款浏览器塔防游戏，玩家在车道放置猫并合并同级猫来防守墙体[S01]；评论者表示玩得有趣，并讨论 Spore DOB 因内容不可变不适合“合并重写猫数据”，但可能通过熔毁两个 Spore 并在同一交易中铸造新 Spore 来实现[S02]。

- Cellula Wallet 开启测试招募，FiberNuts 同步修复和增强：Cellula 正在测试一款住在 passkey 里的钱包，并提供 `yourname.cell` 命名支付体验，测试招募截至 10 月 26 日周一[S09]；FiberNuts 表示已加入严格 CSP、修复“1 claim”措辞、改进安全报告，并为 cash-out 增加精确网络/RUSD 资产校验[S10]。

- Nervlith 由 Mint Gate 更名发布：Nervlith 被介绍为 CKB 原生的 DAO 启动器、token gating 和会员平台[S12]；帖子还提到该产品已提供中文翻译以覆盖更广社区[S12]。

## 值得继续跟进

- Kirea Finance 的现实世界资产执行与验证仍是核心风险，项目方主张依赖链下与链上两层配合，后续要看具体风控和验证安排如何落地[S05,S07]。

- Cellula Wallet 测试招募截止到 10 月 26 日周一，后续可关注测试反馈以及 passkey 钱包和命名支付的实际体验[S09]。

- FiberNuts 已修复若干问题，但事件友好 faucet、基于 LSP 的充值、NUT-13 recovery 和 NUT-11 等仍在更新清单中，值得观察后续落地情况[S10]。

## 来源索引

- `S01` [Nine Cells: a merge tower defense game (testnet)](https://talk.nervos.org/t/nine-cells-a-merge-tower-defense-game-testnet/11046/1) | karasbuilder | 2026-10-25 07:26:53 CST | Hi everyone, I’m Karas, a CKBuilder in the current cohort. I’ve been building Nine Cells, a browser tower defense game where you defend a wall by placing cats in lanes and merging two same-level cats into a stronger one. I’d like to share how it uses cells and get feedback,...
- `S02` [Nine Cells: a merge tower defense game (testnet)](https://talk.nervos.org/t/nine-cells-a-merge-tower-defense-game-testnet/11046/2) | janx | 2026-10-25 15:26:40 CST | Had a lot of fun with it karasbuilder: I also looked at Spore DOBs and decided against them, because Spore content is immutable and a merge needs to rewrite the cat’s data. Might still be possible with Spore DOBs by melting two Spores and mint a new one in the same txn.
- `S03` [[DIS] CKB IDL: Interface Description Language and Discoverability for CKB Scripts](https://talk.nervos.org/t/dis-ckb-idl-interface-description-language-and-discoverability-for-ckb-scripts/11031/7) | OWK50GA | 2026-10-25 14:30:36 CST | Thanks for the thoughtful feedback, @3m1n3nc3 Developer experience is one of my biggest priorities here. The goal is to make IDL generation and consumption fit naturally into existing development workflows, rather than introduce another complicated process. That’s partly why...
- `S04` [[DIS] CKB IDL: Interface Description Language and Discoverability for CKB Scripts](https://talk.nervos.org/t/dis-ckb-idl-interface-description-language-and-discoverability-for-ckb-scripts/11031/8) | OWK50GA | 2026-10-25 14:36:17 CST | Thank you, Arthur. I really appreciate the support, and especially your help exploring IDL integration with the CellScript registry earlier. I agree that the strongest approach is to complement existing tooling rather than duplicate it. CellScript’s existing type information...
- `S05` [[DIS] Kirea Finance: Native RWA Lending Infrastructure for CKB |【DIS】Kirea Finance：面向 CKB 的原生 RWA 借贷基础设施](https://talk.nervos.org/t/dis-kirea-finance-native-rwa-lending-infrastructure-for-ckb-dis-kirea-finance-ckb-rwa/10809/27) | psawyerberlin | 2026-10-25 05:02:47 CST | Interesting concept, and I appreciate the considerable development effort already invested in Kirea Finance. However, I still see a fundamental challenge with real-world asset (RWA) enforcement. CKB can enforce on-chain contracts, but it cannot enforce real-world obligations....
- `S06` [[DIS] Kirea Finance: Native RWA Lending Infrastructure for CKB |【DIS】Kirea Finance：面向 CKB 的原生 RWA 借贷基础设施](https://talk.nervos.org/t/dis-kirea-finance-native-rwa-lending-infrastructure-for-ckb-dis-kirea-finance-ckb-rwa/10809/28) | SalmanDev | 2026-10-25 09:01:06 CST | Thanks @psawyerberlin for the thoughtful, detailed feedback and for recognizing the work already invested in Kirea Finance. You’ve raised two important points, and I appreciate both the critical questions about RWA enforcement and the constructive comment. 1. On RWA...
- `S07` [[DIS] Kirea Finance: Native RWA Lending Infrastructure for CKB |【DIS】Kirea Finance：面向 CKB 的原生 RWA 借贷基础设施](https://talk.nervos.org/t/dis-kirea-finance-native-rwa-lending-infrastructure-for-ckb-dis-kirea-finance-ckb-rwa/10809/29) | SalmanDev | 2026-10-25 09:25:06 CST | To address your point on risk and verification: Across the broader Web3 ecosystem (such as Centrifuge, Goldfinch, and Maple), no RWA protocol enforces real-world obligations through smart contracts alone. They rely on the two complementary layers working together: off-chain...
- `S08` [[DIS] Kirea Finance: Native RWA Lending Infrastructure for CKB |【DIS】Kirea Finance：面向 CKB 的原生 RWA 借贷基础设施](https://talk.nervos.org/t/dis-kirea-finance-native-rwa-lending-infrastructure-for-ckb-dis-kirea-finance-ckb-rwa/10809/30) | SalmanDev | 2026-10-25 09:54:34 CST | Hey everyone! Some important questions came up that others might have too, so I’m sharing a link to my responses on metaforo: https://dao.ckb.community/landing?method=share&thread=80639&refer_id=55318&post=2022504 Feel free to ask me any questions. Happy to answer them.
- `S09` [Cellula Wallet beta on testnet: testers wanted until Monday 26 October](https://talk.nervos.org/t/cellula-wallet-beta-on-testnet-testers-wanted-until-monday-26-october/11048/1) | LusoCryptoLabs | 2026-10-25 09:09:05 CST | image1920×1008 241 KB Hi everyone, Cellula is the name you can pay: cellula.id gives you one name, yourname.cell, that people can pay instead of a blockchain address. Now we are testing the Cellula Wallet, a wallet that lives in your passkey, and we are looking for more...
- `S10` [FiberNuts Community Market: A Testnet App for Cashu + Fiber](https://talk.nervos.org/t/fibernuts-community-market-a-testnet-app-for-cashu-fiber/10792/10) | Code3ks | 2026-10-25 06:16:00 CST | Thanks for the detailed testing and feedback. I’ve now added a strict CSP, fixed the “1 claim” wording, improved security reporting, and added exact network/RUSD asset validation for cash-outs. Event-friendly faucet access, easier LSP-based funding, NUT-13 recovery, and NUT-11...
- `S11` [Twine is up. Try buying and selling CKB without an exchange using Fiber and Nostr](https://talk.nervos.org/t/twine-is-up-try-buying-and-selling-ckb-without-an-exchange-using-fiber-and-nostr/11043/3) | Victor_Okenwa | 2026-10-25 04:47:07 CST | Love the Idea.
- `S12` [Introducing Nervlith (formally Mint Gate): a CKB-native token gating and membership platform](https://talk.nervos.org/t/introducing-nervlith-formally-mint-gate-a-ckb-native-token-gating-and-membership-platform/11045/1) | Victor_Okenwa | 2026-10-25 03:56:04 CST | GM NERVOS BUILDERS!!!, The product previously called Mint Gate is now Nervlith (formally Mint Gate). Nervlith is a CKB-native DAO launcher, token gating and membership platform. image1775×748 141 KB It is also translated to Mandarin for wider community scope image1375×677 103...

## 活跃话题

1. [Nine Cells: a merge tower defense game (testnet)](https://talk.nervos.org/t/nine-cells-a-merge-tower-defense-game-testnet/11046) | 2 条近窗帖子 | 最新活动 2026-10-25 15:26:40 CST | tags: game, testnet
2. [[DIS] CKB IDL: Interface Description Language and Discoverability for CKB Scripts](https://talk.nervos.org/t/dis-ckb-idl-interface-description-language-and-discoverability-for-ckb-scripts/11031) | 2 条近窗帖子 | 最新活动 2026-10-25 14:36:17 CST | tags: CKB-IDL
3. [[DIS] Kirea Finance: Native RWA Lending Infrastructure for CKB |【DIS】Kirea Finance：面向 CKB 的原生 RWA 借贷基础设施](https://talk.nervos.org/t/dis-kirea-finance-native-rwa-lending-infrastructure-for-ckb-dis-kirea-finance-ckb-rwa/10809) | 4 条近窗帖子 | 最新活动 2026-10-25 09:54:34 CST | tags: CKB, DeFi, defi挖矿, lang-es, lang-zh
4. [Cellula Wallet beta on testnet: testers wanted until Monday 26 October](https://talk.nervos.org/t/cellula-wallet-beta-on-testnet-testers-wanted-until-monday-26-october/11048) | 1 条近窗帖子 | 最新活动 2026-10-25 09:09:05 CST | tags: CKB, dapp, testnet
5. [FiberNuts Community Market: A Testnet App for Cashu + Fiber](https://talk.nervos.org/t/fibernuts-community-market-a-testnet-app-for-cashu-fiber/10792) | 1 条近窗帖子 | 最新活动 2026-10-25 06:16:00 CST | tags: CKB, dapp, testnet
6. [Twine is up. Try buying and selling CKB without an exchange using Fiber and Nostr](https://talk.nervos.org/t/twine-is-up-try-buying-and-selling-ckb-without-an-exchange-using-fiber-and-nostr/11043) | 1 条近窗帖子 | 最新活动 2026-10-25 04:47:07 CST | tags: fiber, testnet
7. [Introducing Nervlith (formally Mint Gate): a CKB-native token gating and membership platform](https://talk.nervos.org/t/introducing-nervlith-formally-mint-gate-a-ckb-native-token-gating-and-membership-platform/11045) | 1 条近窗帖子 | 最新活动 2026-10-25 03:56:04 CST | tags: CKB, dapp, lang-en

## 最近帖子摘录

- 2026-10-25 15:26:40 CST | janx | [Nine Cells: a merge tower defense game (testnet)](https://talk.nervos.org/t/nine-cells-a-merge-tower-defense-game-testnet/11046/2) | Had a lot of fun with it karasbuilder: I also looked at Spore DOBs and decided against them, because Spore content is immutable and a merge needs to rewrite the cat’s data....
- 2026-10-25 14:36:17 CST | OWK50GA | [[DIS] CKB IDL: Interface Description Language and Discoverability for CKB Scripts](https://talk.nervos.org/t/dis-ckb-idl-interface-description-language-and-discoverability-for-ckb-scripts/11031/8) | Thank you, Arthur. I really appreciate the support, and especially your help exploring IDL integration with the CellScript registry earlier. I agree that the strongest approach...
- 2026-10-25 14:30:36 CST | OWK50GA | [[DIS] CKB IDL: Interface Description Language and Discoverability for CKB Scripts](https://talk.nervos.org/t/dis-ckb-idl-interface-description-language-and-discoverability-for-ckb-scripts/11031/7) | Thanks for the thoughtful feedback, @3m1n3nc3 Developer experience is one of my biggest priorities here. The goal is to make IDL generation and consumption fit naturally into...
- 2026-10-25 09:54:34 CST | SalmanDev | [[DIS] Kirea Finance: Native RWA Lending Infrastructure for CKB |【DIS】Kirea Finance：面向 CKB 的原生 RWA 借贷基础设施](https://talk.nervos.org/t/dis-kirea-finance-native-rwa-lending-infrastructure-for-ckb-dis-kirea-finance-ckb-rwa/10809/30) | Hey everyone! Some important questions came up that others might have too, so I’m sharing a link to my responses on metaforo:...
- 2026-10-25 09:25:06 CST | SalmanDev | [[DIS] Kirea Finance: Native RWA Lending Infrastructure for CKB |【DIS】Kirea Finance：面向 CKB 的原生 RWA 借贷基础设施](https://talk.nervos.org/t/dis-kirea-finance-native-rwa-lending-infrastructure-for-ckb-dis-kirea-finance-ckb-rwa/10809/29) | To address your point on risk and verification: Across the broader Web3 ecosystem (such as Centrifuge, Goldfinch, and Maple), no RWA protocol enforces real-world obligations...
- 2026-10-25 09:09:05 CST | LusoCryptoLabs | [Cellula Wallet beta on testnet: testers wanted until Monday 26 October](https://talk.nervos.org/t/cellula-wallet-beta-on-testnet-testers-wanted-until-monday-26-october/11048/1) | image1920×1008 241 KB Hi everyone, Cellula is the name you can pay: cellula.id gives you one name, yourname.cell, that people can pay instead of a blockchain address. Now we are...
- 2026-10-25 09:01:06 CST | SalmanDev | [[DIS] Kirea Finance: Native RWA Lending Infrastructure for CKB |【DIS】Kirea Finance：面向 CKB 的原生 RWA 借贷基础设施](https://talk.nervos.org/t/dis-kirea-finance-native-rwa-lending-infrastructure-for-ckb-dis-kirea-finance-ckb-rwa/10809/28) | Thanks @psawyerberlin for the thoughtful, detailed feedback and for recognizing the work already invested in Kirea Finance. You’ve raised two important points, and I appreciate...
- 2026-10-25 07:26:53 CST | karasbuilder | [Nine Cells: a merge tower defense game (testnet)](https://talk.nervos.org/t/nine-cells-a-merge-tower-defense-game-testnet/11046/1) | Hi everyone, I’m Karas, a CKBuilder in the current cohort. I’ve been building Nine Cells, a browser tower defense game where you defend a wall by placing cats in lanes and...
- 2026-10-25 06:16:00 CST | Code3ks | [FiberNuts Community Market: A Testnet App for Cashu + Fiber](https://talk.nervos.org/t/fibernuts-community-market-a-testnet-app-for-cashu-fiber/10792/10) | Thanks for the detailed testing and feedback. I’ve now added a strict CSP, fixed the “1 claim” wording, improved security reporting, and added exact network/RUSD asset...
- 2026-10-25 05:02:47 CST | psawyerberlin | [[DIS] Kirea Finance: Native RWA Lending Infrastructure for CKB |【DIS】Kirea Finance：面向 CKB 的原生 RWA 借贷基础设施](https://talk.nervos.org/t/dis-kirea-finance-native-rwa-lending-infrastructure-for-ckb-dis-kirea-finance-ckb-rwa/10809/27) | Interesting concept, and I appreciate the considerable development effort already invested in Kirea Finance. However, I still see a fundamental challenge with real-world asset...
- 2026-10-25 04:47:07 CST | Victor_Okenwa | [Twine is up. Try buying and selling CKB without an exchange using Fiber and Nostr](https://talk.nervos.org/t/twine-is-up-try-buying-and-selling-ckb-without-an-exchange-using-fiber-and-nostr/11043/3) | Love the Idea.
- 2026-10-25 03:56:04 CST | Victor_Okenwa | [Introducing Nervlith (formally Mint Gate): a CKB-native token gating and membership platform](https://talk.nervos.org/t/introducing-nervlith-formally-mint-gate-a-ckb-native-token-gating-and-membership-platform/11045/1) | GM NERVOS BUILDERS!!!, The product previously called Mint Gate is now Nervlith (formally Mint Gate). Nervlith is a CKB-native DAO launcher, token gating and membership platform....
