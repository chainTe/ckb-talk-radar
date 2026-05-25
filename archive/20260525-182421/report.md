# Nervos Talk 社区简报

- 统计窗口: 2026-05-25 02:24:21 CST 到 2026-05-26 02:24:21 CST
- 生成时间: 2026-05-26 02:24:28 CST
- 话题数: 10
- 帖子数: 14
- 作者数: 11
- 总结模式: ai:openrouter

## 社区总结

## 今日发生了什么

社区今日整体活跃度适中，讨论主要围绕 CKB 与比特币生态的互补资产方案、Fiber 网络隐私与基础设施展开。[S01, S02, S04, S05, S06] 此外，有成员正式提出建立"社区创意板+开发者匹配+资助管道"的新机制，引发对社区协作方式的关注。[S07]

## 重点话题

- **CKB-BTC 互补资产方案引发技术路线讨论**：Ckroamer 对"通过 RGB++ 协议将原生 BTC 映射到 CKB"的机制提出疑问，认为概念存在混淆；[S01] baclaire 随后补充说明原生 BTC 不能直接作为 RGB++ 资产，建议通过比特币闪电网络与 CKB Fiber 网络的跨链原子互换实现，并呼吁核心开发者深入探讨，目标打造出超越 Stacks 的机构级方案。[S02, S03]

- **Fiber 网络隐私提案获社区反馈**：neon.bit 对"fiber-payjoin-kit"隐私增强提案给出正式回应，认可其提升 Fiber 网络隐私的价值，但指出提案在论证深度上仍有提升空间。[S04]

- **Fiber 相关研究与教育资料持续更新**：Ckroamer 发布关于闪电网络瞭望塔（WatchTower）的系统性中文研究，解释其资金安全监控作用及与 LSP 的关系；[S06] 同时强调构建 LSP 对 Fiber 实现与闪电网络全互联的关键价值。[S05] 科普项目"Fiber Storybook"也更新了第二章流动性场景的图示，并回应了读者反馈。[S10, S11]

- **社区协作机制新提议**：T_Silva 提议建立"Community Idea Board"，整合创意征集、开发者匹配与资助申请流程，询问 Nervos 是否已有类似机制。[S07]

- **生态双周报与项目进展发布**：CKB Ecosystem Biweekly Update #17 如期发布，涵盖 CKB-VM 优化等基础设施进展；[S08] 隐私订单簿应用链 Invisibook 继续开发 MPC 结算模块；[S12] Spark Program 项目 Dular 确认收到相关款项，[S09] CKB-UGMP 项目则分享了 DOB 铸造原型的复现步骤与本周进度。[S14]

## 值得继续跟进

- RGB++ 与原生 BTC 映射的技术可行性争议尚未形成共识，核心团队是否回应 baclaire 的 @ 呼吁将影响方案推进节奏。[S01, S02, S03]

- Fiber 隐私提案"fiber-payjoin-kit"是否会在 neon.bit 的反馈基础上迭代，以及该隐私套件与现有闪电网络隐私方案（如 PTLC）的兼容性问题。[S04]

- Community Idea Board 提议如获得足够关注，可能催生新的社区治理与资助分配模式，需观察核心贡献者与基金会的态度。[S07]

## 来源索引

