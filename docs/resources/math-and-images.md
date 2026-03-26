# 公式与图片约定

这套骨架默认继续采用 MkDocs Material，并已经在 `mkdocs.yml` 里预留好数学公式和图片展示所需的基础配置。当前思路是：常规技术文档、专题译文、带少量公式的文章都继续走 MkDocs；只有当内容明显转向“公式密集、交叉引用、参考文献、PDF 并行输出”的研究型或书稿型写作时，再考虑切换到 Quarto。

## 数学公式

当前配置链路是 `pymdownx.arithmatex` + KaTeX。你可以直接在 Markdown 正文里写行内公式和块级公式。

行内公式写法示例：

```markdown
设复杂度为 $O(n \log n)$。
```

块级公式写法示例：

```markdown
$$
\operatorname*{argmin}_\theta \sum_{i=1}^{n} \mathcal{L}(f_\theta(x_i), y_i)
$$
```

如果后续遇到极复杂公式、编号公式、交叉引用、参考文献联动，MkDocs 仍能做一部分，但维护成本会明显上升；那时再切换 Quarto 才更值。

## 图片约定

普通配图、截图、流程图、示意图都建议统一放到 `docs/assets/images/` 下面，并继续按专题或文章 slug 分组。正文里尽量使用相对路径引用图片，这样无论仓库名、Pages 路径还是自定义域名怎么变化，都不容易出错。

示例：

```markdown
![站点目录草图](../assets/images/agentic-engineering-patterns/site-map.png)
```

如果图片和当前页面不在同一层级，请先确认相对路径是否正确；不要滥用以 `/` 开头的站点绝对路径，因为 GitHub Pages 在项目仓库模式下会多一层仓库名前缀。

## 样式层面的默认约定

这次还额外加了 `docs/assets/stylesheets/extra.css`。它主要负责两件事：让大公式在窄屏下可横向滚动，以及让正文图片默认有更稳妥的边距和圆角。后续如果要加图片宽度控制、图注、并排图片，也建议继续往这个文件里加，而不是直接在每篇正文里堆行内样式。
