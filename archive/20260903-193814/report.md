# Nervos Talk 社区简报

- 统计窗口: 2026-09-03 03:38:14 CST 到 2026-09-04 03:38:14 CST
- 生成时间: 2026-09-04 03:38:18 CST
- 话题数: 5
- 帖子数: 6
- 作者数: 6
- 总结模式: ai:openai-compatible

## 社区总结

## 今日发生了什么

过去 24 小时里，Nervos Talk 最集中的动态来自 Spark Program 项目的密集更新：一方面，FiberPass 提案在提交委员会前经历了一轮个人反馈与预算修改，即将进入下一步评审 [S05, S06]；另一方面，CKB Builder Lab 表示整个流程正在收尾，预计下周完成 [S02]。此外，Dular 项目自曝在内部流程结束后才发现交易证据未保存的问题 [S03]，而社区还出现了关于 CKB 移动端 SDK 的新提案 [S01]。

## 重点话题

- **FiberPass 提案评审前互动**：社区成员 xingtianchunyan 在提交委员会前给出个人反馈，主要围绕提案范围提出意见 [S05]；项目方随后回应已对预算做了拆分调整，把 $1,500 分为基础设施与三个阶段开发费用 [S06]。这是今天唯一一组有来有回的提案讨论 [S05, S06]。

- **CKB Builder Lab 预告下周收尾**：devnash 在进度帖中回复称，目前正在完成整个流程的收尾工作，预计下周可以全部做完 [S02]。

- **Dular 项目自曝交易证据保存缺陷**：Dular 团队回应社区质询时承认，内部系统在流程完成后没有保存交易证据，而且这个问题直到整个流程结束后才发现，帖子暂未完整说明成因与影响范围 [S03]。

- **新提案：CKB-Mobile-Core**：sublime247 发布了一个面向 iOS 与 Android 的轻量原生 SDK 提案，目标是降低在 Nervos 上开发原生移动应用的门槛，核心方向包括本地加密签名、Molecule 数据序列化等 [S01]。该提案目前还处于早期介绍阶段 [S01]。

- **Proof of Buy 技术讨论继续深入**：中文技术帖继续讨论 Layer2 共识中来自项目方的“女巫攻击”风险 [S04]。帖子指出，VRF 随机机制可以避免出块权仅由 L1 token 支付数量决定，但并不能解决项目方利用自己在 L1 的出块优势亲自下场垄断出块权的问题 [S04]。

## 值得继续跟进

- **Dular 的交易证据保存问题**：这是 Spark 项目验收流程中比较敏感的缺陷，后续需要关注团队是否会公开问题的具体原因以及补救措施 [S03]。

- **FiberPass 提案的委员会评审结果**：提案已经按反馈调整预算，下一步要看委员会初审意见，以及评审是否会对技术范围提出新要求 [S05, S06]。

- **Proof of Buy 的项目方女巫攻击方案**：帖子目前只是把问题摆了出来，尚未给出完整解法，值得继续跟进作者后续如何设计反制方案 [S04]。

## 来源索引

