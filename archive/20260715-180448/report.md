# Nervos Talk 社区简报

- 统计窗口: 2026-07-15 02:04:48 CST 到 2026-07-16 02:04:48 CST
- 生成时间: 2026-07-16 02:04:54 CST
- 话题数: 8
- 帖子数: 10
- 作者数: 8
- 总结模式: ai:openrouter

## 社区总结

## 今日发生了什么

今天 Nervos Talk 上 Fiber 生态非常活跃，出现了两个新的支付基础设施项目提案：FiberPass 提出预付费、可撤销的 Fiber 支付会话方案，Trickle 则带来了预算上限的流式微支付方案 [S01, S03]。同时，Cellar 和 CKB Appchain Kit 两个 Spark 资助项目也相继亮相，分别瞄准 CKB 存储容量租赁市场和应用链开发工具 [S04, S10]。

## 重点话题

- **FiberPass 发布预付费支付会话基础设施**：XBeach 提出了一套钱包与支付 UX 基础设施，让用户一次授权消费额度后，商户可在 Fiber Network 上按需扣款，且用户可随时撤销授权，旨在改善重复小额支付的体验 [S01]。社区成员 knmo 随即提醒要注意后端 API 和邮件等中心化组件的历史关停风险 [S02]。

- **Trickle 亮相黑客松：流式微支付新方案**：T_Silva 发布了 Trickle，支持为内容消费等场景设置预算上限的实时流式付款，按用量逐秒扣费，用不完可退款，目前已完成 Scryve 链上存证 [S03]。

- **Cellar 申请 Spark 资助，要做 CKB 存储容量租赁市场**：Carlos_Bunny 提案做一个协议，让闲置 CKB 持有者把链上存储容量出租给需要便宜 Cell 空间的开发者，申请 1000 美元资助 [S04]。

- **CKB Appchain Kit 发布 MVP**：Cipher_Kage 推出本地 CKB 锚定应用链的一键启动工具，包含链配置生成、验证器设置、CKB 开发网集成和检查点交易等功能 [S10]。

- **RGB++ BTC 索引器选型引发技术讨论**：fgh 详细分析了现有 btc-assets-api 的局限，指出其缺乏资产维度索引、聚合能力弱、性能一般等问题，为后续索引器选型提供调研基础 [S05]。

## 值得继续跟进

- **Fiber 支付层竞争格局**：FiberPass 和 Trickle 同日出现，加上此前 fiber-pay 已支持 UDT 操作 [S06]，Fiber 生态的支付 UX 基础设施正在快速分化，需观察哪些方案能获得实际采用和协议级整合。

- **ckbfiber.net 链接失效的后续**：社区发现测试网浏览器页眉的官网链接指向失效域名，RetricSu 已提交 PR 修复 [S07, S08]，需确认合并进度及是否还有其他过期引用。

- **Spark 项目交付与资金效率**：Cellar 和 CKB Appchain Kit 均为小额资助请求（1000 美元级别），后续需跟踪其开发进度和实际可用性，评估 Spark 机制对基础设施项目的催化效果 [S04, S10]。

## 来源索引

