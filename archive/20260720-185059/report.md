# Nervos Talk 社区简报

- 统计窗口: 2026-07-20 02:50:59 CST 到 2026-07-21 02:50:59 CST
- 生成时间: 2026-07-21 02:51:04 CST
- 话题数: 4
- 帖子数: 5
- 作者数: 4
- 总结模式: ai:openrouter

## 社区总结

## 今日发生了什么

今天论坛上，ArthurZhang 继续与社区深入讨论两个技术项目：链下 Cell 会话运行时 Myelin 的设计细节，以及 CKB Cell 容量租赁市场 Cellar 的协议架构优化。[S01, S03] 另外，Fiber 桌面版重建项目完成了第二笔里程碑付款。[S05]

## 重点话题

- **Myelin 验证机制讨论**：ArthurZhang 澄清了验证器的工作流程——接收候选批次后，重新计算 CellDAG 排序，在同款 CKB-VM 配置下运行代码块，仅对最终结果签名，暂时不处理 P2P 中继或内存池八卦层。[S01] Ophiuchus 随后理解了这一设计，认可"聚焦最终哈希并只重放争议代码块"比原先设想的更高效。[S02]

- **Cellar 协议设计再细化**：ArthurZhang 从分离关注点角度肯定了讨论者的观点，但指出未必需要同时部署独立的 CellarLeaseLock 和 CellarLeaseType，建议一个定制 lock 搭配 type 已能构成小型分布式协议，避免过度复杂化。[S03]

- **Fiber 桌面版里程碑付款到账**：zz_tovarishch 公布了 M2 里程碑的 CKB 链上交易哈希，按 $0.00088 单价核算，共转出约 170.5 万 CKB。[S05]

## 值得继续跟进

- Myelin 的 P2P 中继与内存池八卦层未来是否会纳入路线图，目前作者明确表示"暂时不解决"，这部分扩展性值得观察。[S01]

- Cellar 的锁脚本与类型脚本具体如何精简合并，ArthurZhang 只点到为止，后续能否产出更完整的协议规范待确认。[S03]

- 隐私订单簿应用链项目虽有"周报 2026.7.19"更新，但内容仅一句话说明"继续上周的工作"，实质性进展不足，信息偏少。[S04]

## 来源索引

