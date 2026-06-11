# Nervos Talk 社区简报

- 统计窗口: 2026-06-11 03:35:03 CST 到 2026-06-12 03:35:03 CST
- 生成时间: 2026-06-12 03:35:09 CST
- 话题数: 12
- 帖子数: 13
- 作者数: 11
- 总结模式: ai:openrouter

## 社区总结

## 今日发生了什么

Antismart 在论坛公开了一份设计草案，计划基于 RFC 44/45 实现 CKB 状态在其他链（优先 EVM）上的验证机制，目前仍处于设计阶段尚未编码。[S01] 同时，mohanson 连续发布了两篇 CKB-VM 快照技术的深度技术文章，从 V1 架构原理讲到 V2 的演进优化。[S10, S11] 此外，ArthurZhang 预告已在 CKB devnet 上跑通了一条基于 Cell 模型的通道工厂（channel factory）实现，周末前将分享更多细节。[S13]

## 重点话题

- **CKB 跨链状态验证设计公开征求意见**：Antismart 提出了一套基于轻客户端头链（SPV header chain）和 DSPV 简化模型的低成本验证方案，目标是在 EVM 链上以约 170-870k gas 验证 CKB 状态，目前放出了完整设计文档、威胁模型和分阶段计划，呼吁社区在设计早期挑错。[S01]

- **CKB-VM 快照技术双连更**：mohanson 罕见地连续发布两篇深度技术文章，先系统梳理了 V1 快照"全页拷贝"的简单正确但开销大的设计哲学，再展开 V2 如何通过差异追踪和细粒度拷贝解决实际性能瓶颈，对节点开发者理解 CKB 脚本执行优化有直接参考价值。[S11, S10]

- **Cell 模型通道工厂取得 devnet 突破**：ArthurZhang 基于此前"Morph Channel"讨论方向，宣布已在 CKB devnet 上完成 channel factory 的实现路径验证，相关 thesis 和形式化验证的初步工作将在周末前放出，这可能为 CKB 的 Layer 2 通道扩容方案提供新的工程范式。[S13]

- **Fiber 桌面端重建提案正式通过**：zz_tovarishch 公布投票结果，fnn desktop app 的 ground-up rebuild 提案以 100% 赞成率、总计 65,057,521 CKB 投票权重通过，且已完成链上后验核查。[S06]

- **Spark 项目申请继续推进**：DWSQUIRES 就 Tiko 创作者商业验证项目发布了更新版提案，回应了委员会的前期反馈，同时另开新帖详细说明了验证冲刺（Validation Sprint）的具体规划。[S04, S05]

## 值得继续跟进

- **跨链验证方案的实际 gas 成本与安全性**：Antismart 的设计虽给出了初步估算，但 EVM 侧合约尚未实现，实际部署时的 gas 波动和 DSPV 假设在复杂攻击场景下的鲁棒性仍需具体代码和审计验证。[S01]

- **Fiber 桌面端重建的执行透明度**：提案已通过，但 v1 的交付时间表、功能范围和与现有 fnn 协议的兼容性细节尚未披露，需要观察后续开发进度是否与提案承诺一致。[S06]

- **ArthurZhang 的通道工厂工程细节**：目前仅有 devnet 验证的定性宣告，缺少吞吐量数据、资本效率参数及与 Fiber Network 的潜在协作或竞争关系说明，周末发布的 thesis 将是关键评估材料。[S13]

## 来源索引

