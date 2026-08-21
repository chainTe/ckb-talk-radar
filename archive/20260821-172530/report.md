# Nervos Talk 社区简报

- 统计窗口: 2026-08-21 01:25:30 CST 到 2026-08-22 01:25:30 CST
- 生成时间: 2026-08-22 01:25:36 CST
- 话题数: 4
- 帖子数: 5
- 作者数: 4
- 总结模式: ai:openai-compatible

## 社区总结

## 今日发生了什么

过去 24 小时，Nervos 论坛主要围绕 Fiber 网络进展和生态项目流程展开 [S01, S02, S03, S04]。最受关注的是 Fiber Studio 发布 v1.1.1，正式捆绑 fnn v0.9.0 稳定版 [S03]；同时社区讨论了将《反恐精英》移植到 Fiber 网络的集成思路 [S02]。此外，有用户报告了 Nervos Explorer 显示区块矿工奖励不一致的问题 [S01]，而 Corven 提案因缺少预算章节被协调员移出讨论阶段 [S04]。

## 重点话题

- **Fiber Studio v1.1.1 发布**：新版本将内置节点升级到官方 fnn v0.9.0 稳定版，并改进了通道状态管理和应用内 UX 反馈 [S03]。
- **《反恐精英》移植到 Fiber 的讨论**：ArthurZhang 认为这是一个很好的 Fiber 集成 demo；游戏是权威/中心化的 1v1 会话制，实时对战仍走 UDP/Renet，Fiber 作为事件驱动结算侧车，只处理预授权价值转移，且服务器和 matchmaker 不接触玩家钱包 [S02]。
- **区块矿工奖励显示疑点**：knmo 发现只有 cellbase 一笔交易的区块，矿工奖励分别为 558.80192866 CKB 和 587.26310400 CKB，且两者都没有 proposals，用户怀疑这是 Nervos Explorer 首页的显示错误 [S01]。
- **Corven 提案流程被打回**：协调员 zz_tovarishch 指出，该提案缺少最基本且必要的预算部分，且一天内未修改，不符合完整提案要求，因此已移除 [DIS] 标签，不能进入社区讨论阶段 [S04]。

## 值得继续跟进

- **Explorer 矿工奖励显示问题**：需要观察这是否只是一个前端显示错误，还是底层计算或数据逻辑存在差异，后续是否有官方回应或修复 [S01]。
- **Fiber 游戏结算集成方向**：Counter Strike 移植方案将实时对战与结算路径分离，但仍依赖权威/中心化服务器；值得关注未来是否出现更多 Fiber 应用场景，以及托管边界的实际安全性 [S02]。
- **Corven 提案是否会修订重提**：作者是否会补充预算部分并重新提交，以及社区对协调员移除 [DIS] 标签这一流程的反应，都值得继续观察 [S04]。

## 来源索引

