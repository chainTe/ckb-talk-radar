# Nervos Talk 社区简报

- 统计窗口: 2026-07-03 02:11:19 CST 到 2026-07-04 02:11:19 CST
- 生成时间: 2026-07-04 02:11:23 CST
- 话题数: 5
- 帖子数: 16
- 作者数: 9
- 总结模式: ai:openrouter

## 社区总结

## 今日发生了什么

社区成员 zz_tovarishch 发布了一款名为《Masked Identity》的互动叙事网页游戏，玩家扮演苏联末期军事医院的医生，对档案进行保留、打码或销毁等抉择，并将最终结局数据以 JSON 格式存储到 CKB 链上。[S01] 该作品因其独特的主题选择和轻量化的链上结合方式，获得了核心贡献者 RetricSu 的高度评价。[S03]

## 重点话题

- **叙事游戏上链引发讨论**：zz_tovarishch 详细解释了游戏结局上链的具体实现方式，采用自定义 JSON Schema 记录玩家的结局 ID、Truth/Safety/Identity 数值等信息，数据轻量且可选上链。[S01, S06] RetricSu 称赞这种应用展现了 CKB 社区独特的"调性"，并好奇询问链上副本能否 decode 出来。[S03, S05]

- **"富豪版"永久记录 DApp 的设想**：社区成员 ckbbkc 提议基于 CKB 开发面向富豪的个人故事、心得永久记录 DApp，利用 CKB 的持久性让信息"永远不会消失"。[S02] 同一作者还发帖询问 CKB 在 RWA 和 AI 领域的应用场景。[S11]

- **Werra 资助提案调整推进**：创作者商业信任基础设施项目 Werra 的提案人 DWSQUIRES 在 zz_tovarishch 澄清 DAO 不支持 USDI 支付后，已将资助请求修改为固定 27,700 美元等值 CKB 支付。[S07, S08] neon.bit 反馈称资助额度越大举证责任越重，建议提供概念验证，DWSQUIRES 回应称将加速推进可检查的 POC。[S09, S10]

- **CKB Builder Lab 首周进度提交**：Spark Program 受资助项目 CKB Builder Lab 提交了第一周进展报告，聚焦 CKB 生态交互式开发者入门基础设施建设。[S13]

## 值得继续跟进

- CellKit Actions 项目的资助流程进展：Fidelcoder 在 Spark Program 申请帖中跟进称自上次回复澄清后未收到对方回音，需观察后续沟通是否恢复。[S12]

- Werra 提案的 POC 产出质量：DWSQUIRES 承诺将推进核心功能的概念验证，社区可观察其是否能回应"大额资助需更强举证"的质疑。[S09, S10]

- RWA 与 AI 应用场景讨论：ckbbkc 抛出的这两个方向目前仅为简短提问，尚未有深入展开，需看是否有社区成员接力回应。[S11]

## 来源索引

