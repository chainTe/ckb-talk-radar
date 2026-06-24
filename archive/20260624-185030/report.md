# Nervos Talk 社区简报

- 统计窗口: 2026-06-24 02:50:30 CST 到 2026-06-25 02:50:30 CST
- 生成时间: 2026-06-25 02:50:35 CST
- 话题数: 7
- 帖子数: 11
- 作者数: 8
- 总结模式: ai:openrouter

## 社区总结

## 今日发生了什么

Nervos Talk 今天新帖不断，社区围绕 Fiber 网络基础设施和开发者工具展开密集讨论。[S01, S04, S08, S09, S11] ArthurZhang 完成了 iCKB 与 CellScript 的首次等效实验，同时 Fiber 支付黑客松和 fiber-pay 工具链都迎来新进展。[S01, S04, S08]

## 重点话题

- **CellScript 完成 iCKB 等效实验**：ArthurZhang 在 CellScript 中基本完成了首个 iCKB 等效实验，并将结果更新到论坛。[S01] phroi 表示目前较忙，预计几周后再跟进反馈。[S02]

- **Fiber 黑客松正式官宣**：neon.bit 发布 "Gone in 60ms" Fiber 网络基础设施黑客松，为期两周的 builder sprint 已开放报名，聚焦强化 Fiber 支付基础设施。[S04]

- **fiber-pay v0.2.7 发布并上线官网**：RetricSu 发布 fiber-pay 新版本，适配 FNN 0.9.0-rc4，修复 CLI 下载 pre-release 二进制的 bug，同时上线了官方落地页，为开发者提供 Fiber 的 CLI + SDK 工具链入口。[S08]

- **Vellum 身份声誉扩展提案申请资助**：truthixify 提交新提案，请求 7000 美元资助以扩展 did:ckb 的参考仪表盘和 SDK，从身份层延伸至声誉层。[S06]

- **USDI 停服引发稳定币替代讨论**：CDEX 发帖询问 USDI discontinuation 后团队是否继续引入稳定币，以及是否彻底退出 DeFi 领域。[S07]

## 值得继续跟进

- **USDI 停服后的稳定币布局**：CDEX 的提问尚未得到官方回应，需观察 Nervos 生态在稳定币和 DeFi 方向的后续动作是否存在真空。[S07]

- **Fiber 黑客松实际参与热度**：报名已开放，但 zz_tovarishch 的回复内容为空，需看两周内是否有实质性项目提交和基础设施改善落地。[S04, S05]

- **CellScript 与 iCKB 实验的后续评审**：phroi 表示数周后才能反馈，这段延迟可能影响该 DSL 在 Cell 模型上的验证进度。[S02]

## 来源索引

