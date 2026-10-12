# Nervos Talk 社区简报

- 统计窗口: 2026-10-12 07:29:12 CST 到 2026-10-13 07:29:12 CST
- 生成时间: 2026-10-13 07:29:20 CST
- 话题数: 9
- 帖子数: 10
- 作者数: 8
- 总结模式: ai:openai-compatible

## 社区总结

## 今日发生了什么

今天 Nervos Talk 的主要动态是几条项目更新同时出现：Noir-CKB 作者在方向检查后发帖，回应 proof 放在 Lock 还是 Type，以及 Noir→Groth16 路线的问题 [S01]。Tactus O1 的 Based EVM Rollup 跟进帖承认最新实验有两个问题：ZK proof 生成约 78 分钟，CKB 验证约 3.985 billion cycles，超过主网 3.5 billion 限制 [S02]。CrowdCell 则改成一个 5,000 美元级别的测试网版本，并追加分类搜索、创作者更新、中文界面等功能 [S07, S08, S09]。整体看，今天论坛不是完全平静，测试网游戏、内容活动和节点收入层等方向也有更新 [S03, S04, S06]。

## 重点话题

- Noir-CKB 更新：作者提到一个月前做过方向检查，收到主要围绕“proof 应该放在 Lock 还是 Type”和“Noir→Groth16 是否合适”的回复 [S01]；今天帖子说明方向检查后的决定、可以尝试的内容和后续走向，但材料没有展开具体决定 [S01]。
- Tactus O1 性能瓶颈：最新实验显示，在作者笔记本上生成一个 ZK proof 大约耗时 78 分钟 [S02]；CKB 上验证消耗约 3.985 billion cycles，超过主网 3.5 billion 的限制，作者表示这是需要解决的两个问题 [S02]。
- CrowdCell/CKB Kickstarter 推进：CrowdCell 重新缩小范围，审计、费用模型和主网启动都被移出，之后作为单独提案回来 [S07]；作者随后在同样 5,000 美元和同样日期下追加分类搜索、campaign 页面创作者更新、中文界面和达标后提前 finalization [S08]；CKB Kickstarter 帖则确认提案已上线，是 5,000 美元的测试网版本，包含 dashboards、用 .cell names 和 Vellum 的创作者身份、创作者工具和 keeper tip [S09]。
- POI 测试网游戏发布技术说明：POI 是 CKB testnet 上的平台游戏，目标是让玩家通过使用来学习 .cell names [S04]；帖子作为 Scryve 介绍后的技术补充，讲每层楼在链上做什么、游戏如何构建、城镇如何运作，以及如何加入 first wave [S04]；游戏入口是 poi.cellula.id，在 CKB testnet 上免费，支持手机或电脑 [S04]。
- 其他社区动态：Rypto 发布 CKB Content & Advocacy Campaign 第二个月报告，报告期为 2026-09-01 到 2026-10-07，称产出和范围较第一个月明显提升，并引入长文 threads [S06]；节点收入层帖下有人支持，称创建了测试 campaign、应用顺畅且没遇到 bug，并认为这个概念适合 CKB cell 模型，campaign 和每笔 pledge 都可以是 cell [S03]；中文区有人提出 Tinder 版预测市场想法，讨论用类似微博问答和 meme 发射的流动性设计来激励高质量预测 [S10]；另外，Kirea Finance 相关帖子被作者删除 [S05]。

## 值得继续跟进

- Tactus O1 的性能问题是否解决：如果 ZK proof 生成时间和 CKB 验证 cycles 不能降下来，主网 3.5 billion cycle 限制会继续是硬门槛 [S02]。
- CrowdCell/CKB Kickstarter 的社区支持与交付节奏：提案刚从完整版缩为 5,000 美元测试网版，又追加了多项功能，后续是否按计划推进值得观察 [S07, S08]；CKB Kickstarter 帖提到需要 30 likes，但材料未展示完整条件 [S09]。
- Noir-CKB 的技术路线选择：proof 放 Lock 还是 Type、Noir→Groth16 是否继续，是作者公开征询后仍未在材料中披露细节的关键点 [S01]；POI first wave 和中文预测市场想法能否形成实际提案或用户反馈，也值得留意 [S04, S10]。

## 来源索引

