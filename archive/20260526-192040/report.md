# Nervos Talk 社区简报

- 统计窗口: 2026-05-26 03:20:40 CST 到 2026-05-27 03:20:40 CST
- 生成时间: 2026-05-27 03:20:46 CST
- 话题数: 8
- 帖子数: 9
- 作者数: 8
- 总结模式: ai:openrouter

## 社区总结

## 今日发生了什么

今天 Nervos Talk 社区开发者工具链更新活跃，CellScript 发布 v0.15 版本并推出 VS Code 扩展教程 [S04, S06]；同时生态项目方面，Holdem Bulls 扑克游戏因登录问题暂停开发至下周 [S03]，而有开发者提出重建 Fiber Network 桌面客户端的资助申请 [S05]。

## 重点话题

- **CellScript 工具链双更新**：ArthurZhang 连续发布 CellScript 0.15 版本（聚焦约束不变量、Covenant ProofPlan 和验证器可靠性加固）[S06]，以及配套的 VS Code 扩展快速教程，帮助开发者直接在编辑器里编写和编译 .cell 合约 [S04]。

- **Fiber 生态两条平行线**：ebubedev 申请 6,000 美元资助，计划从零重建 Fiber Network Node 的桌面客户端，支持普通用户免 VPS 在 macOS/Windows/Linux 上运行节点 [S05]；此前 ILE_LABS 的 Fiber 隐私支付套件也更新了进展，表示正转向围绕核心 Lightning/Fiber 原语的小型概念验证 [S09]。

- **Holdem Bulls 项目遇阻**：扑克游戏 Holdem Bulls 因用户反馈登录问题，开发团队宣布暂停开发至下周日再集中修 Bug [S03]。

- **CKB Action Links 获认可**：社区成员 matt_ckb 对可分享 CKB 交易 URL 的草案协议表示赞赏，认为其很好地将 Open Transaction 与已有广泛采用的设计模式结合了起来 [S01]。

## 值得继续跟进

- Holdem Bulls 下周日能否如期恢复开发并修复登录问题，将检验该游戏项目的交付能力 [S03]。

- Fiber 桌面客户端资助提案（6,000 美元）的社区审议结果，若通过将成为 Fiber 网络节点普及的重要基础设施 [S05]。

- Phroi 在 NDAO 资金销毁提案中与开发者的讨论仍在持续，涉及社区基金 DAO 的预算路径设计 [S08]。相关讨论尚未形成明确结论，需关注后续是否推进到正式提案阶段 [S08]。

## 来源索引