- `S01` [Design notes: verifying CKB state inside other chains (EVM-first, built on RFC 44/45)](https://talk.nervos.org/t/design-notes-verifying-ckb-state-inside-other-chains-evm-first-built-on-rfc-44-45/10372/1) | Antismart | 2026-06-12 02:05:13 CST | Gm everyone! I want to share a design I’ve been working on and have it picked apart before any code gets written. The cheapest time to be wrong is now. NOTE: This is design-stage. Nothing is built. Full design doc with threat model, cost estimates and a phased plan is here:...
- `S02` [[DIS] Mobile-Ready CKB Light Client (Pocket Node) for Android](https://talk.nervos.org/t/dis-mobile-ready-ckb-light-client-pocket-node-for-android/9879/54) | knmo | 2026-06-12 00:14:30 CST | Jnr6: What changed After the last update, A text field appears: “Secure Wallet - To unlock encrypt your wallet keys” It took me several attempts to realize that you have to enter your screen lock password. It would be helpful to have a prompt indicating that a pop-up for the...
- `S03` [[DIS] Mobile-Ready CKB Light Client (Pocket Node) for Android](https://talk.nervos.org/t/dis-mobile-ready-ckb-light-client-pocket-node-for-android/9879/55) | Jnr6 | 2026-06-12 01:27:34 CST | i thought i added this @knmo guess i forgot
- `S04` [Spark Program | Tiko Creator Commerce Expansion + Private Beta Validation](https://talk.nervos.org/t/spark-program-tiko-creator-commerce-expansion-private-beta-validation/10231/7) | DWSQUIRES | 2026-06-11 22:50:45 CST | Thanks for the feedback from the Committee, I came up with an updated proposal as per the feedback. Find it here
- `S05` [Spark Program | Tiko Creator Commerce Validation Sprint](https://talk.nervos.org/t/spark-program-tiko-creator-commerce-validation-sprint/10370/1) | DWSQUIRES | 2026-06-11 22:48:25 CST | Project Name Tiko Creator Commerce Validation Sprint Team / Individual Bio and Contact Project: Tiko Type: CKB-based ticketing and creator commerce prototype Lead: Indie Developer Contact: Discord - @getigeti21 GitHub: GitHub - Tiko-T/Tiko · GitHub Live demo: https://tiko-...
- `S06` [[DIS] Fiber Desktop v1 ground-up rebuild and launch — fnn desktop app](https://talk.nervos.org/t/dis-fiber-desktop-v1-ground-up-rebuild-and-launch-fnn-desktop-app/10317/13) | zz_tovarishch | 2026-06-11 20:59:43 CST | Based on the Metaforo tally at close, the outcome is PASSED. Approval is 100% with total voting weight 65,057,521 CKB. Post-close verification has been completed using CKB DAO Watchdog, together with a manual sanity check. The verification cross-checks Metaforo-recorded voting...
- `S07` [From Hand-Rolled Channels to a Single Fiber SDK Call: Rebuilding "Chat-and-Pay" with Fiber Network](https://talk.nervos.org/t/from-hand-rolled-channels-to-a-single-fiber-sdk-call-rebuilding-chat-and-pay-with-fiber-network/10369/1) | Sonny | 2026-06-11 17:47:35 CST | From Hand-Rolled Channels to a Single SDK Call: Rebuilding “Chat-and-Pay” with Fiber Network If you read my previous “Chat-and-Pay” article, you might remember that I hand-rolled a Spillman unidirectional payment channel from scratch on CKB L1 — writing my own multisig...
- `S08` [Research Notes: What Zero-Knowledge Proofs Enable on CKB](https://talk.nervos.org/t/research-notes-what-zero-knowledge-proofs-enable-on-ckb/10368/1) | Mulandi_Cecilia | 2026-06-11 17:07:53 CST | Gm! I am opening this topic to share my findings as I do some zk research on CKB and explore what is possible and also contribute to existing projects. This is Note 01 in my ongoing research. What I Think Is Possible and Why the Architecture Makes It Tractable NOTE: These are...
- `S09` [[DIS] Rypto — CKB Content & Advocacy Campaign](https://talk.nervos.org/t/dis-rypto-ckb-content-advocacy-campaign/10364/3) | Eyeam | 2026-06-11 16:38:42 CST | No brainer for me. Voted yes. We need people talking about Nervos and you make quite a few videos for CKB already, you’ve even turned up to two community meet ups in Barcelona and Malaga so I dont question your level of commitment to the cause.
- `S10` [Deep Dive into CKB-VM Snapshot V2: Evolution](https://talk.nervos.org/t/deep-dive-into-ckb-vm-snapshot-v2-evolution/10367/1) | mohanson | 2026-06-11 13:55:57 CST | Background In Deep Dive into CKB-VM Snapshot V1: Architecture and Design Principles, we introduced the earliest snapshot approach in CKB-VM: copy every dirty page in full and serialize it together with registers and PC. This approach is correct and simple, but in real...
- `S11` [Deep Dive into CKB-VM Snapshot V1: Architecture and Design Principles](https://talk.nervos.org/t/deep-dive-into-ckb-vm-snapshot-v1-architecture-and-design-principles/10366/1) | mohanson | 2026-06-11 13:50:24 CST | Background After receiving a new transaction, a CKB node must execute its scripts to validate it. A script is a user-provided Turing-complete program, and the compute cost of one execution can vary a lot: a simple signature check may need only a few million cycles, while a...
- `S12` [为 AI 时代的开发者重建文档：CCC 文档站的建设实录(1)](https://talk.nervos.org/t/ai-ccc-1/10365/1) | yixiu.ckbfans.bit | 2026-06-11 13:48:41 CST | 引言 这篇文章是此前发布的《当 84% 的开发者都在用 AI Coding，CKB 开发者体验的下一步怎么走？（附完整调研与路线图）》的延续。上篇报告揭示了 CKB 生态在 AI 可发现性上的系统性缺口，核心问题之一是：CCC 文档匮乏，导致 AI 工具在回答 CKB 相关问题时难以获取准确信息。 本文记录了过去一个多月以来，我们从零建设 docs.ckbccc.com 的完整过程——包括选型决策、内容迭代、DeepWiki 辅助 review 的经验与教训、35 个文档页面的编写和汉化工作流，以及 GA 埋点基础设施的准备。...
- `S13` [Morph Channel：一种 CKB Cell 模型下的通道 / 工厂讨论方向](https://talk.nervos.org/t/morph-channel-ckb-cell/10241/5) | ArthurZhang | 2026-06-11 10:18:11 CST | 简单更新一下，也先抱歉一下，确实有点收不住兴奋。 基于这个帖子的想法，我现在似乎已经在 CKB 上跑通了一条 channel factory 的实现路径，并且通过了严格的 devnet 验收门槛。 周末前我大概率会分享更多内容，也会一起放出一篇我一直在写的 thesis，里面会解释具体机制，以及一些初步的形式化验证工作。 等正式发出来后，也很期待听到大家的意见。 image1732×867 142 KB

## 活跃话题

1. [Design notes: verifying CKB state inside other chains (EVM-first, built on RFC 44/45)](https://talk.nervos.org/t/design-notes-verifying-ckb-state-inside-other-chains-evm-first-built-on-rfc-44-45/10372) | 1 条近窗帖子 | 最新活动 2026-06-12 02:05:13 CST | tags: CKB
2. [[DIS] Mobile-Ready CKB Light Client (Pocket Node) for Android](https://talk.nervos.org/t/dis-mobile-ready-ckb-light-client-pocket-node-for-android/9879) | 2 条近窗帖子 | 最新活动 2026-06-12 01:27:34 CST | tags: CKB, light-client
3. [Spark Program | Tiko Creator Commerce Expansion + Private Beta Validation](https://talk.nervos.org/t/spark-program-tiko-creator-commerce-expansion-private-beta-validation/10231) | 1 条近窗帖子 | 最新活动 2026-06-11 22:50:45 CST | tags: Rejection, Spark-Program
4. [Spark Program | Tiko Creator Commerce Validation Sprint](https://talk.nervos.org/t/spark-program-tiko-creator-commerce-validation-sprint/10370) | 1 条近窗帖子 | 最新活动 2026-06-11 22:48:25 CST | tags: Spark-Program
5. [[DIS] Fiber Desktop v1 ground-up rebuild and launch — fnn desktop app](https://talk.nervos.org/t/dis-fiber-desktop-v1-ground-up-rebuild-and-launch-fnn-desktop-app/10317) | 1 条近窗帖子 | 最新活动 2026-06-11 20:59:43 CST | tags: fiber
6. [From Hand-Rolled Channels to a Single Fiber SDK Call: Rebuilding "Chat-and-Pay" with Fiber Network](https://talk.nervos.org/t/from-hand-rolled-channels-to-a-single-fiber-sdk-call-rebuilding-chat-and-pay-with-fiber-network/10369) | 1 条近窗帖子 | 最新活动 2026-06-11 17:47:35 CST | tags: CKB, dapp
7. [Research Notes: What Zero-Knowledge Proofs Enable on CKB](https://talk.nervos.org/t/research-notes-what-zero-knowledge-proofs-enable-on-ckb/10368) | 1 条近窗帖子 | 最新活动 2026-06-11 17:07:53 CST | tags: CKB-VM, architecture, groth16, sp1, zero-knowledge, zkvm
8. [[DIS] Rypto — CKB Content & Advocacy Campaign](https://talk.nervos.org/t/dis-rypto-ckb-content-advocacy-campaign/10364) | 1 条近窗帖子 | 最新活动 2026-06-11 16:38:42 CST
9. [Deep Dive into CKB-VM Snapshot V2: Evolution](https://talk.nervos.org/t/deep-dive-into-ckb-vm-snapshot-v2-evolution/10367) | 1 条近窗帖子 | 最新活动 2026-06-11 13:55:57 CST | tags: CKB-VM
10. [Deep Dive into CKB-VM Snapshot V1: Architecture and Design Principles](https://talk.nervos.org/t/deep-dive-into-ckb-vm-snapshot-v1-architecture-and-design-principles/10366) | 1 条近窗帖子 | 最新活动 2026-06-11 13:50:24 CST | tags: CKB-VM
11. [为 AI 时代的开发者重建文档：CCC 文档站的建设实录(1)](https://talk.nervos.org/t/ai-ccc-1/10365) | 1 条近窗帖子 | 最新活动 2026-06-11 13:48:41 CST
12. [Morph Channel：一种 CKB Cell 模型下的通道 / 工厂讨论方向](https://talk.nervos.org/t/morph-channel-ckb-cell/10241) | 1 条近窗帖子 | 最新活动 2026-06-11 10:18:11 CST

## 最近帖子摘录

- 2026-06-12 02:05:13 CST | Antismart | [Design notes: verifying CKB state inside other chains (EVM-first, built on RFC 44/45)](https://talk.nervos.org/t/design-notes-verifying-ckb-state-inside-other-chains-evm-first-built-on-rfc-44-45/10372/1) | Gm everyone! I want to share a design I’ve been working on and have it picked apart before any code gets written. The cheapest time to be wrong is now. NOTE: This is design-...
- 2026-06-12 01:27:34 CST | Jnr6 | [[DIS] Mobile-Ready CKB Light Client (Pocket Node) for Android](https://talk.nervos.org/t/dis-mobile-ready-ckb-light-client-pocket-node-for-android/9879/55) | i thought i added this @knmo guess i forgot
- 2026-06-12 00:14:30 CST | knmo | [[DIS] Mobile-Ready CKB Light Client (Pocket Node) for Android](https://talk.nervos.org/t/dis-mobile-ready-ckb-light-client-pocket-node-for-android/9879/54) | Jnr6: What changed After the last update, A text field appears: “Secure Wallet - To unlock encrypt your wallet keys” It took me several attempts to realize that you have to...
- 2026-06-11 22:50:45 CST | DWSQUIRES | [Spark Program | Tiko Creator Commerce Expansion + Private Beta Validation](https://talk.nervos.org/t/spark-program-tiko-creator-commerce-expansion-private-beta-validation/10231/7) | Thanks for the feedback from the Committee, I came up with an updated proposal as per the feedback. Find it here
- 2026-06-11 22:48:25 CST | DWSQUIRES | [Spark Program | Tiko Creator Commerce Validation Sprint](https://talk.nervos.org/t/spark-program-tiko-creator-commerce-validation-sprint/10370/1) | Project Name Tiko Creator Commerce Validation Sprint Team / Individual Bio and Contact Project: Tiko Type: CKB-based ticketing and creator commerce prototype Lead: Indie...
- 2026-06-11 20:59:43 CST | zz_tovarishch | [[DIS] Fiber Desktop v1 ground-up rebuild and launch — fnn desktop app](https://talk.nervos.org/t/dis-fiber-desktop-v1-ground-up-rebuild-and-launch-fnn-desktop-app/10317/13) | Based on the Metaforo tally at close, the outcome is PASSED. Approval is 100% with total voting weight 65,057,521 CKB. Post-close verification has been completed using CKB DAO...
- 2026-06-11 17:47:35 CST | Sonny | [From Hand-Rolled Channels to a Single Fiber SDK Call: Rebuilding "Chat-and-Pay" with Fiber Network](https://talk.nervos.org/t/from-hand-rolled-channels-to-a-single-fiber-sdk-call-rebuilding-chat-and-pay-with-fiber-network/10369/1) | From Hand-Rolled Channels to a Single SDK Call: Rebuilding “Chat-and-Pay” with Fiber Network If you read my previous “Chat-and-Pay” article, you might remember that I hand-...
- 2026-06-11 17:07:53 CST | Mulandi_Cecilia | [Research Notes: What Zero-Knowledge Proofs Enable on CKB](https://talk.nervos.org/t/research-notes-what-zero-knowledge-proofs-enable-on-ckb/10368/1) | Gm! I am opening this topic to share my findings as I do some zk research on CKB and explore what is possible and also contribute to existing projects. This is Note 01 in my...
- 2026-06-11 16:38:42 CST | Eyeam | [[DIS] Rypto — CKB Content & Advocacy Campaign](https://talk.nervos.org/t/dis-rypto-ckb-content-advocacy-campaign/10364/3) | No brainer for me. Voted yes. We need people talking about Nervos and you make quite a few videos for CKB already, you’ve even turned up to two community meet ups in Barcelona...
- 2026-06-11 13:55:57 CST | mohanson | [Deep Dive into CKB-VM Snapshot V2: Evolution](https://talk.nervos.org/t/deep-dive-into-ckb-vm-snapshot-v2-evolution/10367/1) | Background In Deep Dive into CKB-VM Snapshot V1: Architecture and Design Principles, we introduced the earliest snapshot approach in CKB-VM: copy every dirty page in full and...
- 2026-06-11 13:50:24 CST | mohanson | [Deep Dive into CKB-VM Snapshot V1: Architecture and Design Principles](https://talk.nervos.org/t/deep-dive-into-ckb-vm-snapshot-v1-architecture-and-design-principles/10366/1) | Background After receiving a new transaction, a CKB node must execute its scripts to validate it. A script is a user-provided Turing-complete program, and the compute cost of...
- 2026-06-11 13:48:41 CST | yixiu.ckbfans.bit | [为 AI 时代的开发者重建文档：CCC 文档站的建设实录(1)](https://talk.nervos.org/t/ai-ccc-1/10365/1) | 引言 这篇文章是此前发布的《当 84% 的开发者都在用 AI Coding，CKB 开发者体验的下一步怎么走？（附完整调研与路线图）》的延续。上篇报告揭示了 CKB 生态在 AI 可发现性上的系统性缺口，核心问题之一是：CCC 文档匮乏，导致 AI 工具在回答 CKB 相关问题时难以获取准确信息。 本文记录了过去一个多月以来，我们从零建设...
- 2026-06-11 10:18:11 CST | ArthurZhang | [Morph Channel：一种 CKB Cell 模型下的通道 / 工厂讨论方向](https://talk.nervos.org/t/morph-channel-ckb-cell/10241/5) | 简单更新一下，也先抱歉一下，确实有点收不住兴奋。 基于这个帖子的想法，我现在似乎已经在 CKB 上跑通了一条 channel factory 的实现路径，并且通过了严格的 devnet 验收门槛。 周末前我大概率会分享更多内容，也会一起放出一篇我一直在写的 thesis，里面会解释具体机制，以及一些初步的形式化验证工作。...
