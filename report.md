# Nervos Talk 社区简报

- 统计窗口: 2026-10-19 05:19:52 CST 到 2026-10-20 05:19:52 CST
- 生成时间: 2026-10-20 05:19:58 CST
- 话题数: 6
- 帖子数: 6
- 作者数: 5
- 总结模式: ai:openai-compatible

## 社区总结

## 今日发生了什么

今天论坛整体较平静，更新主要是项目进展帖和几条技术讨论回复 [S01, S02, S03, S04, S05, S06]。一条新帖在解释 CKB 的 “Since” 机制及集成方式 [S01]；社区催化项目发布 Q3 2026 报告 [S02]；另有开发者宣布 CKB 钱包连接 UI 包上 npm 并支持 did:ckb [S03]。讨论区里，资产价格预言机和 Fiber 机器支付会话都收到设计追问 [S04, S06]，Metaforo 投票问题也有版主回复 [S05]。

## 重点话题

- CKB “Since” 科普帖：Mannychino 发帖说明它解决什么问题、如何工作以及如何集成到 CKB 应用，并举了资产未来才能花费、代币归属/金库等场景 [S01]。
- 社区催化季度报告：neon.bit 更新 Q3 2026 报告，称 CKBuilders 已接近 100 名活跃 builder 和校友，Build on CKB 活动继续推动开发者 [S02]。
- 钱包 UI 包发布：Victor_Okenwa 宣布 ckb-connect-wallet-kit 已上 npm，是建立在 CCC 上的复合 React 钱包 UI 组件，并加入 did:ckb [S03]。
- 预言机设计追问：it44 在资产价格预言机帖中问 price_feed_type 的 publish_time_ms 除了要比旧值大，是否还要相对交易设置上界 [S04]。
- 治理与支付讨论：Metaforo 投票问题获回复，版主将帖子移到 community fund DAO 分区，并判断大概率是 Neuron 存入 CKB 后在 Metaforo 绑定了错误地址 [S05]；Fiber 帖中有人追问 createPaymentSession({ budget }) 的预算在哪执行，担心 SDK 内计数器会被 agent 进程或提示注入绕过/重置 [S06]。

## 值得继续跟进

- “Since” 帖后续是否引发具体集成问答，值得看开发者会不会分享实现案例 [S01]。
- 预言机 publish_time_ms 上界问题是否会得到作者回应，这是价格更新规则需要澄清的点 [S04]。
- Fiber 支付会话的预算执行位置是关键风险，若只在 SDK 计数器里，agent 进程或工具调用可能绕过 [S06]。

## 来源索引