- `S01` [CellScript x iCKB Equivalence Experiment](https://talk.nervos.org/t/cellscript-x-ickb-equivalence-experiment/10416/1) | ArthurZhang | 2026-06-24 14:11:11 CST | @phroi small update on the iCKB / CellScript benchmark we discussed earlier. I have basically finished the first iCKB equivalence experiment in CellScript: github.com GitHub - CellScript-Labs/CellScript: Domain-specific language for the Cell model. Domain-specific language for...
- `S02` [CellScript x iCKB Equivalence Experiment](https://talk.nervos.org/t/cellscript-x-ickb-equivalence-experiment/10416/2) | phroi | 2026-06-24 23:39:33 CST | Hey @ArthurZhang, glad you put the iCKB test harness to good use!! I’m a little held up at the moment, I’ll try to get back to this in a few weeks! Cheers, Phroi
- `S03` [CellScript x iCKB Equivalence Experiment](https://talk.nervos.org/t/cellscript-x-ickb-equivalence-experiment/10416/3) | ArthurZhang | 2026-06-25 00:50:51 CST | No problem at all. Happy building, Phroi.
- `S04` [Gone in 60ms: Fiber Network Infrastructure Hackathon announcement!](https://talk.nervos.org/t/gone-in-60ms-fiber-network-infrastructure-hackathon-announcement/10418/1) | neon.bit | 2026-06-24 17:55:17 CST | image1920×1080 831 KB Gone in 60ms: Fiber Network Infrastructure Hackathon Powering the next stage of Fiber payment infrastructure Registrations are now open for Gone in 60ms: Fiber Network Infrastructure Hackathon, a two-week builder sprint focused on strengthening the...
- `S05` [Gone in 60ms: Fiber Network Infrastructure Hackathon announcement!](https://talk.nervos.org/t/gone-in-60ms-fiber-network-infrastructure-hackathon-announcement/10418/2) | zz_tovarishch | 2026-06-24 23:32:08 CST | 
- `S06` [[DIS] Vellum: Reputation Extension on did:ckb](https://talk.nervos.org/t/dis-vellum-reputation-extension-on-did-ckb/10419/1) | truthixify | 2026-06-24 23:00:49 CST | [DIS] Vellum: Reputation Extension on did:ckb Summary One-Paragraph Overview This proposal requests a grant of $7,000 to strengthen Vellum, the reference dashboard and SDK for did:ckb, and extend it from identity into reputation, building and rigorously testing the work on...
- `S07` [USDI on CKB will be discontinued. Any alternative for stablecoin?](https://talk.nervos.org/t/usdi-on-ckb-will-be-discontinued-any-alternative-for-stablecoin/10417/1) | CDEX | 2026-06-24 16:58:51 CST | I saw the announcement and was quite surprised. https://x.com/IPN_Intelligent/status/2069601671731380351 Aside from USDI, will the team continue working to introduce stablecoins, or has it completely decided to step away from the DeFi space? I’m also curious how much effort...
- `S08` [Fiber-pay: an ai-friendly CLI for fiber-network](https://talk.nervos.org/t/fiber-pay-an-ai-friendly-cli-for-fiber-network/9974/10) | RetricSu | 2026-06-24 14:31:28 CST | hello 各位，fiber-pay v0.2.7 已经发布，这个版本主要是适配了 0.9.0-rc4 版本的 FNN，以及修复了一个 CLI 下载 pre-release 的 FNN 二进制的 bug。 除此之外，更重要的可能是我们为 fiber-pay 上线了一个非常简单的落地页：fiber-pay | CKB Fiber CLI + SDK Toolchain 希望这可以提供一个入口，供开发者了解。fiber-pay 希望为社区开发者提供一个由社区维护的关于 Fiber 的 CLI + SDK 工具链的选项。
- `S09` [Introducing dir, an open directory and standing request for CKB-native ideas](https://talk.nervos.org/t/introducing-dir-an-open-directory-and-standing-request-for-ckb-native-ideas/10415/1) | truthixify | 2026-06-24 11:18:25 CST | Hey everyone, New builders keep asking the same thing: what should I build on CKB. Good answers exist, but they are scattered across forum threads, Discord, and people’s heads. dir collects them in one place. dir is an open directory of CKB-native project ideas. Each idea...
- `S10` [Introducing dir, an open directory and standing request for CKB-native ideas](https://talk.nervos.org/t/introducing-dir-an-open-directory-and-standing-request-for-ckb-native-ideas/10415/2) | RetricSu | 2026-06-24 11:54:50 CST | This is great! very inspiring
- `S11` [Spark Program | CKB Wallet Behaviour Intelligence](https://talk.nervos.org/t/spark-program-ckb-wallet-behaviour-intelligence/10338/5) | mulinya | 2026-06-24 08:32:56 CST | Hi @xingtianchunyan, Thank you for the thorough review and clear direction. I have gone through all the committee’s points and updated the proposal accordingly – the scope, budget, and deliverables now reflect exactly what was requested. One additional note: the web dashboard...

## 活跃话题

1. [CellScript x iCKB Equivalence Experiment](https://talk.nervos.org/t/cellscript-x-ickb-equivalence-experiment/10416) | 3 条近窗帖子 | 最新活动 2026-06-25 00:50:51 CST | tags: CellScript, iCKB
2. [Gone in 60ms: Fiber Network Infrastructure Hackathon announcement!](https://talk.nervos.org/t/gone-in-60ms-fiber-network-infrastructure-hackathon-announcement/10418) | 2 条近窗帖子 | 最新活动 2026-06-24 23:32:08 CST | tags: CKB, Hackathon, fiber
3. [[DIS] Vellum: Reputation Extension on did:ckb](https://talk.nervos.org/t/dis-vellum-reputation-extension-on-did-ckb/10419) | 1 条近窗帖子 | 最新活动 2026-06-24 23:00:49 CST | tags: CKB, dapp, testnet
4. [USDI on CKB will be discontinued. Any alternative for stablecoin?](https://talk.nervos.org/t/usdi-on-ckb-will-be-discontinued-any-alternative-for-stablecoin/10417) | 1 条近窗帖子 | 最新活动 2026-06-24 16:58:51 CST | tags: Nervos-项目动态
5. [Fiber-pay: an ai-friendly CLI for fiber-network](https://talk.nervos.org/t/fiber-pay-an-ai-friendly-cli-for-fiber-network/9974) | 1 条近窗帖子 | 最新活动 2026-06-24 14:31:28 CST | tags: CKB
6. [Introducing dir, an open directory and standing request for CKB-native ideas](https://talk.nervos.org/t/introducing-dir-an-open-directory-and-standing-request-for-ckb-native-ideas/10415) | 2 条近窗帖子 | 最新活动 2026-06-24 11:54:50 CST | tags: CKB, dapp
7. [Spark Program | CKB Wallet Behaviour Intelligence](https://talk.nervos.org/t/spark-program-ckb-wallet-behaviour-intelligence/10338) | 1 条近窗帖子 | 最新活动 2026-06-24 08:32:56 CST | tags: CKB, Pending, Spark-Program

## 最近帖子摘录

- 2026-06-25 00:50:51 CST | ArthurZhang | [CellScript x iCKB Equivalence Experiment](https://talk.nervos.org/t/cellscript-x-ickb-equivalence-experiment/10416/3) | No problem at all. Happy building, Phroi.
- 2026-06-24 23:39:33 CST | phroi | [CellScript x iCKB Equivalence Experiment](https://talk.nervos.org/t/cellscript-x-ickb-equivalence-experiment/10416/2) | Hey @ArthurZhang, glad you put the iCKB test harness to good use!! I’m a little held up at the moment, I’ll try to get back to this in a few weeks! Cheers, Phroi
- 2026-06-24 23:32:08 CST | zz_tovarishch | [Gone in 60ms: Fiber Network Infrastructure Hackathon announcement!](https://talk.nervos.org/t/gone-in-60ms-fiber-network-infrastructure-hackathon-announcement/10418/2) | 
- 2026-06-24 23:00:49 CST | truthixify | [[DIS] Vellum: Reputation Extension on did:ckb](https://talk.nervos.org/t/dis-vellum-reputation-extension-on-did-ckb/10419/1) | [DIS] Vellum: Reputation Extension on did:ckb Summary One-Paragraph Overview This proposal requests a grant of $7,000 to strengthen Vellum, the reference dashboard and SDK for...
- 2026-06-24 17:55:17 CST | neon.bit | [Gone in 60ms: Fiber Network Infrastructure Hackathon announcement!](https://talk.nervos.org/t/gone-in-60ms-fiber-network-infrastructure-hackathon-announcement/10418/1) | image1920×1080 831 KB Gone in 60ms: Fiber Network Infrastructure Hackathon Powering the next stage of Fiber payment infrastructure Registrations are now open for Gone in 60ms:...
- 2026-06-24 16:58:51 CST | CDEX | [USDI on CKB will be discontinued. Any alternative for stablecoin?](https://talk.nervos.org/t/usdi-on-ckb-will-be-discontinued-any-alternative-for-stablecoin/10417/1) | I saw the announcement and was quite surprised. https://x.com/IPN_Intelligent/status/2069601671731380351 Aside from USDI, will the team continue working to introduce...
- 2026-06-24 14:31:28 CST | RetricSu | [Fiber-pay: an ai-friendly CLI for fiber-network](https://talk.nervos.org/t/fiber-pay-an-ai-friendly-cli-for-fiber-network/9974/10) | hello 各位，fiber-pay v0.2.7 已经发布，这个版本主要是适配了 0.9.0-rc4 版本的 FNN，以及修复了一个 CLI 下载 pre-release 的 FNN 二进制的 bug。 除此之外，更重要的可能是我们为 fiber-pay 上线了一个非常简单的落地页：fiber-pay | CKB Fiber CLI + SDK...
- 2026-06-24 14:11:11 CST | ArthurZhang | [CellScript x iCKB Equivalence Experiment](https://talk.nervos.org/t/cellscript-x-ickb-equivalence-experiment/10416/1) | @phroi small update on the iCKB / CellScript benchmark we discussed earlier. I have basically finished the first iCKB equivalence experiment in CellScript: github.com GitHub -...
- 2026-06-24 11:54:50 CST | RetricSu | [Introducing dir, an open directory and standing request for CKB-native ideas](https://talk.nervos.org/t/introducing-dir-an-open-directory-and-standing-request-for-ckb-native-ideas/10415/2) | This is great! very inspiring
- 2026-06-24 11:18:25 CST | truthixify | [Introducing dir, an open directory and standing request for CKB-native ideas](https://talk.nervos.org/t/introducing-dir-an-open-directory-and-standing-request-for-ckb-native-ideas/10415/1) | Hey everyone, New builders keep asking the same thing: what should I build on CKB. Good answers exist, but they are scattered across forum threads, Discord, and people’s heads....
- 2026-06-24 08:32:56 CST | mulinya | [Spark Program | CKB Wallet Behaviour Intelligence](https://talk.nervos.org/t/spark-program-ckb-wallet-behaviour-intelligence/10338/5) | Hi @xingtianchunyan, Thank you for the thorough review and clear direction. I have gone through all the committee’s points and updated the proposal accordingly – the scope,...
