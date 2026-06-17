# Nervos Talk 社区简报

- 统计窗口: 2026-06-17 03:24:15 CST 到 2026-06-18 03:24:15 CST
- 生成时间: 2026-06-18 03:24:24 CST
- 话题数: 8
- 帖子数: 13
- 作者数: 8
- 总结模式: ai:openrouter

## 社区总结

## 今日发生了什么

社区今天延续了 NDAO 国库资金销毁提案的密集讨论，knmo 与 matt_ckb 就反稀释机制与代币经济模型边界展开交锋 [S05, S06, S07, S08]。同时，Spark Program 多个项目迎来节点性进展：Dular 完成前两期里程碑付款 [S11]，Cell Sandbox 和 ckb-probe 分别进入委员会审核与社区推广阶段 [S10, S09]。此外，开发者 mohanson 发布了一篇关于 CKB-VM 内存模型 W^X 设计的深度技术文章 [S12]。

## 重点话题

- **NDAO 销毁提案陷入代币经济学核心争议**：knmo 提出将早期销毁资金通过智能合约重新分配给 DAO 锁仓者以抵消通胀 [S07]，matt_ckb 反驳称这会突破定位白皮书描述的代币经济模型，复杂度不合理，并强调销毁本身已惠及全体持有者 [S08]。双方对"发行计划作为 CKB 三大不变量之一"的理解出现分歧 [S06, S07]。

- **Spark Program 三项目同步推进**：Dular 公开了里程碑 1/2 的链上付款交易，合计 431,800 CKB [S11]；Cell Sandbox 因 UI/UX 问题被委员会定为 Pending，但认可其在 I/O Cell 可视化、钱包连接扩展等方向的改进 [S10]；ckb-probe 作者 clair 表示将加入运营者群组并持续维护项目 [S09]。

- **PactAgent 优化移动端体验**：Ajay 分享了 UI 重设计后的移动端跟进更新，承认桌面端增强后移动体验仍需补足 [S01]。

- **CKB-VM 内存模型技术深潜**：mohanson 发文详解 W^X（写执行分离）设计，补全了此前快照系列中仅提及未展开的三类页面标志位（FLAG_DIRTY/FLAG_EXECUTABLE/FLAG_WRITABLE）的实现机制 [S12]。

- **链上游戏设计回溯**：xxuejie 在讨论中提及，当前 CKB 链游采用的"单争议块"设计并非新创，而是源自 jjy 在 godwoken/polyjuice 时期的思路——用单笔 CKB 交易运行 EVM 替代二分法 [S13]。

## 值得继续跟进

- **NDAO 提案的妥协空间**：matt_ckb 明确反对调整反稀释机制 [S08]，knmo 是否会退守至更轻量的方案（如纯销毁而不重分配）[S05]，或寻求社区更广泛支持，将决定该提案走向。

- **Cell Sandbox 的 UI/UX 整改周期**：委员会 Pending 状态通常意味着需要实质性修订 [S10]，关注作者 zynor 能否在交互层面给出令委员会满意的迭代。

- **ckb-probe 的节点运营者采纳度**：项目进入"让运行者了解和体验"的阶段 [S09]，实际部署反馈将检验 eBPF 方案在 CKB 节点监控场景的价值。

## 来源索引

