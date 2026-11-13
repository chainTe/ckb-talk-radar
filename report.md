# Nervos Talk 社区简报

- 统计窗口: 2026-11-13 06:22:28 CST 到 2026-11-14 06:22:28 CST
- 生成时间: 2026-11-14 06:22:32 CST
- 话题数: 4
- 帖子数: 5
- 作者数: 3
- 总结模式: ai:openai-compatible

## 社区总结

## 今日发生了什么

今天论坛的更新整体集中在进行中项目的阶段性回复上，没有出现全新的提案或争议帖，因此社区今天整体较平静。[S01, S02, S03, S04, S05] 最活跃的是 Twine 的 Fiber P2P 场外交易概念验证帖：作者先回应了手续费设计反馈，随后贴出了一段从 790605a 到 504c990 的改动说明。[S01, S02] 另外两个 Spark 相关项目也各有进展：Light dApp Kit 的作者接受了评审结论，并继续追问测试问题；Spark Verify 则发布了 v0.1.1 补丁版本。[S04, S05] 需要说明的是，可引用材料只覆盖 2026-11-13 00:47 至 12:02（UTC）之间的几条回复，无法据此确认完整 24 小时窗口内的全部动态。[S01, S02, S03, S04, S05]

## 重点话题

- **Twine 手续费设计获得认可**：作者感谢 @ArthurZhang 的反馈，表示手续费（fee）的费率形状看起来合理，并承诺在 fee 功能落地时把这两点一并实现进去。[S01]

- **Twine 新增对 LSP 钱包发票的支持**：作者列出 790605a 到 504c990 之间的改动，核心是支持支付携带 trampoline 路由提示的买家发票，面向 Cellula 等 LSP 钱包；这类钱包会把 Fiber 的 TrampolineRouteHint 属性（attr 10，fiber#1623）写进发票，而 Fiber 到 0.10.0-rc3 还无法处理。[S02]（该帖内容在原文中被截断，后续细节无法确认）[S02]。

- **CKB IDL 提案继续推进**：作者感谢社区对 IDL 的支持，表示自己正在推进这项工作，并会在达成里程碑时发布更新。[S03]

- **Light dApp Kit 作者接受评审结论并提出遗留问题**：Akane 感谢 @xingtianchunyan 的评审和解释，表示理解委员会的决定；同时请求对方帮忙回应自己上一条帖子里关于 JoyID 的疑问，即在测试网环境下用 Chrome 虚拟认证器创建 passkey 可以成功，但 JoyID 会拒绝。[S04]（原文在此处被截断，具体报错与原因不明）[S04]。

- **Spark Verify 发布 CKB Verify v0.1.1**：该版本以 MIT 协议开源发布，是在 v0.1.0 之上的补丁版本，runner、manifest 规范和报告格式均保持不变。[S05]

## 值得继续跟进

- **JoyID 与 passkey 的测试网兼容性问题**：目前只知道 Chrome 虚拟认证器创建 passkey 成功、JoyID 侧拒绝，具体原因和是否有回复尚不清楚，需等后续帖子。[S04]

- **Twine 对 trampoline 路由的支持能否落地**：帖子明确指出 Fiber 到 0.10.0-rc3 还不支持该属性，这依赖 Fiber 侧的推进节奏。[S02]

- **CKB IDL 的里程碑更新**：作者已承诺按里程碑发帖同步进展，可以观察后续是否有实质性交付。[S03]

## 来源索引

