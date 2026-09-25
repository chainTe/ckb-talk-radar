# Nervos Talk 社区简报

- 统计窗口: 2026-09-25 04:14:27 CST 到 2026-09-26 04:14:27 CST
- 生成时间: 2026-09-26 04:14:36 CST
- 话题数: 7
- 帖子数: 9
- 作者数: 6
- 总结模式: ai:openai-compatible

## 社区总结

## 今日发生了什么

今天 Nervos Talk 最近 24 小时的讨论主要围绕 CKB 节点收入层、Fiber 生态 PoC 和多个 CKB 应用项目展开 [S02, S03, S04, S08, S05, S06]。节点收入层帖子继续追问运行全节点的动机与真实激励 [S02, S03, S04]。Twine 更新了 Fiber P2P PoC 的争议解决功能，Cellula.id 和 SkillPass 也有新回复 [S08, S05, S06]。另外，Fiber L402 paywall 和 Nervape Email Wallet 出现了支持与开源相关提问 [S01, S07]。

## 重点话题

- CKB 节点收入层：psawyerberlin 认为此前“probably yes”判断过快，关键问题是服务收入能否真的带来更多全节点，并指出存储或 webhooks 可以跑在别人的 RPC 上 [S02]。joshyates1980 表示自己五年来自愿运行两个全节点，但一直思考 24/7 全节点有多重要 [S03]。psawyerberlin 回应自己也多年运行两台矿机加主网和测试网节点来支持项目，并指出“signature of acknowledgment”的难点是证明它来自实时同步的全节点 [S04]。
- Twine Fiber P2P PoC：更新称争议解决现已内建到应用（PoC）[S08]。此前设计是协调员审查聊天记录和上传收据，然后决定揭示 preimage 把 CKB 结算给买家，或让 HTLC 过期 [S08]。
- Cellula.id：LusoCryptoLabs 表示相关 watcher 已公开且为 MIT 许可，位于 cells-resolver/src/lockwatch.ts [S05]。他还感谢 Jan 迅速把 .cell 加入 ckbadger [S05]。
- SkillPass：Dangbaty2004 澄清转移仍通过普通 CKB 交易完成，SkillPass 不试图绕过 Cell 转移 [S06]。服务权由 live Cell 代表，Alice 转给 Bob 时旧 Cell 会被消耗 [S06]。
- 其他项目互动：在 Nervape Email Wallet 下，ckbytedance 问是否准备开源 [S07]。在 Spark Program 的 CRT 帖子中，psawyerberlin 回复 Spark Committee，提到第二次 Pending，并计划回答三点、提议申请后续处理 [S09]。在 Fiber L402 paywall 帖子中，有人询问 RetricSu 是否获得足够支持让项目继续开发 [S01]。

## 值得继续跟进

- CKB 节点收入层的核心验证：服务收入是否真能激励更多全节点，以及如何证明节点是实时同步的全节点 [S02, S04]。
- Twine 争议解决 PoC 的后续效果；材料只说明功能已内建，没有给出测试或运行结果 [S08]。
- Spark Program CRT 申请的下一步：该回复提到第二次 Pending，并准备回应三点与提议申请处理方式 [S09]。

## 来源索引

