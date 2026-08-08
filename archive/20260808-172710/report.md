# Nervos Talk 社区简报

- 统计窗口: 2026-08-08 01:27:10 CST 到 2026-08-09 01:27:10 CST
- 生成时间: 2026-08-09 01:27:15 CST
- 话题数: 7
- 帖子数: 12
- 作者数: 10
- 总结模式: ai:openai-compatible

## 社区总结

## 今日发生了什么

过去 24 小时，Nervos Talk 没有重大公告或官方发布，整体以项目进展更新和技术讨论为主。[S02, S04, S09] 讨论最集中的是 VeriCell.net 项目更新和 Pocket Node iOS 版的定价话题。[S02, S04, S05, S08] 此外，CKB Builder Lab 发布了第 4 周进展，Proof of Buy 共识讨论也有新的技术细节补充。[S09, S10] 还有几条零散更新，包括对 RocksDB 重构时间的询问，以及 CKB mBabel 双语字幕工具的新版 UI 介绍。[S01, S12]

## 重点话题

- **VeriCell.net 更名并进入 review 阶段**：项目作者宣布项目更名为 VeriCell.net，代码仓库迁移到 GitHub，并新建了 Telegram 社群。[S02] ckbdapps 一方的 yixiu.ckbfans.bit 表示，这个用 live cell 表达版本历史的思路很好地利用了 CKB Cell Model 的特性，并确认正在 review 项目的 PR #7，如有不符合 ckbdapps 规范的地方会在 PR 里同步。[S04]

- **Pocket Node iOS 版讨论出现“移植”误会**：knmo 认为 Android 版实现已获得过报酬，其价值远高于移植到 Apple 平台的报价，并提到 CCC 集成的问题。[S05, S07] Jnr6 澄清是自己用了“port”（移植）这个词造成误解，容易让人觉得一切都已实现、只需搬运。[S08] matt_ckb 则指出被引用的“like likes like”是断章取义，并顺带提到 Cellora 这个 CKB 索引与查询服务项目。[S06]

- **CKB Builder Lab 发布第 4 周进展**：这个 Spark Program 项目聚焦于为 CKB 生态搭建交互式开发者入门基础设施，本周报告称“Challenge MVP 完成”的里程碑已经达成。[S09]

- **Proof of Buy 共识补充 L2 出块细节**：Lawliet_Chan 进一步解释了当 L2 出块比 L1 更快时，矿工通过 VDF + 支付 L1 token 竞选 L2 出块权会遇到的难题——L1 转账还没确认，L2 区块却已经要出了。[S10]

- **CKB=CKBA 执行团队名单引发疑问**：AryaStark 注意到公众认知中的 Nervos/CKB 联创——Jan Xie、Terry Tai、Kevin Wang、Daniel Lv、Cipher Wang——均未出现在 CKBA 执行团队的负责人名单中。[S11]

## 值得继续跟进

- **VeriCell.net 的 PR #7 审查结果**：ckbdapps 一方正在 review，后续是否提出规范调整将影响项目下一步。[S04]

- **Pocket Node iOS 版的定价与工作量争议**：讨论仍待收敛，涉及 Android 先行成果的估值、三个 Apple 平台的移植成本，以及 CCC 集成路线。[S05, S07, S08]

- **RocksDB #5085 重构的时间表**：knmo 询问该 schema 重构是否有预计实现时间，目前帖子中尚未看到回应，底层存储重构的排期仍然是个悬念。[S01]

## 来源索引

