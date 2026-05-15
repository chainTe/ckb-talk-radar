# Nervos Talk 社区简报

- 统计窗口: 2026-05-14 16:55:27 CST 到 2026-05-15 16:55:27 CST
- 生成时间: 2026-05-15 16:55:29 CST
- 话题数: 4
- 帖子数: 5
- 作者数: 4
- 总结模式: ai:openrouter

## 社区总结

## 今日发生了什么

今天 Nervos Talk 社区整体较平静，主要围绕几项长期在开发的建设者工具展开讨论。[S01, S02] janx 发布了沉淀数月的本地优先 CKB 浏览器 CKBadger，同时开发者 InkHaven 正式开源了一套解决低层开发痛点的工具集 Scryve Tools。 [S01, S02]

## 重点话题

- **CKBadger 本地浏览器问世**：janx 推出了一款"高度主观、并非面向所有人"的本地优先 CKB 原生浏览器，作为其 vibe-coding 实验的成果，目前已提供 GitHub、文档和在线演示。 [S01]

- **Scryve Tools 开源助力开发者**：InkHaven 团队将过去 6 个月内部打磨的 CKB 开发工具集正式开源，涵盖钱包授权、见证编码、xUDT 金额处理、Spore NFT DNA 及支付拆分等常见低层问题。 [S02]

- **Babel 翻译插件遇格式故障**：phroi 在 Babel Reunited 翻译插件的公测反馈中指出，某篇翻译从首版到当前版本存在持续性的格式损坏问题，自称已尝试多次修复未果。 [S03]

- **Vellum DID 凭证粘性获讨论**：truthixify 与 janx 就 did:ckb 的社会凭证框架展开讨论，认为 DID 积累徽章、认证或参与历史后，迁移成本将超过 cell-capacity 退款收益，从而形成用户粘性。[S04, S05]

## 来源索引

- `S01` [CKBadger: a local-first CKB-native explorer, and a vibe-coding experiment](https://talk.nervos.org/t/ckbadger-a-local-first-ckb-native-explorer-and-a-vibe-coding-experiment/10276/1) | janx | 2026-05-15 10:36:09 CST | I’d like to introduce CKBadger, a local-first CKB-native explorer. It’s a small homebrew project that I’ve been working on for months. Github and Docs | Demo CKBadger is highly opinionated and not meant to be for everyone. It’s built around a few questions that I wanted to...
- `S02` [[Open Source] @scryve-tools - CKB developer utilities](https://talk.nervos.org/t/open-source-scryve-tools-ckb-developer-utilities/10275/1) | InkHaven | 2026-05-15 05:14:15 CST | Hello everyone, its been a while, We’ve been busy building Scryve for the past 6 months and ran into the same low-level plumbing problems most CKB developers face, wallet auth flows, witness encoding, xUDT amounts, Spore NFT DNA, payment splitting. We solved them, tested them,...
- `S03` [[ANN]The Babel Reunited translation plugin has started public beta testing in the DAO category](https://talk.nervos.org/t/ann-the-babel-reunited-translation-plugin-has-started-public-beta-testing-in-the-dao-category/10172/8) | phroi | 2026-05-15 04:26:53 CST | Hey @terrytai, Ijust noticed something wrong with a translation formatting: I tried a couple times to work around the issue, but translation seems broken from the first revision until the current one iCKB Contracts Revisited: Old Code, New Audit CKB Development & Technical...
- `S04` [Vellum: a reference dashboard and SDK for did:ckb](https://talk.nervos.org/t/vellum-a-reference-dashboard-and-sdk-for-did-ckb/10274/3) | truthixify | 2026-05-14 18:41:58 CST | Thanks for trying it out. The social-credentials framing is exactly the angle I’m most curious about too. Once a DID accumulates badges, attestations, or a participation history, churn starts working against the holder. Losing all of that costs more than the cell-capacity...
- `S05` [Vellum: a reference dashboard and SDK for did:ckb](https://talk.nervos.org/t/vellum-a-reference-dashboard-and-sdk-for-did-ckb/10274/4) | janx | 2026-05-14 19:23:46 CST | truthixify: The social-credentials framing is exactly the angle I’m most curious about too. Once a DID accumulates badges, attestations, or a participation history, churn starts working against the holder. Losing all of that costs more than the cell-capacity refund pays back....

## 活跃话题

1. [CKBadger: a local-first CKB-native explorer, and a vibe-coding experiment](https://talk.nervos.org/t/ckbadger-a-local-first-ckb-native-explorer-and-a-vibe-coding-experiment/10276) | 1 条近窗帖子 | 最新活动 2026-05-15 10:36:09 CST | tags: app
2. [[Open Source] @scryve-tools - CKB developer utilities](https://talk.nervos.org/t/open-source-scryve-tools-ckb-developer-utilities/10275) | 1 条近窗帖子 | 最新活动 2026-05-15 05:14:15 CST | tags: CKB, Spark-Program, dapp
3. [[ANN]The Babel Reunited translation plugin has started public beta testing in the DAO category](https://talk.nervos.org/t/ann-the-babel-reunited-translation-plugin-has-started-public-beta-testing-in-the-dao-category/10172) | 1 条近窗帖子 | 最新活动 2026-05-15 04:26:53 CST
4. [Vellum: a reference dashboard and SDK for did:ckb](https://talk.nervos.org/t/vellum-a-reference-dashboard-and-sdk-for-did-ckb/10274) | 2 条近窗帖子 | 最新活动 2026-05-14 19:23:46 CST | tags: CKB, NFT, QA, dapp, testnet

## 最近帖子摘录

- 2026-05-15 10:36:09 CST | janx | [CKBadger: a local-first CKB-native explorer, and a vibe-coding experiment](https://talk.nervos.org/t/ckbadger-a-local-first-ckb-native-explorer-and-a-vibe-coding-experiment/10276/1) | I’d like to introduce CKBadger, a local-first CKB-native explorer. It’s a small homebrew project that I’ve been working on for months. Github and Docs | Demo CKBadger is highly...
- 2026-05-15 05:14:15 CST | InkHaven | [[Open Source] @scryve-tools - CKB developer utilities](https://talk.nervos.org/t/open-source-scryve-tools-ckb-developer-utilities/10275/1) | Hello everyone, its been a while, We’ve been busy building Scryve for the past 6 months and ran into the same low-level plumbing problems most CKB developers face, wallet auth...
- 2026-05-15 04:26:53 CST | phroi | [[ANN]The Babel Reunited translation plugin has started public beta testing in the DAO category](https://talk.nervos.org/t/ann-the-babel-reunited-translation-plugin-has-started-public-beta-testing-in-the-dao-category/10172/8) | Hey @terrytai, Ijust noticed something wrong with a translation formatting: I tried a couple times to work around the issue, but translation seems broken from the first revision...
- 2026-05-14 19:23:46 CST | janx | [Vellum: a reference dashboard and SDK for did:ckb](https://talk.nervos.org/t/vellum-a-reference-dashboard-and-sdk-for-did-ckb/10274/4) | truthixify: The social-credentials framing is exactly the angle I’m most curious about too. Once a DID accumulates badges, attestations, or a participation history, churn starts...
- 2026-05-14 18:41:58 CST | truthixify | [Vellum: a reference dashboard and SDK for did:ckb](https://talk.nervos.org/t/vellum-a-reference-dashboard-and-sdk-for-did-ckb/10274/3) | Thanks for trying it out. The social-credentials framing is exactly the angle I’m most curious about too. Once a DID accumulates badges, attestations, or a participation...
