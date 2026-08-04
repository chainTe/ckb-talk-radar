# Nervos Talk 社区简报

- 统计窗口: 2026-08-03 11:31:36 CST 到 2026-08-04 11:31:36 CST
- 生成时间: 2026-08-04 11:31:45 CST
- 话题数: 8
- 帖子数: 10
- 作者数: 9
- 总结模式: ai:openai-compatible

## 社区总结

## 今日发生了什么

过去 24 小时，Nervos Talk 最集中的动态是开发者工具密集发布：一位开发者发布了 CKB 交互式教学工具 “CKB Lab”，并很快获得了社区热心反馈 [S01, S02]。与此同时，Fiber 生态连续冒出多个新项目，覆盖商户支付、网页端支付协议和 Swap 原型，社区整体处于“开发者自发贡献 + 互相提建议”的活跃节奏 [S05, S07, S09]。

## 重点话题

- **CKB Lab 发布并收到建设性反馈**：开发者 timnguyen 自述利用时间构建了这个互动式开发者练习场，让用户通过填表构建真实 CKB 交易来理解每个概念 [S01]。社区成员 yixiu 称赞其 UI/UX 体验，认为它对不熟悉 CKB 的人很友好，并建议作者在工具中接入 CCC skills，因为主流 AI 模型对 CKB 编程的训练数据有限，容易产生无法上链的“幻觉代码” [S02]。作者随后感谢反馈，称会采纳建议 [S03]。

- **Fiber 商户支付工具 FiberFlow 亮相**：开发者 ebubedev 发布了面向 Fiber Network 的自托管商户支付基础设施，定位类似 Stripe 的收款层，包含落地页、商户仪表盘、托管支付页、发票 API 和 webhooks，并提供了 live demo [S05]。

- **多个 Spark 项目同日更新**：Fiber RGB++ Swap 放出了原型仓库链接 [S07]；Cell Sandbox 作者回应了社区评审，承认上一版界面过早暴露了太多实现细节，并表示已做修改 [S08]；Cellar 讨论中则明确了 v0 版本更适合 payload/reference 型存储（如元数据、哈希、指针等），不适用于需要自身 type script 的借款人 cell [S04]。

- **底层协议规范与理念讨论并行**：有人发布了 Treasury Lock Script 的规范说明，指出 treasury cell 只能由共识创建，类似于 cell base [S06]。另有一篇关于 “Fiber WebLN” 的文章，提出借鉴 WebLN 的思路，让网站“请求支付”而不是接管用户钱包 [S09]。

- **长期项目继续推进**：基于 CKB L1 的去中心化隐私订单簿 appchain 更新了周报，提到上周完成了用 co-zk 实现的组件，并正在继续撰写 invisibook 论文的安全分析部分 [S10]。

## 值得继续跟进

- **CKB Lab 能否借 CCC skills 补齐 AI 短板**：作者已明确表示会接入社区推荐的 CCC skills，后续版本的可用性和工具定位值得观察 [S02, S03]。

- **Cellar 的 type slot 设计取舍**：目前 v0 被定位为只适合 payload/reference 型存储，这对借款人 cell 场景构成限制，后续如何演进值得关注 [S04]。

- **Fiber 生态多项早期项目能否走向可用**：FiberFlow 刚发布 demo、Fiber RGB++ Swap 只有原型、Fiber WebLN 还停留在理念阶段，三者的成熟度都还很低，后续是否有实际落地进展是观察重点 [S05, S07, S09]。

## 来源索引

