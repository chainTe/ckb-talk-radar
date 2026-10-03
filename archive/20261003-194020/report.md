# Nervos Talk 社区简报

- 统计窗口: 2026-10-03 03:40:20 CST 到 2026-10-04 03:40:20 CST
- 生成时间: 2026-10-04 03:40:24 CST
- 话题数: 6
- 帖子数: 9
- 作者数: 7
- 总结模式: ai:openai-compatible

## 社区总结

## 今日发生了什么
今天最集中的讨论是“A Revenue Layer for CKB Nodes”有了新名字和更清晰的边界：项目现称 CKB Service Runner，作为安装在完整节点旁边的独立应用，不改 CKB、不改共识，操作员不主动选择就不运行 [S01, S02]。节点收入层的试点也有进展，Ayoub_Lesfer 表示乐意成为两个试点之一，并讨论 tip 应限制在 pledge lock 上限内、按每个 pledge cell 固定收取 [S03]。论坛同时冒出几个新方向：CKB+Fiber 的预测市场、用 CellScript 做制药批次放行证据、轻客户端之间迁移 CKB Script 状态，以及 CCC 的 stealth address 扩展继续交流 [S04, S05, S08, S09]。

## 重点话题
- **CKB Service Runner 成为节点收入层讨论的落点**：作者更新首帖，说明讨论已走到具体项目，并把修正部分保留为删除线以便查看历史 [S01]。项目定位为独立侧应用，不修改 ckb、不引入共识变更，只有节点运营者主动选择才运行 [S02]。Ayoub_Lesfer 表示愿意参与试点，并建议 tip 保持在 pledge lock 的 1 CKB 上限内，最低 pledge 为 100 CKB [S03]。他还主张 tip 按每个 pledge cell 固定额收取，而不是按百分比 [S03]。
- **Tinder 版预测市场被判断为技术上可行**：ArthurZhang 回复该想法，认为现在技术上可行，CKB 可处理市场状态/结算，Fiber 提供微支付层 [S04]。他认为这类高频、小额交互所需的基础原语大多已经具备 [S04]。不过材料中他提到“更大的问题”后截断，具体顾虑未能看到 [S04]。
- **Lineage 新帖探索制药批次放行证据**：ArthurZhang 启动 Lineage，称是在与制药行业朋友讨论后开始构建 [S05]。作为 CellScript 作者，他的核心问题是：当一批次变为“released”时，究竟谁批准了什么，以及另一参与者能否无需询问就检查 [S05]。
- **CCC stealth address 扩展与 Wraith Protocol 形成呼应**：truthixify 称赞该工作，并提到自己过去在 Wraith Protocol 做过 stealth addresses，且 Wraith Protocol 是 CKB 上的 stealth address 支付 [S07]。作者 U-Iriamuzu 回应称研究 CKB 现有 stealth-address 工作时也遇到了 Wraith Protocol，现在专注于让它自然融入 CCC、方便应用采用 [S08]。
- **CKB Script Port 与 CKBA AMA 的零散动态**：Ticoworld 发起 CKB Script Port 实验，目标是测试一个 CKB Script 的已同步状态能否从一个轻客户端安装迁移到另一个，避免新安装总重建相同历史 [S09]。CKBA Dev Rel AMA 中，T_Silva 问 AMA 里的兔子有没有名字、哪只是 @Hanssen，并附了图片 [S06]。

## 值得继续跟进
- 跟进 CKB Service Runner 的试点是否真正启动，以及 tip 设计最终采用固定额还是其他方式；pledge lock 的 1 CKB 上限与最低 100 CKB 质押会直接影响可收费空间 [S03]。
- 观察 ArthurZhang 提到的预测市场“更大的问题”是什么，材料里未展开；同时看 Lineage 是否能把制药批次放行证据的验证推进到可被其他参与方独立检查 [S04, S05]。
- 关注 CCC stealth address 扩展如何接入 CCC，以及它和 Wraith Protocol 的异同是否会影响采用；CKB Script Port 的轻客户端状态迁移实验也值得看后续是否有复现或更多测试 [S07, S08, S09]。

## 来源索引

