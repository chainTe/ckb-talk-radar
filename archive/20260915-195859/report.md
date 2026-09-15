# Nervos Talk 社区简报

- 统计窗口: 2026-09-15 03:58:59 CST 到 2026-09-16 03:58:59 CST
- 生成时间: 2026-09-16 03:59:06 CST
- 话题数: 4
- 帖子数: 6
- 作者数: 5
- 总结模式: ai:openai-compatible

## 社区总结

## 今日发生了什么

今天论坛主要有一项新提案征集反馈和两个 Spark Program 项目周报 [S01, S03, S06]。SkillPass 项目发帖介绍其在 CKB 上做「可携带服务权益」的开源实验，希望在准备正式 Community Fund DAO 提案前先收集社区意见 [S01]，随后该帖被社区成员移动到 Applications & Ecosystem 分区 [S02]。另一边，Spark Program 的 CKB-VM Sail Validation Sprint 发布 Week 6 更新，明确本周不宣布 PASS [S03]，同时 Fiber RGB++ Swap 宣布完成 Week 4 并覆盖全部范围 [S06]。此外，论坛还新增了一份针对 Fiber 节点的预算提案 [S05]。

## 重点话题

- **SkillPass 征集反馈后被调整分区**：作者介绍 SkillPass 是一个开源的 CKB 上可携带服务权益实验，由提供方以 CKB Capability Cell 形式发放服务权益 [S01]；作者表示希望先拿到反馈，再准备正式的 Community Fund DAO 提案 [S01]。社区成员回帖欢迎并感谢分享，同时认为当前阶段更适合放在 Applications & Ecosystem 分区，并按此移动了帖子 [S02]。

- **Sail Validation Sprint Week 6 不宣布 PASS**：作者说明本周未关闭，因此不宣布 PASS [S03]。已落地的是本地工程与验收基础设施，包括 12 槽聚合器、全部验收器、独立临时 VM 的 clean-room 执行路径、1.80 GB xz 固定输入包的公开发布（哈希已核对）、冻结并推送的候选源码，以及回归测试 [S03]。尚未关闭的是五个依赖外部动作的槽：clean-room 全链完成、CI 下载重放、维护者的交付批准、immutable release 和独立第三方复现 [S03]。作者强调按计划原文要求执行，未通过修改验收定义来制造完成状态 [S03]。

- **Sail 项目作者受伤，可能延迟交付**：该作者在同一话题下补充，本周因右臂肌肉拉伤只能靠左臂作业，进度拖慢了不少，sail verification 可能需要延迟交付 [S04]。

- **Fiber RGB++ Swap 完成 Week 4 并收尾全范围**：作者表示 Week 4 已完成，也即完成全部范围，本周内容是测试、演示和文档 [S06]。测试方面，在本地测试网节点上跑通了完整的两节点流程，包括 hub 发布签名广告、listener 通过 gossip sync 发现广告、best-rate 选择等环节 [S06]。

- **新增 Fiber 节点相关预算提案**：论坛出现一份 [DIS] FNN Safeguard 提案，方向是为 Fiber 节点做恢复验证与升级前资格认定 [S05]。该提案类型为 Budget Proposal，申请人为 Dapps over Apps，申请金额为 8,263,000 CKB 固定金额，约合 9,800 美元，参考换算汇率约为每 CKB 0.001186 美元 [S05]。

## 值得继续跟进

- Sail Validation Sprint 剩下的五个依赖外部动作的槽能否关闭，以及作者受伤是否会实际影响交付时间，这两点目前都还没有结论 [S03, S04]。

- SkillPass 被移动到 Applications & Ecosystem 分区后能收到怎样的社区反馈，以及是否会推进为正式的 Community Fund DAO 提案 [S01, S02]。

- FNN Safeguard 这份预算提案的社区讨论走向，包括 8,263,000 CKB 的申请金额与「恢复验证、升级前资格认定」这一范围是否会引发进一步讨论 [S05]。

## 来源索引