- `S01` [It is 2026 and let's run a blog with paywall built on top of fiber l402](https://talk.nervos.org/t/it-is-2026-and-lets-run-a-blog-with-paywall-built-on-top-of-fiber-l402/10140/3) | joshyates1980 | 2026-09-26 02:21:47 CST | @RetricSu did you get enough support to keep this project in development?
- `S02` [A Revenue Layer for CKB Nodes](https://talk.nervos.org/t/a-revenue-layer-for-ckb-nodes/10734/4) | psawyerberlin | 2026-09-25 05:30:28 CST | A second thought on the first question above, whether service income actually brings more full nodes. My “probably yes” was too quick; it’s the real crux. Storage or webhooks can run on any server using someone else’s RPC. So a revenue layer only strengthens CKB if it pays for...
- `S03` [A Revenue Layer for CKB Nodes](https://talk.nervos.org/t/a-revenue-layer-for-ckb-nodes/10734/5) | joshyates1980 | 2026-09-25 21:10:38 CST | I have ran two full nodes out of love for Nervos over the past five years but always wondered about the importance from a different perspective just “how important it is for us to run our 24/7 full nodes.” I primarily run the full nodes as a way to support Nervos, to have the...
- `S04` [A Revenue Layer for CKB Nodes](https://talk.nervos.org/t/a-revenue-layer-for-ckb-nodes/10734/6) | psawyerberlin | 2026-09-26 01:30:15 CST | @joshyates1980 Same here: I’ve been running two miners plus a mainnet and a testnet node for years to support the project. That’s what “RUN CKB” is about. images400×400 12.6 KB Your “signature of acknowledgment” touches the hard part: proving it comes from a live, synced full...
- `S05` [Cellula.id: `.cell` names on CKB, with the contracts public and reproducible](https://talk.nervos.org/t/cellula-id-cell-names-on-ckb-with-the-contracts-public-and-reproducible/10753/5) | LusoCryptoLabs | 2026-09-26 00:46:19 CST | Thanks, Jan. The watcher behind that decision is public, MIT, in cells-resolver/src/lockwatch.ts, for anyone who wants to watch a type id the same way. And thank you for adding .cell to ckbadger so quickly. Cheers.
- `S06` [SkillPass: Portable Service Rights on CKB — Looking for Community Feedback](https://talk.nervos.org/t/skillpass-portable-service-rights-on-ckb-looking-for-community-feedback/10706/10) | Dangbaty2004 | 2026-09-25 14:05:48 CST | Yes, exactly — the transfer still happens through a normal CKB transaction. SkillPass is not trying to avoid the Cell transfer. The idea is that the service right is represented by that live Cell, so when Alice transfers it to Bob, the old Cell is consumed and Bob receives the...
- `S07` [Nervape Email Wallet](https://talk.nervos.org/t/nervape-email-wallet/10742/2) | ckbytedance | 2026-09-25 11:51:10 CST | 准备开源吗？
- `S08` [Twine: Buy and Sell CKB Without Depositing on an Exchange (Fiber P2P PoC)](https://talk.nervos.org/t/twine-buy-and-sell-ckb-without-depositing-on-an-exchange-fiber-p2p-poc/10741/2) | ebubedev | 2026-09-25 09:50:01 CST | Update: Dispute resolution is now built into the app (PoC) In my previous post, I outlined the concept behind handling disputes: the coordinator reviews the chat logs and uploaded receipt, then either reveals the preimage to settle CKB to the buyer or lets the HTLC expire so...
- `S09` [Spark Program | CKB Revocable Timelock (CRT) — Timelock Encryption You Can Cancel](https://talk.nervos.org/t/spark-program-ckb-revocable-timelock-crt-timelock-encryption-you-can-cancel/10698/5) | psawyerberlin | 2026-09-25 04:28:45 CST | Reply to Spark Committee — second Pending Thank you xingtian, and thanks to the committee for a genuinely careful second read. I want to answer the three points properly, and then make a proposal about what happens to this application. Before the details, one thing I should...

## 活跃话题

1. [It is 2026 and let's run a blog with paywall built on top of fiber l402](https://talk.nervos.org/t/it-is-2026-and-lets-run-a-blog-with-paywall-built-on-top-of-fiber-l402/10140) | 1 条近窗帖子 | 最新活动 2026-09-26 02:21:47 CST | tags: lang-en
2. [A Revenue Layer for CKB Nodes](https://talk.nervos.org/t/a-revenue-layer-for-ckb-nodes/10734) | 3 条近窗帖子 | 最新活动 2026-09-26 01:30:15 CST | tags: CKB, CKB-VM
3. [Cellula.id: `.cell` names on CKB, with the contracts public and reproducible](https://talk.nervos.org/t/cellula-id-cell-names-on-ckb-with-the-contracts-public-and-reproducible/10753) | 1 条近窗帖子 | 最新活动 2026-09-26 00:46:19 CST | tags: CKB, dapp
4. [SkillPass: Portable Service Rights on CKB — Looking for Community Feedback](https://talk.nervos.org/t/skillpass-portable-service-rights-on-ckb-looking-for-community-feedback/10706) | 1 条近窗帖子 | 最新活动 2026-09-25 14:05:48 CST | tags: CKB, dapp, fiber, testnet
5. [Nervape Email Wallet](https://talk.nervos.org/t/nervape-email-wallet/10742) | 1 条近窗帖子 | 最新活动 2026-09-25 11:51:10 CST | tags: CKB, lang-zh
6. [Twine: Buy and Sell CKB Without Depositing on an Exchange (Fiber P2P PoC)](https://talk.nervos.org/t/twine-buy-and-sell-ckb-without-depositing-on-an-exchange-fiber-p2p-poc/10741) | 1 条近窗帖子 | 最新活动 2026-09-25 09:50:01 CST | tags: fiber
7. [Spark Program | CKB Revocable Timelock (CRT) — Timelock Encryption You Can Cancel](https://talk.nervos.org/t/spark-program-ckb-revocable-timelock-crt-timelock-encryption-you-can-cancel/10698) | 1 条近窗帖子 | 最新活动 2026-09-25 04:28:45 CST | tags: Pending

## 最近帖子摘录

- 2026-09-26 02:21:47 CST | joshyates1980 | [It is 2026 and let's run a blog with paywall built on top of fiber l402](https://talk.nervos.org/t/it-is-2026-and-lets-run-a-blog-with-paywall-built-on-top-of-fiber-l402/10140/3) | @RetricSu did you get enough support to keep this project in development?
- 2026-09-26 01:30:15 CST | psawyerberlin | [A Revenue Layer for CKB Nodes](https://talk.nervos.org/t/a-revenue-layer-for-ckb-nodes/10734/6) | @joshyates1980 Same here: I’ve been running two miners plus a mainnet and a testnet node for years to support the project. That’s what “RUN CKB” is about. images400×400 12.6 KB...
- 2026-09-26 00:46:19 CST | LusoCryptoLabs | [Cellula.id: `.cell` names on CKB, with the contracts public and reproducible](https://talk.nervos.org/t/cellula-id-cell-names-on-ckb-with-the-contracts-public-and-reproducible/10753/5) | Thanks, Jan. The watcher behind that decision is public, MIT, in cells-resolver/src/lockwatch.ts, for anyone who wants to watch a type id the same way. And thank you for adding...
- 2026-09-25 21:10:38 CST | joshyates1980 | [A Revenue Layer for CKB Nodes](https://talk.nervos.org/t/a-revenue-layer-for-ckb-nodes/10734/5) | I have ran two full nodes out of love for Nervos over the past five years but always wondered about the importance from a different perspective just “how important it is for us...
- 2026-09-25 14:05:48 CST | Dangbaty2004 | [SkillPass: Portable Service Rights on CKB — Looking for Community Feedback](https://talk.nervos.org/t/skillpass-portable-service-rights-on-ckb-looking-for-community-feedback/10706/10) | Yes, exactly — the transfer still happens through a normal CKB transaction. SkillPass is not trying to avoid the Cell transfer. The idea is that the service right is represented...
- 2026-09-25 11:51:10 CST | ckbytedance | [Nervape Email Wallet](https://talk.nervos.org/t/nervape-email-wallet/10742/2) | 准备开源吗？
- 2026-09-25 09:50:01 CST | ebubedev | [Twine: Buy and Sell CKB Without Depositing on an Exchange (Fiber P2P PoC)](https://talk.nervos.org/t/twine-buy-and-sell-ckb-without-depositing-on-an-exchange-fiber-p2p-poc/10741/2) | Update: Dispute resolution is now built into the app (PoC) In my previous post, I outlined the concept behind handling disputes: the coordinator reviews the chat logs and...
- 2026-09-25 05:30:28 CST | psawyerberlin | [A Revenue Layer for CKB Nodes](https://talk.nervos.org/t/a-revenue-layer-for-ckb-nodes/10734/4) | A second thought on the first question above, whether service income actually brings more full nodes. My “probably yes” was too quick; it’s the real crux. Storage or webhooks...
- 2026-09-25 04:28:45 CST | psawyerberlin | [Spark Program | CKB Revocable Timelock (CRT) — Timelock Encryption You Can Cancel](https://talk.nervos.org/t/spark-program-ckb-revocable-timelock-crt-timelock-encryption-you-can-cancel/10698/5) | Reply to Spark Committee — second Pending Thank you xingtian, and thanks to the committee for a genuinely careful second read. I want to answer the three points properly, and...
