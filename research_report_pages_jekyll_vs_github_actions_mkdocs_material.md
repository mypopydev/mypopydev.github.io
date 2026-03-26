# GitHub Pages 仍走 Jekyll 而不是 GitHub Actions + MkDocs Material：排查报告

## Executive Summary
这次排查后，我对根因的判断已经比上一轮更具体了：当前线上站点极大概率仍然使用的是 GitHub Pages 的“从分支发布”模式，而且发布源不是 Actions 产物，而是 `main` 分支下的 `docs/` 目录，因此 GitHub 才会把 `docs/index.md` 等 Markdown 直接按 Jekyll 风格渲染成页面。仓库中的 MkDocs Material 配置和 Actions 工作流本身没有明显问题，公开可见的 `deploy-pages` 工作流甚至已经成功执行过一次，但它现在没有成为用户实际访问站点的有效发布来源。

## Background
这类问题最容易让人误判的地方在于：仓库里可以同时存在三套东西，分别是 `docs/` 里的 Markdown 源文件、`site/` 里的 MkDocs 构建产物，以及 GitHub Pages 的在线发布设置。只看仓库文件时，会以为“已经配好了 MkDocs Material”；只看线上页面内容时，又会误以为“内容已经上线，所以部署没问题”。真正决定用户看到什么的，是 GitHub Pages 当前到底在发布哪一份内容。

## Findings
先看线上证据。`https://mypopydev.github.io/` 和 `https://mypopydev.github.io/series/agentic-engineering-patterns/` 都能正常访问，但返回的真实 HTML 头部明确包含 `meta name="generator" content="Jekyll v3.10.0"`，并加载 `/assets/css/style.css?v=0ebe4ac2c6e7f3c295c1d4397910580f95f004e8`。页面主体容器是 `<div class="container-lg px-3 my-5 markdown-body">` 这一类 GitHub Pages 默认 Jekyll 风格结构，而不是 Material 主题常见的 `mkdocs-material` 页面框架、抽屉导航、搜索组件和 `assets/stylesheets/main.*.css` 等资源。

再看本地构建结果。当前工作区里的 `site/index.html` 明确是标准的 MkDocs Material 成品，头部写着 `meta name="generator" content="mkdocs-1.6.1, mkdocs-material-9.7.6"`，并引用 `assets/stylesheets/main.484c7ddc.min.css`、`assets/stylesheets/extra.css` 与 KaTeX 资源。也就是说，本地 `mkdocs build --strict` 产物是正确的，而且和线上看到的 HTML 明显不是同一套页面框架。

接着看仓库配置。`mkdocs.yml` 设置了 `docs_dir: docs`、`site_dir: site`，主题是 `material`，导航和扩展配置也完整；`.github/workflows/deploy-pages.yml` 的写法同样没有明显问题，它会在 `main` 分支 push 时安装 `requirements-docs.txt`、运行 `mkdocs build --strict`、上传 `site` 目录，并调用 `actions/deploy-pages@v4` 部署。这条链路本身是成立的。

更关键的一条证据是：公开 GitHub API 能查到这条 `deploy-pages` 工作流确实已经成功运行过一次。那次运行的 `build` 和 `deploy` 两个 job 都是 `completed` 且 `conclusion` 为 `success`，对应 commit 是 `0ebe4ac2c6e7f3c295c1d4397910580f95f004e8`。但线上页面同时又展示了典型 Jekyll 输出，而且它引用的 `style.css?v=0ebe4ac...` 恰好带着同一个 commit SHA。这说明两件事同时为真：第一，Actions 工作流跑成功了；第二，用户当前访问到的站点仍然是由 GitHub Pages 用 Jekyll 从源码分支渲染出来的页面，而不是 MkDocs 构建产物。

最后一条几乎可以定性的证据是首页内容来源。线上首页正文和仓库里的 `docs/index.md` 是逐段对应的，而不是根目录 `README.md`。与此同时，`.gitignore` 明确忽略了 `site/`，并且 `git ls-files` 也表明 `site/index.html` 没有被跟踪提交。这意味着线上首页不可能来自已提交的 `site/` 目录，只可能来自 GitHub Pages 对 `docs/` 目录下 Markdown 的直接分支发布渲染。换句话说，当前线上站点极大概率仍然配置成了“从 `main` 分支的 `/docs` 目录发布”。

