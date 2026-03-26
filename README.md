# Agentic Engineering Patterns 中文示范译文集

本仓库收录 Simon Willison《Agentic Engineering Patterns》系列的 15 篇中文示范译文，以及术语/风格指南模板与翻译方案说明。当前版本定位为公开交流与内部协作用的“示范译文包”，不是作者官方中文版。

如果你是第一次来到这里，可以把这份仓库直接当成一个围绕“如何与编码智能体协作开发更好软件”的中文专题首页：前半部分建立方法论，中段进入协作工作流、测试与代码理解，后半部分提供案例与可复用的 Prompt 资源。整套内容按原站 6 个大主题组织，既适合顺序通读，也适合按主题跳读。

## 首页导读

- 想先建立整体认知：从“核心原则”开始。
- 想直接进入工程实践：优先看“协作工作流”和“测试与质量保证”。
- 想快速感受落地方式：直接看“实战案例”和“参考资源”。

## 使用说明

这批文件的使用边界如下：第一，本文集为中文示范译文，不代表原作者官方授权中文版本；第二，目录顺序按原站指南页面的章节顺序整理，如需讨论“第几篇”，默认也按这个顺序理解；第三，代码、命令、URL、路径、文件名、产品名默认保留英文原文；第四，Prompt 默认保留英文原文，并在上下文中补充中文解释；第五，整体流程建议采用“AI 初译 + 人工精修 + 技术复核”。

## 六大主题导航

本系列默认按原站既有 6 个 section 组织，既保留 Simon Willison 原始编排逻辑，也方便中文读者按主题浏览。

### 1. 核心原则

这一组回答“什么是智能体工程，以及为什么要这样做”，对应原站 `Principles`。

- [什么是智能体工程？](./what_is_agentic_engineering_demo_zh.md) — 原文：[What is agentic engineering?](https://simonwillison.net/guides/agentic-engineering-patterns/what-is-agentic-engineering/)
- [现在，写代码很便宜](./writing_code_is_cheap_now_demo_zh.md) — 原文：[Writing code is cheap now](https://simonwillison.net/guides/agentic-engineering-patterns/code-is-cheap/)
- [把你会做的事囤起来](./hoard_things_you_know_how_to_do_demo_zh.md) — 原文：[Hoard things you know how to do](https://simonwillison.net/guides/agentic-engineering-patterns/hoard-things-you-know-how-to-do/)
- [AI 应该帮助我们产出更好的代码](./ai_should_help_us_produce_better_code_demo_zh.md) — 原文：[AI should help us produce better code](https://simonwillison.net/guides/agentic-engineering-patterns/better-code/)
- [反模式：有些事要避免](./anti_patterns_things_to_avoid_demo_zh.md) — 原文：[Anti-patterns: things to avoid](https://simonwillison.net/guides/agentic-engineering-patterns/anti-patterns/)

### 2. 协作工作流

这一组回答“如何把编码智能体真正纳入日常开发流程”，对应原站 `Working with coding agents`。

- [编码智能体如何工作](./how_coding_agents_work_demo_zh.md) — 原文：[How coding agents work](https://simonwillison.net/guides/agentic-engineering-patterns/how-coding-agents-work/)
- [如何将 Git 用于编码智能体工作流](./using_git_with_coding_agents_demo_zh.md) — 原文：[Using Git with coding agents](https://simonwillison.net/guides/agentic-engineering-patterns/using-git-with-coding-agents/)
- [子智能体](./subagents_demo_zh.md) — 原文：[Subagents](https://simonwillison.net/guides/agentic-engineering-patterns/subagents/)

### 3. 测试与质量保证

这一组聚焦“如何让智能体参与测试，同时不牺牲工程质量”，对应原站 `Testing and QA`。

- [红/绿 TDD](./red_green_tdd_demo_zh.md) — 原文：[Red/green TDD](https://simonwillison.net/guides/agentic-engineering-patterns/red-green-tdd/)
- [先跑测试](./first_run_the_tests_demo_zh.md) — 原文：[First run the tests](https://simonwillison.net/guides/agentic-engineering-patterns/first-run-the-tests/)
- [让智能体做手动测试](./agentic_manual_testing_demo_zh.md) — 原文：[Agentic manual testing](https://simonwillison.net/guides/agentic-engineering-patterns/agentic-manual-testing/)

### 4. 代码理解

这一组解决“如何让智能体帮助我们理解现有代码库”，对应原站 `Understanding code`。

- [线性讲解](./linear_walkthroughs_demo_zh.md) — 原文：[Linear walkthroughs](https://simonwillison.net/guides/agentic-engineering-patterns/linear-walkthroughs/)
- [交互式解释](./interactive_explanations_demo_zh.md) — 原文：[Interactive explanations](https://simonwillison.net/guides/agentic-engineering-patterns/interactive-explanations/)

### 5. 实战案例

这一组通过完整实例展示前面那些模式如何真正落地，对应原站 `Annotated prompts`。

- [用 WebAssembly 和 Gifsicle 构建 GIF 优化工具](./gif_optimization_tool_using_webassembly_and_gifsicle_demo_zh.md) — 原文：[GIF optimization tool using WebAssembly and Gifsicle](https://simonwillison.net/guides/agentic-engineering-patterns/gif-optimization/)

### 6. 参考资源

这一组收纳可反复复用的 Prompt 资产与补充材料，对应原站 `Appendix`。

- [我常用的 Prompt](./prompts_i_use_demo_zh.md) — 原文：[Prompts I use](https://simonwillison.net/guides/agentic-engineering-patterns/prompts/)

## 配套文件

配套文件包括：术语表与风格指南模板 [agentic_engineering_translation_glossary_style_guide_template.md](./agentic_engineering_translation_glossary_style_guide_template.md)，翻译方案报告 [research_report_agentic_engineering_patterns_translation_plan.md](./research_report_agentic_engineering_patterns_translation_plan.md)，双语链接映射表 [BILINGUAL_LINK_MAP.md](./BILINGUAL_LINK_MAP.md)，以及版本更新记录 [CHANGELOG.md](./CHANGELOG.md)。

## 当前发布状态

当前 15 篇示范译文已统一补齐基础页头信息，包括原文标题、原文链接、作者、访问日期、发布时间、最后修改时间、译文版本、译文说明与“## 正文”正文入口；同时已补充“所属主题 / 上一篇 / 下一篇”导航，并将首页与双语映射表统一改为 6 大主题分组展示。

此外，仓库已补齐第一版 MkDocs 静态站骨架：站点内容位于 `docs/`，当前专题已落位到 `docs/series/agentic-engineering-patterns/`，并预留了 `articles/`、`resources/` 与 `assets/` 目录，以便后续继续加入不相关的新文章、图片资源与公式渲染支持。站点配置见 [mkdocs.yml](./mkdocs.yml)，本地预览与 GitHub Pages 发布说明见 [docs/resources/deployment.md](./docs/resources/deployment.md)。

如果线上页面虽然能打开、但风格看起来像 GitHub Pages 默认文档页而不是 MkDocs Material，优先检查仓库 `Settings -> Pages` 是否仍设置为 `Deploy from a branch`。当前这套站点必须切到 `GitHub Actions`，否则 GitHub 很可能直接把 `docs/` 下的 Markdown 按 Jekyll 风格渲染出来。

若继续推进，下一步更自然的工作会是：逐篇检查站点内链接是否都切换到 `docs/` 目录下的相对路径；补几张示意图或封面图验证图片资源组织方式；再把仓库推到 GitHub，启用 Pages 并跑通首次自动部署。
