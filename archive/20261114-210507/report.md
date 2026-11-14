# Nervos Talk 社区简报

- 统计窗口: 2026-11-14 05:05:07 CST 到 2026-11-15 05:05:07 CST
- 生成时间: 2026-11-15 05:05:14 CST
- 话题数: 7
- 帖子数: 7
- 作者数: 7
- 总结模式: ai:openai-compatible

## 社区总结

## 今日发生了什么

今天论坛最集中的动态是 Spark Program 下出现三则新项目/申请帖：ServiceSeal 计划在 CKB 上做预付费公用事业通行证并在拉各斯充电亭试点 [S01]；secnev 要做 CKB 原生风险观测站 [S02]；TITANHOLD CKB Pay 计划做开源 CKB 结账模块 [S06]。同时，开发者工具和测试网也有进展：ckbup 已能安装五个 CKB 命令行工具 [S04]；CKB IDL 的 Milestone 0 基础报告进入草案审阅 [S05]；Twine 测试网 beta 更新了与 Fiber Studio 和 Cellula Wallet 的配合 [S07]。FiberNuts 讨论中有人询问初始资金支付时间并表示准备开工 [S03]。

## 重点话题

- Spark Program 下出现 ServiceSeal 提案，申请 900 美元、周期 6 周，目标是在 CKB 上做预付费公用事业通行证，并在拉各斯充电亭试点 [S01]。
- secnev 提出 CKB 原生风险观测站，面向 CKB 稳定币、金库、xUDT/RGB++ 代币和钱包，把 live cells、脚本、池子和协议状态转成可解释风险评分 [S02]。
- TITANHOLD CKB Pay 计划做一个开源 CKB 结账模块，让 TITANHOLD 客户订单可以通过 CKB 网络支付 [S06]。
- ckbup 更新称现在可安装五个工具，覆盖 ckb、fnn、ckb-light-client、ckb-debugger 和 ckb-cli [S04]。
- Twine 测试网 beta 更新称可与 Fiber Studio 和 Cellula Wallet 配合，Fiber Studio 是运行官方 Fiber 节点的桌面应用，Cellula Wallet 是浏览器和 Android 钱包并通过 Fiber 支付 [S07]。FiberNuts 线程中有人追问初始资金何时支付，并表示已准备好开工 [S03]。

## 值得继续跟进

- ServiceSeal 已给出 900 美元申请和 6 周时间表 [S01]；secnev 和 TITANHOLD CKB Pay 目前展示的是项目概览/计划 [S02, S06]，后续是否获批、资金和交付节奏值得观察。
- ckbup 仍以“早期进展、欢迎反馈”的方式发布 [S04]，安装体验和后续工具覆盖是否继续扩展值得跟进。
- CKB IDL 的 Milestone 0 报告是草案，基础交付物可供审阅，最终收尾事项仍列在帖中 [S05]。Twine 测试网 beta 帖子邀请帮助测试不通过交易所买卖 CKB [S07]，更新说明其可与 Fiber Studio 和 Cellula Wallet 配合 [S07]。FiberNuts 线程中初始资金支付时间尚待答复 [S03]。

## 来源索引

