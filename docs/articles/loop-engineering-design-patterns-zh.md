# 10 种 AI 开发者必知的循环工程设计模式（2026）

> 原文：[10 Loop Engineering Design Patterns for AI Builders (2026)](https://datasciencedojo.com/blog/loop-engineering-design-patterns/)  
> 作者：Data Science Dojo · 发布时间：2026 年 6 月 24 日

---

## 核心要点

- **循环工程（Loop Engineering）** 是设计 AI Agent 如何运行、检查自身工作并进行迭代的实践——而不仅仅是编写更好的提示词。
- 从基础的 ReAct 循环到生产环境控制模式（如熔断器和有界执行），共有 **10 种核心模式**。
- 选错模式是 Agent 系统在生产环境中失败的最常见原因之一——而大多数失败都是因为忽略了本列表中的**最后三种模式**。

---

## 什么是循环工程？

**循环工程** 是围绕 AI Agent 设计执行环境的实践。这包括触发器、停止条件、反馈机制和故障控制——它们决定了 Agent 如何运行。

从提示词工程（Prompt Engineering）到循环工程的转变，是一个逐渐加速的过程。**[ReAct 论文（2022）](https://arxiv.org/pdf/2210.03629)** 为研究者提供了一个在单一循环中结合推理（Reasoning）和行动（Action）的框架。到 2025 年年中，开发者已经在运行 "ralph" bash 脚本来自动化 Agent 迭代。到 2026 年 6 月，一篇关于该主题的文章在不到 24 小时内获得了 650 万次浏览，这个词已成为 Agent AI 领域的关注重心。

正如 Anthropic 公司 Claude Code 团队负责人 Boris Cherny 所指出的：他的角色已经从直接的模型提示词编写（prompting），转向了编写协调模型行为的外部**执行循环**。

关于循环工程从 ReAct 到 Ralph Loop，再到 Claude Code 和 Codex 中 `/goal` 命令的完整发展历史，请参阅我们关于 [Agent 循环的深度解析](https://datasciencedojo.com/blog/agentic-loops-explained-from-react-to-loop-engineering-2026-guide/)。

---

## 为什么设计模式在 Agent 循环中很重要

在循环中运行的 Agent 面临标准 LLM 使用中不存在的失败模式：

| 失败模式 | 说明 |
|----------|------|
| **无限反思循环** | 不断消耗 token 却毫无进展 |
| **幻觉式工具调用** | 触发产生实际后果的虚假工具调用 |
| **上下文窗口膨胀** | 窗口填满后输出质量悄然下降 |
| **失控的 token 消耗** | 未定义停止条件时持续烧钱 |

设计模式为这些失败模式赋予了名称和解决方案。以下十种模式源自三个来源：Andrew Ng 的四种基础模式、Anthropic 的五种工作流模式，以及 2025-2026 年间从实际工程团队中涌现的一组生产加固模式。

---

## 10 种循环工程设计模式

这些模式按三个层级组织：每个构建者都应首先理解的基础循环（Foundational Patterns）、用于实际工作流的实践者模式（Practitioner Patterns），以及用于大规模运行系统的生产控制模式（Production Controls）。

---

### 基础模式（1-4）

这些是构建块。如果你是循环工程的新手，在接触更复杂的内容之前，先从这里开始。

#### 模式 1：ReAct 循环（ReAct Loop）

> 来源：AI in Plain Language

Agent 系统的基础模式。ReAct 代表**推理（Reason）和行动（Act）**。Agent 在五个阶段之间循环——**感知（Perceive）、推理（Reason）、规划（Plan）、行动（Act）、观察（Observe）**——每个阶段衔接下一个，直到任务完成或触发停止条件。

每个主要的 AI 实验室（OpenAI、Anthropic、Google、Microsoft）都已收敛到相同的核心循环架构。它是本列表中其他所有内容的起点。

#### 模式 2：反思循环（Reflection Loop）

Agent 生成输出，然后在交付最终结果之前对其进行批评，找出其中的缺陷或错误。循环持续进行，直到输出通过自身的评估标准。

这是循环工程中最简单的自我纠错模式。适用于：

- 减少事实性输出中的幻觉
- 捕获生成代码中的不一致之处
- 在延迟不是首要考虑时提升质量

**局限性：** 它依赖 Agent 自身的判断作为验证器。对于需要外部验证的任务，模式 5 或模式 6 能给你更多控制。

#### 模式 3：工具使用循环（Tool Use Loop）

Agent 在循环中调用外部 API 和工具，以访问其训练数据之外的信息——当前价格、数据库记录、代码执行结果或专有系统。

工具使用是生产级 Agent 系统中最成熟的模式，也是下面大多数更复杂模式的构建块。关于它如何连接到使用 LangChain 和 LangGraph 的多 Agent 系统，[这篇教程](https://datasciencedojo.com/blog/langgraph-tutorial/) 值得收藏。

#### 模式 4：提示词链（Prompt Chaining）

一个 LLM 调用的输出按固定的确定性顺序成为下一个调用的输入。Agent 不决定下一步——代码决定。

在以下情况下使用这种循环工程模式：

- 任务可以分解为顺序明确的子任务
- 你需要高可靠性和可审计性而非灵活性
- 工作流中的每一步都需要在源代码中可追溯

[提示词链](https://www.promptingguide.ai/techniques/prompt_chaining) 位于控制谱的"工作流"端——高可预测性、低自主性。沿着本列表越往下走，Agent 获得的运行时决策权就越多。

---

### 实践者模式（5-7）

这些模式加入了现实世界的约束：外部验证、结构化批评和多 Agent 协调。

#### 模式 5：Ralph 循环（Ralph Loop）

> 来源：Dhanush Kumar

[Ralph 循环](https://github.com/snarktank/ralph) 让 Agent 在一个连续循环中运行，直到外部验证器确认成功。Agent 尝试执行任务，从编译器、代码检查工具（linter）或测试套件获取反馈，然后再次循环，直到所有检查通过。

这个名字来源于 Geoffrey Huntley 在 2025 年 7 月创建的一个 bash 单行命令，以《辛普森一家》中一边喊着"I'm helping"一边撞上门框的角色命名。这种幽默是刻意的：这个模式看起来简单甚至有些幼稚，但在实践中确实可靠地运行。

有两件事让它与**反思循环**不同：

- 退出条件来自确定性软件检查（测试通过、类型错误为零），而非 Agent 的自我评估
- 每次迭代重置上下文，防止长时间运行时上下文窗口退化

Claude Code 的 [**`/goal` 命令**](https://datasciencedojo.com/blog/claude-code-goal-command-vs-codex/) 就是这种循环工程模式的产品化版本。记录中最长的一次实验不间断运行了 25 小时，生成了 3 万行代码。

#### 模式 6：评估器-优化器循环（Evaluator-Optimizer Loop）

在这种 [模式](https://platform.claude.com/cookbook/patterns-agents-evaluator-optimizer) 中，第二个 Agent——评估器（evaluator）——审查主 Agent 的输出并返回结构化反馈。主 Agent 根据反馈修改其工作，循环持续直到评估器批准。

与**反思循环**的关键区别：批评者与生成者是分开的。一个专用的评估器让主 Agent 更难通过与"自己达成一致"来通过低质量工作。

这种循环工程模式适用于有明确质量标准的任务——代码审查、文档起草、结构化数据提取。

#### 模式 7：多 Agent 监督者循环（Multi-Agent Supervisor Loop）

一个监督者 Agent（Supervisor）协调多个专门的工人 Agent。每个工人在自己的内部循环中执行子任务，然后将结构化结果返回给监督者。监督者根据这些结果路由下一个任务。

一个监督者可能协调**研究员（Researcher）、编码员（Coder）和 QA Agent**——每个都有自己的工具、提示词和循环。监督者管理流程，不做具体工作。

结合检索功能构建在此模式之上？[Agent RAG](https://datasciencedojo.com/blog/agentic-rag/) 涵盖了监督者-工人模型如何与 LangGraph 中的多源检索相结合。关于 Agent 如何使用 MCP、A2A 和 ACP 跨框架通信，[Agent AI 通信协议指南](https://datasciencedojo.com/blog/agentic-ai-communication-protocols/) 深入介绍了互操作层。

---

### 生产加固模式（8-10）

这些模式不定义 Agent 做什么，而是定义什么条件下允许它继续运行。大多数生产环境中的循环工程失败，都是因为**跳过了这些模式**。

#### 模式 8：熔断器（Circuit Breaker）

熔断器在多次迭代之间监控 Agent 的进展。如果 Agent 陷入困境——在相同的文件状态之间交替、重复相同的错误、连续三个周期没有可衡量的进展——熔断器触发，终止循环并通知人工介入。

没有熔断器，一个卡住的 Agent 会无限消耗 token。这种模式直接应对循环工程中最昂贵的失败模式之一。

**实现步骤：**

1. 追踪每次迭代的进展信号（修改的文件、通过的测试、新错误 vs 重复错误）
2. 定义停滞条件（N 个周期内无新进展）
3. 触发时：记录完整状态，终止循环，发送告警
4. 只有在人工审查失败原因后才重新启动

#### 模式 9：心跳循环（Heartbeat Loop）

Agent 不是持续运行的。它按照时间表或事件唤醒，检查定义的条件，必要时执行操作，然后休眠直到下一次触发。

这种循环工程模式比持久运行的 Agent 更具成本效率，因为执行由心跳频率限制。PR 监控器、每日报告生成器或告警分类器都自然地适合这个模型。

**关键失败模式：** 心跳重叠。如果前一个周期仍在运行而下一个心跳触发时，两个 Agent 会同时工作在相同状态上。每个心跳实现都需要一个"循环进行中"的锁。

关于原生处理定时和事件驱动循环的框架，[这篇开源 Agent AI 工具汇总](https://datasciencedojo.com/blog/open-source-tools-for-agentic-ai/) 涵盖了当前的可选项。

#### 模式 10：有界执行与上下文工程（Bounded Execution and Context Engineering）

这两个模式几乎总是需要一起实现。

**有界执行** 将循环限制在定义的范围内：最大迭代次数、最大 token 消耗、最大运行时长。没有它，一个没有硬上限的循环最终会触碰到你未曾规划的边界——成本飙升、速率限制或超时。

**上下文工程** 控制 Agent 在每次迭代中携带哪些信息。随着循环运行时间变长，上下文窗口会填满，在你察觉之前输出质量就已经下降。上下文工程是在每个步骤中选择、压缩和隔离进入窗口内容的实践。

多 Agent 系统每次会话的成本比单 Agent 交互高出**至多 15 倍**。将这两个模式结合应用，是保持成本可控的主要机制。[Harness 工程指南](https://datasciencedojo.com/blog/harness-engineering/) 介绍了生产团队如何将这些约束嵌入基础设施而不仅仅是提示词中。

---

## 如何选择正确的模式

循环工程模式不是互斥的。大多数生产系统会组合使用多种模式。

一个常见的起步技术栈：

| 层级 | 模式 | 角色 |
|------|------|------|
| 基础执行 | **工具使用循环** | 基本执行模式 |
| 硬上限 | **有界执行** | 防止失控 |
| 监控 | **熔断器** | 停滞检测 |
| 扩展 | **多 Agent 监督者** | 超出单上下文窗口能力的任务 |

**通用原则：** 从最简单能工作的循环开始，只有在能衡量改进时才增加复杂性。一个带四种工具的单一 ReAct Agent 能处理大多数现实世界任务。完整的监督者循环加上熔断器和心跳，是长时间运行、高风险自主系统的正确工具——而不是默认起点。

---

## 常见问题（FAQ）

**什么是循环工程？**  
循环工程是围绕 AI Agent 设计执行环境的实践：触发器、停止条件、反馈机制和故障控制——这些决定了 Agent 在多个步骤中如何表现，而不仅仅是单次响应。它是提示词工程之上的一层。

**ReAct 循环和 Ralph 循环有什么区别？**  
ReAct 循环是 Agent 在周期中推理和行动的一般模式。Ralph 循环是一个特定实现，其中退出条件来自外部验证（测试通过、类型错误为零），而不是 Agent 自身的判断。Ralph 循环在编码任务中更可靠，因为 Agent 无法通过与"自己达成一致"来通过。

**我应该从哪种循环工程模式开始？**  
以 ReAct 循环和工具使用为基础开始。尽早加入**有界执行**——它是成本最低的生产防护措施。一旦有能自主运行的循环，就叠加**熔断器**。只有在单 Agent 循环确实无法处理任务时，才加入多 Agent 模式。

**循环工程与 Harness 工程有什么关系？**  
循环工程关注单个循环的设计。Harness 工程是构建基础设施——约束、工具链、反馈系统——使这些循环在多次会话中可靠且可复现的更广泛学科。循环工程是 Harness 内部的一层。

**我需要所有 10 种循环工程模式吗？**  
不需要。模式 1 到 4 是基础，大多数开发者会以某种形式使用全部。模式 8 到 10 在循环自主运行于生产环境后是不容妥协的。模式 5 到 7 取决于任务的复杂性以及单个 Agent 是否足够。

---

## 参考来源

| # | 引用 | 链接 |
|---|------|------|
| 1 | ReAct: Synergizing Reasoning and Acting in Language Models (2022) | [arxiv.org](https://arxiv.org/pdf/2210.03629) |
| 2 | Agentic Loops Explained: From ReAct to Loop Engineering (2026) | [datasciencedojo.com](https://datasciencedojo.com/blog/agentic-loops-explained-from-react-to-loop-engineering-2026-guide/) |
| 3 | Ralph Loop — GitHub | [github.com](https://github.com/snarktank/ralph) |
| 4 | Claude Code /goal Command vs Codex | [datasciencedojo.com](https://datasciencedojo.com/blog/claude-code-goal-command-vs-codex/) |
| 5 | Evaluator-Optimizer Agent Pattern — Anthropic Cookbook | [platform.claude.com](https://platform.claude.com/cookbook/patterns-agents-evaluator-optimizer) |
| 6 | Agentic RAG | [datasciencedojo.com](https://datasciencedojo.com/blog/agentic-rag/) |
| 7 | Agentic AI Communication Protocols (MCP, A2A, ACP) | [datasciencedojo.com](https://datasciencedojo.com/blog/agentic-ai-communication-protocols/) |
| 8 | Open-Source Tools for Agentic AI | [datasciencedojo.com](https://datasciencedojo.com/blog/open-source-tools-for-agentic-ai/) |
| 9 | Harness Engineering Guide | [datasciencedojo.com](https://datasciencedojo.com/blog/harness-engineering/) |
| 10 | LangGraph Tutorial | [datasciencedojo.com](https://datasciencedojo.com/blog/langgraph-tutorial/) |
| 11 | Prompt Chaining — Prompt Engineering Guide | [promptingguide.ai](https://www.promptingguide.ai/techniques/prompt_chaining) |
