# Nervos Talk 社区简报

- 统计窗口: 2026-06-23 03:11:38 CST 到 2026-06-24 03:11:38 CST
- 生成时间: 2026-06-24 03:11:43 CST
- 话题数: 7
- 帖子数: 10
- 作者数: 9
- 总结模式: ai:openrouter

## 社区总结

## 今日发生了什么

最近24小时Nervos Talk社区整体较为平静，讨论主要集中在Fiber生态工具和CKB开发基础设施两个方向。[S04, S05, S06, S07] Spark资助项目的评审互动和zk-proof的技术探讨也在推进中，但没有重大公告或突发事件。[S02, S06]

## 重点话题

- **Fiber Desktop完成首个里程碑**：ebubedev宣布Fiber Studio v1重建的Milestone 1已完成，目前已准备好进行早期测试。[S04] 该项目从月初开始重写，采用了新的代码仓库。[S04]

- **FiberLatch新提案寻求资助**：Ticoworld提交了3000美元的Spark grant提案，计划为Fiber支付流构建开源的访问控制层FiberLatch Access，与现有的fiber-pay形成互补。[S05]

- **CellKit资助提案进入深度评审**：xingtianchunyan对Fidelcoder调整后的CellKit提案（预算从1500美元压缩至1000美元）提出三个关键问题，核心追问其与CCC的差异化定位；Fidelcoder回应称CellKit并非替代CCC，而是面向不同开发者需求。[S06, S07]

- **ArthurZhang推迟zk-proof脚本探索**：ArthurZhang回应Mulandi_Cecilia关于基于CellScript构建zk lock script的讨论，表示本周忙于CellScript大型更新，预计下周一/二发布后再深入该方向。[S02]

## 值得继续跟进

- **CellKit能否清晰区分与CCC的边界**：评审方明确要求论证"CCC用3行代码就能完成CKB转账"的前提下CellKit的独立价值，开发者回应尚待委员会进一步反馈。[S06, S07]

- **Fiber Studio早期测试的实际反馈**：Milestone 1刚完成，后续测试者的使用体验将决定这款Fiber桌面工具的市场接受度。[S04]

- **FiberLatch grant评审结果**：作为Fiber支付生态的新基建提案，其3000美元的资助申请能否获批将影响该细分方向的工具丰富度。[S05]

## 来源索引

