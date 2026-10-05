# Nervos Talk 社区简报

- 统计窗口: 2026-10-05 07:03:02 CST 到 2026-10-06 07:03:02 CST
- 生成时间: 2026-10-06 07:03:11 CST
- 话题数: 6
- 帖子数: 15
- 作者数: 8
- 总结模式: ai:openai-compatible

## 社区总结

## 今日发生了什么

就这批材料看，过去 24 小时 Nervos Talk 没有明显的大型新公告，整体更像已有话题下的继续回复、追问和提案征集[S01, S02, S07, S11, S12, S15]。相对活跃的是 CKB Script Port 的轻客户端状态迁移测试：Pocket Node 测试总体顺利，但测试者随后遇到一个未展开的奇怪问题，双方表示继续跟进[S02, S03, S04, S05]。FNN Safeguard 提案也在继续征集反馈，提案者解释恢复验证价值并点名多人查看，已有成员以外部观察者或非 Fiber 节点运营者身份回应[S07, S08, S09, S10]。此外，ZK counter 的审计问题得到“暂无时间表”的回复，Spark Verify 仍在等委员会 review，资产价格预言机方向收到正面评价[S01, S12, S13, S15]。

## 重点话题

- CKB Script Port 轻客户端状态迁移：Jnr6 问用 Pocket Node 测试是否遇到问题[S02]；Ticoworld 说 Pocket 本身问题不大，进入轻客户端状态后能把 Script 状态迁到全新安装、从下一个区块继续，且重启后仍可用，但之后测试时出现奇怪问题[S03]；Jnr6 表示会继续研究，并把它列为后续引入的功能之一[S04]；Ticoworld 说会随上游进展继续更新[S05]；Web3legend 认为新设备或新安装能续接上次同步会很有意义，并期待下一次更新[S06]。
- FNN Safeguard 提案：Dappsoverapps 回应 quake 反馈称，核心价值不只是连接备份工具，而是确保 FNN 备份能恢复相同节点身份和通道/支付状态，并让运营者用真实节点副本测试新 FNN 版本[S07]；他还点名多人请求查看提案并给意见[S08]；ArthurZhang 澄清自己此前不熟悉该项目、未参与设计开发，只能作为外部观察者评论，并大致同意 quake 的担忧，但后续内容在材料中截断[S09]；Ayoub_Lesfer 表示自己不运行 Fiber 节点，无法判断恢复侧，但希望看到一个原生备份看似正常却恢复失败、或恢复后通道状态不同的具体案例[S10]。
- Build a ZK counter on CKB with CellScript：Ksa_1971 询问项目是否需要外部安全审计，以及预计何时进行[S12]；ArthurZhang 回复现阶段没有审计时间表，如果某个 ZK 应用推进生产，届时再定义适当审查范围[S13]；Ksa_1971 随后表示感谢和认可[S14]。
- Asset Price Oracle on Nervos Network：ArthurZhang 认为这是 CKB 真正有用的方向，项目本地 feed cell 加签名拉取更新的模型比全局共享可变 oracle cell 更自然[S15]；他还提到将不可信传输/镜像层分离，但材料在此截断，无法判断完整结论[S15]。
- CKB Nodes 收入层与 Spark Verify：Ayoub_Lesfer 表示自己这边不急，计划把 tip 加到 pledge lock，以便适用于任何 keeper，包括自己的脚本[S11]；他还说如果 Service Runner 那时在测试网，可以看看接口，并认为市场价设上限是合理的，材料之后在链上部分截断[S11]；Akane 在 Spark Verify 帖追问委员会是否已 review 最新更新[S01]。

## 值得继续跟进

- CKB Script Port 轻客户端状态迁移里“后来测试出现的奇怪问题”尚未展开，且上游进展被承诺继续更新，后续要关注问题具体是什么、是否会影响状态迁移功能[S03, S05]。
- FNN Safeguard 需要更具体的恢复失败案例或通道状态不一致证据；目前有回应者不熟悉项目或不运行 Fiber 节点，提案推进可能取决于能否补足可复现数据[S09, S10]。
- ZK counter 的安全审计没有时间表，只有推进生产时才定义审查范围，后续需观察是否出现生产化计划和审计需求[S13]；Spark Verify 的委员会 review 也仍未看到结果[S01]；资产价格预言机的讨论材料被截断，后续设计细节和反馈值得继续看[S15]。

## 来源索引

