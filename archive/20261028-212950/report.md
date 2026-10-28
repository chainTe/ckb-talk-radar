# Nervos Talk 社区简报

- 统计窗口: 2026-10-28 05:29:50 CST 到 2026-10-29 05:29:50 CST
- 生成时间: 2026-10-29 05:30:01 CST
- 话题数: 7
- 帖子数: 11
- 作者数: 8
- 总结模式: ai:openai-compatible

## 社区总结

## 今日发生了什么

今天论坛的主要动静集中在 Myelin 的争议结算问答、CrowdCell 资助投票落地与首笔付款，以及 CKBSwap、CellScript 等开发进展上 [S01, S02, S03, S04, S08, S09, S10]。CrowdCell 投票以 100% 通过，总投票权重为 184,132,635 CKB、共 15 名投票者，并完成首笔 1,086,957 CKB 付款 [S03, S04, S05]。同时，Seedsong 支付第二期 50 美元（33,968 CKB），Kirea Finance 仍在催票以达 quorum [S06, S07]。

## 重点话题

- Myelin 讨论到 court verifier 上线后的结算路径：有人问应用能否用普通 CKB 交易结算单个争议 chunk 而不信任委员会，回复称这是预期设计，普通交易可独立验证有界争议块，但玩家资金还需可用证据和 escrow 规则来执行裁决 [S01, S02]。
- CrowdCell 投票结果为 PASSED，批准率 100%、总权重 184,132,635 CKB、15 名投票者，达到批准门槛和最低参与要求；随后公布首笔付款 1,086,957 CKB，并有成员确认第二次审查的四个小修复及对应 exploit 测试已加入 [S03, S04, S05]。
- Kirea Finance 作者称投票即将结束，但仍需更多投票权重达到 quorum；项目定位为 CKB 上开源、合规门控的 RWA 借贷基础设施，链上流程无桥、无托管 [S07]。
- CKBSwap 讨论中有人认为 batcher 方案不错，并提到 Cardano 上有同类模型；另有成员强调生产发布前 hot cell 问题是必须修复项，并认为 Cardano batcher 方案务实 [S08, S09]。
- CellScript 0.33.0-alpha.1 发布，#47、#48、#49 已关闭，帖子称这是 CellScript 的重要一步，并汇总了 0.31 以来的工作 [S10]。

## 值得继续跟进

- Myelin 的 court verifier 上线后，普通 CKB 交易结算争议块的实际路径、证据要求和 escrow 规则是否足够执行裁决，值得继续观察 [S01, S02]。
- Kirea Finance 投票窗口临近结束，quorum 是否达成以及最终投票结果需要跟进 [S07]。
- CKBSwap 生产发布前 hot cell 问题是否修复，以及 batcher 方案如何落地，是后续上线风险点 [S08, S09]。

## 来源索引

