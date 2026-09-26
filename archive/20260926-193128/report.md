# Nervos Talk 社区简报

- 统计窗口: 2026-09-26 03:31:28 CST 到 2026-09-27 03:31:28 CST
- 生成时间: 2026-09-27 03:31:32 CST
- 话题数: 3
- 帖子数: 7
- 作者数: 6
- 总结模式: ai:openai-compatible

## 社区总结

## 今日发生了什么

过去约一天，Nervos Talk 的讨论主要集中在 Vellum 的 Milestone 1 交付、CKB 节点收入层的继续讨论，以及论坛账号权限处理上 [S01, S03, S06]。Vellum M1 已完成并部署到 CKB Testnet，社区成员表示认可并期待 M2 [S01, S02]。节点收入层帖子出现了视频摘要传播，但作者澄清还没有任何实际构建，讨论重点转向轻客户端服务是否应收费 [S03, S04, S05]。从这些材料看，今天社区整体较平静，更多是延续性讨论 [S01, S02, S03, S04, S05, S06, S07]。

## 重点话题

- Vellum Milestone 1 交付报告已完成并开放社区审查，M1 为 did:ckb 上的可移植声誉打基础，Claim Cell 合约部署在 CKB Testnet，@usevellum/sdk 已发布 [S01]。有社区成员称 M1 交付令人印象深刻，认为 Vellum 从设计进入经过测试的实时 Testnet 实现，并表示期待 M2 [S02]。
- “A Revenue Layer for CKB Nodes” 继续被讨论，有人用短视频在 X 上总结这个想法，作者感谢传播并澄清目前还没有任何东西被构建，帖子仍是想法成形的地方 [S03]。有用户提出服务轻客户端是必须依赖真实全节点的服务，运行在节点自身 p2p 协议上，不能由别人的 RPC 提供，且 CKB 节点已默认免费提供 [S04]。作者回应称这个例子很好，但提醒轻客户端依赖该服务，基本服务应保持免费，否则钱包可能出问题，收费只能作为可选附加 [S05]。
- CKB 生态双周更新帖中，新用户 Heizer 表示自己有担忧想直接向管理员提出，但因账号新还不能发私信，希望管理员联系 [S06]。管理员 zz_tovarishch 回复称已将其账号调整为 Basic Level，可以正常发帖，并提醒后续遵守论坛基本规则 [S07]。

## 值得继续跟进

- Vellum M1 的社区评审反馈，以及 M2 是否会按社区期待继续推进 [S01, S02]。
- 节点收入层是否会从想法进入实际构建，尤其是轻客户端这类基础服务保持免费、收费只作为可选附加的边界如何设计 [S03, S04, S05]。
- Heizer 想向管理员提出的具体担忧是什么，以及论坛新账号权限问题是否会影响新成员参与，后续是否会有公开说明 [S06, S07]。

## 来源索引

