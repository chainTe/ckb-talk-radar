# Nervos Talk 社区简报

- 统计窗口: 2026-08-19 01:23:30 CST 到 2026-08-20 01:23:30 CST
- 生成时间: 2026-08-20 01:23:41 CST
- 话题数: 8
- 帖子数: 12
- 作者数: 8
- 总结模式: ai:openai-compatible

## 社区总结

## 今日发生了什么

过去 24 小时，Nervos 论坛最集中的动态来自 Spark 计划：委员会一边向 Fiber RGB++ Swap 发放首期 20% 拨款，另一边拒绝了 Cellar，并维持对 Corven 的拒绝 [S01, S02, S07]。同时，Tranfr 可编程恢复方案在社区帮助下修复了一个关键安全风险，TeamCKB 也发布了包含 CKB v0.209.0 的进展日志 [S03, S04, S08]。此外，LS-IDL 注册表开放试用，Rosen Bridge 和 CKB-VM 验证工作仍在继续推进 [S09, S11, S12]。

## 重点话题

- **Spark 计划：一笔拨款发出，两个项目被拒** [S01, S02, S07]。Fiber RGB++ Swap 已收到首期 121,952 CKB（占 20%），正等待对方确认并提交首次进度更新 [S01]；Spark 委员会维持对 Corven 云开发平台的拒绝，理由是核心要素没有变化 [S02]；Cellar（CKB Cell 容量租赁市场）也因项目范围和设计成熟度不足被驳回 [S07]。

- **Tranfr 讨论取得关键进展** [S03, S04]。tianji 针对 owner-freeze 路径提出了 CKB 原生构造建议，避免使用调用者选择的截止时间 [S03]；项目方 SalmanDev 表示这修复了提案中最大的开放风险——stale-header attack [S04]。社区还提到了类似项目 InheritVault，但 SalmanDev 认为两者方向不同：Tranfr 的核心是基于不活跃状态的 check-in 机制 [S05, S06]。

- **CKB v0.209.0 发布，开发重心转向 tx-pool** [S08]。TeamCKB 开发日志显示，该版本修复了内存增长和 tx-pool ancestor eviction 问题，并完成了网络与轻客户端加固；下一阶段将继续推进 tx-pool 架构工作 [S08]。

- **LS-IDL 注册表开放试用** [S09]。Unified Registry 已支持 LS-IDL 工作流，用户可以连接 CKB 钱包直接在 cellscript.dev 上查询接口字节 [S09]；社区成员 OWK50GA 认为这个流程非常干净，可以作为整个社区使用的标准 [S10]。

- **Rosen Bridge 与 CKB-VM 验证同步更新** [S11, S12]。Rosen Bridge 的 CKB 集成讨论继续聚焦于跨“观察、解释、批准、签名”环节的不可变身份问题 [S11]；CKB-VM Sail 验证冲刺发布第二周成果，加入了端到端 RVFI-DII 差分测试、PC 回绕检查以及可重放测试产物 [S12]。

## 值得继续跟进

- **Tranfr 的安全修复能否最终落地**：社区提出的 CKB-native 构造已被作者接受，但还需看后续完整实现，确认 stale-header attack 风险是否被彻底消除 [S03, S04]。

- **Spark 被拒项目的后续动向**：Corven 是修订后仍被维持拒绝，Cellar 则因成熟度不足被否决，这两个团队是否会调整方案或继续沟通值得关注 [S02, S07]；同时，Fiber RGB++ Swap 拿到首笔拨款后能否按时交出首个进度更新，也是近期看点 [S01]。

- **CKB v0.209.0 上线后的实际表现**：该版本涉及内存增长和 tx-pool 相关问题修复，加上后续 tx-pool 架构工作还在推进，社区需要继续观察主网和轻客户端的稳定性 [S08]。

## 来源索引

