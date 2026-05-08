# Nervos Talk 社区简报

- 统计窗口: 2026-05-08 02:09:03 CST 到 2026-05-09 02:09:03 CST
- 生成时间: 2026-05-09 02:09:07 CST
- 话题数: 7
- 帖子数: 10
- 作者数: 8
- 总结模式: ai:openrouter

## 社区总结

## 今日发生了什么

Nervos论坛今天讨论活跃，围绕AI Agent支付实验、CellScript合约包管理和链上隐私方案展开了具体的技术讨论。[S01, S02, S05, S06] ArthurZhang发布了CellScript包管理的RFC，提出用GitHub作为极简注册表，避免开发者自建服务器和链上存储成本；同时关于UTXO隐私保护的新思路也引发了关注，强调不对底层协议做改动即可实现可切换的隐私层级。[S05, S06, S07]

## 重点话题

- **AI Agent调用平台方向获确认**：Thinker和RetricSu就基于Fiber的付费AI Agent实验深入交流，RetricSu确认核心动机是让无法直接使用Claude Code等工具的用户能付费使用，并展望了Agent间协作调用的可能性。[S01, S02]

- **CellScript包管理走极简路线**：ArthurZhang提出第一阶段注册表完全基于Git和GitHub，不架设自定义API、不维护专门数据库、不为源代码付链上存储费，目标是在接下来一到两个月落地。[S05]

- **UTXO隐私保护的新思路**：yifenzi提出无需改动底层协议、仅需钱包端实现的隐私方案，利用无限子私钥地址和"一地址一收一付"原则，让普通交易与隐私交易可随时切换，成本可调可控。[S06, S07]

- **fiber-js文档缺口被承认**：RetricSu确认官方文档缺少fiber-js的介绍和引导，表示应该补充这部分内容。[S03]

- **跨链风险监测聚焦xUDT行为分析**：Quantir补充说明在CKB上重点关注异常铸币/销毁模式和RGB++/DEX间突发流动性迁移等行为层指标，而非简单地址追踪。[S04]

## 值得继续跟进

- **CellScript GitHub注册表的落地进度**：该方案虽极简，但实际依赖GitHub的可持续性和去中心化程度存疑，需看社区反馈和代码实现。[S05]

- **Nervos DAO Treasury激活讨论的监管张力**：jimi-winehouse呼吁快速建立建设者激励，Yeti则指出当前二级发行机制已类似以太坊基金会模式，但直接激活国库可能面临复杂监管问题，两种思路尚未调和。[S08, S09]

- **AI Agent实验的付费模型与Fiber集成细节**：目前对话停留在方向确认层面，具体定价、结算和Agent上架机制待披露。[S01, S02]

## 来源索引