- `S01` [CKB-Mobile-Core: Lightweight Native Mobile SDK for iOS & Android](https://talk.nervos.org/t/ckb-mobile-core-lightweight-native-mobile-sdk-for-ios-android/10683/1) | sublime247 | 2026-09-04 00:04:04 CST | CKB-Mobile-Core: Lightweight Native SDK for iOS & Android 1. Objective To eliminate developer friction when building native mobile applications on the Nervos Network. This lightweight SDK will handle local cryptographic signing, Molecule data serialization, and automated cell...
- `S02` [Spark Program | CKB Builder Lab: Interactive Developer Onboarding Infrastructure for the CKB Ecosystem](https://talk.nervos.org/t/spark-program-ckb-builder-lab-interactive-developer-onboarding-infrastructure-for-the-ckb-ecosystem/10385/27) | devnash | 2026-09-03 23:29:38 CST | Hey @xingtianchunyan, thank you for checking in on our latest progress. We’re currently wrapping up the entire process and expect to have everything completed by next week.
- `S03` [Spark Program | Dular](https://talk.nervos.org/t/spark-program-dular/10212/35) | duongja | 2026-09-03 18:51:38 CST | Hello @xingtianchunyan Thank you for reaching out, and apologies for the delayed reply. We recently identified an issue. Our internal systems were not saving the transaction evidence after completion. We only discovered this after the process had finished. It stemmed from our...
- `S04` [Proof of Buy，一种专为Layer1设计的Layer2共识](https://talk.nervos.org/t/proof-of-buy-layer1-layer2/9752/32) | Lawliet_Chan | 2026-09-03 18:14:52 CST | 来自项目方的女巫攻击 前面我们提到， proof of buy会让矿工们支付 L1 token到项目方的地址（以下简称mining addr)上，久而久之，为了防止项目方自己利用自己的 出块无成本的优势（因为矿工的token都是支付给他的）来自己亲自下场挖矿垄断出块权，我们设计了VRF这种伪随机的方式来让L2出块不会仅仅只受L1 token的支付数量的影响。 但有一个问题仍未解决，项目方可以利用自己的L1...
- `S05` [Spark Program | FiberPass: Spending Permission Infrastructure for Fiber Network](https://talk.nervos.org/t/spark-program-fiberpass-spending-permission-infrastructure-for-fiber-network/10679/2) | xingtianchunyan | 2026-09-03 12:54:14 CST | Hi @XBeach , great to see your new proposal! The following are my personal thoughts before submitting this proposal to the committee for review, for your reference. These views are based solely on my own understanding and do not represent the position of the committee. Scope...
- `S06` [Spark Program | FiberPass: Spending Permission Infrastructure for Fiber Network](https://talk.nervos.org/t/spark-program-fiberpass-spending-permission-infrastructure-for-fiber-network/10679/3) | XBeach | 2026-09-03 16:18:40 CST | Hi @xingtianchunyan Thanks for the feedback. Both points have been addressed: Budget: Section 7 now breaks down the full $1,500 — $430 infrastructure (Vercel Pro $150, Railway $200, domain $60, testnet $20) and $1,070 development across three milestones ($350, $350, $370)....

## 活跃话题

1. [CKB-Mobile-Core: Lightweight Native Mobile SDK for iOS & Android](https://talk.nervos.org/t/ckb-mobile-core-lightweight-native-mobile-sdk-for-ios-android/10683) | 1 条近窗帖子 | 最新活动 2026-09-04 00:04:04 CST | tags: CKB, dapp
2. [Spark Program | CKB Builder Lab: Interactive Developer Onboarding Infrastructure for the CKB Ecosystem](https://talk.nervos.org/t/spark-program-ckb-builder-lab-interactive-developer-onboarding-infrastructure-for-the-ckb-ecosystem/10385) | 1 条近窗帖子 | 最新活动 2026-09-03 23:29:38 CST | tags: In-Progress
3. [Spark Program | Dular](https://talk.nervos.org/t/spark-program-dular/10212) | 1 条近窗帖子 | 最新活动 2026-09-03 18:51:38 CST | tags: In-Progress, Spark-Program, lang-en
4. [Proof of Buy，一种专为Layer1设计的Layer2共识](https://talk.nervos.org/t/proof-of-buy-layer1-layer2/9752) | 1 条近窗帖子 | 最新活动 2026-09-03 18:14:52 CST | tags: lang-zh, 共识协议
5. [Spark Program | FiberPass: Spending Permission Infrastructure for Fiber Network](https://talk.nervos.org/t/spark-program-fiberpass-spending-permission-infrastructure-for-fiber-network/10679) | 2 条近窗帖子 | 最新活动 2026-09-03 16:18:40 CST | tags: CKB, fiber

## 最近帖子摘录

- 2026-09-04 00:04:04 CST | sublime247 | [CKB-Mobile-Core: Lightweight Native Mobile SDK for iOS & Android](https://talk.nervos.org/t/ckb-mobile-core-lightweight-native-mobile-sdk-for-ios-android/10683/1) | CKB-Mobile-Core: Lightweight Native SDK for iOS & Android 1. Objective To eliminate developer friction when building native mobile applications on the Nervos Network. This...
- 2026-09-03 23:29:38 CST | devnash | [Spark Program | CKB Builder Lab: Interactive Developer Onboarding Infrastructure for the CKB Ecosystem](https://talk.nervos.org/t/spark-program-ckb-builder-lab-interactive-developer-onboarding-infrastructure-for-the-ckb-ecosystem/10385/27) | Hey @xingtianchunyan, thank you for checking in on our latest progress. We’re currently wrapping up the entire process and expect to have everything completed by next week.
- 2026-09-03 18:51:38 CST | duongja | [Spark Program | Dular](https://talk.nervos.org/t/spark-program-dular/10212/35) | Hello @xingtianchunyan Thank you for reaching out, and apologies for the delayed reply. We recently identified an issue. Our internal systems were not saving the transaction...
- 2026-09-03 18:14:52 CST | Lawliet_Chan | [Proof of Buy，一种专为Layer1设计的Layer2共识](https://talk.nervos.org/t/proof-of-buy-layer1-layer2/9752/32) | 来自项目方的女巫攻击 前面我们提到， proof of buy会让矿工们支付 L1 token到项目方的地址（以下简称mining addr)上，久而久之，为了防止项目方自己利用自己的 出块无成本的优势（因为矿工的token都是支付给他的）来自己亲自下场挖矿垄断出块权，我们设计了VRF这种伪随机的方式来让L2出块不会仅仅只受L1...
- 2026-09-03 16:18:40 CST | XBeach | [Spark Program | FiberPass: Spending Permission Infrastructure for Fiber Network](https://talk.nervos.org/t/spark-program-fiberpass-spending-permission-infrastructure-for-fiber-network/10679/3) | Hi @xingtianchunyan Thanks for the feedback. Both points have been addressed: Budget: Section 7 now breaks down the full $1,500 — $430 infrastructure (Vercel Pro $150, Railway...
- 2026-09-03 12:54:14 CST | xingtianchunyan | [Spark Program | FiberPass: Spending Permission Infrastructure for Fiber Network](https://talk.nervos.org/t/spark-program-fiberpass-spending-permission-infrastructure-for-fiber-network/10679/2) | Hi @XBeach , great to see your new proposal! The following are my personal thoughts before submitting this proposal to the committee for review, for your reference. These views...
