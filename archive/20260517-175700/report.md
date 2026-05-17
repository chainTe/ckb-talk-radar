# Nervos Talk 社区简报

- 统计窗口: 2026-05-17 01:57:00 CST 到 2026-05-18 01:57:00 CST
- 生成时间: 2026-05-18 01:57:07 CST
- 话题数: 5
- 帖子数: 5
- 作者数: 4
- 总结模式: ai:openrouter

## 社区总结

## 今日发生了什么

今天 Nervos Talk 论坛活跃度一般，主要围绕几个长期项目进行中的技术更新。[S01, S02, S03, S04, S05] 最活跃的是 Invisibook 隐私订单簿项目发布周报，以及 CKB-UGMP 无感铸造基础设施和 Rosen Bridge 集成各有进展。[S02, S03, S01]

## 重点话题

- **Invisibook 隐私订单簿持续推进**：开发者 Lawliet_Chan 公布周报，已完成论文 abstract 和 introduce 部分，并正在开发基于 SPDZ 协议和 Poseidon 哈希的 MPC 订单结算模块，相关代码已提交 GitHub PR。[S02]

- **CKB-UGMP 展示大厅初见雏形**：项目本周推进了展示大厅建设，理论上已可展示图片、CID、文件大小等 DOB 信息，并补充了多维度反查功能；当前已具备完整演示链路，但签名问题仍在等待解决后才能继续调试上链功能。[S03]

- **Rosen Bridge 团队主动答疑**：phroi 表示团队随时在帖中解答关于 CKB 集成 Rosen Bridge 的任何问题，显示该跨链桥项目仍在持续运营并与社区保持沟通。[S01]

- **Nervos DAO Treasury 讨论转战 GitHub**：chenyukang 回应 phroi 的反馈后，将概念验证的进一步讨论迁移至 GitHub issue，并发布了代码层面的解释，方便进行行内代码评审。[S04]

- **iCKB 技术栈完成 CCC 迁移更新**：phroi 更新了 iCKB 代码库状态，整个 TypeScript 技术栈（含 SDK、接口、机器人、DAO 工具等）已全面基于 CCC 重建，成为当前部署脚本的主流代码库。[S05]

## 值得继续跟进

- Invisibook 的 MPC 订单结算模块实际运行性能与安全性审计进展，目前仅见代码 PR 提交。[S02]

- CKB-UGMP 的签名问题何时解决将直接决定演示链路能否真正跑通上链，需要观察下周更新。[S03]

- iCKB 完成 CCC 迁移后的用户实际采用情况，以及 dCKB 救援资金的后续拨款是否跟得上开发节奏。[S05]

## 来源索引

