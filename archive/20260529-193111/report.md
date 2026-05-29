# Nervos Talk 社区简报

- 统计窗口: 2026-05-29 03:31:11 CST 到 2026-05-30 03:31:11 CST
- 生成时间: 2026-05-30 03:31:21 CST
- 话题数: 10
- 帖子数: 15
- 作者数: 11
- 总结模式: ai:openrouter

## 社区总结

## 今日发生了什么

今天 Nervos Talk 论坛以星火计划（Spark Program）项目进展为主轴，既有新工具上线申请，也有已结项项目的收尾与后续资金追问 [S03, S04, S05]。Fiber 生态相关的技术讨论和科普内容也持续有更新 [S01, S07, S08, S10]。

## 重点话题

- **ckb-probe 正式结项并追问长期维护经费**：基于 eBPF 的 CKB 节点深度可观测工具 ckb-probe 已完成 8 周开发并提交结项报告，开发者 clair 向星火计划委员会询问结项后能否继续申请 DAO 经费以维持长期维护 [S03, S04]。

- **Cell Sandbox 新提交申请**：开发者 zynorr 提交了一款面向 CKB Cell 模型的可视化交互学习工具，旨在帮助用户直观理解 Cell 模型的工作原理，目前处于星火计划委员会前期审阅阶段 [S05, S06]。

- **UGMP 项目被指出方向偏离**：委员会反馈 UGMP（通用 Spore/DOB 无感铸造基础设施）目前交付物偏向开发者教程，尚未形成面向终端用户的完整产品，要求项目方明确核心定位 [S11]。

- **CKB Action Links 草案继续讨论**：作者 truthixify 在与 Fiber 的对比中进一步澄清了 Action URL 的"无状态、发后即忘"特性，强调其与 Fiber 双向会话的本质区别 [S01]。

- **Fiber 基础设施定位再被强调**：社区成员 Lawliet_Chan 提出 Fiber 是"proof of buying"共识机制在 L2 出块间隙小于 L1 时的必备基础设施，另一成员 Ckroamer 则指出 Fiber 并非统一账本，各通道与 CKB 保持相对独立关系 [S07, S08]。

## 值得继续跟进

- **星火计划结项项目的可持续资金机制**：多个项目集中进入结项或验收阶段，ckb-probe 提出的"结项后长期维护经费如何申请"问题，可能代表一批早期 Grant 项目共同面临的后续运营资金缺口 [S04]。

- **新提交工具项目的委员会评审结果**：Cell Sandbox 刚进入审阅流程，其教育定位与星火计划偏产品/基础设施的支持方向是否匹配，有待委员会正式反馈 [S05, S06]。

- **UGMP 的路径选择**：项目方需在"开发者教育"与"产品化落地"之间做出明确抉择，这将直接影响后续资源投入与社区预期 [S11]。

## 来源索引

