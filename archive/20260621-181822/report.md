# Nervos Talk 社区简报

- 统计窗口: 2026-06-21 02:18:22 CST 到 2026-06-22 02:18:22 CST
- 生成时间: 2026-06-22 02:18:26 CST
- 话题数: 6
- 帖子数: 10
- 作者数: 9
- 总结模式: ai:openrouter

## 社区总结

## 今日发生了什么

Luxvoid Protocol 的 BTC→CKB→EVM 跨链管道在三天内运行次数从 96 次飙升至 239 次，增长远超讨论速度，同时收获了社区成员对其提案的明确支持 [S03, S04]。此外，社区今天出现了多个新方向的发帖，包括基于 Fiber 的 AI 算力市场 Infern、类 Tinder 的预测市场应用构想，以及 CKB 上零知识证明隐私治理的第三篇研究笔记 [S06, S07, S01]。

## 重点话题

- **Luxvoid 管道数据爆发，社区态度转向支持**：项目方更新数据显示，BTC→CKB→EVM 管道运行次数从发帖时的 96 次增至 224 次（触发 239 次），休眠 Cell 从 108 个增至 241 个，增长幅度远超讨论进度 [S03]。有社区成员明确表示被说服并支持该提案，认为其"投资者思维"正是 CKB 生态所需 [S04]，另有一位开发者主动提出可快速上手并开发审计管道 [S05]。

- **CellScript AMM 遭遇身份设计瓶颈，核心开发者快速响应**：WuodOdhis 发现将 action artifact 直接用作 MintAuthority 等 Cell 的 type script 时，CKB 会在输出创建阶段立即执行该脚本导致失败 [S08]。ArthurZhang 确认这是"真实的 UX 设计缺口"，指出 scoped action artifact 应作为主动验证器而非被动资源身份 [S09]，并已在 v0.16.2 版本中修复：明确 always_success 仅用于测试、新增 cellc resource-identity 用于真实资源 Cell 身份 [S10]。

- **Fiber 网络应用构想涌现**：Fisher 提出"类 Tinder 预测市场"想法，利用 Fiber 小额多次支付特性，让用户通过左右滑动对话题下注，默认赌注可设为五毛钱，同时为话题创作者设置 1% 抽成激励 [S07]。truthixify 则发布了 Infern——一个基于 Fiber 的 AI 模型算力市场，允许个人在自有硬件上部署 AI 模型并按请求收费，目前已开源并在测试网运行 [S06]。

- **零知识证明隐私治理研究深入第三篇**：Mulandi_Cecilia 发布系列研究笔记的第三篇，延续前两篇关于国库治理的讨论，聚焦如何在不破坏现有设计的前提下叠加隐私层 [S01]。

- **CKB-UGMP 项目澄清 Pinata 上传架构**：HNO3Miracle 回复委员会提问，说明当前架构中前端不直接请求 Pinata，而是由服务器通过 PINATA_JWT 调用 Pinata API 完成 IPFS 上传 [S02]。

## 值得继续跟进

- **Luxvoid 的"数据跑赢讨论"能否转化为 DAO 支持**：虽然增长数据亮眼且收获了口头支持，但尚未看到实际的 DAO 资金承诺或正式合作落地，需要观察后续是否有治理层面的实质性动作 [S03, S04]。

- **CellScript AMM 的 v0.16.2 修复是否打通主流程**：ArthurZhang 的快速响应解决了资源身份的设计问题，但 WuodOdhis 能否基于此继续推进到 devnet 交易验证，将是判断 CellScript 工具链成熟度的关键 [S10, S08]。

- **Fiber 应用从构想走向原型的距离**：今日出现的 Infern 和 Tinder 预测市场都依赖 Fiber 网络，但前者已在测试网运行、后者尚属头脑风暴，需要关注这两个方向谁能率先产生可交互的用户体验 [S06, S07]。

## 来源索引

