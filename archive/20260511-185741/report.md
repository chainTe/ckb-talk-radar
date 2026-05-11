# Nervos Talk 社区简报

- 统计窗口: 2026-05-11 02:57:41 CST 到 2026-05-12 02:57:41 CST
- 生成时间: 2026-05-12 02:57:53 CST
- 话题数: 9
- 帖子数: 39
- 作者数: 13
- 总结模式: ai:openrouter

## 社区总结

## 今日发生了什么

Nervos Talk 今天最热闹的讨论集中在协议金库（treasury）该不该立刻启动，以及如何启动 [S01, S05]。社区成员 jimi-winehouse 主张直接以中心化方式快速激活金库，把资源投放到高影响力项目上，不需要花一年时间去搞去中心化治理 [S05]；而 matt_ckb 则强调必须遵循定位文件（positioning paper）所代表的"社会契约"，这是网络参与者早已达成的共识 [S01, S06]。与此同时，几个 Grant 项目也在持续推进，包括 Spark Program 旗下的 Nervos Brain 和 Tiko 都发布了最新进展 [S07, S08]。

## 重点话题

- **协议金库激活路线之争愈加热烈**：jimi-winehouse 质疑所谓"社会契约"是否存在、是否是 2019 年的老文件在绑架当下决策 [S02]；Yeti 贴出了 RFC 0001 定位文件的链接和 4.6 Treasury 章节原文，证明金库机制确实白纸黑字写在协议定位里 [S03, S04]。matt_ckb 后续将相关讨论拆分成了独立话题帖 [S11]。

- **"原生稳定币"讨论出现分歧**：matt_ckb 认为运营稳定币和维护公共基础设施难以两全，且链上已有 USDI [S12]；yifenzi 则强烈主张基于 CKB/Fiber 做超额抵押稳定币，并详细描述了用 CCC 工具发币、UTXOSwap 建池的多签实施方案 [S13, S17]。双方对"native"一词的理解似乎存在翻译层面的偏差 [S15]。

- **Pocket Node 项目资金拨付遇阻**：Jnr6 追问 M3 里程碑为何迟迟未通过，zz_tovarishch 回应称已多次提醒委员会打款但尚未得到回复 [S18, S19]。

- **Nervos Brain 复盘 bad case**：IrisNeko 总结近期问题主要出在 prompt 设置过于保守、模型查资料不够积极，以及多库联合调用未触发，认为优化 prompt 和调用逻辑即可解决 [S07]。

- **Bitcoin Renegade 撤回并即将重提媒体提案**：作者确认正在撤回现有方案，会基于社区反馈重新提交 [S09]。joshyates1980 表示支持其现场活动的喜剧化推广方式 [S10]。

## 值得继续跟进

- 协议金库讨论已从"要不要激活"升级到"激活路径之争"——快速中心化启动 vs 严谨去中心化建设，两种路线的拉锯可能会持续数周，需要观察核心开发者和治理委员会的最终表态 [S05, S06]。

- Pocket Node 的资金延迟是委员会流程问题还是项目验收问题，目前信息不足 [S18, S19]，若持续停滞可能影响 Android 轻客户端的交付节奏。

- 原生稳定币的争论表面是方案之争，实际涉及 Nervos 生态是否应亲自下场做稳定币基础设施，还是让第三方自由竞争，这一分歧尚未弥合 [S12, S13, S15]。

## 来源索引