- `S01` [Understanding 'Since' on Nervos CKB](https://talk.nervos.org/t/understanding-since-on-nervos-ckb/11010/1) | Mannychino | 2026-10-20 01:33:07 CST | What it solves, how it works, and how to integrate it into a CKB application Imagine building an application on Nervos CKB where a user deposits an asset today but should not be able to spend it until a future date. The same requirement might arise in token vesting, a treasury...
- `S02` [Nervos Community Catalyst: Quarterly Reports](https://talk.nervos.org/t/nervos-community-catalyst-quarterly-reports/8822/7) | neon.bit | 2026-10-19 21:31:58 CST | Q3 2026 Report Executive summary Q3 brought further growth across Nervos Community Catalyst’s developer programmes and community activity. CKBuilders grew to close to 100 active builders and alumni, while Build on CKB campaigns continued to challenge developers to advance...
- `S03` [Ckb-connect-wallet-kit is on npm: compound React wallet UI for CCC, now with did:ckb](https://talk.nervos.org/t/ckb-connect-wallet-kit-is-on-npm-compound-react-wallet-ui-for-ccc-now-with-did-ckb/11009/1) | Victor_Okenwa | 2026-10-19 21:31:08 CST | Hi everyone, Back in April I posted a revamp of the CKB wallet connection UI as a compound React component on top of CCC. The feedback from CKB builders was consistent: this should be installable as a package, not something you copy out of a demo. That package is now live as...
- `S04` [Asset Price Oracle on Nervos Network](https://talk.nervos.org/t/asset-price-oracle-on-nervos-network/10800/3) | it44 | 2026-10-19 15:14:22 CST | Thanks for the very explicit design write-up, and for stating the limits plainly. One question on price_feed_type: the update rule is new.publish_time_ms > old.publish_time_ms. Is there also an upper bound on publish_time_ms relative to the transaction, for example against a...
- `S05` [Unable to vote/like active proposal — Nervos DAO snapshot behavior on Metaforo](https://talk.nervos.org/t/unable-to-vote-like-active-proposal-nervos-dao-snapshot-behavior-on-metaforo/11004/4) | zz_tovarishch | 2026-10-19 14:08:50 CST | Hi Salman, 感谢您提出这个问题，首先因为这个问题更适合的分区是 community fund DAO, 所以我把帖子移到对应分区 另外您遇到的问题大概率是在使用Neuron存入CKB后，在Metaforo上绑定了错误的地址，可以参看 https://dao.ckb.community/thread/how-to-bind-your-nervos-dao-address-on-metaforo-and-vote-on-proposals-41913 这个帖子进行问题排除 Best,
- `S06` [Routed Machine Payment Sessions on Fiber — Looking for Community Feedback](https://talk.nervos.org/t/routed-machine-payment-sessions-on-fiber-looking-for-community-feedback/10694/2) | it44 | 2026-10-19 10:59:46 CST | Thanks for asking before building. One design question on createPaymentSession({ budget }): where is the budget enforced? If it is a counter inside the SDK, the agent process (or a prompt-injected tool call) can bypass or reset it, so the cap is only as strong as that process....

## 活跃话题

1. [Understanding 'Since' on Nervos CKB](https://talk.nervos.org/t/understanding-since-on-nervos-ckb/11010) | 1 条近窗帖子 | 最新活动 2026-10-20 01:33:07 CST
2. [Nervos Community Catalyst: Quarterly Reports](https://talk.nervos.org/t/nervos-community-catalyst-quarterly-reports/8822) | 1 条近窗帖子 | 最新活动 2026-10-19 21:31:58 CST | tags: lang-en
3. [Ckb-connect-wallet-kit is on npm: compound React wallet UI for CCC, now with did:ckb](https://talk.nervos.org/t/ckb-connect-wallet-kit-is-on-npm-compound-react-wallet-ui-for-ccc-now-with-did-ckb/11009) | 1 条近窗帖子 | 最新活动 2026-10-19 21:31:08 CST | tags: CKB, dapp, lang-en, wallet
4. [Asset Price Oracle on Nervos Network](https://talk.nervos.org/t/asset-price-oracle-on-nervos-network/10800) | 1 条近窗帖子 | 最新活动 2026-10-19 15:14:22 CST | tags: CKB, DeFi, Oracle, dapp
5. [Unable to vote/like active proposal — Nervos DAO snapshot behavior on Metaforo](https://talk.nervos.org/t/unable-to-vote-like-active-proposal-nervos-dao-snapshot-behavior-on-metaforo/11004) | 1 条近窗帖子 | 最新活动 2026-10-19 14:08:50 CST
6. [Routed Machine Payment Sessions on Fiber — Looking for Community Feedback](https://talk.nervos.org/t/routed-machine-payment-sessions-on-fiber-looking-for-community-feedback/10694) | 1 条近窗帖子 | 最新活动 2026-10-19 10:59:46 CST

## 最近帖子摘录

- 2026-10-20 01:33:07 CST | Mannychino | [Understanding 'Since' on Nervos CKB](https://talk.nervos.org/t/understanding-since-on-nervos-ckb/11010/1) | What it solves, how it works, and how to integrate it into a CKB application Imagine building an application on Nervos CKB where a user deposits an asset today but should not be...
- 2026-10-19 21:31:58 CST | neon.bit | [Nervos Community Catalyst: Quarterly Reports](https://talk.nervos.org/t/nervos-community-catalyst-quarterly-reports/8822/7) | Q3 2026 Report Executive summary Q3 brought further growth across Nervos Community Catalyst’s developer programmes and community activity. CKBuilders grew to close to 100 active...
- 2026-10-19 21:31:08 CST | Victor_Okenwa | [Ckb-connect-wallet-kit is on npm: compound React wallet UI for CCC, now with did:ckb](https://talk.nervos.org/t/ckb-connect-wallet-kit-is-on-npm-compound-react-wallet-ui-for-ccc-now-with-did-ckb/11009/1) | Hi everyone, Back in April I posted a revamp of the CKB wallet connection UI as a compound React component on top of CCC. The feedback from CKB builders was consistent: this...
- 2026-10-19 15:14:22 CST | it44 | [Asset Price Oracle on Nervos Network](https://talk.nervos.org/t/asset-price-oracle-on-nervos-network/10800/3) | Thanks for the very explicit design write-up, and for stating the limits plainly. One question on price_feed_type: the update rule is new.publish_time_ms > old.publish_time_ms....
- 2026-10-19 14:08:50 CST | zz_tovarishch | [Unable to vote/like active proposal — Nervos DAO snapshot behavior on Metaforo](https://talk.nervos.org/t/unable-to-vote-like-active-proposal-nervos-dao-snapshot-behavior-on-metaforo/11004/4) | Hi Salman, 感谢您提出这个问题，首先因为这个问题更适合的分区是 community fund DAO, 所以我把帖子移到对应分区 另外您遇到的问题大概率是在使用Neuron存入CKB后，在Metaforo上绑定了错误的地址，可以参看 https://dao.ckb.community/thread/how-to-bind-your-...
- 2026-10-19 10:59:46 CST | it44 | [Routed Machine Payment Sessions on Fiber — Looking for Community Feedback](https://talk.nervos.org/t/routed-machine-payment-sessions-on-fiber-looking-for-community-feedback/10694/2) | Thanks for asking before building. One design question on createPaymentSession({ budget }): where is the budget enforced? If it is a counter inside the SDK, the agent process...