- `S01` [Twine: Buy and Sell CKB Without Depositing on an Exchange (Fiber P2P PoC)](https://talk.nervos.org/t/twine-buy-and-sell-ckb-without-depositing-on-an-exchange-fiber-p2p-poc/10741/18) | ebubedev | 2026-11-13 19:59:57 CST | Thanks @ArthurZhang — glad the fee shape looks sound. I’ll bake both of those in when fees land
- `S02` [Twine: Buy and Sell CKB Without Depositing on an Exchange (Fiber P2P PoC)](https://talk.nervos.org/t/twine-buy-and-sell-ckb-without-depositing-on-an-exchange-fiber-p2p-poc/10741/19) | ebubedev | 2026-11-13 20:02:55 CST | Here is what changed since 790605a through 504c990 Pay buyer invoices that carry a trampoline route hint (Cellula and other LSP wallets) Wallets behind an LSP put Fiber’s TrampolineRouteHint attribute (attr 10, fiber#1623) on their invoices. Fiber through 0.10.0-rc3 cannot...
- `S03` [[DIS] CKB IDL: Interface Description Language and Discoverability for CKB Scripts](https://talk.nervos.org/t/dis-ckb-idl-interface-description-language-and-discoverability-for-ckb-scripts/11031/11) | OWK50GA | 2026-11-13 17:47:52 CST | Thank you, Ser. And thanks to everyone who supported IDL. I am working on it, and will drop updates as I hit the milestones
- `S04` [Spark Program | Light dApp Kit](https://talk.nervos.org/t/spark-program-light-dapp-kit/11062/4) | Akane | 2026-11-13 15:52:24 CST | Thanks @xingtianchunyan for the review and explanation. I understand the committee’s decision. Separately, could you help with the JoyID question in my earlier post? In the testnet setup, passkey creation succeeds with Chrome’s virtual authenticator, but JoyID rejects the...
- `S05` [Spark Program | Spark Verify - Reproducible Acceptance Checks for CKB Projects](https://talk.nervos.org/t/spark-program-spark-verify-reproducible-acceptance-checks-for-ckb-projects/10598/22) | Akane | 2026-11-13 08:47:06 CST | Hi all, a short update on CKB Verify. CKB Verify v0.1.1 is out, open source under the MIT license: GitHub Release ckb-verify v0.1.1 · Akane-CN/spark-verify ckb-verify v0.1.1 A patch release on top of v0.1.0. The runner, the manifest specs, and the report formats are the same....

## 活跃话题

1. [Twine: Buy and Sell CKB Without Depositing on an Exchange (Fiber P2P PoC)](https://talk.nervos.org/t/twine-buy-and-sell-ckb-without-depositing-on-an-exchange-fiber-p2p-poc/10741) | 2 条近窗帖子 | 最新活动 2026-11-13 20:02:55 CST | tags: fiber
2. [[DIS] CKB IDL: Interface Description Language and Discoverability for CKB Scripts](https://talk.nervos.org/t/dis-ckb-idl-interface-description-language-and-discoverability-for-ckb-scripts/11031) | 1 条近窗帖子 | 最新活动 2026-11-13 17:47:52 CST | tags: CKB-IDL
3. [Spark Program | Light dApp Kit](https://talk.nervos.org/t/spark-program-light-dapp-kit/11062) | 1 条近窗帖子 | 最新活动 2026-11-13 15:52:24 CST | tags: Rejection
4. [Spark Program | Spark Verify - Reproducible Acceptance Checks for CKB Projects](https://talk.nervos.org/t/spark-program-spark-verify-reproducible-acceptance-checks-for-ckb-projects/10598) | 1 条近窗帖子 | 最新活动 2026-11-13 08:47:06 CST | tags: Rejection

## 最近帖子摘录

- 2026-11-13 20:02:55 CST | ebubedev | [Twine: Buy and Sell CKB Without Depositing on an Exchange (Fiber P2P PoC)](https://talk.nervos.org/t/twine-buy-and-sell-ckb-without-depositing-on-an-exchange-fiber-p2p-poc/10741/19) | Here is what changed since 790605a through 504c990 Pay buyer invoices that carry a trampoline route hint (Cellula and other LSP wallets) Wallets behind an LSP put Fiber’s...
- 2026-11-13 19:59:57 CST | ebubedev | [Twine: Buy and Sell CKB Without Depositing on an Exchange (Fiber P2P PoC)](https://talk.nervos.org/t/twine-buy-and-sell-ckb-without-depositing-on-an-exchange-fiber-p2p-poc/10741/18) | Thanks @ArthurZhang — glad the fee shape looks sound. I’ll bake both of those in when fees land
- 2026-11-13 17:47:52 CST | OWK50GA | [[DIS] CKB IDL: Interface Description Language and Discoverability for CKB Scripts](https://talk.nervos.org/t/dis-ckb-idl-interface-description-language-and-discoverability-for-ckb-scripts/11031/11) | Thank you, Ser. And thanks to everyone who supported IDL. I am working on it, and will drop updates as I hit the milestones
- 2026-11-13 15:52:24 CST | Akane | [Spark Program | Light dApp Kit](https://talk.nervos.org/t/spark-program-light-dapp-kit/11062/4) | Thanks @xingtianchunyan for the review and explanation. I understand the committee’s decision. Separately, could you help with the JoyID question in my earlier post? In the...
- 2026-11-13 08:47:06 CST | Akane | [Spark Program | Spark Verify - Reproducible Acceptance Checks for CKB Projects](https://talk.nervos.org/t/spark-program-spark-verify-reproducible-acceptance-checks-for-ckb-projects/10598/22) | Hi all, a short update on CKB Verify. CKB Verify v0.1.1 is out, open source under the MIT license: GitHub Release ckb-verify v0.1.1 · Akane-CN/spark-verify ckb-verify v0.1.1 A...
