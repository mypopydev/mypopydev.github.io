# 更新记录

### 2026-07-29
- 新增译文：软件工厂为何失败（Why Software Factories Fail，HumanLayer / Dex，2026）
- 收录 HumanLayer 文章《Why Software Factories Fail》中文译文，置于 `docs/articles/why-software-factories-fail-zh.md`
- 导航：智能体工程 > 独立译文（新增一篇）；首页智能体工程区块新增入口
- 配图本地化：下载原文全部 29 张图至 `docs/assets/images/articles/why-software-factories-fail/`（含 loop-engineering、ryan-lop、faros-code-review/incidents-and-bugs、software-factory 系列、software-factory-lights-off 系列、better-dimensions、claude-code-revenue、swe-agent-tools、bench-task、bad-code 1/2、sota-backprop、sota-changes、frontier-code、lights-on-agentic-1、product-review 系列、dillon_tweet 等）
- 配置：mkdocs.yml 启用 `footnotes` 扩展，以渲染原文 [^1]…[^6] 脚注
- 视频（4 个 GitHub user-attachments 演示 + 多个 YouTube）保留原始外链；YouTube 缩略图保留外链
- 术语表追加 software factory / lights-off software factory / vertical slices / tracer bullets / front-loading alignment / shotgun surgery / brownfield / maintainability / RLVR 等术语
- 原文外链（约 60+ 条，含 OpenAI、StrongDM、Faros AI、FT、arXiv、Wikipedia、X 等）全部保留

### 2026-07-21
- 新增译文：苦涩的教训（Rich Sutton, 2019-03-13）
- 术语表追加 8 项 AI/强化学习术语
- 保留原文所有外链

### 2026-07-15
- 新增译文：TPU 与 GPU 集群内部：集合通信剖析（Aleksa Gordić, 2026-07-14）
- 导航新增「训练系统与集群」栏目
- 术语表追加 32 项集合通信/硬件术语
- 保留原文所有外链；配图落地本地化
- 译文纳入 MkDocs 站点严格构建

## 2026-07-09

**新增《面向自我提升的 Harness 工程（Harness Engineering for Self-Improvement）》译文**

- 收录 Lilian Weng 博文《Harness Engineering for Self-Improvement》（2026-07-04，约 6,400 词）中文译文，置于 `docs/articles/harness-engineering-zh.md`
- 导航：智能体工程 > 独立译文（第 5 篇）；首页智能体工程区块新增入口
- 配图本地化：下载原文全部 17 张图至 `docs/assets/images/articles/harness-engineering/`（openai-agent-loop、coding-harness-loop、ace、mce、meta-harness 系列、ai-scientist、autodata、adas、aflow 系列、STOP 系列、self-harness、alphaevolve 系列、SIA 等）
- 数学：ACE/MCE 双层优化、STOP 元效用与递归更新等 LaTeX 公式按原文重建并由 arithmatex 渲染
- 代码：BibTeX 引用块、工具名（`glob`/`spawn_agent`/`# EVOLVE-BLOCK-START` 等）、模型代号（`Claude 3.5 Sonnet`、`GLM-5` 等）原样保留
- 术语表追加 harness、RSI、上下文工程、ACE、MCE、元 harness、Self-Harness、STOP、奖励作弊、进化搜索、AlphaEvolve/AFlow/ADAS/DGM/SIA 等术语
- 原文外链（含 arXiv、Nature、LessWrong 等约 70 条）与 35 条参考文献全部保留

## 2026-07-08

**新增《从零实现浮点运算：困难模式（Floating point from scratch: Hard Mode）》译文**

- 收录 Julia Desmazes 博文《Floating point from scratch: Hard Mode》（2026-04-03，约 9,355 词）中文译文，置于 `docs/articles/floating-point-from-scratch-hard-mode-zh.md`
- 导航：新增顶层板块「浮点与芯片设计」；首页新增对应区块入口
- 配图本地化：下载原文全部 18 张图至 `docs/assets/images/articles/floating-dragon/`（含 sky130 原理图/版图 SVG、各 floorplan/芯片渲染、placement.gif、waffles.webp 等）
- 数学：保留原文 LaTeX 公式，交由本站 arithmatex 渲染（bfloat16 表示、ulp、误差公式等）
- 代码：C / C++ / Verilog / x86 汇编 / 纯文本代码块原样保留
- 术语：浮点领域术语在文末「术语对照」表中统一，未污染智能体工程术语表
- 原文外链（约 31 条）与 mailto 全部保留

## 2026-07-07

**新增《循环入门（Getting started with loops）》译文**

- 收录 Claude Code 团队（Delba de Oliveira & Michael Segner）博文《Getting started with loops》（2026-06-30）中文译文，置于 `docs/articles/getting-started-with-loops-zh.md`
- 导航：智能体工程 > 独立译文（第 4 篇）；首页智能体工程区块新增入口
- 术语表追加 turn-based / goal-based / time-based / proactive loop、stop condition、evaluator model、auto 模式、dynamic workflows、research preview 等循环类型术语
- 保留原文外链（Claude Code 文档 skills / agents / goal / routines / workflows / code-review）与全部命令（`/goal`、`/loop`、`/schedule` 等）

