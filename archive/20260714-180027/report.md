# Nervos Talk 社区简报

- 统计窗口: 2026-07-14 02:00:27 CST 到 2026-07-15 02:00:27 CST
- 生成时间: 2026-07-15 02:00:35 CST
- 话题数: 5
- 帖子数: 8
- 作者数: 6
- 总结模式: ai:openrouter

## 社区总结

## 今日发生了什么

今天 Nervos Talk 最热闹的讨论发生在 Vellum 声誉协议提案下方，社区成员就该协议发起方的技术投入与承诺发生了短暂但尖锐的交锋，随后澄清了误会。[S01, S02, S03, S04] 同时，Fiber 生态继续成为建设重心，新增了一位开发者提交跨链兑换的 Spark 资助申请，另有一篇关于用 CKB UDT 支付比特币闪电网络账单的教程发布。[S05, S07]

## 重点话题

- **Vellum 提案争议快速反转**：CDEX 最初反对该提案，理由是研究后发现 did:ckb 协议发起方"似乎没有足够信心或持续投入"。[S01] neon.bit 随即反驳，指出 truthixify 曾为社区贡献多个开源资源、工具，并向 CCC 主仓库提交过被接受的代码增强。[S02] CDEX 随后道歉并澄清，自己实际指的是 ckb:did 协议而非 did:ckb。[S03] neon.bit 进一步确认 did:ckb 今年及去年底仍有仓库贡献，CCC 也计划推进 DID 操作，该方向并未被放弃。[S04]

- **Fiber RGB++ 跨链兑换申请 Spark 资助**：独立开发者 Carl 提交提案，计划用 6 周时间、3 个里程碑，实现首个通过 Fiber 在 RGB++ 比特币资产与 CKB 之间的可运行跨链兑换，申请资金 1,000 美元。[S05]

- **CKB-VM B 扩展指令兼容性明确**：mohanson 在技术帖中确认，即便宿主机是 RISC-V，CKB-VM 也不假设宿主必须支持 B 扩展指令，因此目前答案为"不支持"——体现了团队保持虚拟机通用性的设计思路。[S08]

- **Nervos Brain 项目补充测试数据**：IrisNeko 回应委员会审阅反馈，补充说明了"真实群测均值"和"按回答聚合"两项指标的数据来源、原始分布与计算方法，涉及 60 条真实用户回答和 40 条固定验证数据。[S06]

- **Fiber CCH 支付教程上线**：RetricSu 发布实践指南，演示如何通过 Fiber 的跨链枢纽（CCH）用 CKB UDT 自动触发并结算比特币闪电网络账单。[S07]

## 值得继续跟进

- **Vellum 提案投票走向**：尽管误会已澄清，但 CDEX 对协议发起方长期承诺的关切仍具代表性，后续需观察该提案是否获得足够社区信任票，以及 did:ckb 与 ckb:did 的命名混淆是否会在其他场合再次引发认知摩擦。[S01, S03, S04]

- **Fiber RGB++ Swap 的交付可行性**：Carl 作为独立开发者申请 6 周周期，时间紧凑且资金申请较低，里程碑进展是否顺利将影响社区对小型 Fiber 悬赏任务执行模式的评估。[S05]

- **Nervos Brain 委员会评审结果**：项目方已按要求补充了评测方法论细节，下一批反馈或最终决议可能对 Agentic RAG 类工具在 Nervos 生态中的定位产生信号意义。[S06]

## 来源索引