- `S01` [Research Notes: What Zero-Knowledge Proofs Enable on CKB](https://talk.nervos.org/t/research-notes-what-zero-knowledge-proofs-enable-on-ckb/10368/5) | Mulandi_Cecilia | 2026-06-24 01:56:04 CST | Thank you! Yeah, the binding layer is something I’ve been digging into too. Your post nudged me to think about it more concretely.I went through the CellScript material and the framing makes sense to me. On the side, I’ve been thinking about a smaller idea: a lock script that...
- `S02` [Research Notes: What Zero-Knowledge Proofs Enable on CKB](https://talk.nervos.org/t/research-notes-what-zero-knowledge-proofs-enable-on-ckb/10368/6) | ArthurZhang | 2026-06-24 02:28:20 CST | Sure, I’d be very happy to explore this direction. Though this week is a bit packed on my side, as I’m preparing a fairly large CellScript update, once it is out on next Monday/Tuesday-ish, I’d be glad to look at this properly.
- `S03` [Research Notes: What Zero-Knowledge Proofs Enable on CKB](https://talk.nervos.org/t/research-notes-what-zero-knowledge-proofs-enable-on-ckb/10368/7) | Mulandi_Cecilia | 2026-06-24 02:32:21 CST | It’s okay. Feel free to ping me @ceciliamulandi on tg.
- `S04` [[DIS] Fiber Desktop v1 ground-up rebuild and launch — fnn desktop app](https://talk.nervos.org/t/dis-fiber-desktop-v1-ground-up-rebuild-and-launch-fnn-desktop-app/10317/18) | ebubedev | 2026-06-24 00:42:33 CST | Milestone 1 complete: Fiber Studio is ready for early testing Hi everyone, Following up on my Fiber Studio + new repo update - Milestone 1 is done. How we started (beginning of June) Work on the v1 rebuild started at the beginning of this month. Before writing production app...
- `S05` [[DIS] FiberLatch Access - Open-Source Access Control for Fiber Payments](https://talk.nervos.org/t/dis-fiberlatch-access-open-source-access-control-for-fiber-payments/10414/1) | Ticoworld | 2026-06-23 21:00:25 CST | ## Summary This proposal requests a grant of **$3,000** to build **FiberLatch Access**, an open-source access-control layer for Fiber payment flows. The simple idea is this: > fiber-pay helps apps accept Fiber payments. > FiberLatch Access helps apps decide what a paid user...
- `S06` [Spark Program | CellKit Actions — Reusable Transaction Actions for CKB Apps](https://talk.nervos.org/t/spark-program-cellkit-actions-reusable-transaction-actions-for-ckb-apps/10375/4) | xingtianchunyan | 2026-06-23 16:08:07 CST | Hi @Fidelcoder， 感谢你根据上一轮反馈积极调整提案——将预算从 $1,500 压缩至 $1,000，补充了独立的 Open Source Commitment 章节，To-Do List 也做了细化。目前提案的可读性已经大幅提高，但仍有一些问题需要确认，这些仍是我阅读提案后的想法，不代表委员会的立场。 但在提交正式评审之前，我想邀请你先回答以下三个问题： 1. CellKit 解决了 CCC（CKB Core Components）没有解决的具体问题是什么？ CCC 已经可以用 3 行代码完成 CKB 转账： const tx =...
- `S07` [Spark Program | CellKit Actions — Reusable Transaction Actions for CKB Apps](https://talk.nervos.org/t/spark-program-cellkit-actions-reusable-transaction-actions-for-ckb-apps/10375/5) | Fidelcoder | 2026-06-23 18:35:30 CST | Hi @xingtianchunyan, Thank you for the clear questions. I agree this distinction needs to be made more explicit. CellKit is not intended to replace CCC. CCC is already the right low-level SDK/tooling layer for developers building directly in JS/TS. CellKit’s goal is different:...
- `S08` [[DIS] Luxvoid Protocol: The First Working BTC→CKB→EVM Pipeline — Seeking DAO Support/collab for Production Scaling](https://talk.nervos.org/t/dis-luxvoid-protocol-the-first-working-btc-ckb-evm-pipeline-seeking-dao-support-collab-for-production-scaling/10400/14) | baclaire | 2026-06-23 15:52:32 CST | The project is very interesting, in my opinion at this level ,you dont need the Fund from the DAO, you need the community of investors believing in your project. I dont know about Canada regulation , but you can tokenize the $150000, and let others in the community support...
- `S09` [Introducing `cobuild-otx-contracts`: A Reference Implementation for CoBuild OTX Contracts](https://talk.nervos.org/t/introducing-cobuild-otx-contracts-a-reference-implementation-for-cobuild-otx-contracts/10413/2) | Fisher | 2026-06-23 11:10:31 CST | 虽然我看不懂，但你真是人类之光。
- `S10` [CKB Ecosystem Biweekly Update](https://talk.nervos.org/t/ckb-ecosystem-biweekly-update/9821/21) | zz_tovarishch | 2026-06-23 10:53:13 CST | image1380×776 225 KB CKB Ecosystem Biweekly Update #19 Welcome to the latest CKB Ecosystem Biweekly Update. Here’s a quick summary of key dev and ecosystem progress from the past two weeks. Infrastructure & Tooling @CKBdev completed ckb-vote-poc e2e tests + SDK, feasibility...

## 活跃话题

1. [Research Notes: What Zero-Knowledge Proofs Enable on CKB](https://talk.nervos.org/t/research-notes-what-zero-knowledge-proofs-enable-on-ckb/10368) | 3 条近窗帖子 | 最新活动 2026-06-24 02:32:21 CST | tags: CKB-VM, architecture, groth16, sp1, zero-knowledge, zkvm
2. [[DIS] Fiber Desktop v1 ground-up rebuild and launch — fnn desktop app](https://talk.nervos.org/t/dis-fiber-desktop-v1-ground-up-rebuild-and-launch-fnn-desktop-app/10317) | 1 条近窗帖子 | 最新活动 2026-06-24 00:42:33 CST | tags: fiber
3. [[DIS] FiberLatch Access - Open-Source Access Control for Fiber Payments](https://talk.nervos.org/t/dis-fiberlatch-access-open-source-access-control-for-fiber-payments/10414) | 1 条近窗帖子 | 最新活动 2026-06-23 21:00:25 CST | tags: CKB, dapp, testnet
4. [Spark Program | CellKit Actions — Reusable Transaction Actions for CKB Apps](https://talk.nervos.org/t/spark-program-cellkit-actions-reusable-transaction-actions-for-ckb-apps/10375) | 2 条近窗帖子 | 最新活动 2026-06-23 18:35:30 CST | tags: Spark-Program
5. [[DIS] Luxvoid Protocol: The First Working BTC→CKB→EVM Pipeline — Seeking DAO Support/collab for Production Scaling](https://talk.nervos.org/t/dis-luxvoid-protocol-the-first-working-btc-ckb-evm-pipeline-seeking-dao-support-collab-for-production-scaling/10400) | 1 条近窗帖子 | 最新活动 2026-06-23 15:52:32 CST | tags: CKB, RGBpp, testnet
6. [Introducing `cobuild-otx-contracts`: A Reference Implementation for CoBuild OTX Contracts](https://talk.nervos.org/t/introducing-cobuild-otx-contracts-a-reference-implementation-for-cobuild-otx-contracts/10413) | 1 条近窗帖子 | 最新活动 2026-06-23 11:10:31 CST
7. [CKB Ecosystem Biweekly Update](https://talk.nervos.org/t/ckb-ecosystem-biweekly-update/9821) | 1 条近窗帖子 | 最新活动 2026-06-23 10:53:13 CST | tags: Ecosystem-Update

## 最近帖子摘录

- 2026-06-24 02:32:21 CST | Mulandi_Cecilia | [Research Notes: What Zero-Knowledge Proofs Enable on CKB](https://talk.nervos.org/t/research-notes-what-zero-knowledge-proofs-enable-on-ckb/10368/7) | It’s okay. Feel free to ping me @ceciliamulandi on tg.
- 2026-06-24 02:28:20 CST | ArthurZhang | [Research Notes: What Zero-Knowledge Proofs Enable on CKB](https://talk.nervos.org/t/research-notes-what-zero-knowledge-proofs-enable-on-ckb/10368/6) | Sure, I’d be very happy to explore this direction. Though this week is a bit packed on my side, as I’m preparing a fairly large CellScript update, once it is out on next...
- 2026-06-24 01:56:04 CST | Mulandi_Cecilia | [Research Notes: What Zero-Knowledge Proofs Enable on CKB](https://talk.nervos.org/t/research-notes-what-zero-knowledge-proofs-enable-on-ckb/10368/5) | Thank you! Yeah, the binding layer is something I’ve been digging into too. Your post nudged me to think about it more concretely.I went through the CellScript material and the...
- 2026-06-24 00:42:33 CST | ebubedev | [[DIS] Fiber Desktop v1 ground-up rebuild and launch — fnn desktop app](https://talk.nervos.org/t/dis-fiber-desktop-v1-ground-up-rebuild-and-launch-fnn-desktop-app/10317/18) | Milestone 1 complete: Fiber Studio is ready for early testing Hi everyone, Following up on my Fiber Studio + new repo update - Milestone 1 is done. How we started (beginning of...
- 2026-06-23 21:00:25 CST | Ticoworld | [[DIS] FiberLatch Access - Open-Source Access Control for Fiber Payments](https://talk.nervos.org/t/dis-fiberlatch-access-open-source-access-control-for-fiber-payments/10414/1) | ## Summary This proposal requests a grant of **$3,000** to build **FiberLatch Access**, an open-source access-control layer for Fiber payment flows. The simple idea is this: >...
- 2026-06-23 18:35:30 CST | Fidelcoder | [Spark Program | CellKit Actions — Reusable Transaction Actions for CKB Apps](https://talk.nervos.org/t/spark-program-cellkit-actions-reusable-transaction-actions-for-ckb-apps/10375/5) | Hi @xingtianchunyan, Thank you for the clear questions. I agree this distinction needs to be made more explicit. CellKit is not intended to replace CCC. CCC is already the right...
- 2026-06-23 16:08:07 CST | xingtianchunyan | [Spark Program | CellKit Actions — Reusable Transaction Actions for CKB Apps](https://talk.nervos.org/t/spark-program-cellkit-actions-reusable-transaction-actions-for-ckb-apps/10375/4) | Hi @Fidelcoder， 感谢你根据上一轮反馈积极调整提案——将预算从 $1,500 压缩至 $1,000，补充了独立的 Open Source Commitment 章节，To-Do List 也做了细化。目前提案的可读性已经大幅提高，但仍有一些问题需要确认，这些仍是我阅读提案后的想法，不代表委员会的立场。...
- 2026-06-23 15:52:32 CST | baclaire | [[DIS] Luxvoid Protocol: The First Working BTC→CKB→EVM Pipeline — Seeking DAO Support/collab for Production Scaling](https://talk.nervos.org/t/dis-luxvoid-protocol-the-first-working-btc-ckb-evm-pipeline-seeking-dao-support-collab-for-production-scaling/10400/14) | The project is very interesting, in my opinion at this level ,you dont need the Fund from the DAO, you need the community of investors believing in your project. I dont know...
- 2026-06-23 11:10:31 CST | Fisher | [Introducing `cobuild-otx-contracts`: A Reference Implementation for CoBuild OTX Contracts](https://talk.nervos.org/t/introducing-cobuild-otx-contracts-a-reference-implementation-for-cobuild-otx-contracts/10413/2) | 虽然我看不懂，但你真是人类之光。
- 2026-06-23 10:53:13 CST | zz_tovarishch | [CKB Ecosystem Biweekly Update](https://talk.nervos.org/t/ckb-ecosystem-biweekly-update/9821/21) | image1380×776 225 KB CKB Ecosystem Biweekly Update #19 Welcome to the latest CKB Ecosystem Biweekly Update. Here’s a quick summary of key dev and ecosystem progress from the...
