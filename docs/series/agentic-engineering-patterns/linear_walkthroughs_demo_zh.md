# 线性讲解

原文标题：Linear walkthroughs
原文链接：https://simonwillison.net/guides/agentic-engineering-patterns/linear-walkthroughs/
原文作者：Simon Willison
访问日期：2026-03-25
原文发布日期：2026-02-25
原文最后修改：2026-03-04
译文版本：v0.1

## 译文说明

本文为 Simon Willison《Agentic Engineering Patterns》系列中《Linear walkthroughs》的示范中文版。标题采用“线性讲解”，而没有翻成更偏代码评审语境的“线性走查”，因为本文讲的不是正式的代码审查流程，而是让编码智能体按顺序、成体系地把一个代码库讲明白。正文继续沿用本项目既定术语约定，将 Coding Agent 统一译为“编码智能体”，并保留 Showboat、Claude Code、Opus 4.6、SwiftUI、`showboat note`、`showboat exec`、`sed`、`grep`、`cat` 等工具名、产品名与命令原文；`vibe coded` 延续译为“氛围编程（Vibe Coding）”语境下的表达，以保留该词在 AI 辅助开发讨论中的辨识度。

## 正文

> 所属主题：代码理解
> 上一篇：[让智能体做手动测试](./agentic_manual_testing_demo_zh.md)
> 下一篇：[交互式解释](./interactive_explanations_demo_zh.md)

有时候，让编码智能体对一个代码库做一份结构化的讲解，会非常有用。

它可能是一份你需要尽快上手的现有代码，也可能是你自己写过、但已经忘了细节的代码；又或者，整套东西本来就是你用氛围编程（Vibe Coding）一路 Prompt 出来的，现在你得真正搞清楚它到底是怎么工作的。

如果前沿模型配上合适的智能体运行框架，它们是可以构造出一份足够细致的讲解，帮助你理解代码实际工作方式的。

## 一个使用 Showboat 和 Present 的例子

我最近在自己的 Mac 上，用 Claude Code 和 Opus 4.6 氛围编程出了一个 [SwiftUI 幻灯片演示应用](https://simonwillison.net/2026/Feb/25/present/)。

当时我要讲的是 2025 年 11 月到 2026 年 2 月这段时间里前沿模型取得的进展，而我又喜欢在演讲里至少塞一个小 gimmick，也就是一个 [STAR moment](https://simonwillison.net/2019/Dec/10/better-presentations/)——Something They'll Always Remember。在这个例子里，我决定把这个 gimmick 放在演示的最后：揭晓整套幻灯片机制本身，其实就是氛围编程能做到什么的一次展示。

我把代码 [发布到了 GitHub](https://github.com/simonw/present)，然后才突然意识到，我根本不知道它到底是怎么工作的——整套东西几乎都是我一路 Prompt 出来的（[这里有一份部分对话记录](https://gisthost.github.io/?bfbc338977ceb71e298e4d4d5ac7d63c)），而我当时根本没有认真看它写出的代码。

于是我新开了一个 Claude Code for web 实例，把它指向我的仓库，然后给了它下面这段 Prompt：

> Read the source and then plan a linear walkthrough of the code that explains how it all works in detail
>
> Then run "uvx showboat --help" to learn showboat - use showboat to create a walkthrough.md file in the repo and build the walkthrough in there, using showboat note for commentary and showboat exec plus sed or grep or cat or whatever you need to include snippets of code you are talking about

[Showboat](https://github.com/simonw/showboat) 是我做的一个工具，专门用来帮助编码智能体编写能够展示自己工作过程的文档。你可以在[这里看到 `showboat --help` 的输出](https://github.com/simonw/showboat/blob/main/help.txt)。那份帮助文本本身就是为模型准备的，目的是把使用这个工具所需要知道的信息一次性都告诉它。

`showboat note` 命令会往文档里追加 Markdown 内容。`showboat exec` 命令则会接收一条 shell 命令，执行它，然后把这条命令和输出结果一起加进文档里。

我特意要求它使用“`sed` 或 `grep` 或 `cat`，或者任何你需要用来放进你正在讲解的代码片段的方式”，这样就能确保 Claude Code 不会手工把代码片段复制进文档，因为那样会引入幻觉或者抄错内容的风险。

这个方法效果非常好。你可以直接看这份[由 Claude Code 配合 Showboat 生成的文档](https://github.com/simonw/present/blob/main/walkthrough.md)：它把全部六个 `.swift` 文件都细致讲了一遍，并且对这套代码是如何工作的给出了清楚、可直接拿来用的解释。

我光是读这份文档，就学到了很多关于 SwiftUI 应用结构的东西，也顺手吸收了不少 Swift 语言本身的扎实细节。

如果你担心 LLM 会降低你学习新技能的速度，我会非常建议你采用这种模式。哪怕只是一个用氛围编程折腾出来、耗时大约 40 分钟的小玩具项目，也完全可以变成一次探索新生态、顺手学到一些有意思新技巧的机会。
