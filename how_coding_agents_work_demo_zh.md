# 编码智能体如何工作

原文标题：How coding agents work
原文链接：https://simonwillison.net/guides/agentic-engineering-patterns/how-coding-agents-work/
原文作者：Simon Willison
访问日期：2026-03-25
原文发布日期：2026-03-16
原文最后修改：2026-03-16
译文版本：v0.1

## 译文说明

本文为 Simon Willison《Agentic Engineering Patterns》系列第二篇《How coding agents work》的示范中文版。本文沿用本项目既定术语约定，将 Coding Agent 统一译为“编码智能体”，将 Agent 统一译为“智能体”；LLM、Prompt、Token、Context Window 等术语默认保留英文，并在首次出现时按需要补充中文释义。代码块、工具调用标记、产品名和链接均保留原文格式。

## 正文

> 所属主题：协作工作流
> 上一篇：[反模式：有些事要避免](./anti_patterns_things_to_avoid_demo_zh.md)
> 下一篇：[如何将 Git 用于编码智能体工作流](./using_git_with_coding_agents_demo_zh.md)

和任何工具一样，理解[编码智能体](https://simonwillison.net/guides/agentic-engineering-patterns/what-is-agentic-engineering/)在底层是如何工作的，会帮助你更好地判断该怎样使用它们。

编码智能体本质上是一层围绕 LLM 的软件封装。它通过用户看不见的提示词，以及以可调用工具形式实现的额外能力，对 LLM 进行扩展。

## 大语言模型

任何编码智能体的核心都是大语言模型，也就是 LLM。它们的名字可能是 GPT-5.4、Claude Opus 4.6、Gemini 3.1 Pro，或者 Qwen3.5-35B-A3B。

LLM 是一种能够补全文本句子的机器学习模型。给它输入一句话，比如 “the cat sat on the ”，它几乎肯定会建议把 “mat” 作为下一个词。

随着模型规模越来越大、训练数据越来越多，它们也就能补全更复杂的句子——例如 “a python function to download a file from a URL is def download_file(url): ” 这样的内容。

LLM 实际上并不是直接处理单词，而是处理 Token。文本序列会先被转换成整数 Token 序列，所以 “the cat sat on the ” 会变成 `[3086, 9059, 10139, 402, 290, 220]`。理解这一点很重要，因为 LLM 提供商通常按处理的 Token 数量计费，而且模型一次能同时考虑的 Token 数量也是有限的。

你可以在 [platform.openai.com/tokenizer](https://platform.openai.com/tokenizer) 试试 OpenAI 的 tokenizer，看看这个过程是怎么发生的。

输入给 LLM 的内容叫作 Prompt（提示词）。LLM 返回的文本叫作 completion，有时也叫 response。

如今很多模型都是多模态（multimodal）的，这意味着它们能接受的不只是文本输入。视觉 LLM（Vision LLM，vLLM）可以把图片作为输入的一部分，所以你可以把草图、照片或截图喂给它们。一个常见误解是，这些图像会先经过单独的 OCR 或图像分析流程；其实并不是，它们同样会被转换成更多的整数 Token，再用和文本相同的方式处理。

## 聊天模板化 Prompt

最早期的 LLM 是作为补全引擎来使用的——用户需要提供一段 Prompt，然后由模型继续往下补全，就像上面那两个例子那样。

这种方式对用户并不算友好，所以现在大多数模型都改成了使用“聊天模板化 Prompt（chat templated prompts）”的形式，也就是把和模型之间的交流表示成一段模拟对话。

但本质上，这仍然只是一种带有特殊格式的补全 Prompt，大概长这样：

```text
user: write a python function to download a file from a URL
assistant:
```

这个 Prompt 最自然的补全结果，就是由 assistant（也就是 LLM）回答用户的问题，并给出一段 Python 代码。

LLM 是无状态的：每次执行 Prompt 时，它们都会从同一块空白起点重新开始。

为了维持“对话正在持续进行”的这种模拟效果，和模型对话的软件必须自己维护状态，并在用户每次输入新的聊天 Prompt 时，把前面对话的全部内容重新回放一遍：

```text
user: write a python function to download a file from a URL
assistant: def download_url(url):
    return urllib.request.urlopen(url).read()
user: use the requests library instead
assistant:
```

由于提供商会同时对输入 Token 和输出 Token 收费，这就意味着：随着对话越来越长，每次新的 Prompt 都会越来越贵，因为输入 Token 的数量每轮都会继续增长。

## Token 缓存

大多数模型提供商会用“缓存的输入 Token（cached input tokens）”的较低费率，部分缓解这个问题——如果一段常见的 Token 前缀在短时间内已经处理过，底层基础设施就可以缓存并复用处理这些输入时那些昂贵的计算过程，因此这部分输入可以按更低价格计费。

编码智能体在设计时通常会把这种优化考虑进去——它们会尽量避免修改更早的对话内容，从而让缓存能够被尽可能高效地利用。

## 调用工具

LLM 智能体最关键的特征，就是它们可以调用工具。那么，工具到底是什么？

工具就是智能体外壳提供给 LLM 使用的函数。

在 Prompt 这一层面上，它看起来可能大概是这样：

```text
system: If you need to access the weather, end your turn with <tool>get_weather(city_name)</tool>
user: what's the weather in San Francisco?
assistant:
```

这时 assistant 可能会返回下面这样的文本：

```text
<tool>get_weather("San Francisco")</tool>
```

随后，模型外层的封装软件会从这段响应里提取出这个函数调用请求——很可能是通过正则表达式——然后真正去执行这个工具。

然后，它会把执行结果再返回给模型，对应构造出的 Prompt 大致如下：

```text
system: If you need to access the weather, end your turn with <tool>get_weather(city_name)</tool>
user: what's the weather in San Francisco?
assistant: <tool>get_weather("San Francisco")</tool>
user: <tool-result>61°, Partly cloudy</tool-result>
assistant:
```

这时，LLM 就可以利用这个工具返回结果，来帮助生成对用户问题的最终回答。

大多数编码智能体都会定义十几个甚至更多工具供智能体调用。其中最强大的一类工具，允许它们执行代码——例如用来执行终端命令的 `Bash()` 工具，或者用来运行 Python 代码的 `Python()` 工具。

## 系统提示词

在前面的例子里，我放入了一条标记为 “system” 的初始消息，用来告诉 LLM 当前有哪些可用工具，以及应当如何调用它们。

编码智能体通常会在每一轮对话开始时都带上一条这样的系统提示词（system prompt）。它不会展示给用户，但会向模型提供关于“你该如何行动”的指令。

这类系统提示词可能长达数百行。这里有一个截至 2026 年 3 月的 [OpenAI Codex system prompt 示例](https://github.com/openai/codex/blob/rust-v0.114.0/codex-rs/core/templates/model_instructions/gpt-5.2-codex_instructions_template.md)，它非常适合用来清楚理解：究竟是什么样的指令，让这些编码智能体能够运转起来。

## 推理

2025 年一个重要的新进展，是前沿模型家族开始引入推理（reasoning）能力。

在界面上，这种能力有时会被写成 thinking。它指的是：模型会先额外花一些时间生成一段文本，把问题和可能的解法先推演一遍，然后再向用户给出回复。

这看起来有点像人在出声思考，而它带来的效果也确实类似。关键在于，它允许模型为同一个问题投入更多时间——以及更多 Token——从而有机会得到更好的结果。

推理在调试代码时尤其有用，因为它给了模型一个机会去穿过更复杂的代码路径：一边混合使用工具调用，一边在推理阶段沿着函数调用链往回追踪，找到问题可能的根源。

很多编码智能体都提供了可以上调或下调推理强度的选项，用来鼓励模型在更难的问题上投入更多“咀嚼”时间。

## LLM + 系统提示词 + 工具循环

信不信由你，构建一个编码智能体，核心部分差不多就是这些了。

如果你想更深入理解这类系统的工作原理，一个很有价值的练习，就是亲手从零做一个自己的智能体。基于现有 LLM API，再加上几十行代码，你就能做出一个简单的工具循环。

当然，一个“好用”的工具循环，远不止这点工作量；但它最底层的机制，其实出奇地直接。
