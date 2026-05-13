# Nervos Talk 社区简报

- 统计窗口: 2026-05-13 02:56:00 CST 到 2026-05-14 02:56:00 CST
- 生成时间: 2026-05-14 02:56:10 CST
- 话题数: 6
- 帖子数: 13
- 作者数: 8
- 总结模式: ai:openrouter

## 社区总结

## 今日发生了什么

今天社区活跃度中等，围绕生态工具的交付与解释性内容居多。[S03, S07, S10, S12] 最显眼的是一款 Fiber 网络交互式教程上线，同时 CKB 协会继续向公众澄清其定位，而 Nervos DAO Treasury 的设计讨论仍在深入。[S03, S07, S12]

## 重点话题

- **交互式 Fiber 教程出炉**：社区成员 yuqi 发布了"Fiber Storybook"，用小企鹅 Pico 的机场旅程故事讲解 Fiber 网络原理，并提供了可在线试玩的演示链接。[S03] Yeti 试用后对其中行李通道和按摩椅通道的资金归属感到困惑，yuqi 随后澄清这些流动性并非来自 Pico，而是由其他参与者提供。[S04, S05] Ckroamer 也点赞了这种讲故事的方式。[S06]

- **CKB 协会回应外界质疑**：针对"协会与 DAO 有何区别""是否在瑞士注册"等问题，CKBA 账号回复称协会旨在给生态提供更好的协调结构，强调 CKB 网络本身不由协会所有或控制。[S07, S08] 提问者 ebdalezyz_aljhny 表示对法律和治理结构的解释感到满意。[S09]

- **Fiber Desktop 工具持续打磨**：作者 ebubedev 表示会继续改进这款让普通用户在笔记本上跑 Fiber 节点的工具，目标是做到下载即用、降低门槛。[S10] Ckroamer 用中文留言称赞这对普通用户体验 Fiber 非常友好。[S11]

- **ckb-probe 发布性能评估**：Spark 项目成员 clair 分享了 ckb-probe v0.1.1 在 Docker 环境下的测试报告，包含针对特定 commit 改动的验证结果。[S01]

- **DAO Treasury 设计讨论继续**：chenyukang 回应了两处细节：一是强调基础层要保证事实可独立验证，同时钱包和浏览器需要以人类可读的方式呈现；二是关于未使用资金是否燃烧，目前仍是开放问题，核心诉求是让资金有清晰可预测的去向而非无限累积。[S12, S13]

## 值得继续跟进

- Fiber 生态的"用户友好"叙事正在加速——既有 Storybook 这类教育产品，也有 Fiber Desktop 这类降低节点门槛的工具，但两者距离真正的大规模采用还差一个"无感体验"的跳跃，需观察后续是否有更多非技术用户反馈。[S03, S10]

- CKB 协会的注册进度与治理细则尚未完全透明，虽然官方做了原则性回应，但"是否已在瑞士完成注册"这一具体问题尚未给出明确答案。[S07, S08]

- Nervos DAO Treasury 的"燃烧机制"仍处于开放讨论阶段，这对代币经济模型有长期影响，值得跟踪最终 Pre-RFC 的定稿方向。[S13]

## 来源索引

