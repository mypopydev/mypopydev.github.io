# 子智能体

原文标题：Subagents
原文链接：https://simonwillison.net/guides/agentic-engineering-patterns/subagents/
原文作者：Simon Willison
访问日期：2026-03-25
原文发布日期：2026-03-17
原文最后修改：2026-03-17
译文版本：v0.1

## 译文说明

本文为 Simon Willison《Agentic Engineering Patterns》系列中《Subagents》的示范中文版。本文沿用本项目既定术语约定，将 Subagent 统一译为“子智能体”，将 Coding Agent 统一译为“编码智能体”，并继续保留 Context Window、Token、Claude Code、OpenAI Codex、Gemini CLI、Cursor 等高检索价值英文术语、产品名与链接。文中的 Prompt 示例默认保留英文原文，并在上下文中补充中文说明。标题采用“子智能体”，对应原文讨论的并不是“次级角色”，而是由父智能体派出、在独立上下文中完成特定任务的智能体实例。

## 正文

> 所属主题：协作工作流
> 上一篇：[如何将 Git 用于编码智能体工作流](./using_git_with_coding_agents_demo_zh.md)
> 下一篇：[红/绿 TDD](./red_green_tdd_demo_zh.md)

LLM 受限于它们的 **context limit**——也就是在任意时刻，它们的工作记忆里最多能容纳多少 Token。过去两年里，尽管 LLM 自身能力已经有了显著提升，这个数值却并没有增长太多：通常上限仍然在 1,000,000 左右，而各种基准测试也经常报告说，在低于 200,000 的范围内，结果质量反而更好。

精细地管理上下文、让它始终落在这些限制之内，是把模型效果用好的关键。

**子智能体**提供了一种简单但有效的办法：在不大量消耗编码智能体宝贵顶层上下文的前提下，处理更大的任务。

当一个编码智能体使用子智能体时，它本质上是在派出一个全新的“自己”的副本，去完成某个指定目标。这个副本拥有一个全新的 Context Window，从一段全新的 Prompt 开始。

## Claude Code 的 Explore 子智能体

Claude Code 在它的标准工作方式里大量使用子智能体。拿它来举例，会很直观。

每当你针对一个现有 repo 开启新任务时，Claude Code 首先都需要探索这个 repo，弄清它的大致结构，并找到完成任务所需的相关信息。

它的做法是先构造一段 Prompt，然后派出一个子智能体去执行这次探索，再返回它发现了什么的描述。

我曾给 Claude Code 启动过一轮会话，输入是一张[我那篇指南中的页面截图](https://simonwillison.net/guides/agentic-engineering-patterns/linear-walkthroughs/changes/)和下面这段 Prompt：

> Make the chapter diffs also show which characters have changed in this diff view with a darker color of red or green for the individually changed segments of text within the line

这段 Prompt 的意思是：在这个 diff 视图里，不仅要显示哪些行发生了变化，还要把每一行内部具体变动过的字符，用更深的红色或绿色标出来。

[这里是那次会话的完整 transcript](https://gisthost.github.io/?effbdc564939b88fe5c6299387e217da/index.html)。

Claude Code 的起手动作，是先运行一个 “Explore” 子智能体。它给这个子智能体的起始 Prompt 如下：

> Find the code that implements the diff view for "chapters" in this Django blog. I need to find:
>
> 1.  Templates that render diffs (look for diff-related HTML/CSS with red/green backgrounds)
> 2.  Python code that generates diffs (look for difflib usage or similar)
> 3.  Any JavaScript related to diff rendering
> 4.  CSS styles for the diff view (red/green line backgrounds)
>
> Search thoroughly - check templates/, static/, blog/ directories. Look for keywords like "diff", "chapter", "revision", "history", "compare".

也就是说，它先把任务拆成一份更明确的内部搜索说明：要去哪些目录、查哪些关键词、把模板、Python 代码、JavaScript 和 CSS 各自找出来。

子智能体的工作方式，和其他工具调用很像：父智能体像调用别的工具一样派出它们，然后等待返回结果。模型会这样给自己写 Prompt，这件事很有意思——而且它们通常确实挺会写 Prompt。

那个 Explore 子智能体运行了几秒钟，返回的结果开头大概是这样的：

> 太好了！现在我来整理一份包含全部发现的综合摘要：
>
> ### 摘要：Chapter Diff View 的实现
>
> 我已经找到了这个 Django blog 中 chapter diff 视图的完整实现。关键组件如下：
>
> #### 1. **Python 代码：diff 生成**（`/home/user/simonwillisonblog/guides/views.py`，第 139-202 行）
>
> `chapter_changes()` 这个 view function 使用 Python 内置的 `difflib.unified_diff()` 来生成 diff：……

这个子智能体的完整返回结果里，已经包含了父智能体开始修改代码、满足我原始需求所需要的全部细节。

## 并行子智能体

前面这个 Explore 子智能体，是子智能体工作方式里最简单的一种例子：父智能体暂停，等待子智能体跑完。它最大的好处在于，子智能体可以在一个全新的上下文里工作，从而避免消耗父智能体可用额度里的 Token。

子智能体还可以带来很可观的性能提升：父智能体可以同时运行多个子智能体，甚至还可以给这些任务配上更快、更便宜的模型，例如 Claude Haiku，从而进一步加速。

支持子智能体的编码智能体，也可以按照你的指令来这样用它们。你可以试试这样的 Prompt：

```text
Use subagents to find and update all of the templates that are affected by this change.
```

这句话的意思是：用子智能体去找出并更新所有受这次改动影响的模板。

对于那种需要同时修改多个文件、而这些文件彼此又没有依赖关系的任务，这种做法可以明显提速。

## 专业化子智能体

有些编码智能体允许对子智能体再做进一步定制，通常是通过自定义 system prompt、自定义工具，或者两者同时使用，让这些子智能体承担不同角色。

这些角色可以覆盖很多有用的专长：

*   **代码审查**智能体可以审查代码，并识别 bug、功能缺口或设计上的薄弱点。
*   **测试运行**智能体可以跑测试。如果你的测试套件很大、输出又很冗长，这就尤其值得，因为子智能体可以把完整测试输出挡在主编码智能体之外，只回报失败细节。
*   **调试**智能体可以专门负责调试问题，把它自己的 Token 配额花在阅读代码库、运行代码片段、隔离复现步骤，以及确定 bug 根因这些事情上。

不过，把任务过度拆散到几十个不同的专业化子智能体上，确实很容易让人上头；但要记住，子智能体真正的价值，主要还是保住那份宝贵的根上下文，并处理那些特别耗 Token 的操作。只要 Token 还够用，你的根编码智能体本来就完全有能力自己调试，也有能力自己审查它产出的结果。

## 官方文档

目前已经有几款流行的编码智能体支持子智能体，而且各自都提供了如何使用它们的文档：

*   [OpenAI Codex subagents](https://developers.openai.com/codex/subagents/)
*   [Claude subagents](https://code.claude.com/docs/en/sub-agents)
*   [Gemini CLI subagents](https://geminicli.com/docs/core/subagents/)
*   [Mistral Vibe subagents](https://docs.mistral.ai/mistral-vibe/agents-skills#agent-selection)
*   [OpenCode agents](https://opencode.ai/docs/agents/)
*   [Subagents in Visual Studio Code](https://code.visualstudio.com/docs/copilot/agents/subagents)
*   [Cursor Subagents](https://cursor.com/docs/subagents)
