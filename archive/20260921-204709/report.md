# Nervos Talk 社区简报

- 统计窗口: 2026-09-21 04:47:09 CST 到 2026-09-22 04:47:09 CST
- 生成时间: 2026-09-22 04:47:24 CST
- 话题数: 11
- 帖子数: 14
- 作者数: 9
- 总结模式: ai:openai-compatible

## 社区总结

## 今日发生了什么

今天 Nervos Talk 没有单一爆点，更多是既有提案、生态更新和技术讨论的回复与追问 [S01, S02, S04, S06, S07, S08, S10, S11, S12]。最显眼的是 Spark Program 中的 Fiber Weir 提案评审被暂缓，原因指向 Fiber RGB++ Swap 完成请求尚未正式批准 [S01]。Carl 回应表示理解并愿意等待，同时邀请委员会和社区继续对 Fiber Weir 提问或反馈 [S02]。此外，CKBA 的 AMA 公告、CKB 生态双周更新 #25 和 CellScript 0.30 RC 也在今天出现 [S03, S04, S06]。

## 重点话题

- Fiber Weir 评审暂缓：Spark Program 回复称目前无法启动项目评审，因为 Carl 的 Fiber RGB++ Swap 提案完成请求尚未正式获批，委员会仍在审查项目 [S01]。Carl 随后表示理解，愿意等流程允许后再评审，并请委员会或社区在帖中提出疑问、顾虑或反馈 [S02]。

- CKBA AMA 公告：zz_tovarishch 发起新 AMA，嘉宾 Stefan 领导 CKBA 内容与传播团队 [S03]。帖子称这是介绍 CKBA 团队负责人 AMA 系列的一部分，并提到 Stefan 已在 Nervos 生态超过三年 [S03]。

- CKB 生态双周更新 #25：zz_tovarishch 发布第 25 期双周更新，总结过去两周关键开发与生态进展 [S04]。基础设施与工具部分提到 @CKBdev 发布 CKB-VM v0.24.15 [S04]。

- CellScript 0.30 发布候选：ArthurZhang 发帖介绍基于 branch 0.30、commit 6d75a6e7 的 CellScript 0.30 [S06]。匹配成本测试和增长测量在 2026 年 9 月 21 日重新运行 [S06]。0.30.0 目前是 release candidate，0.25 仍是前一稳定版 [S06]。

- 其他技术讨论活跃：SkillPass 帖中有人认可基于 cell 所有权的授权，也有人追问 Alice 把 live cell 转给 Bob 但不想直接交易的机制 [S08, S10]。Sonny 新发帖讨论 Fiber 支付如何让支付与服务同时发生，并涉及解锁数据和控制结算 [S11]。RIVET 帖继续讨论链上记录在商业合同时间证明方面的价值 [S07]。Proof of Buy 周报则提到增加 L1 抗审查攻击方案并继续开发 [S12]。

## 值得继续跟进

- Fiber Weir 的评审进度要看 Fiber RGB++ Swap 完成请求何时正式获批，以及委员会后续审查节奏 [S01, S02]。Carl 已在征集社区对 Fiber Weir 的反馈，相关讨论可能继续 [S02]。

- CellScript 0.30 仍处于 release candidate 阶段，后续可关注成本测试、增长测量细节以及它与 0.25 稳定版的关系 [S06]。

- SkillPass 的 cell 所有权授权与转移设计仍有待澄清，Proof of Buy 的 L1 抗审查方案也在继续开发 [S08, S10, S12]。Fiber 支付实验如 Sonny 所述的方向也值得观察后续落地与反馈 [S11]。

## 来源索引

