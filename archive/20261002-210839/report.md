# Nervos Talk 社区简报

- 统计窗口: 2026-10-02 05:08:39 CST 到 2026-10-03 05:08:39 CST
- 生成时间: 2026-10-03 05:08:48 CST
- 话题数: 8
- 帖子数: 11
- 作者数: 9
- 总结模式: ai:openai-compatible

## 社区总结

## 今日发生了什么

今天论坛最集中的讨论是 CKB 节点收入层，相关讨论把方向推进到一个名为 CKB Service Runner 的独立应用方案 [S04, S05, S06]。CCC 的 stealth-address 扩展与 CKB Script Port 轻客户端状态转移实验也在今天出现 [S01, S02]。Fiber 网络上，兼容性工具和自动流动性再平衡设计都有跟进更新 [S07, S08]。另外，Lean Oracle 在测试网上线，CellScript 0.31 发布，CKBA Dev Rel AMA 收获正面反馈 [S09, S10, S11]。

## 重点话题

- **CKB 节点收入层讨论出现新形态**：NightLantern 质疑“为什么修复没坏的东西”，并称比特币全节点无报酬仍能运行、CKB 已有 state rent 使普通节点保持低成本 [S04]。psawyerberlin 回应称已把最后三个问题一起回答，并在更新首帖，修正处用删除线保留历史 [S05]。随后他宣布项目现在叫 CKB Service Runner，是一个安装在 full node 旁边的独立应用，不需要改 ckb、不需要共识变更，运营者不 opt in 就不运行 [S06]。
- **CCC 迎来 stealth-address 扩展**：U-Iriamuzu 介绍了为 CCC 做的 Incognito Mode，一种可选 stealth-address 能力，目标是让收款人分享可重用的接收身份 [S02]。truthixify 称赞该工作，并提到自己过去在 Wraith Protocol 上做过 CKB 的 stealth-address 支付 [S03]。
- **开发者工具侧有新实验和发布**：Ticoworld 表示自己在做一个小实验 CKB Script Port，想看一个 CKB Script 已同步状态能否从一套 light-client 安装移动到另一套 [S01]。这样新安装不必总是重建同一个 Script 的历史 [S01]。ArthurZhang 则宣布 CellScript 0.31.0 于 10 月 1 日发布，native compiler、独立 artifact checker、VS Code 扩展、网站、Playground 和 Registry 服务一起更新 [S11]。
- **Lean Oracle 在测试网上线**：Adokiye_Destiny 发布 Lean Oracle，称它是 CKB 的委员会签名 pull price oracle，已在 testnet 上线 [S09]。它为 CKB 合约提供可在链上验证的价格，覆盖 BTC、ETH、SOL、USDT 和 CKB，委员会每秒签署一次价格更新，公共镜像提供签名数据 [S09]。
- **Fiber 相关工具与设计继续推进**：ILE_LABS 跟进了 RPC/SDK 兼容性工具，称当前检查可在 Fiber v0.9.0 和 v0.9.1 复现，且没有把结果当作协议回归，而是可能的 live RPC 相关缺口 [S07]。同一团队在自动通道流动性再平衡 RFC 下表示，已准备约束 outgoing channel 和 final return hop 的设计，包括预期失败处理与测试，并会在 review 前分享 [S08]。

## 值得继续跟进

- CKB Service Runner 的后续值得观察：它作为 full node 旁边的独立应用、无需改 ckb 或共识、只在运营者 opt in 时运行，能否回应 NightLantern 的“不要修复没坏东西”担忧并形成真实需求，是节点收入层讨论的关键 [S04, S05, S06]。
- CCC stealth-address 扩展的落地与采用值得跟进：它采用可重用接收身份设计，且社区中已有人提到 Wraith Protocol 的 stealth-address 经验，后续是否被更多应用测试或采用需要观察 [S02, S03]。
- Fiber 的两条后续线值得关注：RPC/SDK 兼容性检查在 v0.9.0/v0.9.1 可复现且可能不是协议回归，自动流动性再平衡设计则等待 review 与测试，结果会影响后续 Fiber 工具与 send_payment 路径相关工作 [S07, S08]。

## 来源索引

