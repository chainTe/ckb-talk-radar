# Nervos Talk 社区简报

- 统计窗口: 2026-08-20 01:25:23 CST 到 2026-08-21 01:25:23 CST
- 生成时间: 2026-08-21 01:25:27 CST
- 话题数: 6
- 帖子数: 8
- 作者数: 7
- 总结模式: ai:openai-compatible

## 社区总结

## 今日发生了什么

过去 24 小时，Nervos Talk 的主要热度集中在 Fiber 网络：一边是社区成员将《反恐精英》移植到 Fiber 上进行真实支付结算的原型展示，引发兴奋讨论 [S02, S03]；另一边有用户对 Fiber 主网 UDT 中 USDI 的存续提出疑问 [S01]。此外，Corven 云开发平台提案正式转入 CKB Community Fund DAO，并被协调员提醒需要写明预算 [S07, S04, S05]。

## 重点话题

- **Fiber 上的《反恐精英》移植**：RetricSu 发布了基于 Fiber 的 1v1 射击游戏原型，每次命中伤害都通过 Fiber 支付通道真实结算，输家无法拒付，目前运行在 testnet 上 [S02]。社区成员 knmo 认为这是 Fiber 与经典游戏的“历史性结合” [S03]。

- **USDI 与 Fiber 主网 UDT 疑问**：有用户提问：如果 USDI 已在 CKB 上停产，为什么 Fiber 仍将其列为主网 UDT？[S01] 并追问 Fiber CCH swaps 实际使用的主网 UDT 是什么 [S01]。

- **Corven 提案迁移至社区基金 DAO**：lestonEth 在 Spark 计划帖中表示尊重委员会决定，将 Corven 项目提案移到 CKB Community Fund DAO [S07]，随后发布了更新版提案，称已纳入委员会反馈并加强了技术架构、生态影响与实施方案 [S04]。DAO 协调员 zz_tovarishch 提醒提案需要明确申请的具体预算金额 [S05]。

- **LS-IDL 获社区好评**：针对 CKB 锁脚本接口描述语言 LS-IDL，有用户回复 “This is fire”，表示高度认可 [S06]。

- **Tranfr 可编程恢复的边界讨论**：tianji 继续讨论 Tranfr 提案中第二个边界条件，即普通所有者支出必须在到期前提交确切效果，并列举了提案中的相关要求 [S08]。

## 值得继续跟进

- Fiber 主网 UDT 列表是否会因 USDI 停产而调整，以及 CCH swaps 的官方回应，值得关注 [S01]。
- Corven 提案目前还缺少明确的预算数字，后续更新中如何补齐并得到 DAO 审核，需要观察 [S05, S04]。
- CS 移植到 Fiber 目前只是 testnet 原型，后续是否会公开试玩、开源或进入主网验证，值得追踪 [S02]。

## 来源索引

