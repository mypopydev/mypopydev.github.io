# 站点结构约定

这套目录是按“站点首页 + 专题 + 独立文章 + 资源 + 共享素材”来设计的，目的不是追求一开始就很复杂，而是保证当前专题能上线，同时未来增加不相关内容时不用重构整站。

## 当前目录骨架

```text
docs/
  index.md
  series/
    index.md
    agentic-engineering-patterns/
      index.md
      *.md
  articles/
    index.md
  resources/
    index.md
    site-structure.md
    math-and-images.md
    ...
  assets/
    images/
    stylesheets/
    javascripts/
```

## 目录分工

`docs/index.md` 是站点首页，只做总导航，不承担某一个专题的全部正文内容。`docs/series/` 用来放需要按组阅读的专题，每个专题单独拥有自己的目录和专题首页。`docs/articles/` 用来放无强依赖关系的单篇内容。`docs/resources/` 用来放配套说明、映射、约定和其他辅助材料。`docs/assets/` 用来放共享静态资源，例如图片、样式和脚本。

## 新增内容时的放置规则

如果新增内容仍然属于《Agentic Engineering Patterns》专题的补充说明、勘误、衍生页，可以继续放在 `docs/series/agentic-engineering-patterns/`。如果新增内容已经和这个专题无关，例如新的 AI 工程文章、翻译方法文章或工具实践记录，优先放到 `docs/articles/`；当某一类独立文章逐渐形成一组时，再把它升级为新的 `series/<series-slug>/`。

## 导航规则

站点级导航负责把人带到“专题”或“栏目”，而不是直接承担跨专题的上一篇/下一篇逻辑。上一篇/下一篇只建议在同一专题内部维护，不要跨专题串联。这样以后无论站点加多少内容，信息架构都会稳定。

## 图片目录建议

共享图片放在 `docs/assets/images/`。如果图片只服务于某个专题，建议再按专题或文章 slug 细分子目录，例如 `docs/assets/images/agentic-engineering-patterns/` 或 `docs/assets/images/articles/mkdocs-notes/`。这样一眼就能看出图片归属，也更方便后续迁移专题。
