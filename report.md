# Nervos Talk 社区简报

- 统计窗口: 2026-11-22 06:16:54 CST 到 2026-11-23 06:16:54 CST
- 生成时间: 2026-11-23 06:17:00 CST
- 话题数: 5
- 帖子数: 6
- 作者数: 6
- 总结模式: ai:openai-compatible

## 社区总结

## 今日发生了什么

今天论坛的主要动静来自项目进展和资助申请，而不是长篇技术争论[S01, S02, S04, S05, S06]。KeyMe 帖继续讨论 v0/v1 边界与 `combine()` 的作用[S02]，FiberVPN 则在 Spark Program 发出 750 美元等值 CKB 的资助申请[S06]。另外，隐私订单簿 appchain 更新了周报，Tranfr 报告问题修复，Turnmark 只收到一句简短好评[S03, S04, S05]。整体看，今天内容量不大，社区偏平静[S01, S02, S03, S04, S05, S06]。

## 重点话题

- KeyMe 帖里出现硬件经验与过往项目案例的询问[S01]，随后回复称相关设想属于 v1，v0 刻意收窄，并解释 `combine()` 是共同签名原语而非构造协议[S02]。
- FiberVPN 在 Spark Program 发帖申请 750 美元等值 CKB，项目定位为基于 Nervos Fiber Network 的按小时/按 MB 付费 WireGuard VPN 出口网关[S06]。
- 隐私订单簿 appchain 发布周报，继续上周 Invisibook 论文并整理 Invisibook 共识，同时准备 Proof of Buy 论文材料[S04]。
- Tranfr 项目方表示问题已修复，并请 @Hanssen 到 GitHub 仓库复查[S05]。
- Turnmark 测试网帖子下只有一句“its cool”的回复，没有展开讨论[S03]。

## 值得继续跟进

- KeyMe 的 v0/v1 边界和 `combine()` 在交易变化时的签名处理值得看后续完整说明[S02]。
- FiberVPN 的资助申请是否获批、收款地址与后续里程碑尚待观察，材料目前只到申请阶段[S06]。
- 隐私订单簿 appchain 的 PoB 论文材料与 Invisibook 共识整理是否继续更新值得跟进[S04]；Tranfr 的修复是否得到 Hanssen 确认也尚未在材料中体现[S05]。

## 来源索引

