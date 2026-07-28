# Nervos Talk 社区简报

- 统计窗口: 2026-07-28 02:12:36 CST 到 2026-07-29 02:12:36 CST
- 生成时间: 2026-07-29 02:12:47 CST
- 话题数: 10
- 帖子数: 12
- 作者数: 8
- 总结模式: ai:openrouter

## 社区总结

## 今日发生了什么

今天 Nervos Talk 社区活动较为活跃，多个核心话题并行推进：Spark 资助项目出现治理与执行层面的摩擦，包括 Nervos Brain 项目尾款因多签问题改由个人钱包支付、Cell Sandbox 交付质量遭委员会成员公开批评，以及 Mini-Grant 发现冒名申请而收紧身份审核；同时，Poolin 矿池破产消息在社区引发对矿工迁移的关注。[S01, S03, S04, S06, S08]

## 重点话题

- **Spark 项目资金支付遇阻**：Nervos Brain 项目尾款因委员会多签钱包故障，临时决定改用个人钱包先行支付，开发者 IrisNeko 随后提供了 ERC20 收款地址，引发对资金管理流程稳健性的关注。[S06, S07]

- **Cell Sandbox 交付遭委员会质疑**：Spark 委员会成员 Yixiu 公开指出 Cell Sandbox 最新版本的 UI/UX 未见实质改善，认为 Learn 页面仍将概念卡片与原始字段表单混杂，未回应委员会两次（6/3、6/17）提出的整改要求，项目验收或面临僵局。[S03]

- **Mini-Grant 收紧身份审核**：Spark 委员会发现近期出现少数冒名 GitHub 开发者身份的申请现象，即日起要求申请人必须在自身 GitHub 账号下建立对应 Spark 项目仓库作为身份证明，以最小化流程摩擦。[S08]

- **Poolin 矿池破产，矿工需紧急迁移**：社区成员通报 Poolin 矿池破产，算力规模达 1.40 PH/s 的 Poolin 矿工须迁移至替代矿池，并提供了 2miners、Antpool、DxPool、Binance Pool 等可选名单。[S04]

- **密码学与状态转换话题延续**：knmo 在 fiber-payjoin-kit 讨论中提及后量子实现与 SPHINCS+ 交易的基准测试需求；xiaomao 则新发帖子探讨"证明有效但状态转换未必有效"的基础设施议题，延续了此前关于 ABI 与 Cell 生命周期的讨论。[S02, S05, S09]

## 值得继续跟进

- Spark 委员会的多签钱包问题是否属于偶发故障，以及改用个人钱包支付是否会成为临时惯例或引发审计层面的争议，需要观察委员会后续的正式说明。[S06]

- Cell Sandbox 项目是否会因委员会成员的公开批评而进入整改期或触发终止条件，Yixiu 提出的验收标准与项目方回应之间的张力值得持续关注。[S03]

- CKBBull 团队宣布从 CKB 钱包全面转向 BTC Lite 钱包，并已在 Reddit 开展 AMA，这一战略转向对 Nervos 生态用户留存的影响尚待评估。[S10]

## 来源索引

