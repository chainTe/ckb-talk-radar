# Nervos Talk 社区简报

- 统计窗口: 2026-09-16 03:50:31 CST 到 2026-09-17 03:50:31 CST
- 生成时间: 2026-09-17 03:50:37 CST
- 话题数: 6
- 帖子数: 10
- 作者数: 6
- 总结模式: ai:openai-compatible

## 社区总结

## 今日发生了什么
从提供的材料看，今天 Nervos Talk 有多个项目更新和反馈互动，整体以进展同步为主 [S01, S04, S05, S06, S08]。最显眼的是 Dular 宣布 Phase 1 完成，并新开帖分享在 Fiber 上服务移动货币用户时学到的经验 [S04]。Spark Program 的 zk-Lock for CKB 更新了 M3 收尾进展，CI 的 GitHub billing hold 已清除，circuit-vk-hash 现在每次 push 都会运行 [S01]。同时 noir-ckb 方向讨论继续，CKBA 更新了贡献会员申请窗口关闭和收到 5 份申请的情况 [S05, S06]。

## 重点话题
- Dular Phase 1 完成：作者说不想只总结交付物，而是要分享为真实移动货币用户在 Fiber 上构建时学到的经验，包括不舒服的发现 [S04]。随后在 Spark Program 帖中补充，已分享 loops vs wallets、缺失身份层、真实利润点和下一步要解决的离线接收者问题 [S03]。
- Spark Program zk-Lock 更新：作者表示已解决并收尾上次更新时剩余事项，M3 正在完全关闭 [S01]。CI 方面，GitHub billing hold 已清除，circuit-vk-hash 现在每次 push 都会运行 [S01]。
- noir-ckb 方向讨论：作者回帖认同 Type script 也会限制花费，并强调 Lock 和 Type 的区别不在谁能拒绝交易，而在执行范围与责任 [S05]。
- CKBA 会员流程：当前 Contributing Member 申请窗口已于 2026 年 6 月 15 日 AOE 关闭，本轮收到 5 份申请 [S06]。所有申请者已被单独联系确认 [S06]。
- SkillPass 反馈：有用户简短回复“good stuff”，作者感谢指导并同意把帖子移到更合适分类 [S07, S08]。作者还表示会继续用该线程收集技术和产品反馈，同时在 CKB Testnet 上改进原型并测试模型 [S08]。期间有一条作者删除的帖子 [S09]。

## 值得继续跟进
- Dular 提出的离线接收者问题、缺失身份层和 loops vs wallets 等方向，后续是否形成具体方案或收到社区反驳，值得观察 [S03, S04]。
- Spark Program 中 Dular 线程有人询问更新，但在提供材料里未见后续回应，zk-Lock 的 M3 收尾后下一步进展也值得继续看 [S02, S01]。
- noir-ckb 关于 Lock/Type Script 执行范围与责任的讨论，以及 SkillPass 在 CKB Testnet 的原型测试和反馈收集，是否推进到下一阶段，值得跟进 [S05, S08]。CKBA 申请者确认后的后续流程也值得观察 [S06]。

## 来源索引

