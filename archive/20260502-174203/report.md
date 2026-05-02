# Nervos Talk 社区简报

- 统计窗口: 2026-05-02 01:42:03 CST 到 2026-05-03 01:42:03 CST
- 生成时间: 2026-05-03 01:42:11 CST
- 话题数: 9
- 帖子数: 14
- 作者数: 6
- 总结模式: ai:openrouter

## 社区总结

## 今日发生了什么

CellScript 作者 ArthurZhang 预告了 0.13.1 补丁计划，重点聚焦本地开发体验和语法治理 [S01]。与此同时，ckb-probe 项目提交了 Week 7 周报，交付了 JSON 全局输出优化和完整的演示说明文档 [S06]。iCKB 合约方面，phroi 发布了新版安全审计报告，并同步整理了 DAO、header、witness 等开发构件，方便 CellScript 团队将其作为成熟度基准进行测试 [S07, S11, S13]。

## 重点话题

- **CellScript 0.13.1 补丁预览**：ArthurZhang 透露下周发布的 0.13.0 将确立"Action Model"（交易提出 Cell 转换、Action 验证转换是否被允许），0.13.1 则聚焦本地人体工程学和语法治理 [S01]。

- **ckb-probe 项目进展**：Clair 发布了覆盖五个核心演示步骤的完整文字报告，所有输出均来自 CKB v0.204.0 测试网节点真实运行数据；同时 Week 7 周报显示 `--json --histogram` 联用输出已统一完成 [S05, S06]。

- **iCKB 合约审计与构件整理**：phroi 发布了截至 2026-05-01 的安全复审报告，包含 Token 通胀等攻击场景的案例追踪；为配合 CellScript 集成，合并了 contracts PR #19，补充了本地可执行审查和重放测试用例 [S07, S08, S11, S13]。

- **CKB PoP 协议修复**：RobaireTH 完成了 ckb-pop 和 ckb-pop-cli 仓库中多个关键漏洞的排查与修复，恢复了此前损坏的核心功能 [S02]。

- **Cellora 索引服务讨论延续**：社区成员 matt_ckb 就区块头验证链路提出追问——在没有 Flyclient 证明的情况下，客户端如何验证 Cellora 返回的区块头确实已被包含在链中 [S10]。

## 值得继续跟进

- CellScript 与 iCKB 的集成进度：ArthurZhang 计划将 iCKB 作为 CellScript 成熟度基准，首批 fixture 就绪后会再次寻求反馈，需观察实际落地节奏 [S09, S12]。

- ckb-probe 的评审与复现：当前文档已可支持评审者直接复制命令复现，但项目仍处于测试网阶段，需关注何时进入主网验证及社区反馈 [S05, S06]。

- Cellora 轻客户端验证方案：matt_ckb 提出的区块头包含性验证问题尚未得到回应，这关系到索引服务的信任模型设计，值得跟踪后续讨论 [S10]。

## 来源索引