- `S01` [Discussion about an alternative to the protocol treasury](https://talk.nervos.org/t/discussion-about-an-alternative-to-the-protocol-treasury/10246/8) | matt_ckb | 2026-05-11 13:03:43 CST | jimi-winehouse: Is the positioning paper a bible I wasn’t aware of? it is a social contract. Ultimately it is up to the participants in the network to activate it, however it needs to be built to fulfill the social contract that’s been created, this is just the nature of doing...
- `S02` [Discussion about an alternative to the protocol treasury](https://talk.nervos.org/t/discussion-about-an-alternative-to-the-protocol-treasury/10246/9) | jimi-winehouse | 2026-05-11 19:25:08 CST | It sounds like an appeal to authority, and a centralized one with the way you’re unwilling to discuss and provide good arguments for. Where is this “social contract” so I can read it, do we refer to some prehistorical 2019 paper? my question was half sarcastic half serious,...
- `S03` [Discussion about an alternative to the protocol treasury](https://talk.nervos.org/t/discussion-about-an-alternative-to-the-protocol-treasury/10246/10) | Yeti | 2026-05-11 19:37:24 CST | jimi-winehouse: can I get a link to this paper? https://github.com/nervosnetwork/rfcs/blob/master/rfcs/0001-positioning/0001-positioning.md
- `S04` [Discussion about an alternative to the protocol treasury](https://talk.nervos.org/t/discussion-about-an-alternative-to-the-protocol-treasury/10246/11) | Yeti | 2026-05-11 19:40:12 CST | 4.6 Treasury The portion of secondary issuance that doesn’t go to 1) miners or 2) long-term holders with tokens locked in the NervosDAO, will go toward a treasury fund. To demonstrate: if 60% of issued CKBytes are used to store state and 30% of the CKBytes are deposited into...
- `S05` [Discussion about an alternative to the protocol treasury](https://talk.nervos.org/t/discussion-about-an-alternative-to-the-protocol-treasury/10246/12) | jimi-winehouse | 2026-05-11 21:32:38 CST | the solution I am proposing is to activate the treasury and just make it centralized and focus on high impact projects. Taking a year of work to decentralized a treasury is resource mismanagement. The whole dilution thing is a meme, I was diluted 95% at least in usd terms by...
- `S06` [Discussion about an alternative to the protocol treasury](https://talk.nervos.org/t/discussion-about-an-alternative-to-the-protocol-treasury/10246/13) | matt_ckb | 2026-05-12 00:59:45 CST | image986×164 17.7 KB appreciate you engaging in this discussion, it seems like you have been around a while. It might be better to move to Nervos Nation or another chat forum to debate the merits of this work. This is not about being the best L1, it’s about fulfilling the...
- `S07` [Spark Program | Nervos Brain - A Global Developer Onboarding Engine and Cross-Language Hub Powered by Agentic RAG](https://talk.nervos.org/t/spark-program-nervos-brain-a-global-developer-onboarding-engine-and-cross-language-hub-powered-by-agentic-rag/9995/37) | IrisNeko | 2026-05-12 02:09:50 CST | 回顾近期的 bad case，主要原因是 prompt 设置过于保守：一方面表现为对用户频繁追问，另一方面是查资料不够积极。此外，上周的数据库问题也是因模型未触发多库联合调用引起的。总体来看，系统并没有严重的设计或架构问题，后续优化 prompt 和调用逻辑即可解决。
- `S08` [Spark Program | Tiko Creator Commerce Expansion + Private Beta Validation](https://talk.nervos.org/t/spark-program-tiko-creator-commerce-expansion-private-beta-validation/10231/3) | DWSQUIRES | 2026-05-12 01:23:41 CST | Updated. I narrowed the supported scope from 7 categories to the first 3 categories: Digital drops, Memberships/passes, and Limited editions/collectibles. I also added a detailed How to Verify section, including: access to the live test environment verification steps and...
- `S09` [[DIS] Bitcoin Renegade CKB Media Campaign](https://talk.nervos.org/t/dis-bitcoin-renegade-ckb-media-campaign/10239/31) | Bitcoin_Renegade | 2026-05-11 22:56:24 CST | Yes I am withdrawing my proposal and putting in a new one
- `S10` [[DIS] Bitcoin Renegade CKB Media Campaign](https://talk.nervos.org/t/dis-bitcoin-renegade-ckb-media-campaign/10239/32) | joshyates1980 | 2026-05-12 01:02:42 CST | As you fine tune your proposal with the plenty of feedback/suggestions from Nervos community, I do support your campaign and comical endeavors at live events which turn heads toward the Nervos booth, and so your knowledge base and personality can benefit the community.
- `S11` [Pre-RFC Discussion: Activating the Nervos DAO Treasury](https://talk.nervos.org/t/pre-rfc-discussion-activating-the-nervos-dao-treasury/10143/13) | matt_ckb | 2026-05-12 00:55:11 CST | 12 posts were split to a new topic: Discussion about an alternative to the protocol treasury
- `S12` [再谈CKB/Fiber支撑的原生稳定币的必要性和紧迫性](https://talk.nervos.org/t/ckb-fiber/10240/2) | matt_ckb | 2026-05-11 13:18:36 CST | Anything built on Fiber is built on CKB. There is already USDI but it is not mentioned ————————————————- ”One can not serve two masters” Operating a stablecoin (especially one that would be competitive against giants like USDC) and maintaining public infrastructure are two...
- `S13` [再谈CKB/Fiber支撑的原生稳定币的必要性和紧迫性](https://talk.nervos.org/t/ckb-fiber/10240/3) | yifenzi | 2026-05-11 14:45:53 CST | 希望你能表现出哪怕有一点点的专业性 一个Usdc本尊其价值都极小 更别说一个模仿的小小版Usdc 现在Uddc/Usdt的没进入是其自身的选择不是想进入被你们拒绝，你先搞清楚这个基本事实，不要一遍又一遍的让人笑话 而Dai的模仿者Rusd是一个很好的说明对象，但这个交易对流量池不应该由普通用户来建立也不应该有单独的盈利点存在，而需要在一个代币创建之初就考虑进去，更多的说明去看我已经发布的信息 我认为理解这个没有什么难度，需要做的只是有勇气面对它:放弃那份不该被独占的利益
- `S14` [再谈CKB/Fiber支撑的原生稳定币的必要性和紧迫性](https://talk.nervos.org/t/ckb-fiber/10240/4) | yifenzi | 2026-05-11 15:15:50 CST | 一个是中心化的，一个是去中心化的 一个是已有巨大影响力的，一个是需要很多人共用建立影响力的 这是肯定会一直存在的对立而又统一的两面，我们总会来到这样的路口然后需要做出自己的选择 那些选择中心化的，选择已有巨大影响力的，没问题，因为总有人选择去中心化选择很多人一起共同建立影响力的路 而中本聪就是其中一个开创者，他选的是后面的路，如果他选择的是前者那还有比特币吗？还有这个至少不是完全被传统金融控制的比之前好不少的个人金融时代吗？
- `S15` [再谈CKB/Fiber支撑的原生稳定币的必要性和紧迫性](https://talk.nervos.org/t/ckb-fiber/10240/5) | matt_ckb | 2026-05-11 15:39:36 CST | it’s good it is now clear that you are arguing for an overcollateralized stablecoin maybe we can blame this on the translation of “native” in the title
- `S16` [再谈CKB/Fiber支撑的原生稳定币的必要性和紧迫性](https://talk.nervos.org/t/ckb-fiber/10240/6) | Yeti | 2026-05-11 16:24:55 CST | yifenzi: As for RUSD, an imitator of DAI, it serves as a good illustrative example. However, the liquidity pool for this trading pair should not be established by ordinary users, nor should there be a separate profit point for it. Instead, it needs to be considered from the...
- `S17` [再谈CKB/Fiber支撑的原生稳定币的必要性和紧迫性](https://talk.nervos.org/t/ckb-fiber/10240/7) | yifenzi | 2026-05-11 16:29:56 CST | 我就来再次说下它的实现方式，大家会发现可以如此简单: 它在已经被实现的工程项目参照下完成 主要参考和工具: Ccc:发币 Utxoswap:交易对用来交换即铸造和赎回 Rusd:一个便于理解的对比对象 用一个多签地址(后面会说为何要多签以及其用处)用ccc工具发布一个代币比如UtxoUSD，数量任意一个极大数字比如100万亿 如果用CKB做价值背书就从其他地方转入CKB(用其他代币同理)，假设用CKB且假设转入100万美元的CKB 然后登陆Utxoswap把这100万亿UtxoUSD和100万美元的CKB提交新的交易对并把所有代币提供流动性...
- `S18` [[DIS] Mobile-Ready CKB Light Client (Pocket Node) for Android](https://talk.nervos.org/t/dis-mobile-ready-ckb-light-client-pocket-node-for-android/9879/40) | Jnr6 | 2026-05-11 14:43:44 CST | Hi @zz_tovarishch it’s close to a month, M4 currently in the pipeline and M3 haven’t been cleared. Is there a reason for the delay?
- `S19` [[DIS] Mobile-Ready CKB Light Client (Pocket Node) for Android](https://talk.nervos.org/t/dis-mobile-ready-ckb-light-client-pocket-node-for-android/9879/41) | zz_tovarishch | 2026-05-11 15:22:31 CST | 已经多次提醒committee打款，但目前尚未得到回复 请耐心等待，有消息会及时同步
- `S20` [Is there any good reason for allowing hidden profiles?](https://talk.nervos.org/t/is-there-any-good-reason-for-allowing-hidden-profiles/10243/4) | Yeti | 2026-05-11 06:11:54 CST | Just found this in the profile settings, I didn’t even realise it was an option to turn on and off. I agree, there doesn’t seem to be any obvious reason this should be allowed and I can’t think of why a legit user would even want to do this. I thought for a second that maybe...
- `S21` [Is there any good reason for allowing hidden profiles?](https://talk.nervos.org/t/is-there-any-good-reason-for-allowing-hidden-profiles/10243/5) | phroi | 2026-05-11 07:07:06 CST | Yeti: There’s certain topics […] that I’m sure some people sit on the sidelines because they don’t want to be seen as taking sides, even though they might have a strong opinion either way. You know, from what I can see, feels like we just have some sort of soft rules against:...
- `S22` [Is there any good reason for allowing hidden profiles?](https://talk.nervos.org/t/is-there-any-good-reason-for-allowing-hidden-profiles/10243/6) | matt_ckb | 2026-05-11 13:05:35 CST | chiming in with my opinion that it should be disabled @terrytai fyi please share your thoughts
- `S23` [CKB Ecosystem Biweekly Update](https://talk.nervos.org/t/ckb-ecosystem-biweekly-update/9821/18) | zz_tovarishch | 2026-05-11 10:27:36 CST | image1200×675 67.1 KB CKB Ecosystem Biweekly Update #16 Welcome to the latest CKB Ecosystem Biweekly Update. Here’s a quick summary of key dev and ecosystem progress from the past two weeks. Infrastructure & Tooling @CKBdev improved CKB-VM ARM64 performance, added SKILL.md for...

## 活跃话题

1. [Discussion about an alternative to the protocol treasury](https://talk.nervos.org/t/discussion-about-an-alternative-to-the-protocol-treasury/10246) | 11 条近窗帖子 | 最新活动 2026-05-12 02:34:26 CST
2. [Spark Program | Nervos Brain - A Global Developer Onboarding Engine and Cross-Language Hub Powered by Agentic RAG](https://talk.nervos.org/t/spark-program-nervos-brain-a-global-developer-onboarding-engine-and-cross-language-hub-powered-by-agentic-rag/9995) | 1 条近窗帖子 | 最新活动 2026-05-12 02:09:50 CST | tags: In-Progress, Spark-Program
3. [Spark Program | Tiko Creator Commerce Expansion + Private Beta Validation](https://talk.nervos.org/t/spark-program-tiko-creator-commerce-expansion-private-beta-validation/10231) | 1 条近窗帖子 | 最新活动 2026-05-12 01:23:41 CST | tags: Pending, Spark-Program
4. [[DIS] Bitcoin Renegade CKB Media Campaign](https://talk.nervos.org/t/dis-bitcoin-renegade-ckb-media-campaign/10239) | 2 条近窗帖子 | 最新活动 2026-05-12 01:02:42 CST
5. [Pre-RFC Discussion: Activating the Nervos DAO Treasury](https://talk.nervos.org/t/pre-rfc-discussion-activating-the-nervos-dao-treasury/10143) | 1 条近窗帖子 | 最新活动 2026-05-12 00:55:11 CST | tags: CKB
6. [再谈CKB/Fiber支撑的原生稳定币的必要性和紧迫性](https://talk.nervos.org/t/ckb-fiber/10240) | 17 条近窗帖子 | 最新活动 2026-05-11 19:49:26 CST
7. [[DIS] Mobile-Ready CKB Light Client (Pocket Node) for Android](https://talk.nervos.org/t/dis-mobile-ready-ckb-light-client-pocket-node-for-android/9879) | 2 条近窗帖子 | 最新活动 2026-05-11 15:22:31 CST | tags: CKB, light-client
8. [Is there any good reason for allowing hidden profiles?](https://talk.nervos.org/t/is-there-any-good-reason-for-allowing-hidden-profiles/10243) | 3 条近窗帖子 | 最新活动 2026-05-11 13:05:35 CST
9. [CKB Ecosystem Biweekly Update](https://talk.nervos.org/t/ckb-ecosystem-biweekly-update/9821) | 1 条近窗帖子 | 最新活动 2026-05-11 10:27:36 CST | tags: Ecosystem-Update

## 最近帖子摘录

- 2026-05-12 02:34:26 CST | matt_ckb | [Discussion about an alternative to the protocol treasury](https://talk.nervos.org/t/discussion-about-an-alternative-to-the-protocol-treasury/10246/18) | It’s a fair critique, however as I have said many times on this thread: We are bound by social contract on this. The treasury needs to be implemented and available for...
- 2026-05-12 02:25:52 CST | jimi-winehouse | [Discussion about an alternative to the protocol treasury](https://talk.nervos.org/t/discussion-about-an-alternative-to-the-protocol-treasury/10246/17) | I would argue this is a regression not a progression towards decentralization. The current system is the most decentralized. Adding a sub PoS system/voting in the L1 is what I...
- 2026-05-12 02:09:50 CST | IrisNeko | [Spark Program | Nervos Brain - A Global Developer Onboarding Engine and Cross-Language Hub Powered by Agentic RAG](https://talk.nervos.org/t/spark-program-nervos-brain-a-global-developer-onboarding-engine-and-cross-language-hub-powered-by-agentic-rag/9995/37) | 回顾近期的 bad case，主要原因是 prompt 设置过于保守：一方面表现为对用户频繁追问，另一方面是查资料不够积极。此外，上周的数据库问题也是因模型未触发多库联合调用引起的。总体来看，系统并没有严重的设计或架构问题，后续优化 prompt 和调用逻辑即可解决。
- 2026-05-12 02:02:26 CST | ebdalezyz_aljhny | [Discussion about an alternative to the protocol treasury](https://talk.nervos.org/t/discussion-about-an-alternative-to-the-protocol-treasury/10246/16) | رسالة It is simply an idea. You may develop it further or reject it entirely. The intention is only to help manage a temporary phase and allow more focus on what is currently...
- 2026-05-12 01:44:08 CST | matt_ckb | [Discussion about an alternative to the protocol treasury](https://talk.nervos.org/t/discussion-about-an-alternative-to-the-protocol-treasury/10246/15) | do the council members have decision making authority? Even in Community Fund DAO v1 it is governance by community members/token holders
- 2026-05-12 01:33:43 CST | ebdalezyz_aljhny | [Discussion about an alternative to the protocol treasury](https://talk.nervos.org/t/discussion-about-an-alternative-to-the-protocol-treasury/10246/14) | If we are allowed to share our opinion, I think it would be a good idea, at least initially, to have a council made up of fifty members responsible for managing the DAO until...
- 2026-05-12 01:23:41 CST | DWSQUIRES | [Spark Program | Tiko Creator Commerce Expansion + Private Beta Validation](https://talk.nervos.org/t/spark-program-tiko-creator-commerce-expansion-private-beta-validation/10231/3) | Updated. I narrowed the supported scope from 7 categories to the first 3 categories: Digital drops, Memberships/passes, and Limited editions/collectibles. I also added a...
- 2026-05-12 01:02:42 CST | joshyates1980 | [[DIS] Bitcoin Renegade CKB Media Campaign](https://talk.nervos.org/t/dis-bitcoin-renegade-ckb-media-campaign/10239/32) | As you fine tune your proposal with the plenty of feedback/suggestions from Nervos community, I do support your campaign and comical endeavors at live events which turn heads...
- 2026-05-12 00:59:45 CST | matt_ckb | [Discussion about an alternative to the protocol treasury](https://talk.nervos.org/t/discussion-about-an-alternative-to-the-protocol-treasury/10246/13) | image986×164 17.7 KB appreciate you engaging in this discussion, it seems like you have been around a while. It might be better to move to Nervos Nation or another chat forum to...
- 2026-05-12 00:55:11 CST | matt_ckb | [Pre-RFC Discussion: Activating the Nervos DAO Treasury](https://talk.nervos.org/t/pre-rfc-discussion-activating-the-nervos-dao-treasury/10143/13) | 12 posts were split to a new topic: Discussion about an alternative to the protocol treasury
- 2026-05-11 22:56:24 CST | Bitcoin_Renegade | [[DIS] Bitcoin Renegade CKB Media Campaign](https://talk.nervos.org/t/dis-bitcoin-renegade-ckb-media-campaign/10239/31) | Yes I am withdrawing my proposal and putting in a new one
- 2026-05-11 21:32:38 CST | jimi-winehouse | [Discussion about an alternative to the protocol treasury](https://talk.nervos.org/t/discussion-about-an-alternative-to-the-protocol-treasury/10246/12) | the solution I am proposing is to activate the treasury and just make it centralized and focus on high impact projects. Taking a year of work to decentralized a treasury is...
- 2026-05-11 19:49:26 CST | yifenzi | [再谈CKB/Fiber支撑的原生稳定币的必要性和紧迫性](https://talk.nervos.org/t/ckb-fiber/10240/18) | 对安全和稳定的认知如此重要我不得不再做一些说明 要明确脱锚和归零的风险是存在的 同时所有人要一起尽量避免它 现实中银行都会倒闭(全世界都有发生过)，甚至整个国家的纸币都会作废直接换新 没有比这个更能说明安全和稳定的相对性了，一些东西很残酷，但必须面对
- 2026-05-11 19:40:12 CST | Yeti | [Discussion about an alternative to the protocol treasury](https://talk.nervos.org/t/discussion-about-an-alternative-to-the-protocol-treasury/10246/11) | 4.6 Treasury The portion of secondary issuance that doesn’t go to 1) miners or 2) long-term holders with tokens locked in the NervosDAO, will go toward a treasury fund. To...
- 2026-05-11 19:37:24 CST | Yeti | [Discussion about an alternative to the protocol treasury](https://talk.nervos.org/t/discussion-about-an-alternative-to-the-protocol-treasury/10246/10) | jimi-winehouse: can I get a link to this paper? https://github.com/nervosnetwork/rfcs/blob/master/rfcs/0001-positioning/0001-positioning.md
- 2026-05-11 19:25:08 CST | jimi-winehouse | [Discussion about an alternative to the protocol treasury](https://talk.nervos.org/t/discussion-about-an-alternative-to-the-protocol-treasury/10246/9) | It sounds like an appeal to authority, and a centralized one with the way you’re unwilling to discuss and provide good arguments for. Where is this “social contract” so I can...
- 2026-05-11 19:23:58 CST | Yeti | [再谈CKB/Fiber支撑的原生稳定币的必要性和紧迫性](https://talk.nervos.org/t/ckb-fiber/10240/17) | yifenzi: This is a timeline everyone should work to avoid. All of our collective efforts are aimed at making things happen in a timeline where CKB’s price grows steadily — not...
- 2026-05-11 19:21:46 CST | yifenzi | [再谈CKB/Fiber支撑的原生稳定币的必要性和紧迫性](https://talk.nervos.org/t/ckb-fiber/10240/16) | 没有绝对安全，只有相对安全 我一直认为这是一个人成熟的第一课 就像密码学的加密算法和攻破方法，一直都是矛和盾的比拼 现在的抗量子算法也一定会被攻破，可能五十年一百年或者更久，但只是时间问题，然后又有一个新的更强大的算法，如此往复 好消息是现在的抗量子算法可能会为我们争取到足够的时间
- 2026-05-11 19:12:12 CST | yifenzi | [再谈CKB/Fiber支撑的原生稳定币的必要性和紧迫性](https://talk.nervos.org/t/ckb-fiber/10240/15) | 在补充一点 在CKB价格平稳和上涨时，对UtxoUSD的价值有保证这点应该都没问题...
- 2026-05-11 18:37:24 CST | Yeti | [再谈CKB/Fiber支撑的原生稳定币的必要性和紧迫性](https://talk.nervos.org/t/ckb-fiber/10240/14) | yifenzi: If CKB truly reaches nearly zero, that means almost all miner nodes are gone — isn’t it perfectly natural that everything on the CKB chain, including UtxoUSD, would...
