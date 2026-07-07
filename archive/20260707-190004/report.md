# Nervos Talk 社区简报

- 统计窗口: 2026-07-07 03:00:04 CST 到 2026-07-08 03:00:04 CST
- 生成时间: 2026-07-08 03:00:13 CST
- 话题数: 9
- 帖子数: 16
- 作者数: 12
- 总结模式: ai:openrouter

## 社区总结

## 今日发生了什么

Nervos Talk 社区今日动静不小，既有底层技术 CKB-VM 宏操作融合的深度讨论，也有多个生态项目拿到 Spark 计划首笔拨款开始动工，外加 Ecosystem Biweekly Update 发布新一期进展。[S03, S05, S12, S15]

## 重点话题

- **CKB-VM 性能优化遇到新思路**：mohanson 发布长文深入解析 CKB-VM 的 Macro-ops Fusion 技术，解释了指令融合在解码阶段如何提升执行效率，但也坦诚指出某些算法（如 sphincsplus_ref）因无法触发融合反而性能倒退；社区随后围绕"更便宜的保守预过滤方案"展开多轮技术辩论，knmo 对实现开销提出质疑，讨论仍在继续。[S05, S06, S07, S08]

- **Spark 计划两笔拨款同步发放**：CKB Wallet Behaviour Intelligence 和 Cell Sandbox 两个项目均于今日收到首期款项，开发者已确认到账，社区期待看到第一份进度更新。[S12, S13, S15]

- **生态工具上新**：Scryve 正式对外开放，定位为"带有认证作者权和永久存档"的长文发布平台；Werra 的创作者商业信任基础设施 POC 也更新了测试链接，支持邮箱登录和托管测试网钱包。[S14, S16]

- **社区目录与 AI 学习工具联动**：XBeach 的 VibeQuest AI 游戏化学习工作bench 被纳入 dir 开放目录，truthixify 邀请其提交 PR。[S01, S02]

- **Invisibook AMA 获社区关注**：隐私订单簿项目的 Reddit AMA 总结帖引发讨论，Fisher 建议官方推特转发扩散。[S09, S11]

## 值得继续跟进

- CKB-VM MOP Fusion 的预过滤优化能否在"语义安全"与"解码开销"之间找到真正低成本的平衡点，将直接影响未来合约执行效率。[S07, S08]

- Scryve 和 Werra 两个新项目均刚进入可用阶段，实际用户体验和后续迭代节奏尚待观察。[S14, S16]

- VibeQuest 修订后的 MVP 聚焦 CKB Cell Model 和 Fiber，其交付质量将成为检验 Spark 计划"窄范围快速验证"策略的样本。[S04]

## 来源索引