- `S01` [UDT For Fiber Mainnet](https://talk.nervos.org/t/udt-for-fiber-mainnet/10649/1) | ebubedev | 2026-08-20 20:29:47 CST | i have some question if USDI has been discontinued on CKB, why does fiber still have it as a mainnet udt? What is mainnet udt for fiber cch swaps?
- `S02` [Porting Couter Strike to Fiber network](https://talk.nervos.org/t/porting-couter-strike-to-fiber-network/10647/1) | RetricSu | 2026-08-20 11:19:24 CST | 最近我在尝试移植一个简单的 1v1 射击游戏(霓虹地图版的 counter-strike)，不同的地方在于：每次命中造成的伤害，都通过 Fiber 支付通道去做真实的结算。 匹配前双方需要开通好 fiber 的通道 匹配好之后，双方各创建 4 张 hold 发票(带 SHA-256 哈希) 通过我的服务器判定谁命中，然后释放对应 preimage 输家为每一发命中真实付费给赢家 玩家无法拒绝为自己吃到的伤害付钱 服务器 64 tick/秒，伤害只由服务器裁决。目前跑在 testnet 上。...
- `S03` [Porting Couter Strike to Fiber network](https://talk.nervos.org/t/porting-couter-strike-to-fiber-network/10647/2) | knmo | 2026-08-20 18:37:52 CST | Overwhelming. For me, CS started out as a Half-Life mod, and at some point, waypoint files for bots became available, which gradually got better and better. Here, the future—in the form of NervosNetwork Fiber—meets a video game that has made history. It’s certainly one of the...
- `S04` [[DIS] Corven — Cloud Development Infrastructure for the CKB Ecosystem](https://talk.nervos.org/t/dis-corven-cloud-development-infrastructure-for-the-ckb-ecosystem/10648/1) | lestonEth | 2026-08-20 15:06:24 CST | Proposal Update: This submission builds on the initial proposal, incorporating committee feedback and strengthening the technical architecture, ecosystem impact, and implementation approach Category: CKB Community Fund DAO Project: Corven Applicant: Jimleston Osoi Role:...
- `S05` [[DIS] Corven — Cloud Development Infrastructure for the CKB Ecosystem](https://talk.nervos.org/t/dis-corven-cloud-development-infrastructure-for-the-ckb-ecosystem/10648/2) | zz_tovarishch | 2026-08-20 17:46:56 CST | Hi @lestonEth As the DAO coordinator, I’d like to gently remind you to clarify the exact budget being requested in your proposal. Best,
- `S06` [LS-IDL: a Lock Script Interface Description Language for CKB (derive, validate, commit)](https://talk.nervos.org/t/ls-idl-a-lock-script-interface-description-language-for-ckb-derive-validate-commit/10596/4) | truthixify | 2026-08-20 13:59:51 CST | This is fire
- `S07` [Spark Program | Corven — Cloud Development Platform for the CKB Ecosystem](https://talk.nervos.org/t/spark-program-corven-cloud-development-platform-for-the-ckb-ecosystem/10528/7) | lestonEth | 2026-08-20 03:15:24 CST | Hi @xingtianchunyan Thank you for the committee’s feedback and response. I understand and respect the committee’s decision, and I’m happy to comply with the recommended direction. I will move the broader Corven project proposal to the CKB Community Fund DAO. I appreciate the...
- `S08` [Tranfr — Programmable Recovery for CKB](https://talk.nervos.org/t/tranfr-programmable-recovery-for-ckb/10644/6) | tianji | 2026-08-20 02:27:33 CST | Second boundary: ordinary owner spending must commit the exact effect before expiry The remaining owner-side boundary is ordinary spending. The proposal currently requires all three of the following: while active, the owner retains normal spending authority; an ordinary spend...

## 活跃话题

1. [UDT For Fiber Mainnet](https://talk.nervos.org/t/udt-for-fiber-mainnet/10649) | 1 条近窗帖子 | 最新活动 2026-08-20 20:29:47 CST
2. [Porting Couter Strike to Fiber network](https://talk.nervos.org/t/porting-couter-strike-to-fiber-network/10647) | 2 条近窗帖子 | 最新活动 2026-08-20 18:37:52 CST | tags: fiber, game
3. [[DIS] Corven — Cloud Development Infrastructure for the CKB Ecosystem](https://talk.nervos.org/t/dis-corven-cloud-development-infrastructure-for-the-ckb-ecosystem/10648) | 2 条近窗帖子 | 最新活动 2026-08-20 17:46:56 CST
4. [LS-IDL: a Lock Script Interface Description Language for CKB (derive, validate, commit)](https://talk.nervos.org/t/ls-idl-a-lock-script-interface-description-language-for-ckb-derive-validate-commit/10596) | 1 条近窗帖子 | 最新活动 2026-08-20 13:59:51 CST | tags: CKB
5. [Spark Program | Corven — Cloud Development Platform for the CKB Ecosystem](https://talk.nervos.org/t/spark-program-corven-cloud-development-platform-for-the-ckb-ecosystem/10528) | 1 条近窗帖子 | 最新活动 2026-08-20 03:15:24 CST | tags: CKB, Grant, Rejection, dapp
6. [Tranfr — Programmable Recovery for CKB](https://talk.nervos.org/t/tranfr-programmable-recovery-for-ckb/10644) | 1 条近窗帖子 | 最新活动 2026-08-20 02:27:33 CST

## 最近帖子摘录

- 2026-08-20 20:29:47 CST | ebubedev | [UDT For Fiber Mainnet](https://talk.nervos.org/t/udt-for-fiber-mainnet/10649/1) | i have some question if USDI has been discontinued on CKB, why does fiber still have it as a mainnet udt? What is mainnet udt for fiber cch swaps?
- 2026-08-20 18:37:52 CST | knmo | [Porting Couter Strike to Fiber network](https://talk.nervos.org/t/porting-couter-strike-to-fiber-network/10647/2) | Overwhelming. For me, CS started out as a Half-Life mod, and at some point, waypoint files for bots became available, which gradually got better and better. Here, the future—in...
- 2026-08-20 17:46:56 CST | zz_tovarishch | [[DIS] Corven — Cloud Development Infrastructure for the CKB Ecosystem](https://talk.nervos.org/t/dis-corven-cloud-development-infrastructure-for-the-ckb-ecosystem/10648/2) | Hi @lestonEth As the DAO coordinator, I’d like to gently remind you to clarify the exact budget being requested in your proposal. Best,
- 2026-08-20 15:06:24 CST | lestonEth | [[DIS] Corven — Cloud Development Infrastructure for the CKB Ecosystem](https://talk.nervos.org/t/dis-corven-cloud-development-infrastructure-for-the-ckb-ecosystem/10648/1) | Proposal Update: This submission builds on the initial proposal, incorporating committee feedback and strengthening the technical architecture, ecosystem impact, and...
- 2026-08-20 13:59:51 CST | truthixify | [LS-IDL: a Lock Script Interface Description Language for CKB (derive, validate, commit)](https://talk.nervos.org/t/ls-idl-a-lock-script-interface-description-language-for-ckb-derive-validate-commit/10596/4) | This is fire
- 2026-08-20 11:19:24 CST | RetricSu | [Porting Couter Strike to Fiber network](https://talk.nervos.org/t/porting-couter-strike-to-fiber-network/10647/1) | 最近我在尝试移植一个简单的 1v1 射击游戏(霓虹地图版的 counter-strike)，不同的地方在于：每次命中造成的伤害，都通过 Fiber 支付通道去做真实的结算。 匹配前双方需要开通好 fiber 的通道 匹配好之后，双方各创建 4 张 hold 发票(带 SHA-256 哈希) 通过我的服务器判定谁命中，然后释放对应 preimage...
- 2026-08-20 03:15:24 CST | lestonEth | [Spark Program | Corven — Cloud Development Platform for the CKB Ecosystem](https://talk.nervos.org/t/spark-program-corven-cloud-development-platform-for-the-ckb-ecosystem/10528/7) | Hi @xingtianchunyan Thank you for the committee’s feedback and response. I understand and respect the committee’s decision, and I’m happy to comply with the recommended...
- 2026-08-20 02:27:33 CST | tianji | [Tranfr — Programmable Recovery for CKB](https://talk.nervos.org/t/tranfr-programmable-recovery-for-ckb/10644/6) | Second boundary: ordinary owner spending must commit the exact effect before expiry The remaining owner-side boundary is ordinary spending. The proposal currently requires all...