- `S01` [[DIS] fiber-payjoin-kit: Collaborative Privacy for the Nervos Fiber Network](https://talk.nervos.org/t/dis-fiber-payjoin-kit-collaborative-privacy-for-the-nervos-fiber-network/10296/16) | zz_tovarishch | 2026-07-28 09:21:59 CST | 目前DAO规则对修订后的再次提交没有明确规定 另外，虽然我作为协调员，对于修订提交的提案会在同步信息时对比原始提案和新提案，但我建议提案人可以主动在新提案中包含对比的部分，方便社区更好的进行审议
- `S02` [[DIS] fiber-payjoin-kit: Collaborative Privacy for the Nervos Fiber Network](https://talk.nervos.org/t/dis-fiber-payjoin-kit-collaborative-privacy-for-the-nervos-fiber-network/10296/17) | knmo | 2026-07-29 01:21:34 CST | Personally, I think we’re navigating some rough waters right now. Do you want to run some benchmarks on the post-quantum implementation? Are SPHINCS+ transactions that are not covered by this privacy-enhancing solution also processed in a block at the same time? So that there...
- `S03` [Spark Program | Cell Sandbox — A Visual Playground for the CKB Cell Model](https://talk.nervos.org/t/spark-program-cell-sandbox-a-visual-playground-for-the-ckb-cell-model/10326/20) | yixiu.ckbfans.bit | 2026-07-28 23:12:58 CST | Hi @zynor， 我是 Spark Program 委员会成员 Yixiu。我最近体验了 Cell Sandbox 的最新版本，发现以下几个问题，先同步给你和委员会同事参考： 1. UI/UX 未见实质改善 立项时委员会两次（6/3、6/17）指出界面混乱、新手难以上手，要求重新规划并打磨。但目前 Learn 页面依然是"概念说明卡片"和"完整可编辑表单"（Capacity/Lock Script/Type Script/Output Data 等原始字段）堆在同一屏，Learn / Design Cells / Build Tx 三个 tab...
- `S04` [Poolin.com | Mining Pool - Bankruptcy](https://talk.nervos.org/t/poolin-com-mining-pool-bankruptcy/10551/1) | knmo | 2026-07-28 20:52:36 CST | poolin.com | Mining Pool - Bankruptcy 1.40 PH/s Poolin miners must migrate to alternative pools. It’s best to choose a provider from this list: https://ckb.2miners.com/ https://antpool.com/ https://www.dxpool.com/ https://pool.binance.com/ Edit: “That happened in September...
- `S05` [Where Is the ABI? Also, Why Is My Cell Dead?](https://talk.nervos.org/t/where-is-the-abi-also-why-is-my-cell-dead/10423/7) | Jnr6 | 2026-07-28 19:07:13 CST | xiaomao: Can a CKB Type Script enforce a valid state transition where the public Cell data is only a commitment to private state? I don’t understand this question can you illustrate with an example?
- `S06` [Spark Program | Nervos Brain - A Global Developer Onboarding Engine and Cross-Language Hub Powered by Agentic RAG](https://talk.nervos.org/t/spark-program-nervos-brain-a-global-developer-onboarding-engine-and-cross-language-hub-powered-by-agentic-rag/9995/48) | zz_tovarishch | 2026-07-28 15:12:51 CST | Hi Iris请提供一个ERC20地址 因为多签钱包有点问题，委员会决定临时用个人钱包先支付该项目的尾款
- `S07` [Spark Program | Nervos Brain - A Global Developer Onboarding Engine and Cross-Language Hub Powered by Agentic RAG](https://talk.nervos.org/t/spark-program-nervos-brain-a-global-developer-onboarding-engine-and-cross-language-hub-powered-by-agentic-rag/9995/49) | IrisNeko | 2026-07-28 17:36:31 CST | 0xabc5400ace1d70d63c05feec6f731e50b97fa719 ETH ERC20
- `S08` [Spark Program: Mini-Grant Initiative](https://talk.nervos.org/t/spark-program-mini-grant-initiative/8752/10) | zz_tovarishch | 2026-07-28 17:00:09 CST | [2026.07.28 更新] 我们很遗憾的发现，近期似乎出现了少数冒名Github开发者身份的申请现象。 Spark作为开源资助项目，申请人会通过Github进行阶段性成果提交，同时在项目结项后委员会将把项目Fork到Spark专属仓库。 因此，出于最小化流程摩擦考虑，后续项目申请人请在递交申请时，同步在作为身份证明的Github账号下建立对应的Spark项目仓库，以便委员会进行核实。如果项目有多位申请人，请主申请人建立仓库，其他申请人进行Fork。
- `S09` [The Proof Is Valid. The Transition Might Not Be](https://talk.nervos.org/t/the-proof-is-valid-the-transition-might-not-be/10550/1) | xiaomao | 2026-07-28 15:02:45 CST | Gm, A few weeks ago, I published: Where Is the ABI? Also, Why Is My Cell Dead? Infrastructure Where Is the ABI? Also, Why Is My Cell Dead? A notes app should not send you into an identity crisis. You type something. You click save. Somewhere, some database politely updates...
- `S10` [Reddit AMA Bitcoin/CKB Lite wallet](https://talk.nervos.org/t/reddit-ama-bitcoin-ckb-lite-wallet/10549/1) | zz_tovarishch | 2026-07-28 09:36:41 CST | Bitcoin Light AMA 20261920×2213 707 KB Hello CKB community, To highlight the new CKBBull project, the team educate the community about their new venture BTC Lite wallet. They have deprecated the CKB Bull wallet and have pivoted towards a BTC compatible wallet. Description “The...
- `S11` [Ckb-viz: read any CKB transaction as a flow of cells](https://talk.nervos.org/t/ckb-viz-read-any-ckb-transaction-as-a-flow-of-cells/10482/10) | truthixify | 2026-07-28 05:12:21 CST | knmo: 0x1166ca65353a5cdd3379229280e2805d9065c9b39f3e11d4cf3352542aeef996 Thank you, this is a huge transaction, 5000+ inputs and 263 outputs, looking for a way to display this(for now, I implemented it in a way that only the first few are shown).
- `S12` [[DIS] CKB Anywhere Card — Tap to Pay via Apple & Google Wallet, Self-Custodial](https://talk.nervos.org/t/dis-ckb-anywhere-card-tap-to-pay-via-apple-google-wallet-self-custodial/10522/24) | BuildUnion | 2026-07-28 03:50:21 CST | Thanks for the questions. This means BTC, USDT, and other UTXO-enabled blockchains that link to Nervos, those assets can be spent crosschain? Potentially, yes, but with an important distinction. The authorization framework isn’t limited to CKB specifically—it’s designed to...

## 活跃话题

1. [[DIS] fiber-payjoin-kit: Collaborative Privacy for the Nervos Fiber Network](https://talk.nervos.org/t/dis-fiber-payjoin-kit-collaborative-privacy-for-the-nervos-fiber-network/10296) | 2 条近窗帖子 | 最新活动 2026-07-29 01:21:34 CST
2. [Spark Program | Cell Sandbox — A Visual Playground for the CKB Cell Model](https://talk.nervos.org/t/spark-program-cell-sandbox-a-visual-playground-for-the-ckb-cell-model/10326) | 1 条近窗帖子 | 最新活动 2026-07-28 23:12:58 CST | tags: In-Progress, Spark-Program, lang-en
3. [Poolin.com | Mining Pool - Bankruptcy](https://talk.nervos.org/t/poolin-com-mining-pool-bankruptcy/10551) | 1 条近窗帖子 | 最新活动 2026-07-28 20:52:36 CST
4. [Where Is the ABI? Also, Why Is My Cell Dead?](https://talk.nervos.org/t/where-is-the-abi-also-why-is-my-cell-dead/10423) | 1 条近窗帖子 | 最新活动 2026-07-28 19:07:13 CST | tags: CKB, cell-model, lang-en, zero-knowledge
5. [Spark Program | Nervos Brain - A Global Developer Onboarding Engine and Cross-Language Hub Powered by Agentic RAG](https://talk.nervos.org/t/spark-program-nervos-brain-a-global-developer-onboarding-engine-and-cross-language-hub-powered-by-agentic-rag/9995) | 2 条近窗帖子 | 最新活动 2026-07-28 17:36:31 CST | tags: In-Progress, Spark-Program, lang-en
6. [Spark Program: Mini-Grant Initiative](https://talk.nervos.org/t/spark-program-mini-grant-initiative/8752) | 1 条近窗帖子 | 最新活动 2026-07-28 17:00:09 CST | tags: Spark-Program, lang-en
7. [The Proof Is Valid. The Transition Might Not Be](https://talk.nervos.org/t/the-proof-is-valid-the-transition-might-not-be/10550) | 1 条近窗帖子 | 最新活动 2026-07-28 15:02:45 CST | tags: CKB, CKB-VM, zero-knowledge, zkp
8. [Reddit AMA Bitcoin/CKB Lite wallet](https://talk.nervos.org/t/reddit-ama-bitcoin-ckb-lite-wallet/10549) | 1 条近窗帖子 | 最新活动 2026-07-28 09:36:41 CST | tags: AMA
9. [Ckb-viz: read any CKB transaction as a flow of cells](https://talk.nervos.org/t/ckb-viz-read-any-ckb-transaction-as-a-flow-of-cells/10482) | 1 条近窗帖子 | 最新活动 2026-07-28 05:12:21 CST | tags: CKB, CKB-VM, dapp, lang-en
10. [[DIS] CKB Anywhere Card — Tap to Pay via Apple & Google Wallet, Self-Custodial](https://talk.nervos.org/t/dis-ckb-anywhere-card-tap-to-pay-via-apple-google-wallet-self-custodial/10522) | 1 条近窗帖子 | 最新活动 2026-07-28 03:50:21 CST

## 最近帖子摘录

- 2026-07-29 01:21:34 CST | knmo | [[DIS] fiber-payjoin-kit: Collaborative Privacy for the Nervos Fiber Network](https://talk.nervos.org/t/dis-fiber-payjoin-kit-collaborative-privacy-for-the-nervos-fiber-network/10296/17) | Personally, I think we’re navigating some rough waters right now. Do you want to run some benchmarks on the post-quantum implementation? Are SPHINCS+ transactions that are not...
- 2026-07-28 23:12:58 CST | yixiu.ckbfans.bit | [Spark Program | Cell Sandbox — A Visual Playground for the CKB Cell Model](https://talk.nervos.org/t/spark-program-cell-sandbox-a-visual-playground-for-the-ckb-cell-model/10326/20) | Hi @zynor， 我是 Spark Program 委员会成员 Yixiu。我最近体验了 Cell Sandbox 的最新版本，发现以下几个问题，先同步给你和委员会同事参考： 1. UI/UX 未见实质改善 立项时委员会两次（6/3、6/17）指出界面混乱、新手难以上手，要求重新规划并打磨。但目前 Learn...
- 2026-07-28 20:52:36 CST | knmo | [Poolin.com | Mining Pool - Bankruptcy](https://talk.nervos.org/t/poolin-com-mining-pool-bankruptcy/10551/1) | poolin.com | Mining Pool - Bankruptcy 1.40 PH/s Poolin miners must migrate to alternative pools. It’s best to choose a provider from this list: https://ckb.2miners.com/...
- 2026-07-28 19:07:13 CST | Jnr6 | [Where Is the ABI? Also, Why Is My Cell Dead?](https://talk.nervos.org/t/where-is-the-abi-also-why-is-my-cell-dead/10423/7) | xiaomao: Can a CKB Type Script enforce a valid state transition where the public Cell data is only a commitment to private state? I don’t understand this question can you...
- 2026-07-28 17:36:31 CST | IrisNeko | [Spark Program | Nervos Brain - A Global Developer Onboarding Engine and Cross-Language Hub Powered by Agentic RAG](https://talk.nervos.org/t/spark-program-nervos-brain-a-global-developer-onboarding-engine-and-cross-language-hub-powered-by-agentic-rag/9995/49) | 0xabc5400ace1d70d63c05feec6f731e50b97fa719 ETH ERC20
- 2026-07-28 17:00:09 CST | zz_tovarishch | [Spark Program: Mini-Grant Initiative](https://talk.nervos.org/t/spark-program-mini-grant-initiative/8752/10) | [2026.07.28 更新] 我们很遗憾的发现，近期似乎出现了少数冒名Github开发者身份的申请现象。 Spark作为开源资助项目，申请人会通过Github进行阶段性成果提交，同时在项目结项后委员会将把项目Fork到Spark专属仓库。...
- 2026-07-28 15:12:51 CST | zz_tovarishch | [Spark Program | Nervos Brain - A Global Developer Onboarding Engine and Cross-Language Hub Powered by Agentic RAG](https://talk.nervos.org/t/spark-program-nervos-brain-a-global-developer-onboarding-engine-and-cross-language-hub-powered-by-agentic-rag/9995/48) | Hi Iris请提供一个ERC20地址 因为多签钱包有点问题，委员会决定临时用个人钱包先支付该项目的尾款
- 2026-07-28 15:02:45 CST | xiaomao | [The Proof Is Valid. The Transition Might Not Be](https://talk.nervos.org/t/the-proof-is-valid-the-transition-might-not-be/10550/1) | Gm, A few weeks ago, I published: Where Is the ABI? Also, Why Is My Cell Dead? Infrastructure Where Is the ABI? Also, Why Is My Cell Dead? A notes app should not send you into...
- 2026-07-28 09:36:41 CST | zz_tovarishch | [Reddit AMA Bitcoin/CKB Lite wallet](https://talk.nervos.org/t/reddit-ama-bitcoin-ckb-lite-wallet/10549/1) | Bitcoin Light AMA 20261920×2213 707 KB Hello CKB community, To highlight the new CKBBull project, the team educate the community about their new venture BTC Lite wallet. They...
- 2026-07-28 09:21:59 CST | zz_tovarishch | [[DIS] fiber-payjoin-kit: Collaborative Privacy for the Nervos Fiber Network](https://talk.nervos.org/t/dis-fiber-payjoin-kit-collaborative-privacy-for-the-nervos-fiber-network/10296/16) | 目前DAO规则对修订后的再次提交没有明确规定 另外，虽然我作为协调员，对于修订提交的提案会在同步信息时对比原始提案和新提案，但我建议提案人可以主动在新提案中包含对比的部分，方便社区更好的进行审议
- 2026-07-28 05:12:21 CST | truthixify | [Ckb-viz: read any CKB transaction as a flow of cells](https://talk.nervos.org/t/ckb-viz-read-any-ckb-transaction-as-a-flow-of-cells/10482/10) | knmo: 0x1166ca65353a5cdd3379229280e2805d9065c9b39f3e11d4cf3352542aeef996 Thank you, this is a huge transaction, 5000+ inputs and 263 outputs, looking for a way to display...
- 2026-07-28 03:50:21 CST | BuildUnion | [[DIS] CKB Anywhere Card — Tap to Pay via Apple & Google Wallet, Self-Custodial](https://talk.nervos.org/t/dis-ckb-anywhere-card-tap-to-pay-via-apple-google-wallet-self-custodial/10522/24) | Thanks for the questions. This means BTC, USDT, and other UTXO-enabled blockchains that link to Nervos, those assets can be spent crosschain? Potentially, yes, but with an...
