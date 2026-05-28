# Nervos Talk 社区简报

- 统计窗口: 2026-05-28 03:35:11 CST 到 2026-05-29 03:35:11 CST
- 生成时间: 2026-05-29 03:35:16 CST
- 话题数: 6
- 帖子数: 13
- 作者数: 10
- 总结模式: ai:openrouter

## 社区总结

## 今日发生了什么

社区今天整体较平静，但 Fiber 相关开发活动集中在近 24 小时密集出现。[S11, S12, S13] 与此同时，社区成员围绕 Common Knowledge Base Association（CKBA）的会员制度持续提出疑问并收到官方回应。[S08, S09, S10]

## 重点话题

- **Fiber 生态工具连发三帖**：joii2020 先后发布了 Fiber Manager 浏览器扩展插件指南[S13] 和在浏览器扩展中运行 fiber-js 的技术验证 demo[S12]；Ticoworld 则推出了 FiberLatch 实验项目，展示如何在测试网上实现"先验证 Fiber 付款、后解锁资源"的完整流程[S11]。这标志着 Fiber 支付场景的开发者工具正在快速落地。[S11, S12, S13]

- **CKBA 一般会员注册即将开放**：woodbury.bit 询问一般会员（General Member）何时开放申请，并表示希望"更直接地参与到生态系统中来"，同时关心一般会员是否具备议政权（旁听、建议等）[S08]。CKBA 官方确认一般会员注册正在最终落实中，将很快在 ckba.build 上线[S10]。

- **CKBA 贡献会员持续吸引技术贡献者**：ArthurZhang 提交贡献会员申请，列举了自己在 CellScript、CellFabric 以及基于 eltoo 改进的 CKB 原生状态通道协议 Morph Channel 等方面的持续工作[S09]。

- **Fiber Desktop 提案的支付货币争议仍在讨论**：ebubedev 申请的 Fiber Desktop v1 重建提案中写明"CKB equivalent at disbursement"，引发关于 DAO 拨款究竟以美元等值还是 CKB 数量结算的辩论[S02, S03]。zz_tovarishch 指出历史上已有项目在过渡期政策外申请并通过了美元等值支付，已将此情况转告委员会等待回复[S06]。

## 值得继续跟进

- CKBA 一般会员注册的实际开放时间及其治理参与度边界，特别是 woodbury.bit 关心的"议政权"能否在制度层面得到明确[S08, S10]

- DAO 委员会对 Fiber Desktop 提案中"CKB equivalent"措辞的最终定性，这将影响 ebubedev 的实际收款方式[S06, S07]

- Fiber Manager 插件和 fiber-js 浏览器扩展的成熟度进展，若从"early development stage"进入实用阶段，可能显著降低 Fiber 节点管理的门槛[S12, S13]

## 来源索引

