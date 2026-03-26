# 《Agentic Engineering Patterns》划分为 6 个大主题的建议方案

## Executive Summary
可以，而且最稳妥的做法不是重新打散 15 篇文章再硬凑成 6 类，而是直接以 Simon Willison 原站主页已经存在的 6 个 section 为骨架，再把每个 section 改写成更适合中文目录页使用的主题名。这样既保留原作者的编排逻辑，又方便中文读者理解和后续维护双语映射。

综合原站目录、现有 15 篇示范译文标题，以及中文技术文档命名习惯后，我建议将整套内容归为“核心原则、协作工作流、测试与质量保证、代码理解、实战案例、参考资源”这 6 个大主题。这套命名比直译更顺，但仍然能一一对应回原站结构。

## Background
这套指南本身已经不是松散文章集合，而是一个经过编排的 guide。主页将内容按 section 排好顺序，形成从方法论到工程实践、从测试到理解、再到案例和附录的递进关系。对于中文发布版本，最重要的不是“重新发明分类”，而是找到一个既忠于原结构、又适合中文导航展示的 6 主题表达。

另外，补充做过一次带时间范围的微信公众号检索，检索词包括“技术文档 信息架构 命名”和“开源项目 README 目录 设计”，结果也再次印证了一个常见原则：目录命名应该短、稳、清楚，优先反映用户查找内容时的意图，而不是追求花哨表达。不过搜狗微信时间筛选存在“结果会混入旧文”的情况，所以这部分只作为中文命名习惯的辅助参考，不作为主题划分的主要依据。

## Findings
原站天然已经分成 6 个部分，分别是 Principles、Working with coding agents、Testing and QA、Understanding code、Annotated prompts 和 Appendix。若直接面向中文读者发布，我建议做成下面这套对应关系。

| 主题序号 | 推荐中文主题名 | 对应原站 section | 包含文章 |
| --- | --- | --- | --- |
| 1 | 核心原则 | Principles | 《什么是智能体工程？》《现在，写代码很便宜》《把你会做的事囤起来》《AI 应该帮助我们产出更好的代码》《反模式：有些事要避免》 |
| 2 | 协作工作流 | Working with coding agents | 《编码智能体如何工作》《如何将 Git 用于编码智能体工作流》《子智能体》 |
| 3 | 测试与质量保证 | Testing and QA | 《红/绿 TDD》《先跑测试》《让智能体做手动测试》 |
| 4 | 代码理解 | Understanding code | 《线性讲解》《交互式解释》 |
| 5 | 实战案例 | Annotated prompts | 《用 WebAssembly 和 Gifsicle 构建 GIF 优化工具》 |
| 6 | 参考资源 | Appendix | 《我常用的 Prompt》 |

这样划分的好处是很明确的。第一，它完全顺着原站的认知路径走：先讲理念，再讲如何协作，再讲怎么保证质量，然后讲如何理解现有代码，最后给出案例和可复用资源。第二，它和你当前已经做好的双语映射、原站顺序、译文标题都天然兼容，不需要重写文件命名，也不需要重新定义“第几篇”。第三，这套命名很适合放在 README、导航页或后续静态站点首页，因为读者一眼就能知道每组内容解决什么问题。

如果你希望更贴近原文 section 名，也可以使用一套更“直译型”的命名，即“原则”“与编码智能体协作”“测试与质量保证”“理解代码”“带注释的 Prompt”“附录”。但我不太推荐直接把 Annotated prompts 译成“带注释的 Prompt”作为一级主题名，因为中文读者第一次看到时未必立刻知道它其实是“案例讲解”。把它处理成“实战案例”更利于导航；在组内简介里再说明它对应原站的 Annotated prompts，就兼顾了可读性和可追溯性。

## Analysis
从内容结构上看，这 6 个主题并不是平均分配文章数量，而是承担不同角色。第一组“核心原则”是整套指南的价值观和方法论基座，文章最多，决定了全书语气。第二组“协作工作流”讲的是人与编码智能体怎么高效配合，属于工程执行层。第三组“测试与质量保证”是把智能体纳入既有软件质量体系。第四组“代码理解”解决的是另一个高频场景：不是让智能体写，而是让智能体讲清楚。第五组“实战案例”用一个完整示范把前面的方法串起来。第六组“参考资源”则提供可以反复调用的 Prompt 资产。

也就是说，这不是普通的六个平行栏目，而是一条很完整的学习与实践路径。中文目录最好保留这种递进感，所以主题名应该偏“问题域”而不是偏“修辞感”。“核心原则、协作工作流、测试与质量保证、代码理解、实战案例、参考资源”正好对应读者最常见的六类问题：这是什么、怎么配合、怎么保质量、怎么看懂、怎么落地、哪里有可复用素材。

## Conclusion
结论很简单：可以，而且最推荐的 6 个大主题其实就是沿用原站现成的 6 个 section，只在中文命名上做适度策展。若你要一个可以直接放进当前项目 README 或目录页的版本，我建议最终采用“核心原则、协作工作流、测试与质量保证、代码理解、实战案例、参考资源”。

如果后续你要继续往前走，这套 6 主题可以直接用于三种场景：一是重写 `README.md` 的目录导航；二是给 15 篇文章加分组标题；三是后面生成静态首页或专题页时，直接做成 6 个入口卡片。

## Limitations
本次结论的主体依据是原站主页结构与现有中文译文，不是对每篇正文重新做主题建模；不过由于用户目标本来就是“参考原站来划分”，所以这种方法反而是最合适的。微信公众号检索已按要求加入时间范围，但搜狗结果会混入旧文章，因此只将其作为中文命名习惯的弱参考。

## References
1. [Agentic Engineering Patterns](https://simonwillison.net/guides/agentic-engineering-patterns/)
2. [What is agentic engineering?](https://simonwillison.net/guides/agentic-engineering-patterns/what-is-agentic-engineering/)
3. [Red/green TDD](https://simonwillison.net/guides/agentic-engineering-patterns/red-green-tdd/)
4. [Linear walkthroughs](https://simonwillison.net/guides/agentic-engineering-patterns/linear-walkthroughs/)
5. [GIF optimization tool using WebAssembly and Gifsicle](https://simonwillison.net/guides/agentic-engineering-patterns/gif-optimization/)
6. [如何写开源项目的readme文档 | PingCode智库](https://docs.pingcode.com/baike/578259)
7. [你真的会写README吗？剖析顶级开源项目的文档结构设计](https://blog.csdn.net/VarIsle/article/details/152457135)
