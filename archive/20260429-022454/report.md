# Nervos Talk 社区简报

- 统计窗口: 2026-04-28 10:24:54 CST 到 2026-04-29 10:24:54 CST
- 生成时间: 2026-04-29 10:24:58 CST
- 话题数: 7
- 帖子数: 10
- 作者数: 7
- 总结模式: ai:openrouter

## 社区总结

## 今日发生了什么

今天 Nervos Talk 整体节奏偏技术向，CKB-VM 基础设施继续成为焦点：一方面有团队提交了基于 Sail + Coq 的形式化验证提案，另一方面 ckb-vm 本身新增了差分测试框架。同时几个星火计划项目都在推进中，Nervos Brain 项目发布了第七周周报，Dular 和 DAO v1.1 项目也有了新的状态更新。

## 重点话题

- **ckb-vm 新增差分测试框架**：TeamCKB 在开发日志中更新了 ckb-vm 的差分测试框架实现，目的是为后续优化和架构变更提供更可靠的验证基础。

- **CKB-VM Sail 形式化验证提案引发讨论**：xingtianchunyan 针对该项目给出了详细反馈，认为其技术方向关键且有价值，但明确指出该复杂度已超出星火计划"低门槛、快节奏"的原型资助范围，建议调整提交策略后再走正式评审流程。

- **Dular 项目暂定为 Pending**：星火委员会要求提案方补充 Daraja 生产环境凭据的可视化证据，并修正 CKB 发放与汇率折算机制的表述，才能进入下一轮正式评审。

- **DAO v1.1 项目正式终止**：经 Terry 建议后确认关闭，团队保留已交付 Milestone 1 对应的款项，代码继续开源留存。

- **Nervos Brain 发布第七周周报**：项目进入"工具闭环与评测基线周"，重点补齐了日志治理、graph 执行主路径调用、多轮评测集建设以及 Telegram/Discord 稳定性回归。

- **CKB Kickstarter 测试网续更**：Ayoub_Lesfer 更新了自动结算机器人已在测试网部署并端到端验证完成，平台在测试网实现全信任化流程。

- **Cellora 索引服务获技术反馈**：ArthurZhang 针对该项目提出务实建议，认为交易包含证明的第一步更宜优先暴露 CKB 现有的 get_transaction_proof / verify_transaction_proof 接口，而非直接上 Flyclient。

## 值得继续跟进

- **星火计划资助边界的实际把握**：CKB-VM Sail 形式化验证提案被拒于星火门槛之外，后续是会转向其他资助渠道、拆分阶段重新申请，还是调整方案缩小范围，值得观察。

- **Nervos Brain 的委员会试用反馈**：IrisNeko 计划本周拉 Telegram 试用群邀请委员会成员体验，这批反馈可能直接影响项目第八周的方向调整。

- **Dular 补件进度**：Pending 状态下两项"可验证凭据"能否及时补齐，尤其是跨境支付落地场景的真实环境证据，关系到该项目能否复活进入投票。

## 活跃话题