- `S01` [Introducing Myelin: a CKB-aligned off-chain Cell session runtime](https://talk.nervos.org/t/introducing-myelin-a-ckb-aligned-off-chain-cell-session-runtime/10498/3) | ArthurZhang | 2026-07-20 12:18:57 CST | Hey @Ophiuchus, appreciate you engaging with it. For now Myelin does not try to solve P2P relay or mempool gossip. A validator receives a candidate batch, recomputes the CellDAG order, runs the chunks under the same CKB-VM profile, and signs only the resulting...
- `S02` [Introducing Myelin: a CKB-aligned off-chain Cell session runtime](https://talk.nervos.org/t/introducing-myelin-a-ckb-aligned-off-chain-cell-session-runtime/10498/4) | Ophiuchus | 2026-07-20 16:27:16 CST | Oh yes I get it now. Focusing on the final hash and only replaying the disputed chunk sounds much more efficient than what I had in mind. Thanks for the explanation.
- `S03` [Spark Program | Cellar — A Capacity Leasing Market for CKB Cells](https://talk.nervos.org/t/spark-program-cellar-a-capacity-leasing-market-for-ckb-cells/10492/7) | ArthurZhang | 2026-07-20 14:29:44 CST | I reckon from certain angle your statement is defensible as a separation-of-concerns design. But from my pov, you probably indeed need not to deploy, say, both a bespoke CellarLeaseLock and a CellarLeaseType, as a bespoke lock plus type creates a small distributed protocol...
- `S04` [[DIS] Decentralized privacy order-book appchain based on CKB L1 - 2026.phase-1](https://talk.nervos.org/t/dis-decentralized-privacy-order-book-appchain-based-on-ckb-l1-2026-phase-1/10015/36) | Lawliet_Chan | 2026-07-20 09:32:49 CST | 周报 2026.7.19 继续上周的工作
- `S05` [[DIS] Fiber Desktop v1 ground-up rebuild and launch — fnn desktop app](https://talk.nervos.org/t/dis-fiber-desktop-v1-ground-up-rebuild-and-launch-fnn-desktop-app/10317/23) | zz_tovarishch | 2026-07-20 09:14:38 CST | M2 Payout $1,500/ @0.00088 = 1,704,546 CKB https://explorer.nervos.org/transaction/0x1565338fd543a257906e5debe6b4b5cedbe4cff86af47ec620e18a3bfb838b9a

## 活跃话题

1. [Introducing Myelin: a CKB-aligned off-chain Cell session runtime](https://talk.nervos.org/t/introducing-myelin-a-ckb-aligned-off-chain-cell-session-runtime/10498) | 2 条近窗帖子 | 最新活动 2026-07-20 16:27:16 CST | tags: CKB-VM, CellScript, lang-en
2. [Spark Program | Cellar — A Capacity Leasing Market for CKB Cells](https://talk.nervos.org/t/spark-program-cellar-a-capacity-leasing-market-for-ckb-cells/10492) | 1 条近窗帖子 | 最新活动 2026-07-20 14:29:44 CST | tags: Spark-Program, lang-en
3. [[DIS] Decentralized privacy order-book appchain based on CKB L1 - 2026.phase-1](https://talk.nervos.org/t/dis-decentralized-privacy-order-book-appchain-based-on-ckb-l1-2026-phase-1/10015) | 1 条近窗帖子 | 最新活动 2026-07-20 09:32:49 CST | tags: appchain
4. [[DIS] Fiber Desktop v1 ground-up rebuild and launch — fnn desktop app](https://talk.nervos.org/t/dis-fiber-desktop-v1-ground-up-rebuild-and-launch-fnn-desktop-app/10317) | 1 条近窗帖子 | 最新活动 2026-07-20 09:14:38 CST | tags: fiber

## 最近帖子摘录

- 2026-07-20 16:27:16 CST | Ophiuchus | [Introducing Myelin: a CKB-aligned off-chain Cell session runtime](https://talk.nervos.org/t/introducing-myelin-a-ckb-aligned-off-chain-cell-session-runtime/10498/4) | Oh yes I get it now. Focusing on the final hash and only replaying the disputed chunk sounds much more efficient than what I had in mind. Thanks for the explanation.
- 2026-07-20 14:29:44 CST | ArthurZhang | [Spark Program | Cellar — A Capacity Leasing Market for CKB Cells](https://talk.nervos.org/t/spark-program-cellar-a-capacity-leasing-market-for-ckb-cells/10492/7) | I reckon from certain angle your statement is defensible as a separation-of-concerns design. But from my pov, you probably indeed need not to deploy, say, both a bespoke...
- 2026-07-20 12:18:57 CST | ArthurZhang | [Introducing Myelin: a CKB-aligned off-chain Cell session runtime](https://talk.nervos.org/t/introducing-myelin-a-ckb-aligned-off-chain-cell-session-runtime/10498/3) | Hey @Ophiuchus, appreciate you engaging with it. For now Myelin does not try to solve P2P relay or mempool gossip. A validator receives a candidate batch, recomputes the CellDAG...
- 2026-07-20 09:32:49 CST | Lawliet_Chan | [[DIS] Decentralized privacy order-book appchain based on CKB L1 - 2026.phase-1](https://talk.nervos.org/t/dis-decentralized-privacy-order-book-appchain-based-on-ckb-l1-2026-phase-1/10015/36) | 周报 2026.7.19 继续上周的工作
- 2026-07-20 09:14:38 CST | zz_tovarishch | [[DIS] Fiber Desktop v1 ground-up rebuild and launch — fnn desktop app](https://talk.nervos.org/t/dis-fiber-desktop-v1-ground-up-rebuild-and-launch-fnn-desktop-app/10317/23) | M2 Payout $1,500/ @0.00088 = 1,704,546 CKB https://explorer.nervos.org/transaction/0x1565338fd543a257906e5debe6b4b5cedbe4cff86af47ec620e18a3bfb838b9a
