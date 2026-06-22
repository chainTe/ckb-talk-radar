# Nervos Talk 社区简报

- 统计窗口: 2026-06-22 04:07:56 CST 到 2026-06-23 04:07:56 CST
- 生成时间: 2026-06-23 04:08:01 CST
- 话题数: 9
- 帖子数: 12
- 作者数: 11
- 总结模式: ai:openrouter

## 社区总结

## 今日发生了什么

Nervos Talk 今天迎来了多个技术项目的实质性更新：Pocket Node 安卓轻客户端发布 v1.7.4 可靠性版本，Liquid Cells 微支付 Rollup 开源上线测试网，同时社区内出现了关于 DAO 提案是否存在诈骗风险的激烈争论。[S02, S11, S07, S08]

## 重点话题

- **Pocket Node 安卓版迭代**：Jnr6 发布了 v1.7.4 版本，主要修复钱包同步和 Nervos DAO 的稳定性问题，这次更新几乎完全基于论坛和 Telegram 的用户反馈。[S02]

- **Liquid Cells 开源亮相**：T_Silva 团队将 operator-trustless 的微支付 Rollup 开源并部署到 Pudge 测试网，允许大量用户在单一 anchor cell 后持有和转移不足 61 CKB 的余额，正在招募代码审查者。[S11]

- **Luxvoid Protocol 推进生产化**：Ar_Hel 详细披露了 BTC→CKB→EVM 管道的 Phase 1-2 路线图，包括 Prometheus + Grafana 监控体系和 SPV 服务同步指标；Aki 对此表示认可，认为其工程拆解与提案高度对齐。[S03, S04]

- **社区信任危机浮现**：ckbbkc 发帖质疑 CKB 正被诈骗团队盯上，通过 DAO 提案骗取资金；matt_ckb 以管理员身份强硬回应，称 DAO 提案公开透明，此类"低 effort"帖子不会被容忍。[S07, S08]

- **开发工具链持续扩展**：orange-xc 发布了 cobuild-otx-contracts 参考实现，用于 CoBuild 与 Open Transaction 工作流的合约开发；PlasticLove 的 CellScript 网站 v0 上线后，社区成员期待 cookbook 发布。[S05, S12]

## 值得继续跟进

- Luxvoid Protocol 的 DAO 资金申请能否通过社区审查，以及其监控体系落地后的实际运行数据。[S03, S04]

- "Scam DIS" 帖引发的紧张氛围是否会蔓延，管理员与质疑者之间的摩擦是否会影响后续提案讨论环境。[S07, S08]

- Liquid Cells 在 Pudge 测试网的表现及外部代码审查反馈，这关系到 CKB 生态首个 operator-trustless 微支付 Rollup 能否进入主网阶段。[S11]

## 来源索引