- `S01` [Spark Program | Fiber Weir — Condition-Gated Payment Streams for Fiber Network](https://talk.nervos.org/t/spark-program-fiber-weir-condition-gated-payment-streams-for-fiber-network/10723/2) | xingtianchunyan | 2026-09-21 10:13:14 CST | Hi @Carl , Thank you for submitting a new proposal, but we are unable to initiate the project review process at this time. The completion request for your Fiber RGB++ Swap proposal has not yet been formally approved, and the committee is still carefully reviewing your project...
- `S02` [Spark Program | Fiber Weir — Condition-Gated Payment Streams for Fiber Network](https://talk.nervos.org/t/spark-program-fiber-weir-condition-gated-payment-streams-for-fiber-network/10723/3) | Carl | 2026-09-22 04:09:54 CST | Thanks for the update, @xingtian — that makes sense, happy to wait until the process allows Fiber Weir to be reviewed. In the meantime, if anyone — committee or community — has questions, concerns, or feedback on the Fiber Weir proposal, please post them here.Happy to clarify,...
- `S03` [AMA with Stefan, CKBA’s Content & Communications Team Lead](https://talk.nervos.org/t/ama-with-stefan-ckba-s-content-communications-team-lead/10733/1) | zz_tovarishch | 2026-09-22 01:53:31 CST | image1928×2222 549 KB Cheers everyone! We’re hosting another AMA! This time, we’re joined by Stefan, who leads CKBA’s Content & Communications team, as part of our AMA series introducing the team leaders within CKBA. Stefan has been part of the Nervos ecosystem for over three...
- `S04` [CKB Ecosystem Biweekly Update](https://talk.nervos.org/t/ckb-ecosystem-biweekly-update/9821/29) | zz_tovarishch | 2026-09-21 22:11:16 CST | CKB Ecosystem Biweekly Update #25 image690×388 97.5 KB Welcome to the latest CKB Ecosystem Biweekly Update. Here’s a quick summary of key dev and ecosystem progress from the past two weeks. Infrastructure & Tooling @CKBdev released CKB-VM v0.24.15. Recent core work also...
- `S05` [Khie，「契」。](https://talk.nervos.org/t/khie/10726/2) | ArthurZhang | 2026-09-21 15:15:23 CST | lol, the logo is such a clever touch.
- `S06` [CellScript 0.30: Abstractions, Bytes, and the Cost](https://talk.nervos.org/t/cellscript-0-30-abstractions-bytes-and-the-cost/10732/1) | ArthurZhang | 2026-09-21 15:01:14 CST | Based on branch 0.30, commit 6d75a6e7. The matched cost tests and growth measurements were rerun on September 21, 2026. Version 0.30.0 is for now a release candidate; 0.25 remains the previous stable release. I deliberately put off the byte and execution costs of CellScript’s...
- `S07` [RIVET: CKB-native GitHub backup using IPFS, RGB++, and CCC](https://talk.nervos.org/t/rivet-ckb-native-github-backup-using-ipfs-rgb-and-ccc/10722/5) | joii2020 | 2026-09-21 14:59:06 CST | For instance, in the case of certain commercial contracts, it serves to prove that the contract actually became effective (or was signed) at specific points in time. Of course, there are other methods—such as email—but the cost of forging something placed on-chain is...
- `S08` [SkillPass: Portable Service Rights on CKB — Looking for Community Feedback](https://talk.nervos.org/t/skillpass-portable-service-rights-on-ckb-looking-for-community-feedback/10706/7) | Crypto_Bull | 2026-09-21 08:14:14 CST | Yes, i think the authorization based on cell ownership is great
- `S09` [SkillPass: Portable Service Rights on CKB — Looking for Community Feedback](https://talk.nervos.org/t/skillpass-portable-service-rights-on-ckb-looking-for-community-feedback/10706/8) | Dangbaty2004 | 2026-09-21 11:17:37 CST | Thank you , really appreciate it !
- `S10` [SkillPass: Portable Service Rights on CKB — Looking for Community Feedback](https://talk.nervos.org/t/skillpass-portable-service-rights-on-ckb-looking-for-community-feedback/10706/9) | joii2020 | 2026-09-21 14:50:43 CST | Let me see if I understand this correctly: There is a live cell held by Alice (meaning she can trade it). Alice wants to transfer this cell to Bob (so that Bob can trade it, while Alice no longer can), but she does not want to transfer this live cell via a direct trade?...
- `S11` [How a Fiber Payment Can Unlock Data and Control Settlement](https://talk.nervos.org/t/how-a-fiber-payment-can-unlock-data-and-control-settlement/10731/1) | Sonny | 2026-09-21 10:19:17 CST | Hi everyone, I’m Sonny. In my earlier “Chat-and-Pay” and “Charge-as-You-Go” experiments, I focused on one question: can payments happen alongside a service, instead of asking users to top up first, consume later, and wait for a platform to settle everything afterward? While...
- `S12` [[DIS] Decentralized privacy order-book appchain based on CKB L1 - 2026.phase-1](https://talk.nervos.org/t/dis-decentralized-privacy-order-book-appchain-based-on-ckb-l1-2026-phase-1/10015/45) | Lawliet_Chan | 2026-09-21 10:16:34 CST | 周报 2026.9.21 讨论并增加proof of buy中的L1抗审查攻击方案： Proof of Buy，一种专为Layer1设计的Layer2共识 - #33 by Lawliet_Chan 继续开发proof of buy: define proof of buy by Lawliet-Chan · Pull Request #8 · invisibook-lab/invisibook · GitHub
- `S13` [CKB, Version Control and Blockchain Evolution](https://talk.nervos.org/t/ckb-version-control-and-blockchain-evolution/4819/11) | Crypto_Bull | 2026-09-21 08:17:38 CST | Absolutely agree. One might ask, what a truly perfect governance looks like?
- `S14` [Cknerv: A Local-first Visualization of CKB](https://talk.nervos.org/t/cknerv-a-local-first-visualization-of-ckb/10689/3) | Crypto_Bull | 2026-09-21 08:00:49 CST | Oh wow, interesting motivation buddy.

## 活跃话题

1. [Spark Program | Fiber Weir — Condition-Gated Payment Streams for Fiber Network](https://talk.nervos.org/t/spark-program-fiber-weir-condition-gated-payment-streams-for-fiber-network/10723) | 2 条近窗帖子 | 最新活动 2026-09-22 04:09:54 CST | tags: Spark-Program
2. [AMA with Stefan, CKBA’s Content & Communications Team Lead](https://talk.nervos.org/t/ama-with-stefan-ckba-s-content-communications-team-lead/10733) | 1 条近窗帖子 | 最新活动 2026-09-22 01:53:31 CST | tags: AMA
3. [CKB Ecosystem Biweekly Update](https://talk.nervos.org/t/ckb-ecosystem-biweekly-update/9821) | 1 条近窗帖子 | 最新活动 2026-09-21 22:11:16 CST | tags: Ecosystem-Update, lang-en
4. [Khie，「契」。](https://talk.nervos.org/t/khie/10726) | 1 条近窗帖子 | 最新活动 2026-09-21 15:15:23 CST | tags: CKB, dapp
5. [CellScript 0.30: Abstractions, Bytes, and the Cost](https://talk.nervos.org/t/cellscript-0-30-abstractions-bytes-and-the-cost/10732) | 1 条近窗帖子 | 最新活动 2026-09-21 15:01:14 CST
6. [RIVET: CKB-native GitHub backup using IPFS, RGB++, and CCC](https://talk.nervos.org/t/rivet-ckb-native-github-backup-using-ipfs-rgb-and-ccc/10722) | 1 条近窗帖子 | 最新活动 2026-09-21 14:59:06 CST | tags: CKB, RGB, appchain, dapp, ipfs, lang-en
7. [SkillPass: Portable Service Rights on CKB — Looking for Community Feedback](https://talk.nervos.org/t/skillpass-portable-service-rights-on-ckb-looking-for-community-feedback/10706) | 3 条近窗帖子 | 最新活动 2026-09-21 14:50:43 CST | tags: CKB, dapp, fiber, testnet
8. [How a Fiber Payment Can Unlock Data and Control Settlement](https://talk.nervos.org/t/how-a-fiber-payment-can-unlock-data-and-control-settlement/10731) | 1 条近窗帖子 | 最新活动 2026-09-21 10:19:17 CST | tags: fiber
9. [[DIS] Decentralized privacy order-book appchain based on CKB L1 - 2026.phase-1](https://talk.nervos.org/t/dis-decentralized-privacy-order-book-appchain-based-on-ckb-l1-2026-phase-1/10015) | 1 条近窗帖子 | 最新活动 2026-09-21 10:16:34 CST | tags: appchain
10. [CKB, Version Control and Blockchain Evolution](https://talk.nervos.org/t/ckb-version-control-and-blockchain-evolution/4819) | 1 条近窗帖子 | 最新活动 2026-09-21 08:17:38 CST | tags: CKB, ELI5, governance, lang-en
11. [Cknerv: A Local-first Visualization of CKB](https://talk.nervos.org/t/cknerv-a-local-first-visualization-of-ckb/10689) | 1 条近窗帖子 | 最新活动 2026-09-21 08:00:49 CST | tags: visualization

## 最近帖子摘录

- 2026-09-22 04:09:54 CST | Carl | [Spark Program | Fiber Weir — Condition-Gated Payment Streams for Fiber Network](https://talk.nervos.org/t/spark-program-fiber-weir-condition-gated-payment-streams-for-fiber-network/10723/3) | Thanks for the update, @xingtian — that makes sense, happy to wait until the process allows Fiber Weir to be reviewed. In the meantime, if anyone — committee or community — has...
- 2026-09-22 01:53:31 CST | zz_tovarishch | [AMA with Stefan, CKBA’s Content & Communications Team Lead](https://talk.nervos.org/t/ama-with-stefan-ckba-s-content-communications-team-lead/10733/1) | image1928×2222 549 KB Cheers everyone! We’re hosting another AMA! This time, we’re joined by Stefan, who leads CKBA’s Content & Communications team, as part of our AMA series...
- 2026-09-21 22:11:16 CST | zz_tovarishch | [CKB Ecosystem Biweekly Update](https://talk.nervos.org/t/ckb-ecosystem-biweekly-update/9821/29) | CKB Ecosystem Biweekly Update #25 image690×388 97.5 KB Welcome to the latest CKB Ecosystem Biweekly Update. Here’s a quick summary of key dev and ecosystem progress from the...
- 2026-09-21 15:15:23 CST | ArthurZhang | [Khie，「契」。](https://talk.nervos.org/t/khie/10726/2) | lol, the logo is such a clever touch.
- 2026-09-21 15:01:14 CST | ArthurZhang | [CellScript 0.30: Abstractions, Bytes, and the Cost](https://talk.nervos.org/t/cellscript-0-30-abstractions-bytes-and-the-cost/10732/1) | Based on branch 0.30, commit 6d75a6e7. The matched cost tests and growth measurements were rerun on September 21, 2026. Version 0.30.0 is for now a release candidate; 0.25...
- 2026-09-21 14:59:06 CST | joii2020 | [RIVET: CKB-native GitHub backup using IPFS, RGB++, and CCC](https://talk.nervos.org/t/rivet-ckb-native-github-backup-using-ipfs-rgb-and-ccc/10722/5) | For instance, in the case of certain commercial contracts, it serves to prove that the contract actually became effective (or was signed) at specific points in time. Of course,...
- 2026-09-21 14:50:43 CST | joii2020 | [SkillPass: Portable Service Rights on CKB — Looking for Community Feedback](https://talk.nervos.org/t/skillpass-portable-service-rights-on-ckb-looking-for-community-feedback/10706/9) | Let me see if I understand this correctly: There is a live cell held by Alice (meaning she can trade it). Alice wants to transfer this cell to Bob (so that Bob can trade it,...
- 2026-09-21 11:17:37 CST | Dangbaty2004 | [SkillPass: Portable Service Rights on CKB — Looking for Community Feedback](https://talk.nervos.org/t/skillpass-portable-service-rights-on-ckb-looking-for-community-feedback/10706/8) | Thank you , really appreciate it !
- 2026-09-21 10:19:17 CST | Sonny | [How a Fiber Payment Can Unlock Data and Control Settlement](https://talk.nervos.org/t/how-a-fiber-payment-can-unlock-data-and-control-settlement/10731/1) | Hi everyone, I’m Sonny. In my earlier “Chat-and-Pay” and “Charge-as-You-Go” experiments, I focused on one question: can payments happen alongside a service, instead of asking...
- 2026-09-21 10:16:34 CST | Lawliet_Chan | [[DIS] Decentralized privacy order-book appchain based on CKB L1 - 2026.phase-1](https://talk.nervos.org/t/dis-decentralized-privacy-order-book-appchain-based-on-ckb-l1-2026-phase-1/10015/45) | 周报 2026.9.21 讨论并增加proof of buy中的L1抗审查攻击方案： Proof of Buy，一种专为Layer1设计的Layer2共识 - #33 by Lawliet_Chan 继续开发proof of buy: define proof of buy by Lawliet-Chan · Pull Request #8 ·...
- 2026-09-21 10:13:14 CST | xingtianchunyan | [Spark Program | Fiber Weir — Condition-Gated Payment Streams for Fiber Network](https://talk.nervos.org/t/spark-program-fiber-weir-condition-gated-payment-streams-for-fiber-network/10723/2) | Hi @Carl , Thank you for submitting a new proposal, but we are unable to initiate the project review process at this time. The completion request for your Fiber RGB++ Swap...
- 2026-09-21 08:17:38 CST | Crypto_Bull | [CKB, Version Control and Blockchain Evolution](https://talk.nervos.org/t/ckb-version-control-and-blockchain-evolution/4819/11) | Absolutely agree. One might ask, what a truly perfect governance looks like?
- 2026-09-21 08:14:14 CST | Crypto_Bull | [SkillPass: Portable Service Rights on CKB — Looking for Community Feedback](https://talk.nervos.org/t/skillpass-portable-service-rights-on-ckb-looking-for-community-feedback/10706/7) | Yes, i think the authorization based on cell ownership is great
- 2026-09-21 08:00:49 CST | Crypto_Bull | [Cknerv: A Local-first Visualization of CKB](https://talk.nervos.org/t/cknerv-a-local-first-visualization-of-ckb/10689/3) | Oh wow, interesting motivation buddy.
