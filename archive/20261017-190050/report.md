# Nervos Talk 社区简报

- 统计窗口: 2026-10-17 03:00:50 CST 到 2026-10-18 03:00:50 CST
- 生成时间: 2026-10-18 03:00:55 CST
- 话题数: 4
- 帖子数: 6
- 作者数: 5
- 总结模式: ai:openai-compatible

## 社区总结

## 今日发生了什么

过去一天论坛最集中的讨论是 Metaforo 投票快照绑定问题：有用户称自己在 Nervos DAO 存入超过 10 万 CKB、Neuron 地址也已绑定 Metaforo，但投票/点赞活跃提案时仍报错 [S01]。随后有社区成员判断可能是绑定交易选错，或误用了 inputs 而不是 outputs，并表示可提供分步指导 [S02]；提问者回应会私信联系 [S03]。RIVET 提案线程公布投票已通过，批准率 52.82%，总投票权重 244,888,704 CKB，并称已用 CKB DAO Watchdog 完成投票后核验 [S04]。Spark Program 下新增 MatchLock 提案 [S05]，Corven cloud-native IDE 线程则补充了 CKB Kisumu Workshop 2026 的照片和视频材料 [S06]。

## 重点话题

- Metaforo 投票绑定求助：用户有 10 万以上 CKB 在 Nervos DAO，但无法对活跃提案投票/点赞 [S01]；社区初步把原因指向绑定交易或 inputs/outputs 选择问题 [S02]，双方已转私信继续沟通 [S03]。
- RIVET 投票结果：线程公布提案以 52.82% 批准率、244,888,704 CKB 总投票权重通过，并称投票后核验已完成 [S04]。
- MatchLock 新提案：Spark Program 下出现一个可复用的 CKB lock/type script 库提案，目标是让项目加入 private-until-match/reveal 双边承诺与原子条件结算 [S05]。
- Corven IDE 补充材料：Corven cloud-native IDE 提案线程里，作者提供了 CKB Kisumu Workshop 2026 的照片画廊和视频，用于记录活动与社区参与 [S06]。

## 值得继续跟进

- Metaforo 快照绑定失败的具体原因尚未在帖中确认，后续私信沟通结果以及是否影响 DAO 投票/点赞体验值得观察 [S01, S02, S03]。
- RIVET 已公布通过和核验完成，后续可关注该结果是否获得进一步社区确认，以及线程是否更新后续进展 [S04]。
- MatchLock 与 Corven IDE 都处在 Spark Program 提案/材料补充阶段，后续讨论、评审反馈和是否推进值得跟进 [S05, S06]。

## 来源索引