- `S01` [Spark Program | Nervos Brain - A Global Developer Onboarding Engine and Cross-Language Hub Powered by Agentic RAG](https://talk.nervos.org/t/spark-program-nervos-brain-a-global-developer-onboarding-engine-and-cross-language-hub-powered-by-agentic-rag/9995/41) | IrisNeko | 2026-06-23 00:17:41 CST | Delivery Report This post is the delivery report for: Spark Program | Nervos Brain - A Global Developer Onboarding Engine and Cross-Language Hub Powered by Agentic RAG Nervos Brain is designed to address two core bottlenecks in the Nervos / CKB ecosystem: High onboarding...
- `S02` [[DIS] Mobile-Ready CKB Light Client (Pocket Node) for Android](https://talk.nervos.org/t/dis-mobile-ready-ckb-light-client-pocket-node-for-android/9879/60) | Jnr6 | 2026-06-22 21:43:07 CST | Title: Pocket Node v1.7.4 is out — sync and Nervos DAO reliability Pocket Node v1.7.4 is live. This one is a reliability release driven almost entirely by your reports here and on Telegram. Thank you to everyone who sent screenshots and steps to reproduce. Sync Wallets with a...
- `S03` [[DIS] Luxvoid Protocol: The First Working BTC→CKB→EVM Pipeline — Seeking DAO Support/collab for Production Scaling](https://talk.nervos.org/t/dis-luxvoid-protocol-the-first-working-btc-ckb-evm-pipeline-seeking-dao-support-collab-for-production-scaling/10400/12) | Ar_Hel | 2026-06-22 18:49:42 CST | roadmap Phase 1: Operational Stability (1-2 months) Goal: Ensure uninterrupted operation of current infrastructure Tasks: Monitoring and alerting Set up Prometheus + Grafana to track: SPV service synchronization (lag from Bitcoin mainnet) Dormant cells status “Fires” success...
- `S04` [[DIS] Luxvoid Protocol: The First Working BTC→CKB→EVM Pipeline — Seeking DAO Support/collab for Production Scaling](https://talk.nervos.org/t/dis-luxvoid-protocol-the-first-working-btc-ckb-evm-pipeline-seeking-dao-support-collab-for-production-scaling/10400/13) | Aki | 2026-06-22 20:22:17 CST | @Ar_Hel — this is exactly the kind of response I was hoping for from this community. A well-structured, engineer-level breakdown that shows you’ve actually read the proposal and understand the infrastructure scope. Your Phase 1-2 aligns directly with what I outlined....
- `S05` [Introducing `cobuild-otx-contracts`: A Reference Implementation for CoBuild OTX Contracts](https://talk.nervos.org/t/introducing-cobuild-otx-contracts-a-reference-implementation-for-cobuild-otx-contracts/10413/1) | orange-xc | 2026-06-22 19:50:35 CST | This repository（ xcshuan/cobuild-otx-contracts） is a working reference implementation and testbed for building CKB contracts around CoBuild and Open Transaction (OTX) workflows. The design is based on the ideas described in: CKB Transaction CoBuild Protocol Overview CKB Open...
- `S06` [Vellum, extended: from identity to reputation on did:ckb](https://talk.nervos.org/t/vellum-extended-from-identity-to-reputation-on-did-ckb/10406/2) | doitian | 2026-06-22 13:43:45 CST | If the claim cell is owned by subjects, where the capacity originates from? It’s interesting design to let subjects destroy claim cells on them. The live cells are bidirectionally approved claims, while the dead cells are rejected by subjects but still accessible in the...
- `S07` [Scam DIS](https://talk.nervos.org/t/scam-dis/10412/1) | ckbbkc | 2026-06-22 11:28:23 CST | Do you think CKB is being targeted by scam teams? They’re frantically applying for various DAO proposals to swindle funds from DAOs. Weak public chains often attract scam teams.
- `S08` [Scam DIS](https://talk.nervos.org/t/scam-dis/10412/2) | matt_ckb | 2026-06-22 12:16:02 CST | The DAO proposals are public, please draw your own conclusions. This type of low effort post won’t be tolerated.
- `S09` [Scam DIS](https://talk.nervos.org/t/scam-dis/10412/3) | matt_ckb | 2026-06-22 12:16:48 CST | 
- `S10` [Research Notes: What Zero-Knowledge Proofs Enable on CKB](https://talk.nervos.org/t/research-notes-what-zero-knowledge-proofs-enable-on-ckb/10368/4) | ArthurZhang | 2026-06-22 12:10:09 CST | Greate notes. I think you already touch the shape of this through the old-cell / new-cell / witness-proof pattern. I wonder whether there is a useful follow-up around the binding layer: how tooling helps make sure the proof is wired to the intended CKB cell transition？ I’ve...
- `S11` [Liquid Cells: an operator-trustless, pooled micro-payment rollup for CKB, now open source, live on Pudge, and looking for reviewers](https://talk.nervos.org/t/liquid-cells-an-operator-trustless-pooled-micro-payment-rollup-for-ckb-now-open-source-live-on-pudge-and-looking-for-reviewers/10411/1) | T_Silva | 2026-06-22 10:50:19 CST | Hi, We’ve just open-sourced Liquid Cells under MIT, and it’s running live on the Pudge testnet. It’s a small, focused thing: a pooled, operator-trustless micro-payment rollup that lets thousands of people hold and move sub-61-CKB balances behind a single anchor cell, with no...
- `S12` [CellScript Website v0 Is Live](https://talk.nervos.org/t/cellscript-website-v0-is-live/10403/2) | PlasticLove | 2026-06-22 10:30:16 CST | 期待 cookbook！

## 活跃话题

1. [Spark Program | Nervos Brain - A Global Developer Onboarding Engine and Cross-Language Hub Powered by Agentic RAG](https://talk.nervos.org/t/spark-program-nervos-brain-a-global-developer-onboarding-engine-and-cross-language-hub-powered-by-agentic-rag/9995) | 1 条近窗帖子 | 最新活动 2026-06-23 00:17:41 CST | tags: In-Progress, Spark-Program
2. [[DIS] Mobile-Ready CKB Light Client (Pocket Node) for Android](https://talk.nervos.org/t/dis-mobile-ready-ckb-light-client-pocket-node-for-android/9879) | 1 条近窗帖子 | 最新活动 2026-06-22 21:43:07 CST | tags: CKB, light-client
3. [[DIS] Luxvoid Protocol: The First Working BTC→CKB→EVM Pipeline — Seeking DAO Support/collab for Production Scaling](https://talk.nervos.org/t/dis-luxvoid-protocol-the-first-working-btc-ckb-evm-pipeline-seeking-dao-support-collab-for-production-scaling/10400) | 2 条近窗帖子 | 最新活动 2026-06-22 20:22:17 CST | tags: CKB, RGBpp, testnet
4. [Introducing `cobuild-otx-contracts`: A Reference Implementation for CoBuild OTX Contracts](https://talk.nervos.org/t/introducing-cobuild-otx-contracts-a-reference-implementation-for-cobuild-otx-contracts/10413) | 1 条近窗帖子 | 最新活动 2026-06-22 19:50:35 CST
5. [Vellum, extended: from identity to reputation on did:ckb](https://talk.nervos.org/t/vellum-extended-from-identity-to-reputation-on-did-ckb/10406) | 1 条近窗帖子 | 最新活动 2026-06-22 13:43:45 CST | tags: CKB, NFT, dapp
6. [Scam DIS](https://talk.nervos.org/t/scam-dis/10412) | 3 条近窗帖子 | 最新活动 2026-06-22 12:16:48 CST
7. [Research Notes: What Zero-Knowledge Proofs Enable on CKB](https://talk.nervos.org/t/research-notes-what-zero-knowledge-proofs-enable-on-ckb/10368) | 1 条近窗帖子 | 最新活动 2026-06-22 12:10:09 CST | tags: CKB-VM, architecture, groth16, sp1, zero-knowledge, zkvm
8. [Liquid Cells: an operator-trustless, pooled micro-payment rollup for CKB, now open source, live on Pudge, and looking for reviewers](https://talk.nervos.org/t/liquid-cells-an-operator-trustless-pooled-micro-payment-rollup-for-ckb-now-open-source-live-on-pudge-and-looking-for-reviewers/10411) | 1 条近窗帖子 | 最新活动 2026-06-22 10:50:19 CST | tags: DIS, layer-2, testnet, zk-rollup
9. [CellScript Website v0 Is Live](https://talk.nervos.org/t/cellscript-website-v0-is-live/10403) | 1 条近窗帖子 | 最新活动 2026-06-22 10:30:16 CST | tags: CellScript

## 最近帖子摘录

- 2026-06-23 00:17:41 CST | IrisNeko | [Spark Program | Nervos Brain - A Global Developer Onboarding Engine and Cross-Language Hub Powered by Agentic RAG](https://talk.nervos.org/t/spark-program-nervos-brain-a-global-developer-onboarding-engine-and-cross-language-hub-powered-by-agentic-rag/9995/41) | Delivery Report This post is the delivery report for: Spark Program | Nervos Brain - A Global Developer Onboarding Engine and Cross-Language Hub Powered by Agentic RAG Nervos...
- 2026-06-22 21:43:07 CST | Jnr6 | [[DIS] Mobile-Ready CKB Light Client (Pocket Node) for Android](https://talk.nervos.org/t/dis-mobile-ready-ckb-light-client-pocket-node-for-android/9879/60) | Title: Pocket Node v1.7.4 is out — sync and Nervos DAO reliability Pocket Node v1.7.4 is live. This one is a reliability release driven almost entirely by your reports here and...
- 2026-06-22 20:22:17 CST | Aki | [[DIS] Luxvoid Protocol: The First Working BTC→CKB→EVM Pipeline — Seeking DAO Support/collab for Production Scaling](https://talk.nervos.org/t/dis-luxvoid-protocol-the-first-working-btc-ckb-evm-pipeline-seeking-dao-support-collab-for-production-scaling/10400/13) | @Ar_Hel — this is exactly the kind of response I was hoping for from this community. A well-structured, engineer-level breakdown that shows you’ve actually read the proposal and...
- 2026-06-22 19:50:35 CST | orange-xc | [Introducing `cobuild-otx-contracts`: A Reference Implementation for CoBuild OTX Contracts](https://talk.nervos.org/t/introducing-cobuild-otx-contracts-a-reference-implementation-for-cobuild-otx-contracts/10413/1) | This repository（ xcshuan/cobuild-otx-contracts） is a working reference implementation and testbed for building CKB contracts around CoBuild and Open Transaction (OTX) workflows....
- 2026-06-22 18:49:42 CST | Ar_Hel | [[DIS] Luxvoid Protocol: The First Working BTC→CKB→EVM Pipeline — Seeking DAO Support/collab for Production Scaling](https://talk.nervos.org/t/dis-luxvoid-protocol-the-first-working-btc-ckb-evm-pipeline-seeking-dao-support-collab-for-production-scaling/10400/12) | roadmap Phase 1: Operational Stability (1-2 months) Goal: Ensure uninterrupted operation of current infrastructure Tasks: Monitoring and alerting Set up Prometheus + Grafana to...
- 2026-06-22 13:43:45 CST | doitian | [Vellum, extended: from identity to reputation on did:ckb](https://talk.nervos.org/t/vellum-extended-from-identity-to-reputation-on-did-ckb/10406/2) | If the claim cell is owned by subjects, where the capacity originates from? It’s interesting design to let subjects destroy claim cells on them. The live cells are...
- 2026-06-22 12:16:48 CST | matt_ckb | [Scam DIS](https://talk.nervos.org/t/scam-dis/10412/3) | 
- 2026-06-22 12:16:02 CST | matt_ckb | [Scam DIS](https://talk.nervos.org/t/scam-dis/10412/2) | The DAO proposals are public, please draw your own conclusions. This type of low effort post won’t be tolerated.
- 2026-06-22 12:10:09 CST | ArthurZhang | [Research Notes: What Zero-Knowledge Proofs Enable on CKB](https://talk.nervos.org/t/research-notes-what-zero-knowledge-proofs-enable-on-ckb/10368/4) | Greate notes. I think you already touch the shape of this through the old-cell / new-cell / witness-proof pattern. I wonder whether there is a useful follow-up around the...
- 2026-06-22 11:28:23 CST | ckbbkc | [Scam DIS](https://talk.nervos.org/t/scam-dis/10412/1) | Do you think CKB is being targeted by scam teams? They’re frantically applying for various DAO proposals to swindle funds from DAOs. Weak public chains often attract scam teams.
- 2026-06-22 10:50:19 CST | T_Silva | [Liquid Cells: an operator-trustless, pooled micro-payment rollup for CKB, now open source, live on Pudge, and looking for reviewers](https://talk.nervos.org/t/liquid-cells-an-operator-trustless-pooled-micro-payment-rollup-for-ckb-now-open-source-live-on-pudge-and-looking-for-reviewers/10411/1) | Hi, We’ve just open-sourced Liquid Cells under MIT, and it’s running live on the Pudge testnet. It’s a small, focused thing: a pooled, operator-trustless micro-payment rollup...
- 2026-06-22 10:30:16 CST | PlasticLove | [CellScript Website v0 Is Live](https://talk.nervos.org/t/cellscript-website-v0-is-live/10403/2) | 期待 cookbook！