- `S01` [A Revenue Layer for CKB Nodes](https://talk.nervos.org/t/a-revenue-layer-for-ckb-nodes/10734/18) | psawyerberlin | 2026-10-03 03:54:34 CST | Thanks all. Answering the last three together. I’m also updating the first post to reflect where this thread has taken the idea. Corrected parts are struck through, not deleted, so the history stays visible. Where this came from. The trigger was a concrete need: CRT needs many...
- `S02` [A Revenue Layer for CKB Nodes](https://talk.nervos.org/t/a-revenue-layer-for-ckb-nodes/10734/19) | psawyerberlin | 2026-10-03 04:44:04 CST | The project is now CKB Service Runner: a separate application you install next to your full node. It needs no change to ckb and no consensus change, and nothing runs unless the operator opts in. github.com GitHub - psawyerberlin/ckb-service-runner: Side application for CKB...
- `S03` [A Revenue Layer for CKB Nodes](https://talk.nervos.org/t/a-revenue-layer-for-ckb-nodes/10734/20) | Ayoub_Lesfer | 2026-10-03 22:19:03 CST | @psawyerberlin sounds good, happy to be one of the two pilots. On the tip: the pledge lock already caps what can leave a pledge cell at 1 CKB on release or refund, and the minimum pledge is 100 CKB, so I’d keep the tip inside that cap. Flat per pledge cell, not a percentage,...
- `S04` [分享一个 Tinder 版预测市场应用的想法](https://talk.nervos.org/t/tinder/10407/2) | ArthurZhang | 2026-10-03 16:59:17 CST | Hi Fisher, I think this is technically feasible now. With CKB handling the market state / settlement and Fiber providing the micropayment layer, most of the primitives needed for this kind of high-frequency, small-value interaction are already there. The bigger issue, in my...
- `S05` [Lineage: working through batch release evidence with CellScript](https://talk.nervos.org/t/lineage-working-through-batch-release-evidence-with-cellscript/10804/1) | ArthurZhang | 2026-10-03 15:48:03 CST | I started building this after discussing the idea with a mate who works in pharma. As the author of CellScript, I kept coming back to the same question: When a batch becomes “released,” what exactly did someone approve—and can another participant check it without asking the...
- `S06` [CKBA Dev Rel AMA](https://talk.nervos.org/t/ckba-dev-rel-ama/10794/4) | T_Silva | 2026-10-03 08:03:06 CST | Do these rabbits have names? and which one is @Hanssen? image400×250 62.7 KB
- `S07` [Introducing a Stealth Address Extension for CCC](https://talk.nervos.org/t/introducing-a-stealth-address-extension-for-ccc/10802/2) | truthixify | 2026-10-03 04:45:24 CST | Nice work. I did something with stealth addresses in the past on wraith protocol: Wraith Protocol: Stealth Address Payments on CKB Nice to see this on CCC.
- `S08` [Introducing a Stealth Address Extension for CCC](https://talk.nervos.org/t/introducing-a-stealth-address-extension-for-ccc/10802/3) | U-Iriamuzu | 2026-10-03 07:42:43 CST | Thanks! I actually came across Wraith Protocol while researching the existing stealth-address work on CKB. It’s great to see another implementation of the idea. My focus now is exploring how this can fit naturally into CCC and make the experience easier for applications to adopt.
- `S09` [CKB Script Port: testing state transfer between light clients](https://talk.nervos.org/t/ckb-script-port-testing-state-transfer-between-light-clients/10803/1) | Ticoworld | 2026-10-03 04:57:29 CST | I’ve been working on a small experiment called CKB Script Port. The idea is to see whether already-synced state for one CKB Script can be moved from one light-client installation to another, so the new installation does not always have to rebuild the same Script history from...

## 活跃话题

1. [A Revenue Layer for CKB Nodes](https://talk.nervos.org/t/a-revenue-layer-for-ckb-nodes/10734) | 3 条近窗帖子 | 最新活动 2026-10-03 22:19:03 CST | tags: CKB, CKB-VM
2. [分享一个 Tinder 版预测市场应用的想法](https://talk.nervos.org/t/tinder/10407) | 1 条近窗帖子 | 最新活动 2026-10-03 16:59:17 CST | tags: lang-zh
3. [Lineage: working through batch release evidence with CellScript](https://talk.nervos.org/t/lineage-working-through-batch-release-evidence-with-cellscript/10804) | 1 条近窗帖子 | 最新活动 2026-10-03 15:48:03 CST | tags: dapp, lang-en
4. [CKBA Dev Rel AMA](https://talk.nervos.org/t/ckba-dev-rel-ama/10794) | 1 条近窗帖子 | 最新活动 2026-10-03 08:03:06 CST | tags: AMA
5. [Introducing a Stealth Address Extension for CCC](https://talk.nervos.org/t/introducing-a-stealth-address-extension-for-ccc/10802) | 2 条近窗帖子 | 最新活动 2026-10-03 07:42:43 CST | tags: CKB, lang-en
6. [CKB Script Port: testing state transfer between light clients](https://talk.nervos.org/t/ckb-script-port-testing-state-transfer-between-light-clients/10803) | 1 条近窗帖子 | 最新活动 2026-10-03 04:57:29 CST | tags: CKB, light-client

## 最近帖子摘录

- 2026-10-03 22:19:03 CST | Ayoub_Lesfer | [A Revenue Layer for CKB Nodes](https://talk.nervos.org/t/a-revenue-layer-for-ckb-nodes/10734/20) | @psawyerberlin sounds good, happy to be one of the two pilots. On the tip: the pledge lock already caps what can leave a pledge cell at 1 CKB on release or refund, and the...
- 2026-10-03 16:59:17 CST | ArthurZhang | [分享一个 Tinder 版预测市场应用的想法](https://talk.nervos.org/t/tinder/10407/2) | Hi Fisher, I think this is technically feasible now. With CKB handling the market state / settlement and Fiber providing the micropayment layer, most of the primitives needed...
- 2026-10-03 15:48:03 CST | ArthurZhang | [Lineage: working through batch release evidence with CellScript](https://talk.nervos.org/t/lineage-working-through-batch-release-evidence-with-cellscript/10804/1) | I started building this after discussing the idea with a mate who works in pharma. As the author of CellScript, I kept coming back to the same question: When a batch becomes...
- 2026-10-03 08:03:06 CST | T_Silva | [CKBA Dev Rel AMA](https://talk.nervos.org/t/ckba-dev-rel-ama/10794/4) | Do these rabbits have names? and which one is @Hanssen? image400×250 62.7 KB
- 2026-10-03 07:42:43 CST | U-Iriamuzu | [Introducing a Stealth Address Extension for CCC](https://talk.nervos.org/t/introducing-a-stealth-address-extension-for-ccc/10802/3) | Thanks! I actually came across Wraith Protocol while researching the existing stealth-address work on CKB. It’s great to see another implementation of the idea. My focus now is...
- 2026-10-03 04:57:29 CST | Ticoworld | [CKB Script Port: testing state transfer between light clients](https://talk.nervos.org/t/ckb-script-port-testing-state-transfer-between-light-clients/10803/1) | I’ve been working on a small experiment called CKB Script Port. The idea is to see whether already-synced state for one CKB Script can be moved from one light-client...
- 2026-10-03 04:45:24 CST | truthixify | [Introducing a Stealth Address Extension for CCC](https://talk.nervos.org/t/introducing-a-stealth-address-extension-for-ccc/10802/2) | Nice work. I did something with stealth addresses in the past on wraith protocol: Wraith Protocol: Stealth Address Payments on CKB Nice to see this on CCC.
- 2026-10-03 04:44:04 CST | psawyerberlin | [A Revenue Layer for CKB Nodes](https://talk.nervos.org/t/a-revenue-layer-for-ckb-nodes/10734/19) | The project is now CKB Service Runner: a separate application you install next to your full node. It needs no change to ckb and no consensus change, and nothing runs unless the...
- 2026-10-03 03:54:34 CST | psawyerberlin | [A Revenue Layer for CKB Nodes](https://talk.nervos.org/t/a-revenue-layer-for-ckb-nodes/10734/18) | Thanks all. Answering the last three together. I’m also updating the first post to reflect where this thread has taken the idea. Corrected parts are struck through, not deleted,...