- `S01` [[DIS] CKB Integration for Rosen Bridge](https://talk.nervos.org/t/dis-ckb-integration-for-rosen-bridge/9756/142) | phroi | 2026-05-18 01:25:48 CST | If anybody has any question about the Rosen Bridge and its integration progress, we are always available here Love & Peace, Phroi
- `S02` [[DIS] Decentralized privacy order-book appchain based on CKB L1 - 2026.phase-1](https://talk.nervos.org/t/dis-decentralized-privacy-order-book-appchain-based-on-ckb-l1-2026-phase-1/10015/27) | Lawliet_Chan | 2026-05-17 21:48:27 CST | 周报 2026.5.17 完成Invisibook论文的 abstract和introduce部分 开发MPC订单结算模块的功能： spdz poseidon with ark-mpc by Lawliet-Chan · Pull Request #1 · invisibook-lab/invisibook · GitHub
- `S03` [Spark Program | CKB-UGMP —— A Universal Spore/DOB Seamless Minting Infrastructure Prototype on CKB —— 基于 CKB 的通用 Spore/DOB 无感铸造基础设施原型](https://talk.nervos.org/t/spark-program-ckb-ugmp-a-universal-spore-dob-seamless-minting-infrastructure-prototype-on-ckb-ckb-spore-dob/10098/21) | HNO3Miracle | 2026-05-17 14:54:08 CST | 各位好，分享一下这周的工作： 本周完成 本周推进了展示大厅的建设。由于签名的问题，等待问题解决后进一步调试 推进了展示大厅的建设，理论上可以展示图片 理论上会展示图片、CID、文件大小、Spore ID、tx hash。 又补了 lookup，可按 CID、IPFS URI、Spore ID、tx hash 反查记录。 当前状态 项目现在已经具备一条演示链路，理论上具有签名上链的能力： 选择图片资源。 上传到 Pinata / IPFS。 生成 DOB metadata 草案。 dry-run 生成本地模拟结果。 保存上传记录和 mint 草案。...
- `S04` [Pre-RFC Discussion: Activating the Nervos DAO Treasury](https://talk.nervos.org/t/pre-rfc-discussion-activating-the-nervos-dao-treasury/10143/20) | chenyukang | 2026-05-17 10:01:13 CST | Thanks @phroi 's feedback! I created a issue on the POC repo and posted a explanation there. It’s more convenient to discuss on Github such as we can inline code on Github comment: github.com/XuJiandong/ckb-vote-poc Questions for the poc opened 01:34AM - 17 May 26 UTC...
- `S05` [[DIS] iCKB & dCKB Rescuer Funding Proposal (Non-Coding Expenses)](https://talk.nervos.org/t/dis-ickb-dckb-rescuer-funding-proposal-non-coding-expenses/8369/29) | phroi | 2026-05-17 03:50:48 CST | Hey all, quick iCKB codebase update iCKB Stack is now the main TypeScript codebase around the deployed scripts: CCC-based SDK, interface, bot, DAO utilities, Limit Order utilities, tester, and Node runtime code. The reason is simple: CCC migration, and the February 2025...

## 活跃话题

1. [[DIS] CKB Integration for Rosen Bridge](https://talk.nervos.org/t/dis-ckb-integration-for-rosen-bridge/9756) | 1 条近窗帖子 | 最新活动 2026-05-18 01:25:48 CST
2. [[DIS] Decentralized privacy order-book appchain based on CKB L1 - 2026.phase-1](https://talk.nervos.org/t/dis-decentralized-privacy-order-book-appchain-based-on-ckb-l1-2026-phase-1/10015) | 1 条近窗帖子 | 最新活动 2026-05-17 21:48:27 CST | tags: appchain
3. [Spark Program | CKB-UGMP —— A Universal Spore/DOB Seamless Minting Infrastructure Prototype on CKB —— 基于 CKB 的通用 Spore/DOB 无感铸造基础设施原型](https://talk.nervos.org/t/spark-program-ckb-ugmp-a-universal-spore-dob-seamless-minting-infrastructure-prototype-on-ckb-ckb-spore-dob/10098) | 1 条近窗帖子 | 最新活动 2026-05-17 14:54:08 CST | tags: In-Progress, Spark-Program
4. [Pre-RFC Discussion: Activating the Nervos DAO Treasury](https://talk.nervos.org/t/pre-rfc-discussion-activating-the-nervos-dao-treasury/10143) | 1 条近窗帖子 | 最新活动 2026-05-17 10:01:13 CST | tags: CKB
5. [[DIS] iCKB & dCKB Rescuer Funding Proposal (Non-Coding Expenses)](https://talk.nervos.org/t/dis-ickb-dckb-rescuer-funding-proposal-non-coding-expenses/8369) | 1 条近窗帖子 | 最新活动 2026-05-17 03:50:48 CST

## 最近帖子摘录

- 2026-05-18 01:25:48 CST | phroi | [[DIS] CKB Integration for Rosen Bridge](https://talk.nervos.org/t/dis-ckb-integration-for-rosen-bridge/9756/142) | If anybody has any question about the Rosen Bridge and its integration progress, we are always available here Love & Peace, Phroi
- 2026-05-17 21:48:27 CST | Lawliet_Chan | [[DIS] Decentralized privacy order-book appchain based on CKB L1 - 2026.phase-1](https://talk.nervos.org/t/dis-decentralized-privacy-order-book-appchain-based-on-ckb-l1-2026-phase-1/10015/27) | 周报 2026.5.17 完成Invisibook论文的 abstract和introduce部分 开发MPC订单结算模块的功能： spdz poseidon with ark-mpc by Lawliet-Chan · Pull Request #1 · invisibook-lab/invisibook · GitHub
- 2026-05-17 14:54:08 CST | HNO3Miracle | [Spark Program | CKB-UGMP —— A Universal Spore/DOB Seamless Minting Infrastructure Prototype on CKB —— 基于 CKB 的通用 Spore/DOB 无感铸造基础设施原型](https://talk.nervos.org/t/spark-program-ckb-ugmp-a-universal-spore-dob-seamless-minting-infrastructure-prototype-on-ckb-ckb-spore-dob/10098/21) | 各位好，分享一下这周的工作： 本周完成 本周推进了展示大厅的建设。由于签名的问题，等待问题解决后进一步调试 推进了展示大厅的建设，理论上可以展示图片 理论上会展示图片、CID、文件大小、Spore ID、tx hash。 又补了 lookup，可按 CID、IPFS URI、Spore ID、tx hash 反查记录。 当前状态...
- 2026-05-17 10:01:13 CST | chenyukang | [Pre-RFC Discussion: Activating the Nervos DAO Treasury](https://talk.nervos.org/t/pre-rfc-discussion-activating-the-nervos-dao-treasury/10143/20) | Thanks @phroi 's feedback! I created a issue on the POC repo and posted a explanation there. It’s more convenient to discuss on Github such as we can inline code on Github...
- 2026-05-17 03:50:48 CST | phroi | [[DIS] iCKB & dCKB Rescuer Funding Proposal (Non-Coding Expenses)](https://talk.nervos.org/t/dis-ickb-dckb-rescuer-funding-proposal-non-coding-expenses/8369/29) | Hey all, quick iCKB codebase update iCKB Stack is now the main TypeScript codebase around the deployed scripts: CCC-based SDK, interface, bot, DAO utilities, Limit Order...
