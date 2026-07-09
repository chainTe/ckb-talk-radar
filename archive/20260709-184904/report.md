# Nervos Talk 社区简报

- 统计窗口: 2026-07-09 02:49:04 CST 到 2026-07-10 02:49:04 CST
- 生成时间: 2026-07-10 02:49:15 CST
- 话题数: 11
- 帖子数: 17
- 作者数: 10
- 总结模式: ai:openrouter

## 社区总结

## 今日发生了什么

社区今天整体较平静，主要围绕基础设施问题和技术讨论展开 [S10, S11, S01]。DAO投票页面访问故障已修复，但引发了关于是否应继续沿用Metaforo平台的争议 [S10, S11, S13]。同时有成员关注到网络算力持续下降，并将其与2022年的历史情况进行对比 [S01]。

## 重点话题

- **DAO投票页面故障与平台争议**：Metaforo访问缓慢问题持续一段时间后已修复 [S11]，但社区成员fishell明确表态支持更换平台，认为其"偏离CKB精神" [S13]；版主zz_tovarishch则认为刷新后仍可投票，倾向维持现状 [S14]。更棘手的是，故障期间恰好有一项关于Fiber支付开源访问控制的投票结束，有成员因页面问题错过投票 [S12]。

- **网络算力历史对比**：成员knmo将当前算力从5.23 EH跌至602.49 PH的下降趋势，与2022年"更突然、更陡峭"的历史暴跌进行类比，引发对网络挖矿动力现状的讨论 [S01]。

- **开发者工具新动向**：CrptoHead发布CKB DevLaunch Kit，定位为开源开发者入门工具包，计划将现有CKB示例打包成带部署脚本的文档化入门模板 [S02]；但同一作者此前发布的同名话题已被自行删除 [S04]。

- **经济模型实验性讨论**：成员pickfire提出一种基于PoW的"钟型曲线"代币发行方案，特点是初期出块量递增、中期维持峰值、后期递减趋近于恒定1币/块，实现无限供应但通胀率趋零 [S08]。

- **生态项目运营状态**：成员knmo发现mobit.app部署已暂停 [S05]；PocketNode轻客户端则出现提款后余额显示异常的技术问题 [S16]。

## 值得继续跟进

- **Metaforo去留与DAO治理韧性**：投票平台故障已非首次，社区对"可刷新解决"与"应更换平台"存在明显分歧，需观察后续是否有正式治理提案推动平台迁移 [S10, S13, S14]。

- **算力持续下滑的后续影响**：当前算力水平与2022年暴跌后的恢复路径是否可比，以及这对网络安全性和矿工生态的实际影响，尚待更多数据和分析 [S01]。

- **Spark项目执行进展**：多个Spark资助项目（VibeQuest、Cell Sandbox）近期仅有简短状态更新，缺乏实质性进展披露，需关注是否进入交付关键期 [S06, S07]。

## 来源索引