- `S01` [Spark Program | Spark Verify - Reproducible Acceptance Checks for CKB Projects](https://talk.nervos.org/t/spark-program-spark-verify-reproducible-acceptance-checks-for-ckb-projects/10598/12) | Akane | 2026-10-06 05:37:51 CST | Hi @zz_tovarishch, just following up on my latest update—has the committee had a chance to review it?
- `S02` [CKB Script Port: testing state transfer between light clients](https://talk.nervos.org/t/ckb-script-port-testing-state-transfer-between-light-clients/10803/2) | Jnr6 | 2026-10-05 18:45:27 CST | Did you hit any issue when testing with Pocket Node.
- `S03` [CKB Script Port: testing state transfer between light clients](https://talk.nervos.org/t/ckb-script-port-testing-state-transfer-between-light-clients/10803/3) | Ticoworld | 2026-10-05 18:55:30 CST | Not really on Pocket itself. The Pocket test actually went pretty smoothly once I got into the light-client state. I was able to move the Script state to a fresh install, continue from the next block, and it still worked after restart. The weird issue came later when I tested...
- `S04` [CKB Script Port: testing state transfer between light clients](https://talk.nervos.org/t/ckb-script-port-testing-state-transfer-between-light-clients/10803/4) | Jnr6 | 2026-10-05 19:06:58 CST | Thank you, I’ll look more into it and this will be one of the features to introduce down the line
- `S05` [CKB Script Port: testing state transfer between light clients](https://talk.nervos.org/t/ckb-script-port-testing-state-transfer-between-light-clients/10803/5) | Ticoworld | 2026-10-05 19:10:58 CST | That’s great to hear, thanks bro. I’ll keep you posted as the upstream side moves.
- `S06` [CKB Script Port: testing state transfer between light clients](https://talk.nervos.org/t/ckb-script-port-testing-state-transfer-between-light-clients/10803/6) | Web3legend | 2026-10-06 01:54:40 CST | will really make sense if syncs on new devices/installs can continue from where the last install stopped without having to do it all over from scratch. excited for your next update.
- `S07` [[DIS] FNN Safeguard — Recovery Verification and Pre-Upgrade Qualification for Fiber Nodes](https://talk.nervos.org/t/dis-fnn-safeguard-recovery-verification-and-pre-upgrade-qualification-for-fiber-nodes/10712/5) | Dappsoverapps | 2026-10-05 11:38:48 CST | Thanks for the feedback @quake The main value here isn’t just connecting existing backup tools. It’s making sure an FNN backup can actually restore the same node identity and channel/payment state, and letting operators test a new FNN version against a copy of their real node...
- `S08` [[DIS] FNN Safeguard — Recovery Verification and Pre-Upgrade Qualification for Fiber Nodes](https://talk.nervos.org/t/dis-fnn-safeguard-recovery-verification-and-pre-upgrade-qualification-for-fiber-nodes/10712/6) | Dappsoverapps | 2026-10-05 11:42:09 CST | @phroi @knmo @Yeti @ArthurZhang @Ayoub_Lesfer . We would appreciate it if you could take a look at this proposal when you have a chance. Any thoughts would be appreciated. Thank you.
- `S09` [[DIS] FNN Safeguard — Recovery Verification and Pre-Upgrade Qualification for Fiber Nodes](https://talk.nervos.org/t/dis-fnn-safeguard-recovery-verification-and-pre-upgrade-qualification-for-fiber-nodes/10712/7) | ArthurZhang | 2026-10-05 13:38:17 CST | Just to clarify my perspective, I wasn’t previously familiar with this project and haven’t been involved in its design or development, so I can only comment as an outside observer based on the proposal and the discussion here. Also I broadly agree with quake’s concern. The...
- `S10` [[DIS] FNN Safeguard — Recovery Verification and Pre-Upgrade Qualification for Fiber Nodes](https://talk.nervos.org/t/dis-fnn-safeguard-recovery-verification-and-pre-upgrade-qualification-for-fiber-nodes/10712/8) | Ayoub_Lesfer | 2026-10-05 18:54:32 CST | Thanks for the tag. I don’t run a Fiber node so I can’t judge the recovery side properly, but on quake’s point, what would help me as a reader is one concrete case where a native backup looked fine and then failed to restore, or came back with different channel state. If...
- `S11` [A Revenue Layer for CKB Nodes](https://talk.nervos.org/t/a-revenue-layer-for-ckb-nodes/10734/22) | Ayoub_Lesfer | 2026-10-05 18:53:57 CST | Makes sense, no rush on my side. I’m planning to add the tip to the pledge lock either way so it works for any keeper, my own script included, and if Service Runner is on testnet by then we can look at an interface. Market price under a cap sounds right to me. On chain I can...
- `S12` [Build a ZK counter on CKB with CellScript](https://talk.nervos.org/t/build-a-zk-counter-on-ckb-with-cellscript/10805/2) | Ksa_1971 | 2026-10-05 11:44:53 CST | Welcome! Do you think the project will require an external security audit, and if so, when do you expect that to happen?
- `S13` [Build a ZK counter on CKB with CellScript](https://talk.nervos.org/t/build-a-zk-counter-on-ckb-with-cellscript/10805/3) | ArthurZhang | 2026-10-05 13:49:42 CST | There is no audit timeline to announce at this stage. If and when we move a particular ZK application towards production, the appropriate review scope can be defined then.
- `S14` [Build a ZK counter on CKB with CellScript](https://talk.nervos.org/t/build-a-zk-counter-on-ckb-with-cellscript/10805/4) | Ksa_1971 | 2026-10-05 15:30:12 CST | Great work. Thank you.
- `S15` [Asset Price Oracle on Nervos Network](https://talk.nervos.org/t/asset-price-oracle-on-nervos-network/10800/2) | ArthurZhang | 2026-10-05 15:12:13 CST | I think this is a genuinely useful direction for CKB. The project-local feed cell + signed pull-update model feels much more natural for the Cell model than maintaining a globally shared mutable oracle cell. In particular, separating an untrusted transport/mirror layer from...

## 活跃话题

1. [Spark Program | Spark Verify - Reproducible Acceptance Checks for CKB Projects](https://talk.nervos.org/t/spark-program-spark-verify-reproducible-acceptance-checks-for-ckb-projects/10598) | 1 条近窗帖子 | 最新活动 2026-10-06 05:37:51 CST | tags: Pending
2. [CKB Script Port: testing state transfer between light clients](https://talk.nervos.org/t/ckb-script-port-testing-state-transfer-between-light-clients/10803) | 5 条近窗帖子 | 最新活动 2026-10-06 01:54:40 CST | tags: CKB, light-client
3. [[DIS] FNN Safeguard — Recovery Verification and Pre-Upgrade Qualification for Fiber Nodes](https://talk.nervos.org/t/dis-fnn-safeguard-recovery-verification-and-pre-upgrade-qualification-for-fiber-nodes/10712) | 4 条近窗帖子 | 最新活动 2026-10-05 18:54:32 CST
4. [A Revenue Layer for CKB Nodes](https://talk.nervos.org/t/a-revenue-layer-for-ckb-nodes/10734) | 1 条近窗帖子 | 最新活动 2026-10-05 18:53:57 CST | tags: CKB, CKB-VM
5. [Build a ZK counter on CKB with CellScript](https://talk.nervos.org/t/build-a-zk-counter-on-ckb-with-cellscript/10805) | 3 条近窗帖子 | 最新活动 2026-10-05 15:30:12 CST | tags: CellScript
6. [Asset Price Oracle on Nervos Network](https://talk.nervos.org/t/asset-price-oracle-on-nervos-network/10800) | 1 条近窗帖子 | 最新活动 2026-10-05 15:12:13 CST | tags: CKB, DeFi, Oracle, dapp

## 最近帖子摘录

- 2026-10-06 05:37:51 CST | Akane | [Spark Program | Spark Verify - Reproducible Acceptance Checks for CKB Projects](https://talk.nervos.org/t/spark-program-spark-verify-reproducible-acceptance-checks-for-ckb-projects/10598/12) | Hi @zz_tovarishch, just following up on my latest update—has the committee had a chance to review it?
- 2026-10-06 01:54:40 CST | Web3legend | [CKB Script Port: testing state transfer between light clients](https://talk.nervos.org/t/ckb-script-port-testing-state-transfer-between-light-clients/10803/6) | will really make sense if syncs on new devices/installs can continue from where the last install stopped without having to do it all over from scratch. excited for your next...
- 2026-10-05 19:10:58 CST | Ticoworld | [CKB Script Port: testing state transfer between light clients](https://talk.nervos.org/t/ckb-script-port-testing-state-transfer-between-light-clients/10803/5) | That’s great to hear, thanks bro. I’ll keep you posted as the upstream side moves.
- 2026-10-05 19:06:58 CST | Jnr6 | [CKB Script Port: testing state transfer between light clients](https://talk.nervos.org/t/ckb-script-port-testing-state-transfer-between-light-clients/10803/4) | Thank you, I’ll look more into it and this will be one of the features to introduce down the line
- 2026-10-05 18:55:30 CST | Ticoworld | [CKB Script Port: testing state transfer between light clients](https://talk.nervos.org/t/ckb-script-port-testing-state-transfer-between-light-clients/10803/3) | Not really on Pocket itself. The Pocket test actually went pretty smoothly once I got into the light-client state. I was able to move the Script state to a fresh install,...
- 2026-10-05 18:54:32 CST | Ayoub_Lesfer | [[DIS] FNN Safeguard — Recovery Verification and Pre-Upgrade Qualification for Fiber Nodes](https://talk.nervos.org/t/dis-fnn-safeguard-recovery-verification-and-pre-upgrade-qualification-for-fiber-nodes/10712/8) | Thanks for the tag. I don’t run a Fiber node so I can’t judge the recovery side properly, but on quake’s point, what would help me as a reader is one concrete case where a...
- 2026-10-05 18:53:57 CST | Ayoub_Lesfer | [A Revenue Layer for CKB Nodes](https://talk.nervos.org/t/a-revenue-layer-for-ckb-nodes/10734/22) | Makes sense, no rush on my side. I’m planning to add the tip to the pledge lock either way so it works for any keeper, my own script included, and if Service Runner is on...
- 2026-10-05 18:45:27 CST | Jnr6 | [CKB Script Port: testing state transfer between light clients](https://talk.nervos.org/t/ckb-script-port-testing-state-transfer-between-light-clients/10803/2) | Did you hit any issue when testing with Pocket Node.
- 2026-10-05 15:30:12 CST | Ksa_1971 | [Build a ZK counter on CKB with CellScript](https://talk.nervos.org/t/build-a-zk-counter-on-ckb-with-cellscript/10805/4) | Great work. Thank you.
- 2026-10-05 15:12:13 CST | ArthurZhang | [Asset Price Oracle on Nervos Network](https://talk.nervos.org/t/asset-price-oracle-on-nervos-network/10800/2) | I think this is a genuinely useful direction for CKB. The project-local feed cell + signed pull-update model feels much more natural for the Cell model than maintaining a...
- 2026-10-05 13:49:42 CST | ArthurZhang | [Build a ZK counter on CKB with CellScript](https://talk.nervos.org/t/build-a-zk-counter-on-ckb-with-cellscript/10805/3) | There is no audit timeline to announce at this stage. If and when we move a particular ZK application towards production, the appropriate review scope can be defined then.
- 2026-10-05 13:38:17 CST | ArthurZhang | [[DIS] FNN Safeguard — Recovery Verification and Pre-Upgrade Qualification for Fiber Nodes](https://talk.nervos.org/t/dis-fnn-safeguard-recovery-verification-and-pre-upgrade-qualification-for-fiber-nodes/10712/7) | Just to clarify my perspective, I wasn’t previously familiar with this project and haven’t been involved in its design or development, so I can only comment as an outside...
- 2026-10-05 11:44:53 CST | Ksa_1971 | [Build a ZK counter on CKB with CellScript](https://talk.nervos.org/t/build-a-zk-counter-on-ckb-with-cellscript/10805/2) | Welcome! Do you think the project will require an external security audit, and if so, when do you expect that to happen?
- 2026-10-05 11:42:09 CST | Dappsoverapps | [[DIS] FNN Safeguard — Recovery Verification and Pre-Upgrade Qualification for Fiber Nodes](https://talk.nervos.org/t/dis-fnn-safeguard-recovery-verification-and-pre-upgrade-qualification-for-fiber-nodes/10712/6) | @phroi @knmo @Yeti @ArthurZhang @Ayoub_Lesfer . We would appreciate it if you could take a look at this proposal when you have a chance. Any thoughts would be appreciated. Thank...
- 2026-10-05 11:38:48 CST | Dappsoverapps | [[DIS] FNN Safeguard — Recovery Verification and Pre-Upgrade Qualification for Fiber Nodes](https://talk.nervos.org/t/dis-fnn-safeguard-recovery-verification-and-pre-upgrade-qualification-for-fiber-nodes/10712/5) | Thanks for the feedback @quake The main value here isn’t just connecting existing backup tools. It’s making sure an FNN backup can actually restore the same node identity and...