- `S01` [Powerful Asset Complementing CKB and BTC/AI Generated Idea](https://talk.nervos.org/t/powerful-asset-complementing-ckb-and-btc-ai-generated-idea/10170/7) | Ckroamer | 2026-05-25 20:18:50 CST | How it works: Bitcoin holders bind their BTC natively to CKB cells using the RGB++ protocol. Excuse me, I was a little confused about this part, how do you use RGB++ protocol to map native BTC token to CKB? The question comes out from the mechanism of RGB++, I remembered this...
- `S02` [Powerful Asset Complementing CKB and BTC/AI Generated Idea](https://talk.nervos.org/t/powerful-asset-complementing-ckb-and-btc-ai-generated-idea/10170/8) | baclaire | 2026-05-26 01:21:35 CST | Since we cant use the raw BTC as the RGB++ Asset. Native Bitcoin holders can access this yield instantly via cross-chain atomic swaps between Bitcoin’s Lightning Network and CKB’s Fiber Network. I think this is quick, secure and trustless.
- `S03` [Powerful Asset Complementing CKB and BTC/AI Generated Idea](https://talk.nervos.org/t/powerful-asset-complementing-ckb-and-btc-ai-generated-idea/10170/9) | baclaire | 2026-05-26 01:53:09 CST | @janx @matt_ckb @ If we discuss this idea in depth, it is going to be the bridge between CKB and BTC communities, we can come up with something better than Stacks. Something instituitional;
- `S04` [[DIS] fiber-payjoin-kit: Collaborative Privacy for the Nervos Fiber Network](https://talk.nervos.org/t/dis-fiber-payjoin-kit-collaborative-privacy-for-the-nervos-fiber-network/10296/10) | neon.bit | 2026-05-25 22:13:14 CST | Hi @ILE_LABS Firstly, welcome to the forum and to the community. The thought given to this proposal and how it could benefit Fiber Network is commendable! Privacy enhancement for Fiber is a great question to address. My feeling is that the proposal would have benefitted from a...
- `S05` [[Fiber] 比特币闪电网络的钱包与支付研究](https://talk.nervos.org/t/fiber/10298/4) | Ckroamer | 2026-05-25 15:52:37 CST | You’re right, building LSP is the most valuable movement for us in my point of view, especially when we achieve our programmability feature in Fiber. Using LSP in a totally same protocol with how currently Lightning Network does, this can make Fiber fully connectable to it and...
- `S06` [[Fiber] 比特币闪电网络的钱包与支付研究](https://talk.nervos.org/t/fiber/10298/5) | Ckroamer | 2026-05-25 20:20:36 CST | WatchTower：资金安全的瞭望塔 作为本篇研究的补充，我将系统性地讲解一下 “瞭望塔（WatchTower）” 对闪电网络的意义以及它在闪闪电网络拓扑结构中的位置。 WatchTower 本身是直接集成在闪电网络节点中的一个功能模块，但绝大多数用户是没有条件去运行它的，比如闪电网络轻节点或者 WASM 版本的 Fiber 就没有此功能，因此这类用户只能将资金安全的监控需求外包给第三方 WatchTower 服务商，在现实状况下，一般都由 LSP 服务商负责提供。 为什么闪电网络一定得需要 WatchTower？...
- `S07` [[DISC] Community Idea Board + Builder Matching + Grant Pipeline](https://talk.nervos.org/t/disc-community-idea-board-builder-matching-grant-pipeline/10316/1) | T_Silva | 2026-05-25 18:18:00 CST | Hey everyone, I’m not sure if something like this already exists in Nervos, but I came across the idea and thought it was really cool, so I wanted to share it here for discussion. The basic concept is a Community Idea Board where people in the community can suggest ideas for...
- `S08` [CKB Ecosystem Biweekly Update](https://talk.nervos.org/t/ckb-ecosystem-biweekly-update/9821/19) | zz_tovarishch | 2026-05-25 17:30:12 CST | image1200×675 67.2 KB CKB Ecosystem Biweekly Update #17 Welcome to the latest CKB Ecosystem Biweekly Update. Here’s a quick summary of key dev and ecosystem progress from the past two weeks. Infrastructure & Tooling @CKBdev optimized blake2b for CKB-VM, completed the CKB-VM...
- `S09` [Spark Program | Dular](https://talk.nervos.org/t/spark-program-dular/10212/9) | duongja | 2026-05-25 16:13:27 CST | Received
- `S10` [Fiber Storybook: Explaining Fiber Through Pico’s Airport Journey](https://talk.nervos.org/t/fiber-storybook-explaining-fiber-through-pico-s-airport-journey/10251/5) | yuqi | 2026-05-25 11:55:05 CST | I updated several scenes in Chapter 2 to make the liquidity flow clearer (Clarify Chapter 2 liquidity flow by yfeng2824 · Pull Request #4 · yfeng2824/fiber-storybook · GitHub). The following sceenshot is one example, showing the updated main scene for the service liquidity...
- `S11` [Fiber Storybook: Explaining Fiber Through Pico’s Airport Journey](https://talk.nervos.org/t/fiber-storybook-explaining-fiber-through-pico-s-airport-journey/10251/6) | Yeti | 2026-05-25 14:58:16 CST | Hi Yuqi, thanks for taking the time to add the extra info, I just went through the story again and that definitely helps to make things clearer about where the 5000 CKB and 100k sats came from. Sorry about this haha, but there’s something else which I think is a bit confusing....
- `S12` [[DIS] Decentralized privacy order-book appchain based on CKB L1 - 2026.phase-1](https://talk.nervos.org/t/dis-decentralized-privacy-order-book-appchain-based-on-ckb-l1-2026-phase-1/10015/28) | Lawliet_Chan | 2026-05-25 10:06:13 CST | 周报 2026.5.25 继续开发MPC结算模块： https://github.com/invisibook-lab/invisibook/pull/1
- `S13` [CKB Action Links: a draft protocol for shareable CKB transaction URLs](https://talk.nervos.org/t/ckb-action-links-a-draft-protocol-for-shareable-ckb-transaction-urls/10315/1) | truthixify | 2026-05-25 04:45:08 CST | Hi all - sharing an early draft of CKB Action Links, a protocol that lets anyone publish a CKB transaction intent as a URL. A user clicks the link, their wallet renders a preview, they sign, the transaction lands on chain. No dApp navigation, no separate wallet-to-dApp...
- `S14` [Spark Program | CKB-UGMP —— A Universal Spore/DOB Seamless Minting Infrastructure Prototype on CKB —— 基于 CKB 的通用 Spore/DOB 无感铸造基础设施原型](https://talk.nervos.org/t/spark-program-ckb-ugmp-a-universal-spore-dob-seamless-minting-infrastructure-prototype-on-ckb-ckb-spore-dob/10098/24) | HNO3Miracle | 2026-05-25 03:52:02 CST | 各位好，和各位分享复现步骤以及上周进度。 复现步骤 进入页面，点击连接钱包，根据步骤登录 joyid ckb 测试网钱包，会显示Address 还有 Capacity，即为连接成功。 选择图片资源，点击上传到 IPFS，上传成功后 CID，点击 Gateway 的网址可以正常访问脸上的图片。 点击 Mine DOB，即可把预览 JSON 上链，在 CKB Testnet 保存。（目前不可用） 点击 打开展示大厅，可以看到自己上传的图片。 本周完成 本周继续推进展示层和链上查询能力，并同步处理签名阻塞问题。 推进了独立展示大厅页面 /gallery...

## 活跃话题

1. [Powerful Asset Complementing CKB and BTC/AI Generated Idea](https://talk.nervos.org/t/powerful-asset-complementing-ckb-and-btc-ai-generated-idea/10170) | 3 条近窗帖子 | 最新活动 2026-05-26 01:53:09 CST | tags: CKB, CKB-VM, Nervos-项目动态, dapp, testnet
2. [[DIS] fiber-payjoin-kit: Collaborative Privacy for the Nervos Fiber Network](https://talk.nervos.org/t/dis-fiber-payjoin-kit-collaborative-privacy-for-the-nervos-fiber-network/10296) | 1 条近窗帖子 | 最新活动 2026-05-25 22:13:14 CST
3. [[Fiber] 比特币闪电网络的钱包与支付研究](https://talk.nervos.org/t/fiber/10298) | 2 条近窗帖子 | 最新活动 2026-05-25 20:20:36 CST
4. [[DISC] Community Idea Board + Builder Matching + Grant Pipeline](https://talk.nervos.org/t/disc-community-idea-board-builder-matching-grant-pipeline/10316) | 1 条近窗帖子 | 最新活动 2026-05-25 18:18:00 CST | tags: CKB, partnership
5. [CKB Ecosystem Biweekly Update](https://talk.nervos.org/t/ckb-ecosystem-biweekly-update/9821) | 1 条近窗帖子 | 最新活动 2026-05-25 17:30:12 CST | tags: Ecosystem-Update
6. [Spark Program | Dular](https://talk.nervos.org/t/spark-program-dular/10212) | 1 条近窗帖子 | 最新活动 2026-05-25 16:13:27 CST | tags: In-Progress, Spark-Program
7. [Fiber Storybook: Explaining Fiber Through Pico’s Airport Journey](https://talk.nervos.org/t/fiber-storybook-explaining-fiber-through-pico-s-airport-journey/10251) | 2 条近窗帖子 | 最新活动 2026-05-25 14:58:16 CST | tags: fiber
8. [[DIS] Decentralized privacy order-book appchain based on CKB L1 - 2026.phase-1](https://talk.nervos.org/t/dis-decentralized-privacy-order-book-appchain-based-on-ckb-l1-2026-phase-1/10015) | 1 条近窗帖子 | 最新活动 2026-05-25 10:06:13 CST | tags: appchain
9. [CKB Action Links: a draft protocol for shareable CKB transaction URLs](https://talk.nervos.org/t/ckb-action-links-a-draft-protocol-for-shareable-ckb-transaction-urls/10315) | 1 条近窗帖子 | 最新活动 2026-05-25 04:45:08 CST | tags: CKB, dapp
10. [Spark Program | CKB-UGMP —— A Universal Spore/DOB Seamless Minting Infrastructure Prototype on CKB —— 基于 CKB 的通用 Spore/DOB 无感铸造基础设施原型](https://talk.nervos.org/t/spark-program-ckb-ugmp-a-universal-spore-dob-seamless-minting-infrastructure-prototype-on-ckb-ckb-spore-dob/10098) | 1 条近窗帖子 | 最新活动 2026-05-25 03:52:02 CST | tags: In-Progress, Spark-Program

## 最近帖子摘录

- 2026-05-26 01:53:09 CST | baclaire | [Powerful Asset Complementing CKB and BTC/AI Generated Idea](https://talk.nervos.org/t/powerful-asset-complementing-ckb-and-btc-ai-generated-idea/10170/9) | @janx @matt_ckb @ If we discuss this idea in depth, it is going to be the bridge between CKB and BTC communities, we can come up with something better than Stacks. Something...
- 2026-05-26 01:21:35 CST | baclaire | [Powerful Asset Complementing CKB and BTC/AI Generated Idea](https://talk.nervos.org/t/powerful-asset-complementing-ckb-and-btc-ai-generated-idea/10170/8) | Since we cant use the raw BTC as the RGB++ Asset. Native Bitcoin holders can access this yield instantly via cross-chain atomic swaps between Bitcoin’s Lightning Network and...
- 2026-05-25 22:13:14 CST | neon.bit | [[DIS] fiber-payjoin-kit: Collaborative Privacy for the Nervos Fiber Network](https://talk.nervos.org/t/dis-fiber-payjoin-kit-collaborative-privacy-for-the-nervos-fiber-network/10296/10) | Hi @ILE_LABS Firstly, welcome to the forum and to the community. The thought given to this proposal and how it could benefit Fiber Network is commendable! Privacy enhancement...
- 2026-05-25 20:20:36 CST | Ckroamer | [[Fiber] 比特币闪电网络的钱包与支付研究](https://talk.nervos.org/t/fiber/10298/5) | WatchTower：资金安全的瞭望塔 作为本篇研究的补充，我将系统性地讲解一下 “瞭望塔（WatchTower）” 对闪电网络的意义以及它在闪闪电网络拓扑结构中的位置。 WatchTower 本身是直接集成在闪电网络节点中的一个功能模块，但绝大多数用户是没有条件去运行它的，比如闪电网络轻节点或者 WASM 版本的 Fiber...
- 2026-05-25 20:18:50 CST | Ckroamer | [Powerful Asset Complementing CKB and BTC/AI Generated Idea](https://talk.nervos.org/t/powerful-asset-complementing-ckb-and-btc-ai-generated-idea/10170/7) | How it works: Bitcoin holders bind their BTC natively to CKB cells using the RGB++ protocol. Excuse me, I was a little confused about this part, how do you use RGB++ protocol to...
- 2026-05-25 18:18:00 CST | T_Silva | [[DISC] Community Idea Board + Builder Matching + Grant Pipeline](https://talk.nervos.org/t/disc-community-idea-board-builder-matching-grant-pipeline/10316/1) | Hey everyone, I’m not sure if something like this already exists in Nervos, but I came across the idea and thought it was really cool, so I wanted to share it here for...
- 2026-05-25 17:30:12 CST | zz_tovarishch | [CKB Ecosystem Biweekly Update](https://talk.nervos.org/t/ckb-ecosystem-biweekly-update/9821/19) | image1200×675 67.2 KB CKB Ecosystem Biweekly Update #17 Welcome to the latest CKB Ecosystem Biweekly Update. Here’s a quick summary of key dev and ecosystem progress from the...
- 2026-05-25 16:13:27 CST | duongja | [Spark Program | Dular](https://talk.nervos.org/t/spark-program-dular/10212/9) | Received
- 2026-05-25 15:52:37 CST | Ckroamer | [[Fiber] 比特币闪电网络的钱包与支付研究](https://talk.nervos.org/t/fiber/10298/4) | You’re right, building LSP is the most valuable movement for us in my point of view, especially when we achieve our programmability feature in Fiber. Using LSP in a totally same...
- 2026-05-25 14:58:16 CST | Yeti | [Fiber Storybook: Explaining Fiber Through Pico’s Airport Journey](https://talk.nervos.org/t/fiber-storybook-explaining-fiber-through-pico-s-airport-journey/10251/6) | Hi Yuqi, thanks for taking the time to add the extra info, I just went through the story again and that definitely helps to make things clearer about where the 5000 CKB and 100k...
- 2026-05-25 11:55:05 CST | yuqi | [Fiber Storybook: Explaining Fiber Through Pico’s Airport Journey](https://talk.nervos.org/t/fiber-storybook-explaining-fiber-through-pico-s-airport-journey/10251/5) | I updated several scenes in Chapter 2 to make the liquidity flow clearer (Clarify Chapter 2 liquidity flow by yfeng2824 · Pull Request #4 · yfeng2824/fiber-storybook · GitHub)....
- 2026-05-25 10:06:13 CST | Lawliet_Chan | [[DIS] Decentralized privacy order-book appchain based on CKB L1 - 2026.phase-1](https://talk.nervos.org/t/dis-decentralized-privacy-order-book-appchain-based-on-ckb-l1-2026-phase-1/10015/28) | 周报 2026.5.25 继续开发MPC结算模块： https://github.com/invisibook-lab/invisibook/pull/1
- 2026-05-25 04:45:08 CST | truthixify | [CKB Action Links: a draft protocol for shareable CKB transaction URLs](https://talk.nervos.org/t/ckb-action-links-a-draft-protocol-for-shareable-ckb-transaction-urls/10315/1) | Hi all - sharing an early draft of CKB Action Links, a protocol that lets anyone publish a CKB transaction intent as a URL. A user clicks the link, their wallet renders a...
- 2026-05-25 03:52:02 CST | HNO3Miracle | [Spark Program | CKB-UGMP —— A Universal Spore/DOB Seamless Minting Infrastructure Prototype on CKB —— 基于 CKB 的通用 Spore/DOB 无感铸造基础设施原型](https://talk.nervos.org/t/spark-program-ckb-ugmp-a-universal-spore-dob-seamless-minting-infrastructure-prototype-on-ckb-ckb-spore-dob/10098/24) | 各位好，和各位分享复现步骤以及上周进度。 复现步骤 进入页面，点击连接钱包，根据步骤登录 joyid ckb 测试网钱包，会显示Address 还有 Capacity，即为连接成功。 选择图片资源，点击上传到 IPFS，上传成功后 CID，点击 Gateway 的网址可以正常访问脸上的图片。 点击 Mine DOB，即可把预览 JSON 上链，在...
