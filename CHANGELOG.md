# Changelog

## 2026-03-25

本次整理形成了首个可发布的中文示范译文包草案，完成内容包括：统一 15 篇译文的基础页头信息与结构入口；为此前缺失“## 正文”入口的文件补齐统一正文标题；新增项目主入口 `README.md`，集中说明项目定位、目录顺序、使用约定与配套文件；新增 `BILINGUAL_LINK_MAP.md`，明确中文译文文件与原文页面的双语映射关系。

本轮整理同时确认并固化了以下发布约定：整套文件按原站目录顺序组织；“Agentic Engineering”统一处理为“智能体工程（Agentic Engineering）”；代码、命令、URL、路径、文件名、产品名默认保留英文；Prompt 默认保留英文原文并在上下文补充中文解释；当前版本定位为“示范译文”，不是官方授权中文版。

同日又完成一次结构改版：`README.md` 从单表目录调整为按 6 大主题组织的首页式导航，并补充更适合首次访问者的导语与阅读路径；`BILINGUAL_LINK_MAP.md` 调整为按相同 6 大主题分段展示；15 篇译文统一补充“所属主题 / 上一篇 / 下一篇”导航，便于顺序通读和站点化发布。

后续若继续推进，建议优先做三类工作：第一，逐篇二次润色，进一步收敛长句、口语感和术语颗粒度；第二，补充对外发布说明，例如版权边界、引用方式和版本命名规则；第三，如需对外长期维护，可考虑生成静态目录页或站点化发布版本。

## 2026-03-26

本次继续把“站点化发布版本”真正落地为可运行骨架：仓库根目录新增 `mkdocs.yml`、`requirements-docs.txt`、`.github/workflows/deploy-pages.yml` 与 `.gitignore`；网站内容统一放入 `docs/`，并按 `index.md`、`series/`、`articles/`、`resources/`、`assets/` 分层组织。

同日还完成了当前专题的站点迁移：`Agentic Engineering Patterns` 已收拢到 `docs/series/agentic-engineering-patterns/`，并新增站点首页、专题总览页、专题首页、独立文章栏目说明、站点结构约定、公式与图片约定、发布与预览说明，以及 KaTeX 脚本和附加样式。

本地已通过 `mkdocs build --strict` 验证构建成功，因此当前仓库已经不是只有 Markdown 原稿，而是具备了直接推到 GitHub 后接入 Pages 的第一版静态站基础设施。后续如果继续推进，对外上线只需补齐仓库远端、开启 GitHub Pages，并根据需要继续细修导航、图片与文章内容。

同日补充了一次上线排障结论：仓库中的 `mkdocs.yml` 与 `.github/workflows/deploy-pages.yml` 配置本身可用，且公开可见的 `deploy-pages` 工作流已经成功执行；但如果 GitHub 仓库 `Settings -> Pages` 仍使用 `Deploy from a branch`（尤其是 `main` + `/docs`），线上会显示 Jekyll 默认样式，而不是 MkDocs Material。因此，发布说明中已显式补充“必须切换为 GitHub Actions”以及上线后如何快速验收实际发布产物。