- `S01` [Miner Reward different for Blocks with only 1 transaction](https://talk.nervos.org/t/miner-reward-different-for-blocks-with-only-1-transaction/10650/1) | knmo | 2026-08-22 00:37:27 CST | Blocks with only 1 transaction (Cellbase) differ in Miner Reward 558.80192866CKB and 587.26310400CKB both have 0 proposals. Why? Edit: It looks like a display error on the main page of the Nervos Explorer? 558.80+ | 587.26 👀 👇 1000002186957×1699 131 KB Edit2: Miner Reward...
- `S02` [Porting Couter Strike to Fiber network](https://talk.nervos.org/t/porting-couter-strike-to-fiber-network/10647/3) | ArthurZhang | 2026-08-21 22:25:34 CST | 我觉得这是一个很棒的Fiber integration demo. 在我的理解这应该是一个 权威性/中心化的 1v1 session-based game，外接 Fiber 作为 事件驱动结算侧车。 简单梳理一下： 实时对战仍然是传统 UDP/Renet， Renet 仍然要负责延迟敏感的输入和快照； Fiber 负责把预先授权的支付条件，在服务器判定伤害后兑现。且 Fiber 恒仅处理 pre-authorised value transfer； 热路径 和 结算路径 分离。 托管边界是服务器和 matchmaker 不接触玩家的 wallet...
- `S03` [[DIS] Fiber Desktop v1 ground-up rebuild and launch — fnn desktop app](https://talk.nervos.org/t/dis-fiber-desktop-v1-ground-up-rebuild-and-launch-fnn-desktop-app/10317/26) | ebubedev | 2026-08-21 20:29:36 CST | Fiber Studio v1.1.1: Bundled FNN v0.9.0 Upgrade & Channel State Handling Hi everyone, We have released Fiber Studio v1.1.1! This release updates our bundled node to the official fnn v0.9.0 stable release and improves channel state management and UX feedback across the app....
- `S04` [Corven — Cloud Development Infrastructure for the CKB Ecosystem](https://talk.nervos.org/t/corven-cloud-development-infrastructure-for-the-ckb-ecosystem/10648/3) | zz_tovarishch | 2026-08-21 14:44:09 CST | Hi @lestonEth, because your proposal lacks the most basic and necessary budget section and hasn’t been modified within a day, it does not in accordance with a complete proposal and cannot proceed to the community discussion stage. As a coordinator, I have removed the [DIS] tag...
- `S05` [Corven — Cloud Development Infrastructure for the CKB Ecosystem](https://talk.nervos.org/t/corven-cloud-development-infrastructure-for-the-ckb-ecosystem/10648/4) | zz_tovarishch | 2026-08-21 14:44:25 CST | 

## 活跃话题

1. [Miner Reward different for Blocks with only 1 transaction](https://talk.nervos.org/t/miner-reward-different-for-blocks-with-only-1-transaction/10650) | 1 条近窗帖子 | 最新活动 2026-08-22 00:37:27 CST
2. [Porting Couter Strike to Fiber network](https://talk.nervos.org/t/porting-couter-strike-to-fiber-network/10647) | 1 条近窗帖子 | 最新活动 2026-08-21 22:25:34 CST | tags: fiber, game
3. [[DIS] Fiber Desktop v1 ground-up rebuild and launch — fnn desktop app](https://talk.nervos.org/t/dis-fiber-desktop-v1-ground-up-rebuild-and-launch-fnn-desktop-app/10317) | 1 条近窗帖子 | 最新活动 2026-08-21 20:29:36 CST | tags: fiber
4. [Corven — Cloud Development Infrastructure for the CKB Ecosystem](https://talk.nervos.org/t/corven-cloud-development-infrastructure-for-the-ckb-ecosystem/10648) | 2 条近窗帖子 | 最新活动 2026-08-21 14:44:09 CST

## 最近帖子摘录

- 2026-08-22 00:37:27 CST | knmo | [Miner Reward different for Blocks with only 1 transaction](https://talk.nervos.org/t/miner-reward-different-for-blocks-with-only-1-transaction/10650/1) | Blocks with only 1 transaction (Cellbase) differ in Miner Reward 558.80192866CKB and 587.26310400CKB both have 0 proposals. Why? Edit: It looks like a display error on the main...
- 2026-08-21 22:25:34 CST | ArthurZhang | [Porting Couter Strike to Fiber network](https://talk.nervos.org/t/porting-couter-strike-to-fiber-network/10647/3) | 我觉得这是一个很棒的Fiber integration demo. 在我的理解这应该是一个 权威性/中心化的 1v1 session-based game，外接 Fiber 作为 事件驱动结算侧车。 简单梳理一下： 实时对战仍然是传统 UDP/Renet， Renet 仍然要负责延迟敏感的输入和快照； Fiber...
- 2026-08-21 20:29:36 CST | ebubedev | [[DIS] Fiber Desktop v1 ground-up rebuild and launch — fnn desktop app](https://talk.nervos.org/t/dis-fiber-desktop-v1-ground-up-rebuild-and-launch-fnn-desktop-app/10317/26) | Fiber Studio v1.1.1: Bundled FNN v0.9.0 Upgrade & Channel State Handling Hi everyone, We have released Fiber Studio v1.1.1! This release updates our bundled node to the official...
- 2026-08-21 14:44:25 CST | zz_tovarishch | [Corven — Cloud Development Infrastructure for the CKB Ecosystem](https://talk.nervos.org/t/corven-cloud-development-infrastructure-for-the-ckb-ecosystem/10648/4) | 
- 2026-08-21 14:44:09 CST | zz_tovarishch | [Corven — Cloud Development Infrastructure for the CKB Ecosystem](https://talk.nervos.org/t/corven-cloud-development-infrastructure-for-the-ckb-ecosystem/10648/3) | Hi @lestonEth, because your proposal lacks the most basic and necessary budget section and hasn’t been modified within a day, it does not in accordance with a complete proposal...
