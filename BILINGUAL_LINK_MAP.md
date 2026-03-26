# 双语链接映射说明

本文用于把当前中文示范译文文件与 Simon Willison 原站页面做一一对应，便于校对、引用、后续批量替换链接或发布时生成导航。

## 映射规则

中文文件名统一采用“原英文 slug 或语义文件名 + `_demo_zh.md`”的形式，表示“示范中文译文”；原文链接统一指向 Simon Willison 指南站中的对应页面。若后续转为正式发布版，可以在不改变原文链接映射关系的前提下，将中文文件另行复制为正式命名版本。

## 按 6 个主题分组的双语映射

### 1. 核心原则（Principles）

| 序号 | 中文文件 | 中文标题 | 原文标题 | 原文 URL |
| --- | --- | --- | --- | --- |
| 1 | `what_is_agentic_engineering_demo_zh.md` | 什么是智能体工程？ | What is agentic engineering? | `https://simonwillison.net/guides/agentic-engineering-patterns/what-is-agentic-engineering/` |
| 3 | `writing_code_is_cheap_now_demo_zh.md` | 现在，写代码很便宜 | Writing code is cheap now | `https://simonwillison.net/guides/agentic-engineering-patterns/code-is-cheap/` |
| 4 | `hoard_things_you_know_how_to_do_demo_zh.md` | 把你会做的事囤起来 | Hoard things you know how to do | `https://simonwillison.net/guides/agentic-engineering-patterns/hoard-things-you-know-how-to-do/` |
| 5 | `ai_should_help_us_produce_better_code_demo_zh.md` | AI 应该帮助我们产出更好的代码 | AI should help us produce better code | `https://simonwillison.net/guides/agentic-engineering-patterns/better-code/` |
| 6 | `anti_patterns_things_to_avoid_demo_zh.md` | 反模式：有些事要避免 | Anti-patterns: things to avoid | `https://simonwillison.net/guides/agentic-engineering-patterns/anti-patterns/` |

### 2. 协作工作流（Working with coding agents）

| 序号 | 中文文件 | 中文标题 | 原文标题 | 原文 URL |
| --- | --- | --- | --- | --- |
| 2 | `how_coding_agents_work_demo_zh.md` | 编码智能体如何工作 | How coding agents work | `https://simonwillison.net/guides/agentic-engineering-patterns/how-coding-agents-work/` |
| 7 | `using_git_with_coding_agents_demo_zh.md` | 如何将 Git 用于编码智能体工作流 | Using Git with coding agents | `https://simonwillison.net/guides/agentic-engineering-patterns/using-git-with-coding-agents/` |
| 8 | `subagents_demo_zh.md` | 子智能体 | Subagents | `https://simonwillison.net/guides/agentic-engineering-patterns/subagents/` |

### 3. 测试与质量保证（Testing and QA）

| 序号 | 中文文件 | 中文标题 | 原文标题 | 原文 URL |
| --- | --- | --- | --- | --- |
| 9 | `red_green_tdd_demo_zh.md` | 红/绿 TDD | Red/green TDD | `https://simonwillison.net/guides/agentic-engineering-patterns/red-green-tdd/` |
| 10 | `first_run_the_tests_demo_zh.md` | 先跑测试 | First run the tests | `https://simonwillison.net/guides/agentic-engineering-patterns/first-run-the-tests/` |
| 11 | `agentic_manual_testing_demo_zh.md` | 让智能体做手动测试 | Agentic manual testing | `https://simonwillison.net/guides/agentic-engineering-patterns/agentic-manual-testing/` |

### 4. 代码理解（Understanding code）

| 序号 | 中文文件 | 中文标题 | 原文标题 | 原文 URL |
| --- | --- | --- | --- | --- |
| 12 | `linear_walkthroughs_demo_zh.md` | 线性讲解 | Linear walkthroughs | `https://simonwillison.net/guides/agentic-engineering-patterns/linear-walkthroughs/` |
| 13 | `interactive_explanations_demo_zh.md` | 交互式解释 | Interactive explanations | `https://simonwillison.net/guides/agentic-engineering-patterns/interactive-explanations/` |

### 5. 实战案例（Annotated prompts）

| 序号 | 中文文件 | 中文标题 | 原文标题 | 原文 URL |
| --- | --- | --- | --- | --- |
| 14 | `gif_optimization_tool_using_webassembly_and_gifsicle_demo_zh.md` | 用 WebAssembly 和 Gifsicle 构建 GIF 优化工具 | GIF optimization tool using WebAssembly and Gifsicle | `https://simonwillison.net/guides/agentic-engineering-patterns/gif-optimization/` |

### 6. 参考资源（Appendix）

| 序号 | 中文文件 | 中文标题 | 原文标题 | 原文 URL |
| --- | --- | --- | --- | --- |
| 15 | `prompts_i_use_demo_zh.md` | 我常用的 Prompt | Prompts I use | `https://simonwillison.net/guides/agentic-engineering-patterns/prompts/` |

## 备注

若后续需要做外部发布页，可以直接把本表作为导航数据源使用；若需要新增“原站目录顺序编号”“发布日期”“译文版本”等字段，也建议继续在本文件维护，而不是散落到多个说明文件里。
