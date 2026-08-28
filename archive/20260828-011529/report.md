# Nervos Talk 社区简报

- 统计窗口: 2026-08-27 09:15:29 CST 到 2026-08-28 09:15:29 CST
- 生成时间: 2026-08-28 09:15:36 CST
- 话题数: 7
- 帖子数: 12
- 作者数: 6
- 总结模式: ai:openai-compatible

## 社区总结

## 今日发生了什么

过去 24 小时，Nervos Talk 的主要动态来自 Spark Program 的密集推进：Tranfr 可编程恢复提案和 NNCBN 社区启动节点提案都被标记为 Pending，FiberTap 打赏项目则被拒绝 [S02, S11, S12]。另一条重要消息是 Vellum 的 did:ckb 声誉扩展 V2 提案正式进入社区投票阶段 [S01]。CKB-VM 验证冲刺项目也更新了第三周进展，开发者与委员会之间还有一段关于更新节奏的友好互动 [S05, S06, S07]。整体来看，论坛没有出现争议性大事件，更多是提案流程和项目跟进的常规推进 [S01, S02, S11, S12]。

## 重点话题

- **Vellum V2 提案进入投票阶段**：项目方宣布 Vellum 的 did:ckb 声誉扩展 V2 提案已在 metaforo 开放投票，并贴出了 dao.ckb.community 的投票链接，标志着该项目从讨论阶段迈向社区决策阶段 [S01]。

- **Spark 委员会批量处理三个提案**：Tranfr（CKB 可编程恢复）与 NNCBN（社区启动节点）均获得 Pending 状态，委员会明确“这不是拒绝” [S02, S11]。Tranfr 的作者随后表示已根据反馈更新了修订版 [S03]。FiberTap 微打赏项目则被拒绝，委员会表示会公开解释拒绝理由 [S12]。

- **CKB-VM Sail 冲刺第三周工作已提交**：本周进展集中在 RVFI-DII 差分验证，包括加固启动流程以防端口竞争和过期会话、引入强制 mutation matrix、为 32 个 ADD/ADDI/BEQ 测试用例提供可重复回放产物，并在每个 PR 上执行差分验证 [S05]。开发者就周报拖延向委员会道歉，委员会则回应“身体健康最重要，不必抱歉” [S06, S07]。

- **Fiber RGB++ Swap 首次进展更新逾期**：委员会发帖指出该项目尚未提交第一次进展更新，正在询问最新进展，同时表达了关心 [S08]。

- **Polycrpt 状态通道定位的讨论**：社区成员澄清 PolyCrypt 并非 CKB 专属团队，而是一直在做多链通用状态通道框架，申请 Nervos grant 时也已同时涉足 Cardano，CKB 相关仓库今年持续更新 [S09]。另一位成员由此确认状态通道并非 CKB 独有 [S10]。

## 值得继续跟进

- **Tranfr 修订版提交后的走向**：提案目前处于 Pending，作者已根据委员会反馈更新了修订版，接下来委员会会如何评估、是否会转为正式接受，值得留意 [S02, S03]。

- **CKB-VM Sail 项目能否恢复稳定周报**：委员会已经注意到更新间隔变长并主动询问，开发者承认是作息不规律导致、承诺改进 [S04, S05, S06]。后续协作节奏是否稳定，值得观察 [S04, S05, S06, S07]。

- **Fiber RGB++ Swap 的首次进展何时提交**：委员会已明确提醒该项目缺少第一次进展更新，目前尚未看到新的提交 [S08]。

## 来源索引

