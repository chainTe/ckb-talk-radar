# Nervos Talk 社区简报

- 统计窗口: 2026-11-21 06:00:14 CST 到 2026-11-22 06:00:14 CST
- 生成时间: 2026-11-22 06:00:21 CST
- 话题数: 8
- 帖子数: 25
- 作者数: 14
- 总结模式: ai:openai-compatible

## 社区总结

## 今日发生了什么

今天论坛最直接的进展是 Vellum 与 Rivet 在帖中对接 Testnet 集成意向 [S01, S02]，同时 Rivet 宣布第二个 grant milestone 的 CKB Testnet 实现与验收测试完成 [S05]。治理方面，DAO 提案公平性讨论继续围绕某桥的社区基金拨款、投票结果和是否启动展开 [S10, S12, S14, S15]。技术讨论中，Lock Proof RFC 澄清“支持所有 lock”的实现思路并补充 Rust crate [S07, S08, S09]，KeyMe 则收到关于 PSCT v0 多签交易和自定义脚本验证的提问 [S06]。其他更新包括 FiberNuts 初始资金已确认到账 [S16, S17]，Productathon 帖收到支持性回复 [S04]，以及用户名修改请求由 Mod 处理完成 [S18, S19, S20]。

## 重点话题

- **Vellum × Rivet 集成意向**：Jedi_dtechmaker 提出将 Vellum 接入 Rivet，让开发者绑定 did:ckb 并在 Rivet passport 旁展示已验证声明，询问 SDK/API 是否支持及是否可做小规模 Testnet 集成 [S01]；truthixify 回复同意并约 Telegram 私聊细节 [S02]。同帖中 Ayoub_Lesfer 表示 v1 只说明活动达标并完成总额，愿意按现状开启并把判断留给读者，其索引器已从收据历史重建支持者 [S03]。
- **Rivet M2 交付完成**：Rivet 第二个 grant milestone 的 CKB Testnet 实现和项目验收测试已完成，交付已发布的跨平台 CLI、独立 Exact Restore 等 [S05]。
- **KeyMe 收到 PSCT v0 关键问题**：ArthurZhang 问 combine() 只合并同一交易的签名时如何支持真正的多参与方交易构建，以及能否用可扩展方式验证自定义脚本语义和签名 [S06]。
- **Lock Proof RFC 澄清“所有 lock”边界**：讨论者询问后端需要接受哪些 lock，并认为钱包绑定场景最好支持所有 lock [S07]；作者回应称就是为所有 lock 构建，验证器在 CKB-VM 中运行 lock 本身，一条代码路径覆盖所有签署交易哈希的 lock，唯一 lock-specific 检查会拒绝 Omnilock 管理员模式 [S08]；作者还补充 Rust crate 位于 ckb-ward 的 rust/，覆盖 npm 包后端侧的消息、钱包模板、verify 和 DAO snapshot helpers [S09]。
- **DAO 提案公平性争论延续**：phroi 表示相关集成是暂停而非放弃，并称 15k 里程碑以 CKB 支付、为 6,313,131 CKB（按当前价格约 5k 美元），社区投票中 64% 权重赞成 [S10, S12]。hao_zhang 让 phroi 回顾对话并看桥的最终结果 [S13]；phroi 则让反对者看投票者名单，并反问是否应照常启动、把用户资金置于风险中 [S14]；asondev 强调质疑社区基金运作本身就是参与治理，相关问题应可在论坛提出 [S15]。

## 值得继续跟进

- **Vellum × Rivet 的 Testnet 集成能否落地**：双方已同意私聊细节，后续可观察是否出现公开的 SDK/API 对接说明或测试网集成结果 [S01, S02]。
- **DAO 拨款争议对桥项目启动的影响**：讨论中一方称集成暂停而非放弃，另一方持续追问是否照常启动及用户资金风险，后续需看项目方是否给出明确上线或暂停决定 [S10, S14]。
- **Lock Proof 的“全 lock”支持边界**：作者称验证器可覆盖所有签署交易哈希的 lock，但会拒绝 Omnilock 管理员模式，后续可关注该限制及 Rust crate 的实际测试情况 [S08, S09]。

## 来源索引