## 2026-07-06

**新增《智能体式代码审查（Agentic Code Review）》译文**

- 收录 Addy Osmani 博文《Agentic Code Review》（2026-06-15）中文译文，置于 `docs/articles/agentic-code-review-zh.md`
- 配图本地化至 `docs/assets/images/articles/agentic-code-review/code-review.jpg`
- 导航：智能体工程 > 综合概览；首页智能体工程区块新增入口
- 术语表追加 Agentic Code Review / blast radius / verification bottleneck / triage / heterogeneous reviewers 等
- 保留原文 21 个外链（经与实时原文逐条 diff，全部精确匹配；站点外壳链接正确排除）；无配图远程依赖

**调整导航结构（智能体工程板块）**

- 将「综合概览」重命名为「独立译文」，集中放置三篇非系列单篇译文（30 概念、循环工程、智能体式代码审查），与 Simon Willison《Agentic Engineering Patterns》系列各主题子项明确区分「系列 vs 单篇」

## 2026-07-05

**新增《循环工程（Loop Engineering）》译文**

- 收录 Addy Osmani 博文《Loop Engineering》（2026-06-07）中文译文，置于 `docs/articles/loop-engineering-zh.md`
- 导航：智能体工程 > 综合概览（与 30 概念并列）；首页智能体工程区块新增入口
- 术语表追加 Loop Engineering / Automations / cognitive surrender / comprehension debt / intent debt / orchestration tax / Maker-Checker 等 coined 术语
- 保留原文 18 个外链（X 引用、Addy 博客、Codex 文档）；原文无配图

**修订《30 个智能体工程核心概念》译文（v0.1 → v0.2）**

- 第二轮句级准确性复核：补全 15 处遗漏（量化数据、工具名、示例句），无事实性误译
  - §9 补回 GPT-5.5（98.1%/74.0%）、Claude Opus 4.7（59.2%→32.2%）及 arxiv 2602.11988 研究
  - §10 补回延迟加载 token 对比（607 / 5,500 / 300）及 Exa 工具栈
  - §12 补回 Exa 作为首选 AI 原生搜索引擎
  - §6 SkillsBench（11 领域 / 86 任务，27.7% vs 22.0%）、§7 Superpowers HARD-GATE、§17 Ralph loop、§20 Cloudflare Dynamic Workers、§25 Ruff/Bandit 等
- 链接：按术语表 §6.4 补回 25 个原始 URL（含 Ralph loop）；跳过 Medium 付费绕行 `?sk=` 链接（决策：不插入正文）
- 链接基准来源说明：Medium 抓取截断，权威原文基准采用作者 newsletter 重发版（newsletter.systemdesign.one）+ teamstation.dev 镜像交叉校验
- 结构调整：移除译文头部元信息块（原文标题/链接/作者/日期/版本/译者/审校）与「译文说明」节；两处原文缺口说明已内联于正文 [译者注]

## 2026-07-04

**新增「智能体工程 > 综合概览」**

- 收录《30 Core Agentic Engineering Concepts Every Developer Should Know》中文译文，置于 `docs/articles/30-core-agentic-engineering-concepts-zh.md`
- 导航新增「综合概览」子项，首页智能体工程区块新增入口
- 术语表追加 Observability / Tracing / Logging / Metrics / Replay / Hook / Permission / Orchestration / Prompt Caching / Context Rot 共 10 个术语
- 备注：第 26 节（可观测性）原文仅一段引导语；第 29 节（回放）依据 teamstation.dev 镜像补全（Medium 抓取缺失）

## 2026-05-25

**新增「数学考证」栏目**

- 收录《"齐次"一词在中文数学术语中的形成》一文，置于 `docs/articles/homogeneous-chinese-translation-etymology-zh.md`
- 导航与首页增加「数学考证」入口

## 2026-04-06

**个人站点化改造**

- 站点名称从"技术专题与研究笔记"更名为"Barry's Tech Notes"
- 首页重写为面向读者的欢迎页，不再是项目说明文档
- 导航结构精简为三大板块：智能体工程 / 深度学习 / 关于
- 移除导航中的内部维护文档（站点结构约定、公式约定、发布说明、研究报告），改为仅供仓库维护参考
- 添加亮色/暗色模式切换、配色方案、社交链接和页脚信息
- 各索引页从面向维护者的语气重写为面向读者的语气

**仓库清理**（同日早些时候完成）

- 删除根目录 15 个 `*_demo_zh.md` 旧副本（正式版在 `docs/series/`）
- 迁移 5 篇研究报告到 `docs/resources/research-reports/`
- 删除根目录重复的 BILINGUAL_LINK_MAP.md、术语表模板和 CHANGELOG.md
- 确保 Single Source of Truth：所有正式内容统一位于 `docs/` 下

## 2026-03-26

站点化骨架落地：MkDocs 配置、GitHub Actions 工作流、内容迁移到 `docs/` 目录。

完成 Pages 排障：确认必须在 GitHub 仓库 Settings → Pages 中将 Source 切换为 GitHub Actions。

## 2026-03-25

首个可发布中文示范译文包草案：统一 15 篇译文的页头信息与结构、按 6 大主题组织、新增双语链接映射表。