- `S01` [CellScript 0.13 Preview: The Action Model and Syntax](https://talk.nervos.org/t/cellscript-0-13-preview-the-action-model-and-syntax/10224/2) | ArthurZhang | 2026-05-02 23:44:55 CST | 0.13.1 Patch Plan Preview Local Ergonomics and Syntax Governance 1. Background CellScript 0.13.0 set to be released next week will establish the new action model: A transaction proposes a Cell transformation. An action verifies whether that transformation is allowed. In this...
- `S02` [Building CKB PoP: a reusable participation primitive on CKB](https://talk.nervos.org/t/building-ckb-pop-a-reusable-participation-primitive-on-ckb/10136/6) | RobaireTH | 2026-05-02 20:43:18 CST | Over the last few days, I have completed a thorough investigation and fix for several critical bugs across the ckb-pop and ckb-pop-cli repositories. I tried to ensure protocol consistency and restore core functionality that was previously broken. Key Bug Fixes & Improvements...
- `S03` [Multi-Model Allocation Guide for Complex Tasks](https://talk.nervos.org/t/multi-model-allocation-guide-for-complex-tasks/10226/1) | zz_tovarishch | 2026-05-02 13:44:50 CST | For routing complex tasks across multiple AI models, I noticed that benchmark-based allocation (HLE, GPQA, IFBench, etc.) only explains part of the story. Each model defaults to a distinct cognitive register when handed the same task. Therefore, have this guide. Claude Opus...
- `S04` [Multi-Model Allocation Guide for Complex Tasks](https://talk.nervos.org/t/multi-model-allocation-guide-for-complex-tasks/10226/2) | ArthurZhang | 2026-05-02 20:34:46 CST | Nice sum-up. One model I would also add to this routing map is GLM 5.1, especially for code review and engineering-risk audit.
- `S05` [Spark Program | Ckb-probe: Deep Observability Tool for CKB Nodes Based on Aya Kernel eBPF/ckb-probe：基于 Aya 内核 eBPF 的 CKB 节点深度可观测性工具](https://talk.nervos.org/t/spark-program-ckb-probe-deep-observability-tool-for-ckb-nodes-based-on-aya-kernel-ebpf-ckb-probe-aya-ebpf-ckb/10008/51) | clair | 2026-05-02 16:17:46 CST | CKB-Probe 演示流程说明 范围：仅限 CKB 测试网 本文档覆盖 ckb-probe 的五个核心演示步骤，每步附完整终端输出、关键命令说明和输出解读。 所有输出均为真实运行数据（2026-05-02，CKB v0.204.0 测试网节点）。 调整说明 本文档替代原计划的演示视频。文字报告在以下方面对评审者更为友好： 评审者可以直接复制报告中的命令进行复现，不需要反复拖动视频进度条 终端输出配合文字解读比视频旁白更容易精确定位到具体的输出字段和数值 报告本身可以作为项目文档的一部分长期保留，便于后续版本更新时同步修改...
- `S06` [Spark Program | Ckb-probe: Deep Observability Tool for CKB Nodes Based on Aya Kernel eBPF/ckb-probe：基于 Aya 内核 eBPF 的 CKB 节点深度可观测性工具](https://talk.nervos.org/t/spark-program-ckb-probe-deep-observability-tool-for-ckb-nodes-based-on-aya-kernel-ebpf-ckb-probe-aya-ebpf-ckb/10008/52) | clair | 2026-05-02 16:19:48 CST | Week 7 周报：JSON 全局输出优化 + 演示说明文档 周期：2026-04-27 ~ 2026-05-03 作者：Clair 项目：ckb-probe — 基于 eBPF 的 CKB 全节点深度可观测性工具 一、本周目标 JSON 全局输出 — 确保所有模式的 JSON 输出格式统一、字段完整 制作完整演示说明文档 — 结构化的文字演示报告（Markdown），覆盖五个演示流程步骤，附完整终端输出和说明 二、完成情况 交付项 状态 说明 JSON --histogram 融合输出 --json --histogram 联用时 JSON 包含...
- `S07` [iCKB Contracts Revisited: Old Code, New Audit](https://talk.nervos.org/t/ickb-contracts-revisited-old-code-new-audit/10225/1) | phroi | 2026-05-02 08:36:46 CST | This post mirrors the original security review report published in ickb/contracts: any question or feedback is more than welcomed Review completion date: 2026-05-01. Reviewed contracts commit: 454cfa9. This is the last commit that changed scripts/contracts/** or...
- `S08` [iCKB Contracts Revisited: Old Code, New Audit](https://talk.nervos.org/t/ickb-contracts-revisited-old-code-new-audit/10225/2) | phroi | 2026-05-02 08:37:05 CST | Appendix: Scenario Analysis The appendix records the case-by-case traces that support the component assessments and the findings summary. Class 1: Token Inflation (minting iCKB without backing) These scenarios test whether iCKB can be created without the corresponding deposit-...
- `S09` [iCKB Contracts Revisited: Old Code, New Audit](https://talk.nervos.org/t/ickb-contracts-revisited-old-code-new-audit/10225/3) | ArthurZhang | 2026-05-02 09:33:02 CST | Great update. This appendix is almost exactly the kind of scenario map I would need before turning iCKB into a CellScript maturity benchmark. The attack-class structure, traces, expected results, and links to concrete tests make it much easier.
- `S10` [Cellora — designing a production indexing and query service for CKB (feedback welcome)](https://talk.nervos.org/t/cellora-designing-a-production-indexing-and-query-service-for-ckb-feedback-welcome/10199/8) | phroi | 2026-05-02 09:21:16 CST | matt_ckb: Without the Flyclient proof, I have trouble seeing how the client can verify that the block header returned from Cellora has been included in the chain. Am I missing something? Even if the returned header is anchored to consensus, there is still the harder question:...
- `S11` [CellScript - A DSL for Cell-Based Contracts](https://talk.nervos.org/t/cellscript-a-dsl-for-cell-based-contracts/10193/18) | phroi | 2026-05-02 08:41:47 CST | Hey Arthur, you are very welcome to try iCKB in CellScript To make that easier, I tightened the iCKB artifacts around the relevant DAO, header, witness, and deployment details: ickb/contracts PR #19: merged. Adds the local executable review plus the expanded scripts/tests...
- `S12` [CellScript - A DSL for Cell-Based Contracts](https://talk.nervos.org/t/cellscript-a-dsl-for-cell-based-contracts/10193/19) | ArthurZhang | 2026-05-02 09:12:37 CST | Hi Phroi, That is very helpful. I will read through these updates before turning this into concrete fixtures. Once I have the first small fixture set ready, I will tag you again for feedback. Really appreciate the help.
- `S13` [[DIS] iCKB & dCKB Rescuer Funding Proposal (Non-Coding Expenses)](https://talk.nervos.org/t/dis-ickb-dckb-rescuer-funding-proposal-non-coding-expenses/8369/28) | phroi | 2026-05-02 08:45:39 CST | Hey all, small update on the iCKB side I cleaned up a few iCKB artifacts around the DAO, headers, witnesses, and deployment notes: ickb/contracts PR #19: merged. Adds the local executable review plus the expanded scripts/tests suites and replay-heavy cases. See also iCKB...
- `S14` [Revamping and Refactoring the CKB Wallet Connection Experience: A Modular Compound Component for React Developers](https://talk.nervos.org/t/revamping-and-refactoring-the-ckb-wallet-connection-experience-a-modular-compound-component-for-react-developers/10221/2) | Ajay | 2026-05-02 03:35:13 CST | This is awesome

## 活跃话题

1. [CellScript 0.13 Preview: The Action Model and Syntax](https://talk.nervos.org/t/cellscript-0-13-preview-the-action-model-and-syntax/10224) | 1 条近窗帖子 | 最新活动 2026-05-02 23:44:55 CST | tags: CKB-VM, CellScript
2. [Building CKB PoP: a reusable participation primitive on CKB](https://talk.nervos.org/t/building-ckb-pop-a-reusable-participation-primitive-on-ckb/10136) | 1 条近窗帖子 | 最新活动 2026-05-02 20:43:18 CST | tags: CKB, NFT, dapp
3. [Multi-Model Allocation Guide for Complex Tasks](https://talk.nervos.org/t/multi-model-allocation-guide-for-complex-tasks/10226) | 2 条近窗帖子 | 最新活动 2026-05-02 20:34:46 CST | tags: AI
4. [Spark Program | Ckb-probe: Deep Observability Tool for CKB Nodes Based on Aya Kernel eBPF/ckb-probe：基于 Aya 内核 eBPF 的 CKB 节点深度可观测性工具](https://talk.nervos.org/t/spark-program-ckb-probe-deep-observability-tool-for-ckb-nodes-based-on-aya-kernel-ebpf-ckb-probe-aya-ebpf-ckb/10008) | 2 条近窗帖子 | 最新活动 2026-05-02 16:19:48 CST | tags: In-Progress, Spark-Program
5. [iCKB Contracts Revisited: Old Code, New Audit](https://talk.nervos.org/t/ickb-contracts-revisited-old-code-new-audit/10225) | 3 条近窗帖子 | 最新活动 2026-05-02 09:33:02 CST
6. [Cellora — designing a production indexing and query service for CKB (feedback welcome)](https://talk.nervos.org/t/cellora-designing-a-production-indexing-and-query-service-for-ckb-feedback-welcome/10199) | 1 条近窗帖子 | 最新活动 2026-05-02 09:21:16 CST | tags: CKB, Nervos-项目动态, dapp, testnet
7. [CellScript - A DSL for Cell-Based Contracts](https://talk.nervos.org/t/cellscript-a-dsl-for-cell-based-contracts/10193) | 2 条近窗帖子 | 最新活动 2026-05-02 09:12:37 CST | tags: CKB-VM, CellScript, DSL
8. [[DIS] iCKB & dCKB Rescuer Funding Proposal (Non-Coding Expenses)](https://talk.nervos.org/t/dis-ickb-dckb-rescuer-funding-proposal-non-coding-expenses/8369) | 1 条近窗帖子 | 最新活动 2026-05-02 08:45:39 CST
9. [Revamping and Refactoring the CKB Wallet Connection Experience: A Modular Compound Component for React Developers](https://talk.nervos.org/t/revamping-and-refactoring-the-ckb-wallet-connection-experience-a-modular-compound-component-for-react-developers/10221) | 1 条近窗帖子 | 最新活动 2026-05-02 03:35:13 CST | tags: CKB, wallet

## 最近帖子摘录

- 2026-05-02 23:44:55 CST | ArthurZhang | [CellScript 0.13 Preview: The Action Model and Syntax](https://talk.nervos.org/t/cellscript-0-13-preview-the-action-model-and-syntax/10224/2) | 0.13.1 Patch Plan Preview Local Ergonomics and Syntax Governance 1. Background CellScript 0.13.0 set to be released next week will establish the new action model: A transaction...
- 2026-05-02 20:43:18 CST | RobaireTH | [Building CKB PoP: a reusable participation primitive on CKB](https://talk.nervos.org/t/building-ckb-pop-a-reusable-participation-primitive-on-ckb/10136/6) | Over the last few days, I have completed a thorough investigation and fix for several critical bugs across the ckb-pop and ckb-pop-cli repositories. I tried to ensure protocol...
- 2026-05-02 20:34:46 CST | ArthurZhang | [Multi-Model Allocation Guide for Complex Tasks](https://talk.nervos.org/t/multi-model-allocation-guide-for-complex-tasks/10226/2) | Nice sum-up. One model I would also add to this routing map is GLM 5.1, especially for code review and engineering-risk audit.
- 2026-05-02 16:19:48 CST | clair | [Spark Program | Ckb-probe: Deep Observability Tool for CKB Nodes Based on Aya Kernel eBPF/ckb-probe：基于 Aya 内核 eBPF 的 CKB 节点深度可观测性工具](https://talk.nervos.org/t/spark-program-ckb-probe-deep-observability-tool-for-ckb-nodes-based-on-aya-kernel-ebpf-ckb-probe-aya-ebpf-ckb/10008/52) | Week 7 周报：JSON 全局输出优化 + 演示说明文档 周期：2026-04-27 ~ 2026-05-03 作者：Clair 项目：ckb-probe — 基于 eBPF 的 CKB 全节点深度可观测性工具 一、本周目标 JSON 全局输出 — 确保所有模式的 JSON 输出格式统一、字段完整 制作完整演示说明文档 —...
- 2026-05-02 16:17:46 CST | clair | [Spark Program | Ckb-probe: Deep Observability Tool for CKB Nodes Based on Aya Kernel eBPF/ckb-probe：基于 Aya 内核 eBPF 的 CKB 节点深度可观测性工具](https://talk.nervos.org/t/spark-program-ckb-probe-deep-observability-tool-for-ckb-nodes-based-on-aya-kernel-ebpf-ckb-probe-aya-ebpf-ckb/10008/51) | CKB-Probe 演示流程说明 范围：仅限 CKB 测试网 本文档覆盖 ckb-probe 的五个核心演示步骤，每步附完整终端输出、关键命令说明和输出解读。 所有输出均为真实运行数据（2026-05-02，CKB v0.204.0 测试网节点）。 调整说明 本文档替代原计划的演示视频。文字报告在以下方面对评审者更为友好：...
- 2026-05-02 13:44:50 CST | zz_tovarishch | [Multi-Model Allocation Guide for Complex Tasks](https://talk.nervos.org/t/multi-model-allocation-guide-for-complex-tasks/10226/1) | For routing complex tasks across multiple AI models, I noticed that benchmark-based allocation (HLE, GPQA, IFBench, etc.) only explains part of the story. Each model defaults to...
- 2026-05-02 09:33:02 CST | ArthurZhang | [iCKB Contracts Revisited: Old Code, New Audit](https://talk.nervos.org/t/ickb-contracts-revisited-old-code-new-audit/10225/3) | Great update. This appendix is almost exactly the kind of scenario map I would need before turning iCKB into a CellScript maturity benchmark. The attack-class structure, traces,...
- 2026-05-02 09:21:16 CST | phroi | [Cellora — designing a production indexing and query service for CKB (feedback welcome)](https://talk.nervos.org/t/cellora-designing-a-production-indexing-and-query-service-for-ckb-feedback-welcome/10199/8) | matt_ckb: Without the Flyclient proof, I have trouble seeing how the client can verify that the block header returned from Cellora has been included in the chain. Am I missing...
- 2026-05-02 09:12:37 CST | ArthurZhang | [CellScript - A DSL for Cell-Based Contracts](https://talk.nervos.org/t/cellscript-a-dsl-for-cell-based-contracts/10193/19) | Hi Phroi, That is very helpful. I will read through these updates before turning this into concrete fixtures. Once I have the first small fixture set ready, I will tag you again...
- 2026-05-02 08:45:39 CST | phroi | [[DIS] iCKB & dCKB Rescuer Funding Proposal (Non-Coding Expenses)](https://talk.nervos.org/t/dis-ickb-dckb-rescuer-funding-proposal-non-coding-expenses/8369/28) | Hey all, small update on the iCKB side I cleaned up a few iCKB artifacts around the DAO, headers, witnesses, and deployment notes: ickb/contracts PR #19: merged. Adds the local...
- 2026-05-02 08:41:47 CST | phroi | [CellScript - A DSL for Cell-Based Contracts](https://talk.nervos.org/t/cellscript-a-dsl-for-cell-based-contracts/10193/18) | Hey Arthur, you are very welcome to try iCKB in CellScript To make that easier, I tightened the iCKB artifacts around the relevant DAO, header, witness, and deployment details:...
- 2026-05-02 08:37:05 CST | phroi | [iCKB Contracts Revisited: Old Code, New Audit](https://talk.nervos.org/t/ickb-contracts-revisited-old-code-new-audit/10225/2) | Appendix: Scenario Analysis The appendix records the case-by-case traces that support the component assessments and the findings summary. Class 1: Token Inflation (minting iCKB...
- 2026-05-02 08:36:46 CST | phroi | [iCKB Contracts Revisited: Old Code, New Audit](https://talk.nervos.org/t/ickb-contracts-revisited-old-code-new-audit/10225/1) | This post mirrors the original security review report published in ickb/contracts: any question or feedback is more than welcomed Review completion date: 2026-05-01. Reviewed...
- 2026-05-02 03:35:13 CST | Ajay | [Revamping and Refactoring the CKB Wallet Connection Experience: A Modular Compound Component for React Developers](https://talk.nervos.org/t/revamping-and-refactoring-the-ckb-wallet-connection-experience-a-modular-compound-component-for-react-developers/10221/2) | This is awesome