- `S01` [A Paid AI Agent Calling Experiment via Fiber](https://talk.nervos.org/t/a-paid-ai-agent-calling-experiment-via-fiber/10229/6) | Thinker | 2026-05-08 16:15:11 CST | 感觉挺有意思，但我还是不太确定我理解是否完全正确。这是想做个开放平台，开放给配置好的如Codex OpenClaw Hermes等这些Agent上架，它们是较强大脑（GPT5.5 Opus4.7 ）或独特技能突出的Agent（如爬虫Skill…），帮助那些没有资源或不想麻烦使用者直接使用？ 就现阶段来说感觉是个不错的方向定位，现在有不少尝鲜者优化配置了不错的Agent，但也有不少无法充分利用其价值 资源浪费，还有不少因渠道或精力问题而没法使用到。甚至为后期agnet学习技能A2A做准备。...
- `S02` [A Paid AI Agent Calling Experiment via Fiber](https://talk.nervos.org/t/a-paid-ai-agent-calling-experiment-via-fiber/10229/7) | RetricSu | 2026-05-08 17:27:31 CST | 你理解得没错。最简单的动机可以认为，很多人用不了 claude code，通过这个平台可以去付费使用。当然你说的更精细化的agent/独特技能的 agent 我觉得也是个方向，甚至后面 agent 去调用 agent 的协作，也可以通过这套方式去做，无外乎是把人的聊天界面换成更适合机器的交互而已。 至于你后面聊的这块，先说说现在已经做的：...
- `S03` [基于 fiber-js 的 Demo 开发](https://talk.nervos.org/t/fiber-js-demo/10230/3) | RetricSu | 2026-05-08 15:47:37 CST | 官方文档中缺少对 fiber-js 的相关介绍和引导，可能会导致一些开发者都不知道其存在的问题。 Yes we should add this part in docs
- `S04` [[DIS] Quantir Risk Intelligence for CKB Ecosystem and Cross-Chain Monitoring](https://talk.nervos.org/t/dis-quantir-risk-intelligence-for-ckb-ecosystem-and-cross-chain-monitoring/10218/7) | Quantir | 2026-05-08 14:15:15 CST | On CKB we’re mostly interested in behavioral and flow-based monitoring rather than only simple address tracking. For xUDT specifically, suspicious activity can be detected through several layers: abnormal mint/burn patterns; sudden liquidity migration between RGB++ / DEX...
- `S05` [[RFC] CellScript 的包管理：一个 Go 语言风格的、基于 GitHub 的 CKB 合约包管理注册表](https://talk.nervos.org/t/rfc-cellscript-go-github-ckb/10238/1) | ArthurZhang | 2026-05-08 11:31:06 CST | Hi，社区 上个月我发布了CellScript的早期预览版，得到了英语社区的一些建设性和温暖的反馈，现在我想用中文来和大家讨论一下未来的包管理的方向。 我在CellScript的后续开发路线 (大约在接下来一两个月) 中做了一个更去中心化也更解决成本的设计，因为我谨慎地认为这个阶段，可能发布和引用智能合约库，不应该需要搭建自定义 API 服务器、维护专门的数据库，或者为仅开发者需要的源代码支付链上存储费用。 CellScript 的第一阶段注册表将采取一种刻意极简的方案：一切都是 Git，一切都在 GitHub...
- `S06` [一点关于隐私保护的看法:所有Utxo系公链都原生具备的能力](https://talk.nervos.org/t/utxo/10237/1) | yifenzi | 2026-05-08 10:20:33 CST | 加密货币中关于隐私保护的讨论设计和实现一直在发生和推进，对不同潜在保护对象的底层认知的不同自然演进出不同的呈现路径 我的观点是隐私保护的对象应该是不作恶也没能力作恶的绝大多数的普通人，而不是在链上盗取勒索别人谋取不义之财的极少数作恶之人 基于这样的尺度，我提出一点关于隐私保护的看法，这个实现方式原生支持所有Utxo系公链，且实现不触及任何底层协议的变动只需要在钱包应用端即可做到，同时隐私保护的成本可调可控...
- `S07` [一点关于隐私保护的看法:所有Utxo系公链都原生具备的能力](https://talk.nervos.org/t/utxo/10237/2) | yifenzi | 2026-05-08 11:17:26 CST | 不管是所谓的独立隐私公链还是比特币网络上的一些项目，追求对付款地址收款地址以及交易金额这三要素的绝对隐藏的大方向可能就错了，其潜在服务对象，潜在技术漏洞和被接受的容易程度都是问题 利用无限子私钥地址以及一个地址只收一次只付一次的原则，让所有人都能在现在的基础上容易的用起来，且普通交易和隐私交易随时可以无缝切换 就像我们出去旅游住宿，绝大多数时候都只需要一间房间就够了，但如果有必要，也可以把整层楼甚至整个酒店包下，作为服务方，提供可选性然后让用户自己选择就行了，而在多个提供可选性的服务商家中，那个最能综合安全方便价格等各个因素的商家一定是胜出者
- `S08` [Pre-RFC Discussion: Activating the Nervos DAO Treasury](https://talk.nervos.org/t/pre-rfc-discussion-activating-the-nervos-dao-treasury/10143/13) | jimi-winehouse | 2026-05-08 07:16:34 CST | I 100% encourage this initiative. We should definitely find a fast solution to having no financial incentives for builders in the ecosystem when every ecosystem is inflating non-stop, running low float/high FDV scams, and managing to suck up all the talent pool and attention....
- `S09` [Pre-RFC Discussion: Activating the Nervos DAO Treasury](https://talk.nervos.org/t/pre-rfc-discussion-activating-the-nervos-dao-treasury/10143/14) | Yeti | 2026-05-08 09:10:57 CST | jimi-winehouse: Ethereum’s ecosystem is 1000x bigger and they still have the foundation basically using the equivalent of this treasury with ICO tokens That’s the current system we have, but I think there would be some pretty complex regulatory issues with the Secondary...
- `S10` [Spark Program | Dular](https://talk.nervos.org/t/spark-program-dular/10212/5) | duongja | 2026-05-08 03:41:42 CST | Updated @xingtianchunyan I have updated the following sections of the main post: Existing Progress clarified that the prototype has a public testnet multi-hop RUSD payment proof Public Testnet Multi-Hop RUSD Proof (new subsection added) added the completed Fiber payment hash...

## 活跃话题

1. [A Paid AI Agent Calling Experiment via Fiber](https://talk.nervos.org/t/a-paid-ai-agent-calling-experiment-via-fiber/10229) | 2 条近窗帖子 | 最新活动 2026-05-08 17:27:31 CST
2. [基于 fiber-js 的 Demo 开发](https://talk.nervos.org/t/fiber-js-demo/10230) | 1 条近窗帖子 | 最新活动 2026-05-08 15:47:37 CST
3. [[DIS] Quantir Risk Intelligence for CKB Ecosystem and Cross-Chain Monitoring](https://talk.nervos.org/t/dis-quantir-risk-intelligence-for-ckb-ecosystem-and-cross-chain-monitoring/10218) | 1 条近窗帖子 | 最新活动 2026-05-08 14:15:15 CST | tags: grant-RFC, grants
4. [[RFC] CellScript 的包管理：一个 Go 语言风格的、基于 GitHub 的 CKB 合约包管理注册表](https://talk.nervos.org/t/rfc-cellscript-go-github-ckb/10238) | 1 条近窗帖子 | 最新活动 2026-05-08 11:31:06 CST | tags: CKB, CKB-VM, CellScript
5. [一点关于隐私保护的看法:所有Utxo系公链都原生具备的能力](https://talk.nervos.org/t/utxo/10237) | 2 条近窗帖子 | 最新活动 2026-05-08 11:17:26 CST
6. [Pre-RFC Discussion: Activating the Nervos DAO Treasury](https://talk.nervos.org/t/pre-rfc-discussion-activating-the-nervos-dao-treasury/10143) | 2 条近窗帖子 | 最新活动 2026-05-08 09:10:57 CST | tags: CKB
7. [Spark Program | Dular](https://talk.nervos.org/t/spark-program-dular/10212) | 1 条近窗帖子 | 最新活动 2026-05-08 03:41:42 CST | tags: Pending, Spark-Program

## 最近帖子摘录

- 2026-05-08 17:27:31 CST | RetricSu | [A Paid AI Agent Calling Experiment via Fiber](https://talk.nervos.org/t/a-paid-ai-agent-calling-experiment-via-fiber/10229/7) | 你理解得没错。最简单的动机可以认为，很多人用不了 claude code，通过这个平台可以去付费使用。当然你说的更精细化的agent/独特技能的 agent 我觉得也是个方向，甚至后面 agent 去调用 agent 的协作，也可以通过这套方式去做，无外乎是把人的聊天界面换成更适合机器的交互而已。 至于你后面聊的这块，先说说现在已经做的：...
- 2026-05-08 16:15:11 CST | Thinker | [A Paid AI Agent Calling Experiment via Fiber](https://talk.nervos.org/t/a-paid-ai-agent-calling-experiment-via-fiber/10229/6) | 感觉挺有意思，但我还是不太确定我理解是否完全正确。这是想做个开放平台，开放给配置好的如Codex OpenClaw Hermes等这些Agent上架，它们是较强大脑（GPT5.5 Opus4.7 ）或独特技能突出的Agent（如爬虫Skill…），帮助那些没有资源或不想麻烦使用者直接使用？...
- 2026-05-08 15:47:37 CST | RetricSu | [基于 fiber-js 的 Demo 开发](https://talk.nervos.org/t/fiber-js-demo/10230/3) | 官方文档中缺少对 fiber-js 的相关介绍和引导，可能会导致一些开发者都不知道其存在的问题。 Yes we should add this part in docs
- 2026-05-08 14:15:15 CST | Quantir | [[DIS] Quantir Risk Intelligence for CKB Ecosystem and Cross-Chain Monitoring](https://talk.nervos.org/t/dis-quantir-risk-intelligence-for-ckb-ecosystem-and-cross-chain-monitoring/10218/7) | On CKB we’re mostly interested in behavioral and flow-based monitoring rather than only simple address tracking. For xUDT specifically, suspicious activity can be detected...
- 2026-05-08 11:31:06 CST | ArthurZhang | [[RFC] CellScript 的包管理：一个 Go 语言风格的、基于 GitHub 的 CKB 合约包管理注册表](https://talk.nervos.org/t/rfc-cellscript-go-github-ckb/10238/1) | Hi，社区 上个月我发布了CellScript的早期预览版，得到了英语社区的一些建设性和温暖的反馈，现在我想用中文来和大家讨论一下未来的包管理的方向。 我在CellScript的后续开发路线 (大约在接下来一两个月) 中做了一个更去中心化也更解决成本的设计，因为我谨慎地认为这个阶段，可能发布和引用智能合约库，不应该需要搭建自定义 API...
- 2026-05-08 11:17:26 CST | yifenzi | [一点关于隐私保护的看法:所有Utxo系公链都原生具备的能力](https://talk.nervos.org/t/utxo/10237/2) | 不管是所谓的独立隐私公链还是比特币网络上的一些项目，追求对付款地址收款地址以及交易金额这三要素的绝对隐藏的大方向可能就错了，其潜在服务对象，潜在技术漏洞和被接受的容易程度都是问题 利用无限子私钥地址以及一个地址只收一次只付一次的原则，让所有人都能在现在的基础上容易的用起来，且普通交易和隐私交易随时可以无缝切换...
- 2026-05-08 10:20:33 CST | yifenzi | [一点关于隐私保护的看法:所有Utxo系公链都原生具备的能力](https://talk.nervos.org/t/utxo/10237/1) | 加密货币中关于隐私保护的讨论设计和实现一直在发生和推进，对不同潜在保护对象的底层认知的不同自然演进出不同的呈现路径 我的观点是隐私保护的对象应该是不作恶也没能力作恶的绝大多数的普通人，而不是在链上盗取勒索别人谋取不义之财的极少数作恶之人...
- 2026-05-08 09:10:57 CST | Yeti | [Pre-RFC Discussion: Activating the Nervos DAO Treasury](https://talk.nervos.org/t/pre-rfc-discussion-activating-the-nervos-dao-treasury/10143/14) | jimi-winehouse: Ethereum’s ecosystem is 1000x bigger and they still have the foundation basically using the equivalent of this treasury with ICO tokens That’s the current system...
- 2026-05-08 07:16:34 CST | jimi-winehouse | [Pre-RFC Discussion: Activating the Nervos DAO Treasury](https://talk.nervos.org/t/pre-rfc-discussion-activating-the-nervos-dao-treasury/10143/13) | I 100% encourage this initiative. We should definitely find a fast solution to having no financial incentives for builders in the ecosystem when every ecosystem is inflating...
- 2026-05-08 03:41:42 CST | duongja | [Spark Program | Dular](https://talk.nervos.org/t/spark-program-dular/10212/5) | Updated @xingtianchunyan I have updated the following sections of the main post: Existing Progress clarified that the prototype has a public testnet multi-hop RUSD payment proof...
