# 将当前译文仓库托管到 GitHub 并发布为静态网站的操作方案

## Executive Summary

如果你的目标只是尽快把这套内容放到 GitHub 上并能访问，最快路径是使用 GitHub Pages 的原生发布能力，补一个 `index.md` 或 `index.html` 作为首页，再在仓库设置里启用 Pages。但如果你的目标是把这 15 篇 Markdown 译文做成一个真正可长期维护的文档站，那么更合适的方案是 GitHub Pages + MkDocs Material + GitHub Actions。对当前这个项目而言，后者明显更匹配：你已经有 6 大主题分组、跨文档相对链接和连续阅读导航，MkDocs 能把这些现有资产更自然地组织成一个带导航、搜索和更稳定 URL 的静态网站。

## Background

当前仓库的内容形态已经很接近文档站原型：主体是 Markdown，首页和双语映射表已经按 6 个主题整理，15 篇译文也已经补齐“所属主题 / 上一篇 / 下一篇”导航。这意味着你现在缺的不是内容，而是“站点包装层”：首页入口、站点配置、部署流程，以及一个适合公开访问的 URL。

根据 GitHub 官方文档，GitHub Pages 在 2026 年主要有两条发布路径。第一条是“从分支发布”，适合简单静态内容或 Jekyll 站点；第二条是“用 GitHub Actions 发布”，适合需要自定义构建流程的静态站点生成器。GitHub 官方同时也说明，如果不是直接使用 Jekyll，而是使用其他静态站点生成器，那么更推荐 GitHub Actions 这条路。MkDocs 官方文档则继续保留了 `mkdocs gh-deploy` 这种快速发布方式，但对团队协作、持续更新和可重复部署来说，GitHub Actions 会更稳。

## Findings

先说结论。对你这个项目，我建议分成“两步走”。第一步是确定仓库公开发布的目录结构；第二步是选一个部署方式。目录结构上，最稳的做法不是直接把现在仓库根目录全部原样暴露出去，而是新增一个 `docs/` 目录作为站点源，把真正要公开的页面放进去。部署方式上，最小改造方案可以先用原生 Pages，长期维护方案建议直接上 MkDocs Material。

为了让差异更清楚，可以把两条主路径放在一起看：

| 方案 | 改造成本 | 适合场景 | 优点 | 局限 |
| --- | --- | --- | --- | --- |
| GitHub Pages 原生 Markdown / Jekyll | 低 | 先上线一个可访问版本 | 配置少、上手快、几乎不需要构建环境 | 导航、搜索、主题能力弱，后续演进成本高 |
| GitHub Pages + MkDocs Material + GitHub Actions | 中 | 做成正式文档站并长期维护 | 导航强、搜索内置、主题成熟、结构清晰、适合文档项目 | 需要新增配置文件和一次性整理目录 |

如果你只是想今天把网站先挂起来，最快的做法是这样的。先把仓库推到 GitHub，新建一个公开仓库。然后确保发布目录顶层有一个真正的网站入口页，最好是 `index.md`，不要只依赖 `README.md`。接着在 GitHub 仓库的 Settings → Pages 里选择发布源。如果你走最轻量路线，可以直接选 `main` 分支和 `/root` 或 `/docs` 文件夹。这样 GitHub Pages 会从你指定的位置生成站点。如果你使用的是 Jekyll 默认能力，可以再补一个 `_config.yml` 来定义站点标题、描述和主题。这样做的优点是快，但你很快就会遇到几个实际问题：一是首页、主题和导航都比较粗糙；二是全文搜索几乎没有；三是你现在已经做好的 6 大主题结构，在原生 Pages 里很难变成一个体验完整的文档站。

所以从项目适配度来看，更值得直接采用的方案是 MkDocs Material。它对 Markdown 文档仓库非常友好，而且和你现在这批文件的组织方式天然兼容。比较实用的目录方案是：保留根目录作为仓库管理层，只把公开网站内容放进 `docs/`。具体可以这样想：根目录继续保留 `README.md`、`BILINGUAL_LINK_MAP.md`、`CHANGELOG.md`、研究报告等仓库文件；`docs/` 里放网站首页 `index.md` 和 15 篇译文；仓库根目录新增 `mkdocs.yml` 和 GitHub Actions 工作流。这样做有个现实好处：你可以把站点和仓库说明分开管理，也能避免把研究性文件一股脑暴露到网站导航里。

针对当前项目，我建议最开始不要把 15 篇文章再拆进太深的子目录，而是先整体放到 `docs/` 根目录。原因很简单：你现在文章之间的链接大多是平级相对路径，比如 `./xxx.md`，如果整批一起平移到 `docs/` 根目录，这些链接基本还能继续工作，改动最小。等网站跑起来后，再决定要不要进一步按 6 大主题拆成 `principles/`、`workflow/`、`testing/` 这样的子目录。