- `S01` [[DIS] Vellum: Reputation Extension on did:ckb](https://talk.nervos.org/t/dis-vellum-reputation-extension-on-did-ckb/10613/9) | truthixify | 2026-09-26 06:06:55 CST | Vellum Milestone 1 delivery report Implementation for Vellum’s first grant milestone is complete and ready for community review. M1 established the foundation for portable reputation on did:ckb: the Claim Cell contracts are deployed on CKB Testnet, @usevellum/sdk is published...
- `S02` [[DIS] Vellum: Reputation Extension on did:ckb](https://talk.nervos.org/t/dis-vellum-reputation-extension-on-did-ckb/10613/10) | Dangbaty2004 | 2026-09-26 19:20:16 CST | Really impressive M1 delivery. Great to see Vellum moving from design into a well-tested, live Testnet implementation. Congrats — looking forward to M2!
- `S03` [A Revenue Layer for CKB Nodes](https://talk.nervos.org/t/a-revenue-layer-for-ckb-nodes/10734/7) | psawyerberlin | 2026-09-26 06:18:03 CST | For those who prefer video: RyptoCrypto made a short summary of this idea on X https://x.com/RyptoCrypto/status/2103525842986864653?s=20 Thanks to him for spreading it. One clarification: nothing is built yet. This thread is still the place where the idea is being shaped.
- `S04` [A Revenue Layer for CKB Nodes](https://talk.nervos.org/t/a-revenue-layer-for-ckb-nodes/10734/8) | LusoCryptoLabs | 2026-09-26 07:23:10 CST | My two cents, one service that needs the node itself is serving light clients. It runs over the node’s own p2p protocol, so it cannot be served from someone else’s RPC, and CKB nodes already do it for free, since light client support is on by default. Wallets that embed a...
- `S05` [A Revenue Layer for CKB Nodes](https://talk.nervos.org/t/a-revenue-layer-for-ckb-nodes/10734/9) | psawyerberlin | 2026-09-26 17:42:05 CST | Thanks, a good example of a service that only a real, synced full node can provide, and every node already runs it. But I’d be careful: light clients depend on it, so the basic service should stay free, or wallets break. A fee could only work as an optional extra on top, e.g....
- `S06` [CKB Ecosystem Biweekly Update](https://talk.nervos.org/t/ckb-ecosystem-biweekly-update/9821/30) | Heizer | 2026-09-26 15:37:24 CST | Hi @zz_tovarishch I have concern that I would like to raise to the admins directly. My account is new so I can’t sent DMs yet. Could someone from the admin team reach out to me? Thanks
- `S07` [CKB Ecosystem Biweekly Update](https://talk.nervos.org/t/ckb-ecosystem-biweekly-update/9821/31) | zz_tovarishch | 2026-09-26 15:41:10 CST | 你好，已经将您的账号调整为Basic Level, 可以正常发帖了 后续请遵守论坛的基本规则，期待您与社区的更多交流，祝玩得愉快

## 活跃话题

1. [[DIS] Vellum: Reputation Extension on did:ckb](https://talk.nervos.org/t/dis-vellum-reputation-extension-on-did-ckb/10613) | 2 条近窗帖子 | 最新活动 2026-09-26 19:20:16 CST
2. [A Revenue Layer for CKB Nodes](https://talk.nervos.org/t/a-revenue-layer-for-ckb-nodes/10734) | 3 条近窗帖子 | 最新活动 2026-09-26 17:42:05 CST | tags: CKB, CKB-VM
3. [CKB Ecosystem Biweekly Update](https://talk.nervos.org/t/ckb-ecosystem-biweekly-update/9821) | 2 条近窗帖子 | 最新活动 2026-09-26 15:41:10 CST | tags: Ecosystem-Update, lang-en

## 最近帖子摘录

- 2026-09-26 19:20:16 CST | Dangbaty2004 | [[DIS] Vellum: Reputation Extension on did:ckb](https://talk.nervos.org/t/dis-vellum-reputation-extension-on-did-ckb/10613/10) | Really impressive M1 delivery. Great to see Vellum moving from design into a well-tested, live Testnet implementation. Congrats — looking forward to M2!
- 2026-09-26 17:42:05 CST | psawyerberlin | [A Revenue Layer for CKB Nodes](https://talk.nervos.org/t/a-revenue-layer-for-ckb-nodes/10734/9) | Thanks, a good example of a service that only a real, synced full node can provide, and every node already runs it. But I’d be careful: light clients depend on it, so the basic...
- 2026-09-26 15:41:10 CST | zz_tovarishch | [CKB Ecosystem Biweekly Update](https://talk.nervos.org/t/ckb-ecosystem-biweekly-update/9821/31) | 你好，已经将您的账号调整为Basic Level, 可以正常发帖了 后续请遵守论坛的基本规则，期待您与社区的更多交流，祝玩得愉快
- 2026-09-26 15:37:24 CST | Heizer | [CKB Ecosystem Biweekly Update](https://talk.nervos.org/t/ckb-ecosystem-biweekly-update/9821/30) | Hi @zz_tovarishch I have concern that I would like to raise to the admins directly. My account is new so I can’t sent DMs yet. Could someone from the admin team reach out to me?...
- 2026-09-26 07:23:10 CST | LusoCryptoLabs | [A Revenue Layer for CKB Nodes](https://talk.nervos.org/t/a-revenue-layer-for-ckb-nodes/10734/8) | My two cents, one service that needs the node itself is serving light clients. It runs over the node’s own p2p protocol, so it cannot be served from someone else’s RPC, and CKB...
- 2026-09-26 06:18:03 CST | psawyerberlin | [A Revenue Layer for CKB Nodes](https://talk.nervos.org/t/a-revenue-layer-for-ckb-nodes/10734/7) | For those who prefer video: RyptoCrypto made a short summary of this idea on X https://x.com/RyptoCrypto/status/2103525842986864653?s=20 Thanks to him for spreading it. One...
- 2026-09-26 06:06:55 CST | truthixify | [[DIS] Vellum: Reputation Extension on did:ckb](https://talk.nervos.org/t/dis-vellum-reputation-extension-on-did-ckb/10613/9) | Vellum Milestone 1 delivery report Implementation for Vellum’s first grant milestone is complete and ready for community review. M1 established the foundation for portable...
