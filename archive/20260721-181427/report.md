# Nervos Talk 社区简报

- 统计窗口: 2026-07-21 02:14:27 CST 到 2026-07-22 02:14:27 CST
- 生成时间: 2026-07-22 02:14:37 CST
- 话题数: 10
- 帖子数: 16
- 作者数: 13
- 总结模式: ai:openrouter

## 社区总结

## 今日发生了什么

今天 Nervos Talk 以生态建设节奏为主，多个 Spark 资助项目出现流程跟进与沟通，同时社区出现一篇关于 CKB-VM 安全扩展的技术长文，以及一项将 CKB 支付接入 Apple/Google Wallet 的新提案。[S02, S06, S10, S15]

## 重点话题

- **zk-Lock 与 JoyID 失败解析两个 Spark 申请被"复活"**：管理员 zz_tovarishch 向申请人解释，他们的提案此前因格式筛选未识别而错过评审，又被论坛改版的 AI 误移入 Archive 区，现已手动迁回 Spark 子区并安排尽快评审。[S02, S12]

- **CellMint 无代码平台回应委员会反馈**：申请人 Kashlynne_Mumbe 更新提案，重点区分了 CellMint 与现有 CCC xUDT 发行工具的差异，并调整了架构以更多采用链上方案。[S07]

- **CKB Anywhere Card V2 亮相**：BuildUnion 发布新版提案，核心变化是改为原生移动端钱包支持，并简化体验为移动优先设计，回应了此前社区反馈。[S06]

- **Fiber 子marine Swap 新提案上线**：George_Liam 提交 Spark 申请，计划为 Fiber Network 实现子marine swap 的测试网版本，以解决新用户入站流动性不足的问题。[S10]

- **CKB-VM CFI 扩展深度技术文**：mohanson 发文解析控制流完整性（CFI）扩展原理，但明确强调该功能仍处于设计开发阶段，尚未正式支持。[S15]

## 值得继续跟进

- **Spark 流程摩擦**：近期多起"格式筛选漏过+AI 误归档"案例暴露资助流程的自动化环节有漏洞，需观察是否会有系统性修复，避免更多申请被延误。[S02, S12]

- **CellMint 差异化能否说服委员会**：项目方虽回应了与 CCC xUDT 工具的差异化问题，但委员会是否认可其独立价值，下周评审结果值得留意。[S07]

- **CKB Anywhere Card 落地可行性**：V2 转向移动原生是正确方向，但 Apple/Google Wallet 的合规与集成复杂度在提案中尚未充分展开，后续技术细节披露需要关注。[S06]

## 来源索引