- `S01` [Research Notes: What Zero-Knowledge Proofs Enable on CKB](https://talk.nervos.org/t/research-notes-what-zero-knowledge-proofs-enable-on-ckb/10368/3) | Mulandi_Cecilia | 2026-06-22 01:18:34 CST | Beyond treasury governance: what privacy would ask of this primitive This is Note 03 in my ongoing research. Continuing from Note 2 Note 2 closed on a question I had handed forward from Note 1: how to layer privacy onto this design without breaking what already works. Before...
- `S02` [Spark Program | CKB-UGMP —— A Universal Spore/DOB Seamless Minting Infrastructure Prototype on CKB —— 基于 CKB 的通用 Spore/DOB 无感铸造基础设施原型](https://talk.nervos.org/t/spark-program-ckb-ugmp-a-universal-spore-dob-seamless-minting-infrastructure-prototype-on-ckb-ckb-spore-dob/10098/30) | HNO3Miracle | 2026-06-21 23:31:06 CST | Hi @xingtianchunyan , 非常感谢委员会的理解。很高兴能收到委员会提出的问题！ Pinata 上传流程 在目前 UGMP 的架构里，前端不直接请求 Pinata，由服务器通过其提供的PINATA_JWT 发出请求。 前端向 UGMP 服务器的 multipart/form-data 接口提交图片。 服务器校验后调用 Pinata API：https://api.pinata.cloud/pinning/pinFileToIPFS Pinata 返回 IpfsHash。 服务端把结果整理为统一的 UploadResult...
- `S03` [[DIS] Luxvoid Protocol: The First Working BTC→CKB→EVM Pipeline — Seeking DAO Support/collab for Production Scaling](https://talk.nervos.org/t/dis-luxvoid-protocol-the-first-working-btc-ckb-evm-pipeline-seeking-dao-support-collab-for-production-scaling/10400/9) | Aki | 2026-06-21 17:51:04 CST | Three days ago I posted with 96 runs and 108 dormant cells. 48 hours later: 239 each. The pipeline outran the discussion. Updated Stats (since the proposal went live 3 days ago): Metric At Posting Now Pipeline runs 96 224 (239 fired) Dormant cells 108 241 CKB code cells...
- `S04` [[DIS] Luxvoid Protocol: The First Working BTC→CKB→EVM Pipeline — Seeking DAO Support/collab for Production Scaling](https://talk.nervos.org/t/dis-luxvoid-protocol-the-first-working-btc-ckb-evm-pipeline-seeking-dao-support-collab-for-production-scaling/10400/10) | ebdalezyz_aljhny | 2026-06-21 18:28:57 CST | Your argument is convincing to me. I support your proposal, and I can genuinely sense the sincerity and ambition behind what you’re building. You speak with an investor’s mindset, and I believe that is exactly the kind of perspective the CKB ecosystem needs more of today. CKB...
- `S05` [[DIS] Luxvoid Protocol: The First Working BTC→CKB→EVM Pipeline — Seeking DAO Support/collab for Production Scaling](https://talk.nervos.org/t/dis-luxvoid-protocol-the-first-working-btc-ckb-evm-pipeline-seeking-dao-support-collab-for-production-scaling/10400/11) | Ar_Hel | 2026-06-21 22:24:36 CST | I know seven programming languages ​​and have four years of IT experience. Of course, I don’t know the intricacies of some of the libraries listed in the application. But I could quickly figure it out and develop any audit pipeline for you.
- `S06` [Introducing Infern: serve an AI model from your own machine and get paid per request over Fiber](https://talk.nervos.org/t/introducing-infern-serve-an-ai-model-from-your-own-machine-and-get-paid-per-request-over-fiber/10408/1) | truthixify | 2026-06-21 20:32:40 CST | Hello, I have been building Infern, a compute marketplace where an individual can serve an AI model from their own hardware and get paid per request over Fiber. It is open source, running on testnet today, and I would love feedback from this community before I take it further....
- `S07` [分享一个 Tinder 版预测市场应用的想法](https://talk.nervos.org/t/tinder/10407/1) | Fisher | 2026-06-21 20:01:45 CST | 作为一个天天盼着 nervos 出一款大众爆款应用的技术盲，我又来头脑风暴了。 一种交互上类似 Tinder 的应用（我真没用过），通过左滑右滑来对卡片话题下注“是”和“否”，不感兴趣就划走。 可以结合 Fiber 适合小额多次支付的特性，主打一个小赌怡情，而不必像 polymarket 一样总是一局定生死。可以设置一个默认赌注金额比如五毛钱，然后每天对着感兴趣的话题划来划去就可以了。 理念上有点接近拼多多，为购物（下注）增加更多娱乐性。 可以为赌注话题创作者设置一个1%抽成，鼓励构思大家感兴趣的赌注话题，生成的赌注话题放在链上占用...
- `S08` [CellScript AMM Builder Integration Log from Bootstrap Friction to Devnet Transactions](https://talk.nervos.org/t/cellscript-amm-builder-integration-log-from-bootstrap-friction-to-devnet-transactions/10386/9) | WuodOdhis | 2026-06-21 04:09:02 CST | The current blocker: We need real MintAuthority, Token, Pool, and LPReceipt cells with proper CellScript identity. But if we use an action artifact like token_mint_with_authority.elf directly as the type script for a MintAuthority cell, CKB runs that script immediately when...
- `S09` [CellScript AMM Builder Integration Log from Bootstrap Friction to Devnet Transactions](https://talk.nervos.org/t/cellscript-amm-builder-integration-log-from-bootstrap-friction-to-devnet-transactions/10386/10) | ArthurZhang | 2026-06-21 10:50:36 CST | Good. I think you have found another real UX design gap here. A scoped action artifact indeed should not be used as the passive type script identity for MintAuthority, Token, Pool, or LPReceipt. It is an active verifier. If CKB runs it during output creation, it will expect...
- `S10` [CellScript AMM Builder Integration Log from Bootstrap Friction to Devnet Transactions](https://talk.nervos.org/t/cellscript-amm-builder-integration-log-from-bootstrap-friction-to-devnet-transactions/10386/11) | ArthurZhang | 2026-06-21 12:54:42 CST | Ok now, quick update: I pushed v0.16.2 to address this. What changed: always_success is now documented as fixture-only. scoped action artifacts are documented as active verifiers, not passive resource identities. added cellc resource-identity for real resource cell identity...

## 活跃话题

1. [Research Notes: What Zero-Knowledge Proofs Enable on CKB](https://talk.nervos.org/t/research-notes-what-zero-knowledge-proofs-enable-on-ckb/10368) | 1 条近窗帖子 | 最新活动 2026-06-22 01:18:34 CST | tags: CKB-VM, architecture, groth16, sp1, zero-knowledge, zkvm
2. [Spark Program | CKB-UGMP —— A Universal Spore/DOB Seamless Minting Infrastructure Prototype on CKB —— 基于 CKB 的通用 Spore/DOB 无感铸造基础设施原型](https://talk.nervos.org/t/spark-program-ckb-ugmp-a-universal-spore-dob-seamless-minting-infrastructure-prototype-on-ckb-ckb-spore-dob/10098) | 1 条近窗帖子 | 最新活动 2026-06-21 23:31:06 CST | tags: In-Progress, Spark-Program
3. [[DIS] Luxvoid Protocol: The First Working BTC→CKB→EVM Pipeline — Seeking DAO Support/collab for Production Scaling](https://talk.nervos.org/t/dis-luxvoid-protocol-the-first-working-btc-ckb-evm-pipeline-seeking-dao-support-collab-for-production-scaling/10400) | 3 条近窗帖子 | 最新活动 2026-06-21 22:24:36 CST | tags: CKB, RGBpp, testnet
4. [Introducing Infern: serve an AI model from your own machine and get paid per request over Fiber](https://talk.nervos.org/t/introducing-infern-serve-an-ai-model-from-your-own-machine-and-get-paid-per-request-over-fiber/10408) | 1 条近窗帖子 | 最新活动 2026-06-21 20:32:40 CST | tags: CKB, dapp
5. [分享一个 Tinder 版预测市场应用的想法](https://talk.nervos.org/t/tinder/10407) | 1 条近窗帖子 | 最新活动 2026-06-21 20:01:45 CST
6. [CellScript AMM Builder Integration Log from Bootstrap Friction to Devnet Transactions](https://talk.nervos.org/t/cellscript-amm-builder-integration-log-from-bootstrap-friction-to-devnet-transactions/10386) | 3 条近窗帖子 | 最新活动 2026-06-21 12:54:42 CST | tags: CellScript, dapp

## 最近帖子摘录

- 2026-06-22 01:18:34 CST | Mulandi_Cecilia | [Research Notes: What Zero-Knowledge Proofs Enable on CKB](https://talk.nervos.org/t/research-notes-what-zero-knowledge-proofs-enable-on-ckb/10368/3) | Beyond treasury governance: what privacy would ask of this primitive This is Note 03 in my ongoing research. Continuing from Note 2 Note 2 closed on a question I had handed...
- 2026-06-21 23:31:06 CST | HNO3Miracle | [Spark Program | CKB-UGMP —— A Universal Spore/DOB Seamless Minting Infrastructure Prototype on CKB —— 基于 CKB 的通用 Spore/DOB 无感铸造基础设施原型](https://talk.nervos.org/t/spark-program-ckb-ugmp-a-universal-spore-dob-seamless-minting-infrastructure-prototype-on-ckb-ckb-spore-dob/10098/30) | Hi @xingtianchunyan , 非常感谢委员会的理解。很高兴能收到委员会提出的问题！ Pinata 上传流程 在目前 UGMP 的架构里，前端不直接请求 Pinata，由服务器通过其提供的PINATA_JWT 发出请求。 前端向 UGMP 服务器的 multipart/form-data 接口提交图片。 服务器校验后调用 Pinata...
- 2026-06-21 22:24:36 CST | Ar_Hel | [[DIS] Luxvoid Protocol: The First Working BTC→CKB→EVM Pipeline — Seeking DAO Support/collab for Production Scaling](https://talk.nervos.org/t/dis-luxvoid-protocol-the-first-working-btc-ckb-evm-pipeline-seeking-dao-support-collab-for-production-scaling/10400/11) | I know seven programming languages ​​and have four years of IT experience. Of course, I don’t know the intricacies of some of the libraries listed in the application. But I...
- 2026-06-21 20:32:40 CST | truthixify | [Introducing Infern: serve an AI model from your own machine and get paid per request over Fiber](https://talk.nervos.org/t/introducing-infern-serve-an-ai-model-from-your-own-machine-and-get-paid-per-request-over-fiber/10408/1) | Hello, I have been building Infern, a compute marketplace where an individual can serve an AI model from their own hardware and get paid per request over Fiber. It is open...
- 2026-06-21 20:01:45 CST | Fisher | [分享一个 Tinder 版预测市场应用的想法](https://talk.nervos.org/t/tinder/10407/1) | 作为一个天天盼着 nervos 出一款大众爆款应用的技术盲，我又来头脑风暴了。 一种交互上类似 Tinder 的应用（我真没用过），通过左滑右滑来对卡片话题下注“是”和“否”，不感兴趣就划走。 可以结合 Fiber 适合小额多次支付的特性，主打一个小赌怡情，而不必像 polymarket...
- 2026-06-21 18:28:57 CST | ebdalezyz_aljhny | [[DIS] Luxvoid Protocol: The First Working BTC→CKB→EVM Pipeline — Seeking DAO Support/collab for Production Scaling](https://talk.nervos.org/t/dis-luxvoid-protocol-the-first-working-btc-ckb-evm-pipeline-seeking-dao-support-collab-for-production-scaling/10400/10) | Your argument is convincing to me. I support your proposal, and I can genuinely sense the sincerity and ambition behind what you’re building. You speak with an investor’s...
- 2026-06-21 17:51:04 CST | Aki | [[DIS] Luxvoid Protocol: The First Working BTC→CKB→EVM Pipeline — Seeking DAO Support/collab for Production Scaling](https://talk.nervos.org/t/dis-luxvoid-protocol-the-first-working-btc-ckb-evm-pipeline-seeking-dao-support-collab-for-production-scaling/10400/9) | Three days ago I posted with 96 runs and 108 dormant cells. 48 hours later: 239 each. The pipeline outran the discussion. Updated Stats (since the proposal went live 3 days...
- 2026-06-21 12:54:42 CST | ArthurZhang | [CellScript AMM Builder Integration Log from Bootstrap Friction to Devnet Transactions](https://talk.nervos.org/t/cellscript-amm-builder-integration-log-from-bootstrap-friction-to-devnet-transactions/10386/11) | Ok now, quick update: I pushed v0.16.2 to address this. What changed: always_success is now documented as fixture-only. scoped action artifacts are documented as active...
- 2026-06-21 10:50:36 CST | ArthurZhang | [CellScript AMM Builder Integration Log from Bootstrap Friction to Devnet Transactions](https://talk.nervos.org/t/cellscript-amm-builder-integration-log-from-bootstrap-friction-to-devnet-transactions/10386/10) | Good. I think you have found another real UX design gap here. A scoped action artifact indeed should not be used as the passive type script identity for MintAuthority, Token,...
- 2026-06-21 04:09:02 CST | WuodOdhis | [CellScript AMM Builder Integration Log from Bootstrap Friction to Devnet Transactions](https://talk.nervos.org/t/cellscript-amm-builder-integration-log-from-bootstrap-friction-to-devnet-transactions/10386/9) | The current blocker: We need real MintAuthority, Token, Pool, and LPReceipt cells with proper CellScript identity. But if we use an action artifact like...
