# Nervos Talk 社区简报

- 统计窗口: 2026-07-13 02:42:21 CST 到 2026-07-14 02:42:21 CST
- 生成时间: 2026-07-14 02:42:28 CST
- 话题数: 8
- 帖子数: 15
- 作者数: 12
- 总结模式: ai:openrouter

## 社区总结

## 今日发生了什么

社区今天围绕 DAO 投票页面访问故障展开了持续争论，有用户因 Metaforo 技术问题错过投票而要求官方回应 [S01, S04]。同时，两个 Spark 生态项目更新了进展，Cell Sandbox 推进了里程碑 1，Fiber Pay Studio 提交了新的申请 [S06, S09]。

## 重点话题

- **DAO 投票争议仍在发酵**：CDEX 继续追问因投票页面打不开而错过的选票能否得到官方回应，遭另一位用户质疑是否想推翻已通过提案，双方简短交锋 [S01, S02, S03]。neon.bit 虽澄清自己并非版主，但承认 Metaforo 故障确实令人困扰 [S04]。

- **Cell Sandbox 发布里程碑 1 演示**：zynor 更新了可视化 CKB Cell 模型沙盒的首个里程碑进度，并放出可体验的线上演示版本 [S09]。

- **Fiber Pay Studio 申请 Spark 计划**：Frank 领衔的 Tefro Labs 提交新项目，定位为 CKB Fiber Network 的轻量支付请求与通道管理面板 [S06]。

- **CKB-VM B 扩展优化获关注**：mohanson 的深度技术文章引出社区提问，Tung_Pham 询问该优化能否落到底层 RISC-V 硬件上运行 [S07, S08]。

- **ckb-viz 工具收获好评**：janx、anihdev 等多位开发者点赞这款将 CKB 交易可视化为细胞流的新工具，认为界面出色且已 star 收藏 [S11, S12, S13]。

## 值得继续跟进

- neon.bit 上周透露 Vellum 提案未通过阶段 2 DAO 投票，今日 CDEX 表态会去该帖补充反对意见 [S10, S05]，需观察具体反馈内容和后续协商走向。

- Cell Sandbox 与 CKB Wallet Behaviour Intelligence 两个 Spark 项目都在早期交付阶段，前者演示已出 [S09]，后者刚推初始代码 [S15]，需跟踪月底交付质量。

- invisibook 隐私订单簿应用链持续低调推进，Lawliet_Chan 本周继续打磨论文并调研协作零知识证明代码库性能 [S14]，学术成果转化节奏有待观察。

## 来源索引