- `S01` [Introducing dir, an open directory and standing request for CKB-native ideas](https://talk.nervos.org/t/introducing-dir-an-open-directory-and-standing-request-for-ckb-native-ideas/10415/3) | XBeach | 2026-07-08 00:13:49 CST | Hello, I’m working on VibeQuest is an AI gamified learning workbench for CKB/Fiber. It turns a learner’s goal into AI-generated lessons, checkpoint questions, lesson-based code quests, verifier files, denial tests, and boss challenges so people do not just vibe-code CKB apps,...
- `S02` [Introducing dir, an open directory and standing request for CKB-native ideas](https://talk.nervos.org/t/introducing-dir-an-open-directory-and-standing-request-for-ckb-native-ideas/10415/4) | truthixify | 2026-07-08 01:02:18 CST | Yes, it would! Please create a PR to add it to the directory
- `S03` [CKB Ecosystem Biweekly Update](https://talk.nervos.org/t/ckb-ecosystem-biweekly-update/9821/22) | zz_tovarishch | 2026-07-07 21:20:45 CST | image1380×776 224 KB CKB Ecosystem Biweekly Update #20 Welcome to the latest CKB Ecosystem Biweekly Update. Here’s a quick summary of key dev and ecosystem progress from the past two weeks. Infrastructure & Tooling @CKBdev launched an AI Resources page, continued security...
- `S04` [Spark Program | VibeQuest: Turning AI-Assisted Coding Into Real Learning](https://talk.nervos.org/t/spark-program-vibequest-turning-ai-assisted-coding-into-real-learning/10446/3) | XBeach | 2026-07-07 20:36:32 CST | Hi @xingtianchunyan, Thank you for the thoughtful feedback. I revised the proposal with your points in mind. The scope is now narrowed around a focused MVP instead of broad ecosystem coverage. The current MVP centers on two practical learning areas: CKB Cell Model and Fiber...
- `S05` [Deep Dive Into CKB-VM Macro-ops Fusion](https://talk.nervos.org/t/deep-dive-into-ckb-vm-macro-ops-fusion/10468/1) | mohanson | 2026-07-07 13:33:20 CST | Deep Dive Into CKB-VM Macro-ops Fusion Overview Macro-Operation Fusion (MOP Fusion) is a performance optimization technique used in modern microprocessor architectures. During instruction decode, several adjacent macro-operations are merged into a single internal micro-...
- `S06` [Deep Dive Into CKB-VM Macro-ops Fusion](https://talk.nervos.org/t/deep-dive-into-ckb-vm-macro-ops-fusion/10468/2) | knmo | 2026-07-07 17:06:26 CST | mohanson: For sphincsplus_ref, because it never triggers any fused opcode, performance regresses after enabling MOP. This is because the MOP decoder introduces extra work during decoding, but the instruction stream of this algorithm offers no fusion opportunities to offset...
- `S07` [Deep Dive Into CKB-VM Macro-ops Fusion](https://talk.nervos.org/t/deep-dive-into-ckb-vm-macro-ops-fusion/10468/3) | mohanson | 2026-07-07 19:44:19 CST | An even cheaper conservative prefilter is: “If a block contains none of the opcodes that can start any fusion rule, skip the MOP decoder for that block immediately.” That keeps the optimization semantics-safe while avoiding repeated decode-time overhead in cases like...
- `S08` [Deep Dive Into CKB-VM Macro-ops Fusion](https://talk.nervos.org/t/deep-dive-into-ckb-vm-macro-ops-fusion/10468/4) | knmo | 2026-07-07 20:35:29 CST | mohanson: cheaper conservative prefilter Would that be expensive? It would have to happen all the time—at least until the bypass check determines that the MOP decoder is needed. “any fused opcode? trigger check” In any case, it’s a more general / better approach than making...
- `S09` [The Invisibook AMA](https://talk.nervos.org/t/the-invisibook-ama/10401/2) | JackyLHH | 2026-07-07 19:34:25 CST | The Invisibook Reddit AMA Recap Invisibook is a privacy-preserving, censorship-resistant, decentralized order book with a purely cryptographic stack. This Reddit AMA covered how Invisibook relates to CKB, why the team is building a privacy-focused order book instead of an AMM,...
- `S10` [The Invisibook AMA](https://talk.nervos.org/t/the-invisibook-ama/10401/3) | matt.eth | 2026-07-07 20:08:01 CST | 赞！！！！
- `S11` [The Invisibook AMA](https://talk.nervos.org/t/the-invisibook-ama/10401/4) | Fisher | 2026-07-07 20:30:29 CST | 这个AMA是不是可以整理下发在官推上？
- `S12` [Spark Program | CKB Wallet Behaviour Intelligence](https://talk.nervos.org/t/spark-program-ckb-wallet-behaviour-intelligence/10338/8) | xingtianchunyan | 2026-07-07 17:06:11 CST | Hi @mulinya , The first installment has been disbursed. Transaction Hash: 0x3bbaecf1b871643edb1fd635c399cf502cfad1ae22fe89851859cf01a380aa16 Please confirm once received. Looking forward to your first progress update. Best, xingtian On behalf of the Spark Program Committee
- `S13` [Spark Program | CKB Wallet Behaviour Intelligence](https://talk.nervos.org/t/spark-program-ckb-wallet-behaviour-intelligence/10338/9) | mulinya | 2026-07-07 19:08:01 CST | Hello @xingtianchunyan I have received , Thank you. Best, Fadhil
- `S14` [[DIS] Werra: Building Trust Infrastructure for Creator Commerce](https://talk.nervos.org/t/dis-werra-building-trust-infrastructure-for-creator-commerce/10453/9) | DWSQUIRES | 2026-07-07 18:42:02 CST | We have updated the proposal to include the live Werra POC link: werra-tau.vercel.app werra The POC is now available for community testing. It currently supports email-based sign-in with managed CKB testnet wallets, separate SME and creator workspaces, brief posting, creator...
- `S15` [Spark Program | Cell Sandbox — A Visual Playground for the CKB Cell Model](https://talk.nervos.org/t/spark-program-cell-sandbox-a-visual-playground-for-the-ckb-cell-model/10326/14) | xingtianchunyan | 2026-07-07 17:05:19 CST | Hi @zynor , The first installment has been disbursed. Transaction Hash: 0xb11d48918d809bb298907abaa2c5862d1abc9acab8c1bd7265f11cf902a1691d Please confirm once received. Looking forward to your first progress update. Best, xingtian On behalf of the Spark Program Committee
- `S16` [Scryve is live - Publish long-form essays with certified authorship and permanent archiving](https://talk.nervos.org/t/scryve-is-live-publish-long-form-essays-with-certified-authorship-and-permanent-archiving/10467/1) | LusoCryptoLabs | 2026-07-07 09:29:44 CST | Hi all, After months of heads-down building, Scryve is live at scryvehq.com. It is a long-form publishing platform made for essays and deep writing rather than short posts. The idea is simple. Writers should own what they publish and be supported directly, without a platform...

## 活跃话题

1. [Introducing dir, an open directory and standing request for CKB-native ideas](https://talk.nervos.org/t/introducing-dir-an-open-directory-and-standing-request-for-ckb-native-ideas/10415) | 2 条近窗帖子 | 最新活动 2026-07-08 01:02:18 CST | tags: CKB, dapp
2. [CKB Ecosystem Biweekly Update](https://talk.nervos.org/t/ckb-ecosystem-biweekly-update/9821) | 1 条近窗帖子 | 最新活动 2026-07-07 21:20:45 CST | tags: Ecosystem-Update
3. [Spark Program | VibeQuest: Turning AI-Assisted Coding Into Real Learning](https://talk.nervos.org/t/spark-program-vibequest-turning-ai-assisted-coding-into-real-learning/10446) | 1 条近窗帖子 | 最新活动 2026-07-07 20:36:32 CST | tags: Spark-Program
4. [Deep Dive Into CKB-VM Macro-ops Fusion](https://talk.nervos.org/t/deep-dive-into-ckb-vm-macro-ops-fusion/10468) | 4 条近窗帖子 | 最新活动 2026-07-07 20:35:29 CST | tags: CKB-VM
5. [The Invisibook AMA](https://talk.nervos.org/t/the-invisibook-ama/10401) | 3 条近窗帖子 | 最新活动 2026-07-07 20:30:29 CST | tags: AMA
6. [Spark Program | CKB Wallet Behaviour Intelligence](https://talk.nervos.org/t/spark-program-ckb-wallet-behaviour-intelligence/10338) | 2 条近窗帖子 | 最新活动 2026-07-07 19:08:01 CST | tags: CKB, In-Progress, Spark-Program
7. [[DIS] Werra: Building Trust Infrastructure for Creator Commerce](https://talk.nervos.org/t/dis-werra-building-trust-infrastructure-for-creator-commerce/10453) | 1 条近窗帖子 | 最新活动 2026-07-07 18:42:02 CST
8. [Spark Program | Cell Sandbox — A Visual Playground for the CKB Cell Model](https://talk.nervos.org/t/spark-program-cell-sandbox-a-visual-playground-for-the-ckb-cell-model/10326) | 1 条近窗帖子 | 最新活动 2026-07-07 17:05:19 CST | tags: In-Progress, Spark-Program
9. [Scryve is live - Publish long-form essays with certified authorship and permanent archiving](https://talk.nervos.org/t/scryve-is-live-publish-long-form-essays-with-certified-authorship-and-permanent-archiving/10467) | 1 条近窗帖子 | 最新活动 2026-07-07 09:29:44 CST | tags: CKB, appchain, dapp

## 最近帖子摘录

- 2026-07-08 01:02:18 CST | truthixify | [Introducing dir, an open directory and standing request for CKB-native ideas](https://talk.nervos.org/t/introducing-dir-an-open-directory-and-standing-request-for-ckb-native-ideas/10415/4) | Yes, it would! Please create a PR to add it to the directory
- 2026-07-08 00:13:49 CST | XBeach | [Introducing dir, an open directory and standing request for CKB-native ideas](https://talk.nervos.org/t/introducing-dir-an-open-directory-and-standing-request-for-ckb-native-ideas/10415/3) | Hello, I’m working on VibeQuest is an AI gamified learning workbench for CKB/Fiber. It turns a learner’s goal into AI-generated lessons, checkpoint questions, lesson-based code...
- 2026-07-07 21:20:45 CST | zz_tovarishch | [CKB Ecosystem Biweekly Update](https://talk.nervos.org/t/ckb-ecosystem-biweekly-update/9821/22) | image1380×776 224 KB CKB Ecosystem Biweekly Update #20 Welcome to the latest CKB Ecosystem Biweekly Update. Here’s a quick summary of key dev and ecosystem progress from the...
- 2026-07-07 20:36:32 CST | XBeach | [Spark Program | VibeQuest: Turning AI-Assisted Coding Into Real Learning](https://talk.nervos.org/t/spark-program-vibequest-turning-ai-assisted-coding-into-real-learning/10446/3) | Hi @xingtianchunyan, Thank you for the thoughtful feedback. I revised the proposal with your points in mind. The scope is now narrowed around a focused MVP instead of broad...
- 2026-07-07 20:35:29 CST | knmo | [Deep Dive Into CKB-VM Macro-ops Fusion](https://talk.nervos.org/t/deep-dive-into-ckb-vm-macro-ops-fusion/10468/4) | mohanson: cheaper conservative prefilter Would that be expensive? It would have to happen all the time—at least until the bypass check determines that the MOP decoder is needed....
- 2026-07-07 20:30:29 CST | Fisher | [The Invisibook AMA](https://talk.nervos.org/t/the-invisibook-ama/10401/4) | 这个AMA是不是可以整理下发在官推上？
- 2026-07-07 20:08:01 CST | matt.eth | [The Invisibook AMA](https://talk.nervos.org/t/the-invisibook-ama/10401/3) | 赞！！！！
- 2026-07-07 19:44:19 CST | mohanson | [Deep Dive Into CKB-VM Macro-ops Fusion](https://talk.nervos.org/t/deep-dive-into-ckb-vm-macro-ops-fusion/10468/3) | An even cheaper conservative prefilter is: “If a block contains none of the opcodes that can start any fusion rule, skip the MOP decoder for that block immediately.” That keeps...
- 2026-07-07 19:34:25 CST | JackyLHH | [The Invisibook AMA](https://talk.nervos.org/t/the-invisibook-ama/10401/2) | The Invisibook Reddit AMA Recap Invisibook is a privacy-preserving, censorship-resistant, decentralized order book with a purely cryptographic stack. This Reddit AMA covered how...
- 2026-07-07 19:08:01 CST | mulinya | [Spark Program | CKB Wallet Behaviour Intelligence](https://talk.nervos.org/t/spark-program-ckb-wallet-behaviour-intelligence/10338/9) | Hello @xingtianchunyan I have received , Thank you. Best, Fadhil
- 2026-07-07 18:42:02 CST | DWSQUIRES | [[DIS] Werra: Building Trust Infrastructure for Creator Commerce](https://talk.nervos.org/t/dis-werra-building-trust-infrastructure-for-creator-commerce/10453/9) | We have updated the proposal to include the live Werra POC link: werra-tau.vercel.app werra The POC is now available for community testing. It currently supports email-based...
- 2026-07-07 17:06:26 CST | knmo | [Deep Dive Into CKB-VM Macro-ops Fusion](https://talk.nervos.org/t/deep-dive-into-ckb-vm-macro-ops-fusion/10468/2) | mohanson: For sphincsplus_ref, because it never triggers any fused opcode, performance regresses after enabling MOP. This is because the MOP decoder introduces extra work during...
- 2026-07-07 17:06:11 CST | xingtianchunyan | [Spark Program | CKB Wallet Behaviour Intelligence](https://talk.nervos.org/t/spark-program-ckb-wallet-behaviour-intelligence/10338/8) | Hi @mulinya , The first installment has been disbursed. Transaction Hash: 0x3bbaecf1b871643edb1fd635c399cf502cfad1ae22fe89851859cf01a380aa16 Please confirm once received....
- 2026-07-07 17:05:19 CST | xingtianchunyan | [Spark Program | Cell Sandbox — A Visual Playground for the CKB Cell Model](https://talk.nervos.org/t/spark-program-cell-sandbox-a-visual-playground-for-the-ckb-cell-model/10326/14) | Hi @zynor , The first installment has been disbursed. Transaction Hash: 0xb11d48918d809bb298907abaa2c5862d1abc9acab8c1bd7265f11cf902a1691d Please confirm once received. Looking...
- 2026-07-07 13:33:20 CST | mohanson | [Deep Dive Into CKB-VM Macro-ops Fusion](https://talk.nervos.org/t/deep-dive-into-ckb-vm-macro-ops-fusion/10468/1) | Deep Dive Into CKB-VM Macro-ops Fusion Overview Macro-Operation Fusion (MOP Fusion) is a performance optimization technique used in modern microprocessor architectures. During...
- 2026-07-07 09:29:44 CST | LusoCryptoLabs | [Scryve is live - Publish long-form essays with certified authorship and permanent archiving](https://talk.nervos.org/t/scryve-is-live-publish-long-form-essays-with-certified-authorship-and-permanent-archiving/10467/1) | Hi all, After months of heads-down building, Scryve is live at scryvehq.com. It is a long-form publishing platform made for essays and deep writing rather than short posts. The...