- `S01` [CKB Lab: Interactive developer playground & transaction builder for CKB](https://talk.nervos.org/t/ckb-lab-interactive-developer-playground-transaction-builder-for-ckb/10573/1) | timnguyen | 2026-08-03 19:00:37 CST | CKB Lab — a small CKB dev lab I built while learning. Would love your feedback Hi everyone, I’ve spent my CKBuilder time making “CKB Lab” a developer lab where each page takes one CKB concept and tries to make it concrete by building a real transaction: you fill in a form,...
- `S02` [CKB Lab: Interactive developer playground & transaction builder for CKB](https://talk.nervos.org/t/ckb-lab-interactive-developer-playground-transaction-builder-for-ckb/10573/2) | yixiu.ckbfans.bit | 2026-08-03 22:03:59 CST | 这个工具的UI/UX体验让我感觉很舒服，要做到这样很难，尤其是对CKB不太熟悉的情况下，可见你对此花了不少心血。 我看到你的代码里用到了CCC的库，这是正确的选择，它可以帮助你更好地组装交易、与链上交互。目前主流的AI模型对CKB编程的训练数据有限，很多代码AI只能靠幻觉输出，构造出来的交易不对或者无法上链。要提高CKB编程的代码准确率，我推荐在你的开发工具中加入CCC的skills： npx skills add ckb-devrel/ccc --all 还有一个小技巧是：ccc playground...
- `S03` [CKB Lab: Interactive developer playground & transaction builder for CKB](https://talk.nervos.org/t/ckb-lab-interactive-developer-playground-transaction-builder-for-ckb/10573/3) | timnguyen | 2026-08-04 11:18:31 CST | Thank you so much for the feedback on the UI/UX! It’s a huge motivation for me to keep bringing helpful tools to the community. The CCC skills tip is super helpful; I’ll definitely add it to my workspace and check out the playground as well.
- `S04` [Spark Program | Cellar — A Capacity Leasing Market for CKB Cells](https://talk.nervos.org/t/spark-program-cellar-a-capacity-leasing-market-for-ckb-cells/10492/10) | Hanssen | 2026-08-04 10:14:16 CST | Carlos_Bunny: Since the Cellar covenant uses the type slot, v0 is better suited for payload/reference-style storage: metadata, hashes, pointers, registry entries, indexable app data, or temporary records. It is not suitable for borrower cells that need their own type script,...
- `S05` [FiberFlow — self-hosted merchant payments for Fiber (try the live demo)](https://talk.nervos.org/t/fiberflow-self-hosted-merchant-payments-for-fiber-try-the-live-demo/10574/1) | ebubedev | 2026-08-04 04:53:09 CST | Hey everyone, I’ve been building FiberFlow — merchant payment infrastructure for the Fiber Network on Nervos CKB. Think of it as a checkout layer stores can plug into: landing page, merchant dashboard, hosted payment page, invoice API, and webhooks — similar in role to Stripe...
- `S06` [A new treasury cell is generated every block](https://talk.nervos.org/t/a-new-treasury-cell-is-generated-every-block/10526/3) | knmo | 2026-08-04 03:14:11 CST | Treasury Lock Script Specification [ⁿ] This spec describes a lock script used in a treasury system. See design document. Introduction A cell with a treasury lock script is called a treasury cell. Treasury cells can only be created by consensus, similar to a cell base. A...
- `S07` [Spark Program | Fiber RGB++ Swap](https://talk.nervos.org/t/spark-program-fiber-rgb-swap/10487/10) | Carl | 2026-08-03 22:33:00 CST | here is the prototype GitHub - oxdev6/Fiber-RGB-Swap · GitHub Screenshot 2026-08-03 173046870×733 31.9 KB
- `S08` [Spark Program | Cell Sandbox — A Visual Playground for the CKB Cell Model](https://talk.nervos.org/t/spark-program-cell-sandbox-a-visual-playground-for-the-ckb-cell-model/10326/22) | zynor | 2026-08-03 22:31:15 CST | Hi Yixiu, Thank you for the detailed review. Your criticism was fair for the version you tested. In particular, the interface still exposed too much implementation detail too early, and I should not have treated functional test results as evidence of usability. I have now...
- `S09` [From WebLN to Fiber WebLN: Let Websites Request Payments, Not Take Over Wallets](https://talk.nervos.org/t/from-webln-to-fiber-webln-let-websites-request-payments-not-take-over-wallets/10571/1) | Sonny | 2026-08-03 13:57:28 CST | From WebLN to Fiber WebLN: Let Websites Request Payments, Not Take Over Wallets Hi everyone, I’m Sonny. Over the past few months, I have built several small projects around Fiber Network: from One-click Start Fiber Network and a Fiber dashboard to Chat-and-Pay and an EV...
- `S10` [[DIS] Decentralized privacy order-book appchain based on CKB L1 - 2026.phase-1](https://talk.nervos.org/t/dis-decentralized-privacy-order-book-appchain-based-on-ckb-l1-2026-phase-1/10015/38) | Lawliet_Chan | 2026-08-03 13:57:06 CST | 周报 2026.8.2 benchmark 上周用co-zk实现的组件 继续撰写invisibook论文的 security analysis section

## 活跃话题

1. [CKB Lab: Interactive developer playground & transaction builder for CKB](https://talk.nervos.org/t/ckb-lab-interactive-developer-playground-transaction-builder-for-ckb/10573) | 3 条近窗帖子 | 最新活动 2026-08-04 11:18:31 CST | tags: CKB, CKB-VM, lang-en
2. [Spark Program | Cellar — A Capacity Leasing Market for CKB Cells](https://talk.nervos.org/t/spark-program-cellar-a-capacity-leasing-market-for-ckb-cells/10492) | 1 条近窗帖子 | 最新活动 2026-08-04 10:14:16 CST | tags: Spark-Program, Submitted
3. [FiberFlow — self-hosted merchant payments for Fiber (try the live demo)](https://talk.nervos.org/t/fiberflow-self-hosted-merchant-payments-for-fiber-try-the-live-demo/10574) | 1 条近窗帖子 | 最新活动 2026-08-04 04:53:09 CST | tags: fiber
4. [A new treasury cell is generated every block](https://talk.nervos.org/t/a-new-treasury-cell-is-generated-every-block/10526) | 1 条近窗帖子 | 最新活动 2026-08-04 03:14:11 CST
5. [Spark Program | Fiber RGB++ Swap](https://talk.nervos.org/t/spark-program-fiber-rgb-swap/10487) | 1 条近窗帖子 | 最新活动 2026-08-03 22:33:00 CST | tags: Pending, Spark-Program
6. [Spark Program | Cell Sandbox — A Visual Playground for the CKB Cell Model](https://talk.nervos.org/t/spark-program-cell-sandbox-a-visual-playground-for-the-ckb-cell-model/10326) | 1 条近窗帖子 | 最新活动 2026-08-03 22:31:15 CST | tags: In-Progress, Spark-Program, lang-en
7. [From WebLN to Fiber WebLN: Let Websites Request Payments, Not Take Over Wallets](https://talk.nervos.org/t/from-webln-to-fiber-webln-let-websites-request-payments-not-take-over-wallets/10571) | 1 条近窗帖子 | 最新活动 2026-08-03 13:57:28 CST | tags: CKB, fiber
8. [[DIS] Decentralized privacy order-book appchain based on CKB L1 - 2026.phase-1](https://talk.nervos.org/t/dis-decentralized-privacy-order-book-appchain-based-on-ckb-l1-2026-phase-1/10015) | 1 条近窗帖子 | 最新活动 2026-08-03 13:57:06 CST | tags: appchain

## 最近帖子摘录

- 2026-08-04 11:18:31 CST | timnguyen | [CKB Lab: Interactive developer playground & transaction builder for CKB](https://talk.nervos.org/t/ckb-lab-interactive-developer-playground-transaction-builder-for-ckb/10573/3) | Thank you so much for the feedback on the UI/UX! It’s a huge motivation for me to keep bringing helpful tools to the community. The CCC skills tip is super helpful; I’ll...
- 2026-08-04 10:14:16 CST | Hanssen | [Spark Program | Cellar — A Capacity Leasing Market for CKB Cells](https://talk.nervos.org/t/spark-program-cellar-a-capacity-leasing-market-for-ckb-cells/10492/10) | Carlos_Bunny: Since the Cellar covenant uses the type slot, v0 is better suited for payload/reference-style storage: metadata, hashes, pointers, registry entries, indexable app...
- 2026-08-04 04:53:09 CST | ebubedev | [FiberFlow — self-hosted merchant payments for Fiber (try the live demo)](https://talk.nervos.org/t/fiberflow-self-hosted-merchant-payments-for-fiber-try-the-live-demo/10574/1) | Hey everyone, I’ve been building FiberFlow — merchant payment infrastructure for the Fiber Network on Nervos CKB. Think of it as a checkout layer stores can plug into: landing...
- 2026-08-04 03:14:11 CST | knmo | [A new treasury cell is generated every block](https://talk.nervos.org/t/a-new-treasury-cell-is-generated-every-block/10526/3) | Treasury Lock Script Specification [ⁿ] This spec describes a lock script used in a treasury system. See design document. Introduction A cell with a treasury lock script is...
- 2026-08-03 22:33:00 CST | Carl | [Spark Program | Fiber RGB++ Swap](https://talk.nervos.org/t/spark-program-fiber-rgb-swap/10487/10) | here is the prototype GitHub - oxdev6/Fiber-RGB-Swap · GitHub Screenshot 2026-08-03 173046870×733 31.9 KB
- 2026-08-03 22:31:15 CST | zynor | [Spark Program | Cell Sandbox — A Visual Playground for the CKB Cell Model](https://talk.nervos.org/t/spark-program-cell-sandbox-a-visual-playground-for-the-ckb-cell-model/10326/22) | Hi Yixiu, Thank you for the detailed review. Your criticism was fair for the version you tested. In particular, the interface still exposed too much implementation detail too...
- 2026-08-03 22:03:59 CST | yixiu.ckbfans.bit | [CKB Lab: Interactive developer playground & transaction builder for CKB](https://talk.nervos.org/t/ckb-lab-interactive-developer-playground-transaction-builder-for-ckb/10573/2) | 这个工具的UI/UX体验让我感觉很舒服，要做到这样很难，尤其是对CKB不太熟悉的情况下，可见你对此花了不少心血。...
- 2026-08-03 19:00:37 CST | timnguyen | [CKB Lab: Interactive developer playground & transaction builder for CKB](https://talk.nervos.org/t/ckb-lab-interactive-developer-playground-transaction-builder-for-ckb/10573/1) | CKB Lab — a small CKB dev lab I built while learning. Would love your feedback Hi everyone, I’ve spent my CKBuilder time making “CKB Lab” a developer lab where each page takes...
- 2026-08-03 13:57:28 CST | Sonny | [From WebLN to Fiber WebLN: Let Websites Request Payments, Not Take Over Wallets](https://talk.nervos.org/t/from-webln-to-fiber-webln-let-websites-request-payments-not-take-over-wallets/10571/1) | From WebLN to Fiber WebLN: Let Websites Request Payments, Not Take Over Wallets Hi everyone, I’m Sonny. Over the past few months, I have built several small projects around...
- 2026-08-03 13:57:06 CST | Lawliet_Chan | [[DIS] Decentralized privacy order-book appchain based on CKB L1 - 2026.phase-1](https://talk.nervos.org/t/dis-decentralized-privacy-order-book-appchain-based-on-ckb-l1-2026-phase-1/10015/38) | 周报 2026.8.2 benchmark 上周用co-zk实现的组件 继续撰写invisibook论文的 security analysis section
