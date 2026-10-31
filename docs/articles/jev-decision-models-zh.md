> 原文：[Jev introduces a new shape of LLM—System One, aka Decision Models](https://simonwillison.net/2026/Sep/21/jev/)
> 作者：[Simon Willison](https://simonwillison.net/) · 发布时间：2026 年 9 月 21 日 23:09 · 更新：2026 年 9 月 22 日

# Jev 带来了一种新形态的 LLM——System One，也就是"决策模型"

上周，[TypeSafe AI](https://typesafe.ai/) 发布了 [Jev](https://typesafe.ai/blog/introducing-system-one-models-and-jev)，这是他们所谓"System One 模型（System One models）"这一全新模型品类的第一个实例（我站 Maggie Appleton 这边，我认为"决策模型（decision models）"是[更好的叫法](https://twitter.com/Mappletons/status/2101560333441610133)）。Jev 是常见 LLM 形态的一个有意思的变体：它照样接受文本输入，但输出的不是文本，而是浮点数——对应类别、是/否问题、评分，以及与之配套的置信度分数。

TypeSafe 是这样描述 Jev 的：

> 可以把 Jev 想成一次"前沿智能的函数调用（frontier-intelligence function call）"：非结构化状态进，带类型的概率化决策出。

它还非常快，而且**极其便宜**。常规 LLM 的[定价](https://www.llm-prices.com)按输入和输出 Token 分别计费，输出单价通常显著更高。Jev 只对输入收费——输出免费——而他们第一个模型的输入价格是每百万 Token 0.042 美元，比 OpenAI 的 [GPT-5 Nano](https://developers.openai.com/api/docs/models/gpt-5-nano)（每百万 0.05 美元）还便宜。

## 三类问题

Jev 让你针对文本或半结构化数据提问。你先拼出一个"状态（state）"对象，内容可以是一个字符串、一个字符串数组，或一组名值对——它可能描述一篇文章、一位客户，或任何别的记录。然后你把它连同一个或多个问题发给他们的 API，每个问题都会得到一个回答。

你可以问三类问题：

- **是/否问题**，Jev 称之为"Noul"问题——他们的 CEO [在 Hacker News 上确认过](https://news.ycombinator.com/item?id=49717558#49718407)，这是 Bernoulli 的缩写，取自[伯努利分布（Bernoulli distribution）](https://en.wikipedia.org/wiki/Bernoulli_distribution)。你给出一个陈述，模型返回一个 0 到 1 之间的浮点数，表示它对该陈述为真的置信度。
- **选择题（Choice questions）**，模型从你提供的一组选项里挑一个——实际上返回的是一个置信度分数，加上覆盖所有选项的概率分布。
- **打分题（Score questions）**，你给出一串带描述的数值等级，模型返回落在这个区间某处的浮点分数。

Jev 的 API 可以接收单个文档（"state"）以及你能塞进 Context Window（上下文窗口）的任意多个问题。这些问题是并行求值的，所以问很多个问题和只问一个，耗时应大致相当。

[Jev 1.13 jaggedness](https://docs.typesafe.ai/model-jaggedness/jev-1.13) 这份文档对 Jev 的强项和弱项给出了很有用的指引。它目前在处理数字、日期以及"对抗性内容（adversarial content）"方面表现不佳。

我认为**决策模型**这个框架，对理解该在哪里用 Jev 很有帮助。凡是能表达成分类任务的事情它都很擅长——比如垃圾内容检测、推荐标签、优先级排序与排名。

我也在拿它试搜索重排（reranking）：先用 BM25 这类廉价算法取回 100 条可能的匹配，再让 Jev 针对原始查询给这 100 个候选打分。

## 黑箱又流行起来了

Jev 让我有点不安的一点是：它实实在在地代表了一次倒退，朝着黑箱机器学习系统又退了一大步。

LLM 本来就已经是黑箱了——你可以要求它为自己的决策说明理由，但你无法保证它说的东西有用或者准确。

Jev 连这个都不给你：你想塞多少文本进去都行，但你唯一能拿回来的就是一个浮点数。如果 Jev 把某条内容标成垃圾内容，究竟是哪些内容特征让它下的判断？

这也意味着，关于偏见（bias）的担忧必须被摆到最显眼的位置。我真的希望别有人拿 Jev 去给求职者排名——那个浮点数可能藏着模型里 baked in 的各种看不见的偏见，而要通过实验把这种偏见拆解出来，会是一件棘手的事。

（我做过一个实验：让 Jev 对旧金山湾区的每一座城市就"是好城市吗？"这个问题给出是/否打分——它把 [Cupertino](https://en.wikipedia.org/wiki/Cupertino,_California) 排在第一，把 [East Palo Alto](https://en.wikipedia.org/wiki/East_Palo_Alto,_California) 排在最后。嗯。）

在实践层面，这一切意味着：评测（evals）和结构化实验比在常规 LLM 项目里更重要。好在 Jev 便宜到这种程度——跑几百甚至几千个实验性 Prompt 也只要几分钱。

## Jev 的非常规用法

过去几天看整个社区给 Jev 想出各种潜在用例，非常有意思。以下是几个吸引我眼球的创意用法：

- Kyle Pena 的 [jevchat](https://github.com/kyle-pena-nlp/jevchat/) 把 Jev 变成了一个（糟糕透顶的）聊天模型。"每一步它都问 Jev 一个问题：给定用户的问题和到目前为止已经写好的回复，下一个符号是什么？" [Hacker News 上的 ericpruitt](https://news.ycombinator.com/item?id=49778162#49778423) 评论："这相当于 Morty 拿着死亡水晶说话的数字版本（It's the digital equivalent of Morty speaking with the death crystal）"。
- Fatih Kadir Akın 的 [jev-leftpad](https://github.com/f/jev-leftpad) 用 Jev 实现了 [left-pad](https://www.npmjs.com/package/left-pad)，用的 Prompt 是"在 value 之前需要多少个空格才能达到 targetLength？"，外加[一个选择题查询](https://github.com/f/jev-leftpad/blob/4f405354de756cc372826d19aa8dfbee2b675778/src/index.js#L9-L30)，可选项从"需要 0 个空格"到"需要 10 个空格"。
- Andy Gayton 的 [jev-2048](https://gist.github.com/cablehead/bdf9ad946ceb26d9008976e49c9bfbbb) 用 Jev 来玩 [2048 滑块拼图游戏](https://simple-jev.featherless.ai/cool-demo/2048/)。

## 开放权重的复刻

此外还涌现出一批项目，试图在开放权重模型之上做出一个类似 Jev 的模型。[Kev](https://github.com/jaredpalmer/kev) 是其中一个有意思的例子，它用 Qwen 3.5 做出了 0.8B、4B 和 9B 三个模型。这是[配套的 Hacker News 讨论串](https://news.ycombinator.com/item?id=49783999)，串里有人贴出了一个 [JevBench](https://benchmarkheaven.com/jev-models) 基准测试，它已经冒出来用于比较"Jev 级的决策模型"。

考虑到 Jev 发布还不到一周，它周围的活跃程度实在令人印象深刻。

## 通过 LLM 使用 Jev

**2026 年 9 月 22 日更新**：我发布了 [llm-typesafe](https://github.com/simonw/llm-typesafe)，这是一个为我的 [LLM](https://llm.datasette.io/) CLI 工具和 Python 库增加 Jev 支持的插件。基本用法如下：

```bash
llm -m jev 'Please refund my last payment.' \
  -s 'Does this message explicitly request a refund?'
```

其他查询类型的示例见[该项目的 README](https://github.com/simonw/llm-typesafe/blob/main/README.md)。

---

## 原文信息

- 原文标签：ai、generative-ai、llms、evals、ai-bias、jev
- 提及的资源：TypeSafe AI / Jev、Jev 1.13 jaggedness 文档、jevchat、jev-leftpad、jev-2048、Kev、JevBench、llm-typesafe

## 版权与许可

- **原文**：Simon Willison，《Jev introduces a new shape of LLM—System One, aka Decision Models》，2026-09-21 — [原文链接](https://simonwillison.net/2026/Sep/21/jev/)
- **原文许可**：原文页面正文、站脚与 `/about/` 页面均未标注任何开放许可协议（未检索到 CC 或其他版权声明），默认视为保留所有权利
- **本译文**：非官方中文翻译，仅作学习与交流用途；已署名原作者并链接原文，如权利人提出异议将即时下架

## 译者注

1. **System One**：TypeSafe 对这类模型的命名，原文未解释来源；命名容易让人联想到 Kahneman《思考，快与慢》里"系统 1（快思考）/ 系统 2（慢思考）"的划分，但本文未对此展开，故不作断言。
2. **Noul 问题**：由 CEO 确认为 Bernoulli（伯努利）的缩写，对应伯努利分布——即单次二值试验的概率分布，与"是/否 + 置信度"的输出形式吻合。
3. **jaggedness**：AI 语境中指模型能力的"参差不齐"——整体很强但在某些窄任务上意外弱。TypeSafe 专门为每个模型版本维护一份 jaggedness 文档，列出已知短板（本文引文：数字、日期、对抗性内容）。
4. **left-pad**：2016 年因作者下架该 npm 包导致大量构建中断的著名事件，此处被戏仿为"用 LLM 判定需要补几个空格"。
5. **death crystal**：出自动画《瑞克和莫蒂》（Rick and Morty）；Hacker News 评论用它比喻"一次只吐一个符号、毫无全局语义"的对话方式。
6. 术语首现附英文：System One 模型（System One models）、决策模型（decision models）、状态（state）、上下文窗口（Context Window）、置信度（confidence）、重排（reranking）、评测（evals）、偏见（bias）。