- `S01` [Similar drop in the hash rate back in 2022](https://talk.nervos.org/t/similar-drop-in-the-hash-rate-back-in-2022/10477/1) | knmo | 2026-07-10 01:45:21 CST | We had a similar drop in the hash rate back in 2022, but at that time it was much more sudden and much steeper. Is the current drop in network mining power comparable to the situation back then? Current: September 24, 2023, 5.23 EH, dropping to July 6, 2026, 602.49 PH. Back...
- `S02` [CKB DevLaunch Kit](https://talk.nervos.org/t/ckb-devlaunch-kit/10476/1) | CrptoHead | 2026-07-10 01:23:39 CST | CKB DevLaunch Kit Summary CKB DevLaunch Kit is an open-source developer onboarding toolkit designed to help new developers quickly start building on Nervos CKB. The project will package existing CKB examples into well-documented starter templates with deployment scripts and...
- `S03` [[DIS] Werra: Building Trust Infrastructure for Creator Commerce](https://talk.nervos.org/t/dis-werra-building-trust-infrastructure-for-creator-commerce/10453/10) | CrptoHead | 2026-07-10 01:08:13 CST | Great
- `S04` [CKB DevLaunch Kit](https://talk.nervos.org/t/ckb-devlaunch-kit/10475/1) | CrptoHead | 2026-07-10 01:07:14 CST | (topic deleted by author)
- `S05` [Mobit.app paused?](https://talk.nervos.org/t/mobit-app-paused/10474/1) | knmo | 2026-07-10 00:39:07 CST | This deployment is temporarily paused https://mobit.app
- `S06` [Spark Program | VibeQuest: Turning AI-Assisted Coding Into Real Learning](https://talk.nervos.org/t/spark-program-vibequest-turning-ai-assisted-coding-into-real-learning/10446/4) | XBeach | 2026-07-09 23:40:34 CST | gm gm @xingtianchunyan hope you had time to review the updated proposal and response
- `S07` [Spark Program | Cell Sandbox — A Visual Playground for the CKB Cell Model](https://talk.nervos.org/t/spark-program-cell-sandbox-a-visual-playground-for-the-ckb-cell-model/10326/15) | zynor | 2026-07-09 22:40:15 CST | Received
- `S08` [分叉：让总供应量呈钟型分布](https://talk.nervos.org/t/topic/10473/1) | pickfire | 2026-07-09 21:42:14 CST | 提问 纯粹的PoW机制，请列出相关的参数，然后参考CKB，列出动态调整挖矿难度、每个块能挖出的币的数量等的公式。 Epoch 也定为 4小时。 减半/增倍的周期为x个Epoch。 已发行币的数量是一个钟型结构，即初期数量很少，一个块出1个币；随着epoch的增加，出块量翻倍；最高每个块出32个币；维持最高峰s 个epoch；然后随着epoch的增加，出块量开始减版，直到最后每个块出1个币，保持恒定。 即发行上限无限，但是通胀率将无限趋近于零。 由 DeepSeek 回答 “钟形曲线”必须作用于整个区块链的生命周期（全局 Epoch...
- `S09` [Cannot open the CKB DAO voting page](https://talk.nervos.org/t/cannot-open-the-ckb-dao-voting-page/10472/2) | 9527 | 2026-07-09 03:01:57 CST | same issue for me
- `S10` [Cannot open the CKB DAO voting page](https://talk.nervos.org/t/cannot-open-the-ckb-dao-voting-page/10472/3) | zz_tovarishch | 2026-07-09 08:46:08 CST | Hi CDEX, 访问缓慢的问题从发生以来，已经多次反馈给了metaforo团队 目前我自己尝试时，大概一半的情况下能正常打开投票页面，在metaforo团队修复问题前，建议多尝试刷新页面
- `S11` [Cannot open the CKB DAO voting page](https://talk.nervos.org/t/cannot-open-the-ckb-dao-voting-page/10472/4) | zz_tovarishch | 2026-07-09 10:40:30 CST | The access issues for Metaforo have been resolved. Community members are welcome to check and cast their votes. If you encounter any further issues, please feel free to reach out.
- `S12` [Cannot open the CKB DAO voting page](https://talk.nervos.org/t/cannot-open-the-ckb-dao-voting-page/10472/5) | CDEX | 2026-07-09 11:17:27 CST | He can access the page now, but the poll https://dao.ckb.community/thread/vot-fiberlatch-access-open-source-access-control-for-fiber-payments-74170 has just closed. How should we handle this?
- `S13` [Cannot open the CKB DAO voting page](https://talk.nervos.org/t/cannot-open-the-ckb-dao-voting-page/10472/6) | fishell | 2026-07-09 12:38:41 CST | I will vote for any proposal to replace metaforo. It’s an acceptable temperary solution but deviates from CKB ethos.
- `S14` [Cannot open the CKB DAO voting page](https://talk.nervos.org/t/cannot-open-the-ckb-dao-voting-page/10472/7) | zz_tovarishch | 2026-07-09 13:31:55 CST | During the slow issue, metaforo is still possible to access and vote, after refreshing a few times. For that reason, I would lean towards maintaining the current situation. Of course, this is purely my personal opinion, and any decision lies beyond my responsibilities as a...
- `S15` [The Invisibook AMA](https://talk.nervos.org/t/the-invisibook-ama/10401/6) | fishell | 2026-07-09 12:40:26 CST | Great AMA, love it!
- `S16` [[DIS] Mobile-Ready CKB Light Client (Pocket Node) for Android](https://talk.nervos.org/t/dis-mobile-ready-ckb-light-client-pocket-node-for-android/9879/69) | knmo | 2026-07-09 07:38:20 CST | Here, the whole process goes in reverse. For future reference. 0x4837a90b65d603b8d0daf4cb81acea3e9aa93b9ea4ea6640441eec43269540e9 After the first withdrawal transaction, the amount of 9,456—which was normally in the wallet—was no longer visible in PocketNode. I also quickly...

## 活跃话题

1. [Similar drop in the hash rate back in 2022](https://talk.nervos.org/t/similar-drop-in-the-hash-rate-back-in-2022/10477) | 1 条近窗帖子 | 最新活动 2026-07-10 01:45:21 CST
2. [CKB DevLaunch Kit](https://talk.nervos.org/t/ckb-devlaunch-kit/10476) | 1 条近窗帖子 | 最新活动 2026-07-10 01:23:39 CST | tags: Spark-Program
3. [[DIS] Werra: Building Trust Infrastructure for Creator Commerce](https://talk.nervos.org/t/dis-werra-building-trust-infrastructure-for-creator-commerce/10453) | 1 条近窗帖子 | 最新活动 2026-07-10 01:08:13 CST
4. [CKB DevLaunch Kit](https://talk.nervos.org/t/ckb-devlaunch-kit/10475) | 1 条近窗帖子 | 最新活动 2026-07-10 01:07:14 CST | tags: Spark-Program
5. [Mobit.app paused?](https://talk.nervos.org/t/mobit-app-paused/10474) | 1 条近窗帖子 | 最新活动 2026-07-10 00:39:07 CST
6. [Spark Program | VibeQuest: Turning AI-Assisted Coding Into Real Learning](https://talk.nervos.org/t/spark-program-vibequest-turning-ai-assisted-coding-into-real-learning/10446) | 1 条近窗帖子 | 最新活动 2026-07-09 23:40:34 CST | tags: Spark-Program
7. [Spark Program | Cell Sandbox — A Visual Playground for the CKB Cell Model](https://talk.nervos.org/t/spark-program-cell-sandbox-a-visual-playground-for-the-ckb-cell-model/10326) | 1 条近窗帖子 | 最新活动 2026-07-09 22:40:15 CST | tags: In-Progress, Spark-Program
8. [分叉：让总供应量呈钟型分布](https://talk.nervos.org/t/topic/10473) | 1 条近窗帖子 | 最新活动 2026-07-09 21:42:14 CST | tags: pow
9. [Cannot open the CKB DAO voting page](https://talk.nervos.org/t/cannot-open-the-ckb-dao-voting-page/10472) | 7 条近窗帖子 | 最新活动 2026-07-09 14:25:24 CST | tags: DAO
10. [The Invisibook AMA](https://talk.nervos.org/t/the-invisibook-ama/10401) | 1 条近窗帖子 | 最新活动 2026-07-09 12:40:26 CST | tags: AMA
11. [[DIS] Mobile-Ready CKB Light Client (Pocket Node) for Android](https://talk.nervos.org/t/dis-mobile-ready-ckb-light-client-pocket-node-for-android/9879) | 1 条近窗帖子 | 最新活动 2026-07-09 07:38:20 CST | tags: CKB, light-client

## 最近帖子摘录

- 2026-07-10 01:45:21 CST | knmo | [Similar drop in the hash rate back in 2022](https://talk.nervos.org/t/similar-drop-in-the-hash-rate-back-in-2022/10477/1) | We had a similar drop in the hash rate back in 2022, but at that time it was much more sudden and much steeper. Is the current drop in network mining power comparable to the...
- 2026-07-10 01:23:39 CST | CrptoHead | [CKB DevLaunch Kit](https://talk.nervos.org/t/ckb-devlaunch-kit/10476/1) | CKB DevLaunch Kit Summary CKB DevLaunch Kit is an open-source developer onboarding toolkit designed to help new developers quickly start building on Nervos CKB. The project will...
- 2026-07-10 01:08:13 CST | CrptoHead | [[DIS] Werra: Building Trust Infrastructure for Creator Commerce](https://talk.nervos.org/t/dis-werra-building-trust-infrastructure-for-creator-commerce/10453/10) | Great
- 2026-07-10 01:07:14 CST | CrptoHead | [CKB DevLaunch Kit](https://talk.nervos.org/t/ckb-devlaunch-kit/10475/1) | (topic deleted by author)
- 2026-07-10 00:39:07 CST | knmo | [Mobit.app paused?](https://talk.nervos.org/t/mobit-app-paused/10474/1) | This deployment is temporarily paused https://mobit.app
- 2026-07-09 23:40:34 CST | XBeach | [Spark Program | VibeQuest: Turning AI-Assisted Coding Into Real Learning](https://talk.nervos.org/t/spark-program-vibequest-turning-ai-assisted-coding-into-real-learning/10446/4) | gm gm @xingtianchunyan hope you had time to review the updated proposal and response
- 2026-07-09 22:40:15 CST | zynor | [Spark Program | Cell Sandbox — A Visual Playground for the CKB Cell Model](https://talk.nervos.org/t/spark-program-cell-sandbox-a-visual-playground-for-the-ckb-cell-model/10326/15) | Received
- 2026-07-09 21:42:14 CST | pickfire | [分叉：让总供应量呈钟型分布](https://talk.nervos.org/t/topic/10473/1) | 提问 纯粹的PoW机制，请列出相关的参数，然后参考CKB，列出动态调整挖矿难度、每个块能挖出的币的数量等的公式。 Epoch 也定为 4小时。 减半/增倍的周期为x个Epoch。 已发行币的数量是一个钟型结构，即初期数量很少，一个块出1个币；随着epoch的增加，出块量翻倍；最高每个块出32个币；维持最高峰s...
- 2026-07-09 14:25:24 CST | woodbury.bit | [Cannot open the CKB DAO voting page](https://talk.nervos.org/t/cannot-open-the-ckb-dao-voting-page/10472/8) | 我个人认为补齐规则是更好的选择。如果明确遇到平台技术故障/可用性问题，是不是应该有个补偿机制，类似延后截止时间或者是在什么时候在投票，尤其是例如有小伙伴想投但是没办法投票的时候。 例如类似DDOS攻击是每个平台都可能遇到的问题，类似打MEMES的时候，当时自动脚本开的太多了，导致RPC服务队列排队太多，都用到了Kill -9...
- 2026-07-09 13:31:55 CST | zz_tovarishch | [Cannot open the CKB DAO voting page](https://talk.nervos.org/t/cannot-open-the-ckb-dao-voting-page/10472/7) | During the slow issue, metaforo is still possible to access and vote, after refreshing a few times. For that reason, I would lean towards maintaining the current situation. Of...
- 2026-07-09 12:40:26 CST | fishell | [The Invisibook AMA](https://talk.nervos.org/t/the-invisibook-ama/10401/6) | Great AMA, love it!
- 2026-07-09 12:38:41 CST | fishell | [Cannot open the CKB DAO voting page](https://talk.nervos.org/t/cannot-open-the-ckb-dao-voting-page/10472/6) | I will vote for any proposal to replace metaforo. It’s an acceptable temperary solution but deviates from CKB ethos.
- 2026-07-09 11:17:27 CST | CDEX | [Cannot open the CKB DAO voting page](https://talk.nervos.org/t/cannot-open-the-ckb-dao-voting-page/10472/5) | He can access the page now, but the poll https://dao.ckb.community/thread/vot-fiberlatch-access-open-source-access-control-for-fiber-payments-74170 has just closed. How should...
- 2026-07-09 10:40:30 CST | zz_tovarishch | [Cannot open the CKB DAO voting page](https://talk.nervos.org/t/cannot-open-the-ckb-dao-voting-page/10472/4) | The access issues for Metaforo have been resolved. Community members are welcome to check and cast their votes. If you encounter any further issues, please feel free to reach out.
- 2026-07-09 08:46:08 CST | zz_tovarishch | [Cannot open the CKB DAO voting page](https://talk.nervos.org/t/cannot-open-the-ckb-dao-voting-page/10472/3) | Hi CDEX, 访问缓慢的问题从发生以来，已经多次反馈给了metaforo团队 目前我自己尝试时，大概一半的情况下能正常打开投票页面，在metaforo团队修复问题前，建议多尝试刷新页面
- 2026-07-09 07:38:20 CST | knmo | [[DIS] Mobile-Ready CKB Light Client (Pocket Node) for Android](https://talk.nervos.org/t/dis-mobile-ready-ckb-light-client-pocket-node-for-android/9879/69) | Here, the whole process goes in reverse. For future reference. 0x4837a90b65d603b8d0daf4cb81acea3e9aa93b9ea4ea6640441eec43269540e9 After the first withdrawal transaction, the...
- 2026-07-09 03:01:57 CST | 9527 | [Cannot open the CKB DAO voting page](https://talk.nervos.org/t/cannot-open-the-ckb-dao-voting-page/10472/2) | same issue for me
