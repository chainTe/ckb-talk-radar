# Nervos Talk 社区简报

- 统计窗口: 2026-09-18 03:25:52 CST 到 2026-09-19 03:25:52 CST
- 生成时间: 2026-09-19 03:26:00 CST
- 话题数: 7
- 帖子数: 8
- 作者数: 4
- 总结模式: ai:openai-compatible

## 社区总结

## 今日发生了什么

材料显示，过去 24 小时的帖子都集中在 2026-09-18 [S01, S02, S03, S04, S05, S06, S07, S08]。今天论坛最集中的动静来自 Spark Program 的结项、付款与进度跟进：Dular 已发放最终款项并发布结项报告，CKB Builder Lab 发布结项评价，CKB Wallet Behaviour Intelligence 被要求更好地向社区展示成果，NNCBN 因首周进度未更新被联系 [S01, S02, S03, S04, S05]。同时，今天还有新讨论帖探索 CKB 上原生 RWA 借贷，以及 TeamCKB 开发日志和 Fiber Network 流动性再平衡 RFC 的回复 [S06, S07, S08]。整体看，论坛不算冷清，主线是资助项目收尾与基础设施开发进展 [S01, S02, S03, S04, S05, S06, S07, S08]。

## 重点话题

- Spark Program 多个项目集中更新：Dular 的最终款项已发放并给出交易哈希，同时说明第三笔款项从个人钱包支付而出现额外事项 [S02]；Dular 结项报告称其在资助周期内完成了从“移动货币场景的稳定币钱包”概念到真实用户试点的闭环，并以 Fiber Network 为结算层，交付手机号身份注册与 OTP 验证、phone → Fiber pubkey 查询 API、基于 Safaricom Daraja 的相关集成等内容 [S03]。
- CKB Builder Lab 发布结项报告：评价摘要称该项目是面向 CKB 生态的交互式开发者入门基础设施，通过浏览器端 Cell 模型模拟器和自动验证挑战系统，让开发者无需配置钱包、节点或环境即可理解 CKB 核心架构概念 [S04]；报告显示项目在约 10 周内完成了 MVP，完成日期为 2025 年 9 月 11 日 [S04]。
- CKB Wallet Behaviour Intelligence 收到委员会反馈：委员会认可已完成工作的工程价值，也理解原目标未完全达成，并希望项目更好地向社区呈现成果 [S05]；NNCBN 则被指出首周进度更新尚未完成，委员会正在联系了解最新进展 [S01]。
- TeamCKB Dev Log 更新：8 月 19 日至 9 月 15 日的周期聚焦节点与轻客户端加固、CKB-VM 维护，以及下一版 tx-pool、存储和网络架构的持续工作 [S07]；里程碑包括 CKB-VM v0.24.15 发布 [S07]。
- 新话题与 RFC 讨论：SalmanDev 发起“RWAs and Lending on CKB”，探索在 CKB 上原生地以现实世界资产索赔进行借贷，且不依赖桥或外部托管 [S06]；在 Fiber Network 自动通道流动性再平衡 RFC 下，有回复认为最好由 @quake 及其团队来回答相关问题，因为他们可能有更准确的信息 [S08]。

## 值得继续跟进

- 关注 Dular 结项后的额外付款事项如何收尾，以及最终款项交易哈希对应的资金发放是否还有后续说明 [S02]；同时留意 CKB Wallet Behaviour Intelligence 是否按委员会要求向社区展示成果 [S05]。
- 关注 NNCBN 首周进度更新是否补齐，以及 Spark Program 其他项目是否继续发布结项报告或评价 [S01, S03, S04]。
- 关注 CKB 上原生 RWA 借贷的讨论是否形成具体方案，尤其是“无桥、无外部托管依赖”的路径如何落地 [S06]；也留意 Fiber Network 流动性再平衡 RFC 是否会由 quake 团队回应，以及 TeamCKB 下一阶段架构工作进展 [S07, S08]。

## 来源索引

