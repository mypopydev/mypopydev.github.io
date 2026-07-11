# 循环入门（Getting started with loops）

最近关于"设计循环（designing loops）"而非给编码智能体下 Prompt 的讨论很多。如果你在 X 上花点时间想弄清楚"循环"究竟是什么，会发现各种说法都有。

在 Claude Code 团队，我们把**循环定义为：智能体不断重复工作周期，直到满足某个停止条件**。我们按以下维度把循环分成几类：

- 如何被触发
- 如何停止
- 用到了哪个 Claude Code 原语
- 每类循环最适合什么类型的任务

接下来我们会介绍主要的循环类型、各自的适用场景，以及如何在控制 Token 用量的同时维持代码质量。并非所有任务都需要复杂的循环；请从最简单的方案入手，有针对性地选用这些模式。

## 基于轮次的循环（Turn-based loops）

- **触发方式**：用户的一条 Prompt。
- **停止标准**：Claude 判断任务已完成，或需要更多上下文。
- **最佳用途**：不属于固定流程或日程的较短任务。
- **用量控制**：写更具体的 Prompt，并用 Skill 改进验证，以减少轮次。

你发出的每条 Prompt 都会开启一个手动循环，由你来主导每一轮。Claude 收集上下文、采取行动、检查自己的工作，必要时重复，最后给出回应。我们把这称为智能体式循环（agentic loop）。

例如，你让 Claude 创建一个"点赞"按钮。它会读取你的代码、做出修改、运行测试，然后交回一个它_认为_能用的结果。接着由你手动检查成果，再写下一条 Prompt。

