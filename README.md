# 技术专题与研究笔记

本仓库是一个基于 MkDocs Material 的中文静态文档站，当前收录 Simon Willison《Agentic Engineering Patterns》系列的 15 篇中文示范译文，以及独立技术文章、术语表和翻译配套资料。

> **在线阅读**：站点已部署到 GitHub Pages，推送到 `main` 分支后由 GitHub Actions 自动构建发布。

## 快速开始

```bash
# 安装依赖
pip install -r requirements-docs.txt

# 本地预览
mkdocs serve
```

浏览器打开 `http://127.0.0.1:8000` 即可预览站点。

## 站点结构

```
docs/
├── index.md                     # 站点首页
├── series/                      # 专题（成组系列文章）
│   └── agentic-engineering-patterns/   # 当前专题：15 篇译文
├── articles/                    # 独立文章（不属于任何专题）
├── resources/                   # 配套资源（术语表、映射表、约定文档）
│   └── research-reports/        # 项目推进过程中的研究报告
└── assets/                      # 图片、样式、脚本
    ├── images/
    ├── stylesheets/
    └── javascripts/
```

所有正式内容均位于 `docs/` 目录下，根目录只保留仓库入口文件（README、mkdocs.yml、依赖清单等）。

## 内容导航

### 专题

- [《Agentic Engineering Patterns》中文译文专题](./docs/series/agentic-engineering-patterns/index.md) — 15 篇译文，按 6 大主题组织

### 独立文章

- [反向传播：想法、数学原理、思想史与最值得读的 5 篇文献](./docs/articles/backpropagation-ideas-math-history-5-readings.md)
- [计算图上的微积分：反向传播](./docs/articles/calculus-on-computational-graphs-backpropagation-zh.md)

### 配套资源

- [站点结构约定](./docs/resources/site-structure.md)
- [公式与图片约定](./docs/resources/math-and-images.md)
- [发布与预览说明](./docs/resources/deployment.md)
- [术语表与风格指南模板](./docs/resources/agentic_engineering_translation_glossary_style_guide_template.md)
- [双语链接映射表](./docs/resources/BILINGUAL_LINK_MAP.md)
- [研究报告](./docs/resources/research-reports/index.md) — 选型分析与决策过程记录
- [版本更新记录](./docs/resources/CHANGELOG.md)

## 使用说明

- 本文集为中文示范译文，不代表原作者官方授权中文版本
- 目录顺序按原站指南页面的章节顺序整理
- 代码、命令、URL、路径、文件名、产品名默认保留英文原文
- Prompt 默认保留英文原文，并在上下文中补充中文解释
- 站点配置见 [mkdocs.yml](./mkdocs.yml)，GitHub Pages 部署说明见 [发布与预览说明](./docs/resources/deployment.md)