- `S01` [[DIS] KeyMe — CKB's PSBT: Open Air-Gapped Signing and the First DIY Hardware](https://talk.nervos.org/t/dis-keyme-ckbs-psbt-open-air-gapped-signing-and-the-first-diy-hardware/11258/8) | Han_Solo | 2026-11-22 21:13:16 CST | WuodOdhis: I am well versed in the hardware side of this build — board-level design, power, displays, scanners and embedded debugging Do you have previous examples of hardware projects that you have worked on?
- `S02` [[DIS] KeyMe — CKB's PSBT: Open Air-Gapped Signing and the First DIY Hardware](https://talk.nervos.org/t/dis-keyme-ckbs-psbt-open-air-gapped-signing-and-the-first-diy-hardware/11258/9) | WuodOdhis | 2026-11-23 00:35:26 CST | Thanks. Both are the right questions, and both land in v1 territory. v0 is deliberately narrow. combine() is the co-signing primitive, not the construction protocol. It merges per-group signatures on the same transaction (tx_hash); if the transaction changes, the signature is...
- `S03` [Turnmark: short-round Up/Down prediction markets on CKB, live on testnet](https://talk.nervos.org/t/turnmark-short-round-up-down-prediction-markets-on-ckb-live-on-testnet/11250/2) | RikoKurnia | 2026-11-23 00:17:13 CST | its cool
- `S04` [[DIS] Decentralized privacy order-book appchain based on CKB L1 - 2026.phase-1](https://talk.nervos.org/t/dis-decentralized-privacy-order-book-appchain-based-on-ckb-l1-2026-phase-1/10015/54) | Lawliet_Chan | 2026-11-22 20:29:09 CST | 周报 2026.11.22 继续上周Invisibook论文 整理invisibook共识 proof of buy的论文材料准备： Proof of Buy（PoB）论文构思：L2 抗审查动机、共识安全目标与研究路线（通用 L1） - Google Docs
- `S05` [Tranfr — Programmable Recovery for CKB](https://talk.nervos.org/t/tranfr-programmable-recovery-for-ckb/10644/37) | SalmanDev | 2026-11-22 19:40:29 CST | Hi @Hanssen the issues are fixed, please check GitHub - salmansarwarr/Tranfr: Tranfr - Programmable Asset Continuity for web3. Inactivity recovery for self-custody. · GitHub
- `S06` [Spark Program | FiberVPN: Pay-Per-Hour WireGuard Tunnels over Fiber](https://talk.nervos.org/t/spark-program-fibervpn-pay-per-hour-wireguard-tunnels-over-fiber/11300/1) | akanjacson | 2026-11-22 19:13:29 CST | Project: FiberVPN Applicant: Akan Theodore (kd-designs on GitHub: GitHub - kd-designs/fibervpn: Pay-per-hour and pay-per-MB WireGuard VPN exit gateway powered by Nervos Fiber Network · GitHub ) Funding requested: $750 USD equivalent in CKB (payout address shared on approval)...

## 活跃话题

1. [[DIS] KeyMe — CKB's PSBT: Open Air-Gapped Signing and the First DIY Hardware](https://talk.nervos.org/t/dis-keyme-ckbs-psbt-open-air-gapped-signing-and-the-first-diy-hardware/11258) | 2 条近窗帖子 | 最新活动 2026-11-23 00:35:26 CST
2. [Turnmark: short-round Up/Down prediction markets on CKB, live on testnet](https://talk.nervos.org/t/turnmark-short-round-up-down-prediction-markets-on-ckb-live-on-testnet/11250) | 1 条近窗帖子 | 最新活动 2026-11-23 00:17:13 CST | tags: DeFi, Oracle
3. [[DIS] Decentralized privacy order-book appchain based on CKB L1 - 2026.phase-1](https://talk.nervos.org/t/dis-decentralized-privacy-order-book-appchain-based-on-ckb-l1-2026-phase-1/10015) | 1 条近窗帖子 | 最新活动 2026-11-22 20:29:09 CST | tags: appchain
4. [Tranfr — Programmable Recovery for CKB](https://talk.nervos.org/t/tranfr-programmable-recovery-for-ckb/10644) | 1 条近窗帖子 | 最新活动 2026-11-22 19:40:29 CST | tags: In-Progress
5. [Spark Program | FiberVPN: Pay-Per-Hour WireGuard Tunnels over Fiber](https://talk.nervos.org/t/spark-program-fibervpn-pay-per-hour-wireguard-tunnels-over-fiber/11300) | 1 条近窗帖子 | 最新活动 2026-11-22 19:13:29 CST | tags: Spark-Program

## 最近帖子摘录

- 2026-11-23 00:35:26 CST | WuodOdhis | [[DIS] KeyMe — CKB's PSBT: Open Air-Gapped Signing and the First DIY Hardware](https://talk.nervos.org/t/dis-keyme-ckbs-psbt-open-air-gapped-signing-and-the-first-diy-hardware/11258/9) | Thanks. Both are the right questions, and both land in v1 territory. v0 is deliberately narrow. combine() is the co-signing primitive, not the construction protocol. It merges...
- 2026-11-23 00:17:13 CST | RikoKurnia | [Turnmark: short-round Up/Down prediction markets on CKB, live on testnet](https://talk.nervos.org/t/turnmark-short-round-up-down-prediction-markets-on-ckb-live-on-testnet/11250/2) | its cool
- 2026-11-22 21:13:16 CST | Han_Solo | [[DIS] KeyMe — CKB's PSBT: Open Air-Gapped Signing and the First DIY Hardware](https://talk.nervos.org/t/dis-keyme-ckbs-psbt-open-air-gapped-signing-and-the-first-diy-hardware/11258/8) | WuodOdhis: I am well versed in the hardware side of this build — board-level design, power, displays, scanners and embedded debugging Do you have previous examples of hardware...
- 2026-11-22 20:29:09 CST | Lawliet_Chan | [[DIS] Decentralized privacy order-book appchain based on CKB L1 - 2026.phase-1](https://talk.nervos.org/t/dis-decentralized-privacy-order-book-appchain-based-on-ckb-l1-2026-phase-1/10015/54) | 周报 2026.11.22 继续上周Invisibook论文 整理invisibook共识 proof of buy的论文材料准备： Proof of Buy（PoB）论文构思：L2 抗审查动机、共识安全目标与研究路线（通用 L1） - Google Docs
- 2026-11-22 19:40:29 CST | SalmanDev | [Tranfr — Programmable Recovery for CKB](https://talk.nervos.org/t/tranfr-programmable-recovery-for-ckb/10644/37) | Hi @Hanssen the issues are fixed, please check GitHub - salmansarwarr/Tranfr: Tranfr - Programmable Asset Continuity for web3. Inactivity recovery for self-custody. · GitHub
- 2026-11-22 19:13:29 CST | akanjacson | [Spark Program | FiberVPN: Pay-Per-Hour WireGuard Tunnels over Fiber](https://talk.nervos.org/t/spark-program-fibervpn-pay-per-hour-wireguard-tunnels-over-fiber/11300/1) | Project: FiberVPN Applicant: Akan Theodore (kd-designs on GitHub: GitHub - kd-designs/fibervpn: Pay-per-hour and pay-per-MB WireGuard VPN exit gateway powered by Nervos Fiber...