- `S01` [FiberPass: Prepaid, Revocable Payment Sessions for Fiber Network](https://talk.nervos.org/t/fiberpass-prepaid-revocable-payment-sessions-for-fiber-network/10491/1) | XBeach | 2026-07-15 16:20:30 CST | Hello CKB and Fiber community, I’m sharing FiberPass for early ecosystem validation and technical feedback. FiberPass is wallet and payment UX infrastructure for prepaid, revocable Fiber Network payment sessions. It allows users to approve a spending limit once, while...
- `S02` [FiberPass: Prepaid, Revocable Payment Sessions for Fiber Network](https://talk.nervos.org/t/fiberpass-prepaid-revocable-payment-sessions-for-fiber-network/10491/2) | knmo | 2026-07-15 23:33:24 CST | Backend (API, Email…) We’ve seen too many centralized implementations in the past that were shut down.
- `S03` [Trickle: Budget-Capped Streaming Micropayments for Fiber Network](https://talk.nervos.org/t/trickle-budget-capped-streaming-micropayments-for-fiber-network/10493/1) | T_Silva | 2026-07-15 18:48:21 CST | Hey everyone, sharing Trickle, my submission for the hackathon, and looking for feedback from people building on Fiber. trickle-1a924×540 13.6 KB Authorship Sealed on Scryve. You can seal your work too, proving you wrote it and preserving it permanently on-chain. 1. The...
- `S04` [Spark Program | Cellar — A Capacity Leasing Market for CKB Cells](https://talk.nervos.org/t/spark-program-cellar-a-capacity-leasing-market-for-ckb-cells/10492/1) | Carlos_Bunny | 2026-07-15 18:39:06 CST | One-line summary A protocol that lets idle CKB holders lease their token’s on-chain storage capacity to developers who need cheap cell space Project type Developer infrastructure / protocol (lock script + SDK + CLI + demo dApp) Requested funding $1,000 USD Payment preference...
- `S05` [面向 RGB++ 的 BTC Indexer 选型调研](https://talk.nervos.org/t/rgb-btc-indexer/10490/1) | fgh | 2026-07-15 12:53:04 CST | 背景 RGB++ 目前没有协议级的索引器。应用侧可用的是 btc-assets-api，它的接口提供了部分索引能力，但实际使用中它的问题比较明显： 查询维度只有 BTC 地址和 outpoint 两种，没有资产维度的能力。给定一种 UDT，查不到持有地址数、持有地址列表、资产维度的流转记录这类数据。它的实现是从地址的 BTC UTXO 正向映射到 CKB Cell，没有维护反向的资产索引。 聚合能力弱、性能一般。 BTC 数据源是自部署的 mempool/electrs 和 mempool.space API，两者的按地址查询 UTXO 均受到...
- `S06` [Fiber-pay: an ai-friendly CLI for fiber-network](https://talk.nervos.org/t/fiber-pay-an-ai-friendly-cli-for-fiber-network/9974/11) | RetricSu | 2026-07-15 10:39:13 CST | Hi community, the fiber-pay v0.3.0 has been rolled out. We support UDT operation like openning udt channels in all the levels of SDKs and CLI in fiber-pay so it is a bit more useful. Also, the react components and our landing page and the online demo has been refactor so it...
- `S07` [Ckbfiber.net Offline?](https://talk.nervos.org/t/ckbfiber-net-offline/10489/1) | knmo | 2026-07-15 06:15:15 CST | The website is linked in the header of the testnet block explorer. https://www.ckbfiber.net offline?
- `S08` [Ckbfiber.net Offline?](https://talk.nervos.org/t/ckbfiber-net-offline/10489/2) | RetricSu | 2026-07-15 07:26:09 CST | the officail website is https://www.fiber.world/ seems explorer is oudated. will fire a PR to fix that. Update: fix: update fiber official website link by humble-little-bear · Pull Request #2137 · nervosnetwork/ckb-explorer-frontend · GitHub
- `S09` [[DIS] Vellum: Reputation Extension on did:ckb](https://talk.nervos.org/t/dis-vellum-reputation-extension-on-did-ckb/10419/9) | truthixify | 2026-07-15 04:17:03 CST | Thanks @neon.bit and @CDEX for the follow-up. On the ckb:did point, Vellum is itself the proof that this protocol works as an open primitive. The web5fans team shipped the contracts, WIP-01, and a reference implementation, deployed to mainnet late last year. Vellum takes that...
- `S10` [Spark Program | CKB Appchain Kit MVP](https://talk.nervos.org/t/spark-program-ckb-appchain-kit-mvp/10488/1) | Cipher_Kage | 2026-07-15 02:42:49 CST | Spark Program | CKB Appchain Kit MVP Project Overview Project Name: CKB Appchain Kit One-Sentence Summary: A developer tool that makes it easy to launch a local CKB-anchored appchain with generated chain config, validator setup, CKB devnet integration, checkpoint transactions,...

## 活跃话题

1. [FiberPass: Prepaid, Revocable Payment Sessions for Fiber Network](https://talk.nervos.org/t/fiberpass-prepaid-revocable-payment-sessions-for-fiber-network/10491) | 2 条近窗帖子 | 最新活动 2026-07-15 23:33:24 CST | tags: fiber
2. [Trickle: Budget-Capped Streaming Micropayments for Fiber Network](https://talk.nervos.org/t/trickle-budget-capped-streaming-micropayments-for-fiber-network/10493) | 1 条近窗帖子 | 最新活动 2026-07-15 18:48:21 CST | tags: CKB, Hackathlon, fiber
3. [Spark Program | Cellar — A Capacity Leasing Market for CKB Cells](https://talk.nervos.org/t/spark-program-cellar-a-capacity-leasing-market-for-ckb-cells/10492) | 1 条近窗帖子 | 最新活动 2026-07-15 18:39:06 CST | tags: Spark-Program
4. [面向 RGB++ 的 BTC Indexer 选型调研](https://talk.nervos.org/t/rgb-btc-indexer/10490) | 1 条近窗帖子 | 最新活动 2026-07-15 12:53:04 CST | tags: RGBpp
5. [Fiber-pay: an ai-friendly CLI for fiber-network](https://talk.nervos.org/t/fiber-pay-an-ai-friendly-cli-for-fiber-network/9974) | 1 条近窗帖子 | 最新活动 2026-07-15 10:39:13 CST | tags: CKB
6. [Ckbfiber.net Offline?](https://talk.nervos.org/t/ckbfiber-net-offline/10489) | 2 条近窗帖子 | 最新活动 2026-07-15 07:26:09 CST
7. [[DIS] Vellum: Reputation Extension on did:ckb](https://talk.nervos.org/t/dis-vellum-reputation-extension-on-did-ckb/10419) | 1 条近窗帖子 | 最新活动 2026-07-15 04:17:03 CST | tags: CKB, dapp, testnet
8. [Spark Program | CKB Appchain Kit MVP](https://talk.nervos.org/t/spark-program-ckb-appchain-kit-mvp/10488) | 1 条近窗帖子 | 最新活动 2026-07-15 02:42:49 CST | tags: Spark-Program

## 最近帖子摘录

- 2026-07-15 23:33:24 CST | knmo | [FiberPass: Prepaid, Revocable Payment Sessions for Fiber Network](https://talk.nervos.org/t/fiberpass-prepaid-revocable-payment-sessions-for-fiber-network/10491/2) | Backend (API, Email…) We’ve seen too many centralized implementations in the past that were shut down.
- 2026-07-15 18:48:21 CST | T_Silva | [Trickle: Budget-Capped Streaming Micropayments for Fiber Network](https://talk.nervos.org/t/trickle-budget-capped-streaming-micropayments-for-fiber-network/10493/1) | Hey everyone, sharing Trickle, my submission for the hackathon, and looking for feedback from people building on Fiber. trickle-1a924×540 13.6 KB Authorship Sealed on Scryve....
- 2026-07-15 18:39:06 CST | Carlos_Bunny | [Spark Program | Cellar — A Capacity Leasing Market for CKB Cells](https://talk.nervos.org/t/spark-program-cellar-a-capacity-leasing-market-for-ckb-cells/10492/1) | One-line summary A protocol that lets idle CKB holders lease their token’s on-chain storage capacity to developers who need cheap cell space Project type Developer...
- 2026-07-15 16:20:30 CST | XBeach | [FiberPass: Prepaid, Revocable Payment Sessions for Fiber Network](https://talk.nervos.org/t/fiberpass-prepaid-revocable-payment-sessions-for-fiber-network/10491/1) | Hello CKB and Fiber community, I’m sharing FiberPass for early ecosystem validation and technical feedback. FiberPass is wallet and payment UX infrastructure for prepaid,...
- 2026-07-15 12:53:04 CST | fgh | [面向 RGB++ 的 BTC Indexer 选型调研](https://talk.nervos.org/t/rgb-btc-indexer/10490/1) | 背景 RGB++ 目前没有协议级的索引器。应用侧可用的是 btc-assets-api，它的接口提供了部分索引能力，但实际使用中它的问题比较明显： 查询维度只有 BTC 地址和 outpoint 两种，没有资产维度的能力。给定一种 UDT，查不到持有地址数、持有地址列表、资产维度的流转记录这类数据。它的实现是从地址的 BTC UTXO 正向映射到...
- 2026-07-15 10:39:13 CST | RetricSu | [Fiber-pay: an ai-friendly CLI for fiber-network](https://talk.nervos.org/t/fiber-pay-an-ai-friendly-cli-for-fiber-network/9974/11) | Hi community, the fiber-pay v0.3.0 has been rolled out. We support UDT operation like openning udt channels in all the levels of SDKs and CLI in fiber-pay so it is a bit more...
- 2026-07-15 07:26:09 CST | RetricSu | [Ckbfiber.net Offline?](https://talk.nervos.org/t/ckbfiber-net-offline/10489/2) | the officail website is https://www.fiber.world/ seems explorer is oudated. will fire a PR to fix that. Update: fix: update fiber official website link by humble-little-bear ·...
- 2026-07-15 06:15:15 CST | knmo | [Ckbfiber.net Offline?](https://talk.nervos.org/t/ckbfiber-net-offline/10489/1) | The website is linked in the header of the testnet block explorer. https://www.ckbfiber.net offline?
- 2026-07-15 04:17:03 CST | truthixify | [[DIS] Vellum: Reputation Extension on did:ckb](https://talk.nervos.org/t/dis-vellum-reputation-extension-on-did-ckb/10419/9) | Thanks @neon.bit and @CDEX for the follow-up. On the ckb:did point, Vellum is itself the proof that this protocol works as an open primitive. The web5fans team shipped the...
- 2026-07-15 02:42:49 CST | Cipher_Kage | [Spark Program | CKB Appchain Kit MVP](https://talk.nervos.org/t/spark-program-ckb-appchain-kit-mvp/10488/1) | Spark Program | CKB Appchain Kit MVP Project Overview Project Name: CKB Appchain Kit One-Sentence Summary: A developer tool that makes it easy to launch a local CKB-anchored...