- `S01` [Spark Program | Fiber RGB++ Swap](https://talk.nervos.org/t/spark-program-fiber-rgb-swap/10487/24) | xingtianchunyan | 2026-08-20 01:10:46 CST | Hi @Carl, All noted. The first installment ( 121,952 CKB, 20% ) has been disbursed: Transfer Hash : 0xd748d4f8d2e80837e11cca7c7cf56c6fb8a79781db3bf89d5c52967ce6761730 Please confirm once received. We looking forward to your first progress update. Best, xingtian, On behalf of...
- `S02` [Spark Program | Corven — Cloud Development Platform for the CKB Ecosystem](https://talk.nervos.org/t/spark-program-corven-cloud-development-platform-for-the-ckb-ecosystem/10528/6) | xingtianchunyan | 2026-08-20 00:32:17 CST | Hi @lestonEth, It’s great to see your thoughtful consideration of and commitment to your proposal. The committee has reviewed your revised Corven project proposal and decided to uphold the rejection. The reasons are as follows: No change with the core elements: Although you...
- `S03` [Tranfr — Programmable Recovery for CKB](https://talk.nervos.org/t/tranfr-programmable-recovery-for-ckb/10644/2) | tianji | 2026-08-19 10:16:41 CST | I looked at the irreversible-expiry boundary more closely and would suggest the following CKB-native construction for the critical owner-freeze path. Core correction For an owner operation that is valid only before a stored deadline, I would not use a caller-selected...
- `S04` [Tranfr — Programmable Recovery for CKB](https://talk.nervos.org/t/tranfr-programmable-recovery-for-ckb/10644/3) | SalmanDev | 2026-08-19 20:24:46 CST | Wow, I really appreciate you looking into this. Thanks for the suggestion, it fixes the biggest open risk in the proposal with stale-header attacks on the freeze mechanism.
- `S05` [Tranfr — Programmable Recovery for CKB](https://talk.nervos.org/t/tranfr-programmable-recovery-for-ckb/10644/4) | neon.bit | 2026-08-19 22:21:51 CST | I saw @Ajay worked on something similar, it’s worth checking out: github.com/Nervos-Community-Catalyst/CKBuilder-projects InheritVault: a time-locked CKB inheritance vault dApp opened 10:52PM - 02 Mar 26 UTC Ajayfrizzy Review request # InheritVault: a time-locked CKB...
- `S06` [Tranfr — Programmable Recovery for CKB](https://talk.nervos.org/t/tranfr-programmable-recovery-for-ckb/10644/5) | SalmanDev | 2026-08-19 23:58:07 CST | Thanks for the pointer, took a look. Ajay is solving a different problem and approach. It’s a fixed-date vault (lock funds, unlock at one target block/timestamp), no check-in or reset mechanism. Tranfr’s core piece is the inactivity-based check-in: owner can keep extending...
- `S07` [Spark Program | Cellar — A Capacity Leasing Market for CKB Cells](https://talk.nervos.org/t/spark-program-cellar-a-capacity-leasing-market-for-ckb-cells/10492/13) | xingtianchunyan | 2026-08-19 23:53:14 CST | Hi @Carlos_Bunny , We are pleased to see your interest in the Spark Program. After reviewing the application, the Spark Committee has regrettably decided to reject the Cellar project. The reasons are as follows: Project scope and design maturity: Although the project has...
- `S08` [TeamCKB Dev Log (Updated: August 19, 2026)](https://talk.nervos.org/t/teamckb-dev-log-updated-august-19-2026/8572/40) | CKBdev | 2026-08-19 20:38:28 CST | Updates This cycle (July 22 – August 19, 2026) focused on the CKB v0.209.0 release, network and light-client hardening, and the next phase of tx-pool architecture work. Key milestones include: CKB v0.209.0 shipped with fixes for memory growth, tx-pool ancestor eviction,...
- `S09` [LS-IDL: a Lock Script Interface Description Language for CKB (derive, validate, commit)](https://talk.nervos.org/t/ls-idl-a-lock-script-interface-description-language-for-ckb-derive-validate-commit/10596/2) | ArthurZhang | 2026-08-19 11:58:05 CST | A quick update for everyone following LS-IDL: the Unified Registry now supports the LS-IDL workflow. You can connect a CKB testnet or mainnet wallet and try it directly here: cellscript.dev CellScript Registry: LS-IDL lookup Fetch the exact interface bytes bound to a CKB code...
- `S10` [LS-IDL: a Lock Script Interface Description Language for CKB (derive, validate, commit)](https://talk.nervos.org/t/ls-idl-a-lock-script-interface-description-language-for-ckb-derive-validate-commit/10596/3) | OWK50GA | 2026-08-19 12:49:09 CST | This flow is so clean. The number of requirements of a registry that are here, that I didn’t think of myself is crazy. This passes for standard an entire community could use Well done, Ser
- `S11` [[DIS] CKB Integration for Rosen Bridge](https://talk.nervos.org/t/dis-ckb-integration-for-rosen-bridge/9756/148) | tianji | 2026-08-19 09:33:56 CST | Trying to follow the forum preference for shorter, incremental comments, I’ll keep this to one concrete continuation of the previous review. The previous comment ended on the need for one immutable identity across source observation, interpretation, approval, signing and...
- `S12` [Spark Program | CKB-VM Sail Validation Sprint：可复现的 RISC-V 语义差分工具、Lean 4 证明与 Rocq/Coq 兼容性 Spike](https://talk.nervos.org/t/spark-program-ckb-vm-sail-validation-sprint-risc-v-lean-4-rocq-coq-spike/10562/14) | TinyuengKwan | 2026-08-19 02:43:58 CST | Update: 已push第二周工作内容.主要包括以下工作: 在固定版本的 Sail-RISC-V 模拟器与 CKB-VM 之间增加端到端的 RVFI-DII 差分测试，包括二进制 DII 客户端、测试套件、按位置注入指令、架构状态比较，以及第 2 周的 RV64I 测试语料库。 同时，加强针对 PC 回绕情况的注入窗口检查，并添加可重放的测试产物以及负向差分测试。

## 活跃话题

1. [Spark Program | Fiber RGB++ Swap](https://talk.nervos.org/t/spark-program-fiber-rgb-swap/10487) | 1 条近窗帖子 | 最新活动 2026-08-20 01:10:46 CST | tags: In-Progress
2. [Spark Program | Corven — Cloud Development Platform for the CKB Ecosystem](https://talk.nervos.org/t/spark-program-corven-cloud-development-platform-for-the-ckb-ecosystem/10528) | 1 条近窗帖子 | 最新活动 2026-08-20 00:32:17 CST | tags: CKB, Grant, dapp
3. [Tranfr — Programmable Recovery for CKB](https://talk.nervos.org/t/tranfr-programmable-recovery-for-ckb/10644) | 4 条近窗帖子 | 最新活动 2026-08-19 23:58:07 CST
4. [Spark Program | Cellar — A Capacity Leasing Market for CKB Cells](https://talk.nervos.org/t/spark-program-cellar-a-capacity-leasing-market-for-ckb-cells/10492) | 1 条近窗帖子 | 最新活动 2026-08-19 23:53:14 CST | tags: Spark-Program, Submitted
5. [TeamCKB Dev Log (Updated: August 19, 2026)](https://talk.nervos.org/t/teamckb-dev-log-updated-august-19-2026/8572) | 1 条近窗帖子 | 最新活动 2026-08-19 20:38:28 CST | tags: CKB, CKB-VM, lang-en
6. [LS-IDL: a Lock Script Interface Description Language for CKB (derive, validate, commit)](https://talk.nervos.org/t/ls-idl-a-lock-script-interface-description-language-for-ckb-derive-validate-commit/10596) | 2 条近窗帖子 | 最新活动 2026-08-19 12:49:09 CST | tags: CKB
7. [[DIS] CKB Integration for Rosen Bridge](https://talk.nervos.org/t/dis-ckb-integration-for-rosen-bridge/9756) | 1 条近窗帖子 | 最新活动 2026-08-19 09:33:56 CST
8. [Spark Program | CKB-VM Sail Validation Sprint：可复现的 RISC-V 语义差分工具、Lean 4 证明与 Rocq/Coq 兼容性 Spike](https://talk.nervos.org/t/spark-program-ckb-vm-sail-validation-sprint-risc-v-lean-4-rocq-coq-spike/10562) | 1 条近窗帖子 | 最新活动 2026-08-19 02:43:58 CST | tags: CKB-VM, In-Progress

## 最近帖子摘录

- 2026-08-20 01:10:46 CST | xingtianchunyan | [Spark Program | Fiber RGB++ Swap](https://talk.nervos.org/t/spark-program-fiber-rgb-swap/10487/24) | Hi @Carl, All noted. The first installment ( 121,952 CKB, 20% ) has been disbursed: Transfer Hash : 0xd748d4f8d2e80837e11cca7c7cf56c6fb8a79781db3bf89d5c52967ce6761730 Please...
- 2026-08-20 00:32:17 CST | xingtianchunyan | [Spark Program | Corven — Cloud Development Platform for the CKB Ecosystem](https://talk.nervos.org/t/spark-program-corven-cloud-development-platform-for-the-ckb-ecosystem/10528/6) | Hi @lestonEth, It’s great to see your thoughtful consideration of and commitment to your proposal. The committee has reviewed your revised Corven project proposal and decided to...
- 2026-08-19 23:58:07 CST | SalmanDev | [Tranfr — Programmable Recovery for CKB](https://talk.nervos.org/t/tranfr-programmable-recovery-for-ckb/10644/5) | Thanks for the pointer, took a look. Ajay is solving a different problem and approach. It’s a fixed-date vault (lock funds, unlock at one target block/timestamp), no check-in or...
- 2026-08-19 23:53:14 CST | xingtianchunyan | [Spark Program | Cellar — A Capacity Leasing Market for CKB Cells](https://talk.nervos.org/t/spark-program-cellar-a-capacity-leasing-market-for-ckb-cells/10492/13) | Hi @Carlos_Bunny , We are pleased to see your interest in the Spark Program. After reviewing the application, the Spark Committee has regrettably decided to reject the Cellar...
- 2026-08-19 22:21:51 CST | neon.bit | [Tranfr — Programmable Recovery for CKB](https://talk.nervos.org/t/tranfr-programmable-recovery-for-ckb/10644/4) | I saw @Ajay worked on something similar, it’s worth checking out: github.com/Nervos-Community-Catalyst/CKBuilder-projects InheritVault: a time-locked CKB inheritance vault dApp...
- 2026-08-19 20:38:28 CST | CKBdev | [TeamCKB Dev Log (Updated: August 19, 2026)](https://talk.nervos.org/t/teamckb-dev-log-updated-august-19-2026/8572/40) | Updates This cycle (July 22 – August 19, 2026) focused on the CKB v0.209.0 release, network and light-client hardening, and the next phase of tx-pool architecture work. Key...
- 2026-08-19 20:24:46 CST | SalmanDev | [Tranfr — Programmable Recovery for CKB](https://talk.nervos.org/t/tranfr-programmable-recovery-for-ckb/10644/3) | Wow, I really appreciate you looking into this. Thanks for the suggestion, it fixes the biggest open risk in the proposal with stale-header attacks on the freeze mechanism.
- 2026-08-19 12:49:09 CST | OWK50GA | [LS-IDL: a Lock Script Interface Description Language for CKB (derive, validate, commit)](https://talk.nervos.org/t/ls-idl-a-lock-script-interface-description-language-for-ckb-derive-validate-commit/10596/3) | This flow is so clean. The number of requirements of a registry that are here, that I didn’t think of myself is crazy. This passes for standard an entire community could use...
- 2026-08-19 11:58:05 CST | ArthurZhang | [LS-IDL: a Lock Script Interface Description Language for CKB (derive, validate, commit)](https://talk.nervos.org/t/ls-idl-a-lock-script-interface-description-language-for-ckb-derive-validate-commit/10596/2) | A quick update for everyone following LS-IDL: the Unified Registry now supports the LS-IDL workflow. You can connect a CKB testnet or mainnet wallet and try it directly here:...
- 2026-08-19 10:16:41 CST | tianji | [Tranfr — Programmable Recovery for CKB](https://talk.nervos.org/t/tranfr-programmable-recovery-for-ckb/10644/2) | I looked at the irreversible-expiry boundary more closely and would suggest the following CKB-native construction for the critical owner-freeze path. Core correction For an...
- 2026-08-19 09:33:56 CST | tianji | [[DIS] CKB Integration for Rosen Bridge](https://talk.nervos.org/t/dis-ckb-integration-for-rosen-bridge/9756/148) | Trying to follow the forum preference for shorter, incremental comments, I’ll keep this to one concrete continuation of the previous review. The previous comment ended on the...
- 2026-08-19 02:43:58 CST | TinyuengKwan | [Spark Program | CKB-VM Sail Validation Sprint：可复现的 RISC-V 语义差分工具、Lean 4 证明与 Rocq/Coq 兼容性 Spike](https://talk.nervos.org/t/spark-program-ckb-vm-sail-validation-sprint-risc-v-lean-4-rocq-coq-spike/10562/14) | Update: 已push第二周工作内容.主要包括以下工作: 在固定版本的 Sail-RISC-V 模拟器与 CKB-VM 之间增加端到端的 RVFI-DII 差分测试，包括二进制 DII 客户端、测试套件、按位置注入指令、架构状态比较，以及第 2 周的 RV64I 测试语料库。 同时，加强针对 PC...