- `S01` [[DIS] Vellum: Reputation Extension on did:ckb](https://talk.nervos.org/t/dis-vellum-reputation-extension-on-did-ckb/10419/5) | CDEX | 2026-07-14 22:51:49 CST | As a response for Cannot open the CKB DAO voting page - #16 by CDEX The reason to oppose the proposal is that based on research, the protocol’s initiator doesn’t appear to have strong confidence in the protocol or to be sufficiently committed to its continued development.
- `S02` [[DIS] Vellum: Reputation Extension on did:ckb](https://talk.nervos.org/t/dis-vellum-reputation-extension-on-did-ckb/10419/6) | neon.bit | 2026-07-14 23:32:23 CST | Thanks for the reply @CDEX. Based on @truthixify’s thread history, he’s contributed multiple open-sourced resources and tools that have been liked by the community. Additionally, he contributed a feature enhancement to CCC that was accepted and pushed to the main repo. CDEX:...
- `S03` [[DIS] Vellum: Reputation Extension on did:ckb](https://talk.nervos.org/t/dis-vellum-reputation-extension-on-did-ckb/10419/7) | CDEX | 2026-07-14 23:52:03 CST | My bad, the protocol I referred to in my reply is ckb:did
- `S04` [[DIS] Vellum: Reputation Extension on did:ckb](https://talk.nervos.org/t/dis-vellum-reputation-extension-on-did-ckb/10419/8) | neon.bit | 2026-07-15 00:30:19 CST | Thank you for clarifying. As far as I can tell, did:ckb has had contributions to its repo this year and end of last year, and CCC had plans to implement DID operations. It is not abandoned in concept or in practice. Truthixify’s contributions helped to accelerate that...
- `S05` [Spark Program | Fiber RGB++ Swap](https://talk.nervos.org/t/spark-program-fiber-rgb-swap/10487/1) | Carl | 2026-07-14 23:27:04 CST | Fiber RGB++ Swap The first working cross-chain swap between RGB++ Bitcoin assets and CKB, over Fiber Applicant: Carl (solo developer) Track: Fiber Network, RGB++ Innovations Requested funding: $1,000 Timeline: 6 weeks, delivered in 3 milestones Executive Summary Fiber’s Cross-...
- `S06` [Spark Program | Nervos Brain - A Global Developer Onboarding Engine and Cross-Language Hub Powered by Agentic RAG](https://talk.nervos.org/t/spark-program-nervos-brain-a-global-developer-onboarding-engine-and-cross-language-hub-powered-by-agentic-rag/9995/47) | IrisNeko | 2026-07-14 17:52:55 CST | Hi xingtian, 感谢委员会的详细审阅和具体反馈。你指出得很准确：此前报告展示了评分结果，但没有充分说明“真实群测均值”和“按回答聚合”两个指标的定义、原始分布和计算方法。现补充如下。 一、数据来源与分组 真实群测： 来自 Telegram 测试群中的真实用户问题和评分，共记录 60 条回答，8 名真实测试者，收集到 27 次 1–5 分评分。 补充跑测： 另外进行了 40 条固定验证，覆盖 8 个补充测试人设。这部分主要使用预设的、部分由 AI...
- `S07` [Paying a Bitcoin Lightning Invoice with CKB UDT on Fiber](https://talk.nervos.org/t/paying-a-bitcoin-lightning-invoice-with-ckb-udt-on-fiber/10486/1) | RetricSu | 2026-07-14 15:36:27 CST | Fiber’s Cross-Chain Hub (CCH) is one of the coolest parts of the current Fiber stack: it allows a Fiber payment on CKB to automatically trigger and settle a payment on a completely different network, like Bitcoin’s Lightning Network. To show how this works in practice, we...
- `S08` [Deep Dive Into CKB-VM B Extension](https://talk.nervos.org/t/deep-dive-into-ckb-vm-b-extension/10484/3) | mohanson | 2026-07-14 08:53:59 CST | We have a RISC-V backend: that’s right, a RISC-V virtual machine running on RISC-V. Since we want CKB-VM to be more versatile, we don’t assume that the RISC-V host running CKB-VM must support B extended instructions. Therefore, the answer is no.

## 活跃话题

1. [[DIS] Vellum: Reputation Extension on did:ckb](https://talk.nervos.org/t/dis-vellum-reputation-extension-on-did-ckb/10419) | 4 条近窗帖子 | 最新活动 2026-07-15 00:30:19 CST | tags: CKB, dapp, testnet
2. [Spark Program | Fiber RGB++ Swap](https://talk.nervos.org/t/spark-program-fiber-rgb-swap/10487) | 1 条近窗帖子 | 最新活动 2026-07-14 23:27:04 CST | tags: Spark-Program
3. [Spark Program | Nervos Brain - A Global Developer Onboarding Engine and Cross-Language Hub Powered by Agentic RAG](https://talk.nervos.org/t/spark-program-nervos-brain-a-global-developer-onboarding-engine-and-cross-language-hub-powered-by-agentic-rag/9995) | 1 条近窗帖子 | 最新活动 2026-07-14 17:52:55 CST | tags: In-Progress, Spark-Program
4. [Paying a Bitcoin Lightning Invoice with CKB UDT on Fiber](https://talk.nervos.org/t/paying-a-bitcoin-lightning-invoice-with-ckb-udt-on-fiber/10486) | 1 条近窗帖子 | 最新活动 2026-07-14 15:36:27 CST | tags: fiber
5. [Deep Dive Into CKB-VM B Extension](https://talk.nervos.org/t/deep-dive-into-ckb-vm-b-extension/10484) | 1 条近窗帖子 | 最新活动 2026-07-14 08:53:59 CST | tags: CKB-VM

## 最近帖子摘录

- 2026-07-15 00:30:19 CST | neon.bit | [[DIS] Vellum: Reputation Extension on did:ckb](https://talk.nervos.org/t/dis-vellum-reputation-extension-on-did-ckb/10419/8) | Thank you for clarifying. As far as I can tell, did:ckb has had contributions to its repo this year and end of last year, and CCC had plans to implement DID operations. It is...
- 2026-07-14 23:52:03 CST | CDEX | [[DIS] Vellum: Reputation Extension on did:ckb](https://talk.nervos.org/t/dis-vellum-reputation-extension-on-did-ckb/10419/7) | My bad, the protocol I referred to in my reply is ckb:did
- 2026-07-14 23:32:23 CST | neon.bit | [[DIS] Vellum: Reputation Extension on did:ckb](https://talk.nervos.org/t/dis-vellum-reputation-extension-on-did-ckb/10419/6) | Thanks for the reply @CDEX. Based on @truthixify’s thread history, he’s contributed multiple open-sourced resources and tools that have been liked by the community....
- 2026-07-14 23:27:04 CST | Carl | [Spark Program | Fiber RGB++ Swap](https://talk.nervos.org/t/spark-program-fiber-rgb-swap/10487/1) | Fiber RGB++ Swap The first working cross-chain swap between RGB++ Bitcoin assets and CKB, over Fiber Applicant: Carl (solo developer) Track: Fiber Network, RGB++ Innovations...
- 2026-07-14 22:51:49 CST | CDEX | [[DIS] Vellum: Reputation Extension on did:ckb](https://talk.nervos.org/t/dis-vellum-reputation-extension-on-did-ckb/10419/5) | As a response for Cannot open the CKB DAO voting page - #16 by CDEX The reason to oppose the proposal is that based on research, the protocol’s initiator doesn’t appear to have...
- 2026-07-14 17:52:55 CST | IrisNeko | [Spark Program | Nervos Brain - A Global Developer Onboarding Engine and Cross-Language Hub Powered by Agentic RAG](https://talk.nervos.org/t/spark-program-nervos-brain-a-global-developer-onboarding-engine-and-cross-language-hub-powered-by-agentic-rag/9995/47) | Hi xingtian, 感谢委员会的详细审阅和具体反馈。你指出得很准确：此前报告展示了评分结果，但没有充分说明“真实群测均值”和“按回答聚合”两个指标的定义、原始分布和计算方法。现补充如下。 一、数据来源与分组 真实群测： 来自 Telegram 测试群中的真实用户问题和评分，共记录 60 条回答，8 名真实测试者，收集到 27 次 1–5 分评分。...
- 2026-07-14 15:36:27 CST | RetricSu | [Paying a Bitcoin Lightning Invoice with CKB UDT on Fiber](https://talk.nervos.org/t/paying-a-bitcoin-lightning-invoice-with-ckb-udt-on-fiber/10486/1) | Fiber’s Cross-Chain Hub (CCH) is one of the coolest parts of the current Fiber stack: it allows a Fiber payment on CKB to automatically trigger and settle a payment on a...
- 2026-07-14 08:53:59 CST | mohanson | [Deep Dive Into CKB-VM B Extension](https://talk.nervos.org/t/deep-dive-into-ckb-vm-b-extension/10484/3) | We have a RISC-V backend: that’s right, a RISC-V virtual machine running on RISC-V. Since we want CKB-VM to be more versatile, we don’t assume that the RISC-V host running CKB-...
