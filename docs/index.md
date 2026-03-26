# 技术专题与研究笔记

这个站点骨架的目标，不是把整个仓库永远绑死在一个专题上，而是先把当前《Agentic Engineering Patterns》中文译文收拢成一个可持续维护的专题，同时给后续不相关的新文章、资源页、图片素材和数学公式留出长期空间。

当前站点默认采用三层结构：站点首页负责总导航，`series/` 负责承载成组专题，`articles/` 负责承载与专题无强绑定的独立文章，`resources/` 负责放站点约定、术语表、映射表和其他配套资料。

## 当前内容入口

- 如果你想从当前主内容开始读，请进入 [《Agentic Engineering Patterns》专题首页](./series/agentic-engineering-patterns/index.md)。
- 如果你后续要新增与该专题无关的内容，请优先放到 [独立文章栏目](./articles/index.md)。
- 如果你要了解目录约定、图片路径、公式渲染方式，请看 [资源区](./resources/index.md)。

## 这套骨架已经预留了什么

这次骨架已经预留了四类能力：第一，专题和独立文章分层，避免未来内容互相污染；第二，`pymdownx.arithmatex` + KaTeX 的数学公式渲染链路；第三，统一的 `docs/assets/images/` 图片目录；第四，GitHub Actions 自动部署到 GitHub Pages 的工作流。

## 下一步最自然的做法

如果你准备正式上线，可以按这个顺序继续推进：先把 GitHub 仓库创建好，再在仓库的 Pages 设置里选择 `GitHub Actions` 作为发布源，然后本地执行 `pip install -r requirements-docs.txt` 和 `mkdocs serve` 预览站点，确认无误后再 push 到 `main`。