- `S01` [[DIS] Vellum: Reputation Extension on did:ckb](https://talk.nervos.org/t/dis-vellum-reputation-extension-on-did-ckb/10613/25) | Jedi_dtechmaker | 2026-11-21 12:33:36 CST | Hi @truthixify , I’m thinking of integrating Vellum into Rivet. Developers could link their did:ckb and display their verified claims alongside their Rivet passport. Does your current SDK/API support this, and would you be open to a small Testnet integration?
- `S02` [[DIS] Vellum: Reputation Extension on did:ckb](https://talk.nervos.org/t/dis-vellum-reputation-extension-on-did-ckb/10613/26) | truthixify | 2026-11-21 12:48:23 CST | Yes! Let’s do this. Send me a DM on telegram so we can discuss the details.
- `S03` [[DIS] Vellum: Reputation Extension on did:ckb](https://talk.nervos.org/t/dis-vellum-reputation-extension-on-did-ckb/10613/27) | Ayoub_Lesfer | 2026-11-22 03:15:23 CST | Makes sense, thanks. Since v1 only says the campaign hit its goal and finalized, with the total, I’m fine turning it on as is and leaving the judgement to whoever reads the claim. Our indexer already rebuilds backers from the receipt history, so distinct backer count and how...
- `S04` [[DIS] CKB Productathon: Ship on CKB (Kisumu, Kenya)](https://talk.nervos.org/t/dis-ckb-productathon-ship-on-ckb-kisumu-kenya/11262/2) | Dorex45 | 2026-11-22 01:35:54 CST | LFG I totally love every bit of this
- `S05` [[DIS] RIVET: Decentralized GitHub Backup, Timestamping and Restore on CKB](https://talk.nervos.org/t/dis-rivet-decentralized-github-backup-timestamping-and-restore-on-ckb/10739/17) | Jedi_dtechmaker | 2026-11-22 00:17:27 CST | Rivet Milestone 2: CLI Restore Tooling and Hardening Delivery update · November 21, 2026 · CKB Testnet Implementation and project acceptance testing for Rivet’s second grant milestone are complete. Milestone 2 delivers a published cross-platform CLI, independent Exact Restore,...
- `S06` [[DIS] KeyMe — CKB's PSBT: Open Air-Gapped Signing and the First DIY Hardware](https://talk.nervos.org/t/dis-keyme-ckbs-psbt-open-air-gapped-signing-and-the-first-diy-hardware/11258/7) | ArthurZhang | 2026-11-21 22:30:18 CST | Very promising initiative, just two questions with PSCT v0, one, combine() only merges signatures for an identical transaction. How would we support actual multi-party transaction construction? two,can we have an extensible way to verify custom script semantics and signing...
- `S07` [RFC draft: Lock Proof, proving control of a CKB lock](https://talk.nervos.org/t/rfc-draft-lock-proof-proving-control-of-a-ckb-lock/11260/6) | tea | 2026-11-21 11:05:26 CST | LusoCryptoLabs: Which locks does your backend need to accept? of course this is wallet binding we’re talking about so ideally all locks getting supported is very beneficial and that’s why I asked. Unless it can be used for something else i’m not aware yet?
- `S08` [RFC draft: Lock Proof, proving control of a CKB lock](https://talk.nervos.org/t/rfc-draft-lock-proof-proving-control-of-a-ckb-lock/11260/7) | LusoCryptoLabs | 2026-11-21 20:39:03 CST | All locks is what it is built for. The verifier runs the lock itself in CKB-VM, so one code path covers every lock that signs the transaction hash; the only lock-specific check refuses Omnilock in administrator mode. A port has no lock to start from, and it would be checked...
- `S09` [RFC draft: Lock Proof, proving control of a CKB lock](https://talk.nervos.org/t/rfc-draft-lock-proof-proving-control-of-a-ckb-lock/11260/8) | LusoCryptoLabs | 2026-11-21 22:04:26 CST | The Rust crate is in the repo: rust/ in ckb-ward. It covers the backend side of the npm package: the message, the template for the wallet, verify, and the DAO snapshot helpers. The lock runs in process with ckb-script, the node’s own crate, so it handles every lock that signs...
- `S10` [DAO提案公平性疑问？](https://talk.nervos.org/t/dao/11261/13) | phroi | 2026-11-21 06:59:22 CST | Fai: And the result? Some people left in disappointment, the project ultimately fell apart, and the DAO wasted precious treasury funds — a lesson that left everyone worse off. Hey @Fai, the integration is on hold, not abandoned: I covered the details in the Rosen thread. The...
- `S11` [DAO提案公平性疑问？](https://talk.nervos.org/t/dao/11261/14) | hao_zhang | 2026-11-21 07:06:53 CST | 15000美金还少吗？
- `S12` [DAO提案公平性疑问？](https://talk.nervos.org/t/dao/11261/15) | phroi | 2026-11-21 07:17:38 CST | hao_zhang: Is $15,000 not enough? Hey @hao_zhang, it was paid in CKB: the $15k milestone is 6,313,131 CKB, about $5k at the current price. We asked for these amounts in the proposal. The community voted on it: 64% of the voting weight was in favor. If you thought it was too...
- `S13` [DAO提案公平性疑问？](https://talk.nervos.org/t/dao/11261/16) | hao_zhang | 2026-11-21 07:52:12 CST | 1.回顾我对话，2.我们看最后结果吧，这座桥会怎么样
- `S14` [DAO提案公平性疑问？](https://talk.nervos.org/t/dao/11261/17) | phroi | 2026-11-21 08:01:39 CST | hao_zhang: Review my conversation Review who voted: I was surprised to see so many well-known community members back the bridge with their own CKB. hao_zhang: Let’s look at the final result — what will happen to this bridge? Should I launch it anyway, putting user funds at...
- `S15` [DAO提案公平性疑问？](https://talk.nervos.org/t/dao/11261/18) | asondev | 2026-11-21 08:03:39 CST | Questioning how the Community Fund operates is part of participating in governance. You can disagree with the tone of posts on X, but that leaves the questions I raised about the DAO unanswered. People should be able to raise those questions here without first having to prove...
- `S16` [[DIS] FiberNuts: Reliable Cashu-over-Fiber Payments with Hosted-LSP Onboarding](https://talk.nervos.org/t/dis-fibernuts-reliable-cashu-over-fiber-payments-with-hosted-lsp-onboarding/11051/13) | zz_tovarishch | 2026-11-21 14:44:16 CST | https://explorer.nervos.org/transaction/0x64b4ddd95cad37fea62f7cd23d70ffda007fba8ae06a54d3df5a3babc0050ce7 Initial funding $1,500/$0.0009 = 1,666,667 CKB
- `S17` [[DIS] FiberNuts: Reliable Cashu-over-Fiber Payments with Hosted-LSP Onboarding](https://talk.nervos.org/t/dis-fibernuts-reliable-cashu-over-fiber-payments-with-hosted-lsp-onboarding/11051/14) | Code3ks | 2026-11-21 17:49:00 CST | Thank you, payment received. Next, I would give an update regarding M1 progress.
- `S18` [How can we change username?](https://talk.nervos.org/t/how-can-we-change-username/11276/4) | zz_tovarishch | 2026-11-21 11:41:23 CST | 我查询了一下Nervos Talk底层的Discourse文档 Discourse – 25 Jun 18 Understanding Discourse Trust Levels The user trust system is a fundamental cornerstone of Discourse. Trust levels are a way of… 似乎修改用户名的权限确实不在各个Level的授权中 所以，如果您想修改您的用户名，或者可以告诉我（作为Mod），我来帮您修改 image1092×1334 74.1 KB
- `S19` [How can we change username?](https://talk.nervos.org/t/how-can-we-change-username/11276/5) | tea | 2026-11-21 12:29:05 CST | zz_tovarishch: So, if you would like to change your username, you can let me know (as a Mod) and I can help you change it awesome. Could you help me change it to just “tea”? I think it’s available
- `S20` [How can we change username?](https://talk.nervos.org/t/how-can-we-change-username/11276/6) | tea | 2026-11-21 13:42:23 CST | @zz_tovarishch username change affected now. Thank you!

## 活跃话题

1. [[DIS] Vellum: Reputation Extension on did:ckb](https://talk.nervos.org/t/dis-vellum-reputation-extension-on-did-ckb/10613) | 3 条近窗帖子 | 最新活动 2026-11-22 03:15:23 CST
2. [[DIS] CKB Productathon: Ship on CKB (Kisumu, Kenya)](https://talk.nervos.org/t/dis-ckb-productathon-ship-on-ckb-kisumu-kenya/11262) | 1 条近窗帖子 | 最新活动 2026-11-22 01:35:54 CST | tags: CKB, CKB-VM, Grant
3. [[DIS] RIVET: Decentralized GitHub Backup, Timestamping and Restore on CKB](https://talk.nervos.org/t/dis-rivet-decentralized-github-backup-timestamping-and-restore-on-ckb/10739) | 1 条近窗帖子 | 最新活动 2026-11-22 00:17:27 CST | tags: CKB
4. [[DIS] KeyMe — CKB's PSBT: Open Air-Gapped Signing and the First DIY Hardware](https://talk.nervos.org/t/dis-keyme-ckbs-psbt-open-air-gapped-signing-and-the-first-diy-hardware/11258) | 1 条近窗帖子 | 最新活动 2026-11-21 22:30:18 CST
5. [RFC draft: Lock Proof, proving control of a CKB lock](https://talk.nervos.org/t/rfc-draft-lock-proof-proving-control-of-a-ckb-lock/11260) | 3 条近窗帖子 | 最新活动 2026-11-21 22:04:26 CST
6. [DAO提案公平性疑问？](https://talk.nervos.org/t/dao/11261) | 11 条近窗帖子 | 最新活动 2026-11-21 18:21:10 CST
7. [[DIS] FiberNuts: Reliable Cashu-over-Fiber Payments with Hosted-LSP Onboarding](https://talk.nervos.org/t/dis-fibernuts-reliable-cashu-over-fiber-payments-with-hosted-lsp-onboarding/11051) | 2 条近窗帖子 | 最新活动 2026-11-21 17:49:00 CST
8. [How can we change username?](https://talk.nervos.org/t/how-can-we-change-username/11276) | 3 条近窗帖子 | 最新活动 2026-11-21 13:42:23 CST | tags: lang-es

## 最近帖子摘录

- 2026-11-22 03:15:23 CST | Ayoub_Lesfer | [[DIS] Vellum: Reputation Extension on did:ckb](https://talk.nervos.org/t/dis-vellum-reputation-extension-on-did-ckb/10613/27) | Makes sense, thanks. Since v1 only says the campaign hit its goal and finalized, with the total, I’m fine turning it on as is and leaving the judgement to whoever reads the...
- 2026-11-22 01:36:15 CST | matt_ckb | [DAO提案公平性疑问？](https://talk.nervos.org/t/dao/11261/23) | 
- 2026-11-22 01:35:54 CST | Dorex45 | [[DIS] CKB Productathon: Ship on CKB (Kisumu, Kenya)](https://talk.nervos.org/t/dis-ckb-productathon-ship-on-ckb-kisumu-kenya/11262/2) | LFG I totally love every bit of this
- 2026-11-22 00:17:27 CST | Jedi_dtechmaker | [[DIS] RIVET: Decentralized GitHub Backup, Timestamping and Restore on CKB](https://talk.nervos.org/t/dis-rivet-decentralized-github-backup-timestamping-and-restore-on-ckb/10739/17) | Rivet Milestone 2: CLI Restore Tooling and Hardening Delivery update · November 21, 2026 · CKB Testnet Implementation and project acceptance testing for Rivet’s second grant...
- 2026-11-21 22:30:18 CST | ArthurZhang | [[DIS] KeyMe — CKB's PSBT: Open Air-Gapped Signing and the First DIY Hardware](https://talk.nervos.org/t/dis-keyme-ckbs-psbt-open-air-gapped-signing-and-the-first-diy-hardware/11258/7) | Very promising initiative, just two questions with PSCT v0, one, combine() only merges signatures for an identical transaction. How would we support actual multi-party...
- 2026-11-21 22:04:26 CST | LusoCryptoLabs | [RFC draft: Lock Proof, proving control of a CKB lock](https://talk.nervos.org/t/rfc-draft-lock-proof-proving-control-of-a-ckb-lock/11260/8) | The Rust crate is in the repo: rust/ in ckb-ward. It covers the backend side of the npm package: the message, the template for the wallet, verify, and the DAO snapshot helpers....
- 2026-11-21 20:39:03 CST | LusoCryptoLabs | [RFC draft: Lock Proof, proving control of a CKB lock](https://talk.nervos.org/t/rfc-draft-lock-proof-proving-control-of-a-ckb-lock/11260/7) | All locks is what it is built for. The verifier runs the lock itself in CKB-VM, so one code path covers every lock that signs the transaction hash; the only lock-specific check...
- 2026-11-21 18:21:10 CST | Fai | [DAO提案公平性疑问？](https://talk.nervos.org/t/dao/11261/22) | phroi: Love & Peace 你的签名是 “Love & Peace” ，希望你能和平，也希望社区和平！ 说下我的看法： 我之所以最近出现在这里，是感觉社区有些问题（目的性太强，缺乏社区精神）；之所以提出来Rosen项目，是不希望现在重蹈覆辙；之所以对某些助资有质疑，是因为长时间没看到有所成果。所以 相信他们也是这样的。...
- 2026-11-21 17:49:00 CST | Code3ks | [[DIS] FiberNuts: Reliable Cashu-over-Fiber Payments with Hosted-LSP Onboarding](https://talk.nervos.org/t/dis-fibernuts-reliable-cashu-over-fiber-payments-with-hosted-lsp-onboarding/11051/14) | Thank you, payment received. Next, I would give an update regarding M1 progress.
- 2026-11-21 15:53:17 CST | phroi | [DAO提案公平性疑问？](https://talk.nervos.org/t/dao/11261/21) | hao_zhang: Ensuring user funds are safe and that bridge ultimately having no users are not contradictory I guess this is not really about Rosen, is it? [DIS] Infinity Wallet...
- 2026-11-21 14:44:16 CST | zz_tovarishch | [[DIS] FiberNuts: Reliable Cashu-over-Fiber Payments with Hosted-LSP Onboarding](https://talk.nervos.org/t/dis-fibernuts-reliable-cashu-over-fiber-payments-with-hosted-lsp-onboarding/11051/13) | https://explorer.nervos.org/transaction/0x64b4ddd95cad37fea62f7cd23d70ffda007fba8ae06a54d3df5a3babc0050ce7 Initial funding $1,500/$0.0009 = 1,666,667 CKB
- 2026-11-21 13:42:23 CST | tea | [How can we change username?](https://talk.nervos.org/t/how-can-we-change-username/11276/6) | @zz_tovarishch username change affected now. Thank you!
- 2026-11-21 12:48:23 CST | truthixify | [[DIS] Vellum: Reputation Extension on did:ckb](https://talk.nervos.org/t/dis-vellum-reputation-extension-on-did-ckb/10613/26) | Yes! Let’s do this. Send me a DM on telegram so we can discuss the details.
- 2026-11-21 12:33:36 CST | Jedi_dtechmaker | [[DIS] Vellum: Reputation Extension on did:ckb](https://talk.nervos.org/t/dis-vellum-reputation-extension-on-did-ckb/10613/25) | Hi @truthixify , I’m thinking of integrating Vellum into Rivet. Developers could link their did:ckb and display their verified claims alongside their Rivet passport. Does your...
- 2026-11-21 12:29:05 CST | tea | [How can we change username?](https://talk.nervos.org/t/how-can-we-change-username/11276/5) | zz_tovarishch: So, if you would like to change your username, you can let me know (as a Mod) and I can help you change it awesome. Could you help me change it to just “tea”? I...
- 2026-11-21 11:41:23 CST | zz_tovarishch | [How can we change username?](https://talk.nervos.org/t/how-can-we-change-username/11276/4) | 我查询了一下Nervos Talk底层的Discourse文档 Discourse – 25 Jun 18 Understanding Discourse Trust Levels The user trust system is a fundamental cornerstone of Discourse. Trust levels are a...
- 2026-11-21 11:05:26 CST | tea | [RFC draft: Lock Proof, proving control of a CKB lock](https://talk.nervos.org/t/rfc-draft-lock-proof-proving-control-of-a-ckb-lock/11260/6) | LusoCryptoLabs: Which locks does your backend need to accept? of course this is wallet binding we’re talking about so ideally all locks getting supported is very beneficial and...
- 2026-11-21 11:00:29 CST | matt_ckb | [DAO提案公平性疑问？](https://talk.nervos.org/t/dao/11261/20) | asondev: good place to start is making project outcomes easier to review and funding decisions easier to scrutinize The next step would be creating a metarule proposal regarding...
- 2026-11-21 10:19:27 CST | hao_zhang | [DAO提案公平性疑问？](https://talk.nervos.org/t/dao/11261/19) | 保证用户资金安全和那个桥最终没有人用，并不矛盾，不讨论了，我们看最后结果吧
- 2026-11-21 08:03:39 CST | asondev | [DAO提案公平性疑问？](https://talk.nervos.org/t/dao/11261/18) | Questioning how the Community Fund operates is part of participating in governance. You can disagree with the tone of posts on X, but that leaves the questions I raised about...
