# Nervos Talk 社区简报

- 统计窗口: 2026-10-23 04:11:35 CST 到 2026-10-24 04:11:35 CST
- 生成时间: 2026-10-24 04:11:42 CST
- 话题数: 7
- 帖子数: 12
- 作者数: 9
- 总结模式: ai:openai-compatible

## 社区总结

## 今日发生了什么

从这批帖子看，过去一天论坛的主要焦点是 CKB IDL 提案，社区反馈整体正面[S01, S02, S04, S05]。治理方面，Kaze X CKB Unitour 延续提案公布了通过结果[S12]。项目侧还有 QuotaCell 测试更新、FiberNuts 测试反馈与作者回应，以及 Omiga 对地址跟踪问题的回应[S08, S09, S10, S11]。整体上论坛不算冷清，讨论集中在少数提案和项目进展上[S01, S12, S08, S09]。

## 重点话题

- OWK50GA 提出 CKB IDL 提案，请求 5,000 美元 grant，计划构建开源、testnet 优先的 Script Registry，用于发布、发现和独立验证 CKB 脚本接口，并推进 IDL 0.1.1[S01]。社区成员正面回应，认为可发现、可验证的脚本接口有助 CKB 可组合性和交易构建，并提到 TypeScript 支持与共享脚本注册表整合[S02, S04, S05]。
- Kaze X CKB Unitour 延续提案以 100% 赞成通过，总投票权重为 183,340,273 CKB、共 13 名投票者，满足通过门槛和最低参与要求，并于 2026 年 10 月 23 日完成投票后验证[S12]。
- QuotaCell 作者更新称，已用发送到隔离 CKB 节点的签名交易测试共享支出额度，不再只依赖早先的合约测试；测试中 Alice 和 Ben 使用独立密钥[S08]。
- 有用户用两个浏览器配置分别作为参与者和商家测试 FiberNuts 市场，首次即成功，领取约 1.5 秒、购买咖啡约 2 秒后商家拿到新 proofs，但也遇到水龙头最后一个 claim 等问题[S09]。FiberNuts 作者回应称该项目目前是 demo，未来更新会硬化 FiberNuts 协议，并覆盖反馈中的各点[S10]。
- 其他动态包括：有帖子介绍 ICDLT 2026，并提到 UTXO 家族钱包的三种 SDK 模式[S06]；防诈骗讨论中，有回复建议怀疑欺诈时在消息里 @ 社区版主[S07]；Omiga 团队回应称目前只跟踪所连接钱包的 Recommended CKB 地址，并提到其他 lock 下由 CCC 派生的资产问题[S11]。

## 值得继续跟进

- CKB IDL 提案的资助决定和落地节奏值得跟进，提案计划构建开源、testnet 优先的 Script Registry 并推进 IDL 0.1.1[S01]；社区对 TypeScript 支持和共享脚本注册表整合有期待[S04]。
- Kaze X CKB Unitour 延续提案已通过，后续可观察执行和验证相关更新；材料目前只给到投票通过与验证结果，执行安排尚未展开[S12]。
- FiberNuts 测试暴露的水龙头 claim 等问题值得跟进，作者称未来更新会硬化协议并覆盖反馈[S09, S10]；Omiga 对其他 lock 下资产跟踪的后续处理也可观察，当前材料只显示团队承认跟踪范围有限[S11]。

## 来源索引