- `S01` [Spark Program | zk-Lock for CKB](https://talk.nervos.org/t/spark-program-zk-lock-for-ckb/10448/18) | Mulandi_Cecilia | 2026-09-17 03:09:48 CST | Hello @xingtianchunyan, Look who is taking the “no late nights” advice seriously today :). An update on fully closing M3 I have resolved and wrapped up what was remaining when I last gave an update. CI: the GitHub billing hold cleared. circuit-vk-hash now runs on every push...
- `S02` [Spark Program | Dular](https://talk.nervos.org/t/spark-program-dular/10212/39) | duongja | 2026-09-16 17:27:12 CST | Hello @xingtianchunyan , any updates?
- `S03` [Spark Program | Dular](https://talk.nervos.org/t/spark-program-dular/10212/40) | duongja | 2026-09-16 22:46:13 CST | I’ve also shared our founder findings from building this, loops vs wallets, the missing identity layer, where the real margins are, and the offline-receiver problem we’re tackling next here: link Built from our pilot, written for Fiber/CKB builders. Pushback welcome,...
- `S04` [Dular: What mobile-money users taught us building on fiber](https://talk.nervos.org/t/dular-what-mobile-money-users-taught-us-building-on-fiber/10717/1) | duongja | 2026-09-16 22:40:04 CST | Dular Phase 1 is complete, and I want to use this post differently: not to summarize deliverables, but to share what building on Fiber for real mobile-money users actually taught us. Founder findings, including the uncomfortable ones. If you’re building payments on Fiber or...
- `S05` [Direction check: should noir-ckb generate CKB Type Scripts from Noir circuits?](https://talk.nervos.org/t/direction-check-should-noir-ckb-generate-ckb-type-scripts-from-noir-circuits/10703/3) | xiaomao | 2026-09-16 18:54:25 CST | Thank you so much for the response! You’re right that the Type script also gates spending. All applicable script groups must pass, so the distinction is not that the Lock can reject a transaction while the Type cannot. It is about execution scope and responsibility: A Lock...
- `S06` [CKBA Membership Process](https://talk.nervos.org/t/ckba-membership-process/10340/11) | CKBAMembership | 2026-09-16 18:30:22 CST | Application window closed for the current Contributing Member cycle The application window for the current Contributing Member cycle has closed as of June 15, 2026 (AOE). 5 applications were received during this cycle. All applicants have been individually contacted to confirm...
- `S07` [SkillPass: Portable Service Rights on CKB — Looking for Community Feedback](https://talk.nervos.org/t/skillpass-portable-service-rights-on-ckb-looking-for-community-feedback/10706/3) | longdevbf | 2026-09-16 14:56:20 CST | good stuff
- `S08` [SkillPass: Portable Service Rights on CKB — Looking for Community Feedback](https://talk.nervos.org/t/skillpass-portable-service-rights-on-ckb-looking-for-community-feedback/10706/4) | Dangbaty2004 | 2026-09-16 16:05:19 CST | Thanks for the guidance and for moving the post to the more appropriate category. That makes sense at this stage. I’ll use this thread to collect technical and product feedback while I continue improving the prototype and testing the model on CKB Testnet. Once the project and...
- `S09` [SkillPass: Portable Service Rights on CKB — Looking for Community Feedback](https://talk.nervos.org/t/skillpass-portable-service-rights-on-ckb-looking-for-community-feedback/10706/5) | Dangbaty2004 | 2026-09-16 16:06:16 CST | (post deleted by author)
- `S10` [SkillPass: Portable Service Rights on CKB — Looking for Community Feedback](https://talk.nervos.org/t/skillpass-portable-service-rights-on-ckb-looking-for-community-feedback/10706/6) | Dangbaty2004 | 2026-09-16 16:07:58 CST | Thanks, really appreciate it!

## 活跃话题

1. [Spark Program | zk-Lock for CKB](https://talk.nervos.org/t/spark-program-zk-lock-for-ckb/10448) | 1 条近窗帖子 | 最新活动 2026-09-17 03:09:48 CST | tags: In-Progress
2. [Spark Program | Dular](https://talk.nervos.org/t/spark-program-dular/10212) | 2 条近窗帖子 | 最新活动 2026-09-16 22:46:13 CST | tags: In-Progress, Spark-Program, lang-en
3. [Dular: What mobile-money users taught us building on fiber](https://talk.nervos.org/t/dular-what-mobile-money-users-taught-us-building-on-fiber/10717) | 1 条近窗帖子 | 最新活动 2026-09-16 22:40:04 CST | tags: CKB, Spark-Program, dapp
4. [Direction check: should noir-ckb generate CKB Type Scripts from Noir circuits?](https://talk.nervos.org/t/direction-check-should-noir-ckb-generate-ckb-type-scripts-from-noir-circuits/10703) | 1 条近窗帖子 | 最新活动 2026-09-16 18:54:25 CST | tags: CKB, CKB-VM, zkp
5. [CKBA Membership Process](https://talk.nervos.org/t/ckba-membership-process/10340) | 1 条近窗帖子 | 最新活动 2026-09-16 18:30:22 CST | tags: CKBA, Membership, lang-en
6. [SkillPass: Portable Service Rights on CKB — Looking for Community Feedback](https://talk.nervos.org/t/skillpass-portable-service-rights-on-ckb-looking-for-community-feedback/10706) | 4 条近窗帖子 | 最新活动 2026-09-16 16:07:58 CST | tags: CKB, dapp, fiber, testnet

## 最近帖子摘录

- 2026-09-17 03:09:48 CST | Mulandi_Cecilia | [Spark Program | zk-Lock for CKB](https://talk.nervos.org/t/spark-program-zk-lock-for-ckb/10448/18) | Hello @xingtianchunyan, Look who is taking the “no late nights” advice seriously today :). An update on fully closing M3 I have resolved and wrapped up what was remaining when I...
- 2026-09-16 22:46:13 CST | duongja | [Spark Program | Dular](https://talk.nervos.org/t/spark-program-dular/10212/40) | I’ve also shared our founder findings from building this, loops vs wallets, the missing identity layer, where the real margins are, and the offline-receiver problem we’re...
- 2026-09-16 22:40:04 CST | duongja | [Dular: What mobile-money users taught us building on fiber](https://talk.nervos.org/t/dular-what-mobile-money-users-taught-us-building-on-fiber/10717/1) | Dular Phase 1 is complete, and I want to use this post differently: not to summarize deliverables, but to share what building on Fiber for real mobile-money users actually...
- 2026-09-16 18:54:25 CST | xiaomao | [Direction check: should noir-ckb generate CKB Type Scripts from Noir circuits?](https://talk.nervos.org/t/direction-check-should-noir-ckb-generate-ckb-type-scripts-from-noir-circuits/10703/3) | Thank you so much for the response! You’re right that the Type script also gates spending. All applicable script groups must pass, so the distinction is not that the Lock can...
- 2026-09-16 18:30:22 CST | CKBAMembership | [CKBA Membership Process](https://talk.nervos.org/t/ckba-membership-process/10340/11) | Application window closed for the current Contributing Member cycle The application window for the current Contributing Member cycle has closed as of June 15, 2026 (AOE). 5...
- 2026-09-16 17:27:12 CST | duongja | [Spark Program | Dular](https://talk.nervos.org/t/spark-program-dular/10212/39) | Hello @xingtianchunyan , any updates?
- 2026-09-16 16:07:58 CST | Dangbaty2004 | [SkillPass: Portable Service Rights on CKB — Looking for Community Feedback](https://talk.nervos.org/t/skillpass-portable-service-rights-on-ckb-looking-for-community-feedback/10706/6) | Thanks, really appreciate it!
- 2026-09-16 16:06:16 CST | Dangbaty2004 | [SkillPass: Portable Service Rights on CKB — Looking for Community Feedback](https://talk.nervos.org/t/skillpass-portable-service-rights-on-ckb-looking-for-community-feedback/10706/5) | (post deleted by author)
- 2026-09-16 16:05:19 CST | Dangbaty2004 | [SkillPass: Portable Service Rights on CKB — Looking for Community Feedback](https://talk.nervos.org/t/skillpass-portable-service-rights-on-ckb-looking-for-community-feedback/10706/4) | Thanks for the guidance and for moving the post to the more appropriate category. That makes sense at this stage. I’ll use this thread to collect technical and product feedback...
- 2026-09-16 14:56:20 CST | longdevbf | [SkillPass: Portable Service Rights on CKB — Looking for Community Feedback](https://talk.nervos.org/t/skillpass-portable-service-rights-on-ckb-looking-for-community-feedback/10706/3) | good stuff