- `S01` [SkillPass: Portable Service Rights on CKB — Looking for Community Feedback](https://talk.nervos.org/t/skillpass-portable-service-rights-on-ckb-looking-for-community-feedback/10706/1) | Dangbaty2004 | 2026-09-15 12:13:12 CST | Hi CKB community, I’m building SkillPass, an open-source experiment for portable service rights on CKB, and I’d like feedback before preparing a formal Community Fund DAO proposal. What is SkillPass? A provider issues a service entitlement as a CKB Capability Cell. The current...
- `S02` [SkillPass: Portable Service Rights on CKB — Looking for Community Feedback](https://talk.nervos.org/t/skillpass-portable-service-rights-on-ckb-looking-for-community-feedback/10706/2) | zz_tovarishch | 2026-09-16 02:46:57 CST | Hi Dangbaty，欢迎加入社区，感谢分享你的项目 虽然这个分享是为后续申请DAO收集反馈，不过当前阶段可能更适合它的地方是 Applications & Ecosystem ，在那个分区可能更适合作为项目本身的讨论 因此，已经将帖子分区移动
- `S03` [Spark Program | CKB-VM Sail Validation Sprint：可复现的 RISC-V 语义差分工具、Lean 4 证明与 Rocq/Coq 兼容性 Spike](https://talk.nervos.org/t/spark-program-ckb-vm-sail-validation-sprint-risc-v-lean-4-rocq-coq-spike/10562/22) | TinyuengKwan | 2026-09-16 01:46:07 CST | Week6 本周未关闭，不宣布 PASS。本地工程与验收基础设施已经完成：12 槽聚合器、全部验收器、独立临时 VM 的 clean-room 执行路径、固定输入包的公开发布（1.80 GB xz，哈希已核对）以及冻结并推送的候选源码，都已落地并有回归测试。尚未关闭的是五个依赖外部动作的槽：clean-room 全链完成、CI 下载重放、维护者的交付批准、immutable release 和独立第三方复现。计划原文要求"未满足的项目按限制发布，不修改验收定义来制造完成状态"，我照此执行。 真实 clean-room 已在全新 KVM...
- `S04` [Spark Program | CKB-VM Sail Validation Sprint：可复现的 RISC-V 语义差分工具、Lean 4 证明与 Rocq/Coq 兼容性 Spike](https://talk.nervos.org/t/spark-program-ckb-vm-sail-validation-sprint-risc-v-lean-4-rocq-coq-spike/10562/23) | TinyuengKwan | 2026-09-16 01:52:55 CST | 同时，我本周由于右臂肌肉拉伤，因此只能靠左臂进行作业，进度拖慢了不少，sail verification可能需要延迟交付。
- `S05` [[DIS] FNN Safeguard — Recovery Verification and Pre-Upgrade Qualification for Fiber Nodes](https://talk.nervos.org/t/dis-fnn-safeguard-recovery-verification-and-pre-upgrade-qualification-for-fiber-nodes/10712/1) | Dappsoverapps | 2026-09-15 22:01:10 CST | Proposal summary Proposal type: Budget Proposal Applicant and project owner: Dapps over Apps Project lead: Abdulkareem Oyeneye Technical lead: Michael Dean Funding requested: 8,263,000 CKB — fixed amount Approximate USD reference: $9,800 Reference conversion: $0.001186 per...
- `S06` [Spark Program | Fiber RGB++ Swap](https://talk.nervos.org/t/spark-program-fiber-rgb-swap/10487/29) | Carl | 2026-09-15 19:46:54 CST | Hi all, Week 4 done, and with it the full scope. Closing update on Fiber RGB++ Swap. What Week 4 was: testing, demo, docs. Testing. Ran the complete two-node flow on local testnet nodes: hub publishes a signed ad, listener discovers it over gossip sync, best-rate picks the...

## 活跃话题

1. [SkillPass: Portable Service Rights on CKB — Looking for Community Feedback](https://talk.nervos.org/t/skillpass-portable-service-rights-on-ckb-looking-for-community-feedback/10706) | 2 条近窗帖子 | 最新活动 2026-09-16 02:46:57 CST | tags: CKB, dapp, fiber, testnet
2. [Spark Program | CKB-VM Sail Validation Sprint：可复现的 RISC-V 语义差分工具、Lean 4 证明与 Rocq/Coq 兼容性 Spike](https://talk.nervos.org/t/spark-program-ckb-vm-sail-validation-sprint-risc-v-lean-4-rocq-coq-spike/10562) | 2 条近窗帖子 | 最新活动 2026-09-16 01:52:55 CST | tags: CKB-VM, In-Progress
3. [[DIS] FNN Safeguard — Recovery Verification and Pre-Upgrade Qualification for Fiber Nodes](https://talk.nervos.org/t/dis-fnn-safeguard-recovery-verification-and-pre-upgrade-qualification-for-fiber-nodes/10712) | 1 条近窗帖子 | 最新活动 2026-09-15 22:01:10 CST
4. [Spark Program | Fiber RGB++ Swap](https://talk.nervos.org/t/spark-program-fiber-rgb-swap/10487) | 1 条近窗帖子 | 最新活动 2026-09-15 19:46:54 CST | tags: In-Progress

## 最近帖子摘录

- 2026-09-16 02:46:57 CST | zz_tovarishch | [SkillPass: Portable Service Rights on CKB — Looking for Community Feedback](https://talk.nervos.org/t/skillpass-portable-service-rights-on-ckb-looking-for-community-feedback/10706/2) | Hi Dangbaty，欢迎加入社区，感谢分享你的项目 虽然这个分享是为后续申请DAO收集反馈，不过当前阶段可能更适合它的地方是 Applications & Ecosystem ，在那个分区可能更适合作为项目本身的讨论 因此，已经将帖子分区移动
- 2026-09-16 01:52:55 CST | TinyuengKwan | [Spark Program | CKB-VM Sail Validation Sprint：可复现的 RISC-V 语义差分工具、Lean 4 证明与 Rocq/Coq 兼容性 Spike](https://talk.nervos.org/t/spark-program-ckb-vm-sail-validation-sprint-risc-v-lean-4-rocq-coq-spike/10562/23) | 同时，我本周由于右臂肌肉拉伤，因此只能靠左臂进行作业，进度拖慢了不少，sail verification可能需要延迟交付。
- 2026-09-16 01:46:07 CST | TinyuengKwan | [Spark Program | CKB-VM Sail Validation Sprint：可复现的 RISC-V 语义差分工具、Lean 4 证明与 Rocq/Coq 兼容性 Spike](https://talk.nervos.org/t/spark-program-ckb-vm-sail-validation-sprint-risc-v-lean-4-rocq-coq-spike/10562/22) | Week6 本周未关闭，不宣布 PASS。本地工程与验收基础设施已经完成：12 槽聚合器、全部验收器、独立临时 VM 的 clean-room 执行路径、固定输入包的公开发布（1.80 GB xz，哈希已核对）以及冻结并推送的候选源码，都已落地并有回归测试。尚未关闭的是五个依赖外部动作的槽：clean-room 全链完成、CI...
- 2026-09-15 22:01:10 CST | Dappsoverapps | [[DIS] FNN Safeguard — Recovery Verification and Pre-Upgrade Qualification for Fiber Nodes](https://talk.nervos.org/t/dis-fnn-safeguard-recovery-verification-and-pre-upgrade-qualification-for-fiber-nodes/10712/1) | Proposal summary Proposal type: Budget Proposal Applicant and project owner: Dapps over Apps Project lead: Abdulkareem Oyeneye Technical lead: Michael Dean Funding requested:...
- 2026-09-15 19:46:54 CST | Carl | [Spark Program | Fiber RGB++ Swap](https://talk.nervos.org/t/spark-program-fiber-rgb-swap/10487/29) | Hi all, Week 4 done, and with it the full scope. Closing update on Fiber RGB++ Swap. What Week 4 was: testing, demo, docs. Testing. Ran the complete two-node flow on local...
- 2026-09-15 12:13:12 CST | Dangbaty2004 | [SkillPass: Portable Service Rights on CKB — Looking for Community Feedback](https://talk.nervos.org/t/skillpass-portable-service-rights-on-ckb-looking-for-community-feedback/10706/1) | Hi CKB community, I’m building SkillPass, an open-source experiment for portable service rights on CKB, and I’d like feedback before preparing a formal Community Fund DAO...