1. [TeamCKB Dev Log (Updated: Apr 29, 2026)](https://talk.nervos.org/t/teamckb-dev-log-updated-apr-29-2026/8572) | 1 条近窗帖子 | 最新活动 2026-04-29 10:01:11 CST | tags: CKB, CKB-VM
2. [Spark Program | CKB-VM Sail Formal Verification — Proving CKB-VM RISC-V Instruction Equivalence via Sail Specification and Coq Theorem Prover / CKB-VM Sail 形式化验证 — 基于 Sail 规范与 Coq 定理证明器的 CKB-VM RISC-V 指令等价性证明](https://talk.nervos.org/t/spark-program-ckb-vm-sail-formal-verification-proving-ckb-vm-risc-v-instruction-equivalence-via-sail-specification-and-coq-theorem-prover-ckb-vm-sail-sail-coq-ckb-vm-risc-v/10214) | 2 条近窗帖子 | 最新活动 2026-04-29 10:00:41 CST | tags: Spark-Program
3. [Spark Program | Dular](https://talk.nervos.org/t/spark-program-dular/10212) | 1 条近窗帖子 | 最新活动 2026-04-29 09:49:03 CST | tags: Spark-Program, Submitted
4. [Introducing CKB Kickstarter: Decentralized All-or-Nothing Crowdfunding on Nervos CKB (Testnet MVP Live)](https://talk.nervos.org/t/introducing-ckb-kickstarter-decentralized-all-or-nothing-crowdfunding-on-nervos-ckb-testnet-mvp-live/10130) | 1 条近窗帖子 | 最新活动 2026-04-29 01:10:24 CST | tags: CKB, dapp
5. [Spark Program | Nervos Brain - A Global Developer Onboarding Engine and Cross-Language Hub Powered by Agentic RAG](https://talk.nervos.org/t/spark-program-nervos-brain-a-global-developer-onboarding-engine-and-cross-language-hub-powered-by-agentic-rag/9995) | 3 条近窗帖子 | 最新活动 2026-04-28 22:03:27 CST | tags: In-Progress, Spark-Program
6. [Discontinuation of the DAO v1.1 project](https://talk.nervos.org/t/discontinuation-of-the-dao-v1-1-project/10204) | 1 条近窗帖子 | 最新活动 2026-04-28 19:56:27 CST
7. [Cellora — designing a production indexing and query service for CKB (feedback welcome)](https://talk.nervos.org/t/cellora-designing-a-production-indexing-and-query-service-for-ckb-feedback-welcome/10199) | 1 条近窗帖子 | 最新活动 2026-04-28 16:40:25 CST | tags: CKB, Nervos-项目动态, dapp, testnet

## 最近帖子摘录

- 2026-04-29 10:01:11 CST | CKBdev | [TeamCKB Dev Log (Updated: Apr 29, 2026)](https://talk.nervos.org/t/teamckb-dev-log-updated-apr-29-2026/8572/35) | Updates Features Differential Testing Framework for ckb-vm Implemented a differential test framework for ckb-vm. This provides a stronger foundation for validating optimizations...
- 2026-04-29 10:00:41 CST | xingtianchunyan | [Spark Program | CKB-VM Sail Formal Verification — Proving CKB-VM RISC-V Instruction Equivalence via Sail Specification and Coq Theorem Prover / CKB-VM Sail 形式化验证 — 基于 Sail 规范与 Coq 定理证明器的 CKB-VM RISC-V 指令等价性证明](https://talk.nervos.org/t/spark-program-ckb-vm-sail-formal-verification-proving-ckb-vm-risc-v-instruction-equivalence-via-sail-specification-and-coq-theorem-prover-ckb-vm-sail-sail-coq-ckb-vm-risc-v/10214/4) | @TinyuengKwan 你好，感谢提交 ckb-vm-sail-verify 的提案。这个方向非常关键：CKB-VM 是 CKB 的执行层安全基石，而你提出的 “Sail（官方规范）+ Coq（形式化证明）+ 差分测试（工程验证）” 的双轨方案，也能看出你在 Sail/ACT 生态中有相对稀缺的一手经验与工程积累。...
- 2026-04-29 09:49:03 CST | xingtianchunyan | [Spark Program | Dular](https://talk.nervos.org/t/spark-program-dular/10212/4) | @duongja 你好，感谢你提交 Dular 项目提案，并根据预审建议补充了 How to Verify、预算拆分与风险说明等内容。整体方向（Fiber + RUSD/UDT + 真实在地试点）很契合 Spark 对“可落地、可验证”的资助导向。 本项目当前状态暂定为...
- 2026-04-29 01:10:24 CST | Ayoub_Lesfer | [Introducing CKB Kickstarter: Decentralized All-or-Nothing Crowdfunding on Nervos CKB (Testnet MVP Live)](https://talk.nervos.org/t/introducing-ckb-kickstarter-decentralized-all-or-nothing-crowdfunding-on-nervos-ckb-testnet-mvp-live/10130/9) | Update: Automatic Finalization Bot live on testnet Following up on the v1.1 update above: the bot is deployed and end-to-end verified on testnet as of yesterday (2026-04-27)....
- 2026-04-28 22:03:27 CST | zz_tovarishch | [Spark Program | Nervos Brain - A Global Developer Onboarding Engine and Cross-Language Hub Powered by Agentic RAG](https://talk.nervos.org/t/spark-program-nervos-brain-a-global-developer-onboarding-engine-and-cross-language-hub-powered-by-agentic-rag/9995/33) | Hi IrisNeko, 目前论坛已经接入AI翻译工具，Spark不再强制要求项目在Talk上沉淀的内容需采用双语版本 期待项目的持续发展！
- 2026-04-28 20:00:25 CST | IrisNeko | [Spark Program | Nervos Brain - A Global Developer Onboarding Engine and Cross-Language Hub Powered by Agentic RAG](https://talk.nervos.org/t/spark-program-nervos-brain-a-global-developer-onboarding-engine-and-cross-language-hub-powered-by-agentic-rag/9995/32) | 感谢您的建议， 我上周对系统做了基础的评测，并计划在这周拉一个Telegram试用群，邀请委员会的成员提前体验。同时欢迎在体验中提出建议，来帮助我改善系统。 Best regards.
- 2026-04-28 19:56:27 CST | _magicsheep | [Discontinuation of the DAO v1.1 project](https://talk.nervos.org/t/discontinuation-of-the-dao-v1-1-project/10204/11) | In consideration of Terry’s advice, the following updates are provided regarding the closure of DAO v1.1: Payment: The proposal team will retain the payment corresponding to the...
- 2026-04-28 19:54:09 CST | IrisNeko | [Spark Program | Nervos Brain - A Global Developer Onboarding Engine and Cross-Language Hub Powered by Agentic RAG](https://talk.nervos.org/t/spark-program-nervos-brain-a-global-developer-onboarding-engine-and-cross-language-hub-powered-by-agentic-rag/9995/31) | 第七周周报 一、本周目标（工具闭环与评测基线周） 本周承接第六周“多轮可持续交互”阶段的工作，重点从“机制已经具备”推进到“关键路径真正闭环、且后续可以被稳定评测”。核心目标有四个： 继续治理运行时日志噪音，补齐最小可观测性闭环。 让 discourse_query / github_search 从协议层定义走到图执行主路径可调用。...
- 2026-04-28 16:40:25 CST | ArthurZhang | [Cellora — designing a production indexing and query service for CKB (feedback welcome)](https://talk.nervos.org/t/cellora-designing-a-production-indexing-and-query-service-for-ckb-feedback-welcome/10199/4) | Just came across this thread and found it interesting, so I’ll try to offer a few suggestions. I think the honest answer is: For tx inclusion proofs, the practical first step is...
- 2026-04-28 11:13:16 CST | ArthurZhang | [Spark Program | CKB-VM Sail Formal Verification — Proving CKB-VM RISC-V Instruction Equivalence via Sail Specification and Coq Theorem Prover / CKB-VM Sail 形式化验证 — 基于 Sail 规范与 Coq 定理证明器的 CKB-VM RISC-V 指令等价性证明](https://talk.nervos.org/t/spark-program-ckb-vm-sail-formal-verification-proving-ckb-vm-risc-v-instruction-equivalence-via-sail-specification-and-coq-theorem-prover-ckb-vm-sail-sail-coq-ckb-vm-risc-v/10214/3) | This looks like a valuable direction. A further verified CKB-VM foundation would strengthen the whole CKB scripting stack. Proving instruction-level equivalence against the Sail...