- `S01` [Spark Program | zk-Lock for CKB](https://talk.nervos.org/t/spark-program-zk-lock-for-ckb/10448/2) | zz_tovarishch | 2026-07-22 00:36:30 CST | 
- `S02` [Spark Program | zk-Lock for CKB](https://talk.nervos.org/t/spark-program-zk-lock-for-ckb/10448/3) | zz_tovarishch | 2026-07-22 00:37:56 CST | Hi @Mulandi_Cecilia 您的申请之前不知道是因为什么原因，没有被我们的格式筛选识别，进而没有进入每周的评审会，后来又因为论坛改版的AI移到了Archive区域 目前已经引动到Spark的子区，会尽快进入评审，感谢您的理解
- `S03` [Ckb,eth ,btc,others](https://talk.nervos.org/t/ckb-eth-btc-others/10517/1) | ckbbkc | 2026-07-21 18:32:51 CST | If BTC and ETH both face difficulties in becoming quantum resistant, how can CKB help BTC and ETH holders?
- `S04` [Ckb,eth ,btc,others](https://talk.nervos.org/t/ckb-eth-btc-others/10517/2) | silenceport | 2026-07-21 21:18:48 CST | Just sell btc and eth and purchase ckb
- `S05` [Ckb,eth ,btc,others](https://talk.nervos.org/t/ckb-eth-btc-others/10517/3) | matt_ckb | 2026-07-21 23:09:29 CST | i don’t think it can, each has their own challenges.
- `S06` [[DIS] CKB Anywhere Card: Apple Wallet & Google Wallet Payments for Nervos](https://talk.nervos.org/t/dis-ckb-anywhere-card-apple-wallet-google-wallet-payments-for-nervos/10522/1) | BuildUnion | 2026-07-21 21:07:57 CST | TL;DR What’s New in V2 Thank you to everyone who supported and provided feedback on the original proposal. The feedback was clear: while the core concept was well received, the solution needed native mobile wallet support and a simpler, mobile-first user experience. Over the...
- `S07` [Spark Program | CellMint, No-Code Token Creation & Management Platform for Nervos CKB](https://talk.nervos.org/t/spark-program-cellmint-no-code-token-creation-management-platform-for-nervos-ckb/10483/4) | Kashlynne_Mumbe | 2026-07-21 19:04:17 CST | Hi @xingtianchunyan Thank you to the committee for the detailed feedback and thoughtful review. I’ve updated the proposal to address the points raised by clearly differentiating CellMint from the existing CCC xUDT issuance tool and revising the architecture to use on-chain...
- `S08` [Spark Program | CellMint, No-Code Token Creation & Management Platform for Nervos CKB](https://talk.nervos.org/t/spark-program-cellmint-no-code-token-creation-management-platform-for-nervos-ckb/10483/5) | discourse_ai_spam | 2026-07-21 19:46:26 CST | 
- `S09` [Spark Program | CellMint, No-Code Token Creation & Management Platform for Nervos CKB](https://talk.nervos.org/t/spark-program-cellmint-no-code-token-creation-management-platform-for-nervos-ckb/10483/6) | system | 2026-07-21 20:24:49 CST | 
- `S10` [Spark Program | Fiber Submarine Swap Service](https://talk.nervos.org/t/spark-program-fiber-submarine-swap-service/10516/1) | George_Liam | 2026-07-21 17:19:18 CST | Spark Program | Fiber Submarine Swap Service Project Name Fiber Submarine Swap Service — A working testnet implementation of a submarine swap for the Fiber Network, solving the inbound liquidity problem that prevents new users from receiving payments on Fiber. Team /...
- `S11` [Spark Program | CKB Builder Lab: Interactive Developer Onboarding Infrastructure for the CKB Ecosystem](https://talk.nervos.org/t/spark-program-ckb-builder-lab-interactive-developer-onboarding-infrastructure-for-the-ckb-ecosystem/10385/14) | devnash | 2026-07-21 16:33:50 CST | Hi @xingtianchunyan, Thank you for the detailed feedback and the time the committee has taken to review our progress. I appreciate both points and I’m already working on addressing them. In the next weekly submission, I’ll include: A clearer demo video that properly showcases...
- `S12` [Spark Program | ckb-joyid-failure-explainer](https://talk.nervos.org/t/spark-program-ckb-joyid-failure-explainer/10426/2) | zz_tovarishch | 2026-07-21 15:13:53 CST | Hi @Crackdevs 您的申请之前不知道是因为什么原因，没有被我们的格式筛选识别，进而没有进入每周的评审会，后来又因为论坛改版的AI移到了Archive区域 目前已经引动到Spark的子区，会尽快进入评审，感谢您的理解
- `S13` [Spark Program | ckb-joyid-failure-explainer](https://talk.nervos.org/t/spark-program-ckb-joyid-failure-explainer/10426/3) | zz_tovarishch | 2026-07-21 15:13:59 CST | 
- `S14` [CKB Ecosystem Biweekly Update](https://talk.nervos.org/t/ckb-ecosystem-biweekly-update/9821/23) | Crackdevs | 2026-07-21 14:21:31 CST | HI @zz_tovarishch , we wanted to follow up on our grant application and know the next step moving forward. Thank you.
- `S15` [Deep Dive Into CKB-VM CFI Extension](https://talk.nervos.org/t/deep-dive-into-ckb-vm-cfi-extension/10515/1) | mohanson | 2026-07-21 11:26:30 CST | It should be emphasized that CKB-VM does not currently officially support the CFI extension instruction set; related functionality is still in the design and development stage. This article aims to illustrate the principles and impact of ROP attacks, as well as the basic...
- `S16` [Spark Program Proposal: Cell Model Documentation Hub](https://talk.nervos.org/t/spark-program-proposal-cell-model-documentation-hub/10514/1) | WuodOdhis | 2026-07-21 05:48:34 CST | 1.Team Profile & Contact Applicant: WuodOdhis GitHub: github.com/WuodOdhis Role: Full-stack developer with experience in blockchain development, CKBuilders program participant, and active contributor to CKB developer education Telegram: @Cyborgsil Discord: alchemist_3970 2....

## 活跃话题

1. [Spark Program | zk-Lock for CKB](https://talk.nervos.org/t/spark-program-zk-lock-for-ckb/10448) | 2 条近窗帖子 | 最新活动 2026-07-22 00:37:56 CST
2. [Ckb,eth ,btc,others](https://talk.nervos.org/t/ckb-eth-btc-others/10517) | 3 条近窗帖子 | 最新活动 2026-07-21 23:09:29 CST
3. [[DIS] CKB Anywhere Card: Apple Wallet & Google Wallet Payments for Nervos](https://talk.nervos.org/t/dis-ckb-anywhere-card-apple-wallet-google-wallet-payments-for-nervos/10522) | 1 条近窗帖子 | 最新活动 2026-07-21 21:07:57 CST
4. [Spark Program | CellMint, No-Code Token Creation & Management Platform for Nervos CKB](https://talk.nervos.org/t/spark-program-cellmint-no-code-token-creation-management-platform-for-nervos-ckb/10483) | 3 条近窗帖子 | 最新活动 2026-07-21 20:24:49 CST | tags: Pending
5. [Spark Program | Fiber Submarine Swap Service](https://talk.nervos.org/t/spark-program-fiber-submarine-swap-service/10516) | 1 条近窗帖子 | 最新活动 2026-07-21 17:19:18 CST | tags: Spark-Program
6. [Spark Program | CKB Builder Lab: Interactive Developer Onboarding Infrastructure for the CKB Ecosystem](https://talk.nervos.org/t/spark-program-ckb-builder-lab-interactive-developer-onboarding-infrastructure-for-the-ckb-ecosystem/10385) | 1 条近窗帖子 | 最新活动 2026-07-21 16:33:50 CST | tags: In-Progress, Spark-Program, lang-en
7. [Spark Program | ckb-joyid-failure-explainer](https://talk.nervos.org/t/spark-program-ckb-joyid-failure-explainer/10426) | 2 条近窗帖子 | 最新活动 2026-07-21 15:13:59 CST | tags: Grant, Submitted, lang-en
8. [CKB Ecosystem Biweekly Update](https://talk.nervos.org/t/ckb-ecosystem-biweekly-update/9821) | 1 条近窗帖子 | 最新活动 2026-07-21 14:21:31 CST | tags: Ecosystem-Update, lang-en
9. [Deep Dive Into CKB-VM CFI Extension](https://talk.nervos.org/t/deep-dive-into-ckb-vm-cfi-extension/10515) | 1 条近窗帖子 | 最新活动 2026-07-21 11:26:30 CST | tags: CKB-VM
10. [Spark Program Proposal: Cell Model Documentation Hub](https://talk.nervos.org/t/spark-program-proposal-cell-model-documentation-hub/10514) | 1 条近窗帖子 | 最新活动 2026-07-21 05:48:34 CST | tags: Submitted

## 最近帖子摘录

- 2026-07-22 00:37:56 CST | zz_tovarishch | [Spark Program | zk-Lock for CKB](https://talk.nervos.org/t/spark-program-zk-lock-for-ckb/10448/3) | Hi @Mulandi_Cecilia 您的申请之前不知道是因为什么原因，没有被我们的格式筛选识别，进而没有进入每周的评审会，后来又因为论坛改版的AI移到了Archive区域 目前已经引动到Spark的子区，会尽快进入评审，感谢您的理解
- 2026-07-22 00:36:30 CST | zz_tovarishch | [Spark Program | zk-Lock for CKB](https://talk.nervos.org/t/spark-program-zk-lock-for-ckb/10448/2) | 
- 2026-07-21 23:09:29 CST | matt_ckb | [Ckb,eth ,btc,others](https://talk.nervos.org/t/ckb-eth-btc-others/10517/3) | i don’t think it can, each has their own challenges.
- 2026-07-21 21:18:48 CST | silenceport | [Ckb,eth ,btc,others](https://talk.nervos.org/t/ckb-eth-btc-others/10517/2) | Just sell btc and eth and purchase ckb
- 2026-07-21 21:07:57 CST | BuildUnion | [[DIS] CKB Anywhere Card: Apple Wallet & Google Wallet Payments for Nervos](https://talk.nervos.org/t/dis-ckb-anywhere-card-apple-wallet-google-wallet-payments-for-nervos/10522/1) | TL;DR What’s New in V2 Thank you to everyone who supported and provided feedback on the original proposal. The feedback was clear: while the core concept was well received, the...
- 2026-07-21 20:24:49 CST | system | [Spark Program | CellMint, No-Code Token Creation & Management Platform for Nervos CKB](https://talk.nervos.org/t/spark-program-cellmint-no-code-token-creation-management-platform-for-nervos-ckb/10483/6) | 
- 2026-07-21 19:46:26 CST | discourse_ai_spam | [Spark Program | CellMint, No-Code Token Creation & Management Platform for Nervos CKB](https://talk.nervos.org/t/spark-program-cellmint-no-code-token-creation-management-platform-for-nervos-ckb/10483/5) | 
- 2026-07-21 19:04:17 CST | Kashlynne_Mumbe | [Spark Program | CellMint, No-Code Token Creation & Management Platform for Nervos CKB](https://talk.nervos.org/t/spark-program-cellmint-no-code-token-creation-management-platform-for-nervos-ckb/10483/4) | Hi @xingtianchunyan Thank you to the committee for the detailed feedback and thoughtful review. I’ve updated the proposal to address the points raised by clearly differentiating...
- 2026-07-21 18:32:51 CST | ckbbkc | [Ckb,eth ,btc,others](https://talk.nervos.org/t/ckb-eth-btc-others/10517/1) | If BTC and ETH both face difficulties in becoming quantum resistant, how can CKB help BTC and ETH holders?
- 2026-07-21 17:19:18 CST | George_Liam | [Spark Program | Fiber Submarine Swap Service](https://talk.nervos.org/t/spark-program-fiber-submarine-swap-service/10516/1) | Spark Program | Fiber Submarine Swap Service Project Name Fiber Submarine Swap Service — A working testnet implementation of a submarine swap for the Fiber Network, solving the...
- 2026-07-21 16:33:50 CST | devnash | [Spark Program | CKB Builder Lab: Interactive Developer Onboarding Infrastructure for the CKB Ecosystem](https://talk.nervos.org/t/spark-program-ckb-builder-lab-interactive-developer-onboarding-infrastructure-for-the-ckb-ecosystem/10385/14) | Hi @xingtianchunyan, Thank you for the detailed feedback and the time the committee has taken to review our progress. I appreciate both points and I’m already working on...
- 2026-07-21 15:13:59 CST | zz_tovarishch | [Spark Program | ckb-joyid-failure-explainer](https://talk.nervos.org/t/spark-program-ckb-joyid-failure-explainer/10426/3) | 
- 2026-07-21 15:13:53 CST | zz_tovarishch | [Spark Program | ckb-joyid-failure-explainer](https://talk.nervos.org/t/spark-program-ckb-joyid-failure-explainer/10426/2) | Hi @Crackdevs 您的申请之前不知道是因为什么原因，没有被我们的格式筛选识别，进而没有进入每周的评审会，后来又因为论坛改版的AI移到了Archive区域 目前已经引动到Spark的子区，会尽快进入评审，感谢您的理解
- 2026-07-21 14:21:31 CST | Crackdevs | [CKB Ecosystem Biweekly Update](https://talk.nervos.org/t/ckb-ecosystem-biweekly-update/9821/23) | HI @zz_tovarishch , we wanted to follow up on our grant application and know the next step moving forward. Thank you.
- 2026-07-21 11:26:30 CST | mohanson | [Deep Dive Into CKB-VM CFI Extension](https://talk.nervos.org/t/deep-dive-into-ckb-vm-cfi-extension/10515/1) | It should be emphasized that CKB-VM does not currently officially support the CFI extension instruction set; related functionality is still in the design and development stage....
- 2026-07-21 05:48:34 CST | WuodOdhis | [Spark Program Proposal: Cell Model Documentation Hub](https://talk.nervos.org/t/spark-program-proposal-cell-model-documentation-hub/10514/1) | 1.Team Profile & Contact Applicant: WuodOdhis GitHub: github.com/WuodOdhis Role: Full-stack developer with experience in blockchain development, CKBuilders program participant,...