你可以通过编写 `SKILL.md` 将你的手动步骤固化下来，从而改进验证环节，让 Claude 能够端到端地自查更多工作。（关于如何选择 skills、hooks 和 subagents 来做这类自动化，可参阅我们的[驾驭 Claude Code](https://claude.com/blog/steering-claude-code-skills-hooks-rules-subagents-and-more) 指南。）其中应包含工具或连接器，让 Claude 能够_看见_、_度量_或与结果_交互_。检查越量化，Claude 自我验证就越容易。

举例来说，你可以在 `SKILL.md` 中这样写：

```plaintext
---
name: verify-frontend-change
description: Verify any UI change end-to-end before declaring it done.
---

# 验证前端改动
任何 UI 改动都不应仅凭编辑成功就宣布完成。以人类审查者的方式进行验证：

1. 启动开发服务器，在浏览器中打开修改后的页面。

2. 直接与改动交互。对于新的控件（按钮、输入框、开关）：点击它，确认状态变化符合预期，并截取前后对比截图。

3. 检查浏览器控制台：应无新增错误或警告。

4. 使用 Chrome Devtools MCP，运行性能追踪（performance trace）并审计 Core Web Vitals。

如果任何步骤失败，修复问题后从第 1 步重新运行——切勿将未完全验证的工作交回。
```

## 基于目标的循环（Goal-based loop，/goal）

- **触发方式**：实时中的手动 Prompt。
- **停止标准**：目标达成，**或**达到最大轮次。
- **最佳用途**：具有可验证退出标准的任务。
- **用量控制**：设定明确的完成标准与显式轮次上限，例如"尝试 5 次后停止"。

有些时候，单轮并不够，尤其是较复杂的任务。智能体在能够迭代时会表现更好。你可以用 `/goal` 来定义"完成"长什么样，从而延长 Claude 持续迭代的时间。

一旦你定义了成功标准，Claude 就无需自行判断"够好了吗"而提前结束循环。每次 Claude 试图停下时，一个评估模型（evaluator model）会检查你的条件，并在目标达成前（或达到你设定的轮次前）把它打回去继续工作。

正因如此，像"通过的测试数量"或"达到某个分数阈值"这类确定性标准才格外有效。

例如：

```plaintext
/goal get the homepage Lighthouse score to 90 or above, stop after 5 tries.
```

## 基于时间的循环（Time-based loop，/loop 与 /schedule）

- **触发方式**：指定的时间间隔。
- **停止标准**：你手动取消，或工作完成（PR 已合并、队列已清空）。
- **最佳用途**：周期性工作，或与外部环境 / 系统对接。
- **用量控制**：设置更长的间隔，或改为基于事件而非基于时间触发。

有些智能体工作是周期性的：任务不变，只是输入在变。比如每天早上汇总 Slack 消息。还有些工作依赖外部系统，而与某个外部系统对接的简单方式就是按间隔去检查它、并对变化做出反应——例如一个可能收到代码评审或 CI 失败的 PR。

对此，你可以用 `/loop` 让 Claude 按间隔重跑某条 Prompt。例如：

```plaintext
/loop 5m check my PR, address review comments, and fix failing CI
```

`/loop` 运行在你的电脑上，所以一旦关闭，它就停了。你也可以用 `/schedule` 创建一个 routine（例程），把循环搬到云端。

## 主动式循环（Proactive loops）

- **触发方式**：由事件或日程触发，无实时人工参与。
- **停止标准**：每个任务在目标达成时退出；routine 本身则一直运行，直到你关闭它。
- **最佳用途**：稳定且定义清晰的重复性工作流：缺陷报告、议题分诊、迁移、依赖升级等。
- **用量控制**：把 routine 路由到更小、更快的模型，而把能力最强的模型留给需要判断的环节。

上述原语，加上 Claude Code 的其他特性如 **auto 模式** 与 **动态工作流（dynamic workflows，研究预览）**，可以组合成一个用于长时间运行工作的循环。

例如，要处理源源不断的反馈，你可以这样组合：

1. 用 **`/schedule`**（研究预览）运行一个 routine，检查是否有新报告
2. 用 **`/goal`** 定义"完成"长什么样，并用 **Skill** 记录如何验证
3. 用 **动态工作流（Dynamic workflows）** 编排多个智能体，对每个报告做分诊、修复并审查修复结果
4. 用 **Auto 模式** 让 routine 在运行中不暂停请求权限

把这些合起来，一条 Prompt 大致会长这样：

```plaintext
/schedule every hour: check #project-feedback for bug reports. /goal: don't stop until every report found this run is triaged, actioned, and responded to. When fixing a bug, use a workflow to explore three solutions in parallel worktrees and have a judge adversarially review them.
```

## 维持代码质量

循环产出的质量，取决于它所处的整个系统。在设计系统时：

- **保持代码库本身整洁**：Claude 会遵循你代码库中已经存在的模式与约定。
- **给 Claude 一种自查工作的方式**：用 [Skill](https://code.claude.com/docs/en/skills) 把"对你和团队而言什么算好"写下来。
- **让文档易于触达**：框架与库的文档里有最新的最佳实践。
- **用第二个智能体做代码审查**：带着全新上下文的审查者偏见更小，也不会受主智能体推理过程的影响。你可以使用内置的 `/code-review` Skill，或用于 GitHub 的 [Code Review](https://code.claude.com/docs/en/code-review)。

当某次结果不达标时，不要止步于修复这一个具体问题，而要尝试把它固化下来，从而改进系统、让今后的每一轮都更好。

## 管理 Token 用量

要管理 Token 用量，循环应有清晰的边界：

- **为任务选对原语与模型**：较小的任务不需要多个智能体或循环；有些任务可以用更便宜、更快的模型。
- **定义清晰的成功与停止标准**：具体说明"完成"长什么样，让 Claude 能更早抵达方案（但别太早）。
- **大批量前先试点**：动态工作流可能派生出成百上千个智能体。先用工作的一小部分估一下用量。
- **用脚本处理确定性工作**：跑一个脚本比一步步推理步骤更省。例如，一个 PDF Skill 可以附带一个填表脚本，让 Claude 每次直接运行，而不是重新推导一遍代码。
- **不要比需要更频繁地运行 routine**：把间隔匹配到你所关注事物的变化频率。
- **审查用量**：`/usage` 命令按 Skill、子智能体、MCP 拆解近期用量；不带参数的 `/goal` 会显示到目前为止的轮次与 Token 用量；`/workflows` 显示每个智能体的 Token 用量，且你可以随时停止某个智能体。

## 入门

总结一下：

| 循环类型 | 你放手的环节 | 适用场景 | 使用方式 |
| --- | --- | --- | --- |
| 基于轮次（Turn-based） | 检查（The check） | 你正在探索或做决策 | 自定义验证 Skill |
| 基于目标（Goal-based） | 停止条件（The stop condition） | 你清楚"完成"长什么样 | `/goal` |
| 基于时间（Time-based） | 触发器（The trigger） | 工作在项目之外按日程发生 | `/loop`、`/schedule` |
| 主动式（Proactive） | Prompt（The prompt） | 工作是周期性的、且定义清晰 | 以上全部，外加动态工作流 |

要开始用循环，先看看你已经在做的工作。挑一个你成为瓶颈的任务，想想其中哪一块可以交出去：你能写出验证检查吗？目标足够清晰吗？工作是按日程到来的吗？

一旦有了想法，就跑起这个循环，观察结果——比如它卡在哪里、或过度伸到了哪里——别害怕对它反复迭代。

想了解更多，请阅读 Claude Code 文档中关于[并行运行智能体](https://code.claude.com/docs/en/agents)的章节，以及 [loop](https://code.claude.com/docs/en/goal)、[schedule](https://code.claude.com/docs/en/routines)、[goal](https://code.claude.com/docs/en/goal)、[dynamic workflows](https://code.claude.com/docs/en/workflows#orchestrate-subagents-at-scale-with-dynamic-workflows) 这几个页面。

_本文由 Delba de Oliveira 与 Michael Segner 撰写_