- `S01` [[DIS] Vellum: Reputation Extension on did:ckb](https://talk.nervos.org/t/dis-vellum-reputation-extension-on-did-ckb/10613/3) | truthixify | 2026-08-27 23:12:22 CST | Thank you all for supporting the project in the discussion phase. Vellum V2 proposal is now live on metaforo for voting stage, you can vote here: https://dao.ckb.community/thread/vot-vellum-reputation-extension-on-did-ckb-77380
- `S02` [Tranfr — Programmable Recovery for CKB](https://talk.nervos.org/t/tranfr-programmable-recovery-for-ckb/10644/7) | xingtianchunyan | 2026-08-27 09:46:17 CST | Hi @SalmanDev, Thank you for your continued interest in the Spark Program and for publishing the Tranfr — Programmable Recovery for CKB proposal. After review by the Spark Program committee, your proposal has been assigned a status of Pending. This is not a rejection, but an...
- `S03` [Tranfr — Programmable Recovery for CKB](https://talk.nervos.org/t/tranfr-programmable-recovery-for-ckb/10644/8) | SalmanDev | 2026-08-27 22:29:01 CST | Thanks for the constructive feedback. The revised proposal is now updated accordingly. Thanks again.
- `S04` [Spark Program | CKB-VM Sail Validation Sprint：可复现的 RISC-V 语义差分工具、Lean 4 证明与 Rocq/Coq 兼容性 Spike](https://talk.nervos.org/t/spark-program-ckb-vm-sail-validation-sprint-risc-v-lean-4-rocq-coq-spike/10562/15) | xingtianchunyan | 2026-08-27 10:58:39 CST | Hi @TinyuengKwan , We have noticed that it has been some time since the last progress update, so we are reaching out to check on the latest developments. First, I hope you and your team are doing well. Please take good care of your health and maintain a balance between work...
- `S05` [Spark Program | CKB-VM Sail Validation Sprint：可复现的 RISC-V 语义差分工具、Lean 4 证明与 Rocq/Coq 兼容性 Spike](https://talk.nervos.org/t/spark-program-ckb-vm-sail-validation-sprint-risc-v-lean-4-rocq-coq-spike/10562/16) | TinyuengKwan | 2026-08-27 13:34:55 CST | Update: 第三周工作已经push。这周工作主要集中在RVFI-DII 差分验证上： 加固 RVFI-DII 的启动流程，防止端口竞争（port race）和过期会话（stale session）问题 添加强制要求的 mutation matrix（变异矩阵）以及稳定的 JSON 报告封装格式 为包含 32 个 ADD/ADDI/BEQ 测试用例的测试集提供可重复回放（replay）的产物 在每个 PR 上执行差分验证，包括冷缓存（cold-cache）构建 下载并回放 CI 上传的验证证据 通过禁用 MOP，使注入的 CKB-VM ISA 与...
- `S06` [Spark Program | CKB-VM Sail Validation Sprint：可复现的 RISC-V 语义差分工具、Lean 4 证明与 Rocq/Coq 兼容性 Spike](https://talk.nervos.org/t/spark-program-ckb-vm-sail-validation-sprint-risc-v-lean-4-rocq-coq-spike/10562/17) | TinyuengKwan | 2026-08-27 13:36:19 CST | 我对我不及时更新周报表示抱歉，这主要由我不规律作息时间导致。我承诺会减少类似状况发生。
- `S07` [Spark Program | CKB-VM Sail Validation Sprint：可复现的 RISC-V 语义差分工具、Lean 4 证明与 Rocq/Coq 兼容性 Spike](https://talk.nervos.org/t/spark-program-ckb-vm-sail-validation-sprint-risc-v-lean-4-rocq-coq-spike/10562/18) | xingtianchunyan | 2026-08-27 20:09:04 CST | 不必抱歉！我们当然希望看到你的稳定更新，但你的身体健康无疑是最重要的！还请以身体健康为主！不论怎么说，看到你参与Spark的同时有机会改善作息，使身心更健康，简直太好了
- `S08` [Spark Program | Fiber RGB++ Swap](https://talk.nervos.org/t/spark-program-fiber-rgb-swap/10487/25) | xingtianchunyan | 2026-08-27 10:56:07 CST | Hi @Carl, We have noticed that the first progress update for Fiber RGB++ Swap has not yet been posted, so we are reaching out to check on the latest developments. First, I hope you and your team are doing well. Please take good care of your health and maintain a balance...
- `S09` [Polycrpt](https://talk.nervos.org/t/polycrpt/10666/2) | zz_tovarishch | 2026-08-27 09:37:42 CST | PolyCrypt 不是 CKB 的独占团队，他们一直是在做面向多链的通用状态通道框架（2024年年报）： image1920×818 127 KB 2023 年申请 Nervos grant 时，他们就已经同时在做 Cardano PolyCrypt - Payment Channels on CKB we recently also gathered some experience with building Perun for Cardano CKB 相关仓库今年一直在更新：GitHub - perun-network/perun-ckb-...
- `S10` [Polycrpt](https://talk.nervos.org/t/polycrpt/10666/3) | ckbbkc | 2026-08-27 09:45:50 CST | 状态通道并不是ckb独有的对吧
- `S11` [Spark Program | NNCBN - Nervos Network Community Boot Nodes](https://talk.nervos.org/t/spark-program-nncbn-nervos-network-community-boot-nodes/10653/2) | xingtianchunyan | 2026-08-27 09:45:23 CST | Hi @NNCBN ， Thank you and @knmo for your continued interest in the Spark Program and for submitting the “NNCBN - Nervos Network Community Boot Nodes” proposal. After review by the Spark Program committee, your proposal has been assigned a status of Pending. This is not a...
- `S12` [Spark Program | FiberTap: One-Line Crypto Tipping for Every Website](https://talk.nervos.org/t/spark-program-fibertap-one-line-crypto-tipping-for-every-website/10655/2) | xingtianchunyan | 2026-08-27 09:40:55 CST | Hi, @FidelCoder, Thank you for your continued interest in the Spark Program. The committee has completed its review. After careful consideration, it regrets to announce the rejection of the proposal for the FiberTap project. We would like to publicly explain the reasons behind...

## 活跃话题

1. [[DIS] Vellum: Reputation Extension on did:ckb](https://talk.nervos.org/t/dis-vellum-reputation-extension-on-did-ckb/10613) | 1 条近窗帖子 | 最新活动 2026-08-27 23:12:22 CST
2. [Tranfr — Programmable Recovery for CKB](https://talk.nervos.org/t/tranfr-programmable-recovery-for-ckb/10644) | 2 条近窗帖子 | 最新活动 2026-08-27 22:29:01 CST | tags: Pending
3. [Spark Program | CKB-VM Sail Validation Sprint：可复现的 RISC-V 语义差分工具、Lean 4 证明与 Rocq/Coq 兼容性 Spike](https://talk.nervos.org/t/spark-program-ckb-vm-sail-validation-sprint-risc-v-lean-4-rocq-coq-spike/10562) | 4 条近窗帖子 | 最新活动 2026-08-27 20:09:04 CST | tags: CKB-VM, In-Progress
4. [Spark Program | Fiber RGB++ Swap](https://talk.nervos.org/t/spark-program-fiber-rgb-swap/10487) | 1 条近窗帖子 | 最新活动 2026-08-27 10:56:07 CST | tags: In-Progress
5. [Polycrpt](https://talk.nervos.org/t/polycrpt/10666) | 2 条近窗帖子 | 最新活动 2026-08-27 09:45:50 CST
6. [Spark Program | NNCBN - Nervos Network Community Boot Nodes](https://talk.nervos.org/t/spark-program-nncbn-nervos-network-community-boot-nodes/10653) | 1 条近窗帖子 | 最新活动 2026-08-27 09:45:23 CST | tags: Node, Pending, Spark-Program, bootnode
7. [Spark Program | FiberTap: One-Line Crypto Tipping for Every Website](https://talk.nervos.org/t/spark-program-fibertap-one-line-crypto-tipping-for-every-website/10655) | 1 条近窗帖子 | 最新活动 2026-08-27 09:40:55 CST | tags: Rejection, Spark-Program

## 最近帖子摘录

- 2026-08-27 23:12:22 CST | truthixify | [[DIS] Vellum: Reputation Extension on did:ckb](https://talk.nervos.org/t/dis-vellum-reputation-extension-on-did-ckb/10613/3) | Thank you all for supporting the project in the discussion phase. Vellum V2 proposal is now live on metaforo for voting stage, you can vote here:...
- 2026-08-27 22:29:01 CST | SalmanDev | [Tranfr — Programmable Recovery for CKB](https://talk.nervos.org/t/tranfr-programmable-recovery-for-ckb/10644/8) | Thanks for the constructive feedback. The revised proposal is now updated accordingly. Thanks again.
- 2026-08-27 20:09:04 CST | xingtianchunyan | [Spark Program | CKB-VM Sail Validation Sprint：可复现的 RISC-V 语义差分工具、Lean 4 证明与 Rocq/Coq 兼容性 Spike](https://talk.nervos.org/t/spark-program-ckb-vm-sail-validation-sprint-risc-v-lean-4-rocq-coq-spike/10562/18) | 不必抱歉！我们当然希望看到你的稳定更新，但你的身体健康无疑是最重要的！还请以身体健康为主！不论怎么说，看到你参与Spark的同时有机会改善作息，使身心更健康，简直太好了
- 2026-08-27 13:36:19 CST | TinyuengKwan | [Spark Program | CKB-VM Sail Validation Sprint：可复现的 RISC-V 语义差分工具、Lean 4 证明与 Rocq/Coq 兼容性 Spike](https://talk.nervos.org/t/spark-program-ckb-vm-sail-validation-sprint-risc-v-lean-4-rocq-coq-spike/10562/17) | 我对我不及时更新周报表示抱歉，这主要由我不规律作息时间导致。我承诺会减少类似状况发生。
- 2026-08-27 13:34:55 CST | TinyuengKwan | [Spark Program | CKB-VM Sail Validation Sprint：可复现的 RISC-V 语义差分工具、Lean 4 证明与 Rocq/Coq 兼容性 Spike](https://talk.nervos.org/t/spark-program-ckb-vm-sail-validation-sprint-risc-v-lean-4-rocq-coq-spike/10562/16) | Update: 第三周工作已经push。这周工作主要集中在RVFI-DII 差分验证上： 加固 RVFI-DII 的启动流程，防止端口竞争（port race）和过期会话（stale session）问题 添加强制要求的 mutation matrix（变异矩阵）以及稳定的 JSON 报告封装格式 为包含 32 个 ADD/ADDI/BEQ...
- 2026-08-27 10:58:39 CST | xingtianchunyan | [Spark Program | CKB-VM Sail Validation Sprint：可复现的 RISC-V 语义差分工具、Lean 4 证明与 Rocq/Coq 兼容性 Spike](https://talk.nervos.org/t/spark-program-ckb-vm-sail-validation-sprint-risc-v-lean-4-rocq-coq-spike/10562/15) | Hi @TinyuengKwan , We have noticed that it has been some time since the last progress update, so we are reaching out to check on the latest developments. First, I hope you and...
- 2026-08-27 10:56:07 CST | xingtianchunyan | [Spark Program | Fiber RGB++ Swap](https://talk.nervos.org/t/spark-program-fiber-rgb-swap/10487/25) | Hi @Carl, We have noticed that the first progress update for Fiber RGB++ Swap has not yet been posted, so we are reaching out to check on the latest developments. First, I hope...
- 2026-08-27 09:46:17 CST | xingtianchunyan | [Tranfr — Programmable Recovery for CKB](https://talk.nervos.org/t/tranfr-programmable-recovery-for-ckb/10644/7) | Hi @SalmanDev, Thank you for your continued interest in the Spark Program and for publishing the Tranfr — Programmable Recovery for CKB proposal. After review by the Spark...
- 2026-08-27 09:45:50 CST | ckbbkc | [Polycrpt](https://talk.nervos.org/t/polycrpt/10666/3) | 状态通道并不是ckb独有的对吧
- 2026-08-27 09:45:23 CST | xingtianchunyan | [Spark Program | NNCBN - Nervos Network Community Boot Nodes](https://talk.nervos.org/t/spark-program-nncbn-nervos-network-community-boot-nodes/10653/2) | Hi @NNCBN ， Thank you and @knmo for your continued interest in the Spark Program and for submitting the “NNCBN - Nervos Network Community Boot Nodes” proposal. After review by...
- 2026-08-27 09:40:55 CST | xingtianchunyan | [Spark Program | FiberTap: One-Line Crypto Tipping for Every Website](https://talk.nervos.org/t/spark-program-fibertap-one-line-crypto-tipping-for-every-website/10655/2) | Hi, @FidelCoder, Thank you for your continued interest in the Spark Program. The committee has completed its review. After careful consideration, it regrets to announce the...
- 2026-08-27 09:37:42 CST | zz_tovarishch | [Polycrpt](https://talk.nervos.org/t/polycrpt/10666/2) | PolyCrypt 不是 CKB 的独占团队，他们一直是在做面向多链的通用状态通道框架（2024年年报）： image1920×818 127 KB 2023 年申请 Nervos grant 时，他们就已经同时在做 Cardano PolyCrypt - Payment Channels on CKB we recently also...