- `S01` [PactAgent Developer Update: UI Redesign, DAO/Bounty Workflow Focus, and Agreement Operations Improvements](https://talk.nervos.org/t/pactagent-developer-update-ui-redesign-dao-bounty-workflow-focus-and-agreement-operations-improvements/10352/2) | Ajay | 2026-06-18 01:05:55 CST | Hi everyone, I’d like to share a smaller follow-up update on PactAgent, focused mainly on the latest mobile view improvements. After the previous UI redesign, I noticed that the desktop experience was becoming much stronger, but the mobile experience still needed more...
- `S02` [Spark Program | “Atlantik” Community Full Node](https://talk.nervos.org/t/spark-program-atlantik-community-full-node/10390/5) | xingtianchunyan | 2026-06-18 00:10:45 CST | Hi @knmo， 很高兴看到你对 Spark Program 感兴趣！以下是我在提交委员会审核前的一些个人看法，供你参考。这些是我的阅读感受，不代表委员会立场。 目前你的帖子内容让我难以判断这是否是一个正式的提案——缺少很多委员会评审所需的关键信息（团队简介、技术方案、执行计划、如何验证等）。 如果你愿意继续推进的话，我们刚刚更新了提案模板，欢迎你按照模板对当前帖子内容进行整理和优化。模板中对每个章节应该包含什么内容都有详细说明，可以帮助你更清晰、更完整地表达项目设计。 整理完成后 @我，我会尽快推进预审流程，并争取早日将提案递交委员会。...
- `S03` [NDAO-0000 burn unused treasury funds](https://talk.nervos.org/t/ndao-0000-burn-unused-treasury-funds/9626/12) | knmo | 2026-06-17 03:36:51 CST | Brilliant suggestion. For proposals that have been approved, use one or more cells—for example, in the case of installment payments. This also allows for flexibility in the event of delays, but it requires frequent interaction in a sensitive area. Regarding the DAO’s...
- `S04` [NDAO-0000 burn unused treasury funds](https://talk.nervos.org/t/ndao-0000-burn-unused-treasury-funds/9626/13) | matt_ckb | 2026-06-17 04:18:37 CST | knmo: So, with a full distribution/activation of the fund issuance, would DAO investors receive a correspondingly higher percentage for their fixed investment? DAO depositors’ rates would remain the same, you can refer to the “burned” proportion here, it is this portion of the...
- `S05` [NDAO-0000 burn unused treasury funds](https://talk.nervos.org/t/ndao-0000-burn-unused-treasury-funds/9626/14) | knmo | 2026-06-17 06:58:09 CST | In that case, we would need to adjust the anti‑dilution so that the percentage of anti-inflationary depositor compensation increases accordingly as soon as the burning is converted to a distribution.
- `S06` [NDAO-0000 burn unused treasury funds](https://talk.nervos.org/t/ndao-0000-burn-unused-treasury-funds/9626/15) | matt_ckb | 2026-06-17 09:24:46 CST | secondary issuance is described in this section of the positioning paper github.com/nervosnetwork/rfcs rfcs/0001-positioning/0001-positioning.md master --- Number: "0001" Category: Informational Status: Final Author: The Nervos Team Created: 2019-09-12 --- # The Nervos Network...
- `S07` [NDAO-0000 burn unused treasury funds](https://talk.nervos.org/t/ndao-0000-burn-unused-treasury-funds/9626/16) | knmo | 2026-06-17 16:39:18 CST | matt_ckb: issuance schedule as one of the 3 invariants of CKB So it would be a smart contract that ensures that a portion of the NDAO distribution—which was burned in the early years—is distributed to DAO-lockers for Offsetting Inflation. Depending on the burn conditions, this...
- `S08` [NDAO-0000 burn unused treasury funds](https://talk.nervos.org/t/ndao-0000-burn-unused-treasury-funds/9626/17) | matt_ckb | 2026-06-17 22:44:25 CST | Unfortunately the complexity of doing this is unreasonable and it changes the existing tokenomics beyond what was described in the positioning paper. Burning the CKB benefits all CKB holders, including DAO depositors.
- `S09` [Spark Program | Ckb-probe: Deep Observability Tool for CKB Nodes Based on Aya Kernel eBPF/ckb-probe：基于 Aya 内核 eBPF 的 CKB 节点深度可观测性工具](https://talk.nervos.org/t/spark-program-ckb-probe-deep-observability-tool-for-ckb-nodes-based-on-aya-kernel-ebpf-ckb-probe-aya-ebpf-ckb/10008/64) | clair | 2026-06-17 20:55:20 CST | 感谢您的详细回复和建议。 我后续会尝试加入群组，与节点运行者和社区成员进行沟通，让大家进一步了解和体验 CKB probe 项目。同时我也会在后续的一段时间内继续维护该项目，进一步完善该项目。
- `S10` [Spark Program | Cell Sandbox — A Visual Playground for the CKB Cell Model](https://talk.nervos.org/t/spark-program-cell-sandbox-a-visual-playground-for-the-ckb-cell-model/10326/8) | xingtianchunyan | 2026-06-17 20:46:56 CST | Hi @zynor， 感谢你对 Spark Program 的持续关注和对 Cell Sandbox 的修订。 经 Spark Program 委员会审核，你的提案当前状态定为 Pending。 委员会认可 Cell Sandbox 的创新潜力，同时也注意到你在修订中对功能部分做了实质性改进：补充了 input/output Cell 显示支持、计划集成 @ckb-ccc/connector-react 扩展钱包连接选项、以及使用指南的放置规划——这些方向都是对的。 但此次修订中，UI/UX...
- `S11` [Spark Program | Dular](https://talk.nervos.org/t/spark-program-dular/10212/18) | zz_tovarishch | 2026-06-17 15:59:59 CST | Payment for milestone 1/2 https://explorer.nervos.org/en/transaction/0x40fa021f0c8c3fe735051e419c24f5c88985d191ee9c363cb662919e465620ee 281800+150000 = 431,800ckb
- `S12` [Deep Dive into CKB-VM Memory Model: Design of W^X](https://talk.nervos.org/t/deep-dive-into-ckb-vm-memory-model-design-of-w-x/10398/1) | mohanson | 2026-06-17 13:35:59 CST | In the previous article, we explored CKB-VM snapshots v1 and snapshots v2. One of the core tasks of snapshotting is marking and saving “dirty pages.” That article repeatedly mentioned page flag markers: FLAG_DIRTY, FLAG_EXECUTABLE, FLAG_WRITABLE but never explained where these...
- `S13` [Trying on-chain games on CKB](https://talk.nervos.org/t/trying-on-chain-games-on-ckb/10395/3) | xxuejie | 2026-06-17 07:48:18 CST | Protocol In theory, you are correct, the one dispute chunk could potentially be a generic design. In fact it was not a new one, I remembered hearing it first from @jjy when working on godwoken / polyjuice, where instead of bisecting, we use one CKB transaction to run EVM and...

## 活跃话题

1. [PactAgent Developer Update: UI Redesign, DAO/Bounty Workflow Focus, and Agreement Operations Improvements](https://talk.nervos.org/t/pactagent-developer-update-ui-redesign-dao-bounty-workflow-focus-and-agreement-operations-improvements/10352) | 1 条近窗帖子 | 最新活动 2026-06-18 01:05:55 CST | tags: CKB, CKB-VM, dapp
2. [Spark Program | “Atlantik” Community Full Node](https://talk.nervos.org/t/spark-program-atlantik-community-full-node/10390) | 1 条近窗帖子 | 最新活动 2026-06-18 00:10:45 CST | tags: Nervos-Network, Node, Spark-Program, bootnode
3. [NDAO-0000 burn unused treasury funds](https://talk.nervos.org/t/ndao-0000-burn-unused-treasury-funds/9626) | 6 条近窗帖子 | 最新活动 2026-06-17 22:44:25 CST
4. [Spark Program | Ckb-probe: Deep Observability Tool for CKB Nodes Based on Aya Kernel eBPF/ckb-probe：基于 Aya 内核 eBPF 的 CKB 节点深度可观测性工具](https://talk.nervos.org/t/spark-program-ckb-probe-deep-observability-tool-for-ckb-nodes-based-on-aya-kernel-ebpf-ckb-probe-aya-ebpf-ckb/10008) | 1 条近窗帖子 | 最新活动 2026-06-17 20:55:20 CST | tags: Completion, Spark-Program
5. [Spark Program | Cell Sandbox — A Visual Playground for the CKB Cell Model](https://talk.nervos.org/t/spark-program-cell-sandbox-a-visual-playground-for-the-ckb-cell-model/10326) | 1 条近窗帖子 | 最新活动 2026-06-17 20:46:56 CST | tags: Spark-Program, Submitted
6. [Spark Program | Dular](https://talk.nervos.org/t/spark-program-dular/10212) | 1 条近窗帖子 | 最新活动 2026-06-17 15:59:59 CST | tags: In-Progress, Spark-Program
7. [Deep Dive into CKB-VM Memory Model: Design of W^X](https://talk.nervos.org/t/deep-dive-into-ckb-vm-memory-model-design-of-w-x/10398) | 1 条近窗帖子 | 最新活动 2026-06-17 13:35:59 CST | tags: CKB-VM
8. [Trying on-chain games on CKB](https://talk.nervos.org/t/trying-on-chain-games-on-ckb/10395) | 1 条近窗帖子 | 最新活动 2026-06-17 07:48:18 CST

## 最近帖子摘录

- 2026-06-18 01:05:55 CST | Ajay | [PactAgent Developer Update: UI Redesign, DAO/Bounty Workflow Focus, and Agreement Operations Improvements](https://talk.nervos.org/t/pactagent-developer-update-ui-redesign-dao-bounty-workflow-focus-and-agreement-operations-improvements/10352/2) | Hi everyone, I’d like to share a smaller follow-up update on PactAgent, focused mainly on the latest mobile view improvements. After the previous UI redesign, I noticed that the...
- 2026-06-18 00:10:45 CST | xingtianchunyan | [Spark Program | “Atlantik” Community Full Node](https://talk.nervos.org/t/spark-program-atlantik-community-full-node/10390/5) | Hi @knmo， 很高兴看到你对 Spark Program 感兴趣！以下是我在提交委员会审核前的一些个人看法，供你参考。这些是我的阅读感受，不代表委员会立场。 目前你的帖子内容让我难以判断这是否是一个正式的提案——缺少很多委员会评审所需的关键信息（团队简介、技术方案、执行计划、如何验证等）。...
- 2026-06-17 22:44:25 CST | matt_ckb | [NDAO-0000 burn unused treasury funds](https://talk.nervos.org/t/ndao-0000-burn-unused-treasury-funds/9626/17) | Unfortunately the complexity of doing this is unreasonable and it changes the existing tokenomics beyond what was described in the positioning paper. Burning the CKB benefits...
- 2026-06-17 20:55:20 CST | clair | [Spark Program | Ckb-probe: Deep Observability Tool for CKB Nodes Based on Aya Kernel eBPF/ckb-probe：基于 Aya 内核 eBPF 的 CKB 节点深度可观测性工具](https://talk.nervos.org/t/spark-program-ckb-probe-deep-observability-tool-for-ckb-nodes-based-on-aya-kernel-ebpf-ckb-probe-aya-ebpf-ckb/10008/64) | 感谢您的详细回复和建议。 我后续会尝试加入群组，与节点运行者和社区成员进行沟通，让大家进一步了解和体验 CKB probe 项目。同时我也会在后续的一段时间内继续维护该项目，进一步完善该项目。
- 2026-06-17 20:46:56 CST | xingtianchunyan | [Spark Program | Cell Sandbox — A Visual Playground for the CKB Cell Model](https://talk.nervos.org/t/spark-program-cell-sandbox-a-visual-playground-for-the-ckb-cell-model/10326/8) | Hi @zynor， 感谢你对 Spark Program 的持续关注和对 Cell Sandbox 的修订。 经 Spark Program 委员会审核，你的提案当前状态定为 Pending。 委员会认可 Cell Sandbox 的创新潜力，同时也注意到你在修订中对功能部分做了实质性改进：补充了 input/output Cell...
- 2026-06-17 16:39:18 CST | knmo | [NDAO-0000 burn unused treasury funds](https://talk.nervos.org/t/ndao-0000-burn-unused-treasury-funds/9626/16) | matt_ckb: issuance schedule as one of the 3 invariants of CKB So it would be a smart contract that ensures that a portion of the NDAO distribution—which was burned in the early...
- 2026-06-17 15:59:59 CST | zz_tovarishch | [Spark Program | Dular](https://talk.nervos.org/t/spark-program-dular/10212/18) | Payment for milestone 1/2 https://explorer.nervos.org/en/transaction/0x40fa021f0c8c3fe735051e419c24f5c88985d191ee9c363cb662919e465620ee 281800+150000 = 431,800ckb
- 2026-06-17 13:35:59 CST | mohanson | [Deep Dive into CKB-VM Memory Model: Design of W^X](https://talk.nervos.org/t/deep-dive-into-ckb-vm-memory-model-design-of-w-x/10398/1) | In the previous article, we explored CKB-VM snapshots v1 and snapshots v2. One of the core tasks of snapshotting is marking and saving “dirty pages.” That article repeatedly...
- 2026-06-17 09:24:46 CST | matt_ckb | [NDAO-0000 burn unused treasury funds](https://talk.nervos.org/t/ndao-0000-burn-unused-treasury-funds/9626/15) | secondary issuance is described in this section of the positioning paper github.com/nervosnetwork/rfcs rfcs/0001-positioning/0001-positioning.md master --- Number: "0001"...
- 2026-06-17 07:48:18 CST | xxuejie | [Trying on-chain games on CKB](https://talk.nervos.org/t/trying-on-chain-games-on-ckb/10395/3) | Protocol In theory, you are correct, the one dispute chunk could potentially be a generic design. In fact it was not a new one, I remembered hearing it first from @jjy when...
- 2026-06-17 06:58:09 CST | knmo | [NDAO-0000 burn unused treasury funds](https://talk.nervos.org/t/ndao-0000-burn-unused-treasury-funds/9626/14) | In that case, we would need to adjust the anti‑dilution so that the percentage of anti-inflationary depositor compensation increases accordingly as soon as the burning is...
- 2026-06-17 04:18:37 CST | matt_ckb | [NDAO-0000 burn unused treasury funds](https://talk.nervos.org/t/ndao-0000-burn-unused-treasury-funds/9626/13) | knmo: So, with a full distribution/activation of the fund issuance, would DAO investors receive a correspondingly higher percentage for their fixed investment? DAO depositors’...
- 2026-06-17 03:36:51 CST | knmo | [NDAO-0000 burn unused treasury funds](https://talk.nervos.org/t/ndao-0000-burn-unused-treasury-funds/9626/12) | Brilliant suggestion. For proposals that have been approved, use one or more cells—for example, in the case of installment payments. This also allows for flexibility in the...
