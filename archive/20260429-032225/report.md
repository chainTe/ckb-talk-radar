# Nervos Talk 社区简报

- 统计窗口: 2026-04-28 11:22:25 CST 到 2026-04-29 11:22:25 CST
- 生成时间: 2026-04-29 11:22:32 CST
- 话题数: 7
- 帖子数: 9
- 作者数: 7
- 总结模式: ai:openrouter

## 社区总结

## 今日发生了什么

今天论坛的核心动态集中在技术基建与星火计划项目推进上：CKB-VM 获得了新的差分测试框架，一个去中心化众筹项目上线测试网自动结算机器人，而多个星火计划资助项目进入了评审、周报更新或收尾阶段。[S01, S02, S04, S05, S08]

## 重点话题

- **CKB-VM 安全基建双线并进**：CKBdev 团队实现了 CKB-VM 的差分测试框架，用于验证优化和未来架构变更；与此同时，社区成员提交的 CKB-VM Sail 形式化验证提案因超出星火计划"低门槛、快节奏"的资助范围，被建议调整后再正式评审。[S01, S02]

- **CKB Kickstarter 测试网实现完全无信任化**：Ayoub_Lesfer 更新了自动结算机器人已在测试网部署并完成端到端验证，众筹流程（创建→认捐→截止→结算）现在无需人工介入即可自动完成。[S04]

- **星火计划项目状态分化**：Dular 项目因需补充 Daraja 生产环境凭据和修正 CKB 发放机制表述，被暂定为 Pending；Nervos Brain 发布第七周周报，重点推进工具闭环、评测基线和 Telegram/Discord 稳定性，并计划本周拉试用群邀请委员会体验。[S03, S05, S06]

- **DAO v1.1 项目正式收尾**：_magicsheep 确认项目终止，已交付的 Milestone 1 对应款项保留，代码继续开源。[S08]

- **Cellora 索引服务获社区反馈**：ArthurZhang 参与讨论，建议交易包含证明优先利用 CKB 现有 RPC 接口而非直接采用 Flyclient 作为务实第一步。[S09]

## 值得继续跟进

- **CKB-VM Sail 形式化验证能否找到合适的资助路径**：该项目被认定对 CKB 执行层安全至关重要，但超出星火计划范畴，需观察提案人是否会调整规模或寻求其他资助渠道。[S02]

- **Nervos Brain 试用群反馈与委员会的验收标准**：本周即将开启委员会体验，其多轮交互稳定性与评测基线能否满足"可验证"要求，将直接影响项目后续进展。[S05, S06]

- **Cellora 索引架构的社区共识走向**：已有资深开发者介入技术路线讨论，后续是否形成更具体的实现方案值得关注。[S09]

## 来源索引