- `S01` [Spark Program | ServiceSeal: Prepaid Utility Passes on CKB](https://talk.nervos.org/t/spark-program-serviceseal-prepaid-utility-passes-on-ckb/11215/1) | hardik | 2026-11-15 01:06:34 CST | Spark Program | ServiceSeal: Prepaid Utility Passes on CKB, Piloted at a Charging Kiosk in Lagos Applicant: Hardik Azmi (GitHub: DegenerateAlchemist (Yugi) · GitHub ) Funding requested: $900 USD Timeline: 6 weeks Category: CKB Application / Retail Utility & State Primitives...
- `S02` [Spark Program | secnev — CKB-native risk observatory](https://talk.nervos.org/t/spark-program-secnev-ckb-native-risk-observatory/11213/1) | TolgaYazan | 2026-11-15 00:19:28 CST | 1. Project overview Project name: secnev One sentence: secnev is an open, CKB-native risk observatory that turns live cells, scripts, pools and protocol state into explainable risk scores for CKB stablecoins, vaults, xUDT/RGB++ tokens and wallets. Positioning: risk...
- `S03` [[DIS] FiberNuts: Reliable Cashu-over-Fiber Payments with Hosted-LSP Onboarding](https://talk.nervos.org/t/dis-fibernuts-reliable-cashu-over-fiber-payments-with-hosted-lsp-onboarding/11051/9) | Code3ks | 2026-11-14 20:52:53 CST | Thank you @zz_tovarishch for updating it, when would the initial funding be paid? . I am all set and ready to commence work.
- `S04` [Ckbup: one installer for CKB command-line tools (early progress, feedback welcome)](https://talk.nervos.org/t/ckbup-one-installer-for-ckb-command-line-tools-early-progress-feedback-welcome/11188/2) | Steven_Hert | 2026-11-14 16:14:57 CST | Update: ckbup now installs five tools. The second step is merged. ckbup install now covers ckb, fnn and ckb-light-client as well as ckb-debugger and ckb-cli. cargo install --git https://github.com/steven3002/ckbup ckbup install ckb ckbup install fnn ckbup install ckb-light-...
- `S05` [[DIS] CKB IDL: Interface Description Language and Discoverability for CKB Scripts](https://talk.nervos.org/t/dis-ckb-idl-interface-description-language-and-discoverability-for-ckb-scripts/11031/12) | OWK50GA | 2026-11-14 11:58:59 CST | CKB IDL — Milestone 0 Foundation Report Status: Draft for publication. Foundation deliverables are available for review; final close-out items are listed below. Milestone 0 establishes the development and delivery foundation for the CKB Script Registry and the broader CKB IDL...
- `S06` [Spark Program | TITANHOLD CKB Pay](https://talk.nervos.org/t/spark-program-titanhold-ckb-pay/11211/1) | hennadii | 2026-11-14 11:08:21 CST | 1. Project Overview Project name: TITANHOLD CKB Pay One-line summary: A planned, open-source CKB checkout module so TITANHOLD client orders (taken by the Amanda assistant or the client Telegram bot) can be paid on the CKB network. Type: payment / checkout integration (library...
- `S07` [Twine testnet beta: help test buying and selling CKB without an exchange](https://talk.nervos.org/t/twine-testnet-beta-help-test-buying-and-selling-ckb-without-an-exchange/11143/2) | ebubedev | 2026-11-14 09:24:00 CST | Update. Twine works with Fiber Studio and Cellula Wallet. Fiber Studio is the desktop app. It runs the official Fiber node on your computer. Cellula Wallet is the other one, in the browser and on Android. It pays over Fiber, and you do not run a node for it. The trade is the...

## 活跃话题

1. [Spark Program | ServiceSeal: Prepaid Utility Passes on CKB](https://talk.nervos.org/t/spark-program-serviceseal-prepaid-utility-passes-on-ckb/11215) | 1 条近窗帖子 | 最新活动 2026-11-15 01:06:34 CST | tags: CKB, Spark-Program
2. [Spark Program | secnev — CKB-native risk observatory](https://talk.nervos.org/t/spark-program-secnev-ckb-native-risk-observatory/11213) | 1 条近窗帖子 | 最新活动 2026-11-15 00:19:28 CST
3. [[DIS] FiberNuts: Reliable Cashu-over-Fiber Payments with Hosted-LSP Onboarding](https://talk.nervos.org/t/dis-fibernuts-reliable-cashu-over-fiber-payments-with-hosted-lsp-onboarding/11051) | 1 条近窗帖子 | 最新活动 2026-11-14 20:52:53 CST
4. [Ckbup: one installer for CKB command-line tools (early progress, feedback welcome)](https://talk.nervos.org/t/ckbup-one-installer-for-ckb-command-line-tools-early-progress-feedback-welcome/11188) | 1 条近窗帖子 | 最新活动 2026-11-14 16:14:57 CST | tags: CKB, Infrastructure, dev-tool, fiber, rust
5. [[DIS] CKB IDL: Interface Description Language and Discoverability for CKB Scripts](https://talk.nervos.org/t/dis-ckb-idl-interface-description-language-and-discoverability-for-ckb-scripts/11031) | 1 条近窗帖子 | 最新活动 2026-11-14 11:58:59 CST | tags: CKB-IDL
6. [Spark Program | TITANHOLD CKB Pay](https://talk.nervos.org/t/spark-program-titanhold-ckb-pay/11211) | 1 条近窗帖子 | 最新活动 2026-11-14 11:08:21 CST
7. [Twine testnet beta: help test buying and selling CKB without an exchange](https://talk.nervos.org/t/twine-testnet-beta-help-test-buying-and-selling-ckb-without-an-exchange/11143) | 1 条近窗帖子 | 最新活动 2026-11-14 09:24:00 CST | tags: CKB, fiber, testnet

## 最近帖子摘录

- 2026-11-15 01:06:34 CST | hardik | [Spark Program | ServiceSeal: Prepaid Utility Passes on CKB](https://talk.nervos.org/t/spark-program-serviceseal-prepaid-utility-passes-on-ckb/11215/1) | Spark Program | ServiceSeal: Prepaid Utility Passes on CKB, Piloted at a Charging Kiosk in Lagos Applicant: Hardik Azmi (GitHub: DegenerateAlchemist (Yugi) · GitHub ) Funding...
- 2026-11-15 00:19:28 CST | TolgaYazan | [Spark Program | secnev — CKB-native risk observatory](https://talk.nervos.org/t/spark-program-secnev-ckb-native-risk-observatory/11213/1) | 1. Project overview Project name: secnev One sentence: secnev is an open, CKB-native risk observatory that turns live cells, scripts, pools and protocol state into explainable...
- 2026-11-14 20:52:53 CST | Code3ks | [[DIS] FiberNuts: Reliable Cashu-over-Fiber Payments with Hosted-LSP Onboarding](https://talk.nervos.org/t/dis-fibernuts-reliable-cashu-over-fiber-payments-with-hosted-lsp-onboarding/11051/9) | Thank you @zz_tovarishch for updating it, when would the initial funding be paid? . I am all set and ready to commence work.
- 2026-11-14 16:14:57 CST | Steven_Hert | [Ckbup: one installer for CKB command-line tools (early progress, feedback welcome)](https://talk.nervos.org/t/ckbup-one-installer-for-ckb-command-line-tools-early-progress-feedback-welcome/11188/2) | Update: ckbup now installs five tools. The second step is merged. ckbup install now covers ckb, fnn and ckb-light-client as well as ckb-debugger and ckb-cli. cargo install --git...
- 2026-11-14 11:58:59 CST | OWK50GA | [[DIS] CKB IDL: Interface Description Language and Discoverability for CKB Scripts](https://talk.nervos.org/t/dis-ckb-idl-interface-description-language-and-discoverability-for-ckb-scripts/11031/12) | CKB IDL — Milestone 0 Foundation Report Status: Draft for publication. Foundation deliverables are available for review; final close-out items are listed below. Milestone 0...
- 2026-11-14 11:08:21 CST | hennadii | [Spark Program | TITANHOLD CKB Pay](https://talk.nervos.org/t/spark-program-titanhold-ckb-pay/11211/1) | 1. Project Overview Project name: TITANHOLD CKB Pay One-line summary: A planned, open-source CKB checkout module so TITANHOLD client orders (taken by the Amanda assistant or the...
- 2026-11-14 09:24:00 CST | ebubedev | [Twine testnet beta: help test buying and selling CKB without an exchange](https://talk.nervos.org/t/twine-testnet-beta-help-test-buying-and-selling-ckb-without-an-exchange/11143/2) | Update. Twine works with Fiber Studio and Cellula Wallet. Fiber Studio is the desktop app. It runs the official Fiber node on your computer. Cellula Wallet is the other one, in...