- `S01` [CKB Action Links: a draft protocol for shareable CKB transaction URLs](https://talk.nervos.org/t/ckb-action-links-a-draft-protocol-for-shareable-ckb-transaction-urls/10315/3) | truthixify | 2026-05-30 00:38:25 CST | Fiber: agreed, and you put the split better than I had. An Action URL is fire-and-forget to a peer the publisher never learns the identity of, while Fiber is a live session between two peers who already share a channel. Cramming that into a stateless URL means smuggling...
- `S02` [A New Chapter for CKB: Introducing the Common Knowledge Base Association](https://talk.nervos.org/t/a-new-chapter-for-ckb-introducing-the-common-knowledge-base-association/10249/10) | NightLantern | 2026-05-29 23:42:12 CST | Hello there, I was curious how long the application for contributing members takes to process? I applied a few weeks ago. Also I was a bit confused trying to find the “Contribution Document” I had listed my contributions but I didnt fill out a specific document. I’m wondering...
- `S03` [Spark Program | Ckb-probe: Deep Observability Tool for CKB Nodes Based on Aya Kernel eBPF/ckb-probe：基于 Aya 内核 eBPF 的 CKB 节点深度可观测性工具](https://talk.nervos.org/t/spark-program-ckb-probe-deep-observability-tool-for-ckb-nodes-based-on-aya-kernel-ebpf-ckb-probe-aya-ebpf-ckb/10008/61) | xingtianchunyan | 2026-05-29 12:51:59 CST | Spark Program｜ckb-probe – 结项报告 1. 结项评价 / / Final Evaluation 完成日期 / Completion Date： 2026年5月13日 评价摘要 / Evaluation Summary： ckb-probe 是基于 aya-rs 实现的一个用于实时监控 CKB 节点性能和行为的工具，利用 eBPF 技术（uprobe/kprobe/tracepoint）以非侵入式方式捕获和分析 CKB 节点的函数调用。项目在 8 周内（2026-03-23 ~...
- `S04` [Spark Program | Ckb-probe: Deep Observability Tool for CKB Nodes Based on Aya Kernel eBPF/ckb-probe：基于 Aya 内核 eBPF 的 CKB 节点深度可观测性工具](https://talk.nervos.org/t/spark-program-ckb-probe-deep-observability-tool-for-ckb-nodes-based-on-aya-kernel-ebpf-ckb-probe-aya-ebpf-ckb/10008/62) | clair | 2026-05-29 21:24:18 CST | 感谢星火计划委员会对 ckb-probe 项目的支持、评审和结项认可。 这个项目能在 8 周内完成核心交付，离不开委员会在申请、Pending、执行和验收各阶段的指导，尤其是对项目范围收敛、验收标准明确化、可复现验证环境等方面的要求，这些建议也让项目最终交付质量更扎实。 ckb-probe 目前已经完成 v0.1.0 / v0.1.1 的核心版本交付，后续我也希望继续维护并逐步推进更多功能，同时也想进一步请教委员会：如果我希望在结项后继续长期维护 ckb-probe，是否能继续向DAO申请经费？ 再次感谢星火计划委员会、CKB-VM...
- `S05` [Spark Program | Cell Sandbox — A Visual Playground for the CKB Cell Model](https://talk.nervos.org/t/spark-program-cell-sandbox-a-visual-playground-for-the-ckb-cell-model/10326/1) | zynor | 2026-05-29 17:07:11 CST | Project Name Cell Sandbox — A Visual Playground for the CKB Cell Model Team / Individual Profile and Contact Information Name: zynorr Role: Sole developer and maintainer Background: Full-stack engineer with deep experience in TypeScript, React, Next.js, and the CKB ecosystem....
- `S06` [Spark Program | Cell Sandbox — A Visual Playground for the CKB Cell Model](https://talk.nervos.org/t/spark-program-cell-sandbox-a-visual-playground-for-the-ckb-cell-model/10326/2) | zz_tovarishch | 2026-05-29 18:52:48 CST | Hey Zynor, welcome to the CKB ecosystem, and thanks for your interest in Spark! A few personal thoughts before this goes to the committee meeting. These are my own read, not the committee’s position. I went through the repo and the live build, I genuinely like it. A few things...
- `S07` [[Fiber] 比特币闪电网络的生态应用解析](https://talk.nervos.org/t/fiber/10320/4) | Lawliet_Chan | 2026-05-29 10:51:51 CST | 增加一个场景，我认为fiber是 proof of buying共识（https://talk.nervos.org/t/proof-of-buying-layer1-layer2/9752）必备的基础设施工具，尤其是在L2的出块间隙< CKB L1 出块间隙的时候
- `S08` [[Fiber] 比特币闪电网络的生态应用解析](https://talk.nervos.org/t/fiber/10320/5) | Ckroamer | 2026-05-29 13:56:08 CST | Fiber 严格意义上来说不是区块链，每个零散的通道都与 CKB 有相对独立的关系，并不是一个统一账本形式的关系
- `S09` [[Fiber] 比特币闪电网络的生态应用解析](https://talk.nervos.org/t/fiber/10320/6) | 123nervos | 2026-05-29 18:07:28 CST | Thanks. I cannot code unfortunately. Who could start formalising a proposal of integration ?
- `S10` [Fiber Storybook: Explaining Fiber Through Pico’s Airport Journey](https://talk.nervos.org/t/fiber-storybook-explaining-fiber-through-pico-s-airport-journey/10251/7) | yuqi | 2026-05-29 13:13:21 CST | Hi Yeti, thank you for your feedback! Yeti: the orange channel distribution boxes also need to be updated as the CKB is moving, so Pico’s Channel Total depletes at the same rate as the Pico CKB (995.7) while the Fiber Pass Total always stays at 5000CKB, showing that the CKB is...
- `S11` [Spark Program | CKB-UGMP —— A Universal Spore/DOB Seamless Minting Infrastructure Prototype on CKB —— 基于 CKB 的通用 Spore/DOB 无感铸造基础设施原型](https://talk.nervos.org/t/spark-program-ckb-ugmp-a-universal-spore-dob-seamless-minting-infrastructure-prototype-on-ckb-ckb-spore-dob/10098/25) | xingtianchunyan | 2026-05-29 12:57:25 CST | Hi @HNO3Miracle ， 感谢提交UGMP项目的阶段性成果。委员会在审阅后，有以下几点意见供您参考： 首先，目前的交付内容更偏向于面向开发者与新手的功能演示与教程，重点展示了储存方式、可选择协议等技术实现细节，尚未形成面向终端用户的完整产品形态。这意味着目前的成果与最初的设计方向存在一定区别。委员会非常愿意协助您厘清接下来的发展路径——究竟是深耕教程与开发者教育，还是转向完整的产品化落地。建议您明确核心定位，集中资源推进，避免在两条路径之间分散精力。...
- `S12` [[DIS] Fiber Desktop v1 ground-up rebuild and launch — fnn desktop app](https://talk.nervos.org/t/dis-fiber-desktop-v1-ground-up-rebuild-and-launch-fnn-desktop-app/10317/8) | zz_tovarishch | 2026-05-29 11:10:37 CST | Hi Chukwuma, Here’s what I can share in my capacity as coordinator. Some earlier proposals have used USD-equivalent wording in their text, and the community voted with that wording visible. For reference, the DAO v1.0 Execution Stage rule states: CKB Community Fund DAO Rules...
- `S13` [[DIS] Decentralized privacy order-book appchain based on CKB L1 - 2026.phase-1](https://talk.nervos.org/t/dis-decentralized-privacy-order-book-appchain-based-on-ckb-l1-2026-phase-1/10015/29) | Lawliet_Chan | 2026-05-29 10:55:10 CST | milestone.2 已完成 代码仓库： https://github.com/invisibook-lab/invisibook 检验方式： invisibook/docs/milestones/test_guide_2.md at main · invisibook-lab/invisibook · GitHub 如果发现任何bug，欢迎给我们提issue
- `S14` [Spark Program | Dular](https://talk.nervos.org/t/spark-program-dular/10212/10) | duongja | 2026-05-29 03:33:00 CST | Hello, Find the detailed Milestone 1 Report in the google docs Milestone 1 Report
- `S15` [Spark Program | Dular](https://talk.nervos.org/t/spark-program-dular/10212/11) | zz_tovarishch | 2026-05-29 09:00:37 CST | Hi Duongja, 谷歌文档没有开放权限 另外，为了方便社区更容易跟进项目的进度，建议直接在Nervos Talk上发布（就像其他项目那样，主要内容直接发布，代码部分用github, 必要的外部内容可以使用跳转的链接）

## 活跃话题

1. [CKB Action Links: a draft protocol for shareable CKB transaction URLs](https://talk.nervos.org/t/ckb-action-links-a-draft-protocol-for-shareable-ckb-transaction-urls/10315) | 1 条近窗帖子 | 最新活动 2026-05-30 00:38:25 CST | tags: CKB, dapp
2. [A New Chapter for CKB: Introducing the Common Knowledge Base Association](https://talk.nervos.org/t/a-new-chapter-for-ckb-introducing-the-common-knowledge-base-association/10249) | 1 条近窗帖子 | 最新活动 2026-05-29 23:42:12 CST | tags: CKB
3. [Spark Program | Ckb-probe: Deep Observability Tool for CKB Nodes Based on Aya Kernel eBPF/ckb-probe：基于 Aya 内核 eBPF 的 CKB 节点深度可观测性工具](https://talk.nervos.org/t/spark-program-ckb-probe-deep-observability-tool-for-ckb-nodes-based-on-aya-kernel-ebpf-ckb-probe-aya-ebpf-ckb/10008) | 2 条近窗帖子 | 最新活动 2026-05-29 21:24:18 CST | tags: Completion, Spark-Program
4. [Spark Program | Cell Sandbox — A Visual Playground for the CKB Cell Model](https://talk.nervos.org/t/spark-program-cell-sandbox-a-visual-playground-for-the-ckb-cell-model/10326) | 2 条近窗帖子 | 最新活动 2026-05-29 18:52:48 CST | tags: Spark-Program, Submitted
5. [[Fiber] 比特币闪电网络的生态应用解析](https://talk.nervos.org/t/fiber/10320) | 3 条近窗帖子 | 最新活动 2026-05-29 18:07:28 CST
6. [Fiber Storybook: Explaining Fiber Through Pico’s Airport Journey](https://talk.nervos.org/t/fiber-storybook-explaining-fiber-through-pico-s-airport-journey/10251) | 1 条近窗帖子 | 最新活动 2026-05-29 13:13:21 CST | tags: fiber
7. [Spark Program | CKB-UGMP —— A Universal Spore/DOB Seamless Minting Infrastructure Prototype on CKB —— 基于 CKB 的通用 Spore/DOB 无感铸造基础设施原型](https://talk.nervos.org/t/spark-program-ckb-ugmp-a-universal-spore-dob-seamless-minting-infrastructure-prototype-on-ckb-ckb-spore-dob/10098) | 1 条近窗帖子 | 最新活动 2026-05-29 12:57:25 CST | tags: In-Progress, Spark-Program
8. [[DIS] Fiber Desktop v1 ground-up rebuild and launch — fnn desktop app](https://talk.nervos.org/t/dis-fiber-desktop-v1-ground-up-rebuild-and-launch-fnn-desktop-app/10317) | 1 条近窗帖子 | 最新活动 2026-05-29 11:10:37 CST | tags: fiber
9. [[DIS] Decentralized privacy order-book appchain based on CKB L1 - 2026.phase-1](https://talk.nervos.org/t/dis-decentralized-privacy-order-book-appchain-based-on-ckb-l1-2026-phase-1/10015) | 1 条近窗帖子 | 最新活动 2026-05-29 10:55:10 CST | tags: appchain
10. [Spark Program | Dular](https://talk.nervos.org/t/spark-program-dular/10212) | 2 条近窗帖子 | 最新活动 2026-05-29 09:00:37 CST | tags: In-Progress, Spark-Program

## 最近帖子摘录

- 2026-05-30 00:38:25 CST | truthixify | [CKB Action Links: a draft protocol for shareable CKB transaction URLs](https://talk.nervos.org/t/ckb-action-links-a-draft-protocol-for-shareable-ckb-transaction-urls/10315/3) | Fiber: agreed, and you put the split better than I had. An Action URL is fire-and-forget to a peer the publisher never learns the identity of, while Fiber is a live session...
- 2026-05-29 23:42:12 CST | NightLantern | [A New Chapter for CKB: Introducing the Common Knowledge Base Association](https://talk.nervos.org/t/a-new-chapter-for-ckb-introducing-the-common-knowledge-base-association/10249/10) | Hello there, I was curious how long the application for contributing members takes to process? I applied a few weeks ago. Also I was a bit confused trying to find the...
- 2026-05-29 21:24:18 CST | clair | [Spark Program | Ckb-probe: Deep Observability Tool for CKB Nodes Based on Aya Kernel eBPF/ckb-probe：基于 Aya 内核 eBPF 的 CKB 节点深度可观测性工具](https://talk.nervos.org/t/spark-program-ckb-probe-deep-observability-tool-for-ckb-nodes-based-on-aya-kernel-ebpf-ckb-probe-aya-ebpf-ckb/10008/62) | 感谢星火计划委员会对 ckb-probe 项目的支持、评审和结项认可。 这个项目能在 8 周内完成核心交付，离不开委员会在申请、Pending、执行和验收各阶段的指导，尤其是对项目范围收敛、验收标准明确化、可复现验证环境等方面的要求，这些建议也让项目最终交付质量更扎实。 ckb-probe 目前已经完成 v0.1.0 / v0.1.1...
- 2026-05-29 18:52:48 CST | zz_tovarishch | [Spark Program | Cell Sandbox — A Visual Playground for the CKB Cell Model](https://talk.nervos.org/t/spark-program-cell-sandbox-a-visual-playground-for-the-ckb-cell-model/10326/2) | Hey Zynor, welcome to the CKB ecosystem, and thanks for your interest in Spark! A few personal thoughts before this goes to the committee meeting. These are my own read, not the...
- 2026-05-29 18:07:28 CST | 123nervos | [[Fiber] 比特币闪电网络的生态应用解析](https://talk.nervos.org/t/fiber/10320/6) | Thanks. I cannot code unfortunately. Who could start formalising a proposal of integration ?
- 2026-05-29 17:07:11 CST | zynor | [Spark Program | Cell Sandbox — A Visual Playground for the CKB Cell Model](https://talk.nervos.org/t/spark-program-cell-sandbox-a-visual-playground-for-the-ckb-cell-model/10326/1) | Project Name Cell Sandbox — A Visual Playground for the CKB Cell Model Team / Individual Profile and Contact Information Name: zynorr Role: Sole developer and maintainer...
- 2026-05-29 13:56:08 CST | Ckroamer | [[Fiber] 比特币闪电网络的生态应用解析](https://talk.nervos.org/t/fiber/10320/5) | Fiber 严格意义上来说不是区块链，每个零散的通道都与 CKB 有相对独立的关系，并不是一个统一账本形式的关系
- 2026-05-29 13:13:21 CST | yuqi | [Fiber Storybook: Explaining Fiber Through Pico’s Airport Journey](https://talk.nervos.org/t/fiber-storybook-explaining-fiber-through-pico-s-airport-journey/10251/7) | Hi Yeti, thank you for your feedback! Yeti: the orange channel distribution boxes also need to be updated as the CKB is moving, so Pico’s Channel Total depletes at the same rate...
- 2026-05-29 12:57:25 CST | xingtianchunyan | [Spark Program | CKB-UGMP —— A Universal Spore/DOB Seamless Minting Infrastructure Prototype on CKB —— 基于 CKB 的通用 Spore/DOB 无感铸造基础设施原型](https://talk.nervos.org/t/spark-program-ckb-ugmp-a-universal-spore-dob-seamless-minting-infrastructure-prototype-on-ckb-ckb-spore-dob/10098/25) | Hi @HNO3Miracle ， 感谢提交UGMP项目的阶段性成果。委员会在审阅后，有以下几点意见供您参考：...
- 2026-05-29 12:51:59 CST | xingtianchunyan | [Spark Program | Ckb-probe: Deep Observability Tool for CKB Nodes Based on Aya Kernel eBPF/ckb-probe：基于 Aya 内核 eBPF 的 CKB 节点深度可观测性工具](https://talk.nervos.org/t/spark-program-ckb-probe-deep-observability-tool-for-ckb-nodes-based-on-aya-kernel-ebpf-ckb-probe-aya-ebpf-ckb/10008/61) | Spark Program｜ckb-probe – 结项报告 1. 结项评价 / / Final Evaluation 完成日期 / Completion Date： 2026年5月13日 评价摘要 / Evaluation Summary： ckb-probe 是基于 aya-rs 实现的一个用于实时监控 CKB 节点性能和行为的工具，利用 eBPF...
- 2026-05-29 11:10:37 CST | zz_tovarishch | [[DIS] Fiber Desktop v1 ground-up rebuild and launch — fnn desktop app](https://talk.nervos.org/t/dis-fiber-desktop-v1-ground-up-rebuild-and-launch-fnn-desktop-app/10317/8) | Hi Chukwuma, Here’s what I can share in my capacity as coordinator. Some earlier proposals have used USD-equivalent wording in their text, and the community voted with that...
- 2026-05-29 10:55:10 CST | Lawliet_Chan | [[DIS] Decentralized privacy order-book appchain based on CKB L1 - 2026.phase-1](https://talk.nervos.org/t/dis-decentralized-privacy-order-book-appchain-based-on-ckb-l1-2026-phase-1/10015/29) | milestone.2 已完成 代码仓库： https://github.com/invisibook-lab/invisibook 检验方式： invisibook/docs/milestones/test_guide_2.md at main · invisibook-lab/invisibook · GitHub...
- 2026-05-29 10:51:51 CST | Lawliet_Chan | [[Fiber] 比特币闪电网络的生态应用解析](https://talk.nervos.org/t/fiber/10320/4) | 增加一个场景，我认为fiber是 proof of buying共识（https://talk.nervos.org/t/proof-of-buying-layer1-layer2/9752）必备的基础设施工具，尤其是在L2的出块间隙< CKB L1 出块间隙的时候
- 2026-05-29 09:00:37 CST | zz_tovarishch | [Spark Program | Dular](https://talk.nervos.org/t/spark-program-dular/10212/11) | Hi Duongja, 谷歌文档没有开放权限 另外，为了方便社区更容易跟进项目的进度，建议直接在Nervos Talk上发布（就像其他项目那样，主要内容直接发布，代码部分用github, 必要的外部内容可以使用跳转的链接）
- 2026-05-29 03:33:00 CST | duongja | [Spark Program | Dular](https://talk.nervos.org/t/spark-program-dular/10212/10) | Hello, Find the detailed Milestone 1 Report in the google docs Milestone 1 Report
