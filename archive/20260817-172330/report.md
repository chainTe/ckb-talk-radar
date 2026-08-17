# Nervos Talk 社区简报

- 统计窗口: 2026-08-17 01:23:30 CST 到 2026-08-18 01:23:30 CST
- 生成时间: 2026-08-18 01:23:49 CST
- 话题数: 7
- 帖子数: 10
- 作者数: 8
- 总结模式: ai:openai-compatible

## 社区总结

## 今日发生了什么

Nervos Talk 今天整体不算热闹，主要是几个 Spark 项目的常规进展更新，以及一条投票提醒 [S01, S03, S04, S05, S06, S07, S08]。最显眼的是 Pocket Node for iOS 的社区投票进入最后 3 天，项目方呼吁支持者抓紧投票 [S01]。此外，关于 CKB-VM 的 Sail Validation Sprint 里出现了一轮围绕 JoyID 登录问题的技术排查对话 [S03, S04, S05]，Corven 提案作者也回应了社区对其方案的质疑 [S07, S08]。

## 重点话题

- **Pocket Node 投票倒计时**：Pocket Node 团队提醒社区，Metaforo 上的投票还剩 3 天，希望大家为这个自托管 CKB iOS 轻客户端项目投票支持 [S01]。

- **JoyID 通行密钥登录问题排查**：在 Sail Validation Sprint 讨论中，有用户反馈无法撤销设备对通行密钥的访问权限，并询问 JoyID 密钥是否能通过 Google 密码管理器同步 [S03, S04]。项目方回复说，取消授权后自然无法访问 Google 密码管理器获取 passkey，并建议用户到 JoyID 的 Discord 开 ticket 跟踪该问题 [S05]。

- **Corven 提案作者回应质疑**：针对社区成员 zz_tovarishch 提出的基础设施成本和提案范围过大的担忧，Corven 作者表示已理解这些顾虑，并称自提交提案以来一直在继续开发和完善该项目 [S07, S08]。

- **Dular 项目本周收尾**：Spark 项目 Dular 的负责人表示本周正在逐步结束工作，整体进展顺利 [S06]。

- **一篇关于微支付的文章**：用户 abel 发帖讨论了微支付场景中“按秒计费”背后隐藏的问题，起因是 CKBA 在 LinkedIn 上关于订阅制存在理由的观点 [S10]。

## 值得继续跟进

- **Pocket Node 投票结果**：投票还剩 3 天，最终能否通过、以及社区支持度如何，值得关注 [S01]。

- **JoyID 通行密钥问题**：目前只是建议去 Discord 开 ticket，问题是否真正解决还有待观察 [S05]。

- **Corven 提案的后续修改**：作者表示会继续完善项目，但尚未给出具体的方案调整细节，可以留意后续更新 [S07, S08]。

## 来源索引