- `S01` [Spark Program | Dular](https://talk.nervos.org/t/spark-program-dular/10212/10) | duongja | 2026-05-29 03:33:00 CST | Hello, Find the detailed Milestone 1 Report in the google docs Milestone 1 Report
- `S02` [[DIS] Fiber Desktop v1 ground-up rebuild and launch — fnn desktop app](https://talk.nervos.org/t/dis-fiber-desktop-v1-ground-up-rebuild-and-launch-fnn-desktop-app/10317/2) | Yeti | 2026-05-28 05:30:22 CST | This is an easy one, really worthwhile project, reasonable funding request. ebubedev: Grant Amount Requested: $6,000 USD (CKB equivalent at disbursement) Maybe I’m misunderstanding your wording here, but just so you know, you won’t be getting the USD equivalent at each...
- `S03` [[DIS] Fiber Desktop v1 ground-up rebuild and launch — fnn desktop app](https://talk.nervos.org/t/dis-fiber-desktop-v1-ground-up-rebuild-and-launch-fnn-desktop-app/10317/3) | phroi | 2026-05-28 07:09:11 CST | Yeti: you won’t be getting the USD equivalent at each payment As you can see from the link (I was pretty surprised too), it’s currently possible to use the USD equivalent: [DIS] CKB Integration for Rosen Bridge CKB Community Fund DAO M1 Payout...
- `S04` [[DIS] Fiber Desktop v1 ground-up rebuild and launch — fnn desktop app](https://talk.nervos.org/t/dis-fiber-desktop-v1-ground-up-rebuild-and-launch-fnn-desktop-app/10317/4) | Yeti | 2026-05-28 07:28:02 CST | Hi Phroi, yeah, I saw your original post bringing up the overpayment, but don’t think I saw the follow up posts. (Btw, I thought that was very honest of you and the team to come forward about that, not sure if everyone would do that.) But I’m still not sure what the case is at...
- `S05` [[DIS] Fiber Desktop v1 ground-up rebuild and launch — fnn desktop app](https://talk.nervos.org/t/dis-fiber-desktop-v1-ground-up-rebuild-and-launch-fnn-desktop-app/10317/5) | ebubedev | 2026-05-28 17:35:49 CST | i think they do, i will have to confirm first @zz_tovarishch
- `S06` [[DIS] Fiber Desktop v1 ground-up rebuild and launch — fnn desktop app](https://talk.nervos.org/t/dis-fiber-desktop-v1-ground-up-rebuild-and-launch-fnn-desktop-app/10317/6) | zz_tovarishch | 2026-05-28 17:59:06 CST | Hi @ebubedev 正如 [DIS] CKB Integration for Rosen Bridge - #137 by zz_tovarishch 这里统计的，在过渡期政策起效（2025年12月）前已经有项目以美元等值提出申请（2025年7月）和支付（2025年8月和10月），此外也有项目在过渡期政策范围外申请了美元等值支付（通过了投票，故按照提案内容进行的美元等值支付） 已经将情况转告委员会，等待他们回复
- `S07` [[DIS] Fiber Desktop v1 ground-up rebuild and launch — fnn desktop app](https://talk.nervos.org/t/dis-fiber-desktop-v1-ground-up-rebuild-and-launch-fnn-desktop-app/10317/7) | ebubedev | 2026-05-28 22:53:13 CST | so what does this mean for my own case, where it states “ckb equivalent” as the time of disbursement for each milestone
- `S08` [A New Chapter for CKB: Introducing the Common Knowledge Base Association](https://talk.nervos.org/t/a-new-chapter-for-ckb-introducing-the-common-knowledge-base-association/10249/7) | woodbury.bit | 2026-05-28 09:59:04 CST | 请问一下，CKBA 的一般会员（General Member）注册什么时候开放？ 我看介绍里面写了会员申请开放，但是我没有看到一般会员申请，只有贡献会员 （Contributing Member) 申请。 例如我这种没有贡献的想报名一般会员，想“更直接地参与到生态系统中来”。什么时候可以报名一般会员呢？ 还有顺便请教一下一般会员有没有议政的权利呢？例如是否可以旁听讨论、提出建议之类的呢？
- `S09` [A New Chapter for CKB: Introducing the Common Knowledge Base Association](https://talk.nervos.org/t/a-new-chapter-for-ckb-introducing-the-common-knowledge-base-association/10249/8) | ArthurZhang | 2026-05-28 13:42:41 CST | I’ve just submitted my Contributing Member application. I’ve been contributing through CellScript, the CellScript VS Code extension, CellFabric, and an ongoing thesis on the eltoo-inspired and ckb-native state channel protocol Morph Channel, with the aim of improving CKB...
- `S10` [A New Chapter for CKB: Introducing the Common Knowledge Base Association](https://talk.nervos.org/t/a-new-chapter-for-ckb-introducing-the-common-knowledge-base-association/10249/9) | CKBA | 2026-05-28 21:52:23 CST | Hi thanks for your question. The General Member registration is being finalised and will open soon on https://www.ckba.build/ We’ll announce it as soon as it’s ready, so keep an eye on our channels.
- `S11` [FiberLatch: live paid Fiber testnet payment to signed access receipt](https://talk.nervos.org/t/fiberlatch-live-paid-fiber-testnet-payment-to-signed-access-receipt/10324/1) | Ticoworld | 2026-05-28 20:15:19 CST | Hi everyone, I’ve been building FiberLatch, a small backend-only experiment around Fiber payment verification and signed access receipts. The idea is simple: A service should only unlock a resource after it verifies that a Fiber payment is actually paid. Once verified,...
- `S12` [Using fiber-js in a Browser Extension](https://talk.nervos.org/t/using-fiber-js-in-a-browser-extension/10323/1) | joii2020 | 2026-05-28 15:18:47 CST | Introduction This demo verifies whether @nervosnetwork/fiber-js can run inside a browser extension. ( fiber-js is a JavaScript wrapper around the Fiber WebAssembly runtime. It starts a Fiber node inside browser workers and exposes JavaScript methods for controlling that node)...
- `S13` [Fiber Manager Plugin Guide](https://talk.nervos.org/t/fiber-manager-plugin-guide/10322/1) | joii2020 | 2026-05-28 15:14:38 CST | Fiber Manager is a browser extension for managing and debugging Fiber nodes from a browser-based workspace. After the extension is loaded, click the extension icon in the browser toolbar to open the management workspace. The plugin is still in an early development stage. It is...

## 活跃话题

1. [Spark Program | Dular](https://talk.nervos.org/t/spark-program-dular/10212) | 1 条近窗帖子 | 最新活动 2026-05-29 03:33:00 CST | tags: In-Progress, Spark-Program
2. [[DIS] Fiber Desktop v1 ground-up rebuild and launch — fnn desktop app](https://talk.nervos.org/t/dis-fiber-desktop-v1-ground-up-rebuild-and-launch-fnn-desktop-app/10317) | 6 条近窗帖子 | 最新活动 2026-05-28 22:53:13 CST | tags: fiber
3. [A New Chapter for CKB: Introducing the Common Knowledge Base Association](https://talk.nervos.org/t/a-new-chapter-for-ckb-introducing-the-common-knowledge-base-association/10249) | 3 条近窗帖子 | 最新活动 2026-05-28 21:52:23 CST | tags: CKB
4. [FiberLatch: live paid Fiber testnet payment to signed access receipt](https://talk.nervos.org/t/fiberlatch-live-paid-fiber-testnet-payment-to-signed-access-receipt/10324) | 1 条近窗帖子 | 最新活动 2026-05-28 20:15:19 CST | tags: CKB, fiber, testnet
5. [Using fiber-js in a Browser Extension](https://talk.nervos.org/t/using-fiber-js-in-a-browser-extension/10323) | 1 条近窗帖子 | 最新活动 2026-05-28 15:18:47 CST | tags: fiber
6. [Fiber Manager Plugin Guide](https://talk.nervos.org/t/fiber-manager-plugin-guide/10322) | 1 条近窗帖子 | 最新活动 2026-05-28 15:14:38 CST | tags: fiber

## 最近帖子摘录

- 2026-05-29 03:33:00 CST | duongja | [Spark Program | Dular](https://talk.nervos.org/t/spark-program-dular/10212/10) | Hello, Find the detailed Milestone 1 Report in the google docs Milestone 1 Report
- 2026-05-28 22:53:13 CST | ebubedev | [[DIS] Fiber Desktop v1 ground-up rebuild and launch — fnn desktop app](https://talk.nervos.org/t/dis-fiber-desktop-v1-ground-up-rebuild-and-launch-fnn-desktop-app/10317/7) | so what does this mean for my own case, where it states “ckb equivalent” as the time of disbursement for each milestone
- 2026-05-28 21:52:23 CST | CKBA | [A New Chapter for CKB: Introducing the Common Knowledge Base Association](https://talk.nervos.org/t/a-new-chapter-for-ckb-introducing-the-common-knowledge-base-association/10249/9) | Hi thanks for your question. The General Member registration is being finalised and will open soon on https://www.ckba.build/ We’ll announce it as soon as it’s ready, so keep an...
- 2026-05-28 20:15:19 CST | Ticoworld | [FiberLatch: live paid Fiber testnet payment to signed access receipt](https://talk.nervos.org/t/fiberlatch-live-paid-fiber-testnet-payment-to-signed-access-receipt/10324/1) | Hi everyone, I’ve been building FiberLatch, a small backend-only experiment around Fiber payment verification and signed access receipts. The idea is simple: A service should...
- 2026-05-28 17:59:06 CST | zz_tovarishch | [[DIS] Fiber Desktop v1 ground-up rebuild and launch — fnn desktop app](https://talk.nervos.org/t/dis-fiber-desktop-v1-ground-up-rebuild-and-launch-fnn-desktop-app/10317/6) | Hi @ebubedev 正如 [DIS] CKB Integration for Rosen Bridge - #137 by zz_tovarishch...
- 2026-05-28 17:35:49 CST | ebubedev | [[DIS] Fiber Desktop v1 ground-up rebuild and launch — fnn desktop app](https://talk.nervos.org/t/dis-fiber-desktop-v1-ground-up-rebuild-and-launch-fnn-desktop-app/10317/5) | i think they do, i will have to confirm first @zz_tovarishch
- 2026-05-28 15:18:47 CST | joii2020 | [Using fiber-js in a Browser Extension](https://talk.nervos.org/t/using-fiber-js-in-a-browser-extension/10323/1) | Introduction This demo verifies whether @nervosnetwork/fiber-js can run inside a browser extension. ( fiber-js is a JavaScript wrapper around the Fiber WebAssembly runtime. It...
- 2026-05-28 15:14:38 CST | joii2020 | [Fiber Manager Plugin Guide](https://talk.nervos.org/t/fiber-manager-plugin-guide/10322/1) | Fiber Manager is a browser extension for managing and debugging Fiber nodes from a browser-based workspace. After the extension is loaded, click the extension icon in the...
- 2026-05-28 13:42:41 CST | ArthurZhang | [A New Chapter for CKB: Introducing the Common Knowledge Base Association](https://talk.nervos.org/t/a-new-chapter-for-ckb-introducing-the-common-knowledge-base-association/10249/8) | I’ve just submitted my Contributing Member application. I’ve been contributing through CellScript, the CellScript VS Code extension, CellFabric, and an ongoing thesis on the...
- 2026-05-28 09:59:04 CST | woodbury.bit | [A New Chapter for CKB: Introducing the Common Knowledge Base Association](https://talk.nervos.org/t/a-new-chapter-for-ckb-introducing-the-common-knowledge-base-association/10249/7) | 请问一下，CKBA 的一般会员（General Member）注册什么时候开放？ 我看介绍里面写了会员申请开放，但是我没有看到一般会员申请，只有贡献会员 （Contributing Member) 申请。 例如我这种没有贡献的想报名一般会员，想“更直接地参与到生态系统中来”。什么时候可以报名一般会员呢？...
- 2026-05-28 07:28:02 CST | Yeti | [[DIS] Fiber Desktop v1 ground-up rebuild and launch — fnn desktop app](https://talk.nervos.org/t/dis-fiber-desktop-v1-ground-up-rebuild-and-launch-fnn-desktop-app/10317/4) | Hi Phroi, yeah, I saw your original post bringing up the overpayment, but don’t think I saw the follow up posts. (Btw, I thought that was very honest of you and the team to come...
- 2026-05-28 07:09:11 CST | phroi | [[DIS] Fiber Desktop v1 ground-up rebuild and launch — fnn desktop app](https://talk.nervos.org/t/dis-fiber-desktop-v1-ground-up-rebuild-and-launch-fnn-desktop-app/10317/3) | Yeti: you won’t be getting the USD equivalent at each payment As you can see from the link (I was pretty surprised too), it’s currently possible to use the USD equivalent: [DIS]...
- 2026-05-28 05:30:22 CST | Yeti | [[DIS] Fiber Desktop v1 ground-up rebuild and launch — fnn desktop app](https://talk.nervos.org/t/dis-fiber-desktop-v1-ground-up-rebuild-and-launch-fnn-desktop-app/10317/2) | This is an easy one, really worthwhile project, reasonable funding request. ebubedev: Grant Amount Requested: $6,000 USD (CKB equivalent at disbursement) Maybe I’m...
