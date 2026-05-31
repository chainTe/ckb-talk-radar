# Nervos Talk 社区简报

- 统计窗口: 2026-05-31 01:59:58 CST 到 2026-06-01 01:59:58 CST
- 生成时间: 2026-06-01 02:00:02 CST
- 话题数: 3
- 帖子数: 4
- 作者数: 3
- 总结模式: ai:openrouter

## 社区总结

## 今日发生了什么

今天 Nervos Talk 论坛整体较平静，主要活动集中在两个移动端项目的进展更新：Pocket Node 轻钱包发布了 v1.7.0 里程碑版本并新增生物识别安全功能，同时社区开发者 wyltek 首次亮相了一款名为"CKB Directory"的生态系统目录应用原型。[S01, S03]

## 重点话题

- **Pocket Node 钱包完成 M4 里程碑**：Android 轻客户端发布 v1.7.0，核心更新是将助记词查看迁移至 BiometricPrompt 生物识别验证，提升安全层级；v1.6.1 用户可通过应用内自动更新直接升级，无需跳转，团队正在推进 Google Play 商店上架流程。[S01, S02]

- **CKB Directory 应用首次公开**：社区开发者 wyltek 展示了一款正在开发的 Android 生态目录应用，计划后续移植 iOS，旨在为 CKB 生态系统提供便捷的项目与资源聚合入口，目前仍处于早期建设阶段。[S03]

- **CellScript 包管理 RFC 持续讨论**：ArthurZhang 补充了关于注册表边界的技术思考，探讨 resolver 是否应扩展至管理 verifier、可部署合约、已部署产物记录等更广泛的 reproducible artifact，为 CellScript 生态的工具链标准化提供长期设计方向。[S04]

## 值得继续跟进

- Pocket Node 的 Google Play 商店审核进展及正式上线时间。[S02]

- CKB Directory 的功能范围界定与生态项目收录标准，目前仅见原型展示，具体数据更新机制尚不明确。[S03]

- CellScript 包管理注册表的边界决策，若扩展至合约部署产物管理，可能影响 CKB 开发者工具链的整体架构。[S04]

## 来源索引

- `S01` [[DIS] Mobile-Ready CKB Light Client (Pocket Node) for Android](https://talk.nervos.org/t/dis-mobile-ready-ckb-light-client-pocket-node-for-android/9879/45) | Jnr6 | 2026-06-01 01:44:48 CST | Milestone 3 Completion Report Project: Pocket Node: Mobile CKB Light Client Wallet for Android Repository: github.com/RaheemJnr/pocket-node Milestone: M4 Releases: v1.7.0 What’s new in v1.7.0 / M4 Security V2 Keystore migration: mnemonic reveal now requires BiometricPrompt (or...
- `S02` [[DIS] Mobile-Ready CKB Light Client (Pocket Node) for Android](https://talk.nervos.org/t/dis-mobile-ready-ckb-light-client-pocket-node-for-android/9879/46) | Jnr6 | 2026-06-01 01:47:39 CST | For user using the v1.6.1 of the app, there is an auto update option that allows you to directly update the app with leaving, this is to make it easier for user to update pending our playstore release which is currently being worked on. image624×1280 75.7 KB
- `S03` [CKB Directory](https://talk.nervos.org/t/ckb-directory/10327/1) | wyltek | 2026-06-01 00:07:05 CST | IMG_95821149×2408 588 KB Gday Nervos fam. One of the numerous things I’m building right now is this, tentatively titled “CKB Directory” app. Initially being built for Android with iOS porting afterwards. The main purpose of the app is to be a convenient directory of ecosystem...
- `S04` [[RFC] CellScript 的包管理：一个 Go 语言风格的、基于 GitHub 的 CKB 合约包管理注册表](https://talk.nervos.org/t/rfc-cellscript-go-github-ckb/10238/4) | ArthurZhang | 2026-05-31 20:22:46 CST | 我补充更新一个关于 registry 边界的想法，未来也可能和前面 Jan 提到的 package.namespace 是否可以扩展到 CellScript 之外的 artifact / ckb-bootstrapper 这类问题有关。 如果 registry 未来不只管理 CellScript 源码包，而是也管理 verifier、deployable contract、deployed artifact record，甚至更一般的 reproducible artifact，那么 resolver 的边界就需要更清楚。 我倾向于区分两类东西。...

## 活跃话题

1. [[DIS] Mobile-Ready CKB Light Client (Pocket Node) for Android](https://talk.nervos.org/t/dis-mobile-ready-ckb-light-client-pocket-node-for-android/9879) | 2 条近窗帖子 | 最新活动 2026-06-01 01:47:39 CST | tags: CKB, light-client
2. [CKB Directory](https://talk.nervos.org/t/ckb-directory/10327) | 1 条近窗帖子 | 最新活动 2026-06-01 00:07:05 CST
3. [[RFC] CellScript 的包管理：一个 Go 语言风格的、基于 GitHub 的 CKB 合约包管理注册表](https://talk.nervos.org/t/rfc-cellscript-go-github-ckb/10238) | 1 条近窗帖子 | 最新活动 2026-05-31 20:22:46 CST | tags: CKB, CKB-VM, CellScript

## 最近帖子摘录

- 2026-06-01 01:47:39 CST | Jnr6 | [[DIS] Mobile-Ready CKB Light Client (Pocket Node) for Android](https://talk.nervos.org/t/dis-mobile-ready-ckb-light-client-pocket-node-for-android/9879/46) | For user using the v1.6.1 of the app, there is an auto update option that allows you to directly update the app with leaving, this is to make it easier for user to update...
- 2026-06-01 01:44:48 CST | Jnr6 | [[DIS] Mobile-Ready CKB Light Client (Pocket Node) for Android](https://talk.nervos.org/t/dis-mobile-ready-ckb-light-client-pocket-node-for-android/9879/45) | Milestone 3 Completion Report Project: Pocket Node: Mobile CKB Light Client Wallet for Android Repository: github.com/RaheemJnr/pocket-node Milestone: M4 Releases: v1.7.0 What’s...
- 2026-06-01 00:07:05 CST | wyltek | [CKB Directory](https://talk.nervos.org/t/ckb-directory/10327/1) | IMG_95821149×2408 588 KB Gday Nervos fam. One of the numerous things I’m building right now is this, tentatively titled “CKB Directory” app. Initially being built for Android...
- 2026-05-31 20:22:46 CST | ArthurZhang | [[RFC] CellScript 的包管理：一个 Go 语言风格的、基于 GitHub 的 CKB 合约包管理注册表](https://talk.nervos.org/t/rfc-cellscript-go-github-ckb/10238/4) | 我补充更新一个关于 registry 边界的想法，未来也可能和前面 Jan 提到的 package.namespace 是否可以扩展到 CellScript 之外的 artifact / ckb-bootstrapper 这类问题有关。 如果 registry 未来不只管理 CellScript 源码包，而是也管理...