- `S01` [Spark Program | NNCBN - Nervos Network Community Boot Nodes](https://talk.nervos.org/t/spark-program-nncbn-nervos-network-community-boot-nodes/10653/9) | xingtianchunyan | 2026-09-18 22:37:19 CST | Hello @NNCBN , We noticed that your first-week progress update has not yet been completed, so we are reaching out to learn about the latest developments with your project. First of all, we hope that you and your team are doing well. Please be sure to take care of yourselves...
- `S02` [Spark Program | Dular](https://talk.nervos.org/t/spark-program-dular/10212/42) | xingtianchunyan | 2026-09-18 22:24:55 CST | Hi @duongja , The final payment has been issued. Transaction hash: 0x30bc50ce75052d3a04565b476366eebd96f61f011bdce48e18b8223b977a932b I also need to inform you that, due to my oversight, I forgot that the third payment was made from a personal wallet, so an additional 400,584...
- `S03` [Spark Program | Dular](https://talk.nervos.org/t/spark-program-dular/10212/43) | xingtianchunyan | 2026-09-18 22:31:52 CST | Spark Program | Dular —— 结项报告 1 结项评价 / Final Evaluation 完成日期 / Completion Date：2026-09-17 1.1 评价摘要 / Evaluation Summary Dular 在星火计划资助周期内完成了从"移动货币场景的稳定币钱包"概念到真实用户试点的完整闭环。开发者 duongja 以 Fiber Network 为结算层，先后交付了手机号身份注册与 OTP 验证系统、公开的 phone → Fiber pubkey 查询 API、基于 Safaricom Daraja...
- `S04` [Spark Program | CKB Builder Lab: Interactive Developer Onboarding Infrastructure for the CKB Ecosystem](https://talk.nervos.org/t/spark-program-ckb-builder-lab-interactive-developer-onboarding-infrastructure-for-the-ckb-ecosystem/10385/31) | xingtianchunyan | 2026-09-18 22:23:25 CST | Spark Program｜CKB Builder Lab – 结项报告 1. 结项评价 / Final Evaluation 完成日期 / Completion Date：2025年9月11日 1.1 评价摘要 / Evaluation Summary： CKB Builder Lab 是一个面向 CKB 生态的交互式开发者入门基础设施，通过浏览器端的 Cell 模型模拟器和自动验证的挑战系统，帮助开发者无需配置钱包、节点或环境即可理解 CKB 的核心架构概念。项目在约 10 周内（2025年7月1日 ~ 2025年9月中旬）完成了 MVP...
- `S05` [Spark Program | CKB Wallet Behaviour Intelligence](https://talk.nervos.org/t/spark-program-ckb-wallet-behaviour-intelligence/10338/24) | xingtianchunyan | 2026-09-18 22:21:37 CST | Hi @mulinya, After reviewing the latest developments, the committee acknowledges the engineering value of the work you have completed to date, while also understanding why the original objectives were not fully achieved. To better present your achievements to the community and...
- `S06` [RWAs and Lending on CKB](https://talk.nervos.org/t/rwas-and-lending-on-ckb/10718/1) | SalmanDev | 2026-09-18 20:34:09 CST | I’m exploring what it takes to lend against a real-world asset claim natively on CKB with no bridge, or external custody dependency. RWA lending is particularly interesting to me because, unlike a lot of DeFi primitives, it has an actual multi-year track record in production,...
- `S07` [TeamCKB Dev Log (Updated: Sep 16, 2026)](https://talk.nervos.org/t/teamckb-dev-log-updated-sep-16-2026/8572/41) | CKBdev | 2026-09-18 12:06:34 CST | Updates This cycle (August 19 – September 15, 2026) focused on node and light-client hardening, CKB-VM maintenance, and continued work on the next tx-pool, storage, and networking architecture. Key milestones include: CKB-VM v0.24.15 was released, followed by additional...
- `S08` [[RFC & Research] Automated Channel Liquidity Rebalancing on Fiber Network](https://talk.nervos.org/t/rfc-research-automated-channel-liquidity-rebalancing-on-fiber-network/10691/4) | zz_tovarishch | 2026-09-18 08:52:51 CST | Hi ILE_LABS, I think it would be better if @quake and his team answered these questions. They’ll probably have more accurate information.

## 活跃话题

1. [Spark Program | NNCBN - Nervos Network Community Boot Nodes](https://talk.nervos.org/t/spark-program-nncbn-nervos-network-community-boot-nodes/10653) | 1 条近窗帖子 | 最新活动 2026-09-18 22:37:19 CST | tags: In-Progress, Node, Spark-Program, bootnode
2. [Spark Program | Dular](https://talk.nervos.org/t/spark-program-dular/10212) | 2 条近窗帖子 | 最新活动 2026-09-18 22:31:52 CST | tags: In-Progress, Spark-Program, lang-en
3. [Spark Program | CKB Builder Lab: Interactive Developer Onboarding Infrastructure for the CKB Ecosystem](https://talk.nervos.org/t/spark-program-ckb-builder-lab-interactive-developer-onboarding-infrastructure-for-the-ckb-ecosystem/10385) | 1 条近窗帖子 | 最新活动 2026-09-18 22:23:25 CST | tags: In-Progress
4. [Spark Program | CKB Wallet Behaviour Intelligence](https://talk.nervos.org/t/spark-program-ckb-wallet-behaviour-intelligence/10338) | 1 条近窗帖子 | 最新活动 2026-09-18 22:21:37 CST | tags: In-Progress
5. [RWAs and Lending on CKB](https://talk.nervos.org/t/rwas-and-lending-on-ckb/10718) | 1 条近窗帖子 | 最新活动 2026-09-18 20:34:09 CST
6. [TeamCKB Dev Log (Updated: Sep 16, 2026)](https://talk.nervos.org/t/teamckb-dev-log-updated-sep-16-2026/8572) | 1 条近窗帖子 | 最新活动 2026-09-18 12:06:34 CST | tags: CKB, CKB-VM, lang-en
7. [[RFC & Research] Automated Channel Liquidity Rebalancing on Fiber Network](https://talk.nervos.org/t/rfc-research-automated-channel-liquidity-rebalancing-on-fiber-network/10691) | 1 条近窗帖子 | 最新活动 2026-09-18 08:52:51 CST

## 最近帖子摘录

- 2026-09-18 22:37:19 CST | xingtianchunyan | [Spark Program | NNCBN - Nervos Network Community Boot Nodes](https://talk.nervos.org/t/spark-program-nncbn-nervos-network-community-boot-nodes/10653/9) | Hello @NNCBN , We noticed that your first-week progress update has not yet been completed, so we are reaching out to learn about the latest developments with your project. First...
- 2026-09-18 22:31:52 CST | xingtianchunyan | [Spark Program | Dular](https://talk.nervos.org/t/spark-program-dular/10212/43) | Spark Program | Dular —— 结项报告 1 结项评价 / Final Evaluation 完成日期 / Completion Date：2026-09-17 1.1 评价摘要 / Evaluation Summary Dular 在星火计划资助周期内完成了从"移动货币场景的稳定币钱包"概念到真实用户试点的完整闭环。开发者...
- 2026-09-18 22:24:55 CST | xingtianchunyan | [Spark Program | Dular](https://talk.nervos.org/t/spark-program-dular/10212/42) | Hi @duongja , The final payment has been issued. Transaction hash: 0x30bc50ce75052d3a04565b476366eebd96f61f011bdce48e18b8223b977a932b I also need to inform you that, due to my...
- 2026-09-18 22:23:25 CST | xingtianchunyan | [Spark Program | CKB Builder Lab: Interactive Developer Onboarding Infrastructure for the CKB Ecosystem](https://talk.nervos.org/t/spark-program-ckb-builder-lab-interactive-developer-onboarding-infrastructure-for-the-ckb-ecosystem/10385/31) | Spark Program｜CKB Builder Lab – 结项报告 1. 结项评价 / Final Evaluation 完成日期 / Completion Date：2025年9月11日 1.1 评价摘要 / Evaluation Summary： CKB Builder Lab 是一个面向 CKB...
- 2026-09-18 22:21:37 CST | xingtianchunyan | [Spark Program | CKB Wallet Behaviour Intelligence](https://talk.nervos.org/t/spark-program-ckb-wallet-behaviour-intelligence/10338/24) | Hi @mulinya, After reviewing the latest developments, the committee acknowledges the engineering value of the work you have completed to date, while also understanding why the...
- 2026-09-18 20:34:09 CST | SalmanDev | [RWAs and Lending on CKB](https://talk.nervos.org/t/rwas-and-lending-on-ckb/10718/1) | I’m exploring what it takes to lend against a real-world asset claim natively on CKB with no bridge, or external custody dependency. RWA lending is particularly interesting to...
- 2026-09-18 12:06:34 CST | CKBdev | [TeamCKB Dev Log (Updated: Sep 16, 2026)](https://talk.nervos.org/t/teamckb-dev-log-updated-sep-16-2026/8572/41) | Updates This cycle (August 19 – September 15, 2026) focused on node and light-client hardening, CKB-VM maintenance, and continued work on the next tx-pool, storage, and...
- 2026-09-18 08:52:51 CST | zz_tovarishch | [[RFC & Research] Automated Channel Liquidity Rebalancing on Fiber Network](https://talk.nervos.org/t/rfc-research-automated-channel-liquidity-rebalancing-on-fiber-network/10691/4) | Hi ILE_LABS, I think it would be better if @quake and his team answered these questions. They’ll probably have more accurate information.