- `S01` [关于“档案、身份与遗忘”的游戏，结尾把档案存进 CKB](https://talk.nervos.org/t/ckb/10454/1) | zz_tovarishch | 2026-07-03 07:54:45 CST | 做了一个小型网页叙事游戏， 《Masked Identity》。 这是一个什么游戏？ 《Masked Identity》是一个基于我个人经历改写的互动叙事游戏。它把一些真实经验、历史想象和对制度性记忆的探讨，放进一个架空的苏联末期军事医院里。 1920×833 281 KB 玩家扮演一名医生，面对一个人的病例、军方记录、家庭材料、事故报告、告密文件和各种被涂改过的档案进行决策： 保留 、打码、销毁一份文件 把某些证据重新呈现给病人 Redact978×1658 254 KB Present984×1664 248 KB...
- `S02` [关于“档案、身份与遗忘”的游戏，结尾把档案存进 CKB](https://talk.nervos.org/t/ckb/10454/2) | ckbbkc | 2026-07-03 08:35:58 CST | 可以考虑推出一个富豪版的个人故事，心得，记录的dapp，基于ckb，让富豪们留下永远不会消失的消息（ckb如果能一直运行下去）
- `S03` [关于“档案、身份与遗忘”的游戏，结尾把档案存进 CKB](https://talk.nervos.org/t/ckb/10454/3) | RetricSu | 2026-07-03 09:08:23 CST | 这个真的很棒！从你的游戏的创意、文本内容的编写，以及你特意选择了很轻量、甚至是某种可选的、和链上结合的方式，我能感觉出来你做这个东西真的有注入许多自己的想法。 我觉得这样的应用会让我眼前一亮，让我看到 ckb 产生了不太一样的东西。这个东西是什么呢？其实就是一种调性。它不一定是 CKB 的某些技术特点产生的（不过这个游戏切入“存档”确实和 ckb 作为共同知识库的定位是非常契合的），更多的我觉得是来自做事情的人的特点。 因为 CKB 社区的人不一样，所以做出来的东西也会不一样。我觉得这个小游戏很好的展示了这一点。你关于...
- `S04` [关于“档案、身份与遗忘”的游戏，结尾把档案存进 CKB](https://talk.nervos.org/t/ckb/10454/4) | Fisher | 2026-07-03 09:56:00 CST | 搞个基于爱泼斯坦档案审判特朗普的游戏
- `S05` [关于“档案、身份与遗忘”的游戏，结尾把档案存进 CKB](https://talk.nervos.org/t/ckb/10454/5) | RetricSu | 2026-07-03 10:16:50 CST | image1920×974 159 KB 请问链上存的副本具体是什么信息？这里可以把这些信息decode出来吗？
- `S06` [关于“档案、身份与遗忘”的游戏，结尾把档案存进 CKB](https://talk.nervos.org/t/ckb/10454/6) | zz_tovarishch | 2026-07-03 10:23:30 CST | 实现方式很简单： 结局页生成 JSON schema 大概是： { "p": "masked-identity", "v": 1, "e": "erased", "t": 0, "s": 100, "i": 0, "l": "en", "d": "2026-07-02", "n": "optional archivist name" } 字段含义： p: 协议标记，Masked Identity 的记录 v: schema 版本 e: 结局 ID t: Truth 数值 s: Safety 数值 i: Identity 数值 l: 语言，zh 或...
- `S07` [[DIS] Werra: Building Trust Infrastructure for Creator Commerce](https://talk.nervos.org/t/dis-werra-building-trust-infrastructure-for-creator-commerce/10453/4) | zz_tovarishch | 2026-07-03 02:35:12 CST | DWSQUIRES: preferably paid in USDI 你好，目前DAO没有基于USDI的支付选项 你可以选择以固定CKB支付或者以固定的USD额度支付 [DIS] Fiber Desktop v1 ground-up rebuild and launch — fnn desktop app CKB Community Fund DAO 就本帖中关于支付条款的疑问，分享委员会的适用确认： 依据 v1.0 第三阶段条款：“If there are additional rules for disbursement, the rules...
- `S08` [[DIS] Werra: Building Trust Infrastructure for Creator Commerce](https://talk.nervos.org/t/dis-werra-building-trust-infrastructure-for-creator-commerce/10453/5) | DWSQUIRES | 2026-07-03 08:38:17 CST | @zz_tovarishch thank you for the clarification. I have updated the proposal to remove the USDI payment request and align with the DAO’s supported payment terms. The grant request is now stated as a fixed USD amount of $27,700, to be paid in CKB equivalent at the time of each...
- `S09` [[DIS] Werra: Building Trust Infrastructure for Creator Commerce](https://talk.nervos.org/t/dis-werra-building-trust-infrastructure-for-creator-commerce/10453/6) | neon.bit | 2026-07-03 16:13:18 CST | Hi @DWSQUIRES Thanks for your proposal, glad to see you are considering solutions for businesses and content creators in the form of escrow platforms. Generally speaking, the greater the grant request, the greater the burden of proof on the proposer to demonstrate relevant...
- `S10` [[DIS] Werra: Building Trust Infrastructure for Creator Commerce](https://talk.nervos.org/t/dis-werra-building-trust-infrastructure-for-creator-commerce/10453/7) | DWSQUIRES | 2026-07-03 19:26:58 CST | Hi @neon.bit Thank you for the thoughtful feedback. I agree with your point. I’m taking this advice seriously and advance the current prototype into a clearer proof of concept that the community can inspect and give feedback on. The POC will focus on demonstrating the core...
- `S11` [Application scenarios of ckb](https://talk.nervos.org/t/application-scenarios-of-ckb/10455/1) | ckbbkc | 2026-07-03 12:48:01 CST | RWA？，how to work with AI?
- `S12` [Spark Program | CellKit Actions — Reusable Transaction Actions for CKB Apps](https://talk.nervos.org/t/spark-program-cellkit-actions-reusable-transaction-actions-for-ckb-apps/10375/6) | Fidelcoder | 2026-07-03 10:36:50 CST | @xingtianchunyan Hello, I’ve not heard from you since my previous response/clarification!
- `S13` [Spark Program | CKB Builder Lab: Interactive Developer Onboarding Infrastructure for the CKB Ecosystem](https://talk.nervos.org/t/spark-program-ckb-builder-lab-interactive-developer-onboarding-infrastructure-for-the-ckb-ecosystem/10385/9) | devnash | 2026-07-03 05:06:18 CST | Week 1 Final Evidence: CKB Builder Lab Hello everyone, This is the Week 1 progress report for CKB Builder Lab, our approved Spark Program project focused on interactive developer onboarding infrastructure for the CKB ecosystem. Week 1 Milestone Github: GitHub - devnash11/ckb-...

## 活跃话题

1. [关于“档案、身份与遗忘”的游戏，结尾把档案存进 CKB](https://talk.nervos.org/t/ckb/10454) | 9 条近窗帖子 | 最新活动 2026-07-03 19:43:10 CST | tags: CKB, game
2. [[DIS] Werra: Building Trust Infrastructure for Creator Commerce](https://talk.nervos.org/t/dis-werra-building-trust-infrastructure-for-creator-commerce/10453) | 4 条近窗帖子 | 最新活动 2026-07-03 19:26:58 CST
3. [Application scenarios of ckb](https://talk.nervos.org/t/application-scenarios-of-ckb/10455) | 1 条近窗帖子 | 最新活动 2026-07-03 12:48:01 CST
4. [Spark Program | CellKit Actions — Reusable Transaction Actions for CKB Apps](https://talk.nervos.org/t/spark-program-cellkit-actions-reusable-transaction-actions-for-ckb-apps/10375) | 1 条近窗帖子 | 最新活动 2026-07-03 10:36:50 CST | tags: Spark-Program, Submitted
5. [Spark Program | CKB Builder Lab: Interactive Developer Onboarding Infrastructure for the CKB Ecosystem](https://talk.nervos.org/t/spark-program-ckb-builder-lab-interactive-developer-onboarding-infrastructure-for-the-ckb-ecosystem/10385) | 1 条近窗帖子 | 最新活动 2026-07-03 05:06:18 CST | tags: In-Progress, Spark-Program

## 最近帖子摘录

- 2026-07-03 19:43:10 CST | janx | [关于“档案、身份与遗忘”的游戏，结尾把档案存进 CKB](https://talk.nervos.org/t/ckb/10454/9) | Thanks for sharing! I really enjoyed the story and the music.
- 2026-07-03 19:26:58 CST | DWSQUIRES | [[DIS] Werra: Building Trust Infrastructure for Creator Commerce](https://talk.nervos.org/t/dis-werra-building-trust-infrastructure-for-creator-commerce/10453/7) | Hi @neon.bit Thank you for the thoughtful feedback. I agree with your point. I’m taking this advice seriously and advance the current prototype into a clearer proof of concept...
- 2026-07-03 16:13:18 CST | neon.bit | [[DIS] Werra: Building Trust Infrastructure for Creator Commerce](https://talk.nervos.org/t/dis-werra-building-trust-infrastructure-for-creator-commerce/10453/6) | Hi @DWSQUIRES Thanks for your proposal, glad to see you are considering solutions for businesses and content creators in the form of escrow platforms. Generally speaking, the...
- 2026-07-03 12:48:01 CST | ckbbkc | [Application scenarios of ckb](https://talk.nervos.org/t/application-scenarios-of-ckb/10455/1) | RWA？，how to work with AI?
- 2026-07-03 10:36:50 CST | Fidelcoder | [Spark Program | CellKit Actions — Reusable Transaction Actions for CKB Apps](https://talk.nervos.org/t/spark-program-cellkit-actions-reusable-transaction-actions-for-ckb-apps/10375/6) | @xingtianchunyan Hello, I’ve not heard from you since my previous response/clarification!
- 2026-07-03 10:34:34 CST | zz_tovarishch | [关于“档案、身份与遗忘”的游戏，结尾把档案存进 CKB](https://talk.nervos.org/t/ckb/10454/8) | 轻量化 轻量化
- 2026-07-03 10:32:10 CST | RetricSu | [关于“档案、身份与遗忘”的游戏，结尾把档案存进 CKB](https://talk.nervos.org/t/ckb/10454/7) | 明白了，我以为会把完整档案上传到链上，更多看起来是一些元数据？
- 2026-07-03 10:23:30 CST | zz_tovarishch | [关于“档案、身份与遗忘”的游戏，结尾把档案存进 CKB](https://talk.nervos.org/t/ckb/10454/6) | 实现方式很简单： 结局页生成 JSON schema 大概是： { "p": "masked-identity", "v": 1, "e": "erased", "t": 0, "s": 100, "i": 0, "l": "en", "d": "2026-07-02", "n": "optional archivist name" } 字段含义：...
- 2026-07-03 10:16:50 CST | RetricSu | [关于“档案、身份与遗忘”的游戏，结尾把档案存进 CKB](https://talk.nervos.org/t/ckb/10454/5) | image1920×974 159 KB 请问链上存的副本具体是什么信息？这里可以把这些信息decode出来吗？
- 2026-07-03 09:56:00 CST | Fisher | [关于“档案、身份与遗忘”的游戏，结尾把档案存进 CKB](https://talk.nervos.org/t/ckb/10454/4) | 搞个基于爱泼斯坦档案审判特朗普的游戏
- 2026-07-03 09:08:23 CST | RetricSu | [关于“档案、身份与遗忘”的游戏，结尾把档案存进 CKB](https://talk.nervos.org/t/ckb/10454/3) | 这个真的很棒！从你的游戏的创意、文本内容的编写，以及你特意选择了很轻量、甚至是某种可选的、和链上结合的方式，我能感觉出来你做这个东西真的有注入许多自己的想法。 我觉得这样的应用会让我眼前一亮，让我看到 ckb 产生了不太一样的东西。这个东西是什么呢？其实就是一种调性。它不一定是 CKB 的某些技术特点产生的（不过这个游戏切入“存档”确实和 ckb...
- 2026-07-03 08:38:17 CST | DWSQUIRES | [[DIS] Werra: Building Trust Infrastructure for Creator Commerce](https://talk.nervos.org/t/dis-werra-building-trust-infrastructure-for-creator-commerce/10453/5) | @zz_tovarishch thank you for the clarification. I have updated the proposal to remove the USDI payment request and align with the DAO’s supported payment terms. The grant...
- 2026-07-03 08:35:58 CST | ckbbkc | [关于“档案、身份与遗忘”的游戏，结尾把档案存进 CKB](https://talk.nervos.org/t/ckb/10454/2) | 可以考虑推出一个富豪版的个人故事，心得，记录的dapp，基于ckb，让富豪们留下永远不会消失的消息（ckb如果能一直运行下去）
- 2026-07-03 07:54:45 CST | zz_tovarishch | [关于“档案、身份与遗忘”的游戏，结尾把档案存进 CKB](https://talk.nervos.org/t/ckb/10454/1) | 做了一个小型网页叙事游戏， 《Masked Identity》。 这是一个什么游戏？ 《Masked Identity》是一个基于我个人经历改写的互动叙事游戏。它把一些真实经验、历史想象和对制度性记忆的探讨，放进一个架空的苏联末期军事医院里。 1920×833 281 KB...
- 2026-07-03 05:06:18 CST | devnash | [Spark Program | CKB Builder Lab: Interactive Developer Onboarding Infrastructure for the CKB Ecosystem](https://talk.nervos.org/t/spark-program-ckb-builder-lab-interactive-developer-onboarding-infrastructure-for-the-ckb-ecosystem/10385/9) | Week 1 Final Evidence: CKB Builder Lab Hello everyone, This is the Week 1 progress report for CKB Builder Lab, our approved Spark Program project focused on interactive...
- 2026-07-03 02:35:12 CST | zz_tovarishch | [[DIS] Werra: Building Trust Infrastructure for Creator Commerce](https://talk.nervos.org/t/dis-werra-building-trust-infrastructure-for-creator-commerce/10453/4) | DWSQUIRES: preferably paid in USDI 你好，目前DAO没有基于USDI的支付选项 你可以选择以固定CKB支付或者以固定的USD额度支付 [DIS] Fiber Desktop v1 ground-up rebuild and launch — fnn desktop app CKB Community Fund DAO...
