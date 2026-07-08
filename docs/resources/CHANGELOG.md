# 更新记录

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
