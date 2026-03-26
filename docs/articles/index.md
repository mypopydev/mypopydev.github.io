# 独立文章栏目说明

`articles/` 用来放与任何现有专题都没有强绑定关系的内容，例如单篇技术随笔、工具实践、翻译方法笔记、站点维护笔记，或者未来某些只需要单独发布、暂时不值得做成专题的文章。

一个简单的判断方法是：如果某篇文章需要和前后文一起读、需要专题页承接、需要专题内上一篇/下一篇导航，那它更适合放到 `series/`；如果它本身就是独立完整的内容，那就更适合放到 `articles/`。

建议后续新增独立文章时，直接使用清晰的英文 slug 命名文件，例如 `articles/mkdocs-notes.md`、`articles/translation-workflow.md`。如果文章有专属配图，可以把图片放到 `assets/images/articles/<article-slug>/`。
