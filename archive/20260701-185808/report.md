# Nervos Talk 社区简报

- 统计窗口: 2026-07-01 02:58:08 CST 到 2026-07-02 02:58:08 CST
- 生成时间: 2026-07-02 02:58:16 CST
- 话题数: 9
- 帖子数: 13
- 作者数: 11
- 总结模式: ai:openrouter

## 社区总结

## 今日发生了什么

今天 Nervos Talk 论坛活跃度中等，Spark Program 持续成为社区焦点，共有四个新项目或更新涌入：从 zk-Lock 零知识锁脚本到 VibeQuest AI 学习平台，开发者们正在 CKB 上探索多元方向 [S01, S03, S05, S06]。同时，Rosen Bridge CKB 集成的技术推进和 Open USD 稳定币的引入接洽，也为生态基础设施增添了看点 [S08, S12]。

## 重点话题

- **zk-Lock 零知识锁脚本登场**：Mulandi_Cecilia 发布了基于 Groth16 证明的可复用 CKB lock script，开发者可用 Circom 电路自定义解锁条件，为 CKB 带来更灵活的隐私与验证能力 [S01]。

- **VibeQuest 想把"氛围编程"变成真学习**：新项目提议用 AI 生成课程 + 实战任务 + 代码验证的方式，引导用户真正学会构建 CKB/Fiber 应用，而非只是复制粘贴 [S05]。

- **CKB Builder Lab 获社区反馈**：ArthurZhang 建议互动教程中应加入"故意破坏的反例"，让学习者识别协议不变量被违反的情况，以加深理解而非仅靠模仿 through [S04]。

- **CellScript AMM 预算调整**：WuodOdhis 回应审阅意见，将项目预算下调至 1,000 美元，承认这主要是技术开发工作 [S06]。

- **PactAgent  builder 将办 Reddit AMA**：7 月 7 日与从零学习 CKB cell 模型到建成合约的前端开发者 Oluwaseun 对话，新手成长路径值得关注 [S07]。

## 值得继续跟进

- **Open USD 接洽进展**：社区成员已主动联系，但 CKB 是否具备足够吸引力说服该联盟入驻仍需观察，matt_ckb 的"unrivaled potential"更多是信心表态而非实证 [S12]。

- **Rosen Bridge 集成落地节奏**：phroi 表示开发正在进行但验证繁琐，"slow and methodic process"意味着短期可能难有里程碑式更新 [S08]。

- **稳定币替代真空**：USDI 停用后，除 Open USD 探索外尚未见其他具体替代方案在讨论中浮现，若接洽受阻生态支付场景可能承压 [S11, S13]。

## 来源索引