- `S01` [CKB Script Port: testing state transfer between light clients](https://talk.nervos.org/t/ckb-script-port-testing-state-transfer-between-light-clients/10803/1) | Ticoworld | 2026-10-03 04:57:29 CST | I’ve been working on a small experiment called CKB Script Port. The idea is to see whether already-synced state for one CKB Script can be moved from one light-client installation to another, so the new installation does not always have to rebuild the same Script history from...
- `S02` [Introducing a Stealth Address Extension for CCC](https://talk.nervos.org/t/introducing-a-stealth-address-extension-for-ccc/10802/1) | U-Iriamuzu | 2026-10-02 21:42:25 CST | Introducing a Stealth Address Extension for CCC Hello everyone, I’ve been working on Incognito Mode for CCC, an opt-in stealth-address capability for applications built with CKBers’ Codebase. The idea is simple: a recipient shares a reusable receiving identity, while each...
- `S03` [Introducing a Stealth Address Extension for CCC](https://talk.nervos.org/t/introducing-a-stealth-address-extension-for-ccc/10802/2) | truthixify | 2026-10-03 04:45:24 CST | Nice work. I did something with stealth addresses in the past on wraith protocol: Wraith Protocol: Stealth Address Payments on CKB Nice to see this on CCC.
- `S04` [A Revenue Layer for CKB Nodes](https://talk.nervos.org/t/a-revenue-layer-for-ckb-nodes/10734/17) | NightLantern | 2026-10-02 09:01:19 CST | My concerns are as follows Why fix what isn’t broken. Bitcoin which is the golden standard. Has full nodes that don’t get paid and the network still works. CKB already handled the part that actually gets expensive with state rent, so a normal node stays cheap to run. Unpaid...
- `S05` [A Revenue Layer for CKB Nodes](https://talk.nervos.org/t/a-revenue-layer-for-ckb-nodes/10734/18) | psawyerberlin | 2026-10-03 03:54:34 CST | Thanks all. Answering the last three together. I’m also updating the first post to reflect where this thread has taken the idea. Corrected parts are struck through, not deleted, so the history stays visible. Where this came from. The trigger was a concrete need: CRT needs many...
- `S06` [A Revenue Layer for CKB Nodes](https://talk.nervos.org/t/a-revenue-layer-for-ckb-nodes/10734/19) | psawyerberlin | 2026-10-03 04:44:04 CST | The project is now CKB Service Runner: a separate application you install next to your full node. It needs no change to ckb and no consensus change, and nothing runs unless the operator opts in. github.com GitHub - psawyerberlin/ckb-service-runner: Side application for CKB...
- `S07` [Compatibility Kit for RPC and SDK Consumers — Technical Feedback](https://talk.nervos.org/t/compatibility-kit-for-rpc-and-sdk-consumers-technical-feedback/10737/2) | ILE_LABS | 2026-10-02 22:48:03 CST | Hi everyone, just following up on this update. We have kept the work focused on a standalone tool, and the current checks are reproducible across Fiber v0.9.0 and v0.9.1. The result so far is not being presented as a protocol regression. It is a possible gap between live RPC...
- `S08` [[RFC & Research] Automated Channel Liquidity Rebalancing on Fiber Network](https://talk.nervos.org/t/rfc-research-automated-channel-liquidity-rebalancing-on-fiber-network/10691/7) | ILE_LABS | 2026-10-02 22:46:04 CST | Thanks for clarifying. We have been reviewing the current send_payment path and have already prepared a focused design for constraining the outgoing channel and final return hop, including the expected failure handling and tests. We’ll share the design for review before...
- `S09` [Asset Price Oracle on Nervos Network](https://talk.nervos.org/t/asset-price-oracle-on-nervos-network/10800/1) | Adokiye_Destiny | 2026-10-02 17:27:02 CST | Lean Oracle: a committee-signed pull price oracle for CKB, live on testnet Lean Oracle gives any CKB contract a price it can verify on chain. It covers BTC, ETH, SOL, USDT and CKB. A committee of publishers signs one price update every second. A public mirror serves the signed...
- `S10` [CKBA Dev Rel AMA](https://talk.nervos.org/t/ckba-dev-rel-ama/10794/3) | Thinker | 2026-10-02 13:19:24 CST | Great event! Hope this becomes a regular occurrence.
- `S11` [CellScript - A DSL for Cell-Based Contracts](https://talk.nervos.org/t/cellscript-a-dsl-for-cell-based-contracts/10193/34) | ArthurZhang | 2026-10-02 08:27:26 CST | CellScript 0.31: Smaller Contracts, Less Repeated Work CellScript 0.31.0 was released on October 1. The native compiler, standalone artifact checker, VS Code extension, website, Playground, and Registry services have been updated together. I also owe this thread a short recap...

## 活跃话题

1. [CKB Script Port: testing state transfer between light clients](https://talk.nervos.org/t/ckb-script-port-testing-state-transfer-between-light-clients/10803) | 1 条近窗帖子 | 最新活动 2026-10-03 04:57:29 CST | tags: CKB, light-client
2. [Introducing a Stealth Address Extension for CCC](https://talk.nervos.org/t/introducing-a-stealth-address-extension-for-ccc/10802) | 2 条近窗帖子 | 最新活动 2026-10-03 04:45:24 CST | tags: CKB, lang-en
3. [A Revenue Layer for CKB Nodes](https://talk.nervos.org/t/a-revenue-layer-for-ckb-nodes/10734) | 3 条近窗帖子 | 最新活动 2026-10-03 04:44:04 CST | tags: CKB, CKB-VM
4. [Compatibility Kit for RPC and SDK Consumers — Technical Feedback](https://talk.nervos.org/t/compatibility-kit-for-rpc-and-sdk-consumers-technical-feedback/10737) | 1 条近窗帖子 | 最新活动 2026-10-02 22:48:03 CST
5. [[RFC & Research] Automated Channel Liquidity Rebalancing on Fiber Network](https://talk.nervos.org/t/rfc-research-automated-channel-liquidity-rebalancing-on-fiber-network/10691) | 1 条近窗帖子 | 最新活动 2026-10-02 22:46:04 CST
6. [Asset Price Oracle on Nervos Network](https://talk.nervos.org/t/asset-price-oracle-on-nervos-network/10800) | 1 条近窗帖子 | 最新活动 2026-10-02 17:27:02 CST | tags: CKB, DeFi, Oracle, dapp
7. [CKBA Dev Rel AMA](https://talk.nervos.org/t/ckba-dev-rel-ama/10794) | 1 条近窗帖子 | 最新活动 2026-10-02 13:19:24 CST | tags: AMA
8. [CellScript - A DSL for Cell-Based Contracts](https://talk.nervos.org/t/cellscript-a-dsl-for-cell-based-contracts/10193) | 1 条近窗帖子 | 最新活动 2026-10-02 08:27:26 CST | tags: CKB-VM, CellScript, DSL, lang-en

## 最近帖子摘录

- 2026-10-03 04:57:29 CST | Ticoworld | [CKB Script Port: testing state transfer between light clients](https://talk.nervos.org/t/ckb-script-port-testing-state-transfer-between-light-clients/10803/1) | I’ve been working on a small experiment called CKB Script Port. The idea is to see whether already-synced state for one CKB Script can be moved from one light-client...
- 2026-10-03 04:45:24 CST | truthixify | [Introducing a Stealth Address Extension for CCC](https://talk.nervos.org/t/introducing-a-stealth-address-extension-for-ccc/10802/2) | Nice work. I did something with stealth addresses in the past on wraith protocol: Wraith Protocol: Stealth Address Payments on CKB Nice to see this on CCC.
- 2026-10-03 04:44:04 CST | psawyerberlin | [A Revenue Layer for CKB Nodes](https://talk.nervos.org/t/a-revenue-layer-for-ckb-nodes/10734/19) | The project is now CKB Service Runner: a separate application you install next to your full node. It needs no change to ckb and no consensus change, and nothing runs unless the...
- 2026-10-03 03:54:34 CST | psawyerberlin | [A Revenue Layer for CKB Nodes](https://talk.nervos.org/t/a-revenue-layer-for-ckb-nodes/10734/18) | Thanks all. Answering the last three together. I’m also updating the first post to reflect where this thread has taken the idea. Corrected parts are struck through, not deleted,...
- 2026-10-02 22:48:03 CST | ILE_LABS | [Compatibility Kit for RPC and SDK Consumers — Technical Feedback](https://talk.nervos.org/t/compatibility-kit-for-rpc-and-sdk-consumers-technical-feedback/10737/2) | Hi everyone, just following up on this update. We have kept the work focused on a standalone tool, and the current checks are reproducible across Fiber v0.9.0 and v0.9.1. The...
- 2026-10-02 22:46:04 CST | ILE_LABS | [[RFC & Research] Automated Channel Liquidity Rebalancing on Fiber Network](https://talk.nervos.org/t/rfc-research-automated-channel-liquidity-rebalancing-on-fiber-network/10691/7) | Thanks for clarifying. We have been reviewing the current send_payment path and have already prepared a focused design for constraining the outgoing channel and final return...
- 2026-10-02 21:42:25 CST | U-Iriamuzu | [Introducing a Stealth Address Extension for CCC](https://talk.nervos.org/t/introducing-a-stealth-address-extension-for-ccc/10802/1) | Introducing a Stealth Address Extension for CCC Hello everyone, I’ve been working on Incognito Mode for CCC, an opt-in stealth-address capability for applications built with...
- 2026-10-02 17:27:02 CST | Adokiye_Destiny | [Asset Price Oracle on Nervos Network](https://talk.nervos.org/t/asset-price-oracle-on-nervos-network/10800/1) | Lean Oracle: a committee-signed pull price oracle for CKB, live on testnet Lean Oracle gives any CKB contract a price it can verify on chain. It covers BTC, ETH, SOL, USDT and...
- 2026-10-02 13:19:24 CST | Thinker | [CKBA Dev Rel AMA](https://talk.nervos.org/t/ckba-dev-rel-ama/10794/3) | Great event! Hope this becomes a regular occurrence.
- 2026-10-02 09:01:19 CST | NightLantern | [A Revenue Layer for CKB Nodes](https://talk.nervos.org/t/a-revenue-layer-for-ckb-nodes/10734/17) | My concerns are as follows Why fix what isn’t broken. Bitcoin which is the golden standard. Has full nodes that don’t get paid and the network still works. CKB already handled...
- 2026-10-02 08:27:26 CST | ArthurZhang | [CellScript - A DSL for Cell-Based Contracts](https://talk.nervos.org/t/cellscript-a-dsl-for-cell-based-contracts/10193/34) | CellScript 0.31: Smaller Contracts, Less Repeated Work CellScript 0.31.0 was released on October 1. The native compiler, standalone artifact checker, VS Code extension, website,...