- `S01` [Spark Program | Ckb-probe: Deep Observability Tool for CKB Nodes Based on Aya Kernel eBPF/ckb-probe：基于 Aya 内核 eBPF 的 CKB 节点深度可观测性工具](https://talk.nervos.org/t/spark-program-ckb-probe-deep-observability-tool-for-ckb-nodes-based-on-aya-kernel-ebpf-ckb-probe-aya-ebpf-ckb/10008/58) | clair | 2026-05-14 02:16:52 CST | ckb-probe v0.1.1 性能评估与案例研究报告 Generated: 2026-05-13 Mode: Docker, RingBuf, threshold=1000us 环境: Linux 6.8.0-110-generic, 24 CPU, CKB testnet 一、测试背景 本次测试针对以下 commit 的改动进行验证： fix(ebpf): work around WSL2 JIT hashmap lookup bug by attach-time PID filter 将 PID 过滤从 BPF 侧 hashmap...
- `S02` [InkHaven: A CKB-Native Publishing Platform Built for Global Writers](https://talk.nervos.org/t/inkhaven-a-ckb-native-publishing-platform-built-for-global-writers/9819/36) | Ckroamer | 2026-05-14 00:19:46 CST | I’m just curious about current working progress and where I can experience it, is it still in progressing? I seldom and glad to see community members can put such efforts into developing a project that focuses on Application/Customer layer, I really hope you can keep on and...
- `S03` [Fiber Storybook: Explaining Fiber Through Pico’s Airport Journey](https://talk.nervos.org/t/fiber-storybook-explaining-fiber-through-pico-s-airport-journey/10251/1) | yuqi | 2026-05-13 09:33:20 CST | Hi everyone, I recently made Fiber Storybook, a small interactive demo that explains Fiber Network through Pico’s airport journey. Preview: https://fiber-storybook-seven.vercel.app/ GitHub: GitHub - yfeng2824/fiber-storybook · GitHub (A small note before you try it: the demo...
- `S04` [Fiber Storybook: Explaining Fiber Through Pico’s Airport Journey](https://talk.nervos.org/t/fiber-storybook-explaining-fiber-through-pico-s-airport-journey/10251/2) | Yeti | 2026-05-13 14:35:18 CST | Really cool Yuqi, thanks for making this! One thing I found a bit hard to understand was the channels for the luggage and massage chair part. Pico has a channel with 1000 CKB and the luggage channel has 5000 CKB. image1026×261 13.9 KB But I’m unsure who has funded the Luggage...
- `S05` [Fiber Storybook: Explaining Fiber Through Pico’s Airport Journey](https://talk.nervos.org/t/fiber-storybook-explaining-fiber-through-pico-s-airport-journey/10251/3) | yuqi | 2026-05-13 17:15:28 CST | Good question. In this demo, the 5,000 CKB in the luggage channel and the 100,000 sats in the massage route are not Pico’s CKB. The 1,000 CKB Pico set up earlier remains in his own payment channel with the Fiber Airport Pass. It represents the liquidity Pico makes available...
- `S06` [Fiber Storybook: Explaining Fiber Through Pico’s Airport Journey](https://talk.nervos.org/t/fiber-storybook-explaining-fiber-through-pico-s-airport-journey/10251/4) | Ckroamer | 2026-05-14 00:01:56 CST | Good work, I like the feeling of storytelling of this interactive project, keep working!
- `S07` [A New Chapter for CKB: Introducing the Common Knowledge Base Association](https://talk.nervos.org/t/a-new-chapter-for-ckb-introducing-the-common-knowledge-base-association/10249/3) | ebdalezyz_aljhny | 2026-05-13 17:03:24 CST | Is there anyone who can explain, in simple terms for non-specialists, what the purpose of creating this association is and how it differs from a DAO? Also, has it been officially registered in Switzerland? If not, why announce it before registration? Best regards.
- `S08` [A New Chapter for CKB: Introducing the Common Knowledge Base Association](https://talk.nervos.org/t/a-new-chapter-for-ckb-introducing-the-common-knowledge-base-association/10249/4) | CKBA | 2026-05-13 23:12:27 CST | Thanks for the question. In simple terms, the purpose of creating CKBA is to give the CKB ecosystem a better coordination structure. CKB itself is a decentralized public network. It is not owned or controlled by the Association, just as Bitcoin is not owned or controlled by...
- `S09` [A New Chapter for CKB: Introducing the Common Knowledge Base Association](https://talk.nervos.org/t/a-new-chapter-for-ckb-introducing-the-common-knowledge-base-association/10249/5) | ebdalezyz_aljhny | 2026-05-13 23:54:29 CST | Thank you for the clarification and for taking the time to explain the difference in a simple and practical way. The explanation regarding the legal structure versus DAO governance was especially helpful and appreciated.
- `S10` [Fiber Desktop — run Fiber (FNN) on your laptop without the “public node” headache](https://talk.nervos.org/t/fiber-desktop-run-fiber-fnn-on-your-laptop-without-the-public-node-headache/10247/3) | ebubedev | 2026-05-13 21:03:09 CST | thank you, i will be improving it from time to time, till its ready for public use and ppl can download and use without having to too much work if you have any feature you will like for me to add, feel free to let me know
- `S11` [Fiber Desktop — run Fiber (FNN) on your laptop without the “public node” headache](https://talk.nervos.org/t/fiber-desktop-run-fiber-fnn-on-your-laptop-without-the-public-node-headache/10247/4) | Ckroamer | 2026-05-13 23:28:30 CST | 很棒，这对于普通用户想要体验 Fiber 功能来说是非常好的选择
- `S12` [Pre-RFC Discussion: Activating the Nervos DAO Treasury](https://talk.nervos.org/t/pre-rfc-discussion-activating-the-nervos-dao-treasury/10143/15) | chenyukang | 2026-05-13 09:42:42 CST | On user-friendly: yes, this should be a design goal for us. The base layer should make the facts independently verifiable, while wallets, explorers, and governance interfaces should present the same information in a human-readable way. For a non-technical user, the expected...
- `S13` [Pre-RFC Discussion: Activating the Nervos DAO Treasury](https://talk.nervos.org/t/pre-rfc-discussion-activating-the-nervos-dao-treasury/10143/16) | chenyukang | 2026-05-13 09:48:31 CST | For burning unused funds: this is still an open question. The core purpose is we want unused treasury funds to have a clear and predictable path instead of accumulating forever. The intention is not necessarily that the community must create and vote on a separate “burn...

## 活跃话题

1. [Spark Program | Ckb-probe: Deep Observability Tool for CKB Nodes Based on Aya Kernel eBPF/ckb-probe：基于 Aya 内核 eBPF 的 CKB 节点深度可观测性工具](https://talk.nervos.org/t/spark-program-ckb-probe-deep-observability-tool-for-ckb-nodes-based-on-aya-kernel-ebpf-ckb-probe-aya-ebpf-ckb/10008) | 1 条近窗帖子 | 最新活动 2026-05-14 02:16:52 CST | tags: In-Progress, Spark-Program
2. [InkHaven: A CKB-Native Publishing Platform Built for Global Writers](https://talk.nervos.org/t/inkhaven-a-ckb-native-publishing-platform-built-for-global-writers/9819) | 1 条近窗帖子 | 最新活动 2026-05-14 00:19:46 CST | tags: CKB, dapp, partnership
3. [Fiber Storybook: Explaining Fiber Through Pico’s Airport Journey](https://talk.nervos.org/t/fiber-storybook-explaining-fiber-through-pico-s-airport-journey/10251) | 4 条近窗帖子 | 最新活动 2026-05-14 00:01:56 CST | tags: fiber
4. [A New Chapter for CKB: Introducing the Common Knowledge Base Association](https://talk.nervos.org/t/a-new-chapter-for-ckb-introducing-the-common-knowledge-base-association/10249) | 3 条近窗帖子 | 最新活动 2026-05-13 23:54:29 CST | tags: CKB
5. [Fiber Desktop — run Fiber (FNN) on your laptop without the “public node” headache](https://talk.nervos.org/t/fiber-desktop-run-fiber-fnn-on-your-laptop-without-the-public-node-headache/10247) | 2 条近窗帖子 | 最新活动 2026-05-13 23:28:30 CST | tags: fiber, testnet
6. [Pre-RFC Discussion: Activating the Nervos DAO Treasury](https://talk.nervos.org/t/pre-rfc-discussion-activating-the-nervos-dao-treasury/10143) | 2 条近窗帖子 | 最新活动 2026-05-13 09:48:31 CST | tags: CKB

## 最近帖子摘录

- 2026-05-14 02:16:52 CST | clair | [Spark Program | Ckb-probe: Deep Observability Tool for CKB Nodes Based on Aya Kernel eBPF/ckb-probe：基于 Aya 内核 eBPF 的 CKB 节点深度可观测性工具](https://talk.nervos.org/t/spark-program-ckb-probe-deep-observability-tool-for-ckb-nodes-based-on-aya-kernel-ebpf-ckb-probe-aya-ebpf-ckb/10008/58) | ckb-probe v0.1.1 性能评估与案例研究报告 Generated: 2026-05-13 Mode: Docker, RingBuf, threshold=1000us 环境: Linux 6.8.0-110-generic, 24 CPU, CKB testnet 一、测试背景 本次测试针对以下 commit 的改动进行验证：...
- 2026-05-14 00:19:46 CST | Ckroamer | [InkHaven: A CKB-Native Publishing Platform Built for Global Writers](https://talk.nervos.org/t/inkhaven-a-ckb-native-publishing-platform-built-for-global-writers/9819/36) | I’m just curious about current working progress and where I can experience it, is it still in progressing? I seldom and glad to see community members can put such efforts into...
- 2026-05-14 00:01:56 CST | Ckroamer | [Fiber Storybook: Explaining Fiber Through Pico’s Airport Journey](https://talk.nervos.org/t/fiber-storybook-explaining-fiber-through-pico-s-airport-journey/10251/4) | Good work, I like the feeling of storytelling of this interactive project, keep working!
- 2026-05-13 23:54:29 CST | ebdalezyz_aljhny | [A New Chapter for CKB: Introducing the Common Knowledge Base Association](https://talk.nervos.org/t/a-new-chapter-for-ckb-introducing-the-common-knowledge-base-association/10249/5) | Thank you for the clarification and for taking the time to explain the difference in a simple and practical way. The explanation regarding the legal structure versus DAO...
- 2026-05-13 23:28:30 CST | Ckroamer | [Fiber Desktop — run Fiber (FNN) on your laptop without the “public node” headache](https://talk.nervos.org/t/fiber-desktop-run-fiber-fnn-on-your-laptop-without-the-public-node-headache/10247/4) | 很棒，这对于普通用户想要体验 Fiber 功能来说是非常好的选择
- 2026-05-13 23:12:27 CST | CKBA | [A New Chapter for CKB: Introducing the Common Knowledge Base Association](https://talk.nervos.org/t/a-new-chapter-for-ckb-introducing-the-common-knowledge-base-association/10249/4) | Thanks for the question. In simple terms, the purpose of creating CKBA is to give the CKB ecosystem a better coordination structure. CKB itself is a decentralized public...
- 2026-05-13 21:03:09 CST | ebubedev | [Fiber Desktop — run Fiber (FNN) on your laptop without the “public node” headache](https://talk.nervos.org/t/fiber-desktop-run-fiber-fnn-on-your-laptop-without-the-public-node-headache/10247/3) | thank you, i will be improving it from time to time, till its ready for public use and ppl can download and use without having to too much work if you have any feature you will...
- 2026-05-13 17:15:28 CST | yuqi | [Fiber Storybook: Explaining Fiber Through Pico’s Airport Journey](https://talk.nervos.org/t/fiber-storybook-explaining-fiber-through-pico-s-airport-journey/10251/3) | Good question. In this demo, the 5,000 CKB in the luggage channel and the 100,000 sats in the massage route are not Pico’s CKB. The 1,000 CKB Pico set up earlier remains in his...
- 2026-05-13 17:03:24 CST | ebdalezyz_aljhny | [A New Chapter for CKB: Introducing the Common Knowledge Base Association](https://talk.nervos.org/t/a-new-chapter-for-ckb-introducing-the-common-knowledge-base-association/10249/3) | Is there anyone who can explain, in simple terms for non-specialists, what the purpose of creating this association is and how it differs from a DAO? Also, has it been...
- 2026-05-13 14:35:18 CST | Yeti | [Fiber Storybook: Explaining Fiber Through Pico’s Airport Journey](https://talk.nervos.org/t/fiber-storybook-explaining-fiber-through-pico-s-airport-journey/10251/2) | Really cool Yuqi, thanks for making this! One thing I found a bit hard to understand was the channels for the luggage and massage chair part. Pico has a channel with 1000 CKB...
- 2026-05-13 09:48:31 CST | chenyukang | [Pre-RFC Discussion: Activating the Nervos DAO Treasury](https://talk.nervos.org/t/pre-rfc-discussion-activating-the-nervos-dao-treasury/10143/16) | For burning unused funds: this is still an open question. The core purpose is we want unused treasury funds to have a clear and predictable path instead of accumulating forever....
- 2026-05-13 09:42:42 CST | chenyukang | [Pre-RFC Discussion: Activating the Nervos DAO Treasury](https://talk.nervos.org/t/pre-rfc-discussion-activating-the-nervos-dao-treasury/10143/15) | On user-friendly: yes, this should be a design goal for us. The base layer should make the facts independently verifiable, while wallets, explorers, and governance interfaces...
- 2026-05-13 09:33:20 CST | yuqi | [Fiber Storybook: Explaining Fiber Through Pico’s Airport Journey](https://talk.nervos.org/t/fiber-storybook-explaining-fiber-through-pico-s-airport-journey/10251/1) | Hi everyone, I recently made Fiber Storybook, a small interactive demo that explains Fiber Network through Pico’s airport journey. Preview: https://fiber-storybook-...