- `S01` [[DIS] CKB IDL: Interface Description Language and Discoverability for CKB Scripts](https://talk.nervos.org/t/dis-ckb-idl-interface-description-language-and-discoverability-for-ckb-scripts/11031/1) | OWK50GA | 2026-10-23 15:41:30 CST | Summary One-paragraph Overview: This proposal requests a grant of $5,000 to build the next phase of the CKB IDL lifecycle: an open-source, testnet-first Script Registry for publishing, discovering, and independently verifying CKB script interfaces, together with IDL 0.1.1...
- `S02` [[DIS] CKB IDL: Interface Description Language and Discoverability for CKB Scripts](https://talk.nervos.org/t/dis-ckb-idl-interface-description-language-and-discoverability-for-ckb-scripts/11031/2) | Jedi_dtechmaker | 2026-10-23 16:08:57 CST | Really love the direction of this. Making script interfaces discoverable and verifiable is a massive win for CKB composability. This solves a huge headache for transaction builders. Wishing you the best with this proposal!
- `S03` [[DIS] CKB IDL: Interface Description Language and Discoverability for CKB Scripts](https://talk.nervos.org/t/dis-ckb-idl-interface-description-language-and-discoverability-for-ckb-scripts/11031/3) | OWK50GA | 2026-10-23 16:30:12 CST | Thank you, Jedi
- `S04` [[DIS] CKB IDL: Interface Description Language and Discoverability for CKB Scripts](https://talk.nervos.org/t/dis-ckb-idl-interface-description-language-and-discoverability-for-ckb-scripts/11031/4) | Code3ks | 2026-10-23 17:34:08 CST | This is a valuable step toward improving CKB developer experience. A verifiable IDL could help wallets and transaction builders discover script interfaces and catch witness-format errors before submission. TypeScript support and integration with a shared script registry would...
- `S05` [[DIS] CKB IDL: Interface Description Language and Discoverability for CKB Scripts](https://talk.nervos.org/t/dis-ckb-idl-interface-description-language-and-discoverability-for-ckb-scripts/11031/5) | 3m1n3nc3 | 2026-10-24 03:41:42 CST | This is a much-needed piece of infrastructure for the CKB ecosystem. One of the biggest barriers to building reusable applications on programmable blockchains is the amount of script-specific knowledge developers need before they can integrate with existing contracts or...
- `S06` [IEEE International Conference on DLT - PT 2026](https://talk.nervos.org/t/ieee-international-conference-on-dlt-pt-2026/11035/1) | knmo | 2026-10-23 20:18:00 CST | IEEE International Conference on Distributed Ledger Technologies (ICDLT) 2026! Three SDK Patterns for UTXO-Family Wallets The conference brings together academia and industry, with organizers from Nova School of Business and Economics, NOVA Information Management School, and...
- `S07` [这是诈骗邮件吧？](https://talk.nervos.org/t/topic/11022/4) | knmo | 2026-10-23 17:32:45 CST | You can tag moderators in messages like this here on the forum. If you’re unsure or suspect fraud, please tag a community moderator in the message. @zz_tovarishch
- `S08` [QuotaCell: Let your team spend without handing over the treasury](https://talk.nervos.org/t/quotacell-let-your-team-spend-without-handing-over-the-treasury/11002/4) | Ticoworld | 2026-10-23 13:55:16 CST | A small update on QuotaCell since I introduced it here last week. I’ve now tested the shared spending allowance using signed transactions sent to an isolated CKB node, rather than relying only on the earlier contract tests. For the test, Alice and Ben had separate keys and...
- `S09` [FiberNuts Community Market: A Testnet App for Cashu + Fiber](https://talk.nervos.org/t/fibernuts-community-market-a-testnet-app-for-cashu-fiber/10792/8) | LusoCryptoLabs | 2026-10-23 07:16:02 CST | Hi, I tried market.fibernuts.xyz last night with two browser profiles, one as attendee and one as vendor. Worked first time. The claim took about 1.5 s and a coffee about 2 s until the vendor had fresh proofs. Nice work. Some things I ran into: I got the last faucet claim of...
- `S10` [FiberNuts Community Market: A Testnet App for Cashu + Fiber](https://talk.nervos.org/t/fibernuts-community-market-a-testnet-app-for-cashu-fiber/10792/9) | Code3ks | 2026-10-23 12:29:15 CST | Thanks for the valuable feedback, this is a demo project at the moment, future updates includes hardening FiberNuts protocol, hence every point outlined here will be covered.
- `S11` [Omiga v1.2.0 Release: Enhanced On-Chain Asset Management and Deeper CCC Integration](https://talk.nervos.org/t/omiga-v1-2-0-release-enhanced-on-chain-asset-management-and-deeper-ccc-integration/10699/4) | Oliver | 2026-10-23 10:30:58 CST | Hi @phroi, thank you for the detailed write-up, and for taking the time to post it here even without an issue tracker to file it in. You’re right: Omiga currently only tracks the Recommended CKB address of the connected wallet, so assets held under other locks that CCC derives...
- `S12` [[DIS] Kaze X CKB Unitour Continuation Proposal](https://talk.nervos.org/t/dis-kaze-x-ckb-unitour-continuation-proposal/10736/5) | zz_tovarishch | 2026-10-23 09:57:23 CST | Based on the Metaforo tally at close, the outcome is PASSED. Approval is 100%, with total voting weight of 183,340,273 CKB from 13 voters. Both the approval threshold and minimum participation requirement are met. Post-close verification was completed on 23 October 2026 using...

## 活跃话题

1. [[DIS] CKB IDL: Interface Description Language and Discoverability for CKB Scripts](https://talk.nervos.org/t/dis-ckb-idl-interface-description-language-and-discoverability-for-ckb-scripts/11031) | 5 条近窗帖子 | 最新活动 2026-10-24 03:41:42 CST | tags: CKB-IDL
2. [IEEE International Conference on DLT - PT 2026](https://talk.nervos.org/t/ieee-international-conference-on-dlt-pt-2026/11035) | 1 条近窗帖子 | 最新活动 2026-10-23 20:18:00 CST | tags: Conference, ICDLT, IEEE
3. [这是诈骗邮件吧？](https://talk.nervos.org/t/topic/11022) | 1 条近窗帖子 | 最新活动 2026-10-23 17:32:45 CST
4. [QuotaCell: Let your team spend without handing over the treasury](https://talk.nervos.org/t/quotacell-let-your-team-spend-without-handing-over-the-treasury/11002) | 1 条近窗帖子 | 最新活动 2026-10-23 13:55:16 CST | tags: CKB, CKB-VM, lang-en
5. [FiberNuts Community Market: A Testnet App for Cashu + Fiber](https://talk.nervos.org/t/fibernuts-community-market-a-testnet-app-for-cashu-fiber/10792) | 2 条近窗帖子 | 最新活动 2026-10-23 12:29:15 CST | tags: CKB, dapp, testnet
6. [Omiga v1.2.0 Release: Enhanced On-Chain Asset Management and Deeper CCC Integration](https://talk.nervos.org/t/omiga-v1-2-0-release-enhanced-on-chain-asset-management-and-deeper-ccc-integration/10699) | 1 条近窗帖子 | 最新活动 2026-10-23 10:30:58 CST | tags: Nervos-项目动态, lang-en
7. [[DIS] Kaze X CKB Unitour Continuation Proposal](https://talk.nervos.org/t/dis-kaze-x-ckb-unitour-continuation-proposal/10736) | 1 条近窗帖子 | 最新活动 2026-10-23 09:57:23 CST | tags: CKB, CKB-VM, Grant, Nervos-项目动态, Spark-Program, appchain, dapp

## 最近帖子摘录

- 2026-10-24 03:41:42 CST | 3m1n3nc3 | [[DIS] CKB IDL: Interface Description Language and Discoverability for CKB Scripts](https://talk.nervos.org/t/dis-ckb-idl-interface-description-language-and-discoverability-for-ckb-scripts/11031/5) | This is a much-needed piece of infrastructure for the CKB ecosystem. One of the biggest barriers to building reusable applications on programmable blockchains is the amount of...
- 2026-10-23 20:18:00 CST | knmo | [IEEE International Conference on DLT - PT 2026](https://talk.nervos.org/t/ieee-international-conference-on-dlt-pt-2026/11035/1) | IEEE International Conference on Distributed Ledger Technologies (ICDLT) 2026! Three SDK Patterns for UTXO-Family Wallets The conference brings together academia and industry,...
- 2026-10-23 17:34:08 CST | Code3ks | [[DIS] CKB IDL: Interface Description Language and Discoverability for CKB Scripts](https://talk.nervos.org/t/dis-ckb-idl-interface-description-language-and-discoverability-for-ckb-scripts/11031/4) | This is a valuable step toward improving CKB developer experience. A verifiable IDL could help wallets and transaction builders discover script interfaces and catch witness-...
- 2026-10-23 17:32:45 CST | knmo | [这是诈骗邮件吧？](https://talk.nervos.org/t/topic/11022/4) | You can tag moderators in messages like this here on the forum. If you’re unsure or suspect fraud, please tag a community moderator in the message. @zz_tovarishch
- 2026-10-23 16:30:12 CST | OWK50GA | [[DIS] CKB IDL: Interface Description Language and Discoverability for CKB Scripts](https://talk.nervos.org/t/dis-ckb-idl-interface-description-language-and-discoverability-for-ckb-scripts/11031/3) | Thank you, Jedi
- 2026-10-23 16:08:57 CST | Jedi_dtechmaker | [[DIS] CKB IDL: Interface Description Language and Discoverability for CKB Scripts](https://talk.nervos.org/t/dis-ckb-idl-interface-description-language-and-discoverability-for-ckb-scripts/11031/2) | Really love the direction of this. Making script interfaces discoverable and verifiable is a massive win for CKB composability. This solves a huge headache for transaction...
- 2026-10-23 15:41:30 CST | OWK50GA | [[DIS] CKB IDL: Interface Description Language and Discoverability for CKB Scripts](https://talk.nervos.org/t/dis-ckb-idl-interface-description-language-and-discoverability-for-ckb-scripts/11031/1) | Summary One-paragraph Overview: This proposal requests a grant of $5,000 to build the next phase of the CKB IDL lifecycle: an open-source, testnet-first Script Registry for...
- 2026-10-23 13:55:16 CST | Ticoworld | [QuotaCell: Let your team spend without handing over the treasury](https://talk.nervos.org/t/quotacell-let-your-team-spend-without-handing-over-the-treasury/11002/4) | A small update on QuotaCell since I introduced it here last week. I’ve now tested the shared spending allowance using signed transactions sent to an isolated CKB node, rather...
- 2026-10-23 12:29:15 CST | Code3ks | [FiberNuts Community Market: A Testnet App for Cashu + Fiber](https://talk.nervos.org/t/fibernuts-community-market-a-testnet-app-for-cashu-fiber/10792/9) | Thanks for the valuable feedback, this is a demo project at the moment, future updates includes hardening FiberNuts protocol, hence every point outlined here will be covered.
- 2026-10-23 10:30:58 CST | Oliver | [Omiga v1.2.0 Release: Enhanced On-Chain Asset Management and Deeper CCC Integration](https://talk.nervos.org/t/omiga-v1-2-0-release-enhanced-on-chain-asset-management-and-deeper-ccc-integration/10699/4) | Hi @phroi, thank you for the detailed write-up, and for taking the time to post it here even without an issue tracker to file it in. You’re right: Omiga currently only tracks...
- 2026-10-23 09:57:23 CST | zz_tovarishch | [[DIS] Kaze X CKB Unitour Continuation Proposal](https://talk.nervos.org/t/dis-kaze-x-ckb-unitour-continuation-proposal/10736/5) | Based on the Metaforo tally at close, the outcome is PASSED. Approval is 100%, with total voting weight of 183,340,273 CKB from 13 voters. Both the approval threshold and...
- 2026-10-23 07:16:02 CST | LusoCryptoLabs | [FiberNuts Community Market: A Testnet App for Cashu + Fiber](https://talk.nervos.org/t/fibernuts-community-market-a-testnet-app-for-cashu-fiber/10792/8) | Hi, I tried market.fibernuts.xyz last night with two browser profiles, one as attendee and one as vendor. Worked first time. The claim took about 1.5 s and a coffee about 2 s...