实际操作上，推荐流程如下。第一步，在 GitHub 创建公开仓库并推送当前项目。第二步，在本地新增 `docs/index.md`，把现在 `README.md` 里更像站点首页的导语、导读和 6 大主题导航改造成网站首页内容。第三步，把 15 篇对外要展示的译文放进 `docs/`。第四步，在仓库根目录新增 `mkdocs.yml`，定义站点名称、主题、语言和 6 大主题导航。第五步，在本地安装 MkDocs 和 Material 主题，用 `mkdocs serve` 做预览，确认导航、站内链接和中文显示没问题。第六步，在 GitHub 仓库的 Pages 设置中把发布方式切换为 GitHub Actions。第七步，新增一个部署工作流，让每次推送到 `main` 后自动构建并发布。

这一套流程的关键不是“能不能发布”，而是“发布后是否好维护”。GitHub 官方文档明确区分了“从分支发布”和“用 Actions 发布”，前者适合不需要控制构建过程的简单站点，后者适合自定义构建。你的项目已经不再是简单的个人单页说明，而是一个具有结构化导航的文档集，所以用 Actions 反而更符合官方推荐思路。MkDocs 官方也提供了面向 GitHub Pages 的发布方式，说明这条组合路线本身就是成熟路径，而不是折腾。

## Recommended Path for This Project

如果只给一个推荐，我会建议你直接采用“GitHub Pages + MkDocs Material + GitHub Actions”。理由有四个。第一，你现在的内容以 Markdown 为主，这正是 MkDocs 的主战场。第二，你已经做了 6 大主题导航和文间串联，MkDocs 的 `nav` 能把这些直接变成正式站点结构。第三，Material 主题自带搜索和更完整的阅读体验，比原生 Pages 更像一个真正的专题站。第四，后续你还可能继续补术语页、专题首页、站点化目录，MkDocs 的扩展成本明显低于在原生 Pages / Jekyll 上继续缝合。

一个适合你当前项目的最小目录草案会是这样：仓库根目录包含 `README.md`、`mkdocs.yml`、`.github/workflows/deploy-pages.yml` 和其他仓库说明文件；`docs/` 目录包含 `index.md`、15 篇译文以及将来可能补充的 `glossary.md` 或 `about.md`。这样网站首页和仓库首页各司其职：GitHub 仓库页面看 `README.md`，静态网站看 `docs/index.md`。

## Common Pitfalls

这里有几个坑值得提前避开。第一，不要把“仓库 README 能显示”误当成“网站首页已准备好”。GitHub 仓库首页和 GitHub Pages 首页是两回事，网站最好明确提供 `index.md` 或 `index.html`。第二，如果仓库名不是 `<username>.github.io`，那么项目站点 URL 会带一层仓库名路径，也就是 `https://<username>.github.io/<repo>/`。这会影响那些以 `/` 开头的绝对路径，所以站内资源和页面链接最好坚持用相对路径。第三，自定义域名不要只加一个 `CNAME` 文件就完事，GitHub 官方文档明确说还要在 Pages 设置里配置域名。第四，如果后面走 GitHub Actions 路线，最好让 Pages 的部署只来自默认分支，避免其他分支误触发生产发布。

## Conclusion

如果你想把这套内容托管到 GitHub 并作为静态网站发布，技术上最简单的做法是直接启用 GitHub Pages；但如果你是想把它做成一个更像正式专题站、可以继续维护和扩展的公开网站，那么当前项目最推荐的路线是：把网站内容整理到 `docs/`，新增 `mkdocs.yml`，使用 MkDocs Material 生成站点，并通过 GitHub Actions 发布到 GitHub Pages。这样做既贴合你现在这套 Markdown 译文资产，也为后续继续补导航、搜索、专题页和术语页留出了空间。

如果下一步让我直接动手，我会按这个顺序改：先建立 `docs/` 网站源目录和 `docs/index.md` 首页，再补 `mkdocs.yml` 导航配置，然后添加 GitHub Pages 部署工作流，最后把现有 15 篇译文平移到站点目录并检查相对链接。

## References

1. [GitHub Docs - Creating a GitHub Pages site](https://docs.github.com/en/pages/getting-started-with-github-pages/creating-a-github-pages-site)
2. [GitHub Docs - Getting started with GitHub Pages](https://docs.github.com/en/pages/getting-started-with-github-pages)
3. [GitHub Docs - Configuring a publishing source for your GitHub Pages site](https://docs.github.com/en/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site)
4. [GitHub Docs - About GitHub Pages and Jekyll](https://docs.github.com/en/pages/setting-up-a-github-pages-site-with-jekyll/about-github-pages-and-jekyll)
5. [GitHub Docs - Troubleshooting 404 errors for GitHub Pages sites](https://docs.github.com/zh/pages/getting-started-with-github-pages/troubleshooting-404-errors-for-github-pages-sites)
6. [MkDocs - Deploying Your Docs](https://www.mkdocs.org/user-guide/deploying-your-docs/)
7. [Material for MkDocs - Official repository](https://github.com/squidfunk/mkdocs-material)
