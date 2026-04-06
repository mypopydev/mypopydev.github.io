# 含 LaTeX 与图片需求时的静态站方案选型建议

## Executive Summary

如果你后续只是“需要在文档里插入一些 LaTeX 公式和图片”，那并不足以推翻当前的推荐方案。对这个项目来说，默认仍然最适合选择 `GitHub Pages + MkDocs Material + GitHub Actions`：它对数学公式和图片都支持得足够完整，配置成本低，而且最贴合当前以 Markdown 为核心的专题文档形态。只有当站点未来明显转向“重学术写作、强交叉引用、大量公式、可能还要同时导出 PDF/Word”时，Quarto 才会开始变成更强的候选；如果未来更强调 React 组件、文档版本化、多语言和高度交互式页面，Docusaurus 才更值得考虑。

## Background

这个问题不是抽象地问“哪个静态站工具最强”，而是在当前项目语境下做选型。你现在手里是一套以 Markdown 为主的中文译文专题站：已经有 15 篇正文、6 大主题导航、双语映射表，以及文章间的顺序导航。也就是说，当前项目的本质仍然是“文档型站点”，不是博客平台，不是交互式前端应用，也不是科研论文出版系统。

因此，新增加的两个约束——LaTeX 渲染和图片插入——真正需要回答的是：这些需求会不会把当前项目从“文档站”推向“学术出版工具”或“前端应用框架”？如果不会，那么最佳方案不该因为少量公式和图片就被轻易推翻。

## Findings

先说最关键的一点。Material for MkDocs 官方文档已经明确支持数学公式渲染，而且支持两条成熟路径：MathJax 和 KaTeX。官方给出的方式是通过 `pymdownx.arithmatex` 扩展配合前端渲染库来实现，既支持行内公式，也支持块级公式。KaTeX 的优势是更快，适合公式较多但语法相对常规的场景；MathJax 的优势是兼容性更广、支持更丰富的 LaTeX 能力，也对辅助功能更友好。对当前这类技术文章译文站来说，偶尔插入公式时用 KaTeX 就已经很够了；如果以后公式越来越复杂，再切到 MathJax 也不难。

图片这块，Material for MkDocs 也不是“只能勉强显示 Markdown 图片”。它官方就提供了图片展示增强能力，包括图片标题、对齐、懒加载、浅色/深色模式分别使用不同图片，以及通过插件实现灯箱放大。也就是说，如果你说的“添加图片”是普通技术文档常见的几类图片，例如截图、流程图、公式图、示意图、配图、图表，那么 MkDocs Material 已经足够胜任，而且体验不差。

为了把结论说清楚，最有价值的是看它与几个常见备选方案的边界差异。

| 方案 | LaTeX/数学公式 | 图片支持 | GitHub Pages 兼容性 | 对当前项目的适配度 |
| --- | --- | --- | --- | --- |
| MkDocs Material | 强，需少量配置，支持 KaTeX/MathJax | 强，支持标题、对齐、懒加载、灯箱扩展 | 强，适合配合 Actions 发布 | 最高 |
| Jekyll on GitHub Pages | 可做，但通常要手动接入 MathJax，受 GitHub Pages 安全模式和插件限制影响 | 基础支持没问题，但增强能力一般 | 原生支持最强 | 中等偏低 |
| Docusaurus | 强，通过 `remark-math` + `rehype-katex` 配置 | 强，静态资源与 Markdown 图片处理成熟 | 适合配合 Actions | 中等 |
| Quarto | 很强，对技术写作、公式、交叉引用、LaTeX 原生支持最好 | 很强，适合图表、学术图文、可引用图片 | 可发布到 GitHub Pages | 中等偏高，但更偏学术出版 |

Jekyll 的问题不是它不能做，而是它在 GitHub Pages 语境下不够舒服。GitHub 官方文档已经说明，GitHub Pages 上的 Jekyll 运行在受限制模式下，一些配置和插件是被锁死的。对于纯简单博客这问题不大，但对一个后续可能要继续扩展的技术专题站来说，这意味着数学公式、图片增强、后续扩展能力都更依赖手工拼装。它的最大优势是“原生、最省心地被 GitHub Pages 接住”，但这只在你追求极简上线时有意义，不是长期最优。

Docusaurus 的情况正相反。它在功能上当然强，尤其是当你需要文档版本化、国际化、博客、React 组件嵌入和更重的交互体验时，Docusaurus 会很有吸引力。官方文档也清楚说明了数学公式通过 `remark-math` 和 `rehype-katex` 即可启用，图片和静态资源也有一套完整的处理方式，甚至会自动考虑 `baseUrl` 问题。问题在于，你当前项目并不需要 React 带来的那层复杂度。它更像是在为未来可能出现的“重前端需求”提前付学费。如果你只是想放 LaTeX 和图片，Docusaurus 太重了。

