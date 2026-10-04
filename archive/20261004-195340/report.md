# Nervos Talk 社区简报

- 统计窗口: 2026-10-04 03:53:40 CST 到 2026-10-05 03:53:40 CST
- 生成时间: 2026-10-05 03:53:45 CST
- 话题数: 3
- 帖子数: 3
- 作者数: 2
- 总结模式: ai:openai-compatible

## 社区总结

## 今日发生了什么
按给定材料中的 10 月 4 日更新，Nervos Talk 今天的主要动静集中在 ZK/CellScript：ArthurZhang 宣布 CellScript 已支持面向 CKB 状态转换的 BN254 Groth16 证明 [S01]。同一天，他还说明已把 CellScript counter 通过 Spawn/IPC/Wait 接到 Groth16 verifier，并在本地 CKB 节点跑过创建、两次更新和重放拒绝 [S03]。另一条更新来自 Tinder 版预测市场应用帖子，回复者表示自己不懂技术，但希望贡献灵感，并期待 CKB 早日出现 mass adoption 应用 [S02]。今天可引用的社区内容不多，整体较平静，主线明显是 ZK 实验进展 [S01, S02, S03]。

## 重点话题
- CellScript 宣布支持 Groth16 over BN254，用于 CKB 状态转换 [S01]。
- 配套已有可工作的 counter 应用，以及 Rust 和 TypeScript 客户端；测试在 CKB-VM 中运行 verifier，并在一次性本地环境确认交易 [S01]。
- ArthurZhang 进一步把 CellScript counter 接到 Groth16 verifier，链路走 Spawn/IPC/Wait，并使用真实 secret-knowledge circuit 和 pinned VK [S03]。
- 该集成在本地 CKB 节点通过了创建、两次更新和重放拒绝，但 key 使用 single-party setup，且尚未部署 [S03]。
- 社区另有一条偏灵感型回复，围绕 Tinder 版预测市场应用，表达对 mass adoption 应用的期待 [S02]。

## 值得继续跟进
- 关注该 Groth16/CellScript 方案是否从本地测试走向实际部署；当前作者明确说尚未部署 [S03]。
- 当前 key 使用 single-party setup，后续是否调整这一设置值得观察 [S03]。
- 关注 CKB 上 ZK 工具链和示例应用后续是否继续更新，例如 counter、Rust/TypeScript 客户端 [S01, S03]。
- 关注 Tinder 版预测市场应用想法是否会出现后续技术讨论或推进 [S02]。

## 来源索引

- `S01` [Build a ZK counter on CKB with CellScript](https://talk.nervos.org/t/build-a-zk-counter-on-ckb-with-cellscript/10805/1) | ArthurZhang | 2026-10-04 23:03:50 CST | I am actually a bit excited to say, now CellScript supports Groth16 proofs over BN254 for CKB state transitions. We have a working counter application, Rust and TypeScript clients, and tests that exercise the verifier in CKB-VM and confirm transactions on a disposable local...
- `S02` [分享一个 Tinder 版预测市场应用的想法](https://talk.nervos.org/t/tinder/10407/3) | Fisher | 2026-10-04 18:06:47 CST | 感谢打捞，不懂技术，纯尝试贡献灵感，希望 ckb 早日诞生 mass adoption 的应用
- `S03` [Research Notes: What Zero-Knowledge Proofs Enable on CKB](https://talk.nervos.org/t/research-notes-what-zero-knowledge-proofs-enable-on-ckb/10368/11) | ArthurZhang | 2026-10-04 16:00:35 CST | ok I’ve now wired a CellScript counter to your Groth16 verifier through Spawn/IPC/Wait, with a real secret-knowledge circuit and a pinned VK. It passed creation, two updates and replay rejection on a local CKB node; the key uses a single-party setup, and I haven’t deployed it...

## 活跃话题

1. [Build a ZK counter on CKB with CellScript](https://talk.nervos.org/t/build-a-zk-counter-on-ckb-with-cellscript/10805) | 1 条近窗帖子 | 最新活动 2026-10-04 23:03:50 CST | tags: CellScript
2. [分享一个 Tinder 版预测市场应用的想法](https://talk.nervos.org/t/tinder/10407) | 1 条近窗帖子 | 最新活动 2026-10-04 18:06:47 CST | tags: lang-zh
3. [Research Notes: What Zero-Knowledge Proofs Enable on CKB](https://talk.nervos.org/t/research-notes-what-zero-knowledge-proofs-enable-on-ckb/10368) | 1 条近窗帖子 | 最新活动 2026-10-04 16:00:35 CST | tags: CKB-VM, architecture, groth16, lang-en, sp1, zero-knowledge, zkvm

## 最近帖子摘录

- 2026-10-04 23:03:50 CST | ArthurZhang | [Build a ZK counter on CKB with CellScript](https://talk.nervos.org/t/build-a-zk-counter-on-ckb-with-cellscript/10805/1) | I am actually a bit excited to say, now CellScript supports Groth16 proofs over BN254 for CKB state transitions. We have a working counter application, Rust and TypeScript...
- 2026-10-04 18:06:47 CST | Fisher | [分享一个 Tinder 版预测市场应用的想法](https://talk.nervos.org/t/tinder/10407/3) | 感谢打捞，不懂技术，纯尝试贡献灵感，希望 ckb 早日诞生 mass adoption 的应用
- 2026-10-04 16:00:35 CST | ArthurZhang | [Research Notes: What Zero-Knowledge Proofs Enable on CKB](https://talk.nervos.org/t/research-notes-what-zero-knowledge-proofs-enable-on-ckb/10368/11) | ok I’ve now wired a CellScript counter to your Groth16 verifier through Spawn/IPC/Wait, with a real secret-knowledge circuit and a pinned VK. It passed creation, two updates and...