- `S01` [Noir-CKB update: what I decided after the direction check, what you can try today, and where this is going](https://talk.nervos.org/t/noir-ckb-update-what-i-decided-after-the-direction-check-what-you-can-try-today-and-where-this-is-going/10968/1) | xiaomao | 2026-10-13 06:27:25 CST | About a month ago I shared a direction check here for noir-ckb, asking for feedback on what I was building. I got really thoughtful replies, mostly around two questions: Where should a proof live in a CKB transaction (Lock or Type?), and is Noir → Groth16 even the right...
- `S02` [Tactus O1: First Based EVM Rollup on CKB](https://talk.nervos.org/t/tactus-o1-first-based-evm-rollup-on-ckb/10861/2) | ArthurZhang | 2026-10-13 06:02:27 CST | A follow-up on Tactus O1. The latest experiments exposed two problems I need to address. Generating a ZK proof took roughly 78 minutes on my laptop, while verification on CKB consumed about 3.985 billion cycles, exceeding mainnet’s 3.5 billion limit. The prototype works on a...
- `S03` [A Revenue Layer for CKB Nodes](https://talk.nervos.org/t/a-revenue-layer-for-ckb-nodes/10734/23) | psawyerberlin | 2026-10-13 05:37:07 CST | Hi @Ayoub_Lesfer, Happy to support this. I created a test campaign on the current version and the app is nice to use. It worked smoothly and I didn’t hit any bugs. The concept is a very good fit for the CKB cell model: a campaign is a cell, each pledge is its own cell, and the...
- `S04` [POI: Proof of Identity, a platformer on CKB testnet that teaches .cell names by using them](https://talk.nervos.org/t/poi-proof-of-identity-a-platformer-on-ckb-testnet-that-teaches-cell-names-by-using-them/10967/1) | LusoCryptoLabs | 2026-10-12 23:41:20 CST | cover1920×1080 137 KB A follow-up to the introduction on Scryve, with the technical side: what each floor does on chain, how the game is built, how the town works, and how to join its first wave. Play: poi.cellula.id (CKB testnet, free, phone or computer) What it is, in one...
- `S05` [[DIS] Kirea Finance: Native RWA Lending Infrastructure for CKB |【DIS】Kirea Finance：面向 CKB 的原生 RWA 借贷基础设施](https://talk.nervos.org/t/dis-kirea-finance-native-rwa-lending-infrastructure-for-ckb-dis-kirea-finance-ckb-rwa/10809/9) | SalmanDev | 2026-10-12 22:15:13 CST | (post deleted by author)
- `S06` [[DIS] Rypto — CKB Content & Advocacy Campaign](https://talk.nervos.org/t/dis-rypto-ckb-content-advocacy-campaign/10364/8) | Rypto | 2026-10-12 19:10:52 CST | Rypto — CKB Content Campaign: Month 2 Report Reporting Period: September 1 – October 7, 2026 Overview Month 2 saw a significant step up from Month 1 in both output and scope. Alongside the continued short-form video schedule, this month introduced long-form written threads...
- `S07` [[DIS] CrowdCell: From Testnet Demo to a Crowdfunding Product on CKB | CrowdCell：把 CKB 测试网上的免信任众筹做成产品](https://talk.nervos.org/t/dis-crowdcell-from-testnet-demo-to-a-crowdfunding-product-on-ckb-crowdcell-ckb/10937/1) | Ayoub_Lesfer | 2026-10-12 16:26:15 CST | This is a smaller, rescoped version of the first CrowdCell proposal. The audit, the fee model and the mainnet launch are out of this one and will come back as a separate proposal later. Edited 2026-10-12. Added at no change to the ask: categories and search (M1), creator...
- `S08` [[DIS] CrowdCell: From Testnet Demo to a Crowdfunding Product on CKB | CrowdCell：把 CKB 测试网上的免信任众筹做成产品](https://talk.nervos.org/t/dis-crowdcell-from-testnet-demo-to-a-crowdfunding-product-on-ckb-crowdcell-ckb/10937/2) | Ayoub_Lesfer | 2026-10-12 18:02:57 CST | I added four things to the proposal at the same $5k and the same dates. Categories and search on the campaign list, creator updates on campaign pages, a Chinese interface, and early finalization once a campaign reaches its goal. They’re marked “added” in sections 8 and 9.
- `S09` [Introducing CKB Kickstarter: Decentralized All-or-Nothing Crowdfunding on Nervos CKB (Testnet MVP Live)](https://talk.nervos.org/t/introducing-ckb-kickstarter-decentralized-all-or-nothing-crowdfunding-on-nervos-ckb-testnet-mvp-live/10130/16) | Ayoub_Lesfer | 2026-10-12 16:42:17 CST | The proposal is up: [DIS] CrowdCell: From Testnet Demo to a Crowdfunding Product on CKB | CrowdCell：把 CKB 测试网上的免信任众筹做成产品 It’s the $5k testnet version: dashboards, creator identity with .cell names and Vellum, creator tooling and a keeper tip. It needs 30 likes on the first...
- `S10` [分享一个 Tinder 版预测市场应用的想法](https://talk.nervos.org/t/tinder/10407/4) | Fisher | 2026-10-12 13:17:42 CST | 关于初始流动性，不知道可不可以类比早年的微博问答模式，粉丝花费100元向大V提问题，大V回答后赚到100，之后有人如果对这个问题感兴趣需要付费查看，然后最开始提出问题的粉丝就可以从中赚钱了。回到这个长尾/利基预测市场平台，提交预测题干就相当于提问题，也可以类比成发射meme币，需要提供比如100刀流动性，后续只要参与的人多起来Ta就能从中盈利，这样也能激励所提预测的质量。

## 活跃话题

1. [Noir-CKB update: what I decided after the direction check, what you can try today, and where this is going](https://talk.nervos.org/t/noir-ckb-update-what-i-decided-after-the-direction-check-what-you-can-try-today-and-where-this-is-going/10968) | 1 条近窗帖子 | 最新活动 2026-10-13 06:27:25 CST | tags: CKB, zkp
2. [Tactus O1: First Based EVM Rollup on CKB](https://talk.nervos.org/t/tactus-o1-first-based-evm-rollup-on-ckb/10861) | 1 条近窗帖子 | 最新活动 2026-10-13 06:02:27 CST
3. [A Revenue Layer for CKB Nodes](https://talk.nervos.org/t/a-revenue-layer-for-ckb-nodes/10734) | 1 条近窗帖子 | 最新活动 2026-10-13 05:37:07 CST | tags: CKB, CKB-VM
4. [POI: Proof of Identity, a platformer on CKB testnet that teaches .cell names by using them](https://talk.nervos.org/t/poi-proof-of-identity-a-platformer-on-ckb-testnet-that-teaches-cell-names-by-using-them/10967) | 1 条近窗帖子 | 最新活动 2026-10-12 23:41:20 CST
5. [[DIS] Kirea Finance: Native RWA Lending Infrastructure for CKB |【DIS】Kirea Finance：面向 CKB 的原生 RWA 借贷基础设施](https://talk.nervos.org/t/dis-kirea-finance-native-rwa-lending-infrastructure-for-ckb-dis-kirea-finance-ckb-rwa/10809) | 1 条近窗帖子 | 最新活动 2026-10-12 22:15:13 CST | tags: CKB, DeFi, defi挖矿, lang-es, lang-zh
6. [[DIS] Rypto — CKB Content & Advocacy Campaign](https://talk.nervos.org/t/dis-rypto-ckb-content-advocacy-campaign/10364) | 1 条近窗帖子 | 最新活动 2026-10-12 19:10:52 CST
7. [[DIS] CrowdCell: From Testnet Demo to a Crowdfunding Product on CKB | CrowdCell：把 CKB 测试网上的免信任众筹做成产品](https://talk.nervos.org/t/dis-crowdcell-from-testnet-demo-to-a-crowdfunding-product-on-ckb-crowdcell-ckb/10937) | 2 条近窗帖子 | 最新活动 2026-10-12 18:02:57 CST | tags: lang-en
8. [Introducing CKB Kickstarter: Decentralized All-or-Nothing Crowdfunding on Nervos CKB (Testnet MVP Live)](https://talk.nervos.org/t/introducing-ckb-kickstarter-decentralized-all-or-nothing-crowdfunding-on-nervos-ckb-testnet-mvp-live/10130) | 1 条近窗帖子 | 最新活动 2026-10-12 16:42:17 CST | tags: CKB, dapp, lang-en
9. [分享一个 Tinder 版预测市场应用的想法](https://talk.nervos.org/t/tinder/10407) | 1 条近窗帖子 | 最新活动 2026-10-12 13:17:42 CST | tags: lang-zh

## 最近帖子摘录

- 2026-10-13 06:27:25 CST | xiaomao | [Noir-CKB update: what I decided after the direction check, what you can try today, and where this is going](https://talk.nervos.org/t/noir-ckb-update-what-i-decided-after-the-direction-check-what-you-can-try-today-and-where-this-is-going/10968/1) | About a month ago I shared a direction check here for noir-ckb, asking for feedback on what I was building. I got really thoughtful replies, mostly around two questions: Where...
- 2026-10-13 06:02:27 CST | ArthurZhang | [Tactus O1: First Based EVM Rollup on CKB](https://talk.nervos.org/t/tactus-o1-first-based-evm-rollup-on-ckb/10861/2) | A follow-up on Tactus O1. The latest experiments exposed two problems I need to address. Generating a ZK proof took roughly 78 minutes on my laptop, while verification on CKB...
- 2026-10-13 05:37:07 CST | psawyerberlin | [A Revenue Layer for CKB Nodes](https://talk.nervos.org/t/a-revenue-layer-for-ckb-nodes/10734/23) | Hi @Ayoub_Lesfer, Happy to support this. I created a test campaign on the current version and the app is nice to use. It worked smoothly and I didn’t hit any bugs. The concept...
- 2026-10-12 23:41:20 CST | LusoCryptoLabs | [POI: Proof of Identity, a platformer on CKB testnet that teaches .cell names by using them](https://talk.nervos.org/t/poi-proof-of-identity-a-platformer-on-ckb-testnet-that-teaches-cell-names-by-using-them/10967/1) | cover1920×1080 137 KB A follow-up to the introduction on Scryve, with the technical side: what each floor does on chain, how the game is built, how the town works, and how to...
- 2026-10-12 22:15:13 CST | SalmanDev | [[DIS] Kirea Finance: Native RWA Lending Infrastructure for CKB |【DIS】Kirea Finance：面向 CKB 的原生 RWA 借贷基础设施](https://talk.nervos.org/t/dis-kirea-finance-native-rwa-lending-infrastructure-for-ckb-dis-kirea-finance-ckb-rwa/10809/9) | (post deleted by author)
- 2026-10-12 19:10:52 CST | Rypto | [[DIS] Rypto — CKB Content & Advocacy Campaign](https://talk.nervos.org/t/dis-rypto-ckb-content-advocacy-campaign/10364/8) | Rypto — CKB Content Campaign: Month 2 Report Reporting Period: September 1 – October 7, 2026 Overview Month 2 saw a significant step up from Month 1 in both output and scope....
- 2026-10-12 18:02:57 CST | Ayoub_Lesfer | [[DIS] CrowdCell: From Testnet Demo to a Crowdfunding Product on CKB | CrowdCell：把 CKB 测试网上的免信任众筹做成产品](https://talk.nervos.org/t/dis-crowdcell-from-testnet-demo-to-a-crowdfunding-product-on-ckb-crowdcell-ckb/10937/2) | I added four things to the proposal at the same $5k and the same dates. Categories and search on the campaign list, creator updates on campaign pages, a Chinese interface, and...
- 2026-10-12 16:42:17 CST | Ayoub_Lesfer | [Introducing CKB Kickstarter: Decentralized All-or-Nothing Crowdfunding on Nervos CKB (Testnet MVP Live)](https://talk.nervos.org/t/introducing-ckb-kickstarter-decentralized-all-or-nothing-crowdfunding-on-nervos-ckb-testnet-mvp-live/10130/16) | The proposal is up: [DIS] CrowdCell: From Testnet Demo to a Crowdfunding Product on CKB | CrowdCell：把 CKB 测试网上的免信任众筹做成产品 It’s the $5k testnet version: dashboards, creator...
- 2026-10-12 16:26:15 CST | Ayoub_Lesfer | [[DIS] CrowdCell: From Testnet Demo to a Crowdfunding Product on CKB | CrowdCell：把 CKB 测试网上的免信任众筹做成产品](https://talk.nervos.org/t/dis-crowdcell-from-testnet-demo-to-a-crowdfunding-product-on-ckb-crowdcell-ckb/10937/1) | This is a smaller, rescoped version of the first CrowdCell proposal. The audit, the fee model and the mainnet launch are out of this one and will come back as a separate...
- 2026-10-12 13:17:42 CST | Fisher | [分享一个 Tinder 版预测市场应用的想法](https://talk.nervos.org/t/tinder/10407/4) | ...