## Analysis
把这些证据连起来，根因就比较清楚了。当前不是“MkDocs 工作流写错了”，也不是“Material 配置无效”，而是“GitHub Pages 当前仍在按分支源直接发布 `docs/`，所以线上站点走的是 Jekyll 渲染链路”。这也解释了为什么会出现一个看似矛盾的状态：Actions 成功了，但线上仍是 Jekyll。因为对 GitHub Pages 来说，是否真的把 Actions 产物作为公开站点提供，取决于仓库 Settings 里的 Pages 发布源设置，而不是仓库里有没有 workflow 文件。

我对最可能根因的排序是这样的。第一位，也是高概率根因，是 Pages 设置里 `Build and deployment` 的 `Source` 仍然是 “Deploy from a branch”，而且分支/目录大概率还是 `main` + `/docs`。这是因为线上首页内容和 `docs/index.md` 一致，且线上风格是 Jekyll。第二位是一个稍弱但相关的可能性：Pages 曾经切到过 GitHub Actions，但后来又被保留在分支发布，或 Actions 部署没有成为当前公开站点来源。第三位才是低概率原因，例如 Actions 虽然显示成功，但部署到的是另一个无效通道；不过从目前公开证据看，没有必要先怀疑这一层。

## Conclusion
结论可以说得更直接一点：当前 `mypopydev.github.io` 之所以还在走 Jekyll，而不是 GitHub Actions + MkDocs Material，不是因为你的 MkDocs 配置错了，也不是因为 workflow 没跑，而是因为 GitHub Pages 现在实际上仍在发布 `docs/` 目录的 Markdown 源文件。也就是说，线上网站的有效发布源还停留在分支发布模式，而没有真正切到 Actions 产出的 `site/` 静态文件。

## Recommended Next Step
你接下来最该检查的不是代码，而是 GitHub 仓库后台的 Pages 设置。进入 `Settings → Pages`，在 `Build and deployment` 里确认 `Source` 是否还是 `Deploy from a branch`。如果是，就把它改成 `GitHub Actions`。改完之后，最稳的做法是手动重新运行一次 `deploy-pages` 工作流，或者重新 push 一个空提交触发它。等它再成功后，刷新线上页面；如果切换生效，首页 HTML 头部就不该再出现 `Jekyll v3.10.0`，而应该更接近本地 `site/index.html` 的 MkDocs Material 输出。

修复完成后，最简单的验收方式只有两条。第一，看页面外观：应该出现 Material 的顶部导航、侧边栏、搜索等结构。第二，看源码：`meta generator` 应从 `Jekyll v3.10.0` 变成 `mkdocs-1.6.1, mkdocs-material-9.7.6` 一类标识。

## Limitations
这次排查已经拿到了比较强的公开证据，但我没有直接登录 GitHub 仓库后台读取 Pages 设置页面，因此“当前就是 `main` + `/docs`”这一点仍然属于高置信度推断，而不是后台截图级别的绝对确认。不过从线上首页内容、Jekyll HTML 结构、`docs/index.md` 一致性、`site/` 被忽略且未跟踪提交、以及 Actions 已成功运行这几条证据叠加来看，这个判断已经足够接近事实。

## References
1. [线上首页](https://mypopydev.github.io/)
2. [线上专题页](https://mypopydev.github.io/series/agentic-engineering-patterns/)
3. [仓库中的 MkDocs 配置](https://raw.githubusercontent.com/mypopydev/mypopydev.github.io/main/mkdocs.yml)
4. [仓库中的 Pages 工作流](https://raw.githubusercontent.com/mypopydev/mypopydev.github.io/main/.github/workflows/deploy-pages.yml)
5. [仓库中的 docs/index.md](https://raw.githubusercontent.com/mypopydev/mypopydev.github.io/main/docs/index.md)
6. [GitHub Pages 文档](https://docs.github.com/en/pages)
7. [Using custom workflows with GitHub Pages](https://docs.github.com/en/pages/getting-started-with-github-pages/using-custom-workflows-with-github-pages)
