# Nervos Talk 社区简报

- 统计窗口: 2026-11-15 05:27:56 CST 到 2026-11-16 05:27:56 CST
- 生成时间: 2026-11-16 05:28:02 CST
- 话题数: 5
- 帖子数: 5
- 作者数: 5
- 总结模式: ai:openai-compatible

## 社区总结

## 今日发生了什么

今天 Nervos Talk 有多条项目周报和技术进展更新，涉及 Spark Program、CKB 客户端与后量子锁等方向[S01, S02, S03, S04, S05]。Corven 发布 Spark Program 第二周进度报告，称总体按计划推进但有一项变更[S01]。Seedsong 报告在测试中发现 ckb-light-client 的 bug，同时称 M3 大部分功能已完成[S03]。ShareCut 介绍了基于 Fiber 测试网的小店推荐返佣方案[S04]；隐私订单簿应用链项目称已开始开发与以太坊的跨链桥[S02]；另有团队展示了仅限测试网的 ML-DSA 后量子锁原型[S05]。

## 重点话题

- Corven 的 Spark Program 第二周进度报告称项目总体按计划推进，但有一项变更，帖子摘要没有说明变更细节[S01]。
- Seedsong 在测试中发现 ckb-light-client 的 bug，并称 M3 大部分功能已完成；帖子提到一个 storage 修复 PR 用于防止历史回放复活已花费 cells，但修复是否合入未说明[S03]。
- ShareCut 在 Spark Program 下发帖介绍面向拉各斯小店的 Fiber 测试网推荐返佣方案，推荐人通过个人链接或二维码跟踪，并由 Fiber 支付返佣[S04]。
- 基于 CKB L1 的去中心化隐私订单簿应用链发布周报，称继续论文修改并开始开发 invisibook 与以太坊之间的跨链桥[S02]。
- 有团队构建了基于 ML-DSA 的 CKB 第二个后量子锁原型，与现有 SPHINCS+ 并列；该工作仅限测试网，代码只有几天新[S05]。

## 值得继续跟进

- 跟进 Seedsong 发现的 ckb-light-client bug 及对应 storage 修复 PR 是否合入和验证完成，因为当前材料没有给出结论[S03]。
- 观察 ML-DSA 后量子锁从测试网原型走向更成熟评估的进展，当前仅为测试网原型且代码只有几天新[S05]。
- 关注 ShareCut 在 Fiber 测试网上的后续进展，以及 Corven 提到的那项变更具体是什么[S04, S01]。

## 来源索引

