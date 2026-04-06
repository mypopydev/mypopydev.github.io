# 独立文章栏目说明

`articles/` 用来放与任何现有专题都没有强绑定关系的内容，例如单篇技术随笔、工具实践、翻译方法笔记、站点维护笔记，或者未来某些只需要单独发布、暂时不值得做成专题的文章。

一个简单的判断方法是：如果某篇文章需要和前后文一起读、需要专题页承接、需要专题内上一篇/下一篇导航，那它更适合放到 `series/`；如果它本身就是独立完整的内容，那就更适合放到 `articles/`。

建议后续新增独立文章时，直接使用清晰的英文 slug 命名文件，例如 `articles/mkdocs-notes.md`、`articles/translation-workflow.md`。如果文章有专属配图，可以把图片放到 `assets/images/articles/<article-slug>/`。

## 当前已纳入的独立文章

- [反向传播：想法、数学原理、思想史与最值得读的 5 篇文献](./backpropagation-ideas-math-history-5-readings.md)

  这是一篇面向机器学习学习者与工程实践者的长文，系统梳理反向传播的核心直觉、链式法则与计算图、reverse-mode automatic differentiation、历史发展脉络，以及最值得读的 5 篇论文或文章。文中配有 7 张示意图，适合作为学习笔记、讲解材料或后续专题扩展的入口。

- [计算图上的微积分：反向传播](./calculus-on-computational-graphs-backpropagation-zh.md)

  这是一篇对 Christopher Olah 经典文章《Calculus on Computational Graphs: Backpropagation》的中文整理稿，重点从标量计算图出发解释链式法则、路径因式分解，以及为什么 reverse-mode automatic differentiation 能高效求出“一个输出对所有输入”的导数。文中配套收录了原文相关示意图，适合作为理解反向传播直觉与自动微分基础的入门材料。