- `S01` [When "Refactor rocksdb" #5085](https://talk.nervos.org/t/when-refactor-rocksdb-5085/10595/1) | knmo | 2026-08-08 22:26:51 CST | When “Refactor rocksdb” #5085 breaking RocksDB schema refactor Is there already an estimate of when this will be implemented?
- `S02` [VeriCell.net — proof of authorship, integrity and time in live CKB cells](https://talk.nervos.org/t/vericell-net-proof-of-authorship-integrity-and-time-in-live-ckb-cells/10497/2) | psawyerberlin | 2026-08-08 05:33:10 CST | Quick update: the project is now branded VeriCell.net (repo moved to GitHub - psawyerberlin/vericellnet: Proof of authorship, integrity and time for any digital project, anchored in a live cell on Nervos CKB. · GitHub ), and there’s a community group at Telegram: View...
- `S03` [VeriCell.net — proof of authorship, integrity and time in live CKB cells](https://talk.nervos.org/t/vericell-net-proof-of-authorship-integrity-and-time-in-live-ckb-cells/10497/3) | Fisher | 2026-08-08 08:36:42 CST | @yixiu.ckbfans.bit
- `S04` [VeriCell.net — proof of authorship, integrity and time in live CKB cells](https://talk.nervos.org/t/vericell-net-proof-of-authorship-integrity-and-time-in-live-ckb-cells/10497/4) | yixiu.ckbfans.bit | 2026-08-08 22:00:13 CST | Hi @psawyerberlin, VeriCell.net 这个想法很有意思——用 live cell 的消费/重建来表达版本历史，用 lock 证明所有权、block header 锁定时间戳，这个思路很好地利用了 CKB Cell Model 的特性，而不是简单地把哈希写上链了事。 PR #7 我已经看到了，正在 review，非常感谢你的贡献 。如果需要根据 ckbdapps 的规范做任何调整，我会在 PR 里跟你同步。
- `S05` [[DIS] Pocket Node for iOS: a self-custody CKB light client for iPhone, iPad, and Mac](https://talk.nervos.org/t/dis-pocket-node-for-ios-a-self-custody-ckb-light-client-for-iphone-ipad-and-mac/10583/10) | knmo | 2026-08-08 01:37:32 CST | Jnr6: I would have to strip that device cost out and absorb the hardware myself. I’m also targetting three Apple platforms and a CCC signer the Android app does not have You’ve already been paid for the Android implementation. That initial work was worth significantly more...
- `S06` [[DIS] Pocket Node for iOS: a self-custody CKB light client for iPhone, iPad, and Mac](https://talk.nervos.org/t/dis-pocket-node-for-ios-a-self-custody-ckb-light-client-for-iphone-ipad-and-mac/10583/11) | matt_ckb | 2026-08-08 01:44:35 CST | Cellora — designing a production indexing and query service for CKB (feedback welcome) “like likes like” just want to share that this is taken out of context, the original is meant to communicate that secure practices seem to lead to downstream designs that uphold secure...
- `S07` [[DIS] Pocket Node for iOS: a self-custody CKB light client for iPhone, iPad, and Mac](https://talk.nervos.org/t/dis-pocket-node-for-ios-a-self-custody-ckb-light-client-for-iphone-ipad-and-mac/10583/12) | knmo | 2026-08-08 01:51:51 CST | matt_ckb: I don’t see it as applicable to one’s experience with development on one mobile platform versus another. Thanks for the clarification; I wasn’t clear on that point—I was referring to integrating CCC into PocketNode. But it’s still great and important that the CCC...
- `S08` [[DIS] Pocket Node for iOS: a self-custody CKB light client for iPhone, iPad, and Mac](https://talk.nervos.org/t/dis-pocket-node-for-ios-a-self-custody-ckb-light-client-for-iphone-ipad-and-mac/10583/13) | Jnr6 | 2026-08-08 21:08:58 CST | knmo: That initial work was worth significantly more than porting to Apple platforms is worth I created the misunderstanding, when i used the word “Port” in the proposal, that created the idea of everything needed is already implemented and just need to be transfered over....
- `S09` [Spark Program | CKB Builder Lab: Interactive Developer Onboarding Infrastructure for the CKB Ecosystem](https://talk.nervos.org/t/spark-program-ckb-builder-lab-interactive-developer-onboarding-infrastructure-for-the-ckb-ecosystem/10385/17) | devnash | 2026-08-08 16:43:38 CST | Week 4 Progress Report: CKB Builder Lab Hello everyone, This is the Week 4 progress report for CKB Builder Lab, our Spark Program project focused on interactive developer onboarding for the CKB ecosystem. Week 4 Milestone The Week 4 milestone was: Challenge MVP completed. The...
- `S10` [Proof of Buy，一种专为Layer1设计的Layer2共识](https://talk.nervos.org/t/proof-of-buy-layer1-layer2/9752/28) | Lawliet_Chan | 2026-08-08 16:11:37 CST | 补，如何解决L2出块间隙比L1短的情况下的出块共识问题 前面我们提及了proof of buy要在出块共识的时候通过 VDF + 支付L1 token的方式来竞选出块权， 但我没有解释一个问题，如何支付L1 token？ 我们都知道， L2的出块间隔 跟L1往往不同， 如果L2比L1出块更慢还好， 倘若L2出块比L1更快呢？ 此时，如果矿工支付L1 token来竞选高度为100的L2区块，那么当发起了一笔L1 token的转账之后，L2 的第100个区块已经要出块了，而L1的出块还早，这就导致你这个支付token的交易在L1上还未出块呢，...
- `S11` [Ckb=Ckba](https://talk.nervos.org/t/ckb-ckba/10471/8) | AryaStark | 2026-08-08 15:42:13 CST | Thank you for providing this overview. I noticed that the people commonly known as the co-founders of Nervos/CKB—Jan Xie, Terry Tai, Kevin Wang, Daniel Lv and Cipher Wang—are not listed among the leads of CKBA’s execution teams. I understand that this post may only list the...
- `S12` [CKB mBabel: Live Bilingual Captions for zh↔en Meetings](https://talk.nervos.org/t/ckb-mbabel-live-bilingual-captions-for-zh-en-meetings/10593/3) | zz_tovarishch | 2026-08-08 06:26:08 CST | Aug 8 Updates 2: Redesigned UI: a single bilingual transcript (speaker + time in the margin, original above, translation below), light/dark themes, per-viewer language view and font sizes with a presentation mode. image1920×1493 348 KB Draft-first pipeline: the live draft is...

## 活跃话题

1. [When "Refactor rocksdb" #5085](https://talk.nervos.org/t/when-refactor-rocksdb-5085/10595) | 1 条近窗帖子 | 最新活动 2026-08-08 22:26:51 CST
2. [VeriCell.net — proof of authorship, integrity and time in live CKB cells](https://talk.nervos.org/t/vericell-net-proof-of-authorship-integrity-and-time-in-live-ckb-cells/10497) | 3 条近窗帖子 | 最新活动 2026-08-08 22:00:13 CST | tags: dapp, lang-en
3. [[DIS] Pocket Node for iOS: a self-custody CKB light client for iPhone, iPad, and Mac](https://talk.nervos.org/t/dis-pocket-node-for-ios-a-self-custody-ckb-light-client-for-iphone-ipad-and-mac/10583) | 4 条近窗帖子 | 最新活动 2026-08-08 21:08:58 CST | tags: Pocket-Node, light-client
4. [Spark Program | CKB Builder Lab: Interactive Developer Onboarding Infrastructure for the CKB Ecosystem](https://talk.nervos.org/t/spark-program-ckb-builder-lab-interactive-developer-onboarding-infrastructure-for-the-ckb-ecosystem/10385) | 1 条近窗帖子 | 最新活动 2026-08-08 16:43:38 CST | tags: In-Progress, Spark-Program, lang-en
5. [Proof of Buy，一种专为Layer1设计的Layer2共识](https://talk.nervos.org/t/proof-of-buy-layer1-layer2/9752) | 1 条近窗帖子 | 最新活动 2026-08-08 16:11:37 CST | tags: lang-zh, 共识协议
6. [Ckb=Ckba](https://talk.nervos.org/t/ckb-ckba/10471) | 1 条近窗帖子 | 最新活动 2026-08-08 15:42:13 CST | tags: lang-en
7. [CKB mBabel: Live Bilingual Captions for zh↔en Meetings](https://talk.nervos.org/t/ckb-mbabel-live-bilingual-captions-for-zh-en-meetings/10593) | 1 条近窗帖子 | 最新活动 2026-08-08 06:26:08 CST

## 最近帖子摘录

- 2026-08-08 22:26:51 CST | knmo | [When "Refactor rocksdb" #5085](https://talk.nervos.org/t/when-refactor-rocksdb-5085/10595/1) | When “Refactor rocksdb” #5085 breaking RocksDB schema refactor Is there already an estimate of when this will be implemented?
- 2026-08-08 22:00:13 CST | yixiu.ckbfans.bit | [VeriCell.net — proof of authorship, integrity and time in live CKB cells](https://talk.nervos.org/t/vericell-net-proof-of-authorship-integrity-and-time-in-live-ckb-cells/10497/4) | Hi @psawyerberlin, VeriCell.net 这个想法很有意思——用 live cell 的消费/重建来表达版本历史，用 lock 证明所有权、block header 锁定时间戳，这个思路很好地利用了 CKB Cell Model 的特性，而不是简单地把哈希写上链了事。 PR #7 我已经看到了，正在 review，非常感谢你的贡献...
- 2026-08-08 21:08:58 CST | Jnr6 | [[DIS] Pocket Node for iOS: a self-custody CKB light client for iPhone, iPad, and Mac](https://talk.nervos.org/t/dis-pocket-node-for-ios-a-self-custody-ckb-light-client-for-iphone-ipad-and-mac/10583/13) | knmo: That initial work was worth significantly more than porting to Apple platforms is worth I created the misunderstanding, when i used the word “Port” in the proposal, that...
- 2026-08-08 16:43:38 CST | devnash | [Spark Program | CKB Builder Lab: Interactive Developer Onboarding Infrastructure for the CKB Ecosystem](https://talk.nervos.org/t/spark-program-ckb-builder-lab-interactive-developer-onboarding-infrastructure-for-the-ckb-ecosystem/10385/17) | Week 4 Progress Report: CKB Builder Lab Hello everyone, This is the Week 4 progress report for CKB Builder Lab, our Spark Program project focused on interactive developer...
- 2026-08-08 16:11:37 CST | Lawliet_Chan | [Proof of Buy，一种专为Layer1设计的Layer2共识](https://talk.nervos.org/t/proof-of-buy-layer1-layer2/9752/28) | 补，如何解决L2出块间隙比L1短的情况下的出块共识问题 前面我们提及了proof of buy要在出块共识的时候通过 VDF + 支付L1 token的方式来竞选出块权， 但我没有解释一个问题，如何支付L1 token？ 我们都知道， L2的出块间隔 跟L1往往不同， 如果L2比L1出块更慢还好， 倘若L2出块比L1更快呢？ 此时，如果矿工支付L1...
- 2026-08-08 15:42:13 CST | AryaStark | [Ckb=Ckba](https://talk.nervos.org/t/ckb-ckba/10471/8) | Thank you for providing this overview. I noticed that the people commonly known as the co-founders of Nervos/CKB—Jan Xie, Terry Tai, Kevin Wang, Daniel Lv and Cipher Wang—are...
- 2026-08-08 08:36:42 CST | Fisher | [VeriCell.net — proof of authorship, integrity and time in live CKB cells](https://talk.nervos.org/t/vericell-net-proof-of-authorship-integrity-and-time-in-live-ckb-cells/10497/3) | @yixiu.ckbfans.bit
- 2026-08-08 06:26:08 CST | zz_tovarishch | [CKB mBabel: Live Bilingual Captions for zh↔en Meetings](https://talk.nervos.org/t/ckb-mbabel-live-bilingual-captions-for-zh-en-meetings/10593/3) | Aug 8 Updates 2: Redesigned UI: a single bilingual transcript (speaker + time in the margin, original above, translation below), light/dark themes, per-viewer language view and...
- 2026-08-08 05:33:10 CST | psawyerberlin | [VeriCell.net — proof of authorship, integrity and time in live CKB cells](https://talk.nervos.org/t/vericell-net-proof-of-authorship-integrity-and-time-in-live-ckb-cells/10497/2) | Quick update: the project is now branded VeriCell.net (repo moved to GitHub - psawyerberlin/vericellnet: Proof of authorship, integrity and time for any digital project,...
- 2026-08-08 01:51:51 CST | knmo | [[DIS] Pocket Node for iOS: a self-custody CKB light client for iPhone, iPad, and Mac](https://talk.nervos.org/t/dis-pocket-node-for-ios-a-self-custody-ckb-light-client-for-iphone-ipad-and-mac/10583/12) | matt_ckb: I don’t see it as applicable to one’s experience with development on one mobile platform versus another. Thanks for the clarification; I wasn’t clear on that point—I...
- 2026-08-08 01:44:35 CST | matt_ckb | [[DIS] Pocket Node for iOS: a self-custody CKB light client for iPhone, iPad, and Mac](https://talk.nervos.org/t/dis-pocket-node-for-ios-a-self-custody-ckb-light-client-for-iphone-ipad-and-mac/10583/11) | Cellora — designing a production indexing and query service for CKB (feedback welcome) “like likes like” just want to share that this is taken out of context, the original is...
- 2026-08-08 01:37:32 CST | knmo | [[DIS] Pocket Node for iOS: a self-custody CKB light client for iPhone, iPad, and Mac](https://talk.nervos.org/t/dis-pocket-node-for-ios-a-self-custody-ckb-light-client-for-iphone-ipad-and-mac/10583/10) | Jnr6: I would have to strip that device cost out and absorb the hardware myself. I’m also targetting three Apple platforms and a CCC signer the Android app does not have You’ve...