- `S01` [Spark Program | zk-Lock for CKB](https://talk.nervos.org/t/spark-program-zk-lock-for-ckb/10448/1) | Mulandi_Cecilia | 2026-07-01 23:52:19 CST | 1. Project overview and positioning / 项目概述与定位 zk-Lock is a reusable CKB lock script that conditions cell spending on a valid Groth16 proof. Any developer can write a Circom circuit, commit to its verifying key, and lock CKB cells behind it; to spend the cell, the spender...
- `S02` [DOB Pattern Studio Spark Program |](https://talk.nervos.org/t/dob-pattern-studio-spark-program/10428/3) | Frank | 2026-07-01 23:14:14 CST | Hi @xingtianchunyan, Thanks so much for the detailed feedback — really appreciate you taking the time before formal review. Here are my responses: 1. Proposal formatting Updated — the title now starts with “Spark Program | [your project name]”. I’ve also cleaned up the...
- `S03` [Spark Program | CKB Builder Lab: Interactive Developer Onboarding Infrastructure for the CKB Ecosystem](https://talk.nervos.org/t/spark-program-ckb-builder-lab-interactive-developer-onboarding-infrastructure-for-the-ckb-ecosystem/10385/7) | devnash | 2026-07-01 19:21:31 CST | Thanks Received
- `S04` [Spark Program | CKB Builder Lab: Interactive Developer Onboarding Infrastructure for the CKB Ecosystem](https://talk.nervos.org/t/spark-program-ckb-builder-lab-interactive-developer-onboarding-infrastructure-for-the-ckb-ecosystem/10385/8) | ArthurZhang | 2026-07-01 22:56:54 CST | interesting direction, this kind of reminds me a bit of how Vulcans train children. one suggestion though, maybe each quest should include a deliberately broken counterfactual case where the learner has to identify which protocol invariant was violated, so it does not risk...
- `S05` [Spark Program | VibeQuest: Turning AI-Assisted Coding Into Real Learning](https://talk.nervos.org/t/spark-program-vibequest-turning-ai-assisted-coding-into-real-learning/10446/1) | XBeach | 2026-07-01 20:06:49 CST | 1. Project Overview Project Name: VibeQuest One-Sentence Summary: VibeQuest turns vibe-coding into real learning by guiding users through AI-generated lessons, practical quests, code verification, and proof-of-understanding challenges so they can build CKB/Fiber applications...
- `S06` [Spark Program | CellScript AMM Transaction Builder](https://talk.nervos.org/t/spark-program-cellscript-amm-transaction-builder/10431/5) | WuodOdhis | 2026-07-01 19:40:28 CST | Hi @xingtianchunyan, thank you for the careful review and for the helpful comments. I agree with the points raised, and I will adjust the proposal accordingly. 1. Budget I will revise the requested budget to $1,000. You are right that this is primarily a technical development...
- `S07` [Reddit AMA with PactAgent Builder Oluwaseun – July 7](https://talk.nervos.org/t/reddit-ama-with-pactagent-builder-oluwaseun-july-7/10442/1) | JackyLHH | 2026-07-01 14:30:51 CST | the-pact-agent-ama1920×2213 1.11 MB Hello CKB community, Our next Reddit AMA is with Oluwaseun (@Ajay), a frontend/blockchain developer who started his blockchain journey on CKB with zero prior experience. He learned the cell model from scratch, built his first contract,...
- `S08` [[DIS] CKB Integration for Rosen Bridge](https://talk.nervos.org/t/dis-ckb-integration-for-rosen-bridge/9756/144) | phroi | 2026-07-01 11:08:33 CST | Implementation is actively on-going! Nowadays coding is fast, but making sure that everything works as it should is a bit trickier. So ultimately it’s a slow and methodic process. I feel lucky that I can compare my solutions with other integrations, just CKB flexibility &...
- `S09` [[DIS] FiberLatch Access - Open-Source Access Control for Fiber Payments](https://talk.nervos.org/t/dis-fiberlatch-access-open-source-access-control-for-fiber-payments/10414/2) | Ticoworld | 2026-07-01 08:14:32 CST | (post deleted by author)
- `S10` [[DIS] FiberLatch Access - Open-Source Access Control for Fiber Payments](https://talk.nervos.org/t/dis-fiberlatch-access-open-source-access-control-for-fiber-payments/10414/3) | Ticoworld | 2026-07-01 08:17:33 CST | If you are a DAO member please vote for me https://dao.ckb.community/landing?method=share&thread=vot-fiberlatch-access-open-source-access-control-for-fiber-payments-74170
- `S11` [USDI on CKB will be discontinued. Any alternative for stablecoin?](https://talk.nervos.org/t/usdi-on-ckb-will-be-discontinued-any-alternative-for-stablecoin/10417/14) | ebdalezyz_aljhny | 2026-07-01 05:42:57 CST | That sounds great, but does CKB currently have anything compelling enough to attract a consortium like this?
- `S12` [USDI on CKB will be discontinued. Any alternative for stablecoin?](https://talk.nervos.org/t/usdi-on-ckb-will-be-discontinued-any-alternative-for-stablecoin/10417/15) | matt_ckb | 2026-07-01 06:31:27 CST | CDEX: Will we try to engage with Open USD or explore bringing it to CKB? Yes, @zz_tovarishch has already reached out. ebdalezyz_aljhny: does CKB currently have anything compelling enough to attract a consortium like this unrivaled potential : D
- `S13` [USDI on CKB will be discontinued. Any alternative for stablecoin?](https://talk.nervos.org/t/usdi-on-ckb-will-be-discontinued-any-alternative-for-stablecoin/10417/16) | ebdalezyz_aljhny | 2026-07-01 06:53:37 CST | That’s great. Hopefully, the initial contact will make it easier to get them interested in CKB.

## 活跃话题

1. [Spark Program | zk-Lock for CKB](https://talk.nervos.org/t/spark-program-zk-lock-for-ckb/10448) | 1 条近窗帖子 | 最新活动 2026-07-01 23:52:19 CST | tags: Grant
2. [DOB Pattern Studio Spark Program |](https://talk.nervos.org/t/dob-pattern-studio-spark-program/10428) | 1 条近窗帖子 | 最新活动 2026-07-01 23:14:14 CST | tags: Spark-Program
3. [Spark Program | CKB Builder Lab: Interactive Developer Onboarding Infrastructure for the CKB Ecosystem](https://talk.nervos.org/t/spark-program-ckb-builder-lab-interactive-developer-onboarding-infrastructure-for-the-ckb-ecosystem/10385) | 2 条近窗帖子 | 最新活动 2026-07-01 22:56:54 CST | tags: In-Progress, Spark-Program
4. [Spark Program | VibeQuest: Turning AI-Assisted Coding Into Real Learning](https://talk.nervos.org/t/spark-program-vibequest-turning-ai-assisted-coding-into-real-learning/10446) | 1 条近窗帖子 | 最新活动 2026-07-01 20:06:49 CST | tags: Spark-Program
5. [Spark Program | CellScript AMM Transaction Builder](https://talk.nervos.org/t/spark-program-cellscript-amm-transaction-builder/10431) | 1 条近窗帖子 | 最新活动 2026-07-01 19:40:28 CST | tags: Spark-Program
6. [Reddit AMA with PactAgent Builder Oluwaseun – July 7](https://talk.nervos.org/t/reddit-ama-with-pactagent-builder-oluwaseun-july-7/10442) | 1 条近窗帖子 | 最新活动 2026-07-01 14:30:51 CST | tags: AMA
7. [[DIS] CKB Integration for Rosen Bridge](https://talk.nervos.org/t/dis-ckb-integration-for-rosen-bridge/9756) | 1 条近窗帖子 | 最新活动 2026-07-01 11:08:33 CST
8. [[DIS] FiberLatch Access - Open-Source Access Control for Fiber Payments](https://talk.nervos.org/t/dis-fiberlatch-access-open-source-access-control-for-fiber-payments/10414) | 2 条近窗帖子 | 最新活动 2026-07-01 08:17:33 CST | tags: CKB, dapp, testnet
9. [USDI on CKB will be discontinued. Any alternative for stablecoin?](https://talk.nervos.org/t/usdi-on-ckb-will-be-discontinued-any-alternative-for-stablecoin/10417) | 3 条近窗帖子 | 最新活动 2026-07-01 06:53:37 CST | tags: Nervos-项目动态

## 最近帖子摘录

- 2026-07-01 23:52:19 CST | Mulandi_Cecilia | [Spark Program | zk-Lock for CKB](https://talk.nervos.org/t/spark-program-zk-lock-for-ckb/10448/1) | 1. Project overview and positioning / 项目概述与定位 zk-Lock is a reusable CKB lock script that conditions cell spending on a valid Groth16 proof. Any developer can write a Circom...
- 2026-07-01 23:14:14 CST | Frank | [DOB Pattern Studio Spark Program |](https://talk.nervos.org/t/dob-pattern-studio-spark-program/10428/3) | Hi @xingtianchunyan, Thanks so much for the detailed feedback — really appreciate you taking the time before formal review. Here are my responses: 1. Proposal formatting Updated...
- 2026-07-01 22:56:54 CST | ArthurZhang | [Spark Program | CKB Builder Lab: Interactive Developer Onboarding Infrastructure for the CKB Ecosystem](https://talk.nervos.org/t/spark-program-ckb-builder-lab-interactive-developer-onboarding-infrastructure-for-the-ckb-ecosystem/10385/8) | interesting direction, this kind of reminds me a bit of how Vulcans train children. one suggestion though, maybe each quest should include a deliberately broken counterfactual...
- 2026-07-01 20:06:49 CST | XBeach | [Spark Program | VibeQuest: Turning AI-Assisted Coding Into Real Learning](https://talk.nervos.org/t/spark-program-vibequest-turning-ai-assisted-coding-into-real-learning/10446/1) | 1. Project Overview Project Name: VibeQuest One-Sentence Summary: VibeQuest turns vibe-coding into real learning by guiding users through AI-generated lessons, practical quests,...
- 2026-07-01 19:40:28 CST | WuodOdhis | [Spark Program | CellScript AMM Transaction Builder](https://talk.nervos.org/t/spark-program-cellscript-amm-transaction-builder/10431/5) | Hi @xingtianchunyan, thank you for the careful review and for the helpful comments. I agree with the points raised, and I will adjust the proposal accordingly. 1. Budget I will...
- 2026-07-01 19:21:31 CST | devnash | [Spark Program | CKB Builder Lab: Interactive Developer Onboarding Infrastructure for the CKB Ecosystem](https://talk.nervos.org/t/spark-program-ckb-builder-lab-interactive-developer-onboarding-infrastructure-for-the-ckb-ecosystem/10385/7) | Thanks Received
- 2026-07-01 14:30:51 CST | JackyLHH | [Reddit AMA with PactAgent Builder Oluwaseun – July 7](https://talk.nervos.org/t/reddit-ama-with-pactagent-builder-oluwaseun-july-7/10442/1) | the-pact-agent-ama1920×2213 1.11 MB Hello CKB community, Our next Reddit AMA is with Oluwaseun (@Ajay), a frontend/blockchain developer who started his blockchain journey on CKB...
- 2026-07-01 11:08:33 CST | phroi | [[DIS] CKB Integration for Rosen Bridge](https://talk.nervos.org/t/dis-ckb-integration-for-rosen-bridge/9756/144) | Implementation is actively on-going! Nowadays coding is fast, but making sure that everything works as it should is a bit trickier. So ultimately it’s a slow and methodic...
- 2026-07-01 08:17:33 CST | Ticoworld | [[DIS] FiberLatch Access - Open-Source Access Control for Fiber Payments](https://talk.nervos.org/t/dis-fiberlatch-access-open-source-access-control-for-fiber-payments/10414/3) | If you are a DAO member please vote for me https://dao.ckb.community/landing?method=share&thread=vot-fiberlatch-access-open-source-access-control-for-fiber-payments-74170
- 2026-07-01 08:14:32 CST | Ticoworld | [[DIS] FiberLatch Access - Open-Source Access Control for Fiber Payments](https://talk.nervos.org/t/dis-fiberlatch-access-open-source-access-control-for-fiber-payments/10414/2) | (post deleted by author)
- 2026-07-01 06:53:37 CST | ebdalezyz_aljhny | [USDI on CKB will be discontinued. Any alternative for stablecoin?](https://talk.nervos.org/t/usdi-on-ckb-will-be-discontinued-any-alternative-for-stablecoin/10417/16) | That’s great. Hopefully, the initial contact will make it easier to get them interested in CKB.
- 2026-07-01 06:31:27 CST | matt_ckb | [USDI on CKB will be discontinued. Any alternative for stablecoin?](https://talk.nervos.org/t/usdi-on-ckb-will-be-discontinued-any-alternative-for-stablecoin/10417/15) | CDEX: Will we try to engage with Open USD or explore bringing it to CKB? Yes, @zz_tovarishch has already reached out. ebdalezyz_aljhny: does CKB currently have anything...
- 2026-07-01 05:42:57 CST | ebdalezyz_aljhny | [USDI on CKB will be discontinued. Any alternative for stablecoin?](https://talk.nervos.org/t/usdi-on-ckb-will-be-discontinued-any-alternative-for-stablecoin/10417/14) | That sounds great, but does CKB currently have anything compelling enough to attract a consortium like this?