- `S01` [TeamCKB Dev Log (Updated: Apr 29, 2026)](https://talk.nervos.org/t/teamckb-dev-log-updated-apr-29-2026/8572/35) | CKBdev | 2026-04-29 10:01:11 CST | Updates Features Differential Testing Framework for ckb-vm Implemented a differential test framework for ckb-vm. This provides a stronger foundation for validating optimizations and future architecture changes: GitHub - yuqiliu617/ckb-vm-contrib at differential-test · GitHub...
- `S02` [Spark Program | CKB-VM Sail Formal Verification — Proving CKB-VM RISC-V Instruction Equivalence via Sail Specification and Coq Theorem Prover / CKB-VM Sail 形式化验证 — 基于 Sail 规范与 Coq 定理证明器的 CKB-VM RISC-V 指令等价性证明](https://talk.nervos.org/t/spark-program-ckb-vm-sail-formal-verification-proving-ckb-vm-risc-v-instruction-equivalence-via-sail-specification-and-coq-theorem-prover-ckb-vm-sail-sail-coq-ckb-vm-risc-v/10214/4) | xingtianchunyan | 2026-04-29 10:00:41 CST | @TinyuengKwan 你好，感谢提交 ckb-vm-sail-verify 的提案。这个方向非常关键：CKB-VM 是 CKB 的执行层安全基石，而你提出的 “Sail（官方规范）+ Coq（形式化证明）+ 差分测试（工程验证）” 的双轨方案，也能看出你在 Sail/ACT 生态中有相对稀缺的一手经验与工程积累。 需要说明的是，该项目已明显超出星火计划的支持范围（以 低门槛、快节奏 的方式帮助社区开发者启动小型原型项目）。如果你仍希望向委员会正式递交该项目，那么在提交委员会正式评审前，我个人建议你按 Spark...
- `S03` [Spark Program | Dular](https://talk.nervos.org/t/spark-program-dular/10212/4) | xingtianchunyan | 2026-04-29 09:49:03 CST | @duongja 你好，感谢你提交 Dular 项目提案，并根据预审建议补充了 How to Verify、预算拆分与风险说明等内容。整体方向（Fiber + RUSD/UDT + 真实在地试点）很契合 Spark 对“可落地、可验证”的资助导向。 本项目当前状态暂定为 Pending，并非否定项目价值，而是表示：在进入下次正式评审/投票前，我们还需要你补齐两类“可验证凭据”，并纠正提案中关于 CKB 发放与汇率折算机制的表述，以避免后续沟通成本与验收争议。 1) 请补充：Daraja 生产环境凭据的可视化证据。 你已声明持有 STK Push +...
- `S04` [Introducing CKB Kickstarter: Decentralized All-or-Nothing Crowdfunding on Nervos CKB (Testnet MVP Live)](https://talk.nervos.org/t/introducing-ckb-kickstarter-decentralized-all-or-nothing-crowdfunding-on-nervos-ckb-testnet-mvp-live/10130/9) | Ayoub_Lesfer | 2026-04-29 01:10:24 CST | Update: Automatic Finalization Bot live on testnet Following up on the v1.1 update above: the bot is deployed and end-to-end verified on testnet as of yesterday (2026-04-27). The platform is now fully trustless on testnet, campaigns flow create → pledge → deadline →...
- `S05` [Spark Program | Nervos Brain - A Global Developer Onboarding Engine and Cross-Language Hub Powered by Agentic RAG](https://talk.nervos.org/t/spark-program-nervos-brain-a-global-developer-onboarding-engine-and-cross-language-hub-powered-by-agentic-rag/9995/31) | IrisNeko | 2026-04-28 19:54:09 CST | 第七周周报 一、本周目标（工具闭环与评测基线周） 本周承接第六周“多轮可持续交互”阶段的工作，重点从“机制已经具备”推进到“关键路径真正闭环、且后续可以被稳定评测”。核心目标有四个： 继续治理运行时日志噪音，补齐最小可观测性闭环。 让 discourse_query / github_search 从协议层定义走到图执行主路径可调用。 建立第一版多轮评测集，为后续 benchmark 和量化回归提供统一输入。 补齐 Telegram / Discord 两端在长消息与异常路径下的稳定性回归。 二、本周完成 日志治理与诊断视图补齐...
- `S06` [Spark Program | Nervos Brain - A Global Developer Onboarding Engine and Cross-Language Hub Powered by Agentic RAG](https://talk.nervos.org/t/spark-program-nervos-brain-a-global-developer-onboarding-engine-and-cross-language-hub-powered-by-agentic-rag/9995/32) | IrisNeko | 2026-04-28 20:00:25 CST | 感谢您的建议， 我上周对系统做了基础的评测，并计划在这周拉一个Telegram试用群，邀请委员会的成员提前体验。同时欢迎在体验中提出建议，来帮助我改善系统。 Best regards.
- `S07` [Spark Program | Nervos Brain - A Global Developer Onboarding Engine and Cross-Language Hub Powered by Agentic RAG](https://talk.nervos.org/t/spark-program-nervos-brain-a-global-developer-onboarding-engine-and-cross-language-hub-powered-by-agentic-rag/9995/33) | zz_tovarishch | 2026-04-28 22:03:27 CST | Hi IrisNeko, 目前论坛已经接入AI翻译工具，Spark不再强制要求项目在Talk上沉淀的内容需采用双语版本 期待项目的持续发展！
- `S08` [Discontinuation of the DAO v1.1 project](https://talk.nervos.org/t/discontinuation-of-the-dao-v1-1-project/10204/11) | _magicsheep | 2026-04-28 19:56:27 CST | In consideration of Terry’s advice, the following updates are provided regarding the closure of DAO v1.1: Payment: The proposal team will retain the payment corresponding to the already‑delivered Milestone 1. Code: The code will remain open source and is accessible at this...
- `S09` [Cellora — designing a production indexing and query service for CKB (feedback welcome)](https://talk.nervos.org/t/cellora-designing-a-production-indexing-and-query-service-for-ckb-feedback-welcome/10199/4) | ArthurZhang | 2026-04-28 16:40:25 CST | Just came across this thread and found it interesting, so I’ll try to offer a few suggestions. I think the honest answer is: For tx inclusion proofs, the practical first step is likely not Flyclient, but exposing CKB’s existing get_transaction_proof / verify_transaction_proof...

## 活跃话题

1. [TeamCKB Dev Log (Updated: Apr 29, 2026)](https://talk.nervos.org/t/teamckb-dev-log-updated-apr-29-2026/8572) | 1 条近窗帖子 | 最新活动 2026-04-29 10:01:11 CST | tags: CKB, CKB-VM
2. [Spark Program | CKB-VM Sail Formal Verification — Proving CKB-VM RISC-V Instruction Equivalence via Sail Specification and Coq Theorem Prover / CKB-VM Sail 形式化验证 — 基于 Sail 规范与 Coq 定理证明器的 CKB-VM RISC-V 指令等价性证明](https://talk.nervos.org/t/spark-program-ckb-vm-sail-formal-verification-proving-ckb-vm-risc-v-instruction-equivalence-via-sail-specification-and-coq-theorem-prover-ckb-vm-sail-sail-coq-ckb-vm-risc-v/10214) | 1 条近窗帖子 | 最新活动 2026-04-29 10:00:41 CST | tags: Spark-Program
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
