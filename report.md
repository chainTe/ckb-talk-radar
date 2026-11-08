# Nervos Talk 社区简报

- 统计窗口: 2026-11-08 04:57:00 CST 到 2026-11-09 04:57:00 CST
- 生成时间: 2026-11-09 04:57:08 CST
- 话题数: 9
- 帖子数: 10
- 作者数: 8
- 总结模式: ai:openai-compatible

## 社区总结

## 今日发生了什么

今天论坛的动静主要来自开发者项目更新、资助提案和代码修复，而不是单一热点事件。[S01,S04,S05,S06,S10] 新帖里有 ILE Labs 的 ckb-msig 多签工具介绍，以及 CKB Escrow Security Test Kit 的资助申请。[S01,S04] Noir-CKB 私有 tally、Twine Fiber P2P PoC、QuotaCell 和 nervos.org 网站 PR 都有后续讨论或修改，隐私订单簿 appchain 也更新周报称继续修改论文。[S02,S03,S05,S08,S09,S10] 整体看，社区今天不算平静，但话题分散在多个开发项目上。[S01,S04,S05,S06,S08,S10]

## 重点话题

- ILE Labs 在 Spark Program 下发帖介绍 ckb-msig，目标是从 ckb-cli、Neuron 和 CCC 检查并合并 CKB 多签签名。[S01] 帖子把多方共同组装和签名同一笔交易视为要解决的缺口，并提到当前 CKB 多签付款和合约升级的签名方式。[S01]
- devnash 发布 CKB Escrow Security Test Kit 提案，申请 2,000 USDI，计划 8 周内在 CKB Testnet 上做开源 Rust 测试框架和 escrow 脚本参考实现。[S04] 申请人为 Zuhudev 和 Charles。[S04]
- xiaomao 在 Noir-CKB 私有 tally 帖下回应投票设计，提到今年早些时候为 Buidl Guidl challenge 构建 ZK 投票系统并复盘问题。[S02] psawyerberlin 接着围绕 commitment tree、per-election nullifier 和 paymaster 三要素继续交流。[S03]
- Twine 作者回应 ArthurZhang 的代码审查，承认问题真实，并列出从 514c33a 到 79788a8 的修复，包括两条腿使用相同哈希算法、移除硬编码 SHA-256。[S05] 另一边，mulham_na 分享 @fiber-pay/react-native 的进展，目标是给 Fiber Network 支付提供 React Native hooks，项目来自 CKBuilders capstone。[S06]
- NNCBN 帖中出现确认并更换接收资金 CKB 钱包地址的请求，给出了新地址。[S07] psawyerberlin 则为 nervos.org 提交 PR #34，移除过时信息并保留网站长期内容，改动包括 Journey 中过时的 In progress 信息。[S10]

## 值得继续跟进

- ILE Labs 提到相关工具仍在建设且私有，后续是否公开代码、能覆盖哪些多签签名流程值得观察。[S01]
- CKB Escrow Security Test Kit 目前只是 2,000 USDI 的资助申请，是否获批以及 8 周交付、测试网验证进度值得跟进。[S04]
- NNCBN 帖中的收款地址更换请求涉及资金接收，后续应确认地址是否经过官方确认，避免资金风险。[S07]

## 来源索引