- `S01` [Cannot open the CKB DAO voting page](https://talk.nervos.org/t/cannot-open-the-ckb-dao-voting-page/10472/12) | CDEX | 2026-07-13 23:20:07 CST | I’m glad to see that another MOD has noticed this issue([DIS] Vellum: Reputation Extension on did:ckb - #4 by neon.bit) @neon.bit what is your view on this? Can the community expect an official response to the votes that were missed due to this access issue?
- `S02` [Cannot open the CKB DAO voting page](https://talk.nervos.org/t/cannot-open-the-ckb-dao-voting-page/10472/13) | truthixify | 2026-07-13 23:35:14 CST | You mean you want them to reverse proposals that have already passed so you can vote NO?
- `S03` [Cannot open the CKB DAO voting page](https://talk.nervos.org/t/cannot-open-the-ckb-dao-voting-page/10472/14) | CDEX | 2026-07-13 23:39:11 CST | I don’t think I ever said that. If I did, please point me to where I said it.
- `S04` [Cannot open the CKB DAO voting page](https://talk.nervos.org/t/cannot-open-the-ckb-dao-voting-page/10472/15) | neon.bit | 2026-07-14 00:00:20 CST | CDEX: I’m glad to see that another MOD has noticed this issue I’m not a mod CDEX: @neon.bit what is your view on this? Can the community expect an official response to the votes that were missed due to this access issue? In my opinion, the Metaforo issue was quite annoying,...
- `S05` [Cannot open the CKB DAO voting page](https://talk.nervos.org/t/cannot-open-the-ckb-dao-voting-page/10472/16) | CDEX | 2026-07-14 00:17:10 CST | Thank you for the clarification. I will check the concern and reply in that thread
- `S06` [Spark Program | Fiber Pay Studio](https://talk.nervos.org/t/spark-program-fiber-pay-studio/10485/1) | Frank | 2026-07-13 20:28:11 CST | Project Name Fiber Pay Studio — A Lightweight Payment-Request and Channel Dashboard for the CKB Fiber Network **Team / Individual Profile and Contact Information ** Name: Frank Role: Lead developer, Tefro Labs Background: Frontend-focused development studio applying to the CKB...
- `S07` [Deep Dive Into CKB-VM B Extension](https://talk.nervos.org/t/deep-dive-into-ckb-vm-b-extension/10484/1) | mohanson | 2026-07-13 14:25:40 CST | When writing code, we always hope it runs as fast as possible. The same is true for smart contracts on a blockchain. Faster execution means higher TPS. Of course, TPS is affected by many factors, and execution speed is only one dimension. At the same time, faster execution...
- `S08` [Deep Dive Into CKB-VM B Extension](https://talk.nervos.org/t/deep-dive-into-ckb-vm-b-extension/10484/2) | Tung_Pham | 2026-07-13 19:49:57 CST | mohanson: In the specification, RISC- Nice post! Thanks for sharing. So this optimization is inside CKBVM. Can it make to the host machine for example when I run CKBVM on an actual RISC-V machine(with B-extension)?
- `S09` [Spark Program | Cell Sandbox — A Visual Playground for the CKB Cell Model](https://talk.nervos.org/t/spark-program-cell-sandbox-a-visual-playground-for-the-ckb-cell-model/10326/16) | zynor | 2026-07-13 19:40:08 CST | Weekly Sync: Milestone 1 Progress Update Hi everyone, This week I worked on the Milestone 1 flow for Cell Sandbox and pushed the latest updates for review. Live demo: cell-sandbox-m.vercel.app Cell Sandbox — Visual CKB Cell Model Playground Build, inspect, and simulate CKB...
- `S10` [[DIS] Vellum: Reputation Extension on did:ckb](https://talk.nervos.org/t/dis-vellum-reputation-extension-on-did-ckb/10419/4) | neon.bit | 2026-07-13 18:08:45 CST | This proposal did not pass the stage 2 DAO vote. Presumably, the context involves this thread, although the reasoning is still unclear. It would be helpful, @CDEX, if you could leave feedback concerning your opposition to this proposal. It gives the proposer an opportunity to...
- `S11` [Ckb-viz: read any CKB transaction as a flow of cells](https://talk.nervos.org/t/ckb-viz-read-any-ckb-transaction-as-a-flow-of-cells/10482/4) | janx | 2026-07-13 15:22:10 CST | Very neat tool, love it!
- `S12` [Ckb-viz: read any CKB transaction as a flow of cells](https://talk.nervos.org/t/ckb-viz-read-any-ckb-transaction-as-a-flow-of-cells/10482/5) | anihdev | 2026-07-13 16:34:30 CST | cool stuff, the UI is amazing!
- `S13` [Ckb-viz: read any CKB transaction as a flow of cells](https://talk.nervos.org/t/ckb-viz-read-any-ckb-transaction-as-a-flow-of-cells/10482/6) | ArthurZhang | 2026-07-13 16:38:56 CST | looks promising, starred.
- `S14` [[DIS] Decentralized privacy order-book appchain based on CKB L1 - 2026.phase-1](https://talk.nervos.org/t/dis-decentralized-privacy-order-book-appchain-based-on-ckb-l1-2026-phase-1/10015/35) | Lawliet_Chan | 2026-07-13 13:01:03 CST | 周报 2026.7.12 继续打磨 invisibook 论文： Overleaf, Online LaTeX Editor 调研co-zk代码库 GitHub - TaceoLabs/co-snarks: Tooling for creating collaborative SNARKs for Circom and Noir circuits. · GitHub 开始使用测试性能数据
- `S15` [Spark Program | CKB Wallet Behaviour Intelligence](https://talk.nervos.org/t/spark-program-ckb-wallet-behaviour-intelligence/10338/10) | mulinya | 2026-07-13 04:55:10 CST | Hi @ xingtianchunyan, What’s done in week 1: Initial commit pushed: GitHub - FadhilMulinya/ckb-intel · GitHub Ingestion pipeline: give it a CKB address → it resolves the lock script hash (via CCC), pulls the transaction history from the CKB Explorer API (paginated), filters by...

## 活跃话题

1. [Cannot open the CKB DAO voting page](https://talk.nervos.org/t/cannot-open-the-ckb-dao-voting-page/10472) | 5 条近窗帖子 | 最新活动 2026-07-14 00:17:10 CST | tags: DAO
2. [Spark Program | Fiber Pay Studio](https://talk.nervos.org/t/spark-program-fiber-pay-studio/10485) | 1 条近窗帖子 | 最新活动 2026-07-13 20:28:11 CST | tags: Spark-Program
3. [Deep Dive Into CKB-VM B Extension](https://talk.nervos.org/t/deep-dive-into-ckb-vm-b-extension/10484) | 2 条近窗帖子 | 最新活动 2026-07-13 19:49:57 CST | tags: CKB-VM
4. [Spark Program | Cell Sandbox — A Visual Playground for the CKB Cell Model](https://talk.nervos.org/t/spark-program-cell-sandbox-a-visual-playground-for-the-ckb-cell-model/10326) | 1 条近窗帖子 | 最新活动 2026-07-13 19:40:08 CST | tags: In-Progress, Spark-Program
5. [[DIS] Vellum: Reputation Extension on did:ckb](https://talk.nervos.org/t/dis-vellum-reputation-extension-on-did-ckb/10419) | 1 条近窗帖子 | 最新活动 2026-07-13 18:08:45 CST | tags: CKB, dapp, testnet
6. [Ckb-viz: read any CKB transaction as a flow of cells](https://talk.nervos.org/t/ckb-viz-read-any-ckb-transaction-as-a-flow-of-cells/10482) | 3 条近窗帖子 | 最新活动 2026-07-13 16:38:56 CST | tags: CKB, CKB-VM, dapp
7. [[DIS] Decentralized privacy order-book appchain based on CKB L1 - 2026.phase-1](https://talk.nervos.org/t/dis-decentralized-privacy-order-book-appchain-based-on-ckb-l1-2026-phase-1/10015) | 1 条近窗帖子 | 最新活动 2026-07-13 13:01:03 CST | tags: appchain
8. [Spark Program | CKB Wallet Behaviour Intelligence](https://talk.nervos.org/t/spark-program-ckb-wallet-behaviour-intelligence/10338) | 1 条近窗帖子 | 最新活动 2026-07-13 04:55:10 CST | tags: CKB, In-Progress, Spark-Program

## 最近帖子摘录

- 2026-07-14 00:17:10 CST | CDEX | [Cannot open the CKB DAO voting page](https://talk.nervos.org/t/cannot-open-the-ckb-dao-voting-page/10472/16) | Thank you for the clarification. I will check the concern and reply in that thread
- 2026-07-14 00:00:20 CST | neon.bit | [Cannot open the CKB DAO voting page](https://talk.nervos.org/t/cannot-open-the-ckb-dao-voting-page/10472/15) | CDEX: I’m glad to see that another MOD has noticed this issue I’m not a mod CDEX: @neon.bit what is your view on this? Can the community expect an official response to the votes...
- 2026-07-13 23:39:11 CST | CDEX | [Cannot open the CKB DAO voting page](https://talk.nervos.org/t/cannot-open-the-ckb-dao-voting-page/10472/14) | I don’t think I ever said that. If I did, please point me to where I said it.
- 2026-07-13 23:35:14 CST | truthixify | [Cannot open the CKB DAO voting page](https://talk.nervos.org/t/cannot-open-the-ckb-dao-voting-page/10472/13) | You mean you want them to reverse proposals that have already passed so you can vote NO?
- 2026-07-13 23:20:07 CST | CDEX | [Cannot open the CKB DAO voting page](https://talk.nervos.org/t/cannot-open-the-ckb-dao-voting-page/10472/12) | I’m glad to see that another MOD has noticed this issue([DIS] Vellum: Reputation Extension on did:ckb - #4 by neon.bit) @neon.bit what is your view on this? Can the community...
- 2026-07-13 20:28:11 CST | Frank | [Spark Program | Fiber Pay Studio](https://talk.nervos.org/t/spark-program-fiber-pay-studio/10485/1) | Project Name Fiber Pay Studio — A Lightweight Payment-Request and Channel Dashboard for the CKB Fiber Network **Team / Individual Profile and Contact Information ** Name: Frank...
- 2026-07-13 19:49:57 CST | Tung_Pham | [Deep Dive Into CKB-VM B Extension](https://talk.nervos.org/t/deep-dive-into-ckb-vm-b-extension/10484/2) | mohanson: In the specification, RISC- Nice post! Thanks for sharing. So this optimization is inside CKBVM. Can it make to the host machine for example when I run CKBVM on an...
- 2026-07-13 19:40:08 CST | zynor | [Spark Program | Cell Sandbox — A Visual Playground for the CKB Cell Model](https://talk.nervos.org/t/spark-program-cell-sandbox-a-visual-playground-for-the-ckb-cell-model/10326/16) | Weekly Sync: Milestone 1 Progress Update Hi everyone, This week I worked on the Milestone 1 flow for Cell Sandbox and pushed the latest updates for review. Live demo: cell-...
- 2026-07-13 18:08:45 CST | neon.bit | [[DIS] Vellum: Reputation Extension on did:ckb](https://talk.nervos.org/t/dis-vellum-reputation-extension-on-did-ckb/10419/4) | This proposal did not pass the stage 2 DAO vote. Presumably, the context involves this thread, although the reasoning is still unclear. It would be helpful, @CDEX, if you could...
- 2026-07-13 16:38:56 CST | ArthurZhang | [Ckb-viz: read any CKB transaction as a flow of cells](https://talk.nervos.org/t/ckb-viz-read-any-ckb-transaction-as-a-flow-of-cells/10482/6) | looks promising, starred.
- 2026-07-13 16:34:30 CST | anihdev | [Ckb-viz: read any CKB transaction as a flow of cells](https://talk.nervos.org/t/ckb-viz-read-any-ckb-transaction-as-a-flow-of-cells/10482/5) | cool stuff, the UI is amazing!
- 2026-07-13 15:22:10 CST | janx | [Ckb-viz: read any CKB transaction as a flow of cells](https://talk.nervos.org/t/ckb-viz-read-any-ckb-transaction-as-a-flow-of-cells/10482/4) | Very neat tool, love it!
- 2026-07-13 14:25:40 CST | mohanson | [Deep Dive Into CKB-VM B Extension](https://talk.nervos.org/t/deep-dive-into-ckb-vm-b-extension/10484/1) | When writing code, we always hope it runs as fast as possible. The same is true for smart contracts on a blockchain. Faster execution means higher TPS. Of course, TPS is...
- 2026-07-13 13:01:03 CST | Lawliet_Chan | [[DIS] Decentralized privacy order-book appchain based on CKB L1 - 2026.phase-1](https://talk.nervos.org/t/dis-decentralized-privacy-order-book-appchain-based-on-ckb-l1-2026-phase-1/10015/35) | 周报 2026.7.12 继续打磨 invisibook 论文： Overleaf, Online LaTeX Editor 调研co-zk代码库 GitHub - TaceoLabs/co-snarks: Tooling for creating collaborative SNARKs for Circom and Noir circuits. ·...
- 2026-07-13 04:55:10 CST | mulinya | [Spark Program | CKB Wallet Behaviour Intelligence](https://talk.nervos.org/t/spark-program-ckb-wallet-behaviour-intelligence/10338/10) | Hi @ xingtianchunyan, What’s done in week 1: Initial commit pushed: GitHub - FadhilMulinya/ckb-intel · GitHub Ingestion pipeline: give it a CKB address → it resolves the lock...
