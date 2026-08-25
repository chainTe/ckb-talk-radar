# Nervos Talk 社区简报

- 统计窗口: 2026-08-25 01:28:54 CST 到 2026-08-26 01:28:54 CST
- 生成时间: 2026-08-26 01:28:58 CST
- 话题数: 3
- 帖子数: 3
- 作者数: 3
- 总结模式: ai:openai-compatible

## 社区总结

## 今日发生了什么

今天 Nervos Talk 整体比较平静，主要更新集中在三个主题：一个新开发者工具 Orbital 亮相、Proof of Buy 共识讨论继续推进、以及 CKB 生态双周更新 #23 发布。[S01, S02, S03] 其中 Orbital 是今天唯一的新帖，另外两个都是既有讨论的延续。[S01, S02, S03]

## 重点话题

- 社区成员 vibes 发布了 Orbital，定位是 CKB 的开发者环境，目标是让构建和部署 CKB 应用的过程不再像“一堆断开的步骤”，但目前帖子内容在“Live:”处截断，具体开放状态和体验方式还不完整。[S01]
- Proof of Buy 讨论更新到 29 楼，作者回应了“为什么不直接把 L1 token 烧掉”的疑问：PoB 的设计前提是希望更多应用链作为 L2 挂载在 L1 上，因此要考虑大规模可持续使用；如果销毁速度超过增发速度，本质是在消灭 L1 的财富，可能导致流动性枯竭甚至消亡，并不利于 L1 加众多 L2 的可持续发展。[S02]
- 生态双周更新 #23 发布，已能看到的基础设施部分包括：@CKBdev 推出了 Tentacle v0.7.7，并对 light-client 相关代码做了收紧；不过原帖在“tightened light-client...”处截断，完整进展需要点进原帖查看。[S03]

## 值得继续跟进

- Orbital 目前只露出一个“Live”的尾巴，后续值得关注它是否开放了公开测试、文档或具体链接，以及它在开发体验上究竟解决了什么痛点。[S01]
- Proof of Buy 的“不销毁 L1 token”立场已经明确，但燃烧速度与增发速度的关系、流动性风险的量化边界还没有展开，后续可以观察是否有更多设计细节被讨论。[S02]
- 双周更新 #23 的正文被截断，除了 Tentacle 和 light-client 之外是否还有其他值得注意的生态或开发者工具进展，需要直接到原帖确认。[S03]

## 来源索引

- `S01` [A New Development Experience for CKB](https://talk.nervos.org/t/a-new-development-experience-for-ckb/10663/1) | vibes | 2026-08-25 18:54:08 CST | I’ve been building something for the CKB ecosystem that I think is worth putting in front of the community. Orbital is a developer environment for building and deploying CKB applications without having the development process feel like a collection of disconnected steps. Live:...
- `S02` [Proof of Buy，一种专为Layer1设计的Layer2共识](https://talk.nervos.org/t/proof-of-buy-layer1-layer2/9752/29) | Lawliet_Chan | 2026-08-25 17:24:41 CST | why NOT burn 会有人疑问为何不将L1的token直接烧掉，这样可以制造通缩从而抬升L1 token的币价。首先，要强调一个前提，proof of buy的设计是希望更多的应用链可以作为L2挂载在L1上，也就意味着我们预先考虑的一个问题是如何让proof of buy在L1上可以大规模可持续性的使用。 此时，如果将L1 token燃烧掉，我们将可能面临两个后果： 当燃烧速度 > L1 token的增发速度，其本质是在消灭L1的财富，L1将面临流动性枯竭甚至消亡的可能。这并不是一个可以让 L1 + 众多 L2可持续发展的方式 当燃烧速度...
- `S03` [CKB Ecosystem Biweekly Update](https://talk.nervos.org/t/ckb-ecosystem-biweekly-update/9821/27) | zz_tovarishch | 2026-08-25 11:22:47 CST | image690×388 97.5 KB CKB Ecosystem Biweekly Update #23 Welcome to the latest CKB Ecosystem Biweekly Update. Here’s a quick summary of key dev and ecosystem progress from the past two weeks. Infrastructure & Tooling @CKBdev shipped Tentacle v0.7.7, tightened light-client...

## 活跃话题

1. [A New Development Experience for CKB](https://talk.nervos.org/t/a-new-development-experience-for-ckb/10663) | 1 条近窗帖子 | 最新活动 2026-08-25 18:54:08 CST | tags: CKB, CKB-VM
2. [Proof of Buy，一种专为Layer1设计的Layer2共识](https://talk.nervos.org/t/proof-of-buy-layer1-layer2/9752) | 1 条近窗帖子 | 最新活动 2026-08-25 17:24:41 CST | tags: lang-zh, 共识协议
3. [CKB Ecosystem Biweekly Update](https://talk.nervos.org/t/ckb-ecosystem-biweekly-update/9821) | 1 条近窗帖子 | 最新活动 2026-08-25 11:22:47 CST | tags: Ecosystem-Update, lang-en

## 最近帖子摘录

- 2026-08-25 18:54:08 CST | vibes | [A New Development Experience for CKB](https://talk.nervos.org/t/a-new-development-experience-for-ckb/10663/1) | I’ve been building something for the CKB ecosystem that I think is worth putting in front of the community. Orbital is a developer environment for building and deploying CKB...
- 2026-08-25 17:24:41 CST | Lawliet_Chan | [Proof of Buy，一种专为Layer1设计的Layer2共识](https://talk.nervos.org/t/proof-of-buy-layer1-layer2/9752/29) | why NOT burn 会有人疑问为何不将L1的token直接烧掉，这样可以制造通缩从而抬升L1 token的币价。首先，要强调一个前提，proof of buy的设计是希望更多的应用链可以作为L2挂载在L1上，也就意味着我们预先考虑的一个问题是如何让proof of buy在L1上可以大规模可持续性的使用。 此时，如果将L1...
- 2026-08-25 11:22:47 CST | zz_tovarishch | [CKB Ecosystem Biweekly Update](https://talk.nervos.org/t/ckb-ecosystem-biweekly-update/9821/27) | image690×388 97.5 KB CKB Ecosystem Biweekly Update #23 Welcome to the latest CKB Ecosystem Biweekly Update. Here’s a quick summary of key dev and ecosystem progress from the...