- `S01` [Introducing Myelin: a CKB-aligned off-chain Cell session runtime](https://talk.nervos.org/t/introducing-myelin-a-ckb-aligned-off-chain-cell-session-runtime/10498/13) | Kaylah | 2026-10-28 20:24:35 CST | Great work on this! so I’ve been reading this closely. One question about the court path, once the on-chain court verifier is live, could an application settle a single disputed chunk with a normal CKB transaction, without trusting the committee? I think that would make Myelin...
- `S02` [Introducing Myelin: a CKB-aligned off-chain Cell session runtime](https://talk.nervos.org/t/introducing-myelin-a-ckb-aligned-off-chain-cell-session-runtime/10498/14) | ArthurZhang | 2026-10-29 00:49:29 CST | Hi @Kaylah, yes , that is the intended design: a normal CKB transaction would verify a bounded disputed chunk independently of the committee. For players’ funds, the application also needs available evidence and escrow rules that enforce the verdict, allowing challenges and...
- `S03` [[DIS] CrowdCell: From Testnet Demo to a Crowdfunding Product on CKB | CrowdCell：把 CKB 测试网上的免信任众筹做成产品](https://talk.nervos.org/t/dis-crowdcell-from-testnet-demo-to-a-crowdfunding-product-on-ckb-crowdcell-ckb/10937/8) | zz_tovarishch | 2026-10-28 17:29:55 CST | Based on the Metaforo tally at close, the outcome is PASSED. Approval is 100%, with total voting weight of 184,132,635 CKB from 15 voters. Both the approval threshold and minimum participation requirement are met. Post-close verification was completed on 28 October 2026 using...
- `S04` [[DIS] CrowdCell: From Testnet Demo to a Crowdfunding Product on CKB | CrowdCell：把 CKB 测试网上的免信任众筹做成产品](https://talk.nervos.org/t/dis-crowdcell-from-testnet-demo-to-a-crowdfunding-product-on-ckb-crowdcell-ckb/10937/9) | zz_tovarishch | 2026-10-28 23:46:47 CST | Initial Payout $1,500/0.00138=1,086,957 CKB https://explorer.nervos.org/transaction/0x3d12304de80fcf871c7a8cc7adf67821c86da301843654f91d16299977030dd4
- `S05` [[DIS] CrowdCell: From Testnet Demo to a Crowdfunding Product on CKB | CrowdCell：把 CKB 测试网上的免信任众筹做成产品](https://talk.nervos.org/t/dis-crowdcell-from-testnet-demo-to-a-crowdfunding-product-on-ckb-crowdcell-ckb/10937/10) | Ayoub_Lesfer | 2026-10-29 00:26:32 CST | Thanks everyone who voted, and @zz_tovarishch for the verification and for sending the first payout. As promised in §6.5, the four small fixes from Officeyutong’s second review are in, each with an exploit test that was accepted by the old contracts and is rejected now, and...
- `S06` [[Spark Program] SeedsSpark Program | Seedsong: On-Chain Generative Music with Spore DOB and light-client-wasmong 种子唱片：基于 Spore DOB 与 light-client-wasm 的链上生成音乐](https://talk.nervos.org/t/spark-program-seedsspark-program-seedsong-on-chain-generative-music-with-spore-dob-and-light-client-wasmong-spore-dob-light-client-wasm/10997/6) | xingtianchunyan | 2026-10-28 20:47:29 CST | Hi @Officeyutong , The second installment (50 USD) : 33,968 CKB 0xac98590ce7cc48aea9412a62360e45253ea7ed8ea69246e0ee64dc29983c106b Best, xingtian On behalf of the Spark Program Committee
- `S07` [[DIS] Kirea Finance: Native RWA Lending Infrastructure for CKB |【DIS】Kirea Finance：面向 CKB 的原生 RWA 借贷基础设施](https://talk.nervos.org/t/dis-kirea-finance-native-rwa-lending-infrastructure-for-ckb-dis-kirea-finance-ckb-rwa/10809/31) | SalmanDev | 2026-10-28 19:38:27 CST | Hey everyone, voting on Kirea Finance closes soon, and I still need more voting weight to reach quorum! Kirea Finance is building open-source infrastructure for compliance-gated RWA lending directly on CKB, with no bridge and no custodian in the on-chain flow. The full lending...
- `S08` [Introducing CKBSwap — Building on CKB for the Long Term](https://talk.nervos.org/t/introducing-ckbswap-building-on-ckb-for-the-long-term/11060/5) | longdevbf | 2026-10-28 08:35:13 CST | I think batcher is good. I seen the same model and dex on cardano. minswap.org
- `S09` [Introducing CKBSwap — Building on CKB for the Long Term](https://talk.nervos.org/t/introducing-ckbswap-building-on-ckb-for-the-long-term/11060/6) | RetricSu | 2026-10-28 14:15:02 CST | great to know that. I think for the production launch, the hot cell issue is a must-fix problem. otherwise people won’t take it seriously. the cardano batcher solution seems practical. thanks @longdevbf I think DeFi might not be the killer app for CKB, but it definitely is...
- `S10` [CellScript - A DSL for Cell-Based Contracts](https://talk.nervos.org/t/cellscript-a-dsl-for-cell-based-contracts/10193/35) | ArthurZhang | 2026-10-28 13:11:24 CST | CellScript 0.33 Alpha: A Major Step Forward for CellScript Contracts CellScript 0.33.0-alpha.1 is out, and #47, #48, #49 are now closed. This is one of the largest steps forward CellScript has taken. The release brings together the work since 0.31, including the intervening...
- `S11` [UTXOPlay: A Community-Driven Gaming Platform for Nervos](https://talk.nervos.org/t/utxoplay-a-community-driven-gaming-platform-for-nervos/11049/4) | longdevbf | 2026-10-28 08:49:00 CST | Good stuffs

## 活跃话题

1. [Introducing Myelin: a CKB-aligned off-chain Cell session runtime](https://talk.nervos.org/t/introducing-myelin-a-ckb-aligned-off-chain-cell-session-runtime/10498) | 2 条近窗帖子 | 最新活动 2026-10-29 00:49:29 CST | tags: CKB-VM, CellScript, Myelin, lang-en
2. [[DIS] CrowdCell: From Testnet Demo to a Crowdfunding Product on CKB | CrowdCell：把 CKB 测试网上的免信任众筹做成产品](https://talk.nervos.org/t/dis-crowdcell-from-testnet-demo-to-a-crowdfunding-product-on-ckb-crowdcell-ckb/10937) | 3 条近窗帖子 | 最新活动 2026-10-29 00:26:32 CST | tags: lang-en
3. [[Spark Program] SeedsSpark Program | Seedsong: On-Chain Generative Music with Spore DOB and light-client-wasmong 种子唱片：基于 Spore DOB 与 light-client-wasm 的链上生成音乐](https://talk.nervos.org/t/spark-program-seedsspark-program-seedsong-on-chain-generative-music-with-spore-dob-and-light-client-wasmong-spore-dob-light-client-wasm/10997) | 1 条近窗帖子 | 最新活动 2026-10-28 20:47:29 CST | tags: In-Progress, Spark-Program
4. [[DIS] Kirea Finance: Native RWA Lending Infrastructure for CKB |【DIS】Kirea Finance：面向 CKB 的原生 RWA 借贷基础设施](https://talk.nervos.org/t/dis-kirea-finance-native-rwa-lending-infrastructure-for-ckb-dis-kirea-finance-ckb-rwa/10809) | 1 条近窗帖子 | 最新活动 2026-10-28 19:38:27 CST | tags: CKB, DeFi, defi挖矿, lang-es, lang-zh
5. [Introducing CKBSwap — Building on CKB for the Long Term](https://talk.nervos.org/t/introducing-ckbswap-building-on-ckb-for-the-long-term/11060) | 2 条近窗帖子 | 最新活动 2026-10-28 14:15:02 CST
6. [CellScript - A DSL for Cell-Based Contracts](https://talk.nervos.org/t/cellscript-a-dsl-for-cell-based-contracts/10193) | 1 条近窗帖子 | 最新活动 2026-10-28 13:11:24 CST | tags: CKB-VM, CellScript, DSL, lang-en
7. [UTXOPlay: A Community-Driven Gaming Platform for Nervos](https://talk.nervos.org/t/utxoplay-a-community-driven-gaming-platform-for-nervos/11049) | 1 条近窗帖子 | 最新活动 2026-10-28 08:49:00 CST | tags: CKB, game

## 最近帖子摘录

- 2026-10-29 00:49:29 CST | ArthurZhang | [Introducing Myelin: a CKB-aligned off-chain Cell session runtime](https://talk.nervos.org/t/introducing-myelin-a-ckb-aligned-off-chain-cell-session-runtime/10498/14) | Hi @Kaylah, yes , that is the intended design: a normal CKB transaction would verify a bounded disputed chunk independently of the committee. For players’ funds, the application...
- 2026-10-29 00:26:32 CST | Ayoub_Lesfer | [[DIS] CrowdCell: From Testnet Demo to a Crowdfunding Product on CKB | CrowdCell：把 CKB 测试网上的免信任众筹做成产品](https://talk.nervos.org/t/dis-crowdcell-from-testnet-demo-to-a-crowdfunding-product-on-ckb-crowdcell-ckb/10937/10) | Thanks everyone who voted, and @zz_tovarishch for the verification and for sending the first payout. As promised in §6.5, the four small fixes from Officeyutong’s second review...
- 2026-10-28 23:46:47 CST | zz_tovarishch | [[DIS] CrowdCell: From Testnet Demo to a Crowdfunding Product on CKB | CrowdCell：把 CKB 测试网上的免信任众筹做成产品](https://talk.nervos.org/t/dis-crowdcell-from-testnet-demo-to-a-crowdfunding-product-on-ckb-crowdcell-ckb/10937/9) | Initial Payout $1,500/0.00138=1,086,957 CKB https://explorer.nervos.org/transaction/0x3d12304de80fcf871c7a8cc7adf67821c86da301843654f91d16299977030dd4
- 2026-10-28 20:47:29 CST | xingtianchunyan | [[Spark Program] SeedsSpark Program | Seedsong: On-Chain Generative Music with Spore DOB and light-client-wasmong 种子唱片：基于 Spore DOB 与 light-client-wasm 的链上生成音乐](https://talk.nervos.org/t/spark-program-seedsspark-program-seedsong-on-chain-generative-music-with-spore-dob-and-light-client-wasmong-spore-dob-light-client-wasm/10997/6) | Hi @Officeyutong , The second installment (50 USD) : 33,968 CKB 0xac98590ce7cc48aea9412a62360e45253ea7ed8ea69246e0ee64dc29983c106b Best, xingtian On behalf of the Spark Program...
- 2026-10-28 20:24:35 CST | Kaylah | [Introducing Myelin: a CKB-aligned off-chain Cell session runtime](https://talk.nervos.org/t/introducing-myelin-a-ckb-aligned-off-chain-cell-session-runtime/10498/13) | Great work on this! so I’ve been reading this closely. One question about the court path, once the on-chain court verifier is live, could an application settle a single disputed...
- 2026-10-28 19:38:27 CST | SalmanDev | [[DIS] Kirea Finance: Native RWA Lending Infrastructure for CKB |【DIS】Kirea Finance：面向 CKB 的原生 RWA 借贷基础设施](https://talk.nervos.org/t/dis-kirea-finance-native-rwa-lending-infrastructure-for-ckb-dis-kirea-finance-ckb-rwa/10809/31) | Hey everyone, voting on Kirea Finance closes soon, and I still need more voting weight to reach quorum! Kirea Finance is building open-source infrastructure for compliance-gated...
- 2026-10-28 17:29:55 CST | zz_tovarishch | [[DIS] CrowdCell: From Testnet Demo to a Crowdfunding Product on CKB | CrowdCell：把 CKB 测试网上的免信任众筹做成产品](https://talk.nervos.org/t/dis-crowdcell-from-testnet-demo-to-a-crowdfunding-product-on-ckb-crowdcell-ckb/10937/8) | Based on the Metaforo tally at close, the outcome is PASSED. Approval is 100%, with total voting weight of 184,132,635 CKB from 15 voters. Both the approval threshold and...
- 2026-10-28 14:15:02 CST | RetricSu | [Introducing CKBSwap — Building on CKB for the Long Term](https://talk.nervos.org/t/introducing-ckbswap-building-on-ckb-for-the-long-term/11060/6) | great to know that. I think for the production launch, the hot cell issue is a must-fix problem. otherwise people won’t take it seriously. the cardano batcher solution seems...
- 2026-10-28 13:11:24 CST | ArthurZhang | [CellScript - A DSL for Cell-Based Contracts](https://talk.nervos.org/t/cellscript-a-dsl-for-cell-based-contracts/10193/35) | CellScript 0.33 Alpha: A Major Step Forward for CellScript Contracts CellScript 0.33.0-alpha.1 is out, and #47, #48, #49 are now closed. This is one of the largest steps forward...
- 2026-10-28 08:49:00 CST | longdevbf | [UTXOPlay: A Community-Driven Gaming Platform for Nervos](https://talk.nervos.org/t/utxoplay-a-community-driven-gaming-platform-for-nervos/11049/4) | Good stuffs
- 2026-10-28 08:35:13 CST | longdevbf | [Introducing CKBSwap — Building on CKB for the Long Term](https://talk.nervos.org/t/introducing-ckbswap-building-on-ckb-for-the-long-term/11060/5) | I think batcher is good. I seen the same model and dex on cardano. minswap.org