- `S01` [CKB Action Links: a draft protocol for shareable CKB transaction URLs](https://talk.nervos.org/t/ckb-action-links-a-draft-protocol-for-shareable-ckb-transaction-urls/10315/2) | matt_ckb | 2026-05-27 02:56:22 CST | this is a really cool interface for open transactions. It’s been clear for a long time that they represent a very different way of building dapps and really good to see how you’ve connected them with a design pattern that already has adoption and experimentation around it. I...
- `S02` [Bringing poker back to Nervos - introducing Holdem Bulls V1](https://talk.nervos.org/t/bringing-poker-back-to-nervos-introducing-holdem-bulls-v1/10310/14) | Starhopper.bit | 2026-05-26 21:08:58 CST | I get the same log in issue as above.
- `S03` [Bringing poker back to Nervos - introducing Holdem Bulls V1](https://talk.nervos.org/t/bringing-poker-back-to-nervos-introducing-holdem-bulls-v1/10310/15) | Hbulls | 2026-05-27 02:47:53 CST | I know.unfortunatly we have development paused up until next Sunday. As soon as we resume we’ll address all bugs. Appreciate you trying
- `S04` [CellScript VS Code Extension Quick Tutorial](https://talk.nervos.org/t/cellscript-vs-code-extension-quick-tutorial/10318/1) | ArthurZhang | 2026-05-26 19:11:37 CST | Background The CellScript VS Code extension is local editor tooling for .cell contracts. It uses cellc --lsp for language features and spawns cellc directly for compile, metadata, constraints, and production report commands. image2342×2088 505 KB Below is a tutorial for using...
- `S05` [[DIS] Fiber Desktop v1 ground-up rebuild and launch — fnn desktop app](https://talk.nervos.org/t/dis-fiber-desktop-v1-ground-up-rebuild-and-launch-fnn-desktop-app/10317/1) | ebubedev | 2026-05-26 19:02:03 CST | 2. Summary This proposal requests a $6,000 USD grant (payable in CKB) to build v1 from the ground up — a production-ready desktop application that lets ordinary users run the official Fiber Network Node (fnn) on macOS, Windows, and Linux, without VPS hosting, router...
- `S06` [CellScript - A DSL for Cell-Based Contracts](https://talk.nervos.org/t/cellscript-a-dsl-for-cell-based-contracts/10193/24) | ArthurZhang | 2026-05-26 18:52:36 CST | CellScript 0.15 Release Notes Release date: 2026-05-26. Release tag: v0.15.0 GitHub release: https://github.com/a19q3/CellScript/releases/tag/v0.15.0. CellScript 0.15 is the scoped-invariant, Covenant ProofPlan, and verifier soundness hardening release. It closes the known...
- `S07` [Powerful Asset Complementing CKB and BTC/AI Generated Idea](https://talk.nervos.org/t/powerful-asset-complementing-ckb-and-btc-ai-generated-idea/10170/10) | Ckroamer | 2026-05-26 14:55:54 CST | Cool, this means if you are eager to push this project forward, the basis of it definitely should be a well functioning BTC and CKB swaps via Fiber. It must be struggled to achieve but quite meaningful to you, your project, and obviously the entire CKB ecosystem. Good luck to...
- `S08` [NDAO-0000 burn unused treasury funds](https://talk.nervos.org/t/ndao-0000-burn-unused-treasury-funds/9626/11) | phroi | 2026-05-26 08:50:20 CST | Hey @chenyukang and @xjd, thanks for keeping the treasury economic model caveat explicit in the ZK voting PoC. PoC path: Reviewing the PoC from the ZK voting PoC, I understand the current solution as a Community Fund DAO v1.0-style budget request path: a proposal names a...
- `S09` [[DIS] fiber-payjoin-kit: Collaborative Privacy for the Nervos Fiber Network](https://talk.nervos.org/t/dis-fiber-payjoin-kit-collaborative-privacy-for-the-nervos-fiber-network/10296/11) | ILE_LABS | 2026-05-26 04:21:37 CST | Thanks again for the thoughtful feedback and guidance shared so far. @neon.bit , based on the discussions and recommendations from the community, the team is currently moving toward a smaller proof-of-concept implementation focused around the core Lightning/Fiber primitives...

## 活跃话题

1. [CKB Action Links: a draft protocol for shareable CKB transaction URLs](https://talk.nervos.org/t/ckb-action-links-a-draft-protocol-for-shareable-ckb-transaction-urls/10315) | 1 条近窗帖子 | 最新活动 2026-05-27 02:56:22 CST | tags: CKB, dapp
2. [Bringing poker back to Nervos - introducing Holdem Bulls V1](https://talk.nervos.org/t/bringing-poker-back-to-nervos-introducing-holdem-bulls-v1/10310) | 2 条近窗帖子 | 最新活动 2026-05-27 02:47:53 CST | tags: CKB, QA, Spark-Program, dapp, partnership, testnet
3. [CellScript VS Code Extension Quick Tutorial](https://talk.nervos.org/t/cellscript-vs-code-extension-quick-tutorial/10318) | 1 条近窗帖子 | 最新活动 2026-05-26 19:11:37 CST | tags: CKB, CKB-VM, CellScript
4. [[DIS] Fiber Desktop v1 ground-up rebuild and launch — fnn desktop app](https://talk.nervos.org/t/dis-fiber-desktop-v1-ground-up-rebuild-and-launch-fnn-desktop-app/10317) | 1 条近窗帖子 | 最新活动 2026-05-26 19:02:03 CST | tags: fiber
5. [CellScript - A DSL for Cell-Based Contracts](https://talk.nervos.org/t/cellscript-a-dsl-for-cell-based-contracts/10193) | 1 条近窗帖子 | 最新活动 2026-05-26 18:52:36 CST | tags: CKB-VM, CellScript, DSL
6. [Powerful Asset Complementing CKB and BTC/AI Generated Idea](https://talk.nervos.org/t/powerful-asset-complementing-ckb-and-btc-ai-generated-idea/10170) | 1 条近窗帖子 | 最新活动 2026-05-26 14:55:54 CST | tags: CKB, CKB-VM, Nervos-项目动态, dapp, testnet
7. [NDAO-0000 burn unused treasury funds](https://talk.nervos.org/t/ndao-0000-burn-unused-treasury-funds/9626) | 1 条近窗帖子 | 最新活动 2026-05-26 08:50:20 CST
8. [[DIS] fiber-payjoin-kit: Collaborative Privacy for the Nervos Fiber Network](https://talk.nervos.org/t/dis-fiber-payjoin-kit-collaborative-privacy-for-the-nervos-fiber-network/10296) | 1 条近窗帖子 | 最新活动 2026-05-26 04:21:37 CST

## 最近帖子摘录

- 2026-05-27 02:56:22 CST | matt_ckb | [CKB Action Links: a draft protocol for shareable CKB transaction URLs](https://talk.nervos.org/t/ckb-action-links-a-draft-protocol-for-shareable-ckb-transaction-urls/10315/2) | this is a really cool interface for open transactions. It’s been clear for a long time that they represent a very different way of building dapps and really good to see how...
- 2026-05-27 02:47:53 CST | Hbulls | [Bringing poker back to Nervos - introducing Holdem Bulls V1](https://talk.nervos.org/t/bringing-poker-back-to-nervos-introducing-holdem-bulls-v1/10310/15) | I know.unfortunatly we have development paused up until next Sunday. As soon as we resume we’ll address all bugs. Appreciate you trying
- 2026-05-26 21:08:58 CST | Starhopper.bit | [Bringing poker back to Nervos - introducing Holdem Bulls V1](https://talk.nervos.org/t/bringing-poker-back-to-nervos-introducing-holdem-bulls-v1/10310/14) | I get the same log in issue as above.
- 2026-05-26 19:11:37 CST | ArthurZhang | [CellScript VS Code Extension Quick Tutorial](https://talk.nervos.org/t/cellscript-vs-code-extension-quick-tutorial/10318/1) | Background The CellScript VS Code extension is local editor tooling for .cell contracts. It uses cellc --lsp for language features and spawns cellc directly for compile,...
- 2026-05-26 19:02:03 CST | ebubedev | [[DIS] Fiber Desktop v1 ground-up rebuild and launch — fnn desktop app](https://talk.nervos.org/t/dis-fiber-desktop-v1-ground-up-rebuild-and-launch-fnn-desktop-app/10317/1) | 2. Summary This proposal requests a $6,000 USD grant (payable in CKB) to build v1 from the ground up — a production-ready desktop application that lets ordinary users run the...
- 2026-05-26 18:52:36 CST | ArthurZhang | [CellScript - A DSL for Cell-Based Contracts](https://talk.nervos.org/t/cellscript-a-dsl-for-cell-based-contracts/10193/24) | CellScript 0.15 Release Notes Release date: 2026-05-26. Release tag: v0.15.0 GitHub release: https://github.com/a19q3/CellScript/releases/tag/v0.15.0. CellScript 0.15 is the...
- 2026-05-26 14:55:54 CST | Ckroamer | [Powerful Asset Complementing CKB and BTC/AI Generated Idea](https://talk.nervos.org/t/powerful-asset-complementing-ckb-and-btc-ai-generated-idea/10170/10) | Cool, this means if you are eager to push this project forward, the basis of it definitely should be a well functioning BTC and CKB swaps via Fiber. It must be struggled to...
- 2026-05-26 08:50:20 CST | phroi | [NDAO-0000 burn unused treasury funds](https://talk.nervos.org/t/ndao-0000-burn-unused-treasury-funds/9626/11) | Hey @chenyukang and @xjd, thanks for keeping the treasury economic model caveat explicit in the ZK voting PoC. PoC path: Reviewing the PoC from the ZK voting PoC, I understand...
- 2026-05-26 04:21:37 CST | ILE_LABS | [[DIS] fiber-payjoin-kit: Collaborative Privacy for the Nervos Fiber Network](https://talk.nervos.org/t/dis-fiber-payjoin-kit-collaborative-privacy-for-the-nervos-fiber-network/10296/11) | Thanks again for the thoughtful feedback and guidance shared so far. @neon.bit , based on the discussions and recommendations from the community, the team is currently moving...