- `S01` [[DIS] Pocket Node for iOS: a self-custody CKB light client for Apple and Identity/Signer for CCC web apps](https://talk.nervos.org/t/dis-pocket-node-for-ios-a-self-custody-ckb-light-client-for-apple-and-identity-signer-for-ccc-web-apps/10583/17) | Jnr6 | 2026-08-17 21:36:49 CST | Hi everyone we have 3 days left to vote on Metaforo. don’t forget to show your support for pocket node. https://dao.ckb.community/thread/vot-pocket-node-for-ios-a-self-custody-ckb-light-client-for-apple-and-identity-signer-for-ccc-web-apps-76502
- `S02` [Questions about CKBA](https://talk.nervos.org/t/questions-about-ckba/10471/30) | matt_ckb | 2026-08-17 21:10:30 CST | AryaStark: who is responsible for turning those three priorities into actual budgets, milestones, and deliverables—the Operations Director or the Board? budget is proposed by the board and voted on by the GA. There are not milestones and deliverables, team leads organize 2...
- `S03` [Spark Program | CKB-VM Sail Validation Sprint：可复现的 RISC-V 语义差分工具、Lean 4 证明与 Rocq/Coq 兼容性 Spike](https://talk.nervos.org/t/spark-program-ckb-vm-sail-validation-sprint-risc-v-lean-4-rocq-coq-spike/10562/10) | mfuuzy | 2026-08-17 09:19:34 CST | 我看你截图有4登录账户，你是哪一个用不了？最下面的两个是google passkey ，不能在浏览器设置 “撤销此设备对通行密钥的访问权限”
- `S04` [Spark Program | CKB-VM Sail Validation Sprint：可复现的 RISC-V 语义差分工具、Lean 4 证明与 Rocq/Coq 兼容性 Spike](https://talk.nervos.org/t/spark-program-ckb-vm-sail-validation-sprint-risc-v-lean-4-rocq-coq-spike/10562/11) | TinyuengKwan | 2026-08-17 20:11:00 CST | 我登陆的是第三个账户;为什么不能撤销此设备对通行密钥的访问权限? joyid的密钥不是保存在google密码管理器里的吗,不能自动同步吗?
- `S05` [Spark Program | CKB-VM Sail Validation Sprint：可复现的 RISC-V 语义差分工具、Lean 4 证明与 Rocq/Coq 兼容性 Spike](https://talk.nervos.org/t/spark-program-ckb-vm-sail-validation-sprint-risc-v-lean-4-rocq-coq-spike/10562/12) | mfuuzy | 2026-08-17 20:33:20 CST | 就是需要有权限读取，你才能访问google密码管理器，获取 passkey 登录Joyid，你取消授权了，不就没权限了吗 你到 Joyid 的 Discord 开一个 ticket，我们追踪一下这个问题，参考下图这里，进去创建就行 image295×214 9.68 KB
- `S06` [Spark Program | Dular](https://talk.nervos.org/t/spark-program-dular/10212/32) | duongja | 2026-08-17 17:31:02 CST | We are winding down this week, all good
- `S07` [Spark Program | Corven — Cloud Development Platform for the CKB Ecosystem](https://talk.nervos.org/t/spark-program-corven-cloud-development-platform-for-the-ckb-ecosystem/10528/4) | lestonEth | 2026-08-17 14:14:13 CST | Hi zz_tovarishch Thank you for the feedback and for taking the time to review the Corven proposal. I understand the concerns around infrastructure costs and the scope of the initial proposal. Since submitting it, I have continued developing Corven and have been refining the...
- `S08` [Spark Program | Corven — Cloud Development Platform for the CKB Ecosystem](https://talk.nervos.org/t/spark-program-corven-cloud-development-platform-for-the-ckb-ecosystem/10528/5) | lestonEth | 2026-08-17 15:00:05 CST | lestonEth: Hi zz_tovarishch Thank you for the feedback and for taking the time to review the Corven proposal. I understand the concerns around infrastructure costs and the scope of the initial proposal. Since submitting it, I have continued developing Corven and have been...
- `S09` [Tapeout base on ckb](https://talk.nervos.org/t/tapeout-base-on-ckb/10632/1) | ckbbkc | 2026-08-17 07:07:57 CST | (topic deleted by author)
- `S10` [Pay By The Second, Watched By The Second: The Problem Hiding Inside Micropayments](https://talk.nervos.org/t/pay-by-the-second-watched-by-the-second-the-problem-hiding-inside-micropayments/10631/1) | abel | 2026-08-17 03:25:37 CST | IMG_98801600×900 106 KB A few weeks ago I came across a post from CKBA on LinkedIn about micropayments. The argument was that subscriptions exist mostly because charging tiny amounts continuously has never been practical, and that once you fix that, you can sell things that...

## 活跃话题

1. [[DIS] Pocket Node for iOS: a self-custody CKB light client for Apple and Identity/Signer for CCC web apps](https://talk.nervos.org/t/dis-pocket-node-for-ios-a-self-custody-ckb-light-client-for-apple-and-identity-signer-for-ccc-web-apps/10583) | 1 条近窗帖子 | 最新活动 2026-08-17 21:36:49 CST | tags: Pocket-Node, light-client
2. [Questions about CKBA](https://talk.nervos.org/t/questions-about-ckba/10471) | 1 条近窗帖子 | 最新活动 2026-08-17 21:10:30 CST | tags: lang-en
3. [Spark Program | CKB-VM Sail Validation Sprint：可复现的 RISC-V 语义差分工具、Lean 4 证明与 Rocq/Coq 兼容性 Spike](https://talk.nervos.org/t/spark-program-ckb-vm-sail-validation-sprint-risc-v-lean-4-rocq-coq-spike/10562) | 3 条近窗帖子 | 最新活动 2026-08-17 20:33:20 CST | tags: CKB-VM, In-Progress
4. [Spark Program | Dular](https://talk.nervos.org/t/spark-program-dular/10212) | 1 条近窗帖子 | 最新活动 2026-08-17 17:31:02 CST | tags: In-Progress, Spark-Program, lang-en
5. [Spark Program | Corven — Cloud Development Platform for the CKB Ecosystem](https://talk.nervos.org/t/spark-program-corven-cloud-development-platform-for-the-ckb-ecosystem/10528) | 2 条近窗帖子 | 最新活动 2026-08-17 15:00:05 CST | tags: Rejection
6. [Tapeout base on ckb](https://talk.nervos.org/t/tapeout-base-on-ckb/10632) | 1 条近窗帖子 | 最新活动 2026-08-17 07:07:57 CST
7. [Pay By The Second, Watched By The Second: The Problem Hiding Inside Micropayments](https://talk.nervos.org/t/pay-by-the-second-watched-by-the-second-the-problem-hiding-inside-micropayments/10631) | 1 条近窗帖子 | 最新活动 2026-08-17 03:25:37 CST | tags: fiber

## 最近帖子摘录

- 2026-08-17 21:36:49 CST | Jnr6 | [[DIS] Pocket Node for iOS: a self-custody CKB light client for Apple and Identity/Signer for CCC web apps](https://talk.nervos.org/t/dis-pocket-node-for-ios-a-self-custody-ckb-light-client-for-apple-and-identity-signer-for-ccc-web-apps/10583/17) | Hi everyone we have 3 days left to vote on Metaforo. don’t forget to show your support for pocket node. https://dao.ckb.community/thread/vot-pocket-node-for-ios-a-self-custody-...
- 2026-08-17 21:10:30 CST | matt_ckb | [Questions about CKBA](https://talk.nervos.org/t/questions-about-ckba/10471/30) | AryaStark: who is responsible for turning those three priorities into actual budgets, milestones, and deliverables—the Operations Director or the Board? budget is proposed by...
- 2026-08-17 20:33:20 CST | mfuuzy | [Spark Program | CKB-VM Sail Validation Sprint：可复现的 RISC-V 语义差分工具、Lean 4 证明与 Rocq/Coq 兼容性 Spike](https://talk.nervos.org/t/spark-program-ckb-vm-sail-validation-sprint-risc-v-lean-4-rocq-coq-spike/10562/12) | 就是需要有权限读取，你才能访问google密码管理器，获取 passkey 登录Joyid，你取消授权了，不就没权限了吗 你到 Joyid 的 Discord 开一个 ticket，我们追踪一下这个问题，参考下图这里，进去创建就行 image295×214 9.68 KB
- 2026-08-17 20:11:00 CST | TinyuengKwan | [Spark Program | CKB-VM Sail Validation Sprint：可复现的 RISC-V 语义差分工具、Lean 4 证明与 Rocq/Coq 兼容性 Spike](https://talk.nervos.org/t/spark-program-ckb-vm-sail-validation-sprint-risc-v-lean-4-rocq-coq-spike/10562/11) | 我登陆的是第三个账户;为什么不能撤销此设备对通行密钥的访问权限? joyid的密钥不是保存在google密码管理器里的吗,不能自动同步吗?
- 2026-08-17 17:31:02 CST | duongja | [Spark Program | Dular](https://talk.nervos.org/t/spark-program-dular/10212/32) | We are winding down this week, all good
- 2026-08-17 15:00:05 CST | lestonEth | [Spark Program | Corven — Cloud Development Platform for the CKB Ecosystem](https://talk.nervos.org/t/spark-program-corven-cloud-development-platform-for-the-ckb-ecosystem/10528/5) | lestonEth: Hi zz_tovarishch Thank you for the feedback and for taking the time to review the Corven proposal. I understand the concerns around infrastructure costs and the scope...
- 2026-08-17 14:14:13 CST | lestonEth | [Spark Program | Corven — Cloud Development Platform for the CKB Ecosystem](https://talk.nervos.org/t/spark-program-corven-cloud-development-platform-for-the-ckb-ecosystem/10528/4) | Hi zz_tovarishch Thank you for the feedback and for taking the time to review the Corven proposal. I understand the concerns around infrastructure costs and the scope of the...
- 2026-08-17 09:19:34 CST | mfuuzy | [Spark Program | CKB-VM Sail Validation Sprint：可复现的 RISC-V 语义差分工具、Lean 4 证明与 Rocq/Coq 兼容性 Spike](https://talk.nervos.org/t/spark-program-ckb-vm-sail-validation-sprint-risc-v-lean-4-rocq-coq-spike/10562/10) | 我看你截图有4登录账户，你是哪一个用不了？最下面的两个是google passkey ，不能在浏览器设置 “撤销此设备对通行密钥的访问权限”
- 2026-08-17 07:07:57 CST | ckbbkc | [Tapeout base on ckb](https://talk.nervos.org/t/tapeout-base-on-ckb/10632/1) | (topic deleted by author)
- 2026-08-17 03:25:37 CST | abel | [Pay By The Second, Watched By The Second: The Problem Hiding Inside Micropayments](https://talk.nervos.org/t/pay-by-the-second-watched-by-the-second-the-problem-hiding-inside-micropayments/10631/1) | IMG_98801600×900 106 KB A few weeks ago I came across a post from CKBA on LinkedIn about micropayments. The argument was that subscriptions exist mostly because charging tiny...