Quarto 是这次比较里最值得认真看的备选。因为一旦提到 LaTeX，很多项目其实不是“需要显示几条公式”，而是“未来可能越来越像研究报告、课程讲义、技术书、带引用和交叉引用的长文系统”。而这正是 Quarto 的强项。Quarto 官方文档明确强调 technical writing 场景，支持公式、原生 LaTeX、图片、交叉引用、引用管理等能力；其发布到 GitHub Pages 也有成熟路径，可以输出到 `docs/`，也能通过 GitHub Actions 自动化部署。它真正强的地方在于：如果你的内容未来大量使用公式编号、图编号、表编号、交叉引用、甚至还想一份源同时产出 HTML 和 PDF，那么它会比 MkDocs 更像一把正合手的工具。

但问题也在这里。当前项目还是译文专题站，不是科研写作工作流。你现在更需要的是：简单、稳定、好看、导航强、对 Markdown 友好、部署顺。Quarto 虽然强，但它的强项有一部分是你当前根本还没用上。如果为了“以后可能会有更多公式”就提前换到 Quarto，反而容易过度设计。

## Analysis

所以真正该问的不是“哪个工具功能更多”，而是“新增 LaTeX 和图片之后，当前项目的主导需求有没有变化”。我的判断是：没有。

因为“文档站 + 少量到中量公式 + 图片”本身就是 MkDocs Material 的舒适区。你只需要在 `mkdocs.yml` 里增加一小段数学扩展配置，再准备一个本地图片目录，就能满足大部分技术专题站的需要。它不会逼你换内容格式，不会逼你转向 React，也不会逼你把整个项目改造成学术出版流水线。

但这里确实有一个重要分界线。如果未来内容开始明显出现下面这些特征，那么就应该重新评估，甚至优先考虑 Quarto。比如：公式非常多而且复杂；公式、图片、表格都需要编号和交叉引用；文章经常需要插图说明并在文中引用“见图 3”“见式 2”；你希望同一份内容同时导出网页版和 PDF；或者文章开始带有参考文献、脚注和更标准的技术写作结构。这类需求不是“加几条公式”那么简单，而是已经接近技术书或研究报告系统了。到了那个阶段，Quarto 会比 MkDocs 更自然。

Docusaurus 的切换阈值又是另一种。如果未来这个站不再是“读文档”，而是“需要很多交互式界面、内嵌 React 组件、版本化文档、多语言切换、博客系统”，那才是 Docusaurus 的舞台。换句话说，Quarto 是在“更偏学术/出版”时胜出，Docusaurus 是在“更偏前端交互/产品文档平台”时胜出。

## Recommendation for This Project

针对你当前这个项目，如果只是计划“后续可能会插入 LaTeX 公式和图片”，我的推荐不变，仍然是 `MkDocs Material`。

更具体一点说，我会这样定规则。第一，默认继续走 `GitHub Pages + MkDocs Material + GitHub Actions`。第二，数学公式默认优先用 KaTeX，因为更轻更快；如果后面确实遇到兼容性更强的公式需求，再切换到 MathJax。第三，图片资源统一收纳到专题目录下的 `images/` 或 `assets/images/`，尽量保持相对路径，不要乱用绝对路径。第四，如果未来出现大量公式编号、交叉引用、参考文献和 PDF 并行输出需求，再单独评估是否把整个站迁移到 Quarto，而不是现在就提前换栈。

所以最直接的一句话结论是：仅仅因为需要 LaTeX 和图片，不需要换掉 MkDocs；但如果未来内容逐渐变成“研究型、书稿型、公式密集型”的技术出版站，再优先考虑 Quarto。

## Conclusion

对当前项目来说，新增 LaTeX 和图片需求后，最合适的方案仍然是 MkDocs Material，而不是 Jekyll、Docusaurus 或 Quarto。它已经具备成熟的数学公式支持和足够强的图片展示能力，且与当前 Markdown 文档结构、GitHub 托管方式和后续专题扩展路径都最吻合。只有在需求从“文档站增强”升级为“学术技术出版”或“高交互前端文档平台”时，才值得分别转向 Quarto 或 Docusaurus。

如果下一步让我直接动手，我会继续沿着 MkDocs 路线做，并顺手把数学公式和图片支持预留进去，例如在 `mkdocs.yml` 中补好公式扩展位、规划图片资源目录，并把未来可能需要的专题结构一并设计好。

## References

1. [Material for MkDocs - Math](https://squidfunk.github.io/mkdocs-material/reference/math/)
2. [Material for MkDocs - Images](https://squidfunk.github.io/mkdocs-material/reference/images/)
3. [GitHub Docs - About GitHub Pages and Jekyll](https://docs.github.com/en/pages/setting-up-a-github-pages-site-with-jekyll/about-github-pages-and-jekyll)
4. [Docusaurus - Math Equations](https://docusaurus.io/docs/markdown-features/math-equations)
5. [Docusaurus - Static Assets](https://docusaurus.io/docs/static-assets)
6. [Quarto - Technical Writing](https://quarto.org/docs/visual-editor/technical.html)
7. [Quarto - Publishing to GitHub Pages](https://quarto.org/docs/publishing/github-pages.html)
