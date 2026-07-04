# 更新记录

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