- `S01` [Unable to vote/like active proposal — Nervos DAO snapshot behavior on Metaforo](https://talk.nervos.org/t/unable-to-vote-like-active-proposal-nervos-dao-snapshot-behavior-on-metaforo/11004/1) | SalmanDev | 2026-10-17 04:03:41 CST | Hi everyone, I have a technical question regarding Metaforo voting snapshot rules: I currently have over 100,000 CKB deposited into the Nervos DAO via my Neuron wallet. My Neuron wallet address is bound to my Metaforo account. However, I receive an error when attempting to...
- `S02` [Unable to vote/like active proposal — Nervos DAO snapshot behavior on Metaforo](https://talk.nervos.org/t/unable-to-vote-like-active-proposal-nervos-dao-snapshot-behavior-on-metaforo/11004/2) | Jedi_dtechmaker | 2026-10-17 07:24:05 CST | GM chief, I think you might have binded the wrong transaction. Or you used inputs for sign in, instead of outputs. I experienced similar issues too when I was trying to bind my wallet. Happy to help out if you need a step by step guide on that chief​
- `S03` [Unable to vote/like active proposal — Nervos DAO snapshot behavior on Metaforo](https://talk.nervos.org/t/unable-to-vote-like-active-proposal-nervos-dao-snapshot-behavior-on-metaforo/11004/3) | SalmanDev | 2026-10-17 23:57:12 CST | Thanks, I will dm you.
- `S04` [[DIS] RIVET: Decentralized GitHub Backup, Timestamping and Restore on CKB](https://talk.nervos.org/t/dis-rivet-decentralized-github-backup-timestamping-and-restore-on-ckb/10739/13) | zz_tovarishch | 2026-10-17 14:01:31 CST | Based on the Metaforo tally at close, the outcome is PASSED. Approval is 52.82% with total voting weight 244,888,704 CKB. Post-close verification has been completed using CKB DAO Watchdog (GitHub - CKBFansDAO/ckb-dao-watchdog: Community-driven tools for auditing and verifying...
- `S05` [Spark Program | MatchLock: A Reusable Script Primitive for Private-Until-Match Bilateral Settlement on CKB](https://talk.nervos.org/t/spark-program-matchlock-a-reusable-script-primitive-for-private-until-match-bilateral-settlement-on-ckb/11005/1) | Chaichamp | 2026-10-17 12:38:40 CST | 1. Overview Project name: MatchLock One-sentence summary: A permissively licensed CKB lock/type script library, with an SDK and documentation, that lets any CKB project add private-until-match/reveal bilateral commitments and atomic conditional settlement to its own...
- `S06` [Spark Program Proposal: Corven cloud-native IDE](https://talk.nervos.org/t/spark-program-proposal-corven-cloud-native-ide/10807/5) | lestonEth | 2026-10-17 04:24:49 CST | GM @xingtianchunyan, Here is the media evidence from the CKB Kisumu Workshop 2026, documenting the event and community engagement activities. Workshop photo gallery: Pixieset CKB Kisumu Workshop Photo collection by aten studios ke Workshop video: The video highlights Corven...

## 活跃话题

1. [Unable to vote/like active proposal — Nervos DAO snapshot behavior on Metaforo](https://talk.nervos.org/t/unable-to-vote-like-active-proposal-nervos-dao-snapshot-behavior-on-metaforo/11004) | 3 条近窗帖子 | 最新活动 2026-10-17 23:57:12 CST
2. [[DIS] RIVET: Decentralized GitHub Backup, Timestamping and Restore on CKB](https://talk.nervos.org/t/dis-rivet-decentralized-github-backup-timestamping-and-restore-on-ckb/10739) | 1 条近窗帖子 | 最新活动 2026-10-17 14:01:31 CST | tags: CKB
3. [Spark Program | MatchLock: A Reusable Script Primitive for Private-Until-Match Bilateral Settlement on CKB](https://talk.nervos.org/t/spark-program-matchlock-a-reusable-script-primitive-for-private-until-match-bilateral-settlement-on-ckb/11005) | 1 条近窗帖子 | 最新活动 2026-10-17 12:38:40 CST | tags: appchain
4. [Spark Program Proposal: Corven cloud-native IDE](https://talk.nervos.org/t/spark-program-proposal-corven-cloud-native-ide/10807) | 1 条近窗帖子 | 最新活动 2026-10-17 04:24:49 CST | tags: CKB, Grant, Pending, Spark-Program

## 最近帖子摘录

- 2026-10-17 23:57:12 CST | SalmanDev | [Unable to vote/like active proposal — Nervos DAO snapshot behavior on Metaforo](https://talk.nervos.org/t/unable-to-vote-like-active-proposal-nervos-dao-snapshot-behavior-on-metaforo/11004/3) | Thanks, I will dm you.
- 2026-10-17 14:01:31 CST | zz_tovarishch | [[DIS] RIVET: Decentralized GitHub Backup, Timestamping and Restore on CKB](https://talk.nervos.org/t/dis-rivet-decentralized-github-backup-timestamping-and-restore-on-ckb/10739/13) | Based on the Metaforo tally at close, the outcome is PASSED. Approval is 52.82% with total voting weight 244,888,704 CKB. Post-close verification has been completed using CKB...
- 2026-10-17 12:38:40 CST | Chaichamp | [Spark Program | MatchLock: A Reusable Script Primitive for Private-Until-Match Bilateral Settlement on CKB](https://talk.nervos.org/t/spark-program-matchlock-a-reusable-script-primitive-for-private-until-match-bilateral-settlement-on-ckb/11005/1) | 1. Overview Project name: MatchLock One-sentence summary: A permissively licensed CKB lock/type script library, with an SDK and documentation, that lets any CKB project add...
- 2026-10-17 07:24:05 CST | Jedi_dtechmaker | [Unable to vote/like active proposal — Nervos DAO snapshot behavior on Metaforo](https://talk.nervos.org/t/unable-to-vote-like-active-proposal-nervos-dao-snapshot-behavior-on-metaforo/11004/2) | GM chief, I think you might have binded the wrong transaction. Or you used inputs for sign in, instead of outputs. I experienced similar issues too when I was trying to bind my...
- 2026-10-17 04:24:49 CST | lestonEth | [Spark Program Proposal: Corven cloud-native IDE](https://talk.nervos.org/t/spark-program-proposal-corven-cloud-native-ide/10807/5) | GM @xingtianchunyan, Here is the media evidence from the CKB Kisumu Workshop 2026, documenting the event and community engagement activities. Workshop photo gallery: Pixieset...
- 2026-10-17 04:03:41 CST | SalmanDev | [Unable to vote/like active proposal — Nervos DAO snapshot behavior on Metaforo](https://talk.nervos.org/t/unable-to-vote-like-active-proposal-nervos-dao-snapshot-behavior-on-metaforo/11004/1) | Hi everyone, I have a technical question regarding Metaforo voting snapshot rules: I currently have over 100,000 CKB deposited into the Nervos DAO via my Neuron wallet. My...