- `S01` [Spark Program | ckb-msig: check and merge CKB multisig signatures from ckb-cli, Neuron and CCC](https://talk.nervos.org/t/spark-program-ckb-msig-check-and-merge-ckb-multisig-signatures-from-ckb-cli-neuron-and-ccc/11151/1) | ILE_LABS | 2026-11-09 04:19:38 CST | In our own words At ILE Labs we build tools. One of them, still under construction and private, led us to this gap: several parties putting together and signing one transaction. When we looked at how CKB’s own multisig payouts and contract upgrades get signed today, we saw the...
- `S02` [Noir-CKB: the private tally is live on CKB testnet, try it yourself](https://talk.nervos.org/t/noir-ckb-the-private-tally-is-live-on-ckb-testnet-try-it-yourself/11132/3) | xiaomao | 2026-11-08 17:13:37 CST | Thanks for reading it this closely, and for the ideas. Voting is actually something I’ve spent a lot of time on. Earlier this year I built a ZK voting system for the Buidl Guidl challenge, and I wrote up everything that broke along the way: Anonymous Blockchain Voting is...
- `S03` [Noir-CKB: the private tally is live on CKB testnet, try it yourself](https://talk.nervos.org/t/noir-ckb-the-private-tally-is-live-on-ckb-testnet-try-it-yourself/11132/4) | psawyerberlin | 2026-11-09 03:28:41 CST | xiaomao: Voting Hi xiaomao, Thanks for the thoughtful reply, and for the write-up on what broke in your Buidl Guidl system. Your three ingredients (commitment tree, per-election nullifier, paymaster) are exactly the list I keep landing on too. Some context, so you know where I...
- `S04` [CKB Escrow Security Test Kit](https://talk.nervos.org/t/ckb-escrow-security-test-kit/11150/1) | devnash | 2026-11-09 02:57:59 CST | CKB Escrow Security Test Kit A Reusable Rust Testing Framework and Reference Implementation for CKB Escrow Scripts Applicant: Zuhudev and Charles Funding Requested: $2,000 USDI Estimated Duration: 8 Weeks Target Network: CKB Testnet Project Type: Open-source developer...
- `S05` [Twine: Buy and Sell CKB Without Depositing on an Exchange (Fiber P2P PoC)](https://talk.nervos.org/t/twine-buy-and-sell-ckb-without-depositing-on-an-exchange-fiber-p2p-poc/10741/13) | ebubedev | 2026-11-09 02:38:19 CST | Thanks for going through the code carefully @ArthurZhang. Every point you raised was real. Here is what changed since 514c33a through 79788a8 (both directly from your notes and a few fixes around them): 1. Same hash algorithm on both legs Removed the hardcoded SHA-256...
- `S06` [React Native hooks for Fiber Network payments (`@fiber-pay/react-native`)](https://talk.nervos.org/t/react-native-hooks-for-fiber-network-payments-fiber-pay-react-native/11147/1) | mulham_na | 2026-11-09 02:17:50 CST | Hi everyone! I’ve been working on @fiber-pay/react-native for my CKBuilders capstone and wanted to share where it stands. The idea came from looking at khie-mobile, a React Native wallet for CKB. It doesn’t support Fiber payments yet. fiber-pay already has React hooks, but...
- `S07` [Spark Program | NNCBN - Nervos Network Community Boot Nodes](https://talk.nervos.org/t/spark-program-nncbn-nervos-network-community-boot-nodes/10653/24) | NNCBN | 2026-11-08 23:23:23 CST | xingtianchunyan: Please confirm whether the CKB wallet address included in your proposal is the official address for receiving the funds. Plesse change the address to: ckb1qzda0cr08m85hc8jlnfp3zer7xulejywt49kt2rr0vthywaa50xwsqvx3uktng4cvat879zw3e92w0uc6nqwttq6asuag
- `S08` [QuotaCell: Let your team spend without handing over the treasury](https://talk.nervos.org/t/quotacell-let-your-team-spend-without-handing-over-the-treasury/11002/13) | psawyerberlin | 2026-11-08 20:33:23 CST | Ticoworld: QuotaCell delegate key, without needing access to the owner’s key? Thanks @Ticoworld, and sorry for the slow follow-up. I wanted to check this properly against how CSR actually works before answering. The honest answer: yes, technically, but it doesn’t add much. A...
- `S09` [[DIS] Decentralized privacy order-book appchain based on CKB L1 - 2026.phase-1](https://talk.nervos.org/t/dis-decentralized-privacy-order-book-appchain-based-on-ckb-l1-2026-phase-1/10015/52) | Lawliet_Chan | 2026-11-08 17:26:12 CST | 周报 2026.11.8 继续上周的修改论文
- `S10` [Web page www.nervos.org - Discussion for new pull request](https://talk.nervos.org/t/web-page-www-nervos-org-discussion-for-new-pull-request/11133/7) | psawyerberlin | 2026-11-08 08:13:11 CST | Thanks everyone for the feedback. I’ve submitted the changes as a pull request: Remove outdated information and keep nervos.org timeless by psawyerberlin · Pull Request #34 · nervosnetwork/nervos-official-website · GitHub What changes: Journey: the outdated In progress /...

## 活跃话题

1. [Spark Program | ckb-msig: check and merge CKB multisig signatures from ckb-cli, Neuron and CCC](https://talk.nervos.org/t/spark-program-ckb-msig-check-and-merge-ckb-multisig-signatures-from-ckb-cli-neuron-and-ccc/11151) | 1 条近窗帖子 | 最新活动 2026-11-09 04:19:38 CST
2. [Noir-CKB: the private tally is live on CKB testnet, try it yourself](https://talk.nervos.org/t/noir-ckb-the-private-tally-is-live-on-ckb-testnet-try-it-yourself/11132) | 2 条近窗帖子 | 最新活动 2026-11-09 03:28:41 CST | tags: zkp
3. [CKB Escrow Security Test Kit](https://talk.nervos.org/t/ckb-escrow-security-test-kit/11150) | 1 条近窗帖子 | 最新活动 2026-11-09 02:57:59 CST | tags: Spark-Program
4. [Twine: Buy and Sell CKB Without Depositing on an Exchange (Fiber P2P PoC)](https://talk.nervos.org/t/twine-buy-and-sell-ckb-without-depositing-on-an-exchange-fiber-p2p-poc/10741) | 1 条近窗帖子 | 最新活动 2026-11-09 02:38:19 CST | tags: fiber
5. [React Native hooks for Fiber Network payments (`@fiber-pay/react-native`)](https://talk.nervos.org/t/react-native-hooks-for-fiber-network-payments-fiber-pay-react-native/11147) | 1 条近窗帖子 | 最新活动 2026-11-09 02:17:50 CST | tags: CKB
6. [Spark Program | NNCBN - Nervos Network Community Boot Nodes](https://talk.nervos.org/t/spark-program-nncbn-nervos-network-community-boot-nodes/10653) | 1 条近窗帖子 | 最新活动 2026-11-08 23:23:23 CST | tags: In-Progress, Node, Spark-Program, bootnode
7. [QuotaCell: Let your team spend without handing over the treasury](https://talk.nervos.org/t/quotacell-let-your-team-spend-without-handing-over-the-treasury/11002) | 1 条近窗帖子 | 最新活动 2026-11-08 20:33:23 CST | tags: CKB, CKB-VM, lang-en
8. [[DIS] Decentralized privacy order-book appchain based on CKB L1 - 2026.phase-1](https://talk.nervos.org/t/dis-decentralized-privacy-order-book-appchain-based-on-ckb-l1-2026-phase-1/10015) | 1 条近窗帖子 | 最新活动 2026-11-08 17:26:12 CST | tags: appchain
9. [Web page www.nervos.org - Discussion for new pull request](https://talk.nervos.org/t/web-page-www-nervos-org-discussion-for-new-pull-request/11133) | 1 条近窗帖子 | 最新活动 2026-11-08 08:13:11 CST

## 最近帖子摘录

- 2026-11-09 04:19:38 CST | ILE_LABS | [Spark Program | ckb-msig: check and merge CKB multisig signatures from ckb-cli, Neuron and CCC](https://talk.nervos.org/t/spark-program-ckb-msig-check-and-merge-ckb-multisig-signatures-from-ckb-cli-neuron-and-ccc/11151/1) | In our own words At ILE Labs we build tools. One of them, still under construction and private, led us to this gap: several parties putting together and signing one transaction....
- 2026-11-09 03:28:41 CST | psawyerberlin | [Noir-CKB: the private tally is live on CKB testnet, try it yourself](https://talk.nervos.org/t/noir-ckb-the-private-tally-is-live-on-ckb-testnet-try-it-yourself/11132/4) | xiaomao: Voting Hi xiaomao, Thanks for the thoughtful reply, and for the write-up on what broke in your Buidl Guidl system. Your three ingredients (commitment tree, per-election...
- 2026-11-09 02:57:59 CST | devnash | [CKB Escrow Security Test Kit](https://talk.nervos.org/t/ckb-escrow-security-test-kit/11150/1) | CKB Escrow Security Test Kit A Reusable Rust Testing Framework and Reference Implementation for CKB Escrow Scripts Applicant: Zuhudev and Charles Funding Requested: $2,000 USDI...
- 2026-11-09 02:38:19 CST | ebubedev | [Twine: Buy and Sell CKB Without Depositing on an Exchange (Fiber P2P PoC)](https://talk.nervos.org/t/twine-buy-and-sell-ckb-without-depositing-on-an-exchange-fiber-p2p-poc/10741/13) | Thanks for going through the code carefully @ArthurZhang. Every point you raised was real. Here is what changed since 514c33a through 79788a8 (both directly from your notes and...
- 2026-11-09 02:17:50 CST | mulham_na | [React Native hooks for Fiber Network payments (`@fiber-pay/react-native`)](https://talk.nervos.org/t/react-native-hooks-for-fiber-network-payments-fiber-pay-react-native/11147/1) | Hi everyone! I’ve been working on @fiber-pay/react-native for my CKBuilders capstone and wanted to share where it stands. The idea came from looking at khie-mobile, a React...
- 2026-11-08 23:23:23 CST | NNCBN | [Spark Program | NNCBN - Nervos Network Community Boot Nodes](https://talk.nervos.org/t/spark-program-nncbn-nervos-network-community-boot-nodes/10653/24) | xingtianchunyan: Please confirm whether the CKB wallet address included in your proposal is the official address for receiving the funds. Plesse change the address to:...
- 2026-11-08 20:33:23 CST | psawyerberlin | [QuotaCell: Let your team spend without handing over the treasury](https://talk.nervos.org/t/quotacell-let-your-team-spend-without-handing-over-the-treasury/11002/13) | Ticoworld: QuotaCell delegate key, without needing access to the owner’s key? Thanks @Ticoworld, and sorry for the slow follow-up. I wanted to check this properly against how...
- 2026-11-08 17:26:12 CST | Lawliet_Chan | [[DIS] Decentralized privacy order-book appchain based on CKB L1 - 2026.phase-1](https://talk.nervos.org/t/dis-decentralized-privacy-order-book-appchain-based-on-ckb-l1-2026-phase-1/10015/52) | 周报 2026.11.8 继续上周的修改论文
- 2026-11-08 17:13:37 CST | xiaomao | [Noir-CKB: the private tally is live on CKB testnet, try it yourself](https://talk.nervos.org/t/noir-ckb-the-private-tally-is-live-on-ckb-testnet-try-it-yourself/11132/3) | Thanks for reading it this closely, and for the ideas. Voting is actually something I’ve spent a lot of time on. Earlier this year I built a ZK voting system for the Buidl Guidl...
- 2026-11-08 08:13:11 CST | psawyerberlin | [Web page www.nervos.org - Discussion for new pull request](https://talk.nervos.org/t/web-page-www-nervos-org-discussion-for-new-pull-request/11133/7) | Thanks everyone for the feedback. I’ve submitted the changes as a pull request: Remove outdated information and keep nervos.org timeless by psawyerberlin · Pull Request #34 ·...