- `S01` [Spark Program Proposal: Corven cloud-native IDE](https://talk.nervos.org/t/spark-program-proposal-corven-cloud-native-ide/10807/17) | lestonEth | 2026-11-16 03:10:34 CST | Corven Spark Program: Week 2 Progress Report Project: Corven, a browser-based IDE for building on CKB and Fiber Network Reporting period: Week 2 (9–15 November 2026) Reported: 15 November 2026 Project website: https://corvanide.space/ Status: On track, with one change to the...
- `S02` [[DIS] Decentralized privacy order-book appchain based on CKB L1 - 2026.phase-1](https://talk.nervos.org/t/dis-decentralized-privacy-order-book-appchain-based-on-ckb-l1-2026-phase-1/10015/53) | Lawliet_Chan | 2026-11-15 21:51:45 CST | 周报 2026.11.15 继续上周的论文修改 开始开发 invisibook ↔ eth 跨链桥功能
- `S03` [[Spark Program] SeedsSpark Program | Seedsong: On-Chain Generative Music with Spore DOB and light-client-wasmong 种子唱片：基于 Spore DOB 与 light-client-wasm 的链上生成音乐](https://talk.nervos.org/t/spark-program-seedsspark-program-seedsong-on-chain-generative-music-with-spore-dob-and-light-client-wasmong-spore-dob-light-client-wasm/10997/10) | Officeyutong | 2026-11-15 20:16:37 CST | I have found a bug in ckb-light-client when testing SeedSong. Currently most features of M3 have been finished. After this PR fix(storage): prevent historical replay from resurrecting spent cells by Officeyutong · Pull Request #308 · nervosnetwork/ckb-light-client · GitHub was...
- `S04` [Spark Program | ShareCut: referral payouts for small shops over Fiber (testnet)](https://talk.nervos.org/t/spark-program-sharecut-referral-payouts-for-small-shops-over-fiber-testnet/11218/1) | abdul | 2026-11-15 17:19:31 CST | 1. Project Overview Small shops in Lagos get most new customers by word of mouth, but they rarely track it or pay the people who bring customers in. ShareCut gives each promoter a personal link or QR code. When a customer they referred pays through Fiber, the promoter’s agreed...
- `S05` [A second post-quantum lock for CKB? ML-DSA beside SPHINCS+, checked and measured](https://talk.nervos.org/t/a-second-post-quantum-lock-for-ckb-ml-dsa-beside-sphincs-checked-and-measured/11217/1) | LusoCryptoLabs | 2026-11-15 12:26:22 CST | What each signature rests on, and what that safety costs1600×900 80.3 KB This is a study and a prototype, on testnet only, with code that is days old. In short CKB has one lock today built to resist a quantum computer: SPHINCS+. We built a second one, on ML-DSA, another...

## 活跃话题

1. [Spark Program Proposal: Corven cloud-native IDE](https://talk.nervos.org/t/spark-program-proposal-corven-cloud-native-ide/10807) | 1 条近窗帖子 | 最新活动 2026-11-16 03:10:34 CST | tags: CKB, Grant, In-Progress, Spark-Program
2. [[DIS] Decentralized privacy order-book appchain based on CKB L1 - 2026.phase-1](https://talk.nervos.org/t/dis-decentralized-privacy-order-book-appchain-based-on-ckb-l1-2026-phase-1/10015) | 1 条近窗帖子 | 最新活动 2026-11-15 21:51:45 CST | tags: appchain
3. [[Spark Program] SeedsSpark Program | Seedsong: On-Chain Generative Music with Spore DOB and light-client-wasmong 种子唱片：基于 Spore DOB 与 light-client-wasm 的链上生成音乐](https://talk.nervos.org/t/spark-program-seedsspark-program-seedsong-on-chain-generative-music-with-spore-dob-and-light-client-wasmong-spore-dob-light-client-wasm/10997) | 1 条近窗帖子 | 最新活动 2026-11-15 20:16:37 CST | tags: In-Progress, Spark-Program
4. [Spark Program | ShareCut: referral payouts for small shops over Fiber (testnet)](https://talk.nervos.org/t/spark-program-sharecut-referral-payouts-for-small-shops-over-fiber-testnet/11218) | 1 条近窗帖子 | 最新活动 2026-11-15 17:19:31 CST
5. [A second post-quantum lock for CKB? ML-DSA beside SPHINCS+, checked and measured](https://talk.nervos.org/t/a-second-post-quantum-lock-for-ckb-ml-dsa-beside-sphincs-checked-and-measured/11217) | 1 条近窗帖子 | 最新活动 2026-11-15 12:26:22 CST

## 最近帖子摘录

- 2026-11-16 03:10:34 CST | lestonEth | [Spark Program Proposal: Corven cloud-native IDE](https://talk.nervos.org/t/spark-program-proposal-corven-cloud-native-ide/10807/17) | Corven Spark Program: Week 2 Progress Report Project: Corven, a browser-based IDE for building on CKB and Fiber Network Reporting period: Week 2 (9–15 November 2026) Reported:...
- 2026-11-15 21:51:45 CST | Lawliet_Chan | [[DIS] Decentralized privacy order-book appchain based on CKB L1 - 2026.phase-1](https://talk.nervos.org/t/dis-decentralized-privacy-order-book-appchain-based-on-ckb-l1-2026-phase-1/10015/53) | 周报 2026.11.15 继续上周的论文修改 开始开发 invisibook ↔ eth 跨链桥功能
- 2026-11-15 20:16:37 CST | Officeyutong | [[Spark Program] SeedsSpark Program | Seedsong: On-Chain Generative Music with Spore DOB and light-client-wasmong 种子唱片：基于 Spore DOB 与 light-client-wasm 的链上生成音乐](https://talk.nervos.org/t/spark-program-seedsspark-program-seedsong-on-chain-generative-music-with-spore-dob-and-light-client-wasmong-spore-dob-light-client-wasm/10997/10) | I have found a bug in ckb-light-client when testing SeedSong. Currently most features of M3 have been finished. After this PR fix(storage): prevent historical replay from...
- 2026-11-15 17:19:31 CST | abdul | [Spark Program | ShareCut: referral payouts for small shops over Fiber (testnet)](https://talk.nervos.org/t/spark-program-sharecut-referral-payouts-for-small-shops-over-fiber-testnet/11218/1) | 1. Project Overview Small shops in Lagos get most new customers by word of mouth, but they rarely track it or pay the people who bring customers in. ShareCut gives each promoter...
- 2026-11-15 12:26:22 CST | LusoCryptoLabs | [A second post-quantum lock for CKB? ML-DSA beside SPHINCS+, checked and measured](https://talk.nervos.org/t/a-second-post-quantum-lock-for-ckb-ml-dsa-beside-sphincs-checked-and-measured/11217/1) | What each signature rests on, and what that safety costs1600×900 80.3 KB This is a study and a prototype, on testnet only, with code that is days old. In short CKB has one lock...
