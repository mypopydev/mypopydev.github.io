# 翻译 Simon Willison《Agentic Engineering Patterns》的可执行方案

## Executive Summary
如果要翻译 https://simonwillison.net/guides/agentic-engineering-patterns/ 这一组内容，最合适的做法不是直接整站机翻，而是采用“按章节拆分、AI 初译、人工精修、术语先行、代码与提示词谨慎处理、分平台发布”的方案。基于对原站结构、技术长文翻译流程和中文技术社区术语习惯的综合研究，我更推荐把它当作一个“小型技术翻译项目”来做，而不是一次性翻译任务。

这组内容本质上是一份持续更新的指南，包含多个子页面、术语密集段落、代码块、提示词、Git 命令、方法论表述和大量内部链接。因此，最佳方案是先建立术语表和风格规范，再用“AI 初译 + 人工精修 + 技术校对 + 发布同步”的流程推进。若由单人执行，建议分 3 个批次完成；若由小团队执行，建议采用“主译 + 审校 + 技术复核”的协作模式。

## Background / Context
这份指南不是一篇普通博客，而是一组围绕 agentic engineering 的系列页面。研究中获取到的信息显示，它至少包含 6 个大部分、15 个子页面，覆盖原则、与 coding agents 协作、测试与 QA、理解代码、带注释的提示词案例和附录等内容。其内容特点决定了翻译难度不主要来自英文句子本身，而来自以下几个方面：第一，术语仍在快速演化，中文尚未完全定型；第二，页面之间有章节层级和交叉链接；第三，部分内容包含代码、命令、提示词和工程方法论，不能按普通文章的方式处理；第四，这个系列仍可能继续更新，译文需要考虑后续同步维护。

## Research Findings

## 原文结构与翻译对象拆解
这组内容可以拆成三类。第一类是概念与原则类页面，例如“什么是 agentic engineering”“代码现在很便宜”“反模式”等，这部分决定整套译文的术语和论述基调。第二类是操作与工程实践类页面，例如 how coding agents work、using Git with coding agents、subagents、red/green TDD，这部分对术语一致性和技术准确性要求最高。第三类是案例与附录类页面，例如 GIF optimization tool 和 prompts，这部分最容易因为提示词、代码块、外链和工具名处理不当而让译文变形。

因此，不建议按“整站一次性翻译”推进，更合理的方式是按三批翻译。第一批先翻原则和定义页，用来锁定术语；第二批翻工作流、Git、subagents、TDD 等高价值章节；第三批再翻案例和附录，因为这部分对整体理解要求更高，且最适合在术语稳定后处理。

## 推荐术语策略
综合中文技术社区现状和现有中文翻译实践，我建议把 Agentic Engineering 主译为“智能体工程”，首次出现写作“智能体工程（Agentic Engineering）”。“智能体化工程”也有人使用，但略长，且在标题、目录、链接锚文本中不如“智能体工程”干净。Agent 建议译为“智能体”，Coding Agent 建议译为“编码智能体”或“编程智能体”，其中如果希望更贴近 Simon Willison 原文，可优先用“编码智能体”；如果目标读者更偏中文技术社区常用法，则“编程智能体”也成立，但全文只能二选一。

Planning、Memory、Workflow、Reasoning、Reflection、Tool Use、Delegation 这类术语，建议以中文为主，必要时首次括注英文。也就是说，可以写作“规划（planning）”“记忆（memory）”“工具使用（tool use）”。但像 LLM、RAG、MCP、Token、Prompt 这类已经高度行业化、且英文检索价值更高的术语，建议保留英文缩写或英文原词，并在首次出现时给出中文释义，例如“Token（词元）”“Prompt（提示词）”。

对 Vibe Coding 这类带有作者语境和社区语感的词，不建议彻底意译。可以采用“氛围编程（Vibe Coding）”这种处理：既保留原词，又给中文读者一个可理解的入口。

## 最推荐的翻译流程
对这组内容，最优流程不是纯人工，也不是纯机器，而是“AI 初译 + 人工精修 + 术语审校 + 技术复核”的混合流程。原因很简单：文章整体结构规整，适合 AI 提前完成段落级初译；但概念定义、长句论证、术语细微差别、提示词原貌、代码相关语义，必须靠人工修正。

具体执行时，建议分成七步。第一步，抓取并整理目录，把 15 个子页面保存成结构化文本，保留标题层级和原始链接。第二步，先建立一版术语表，至少覆盖 Agentic Engineering、Agent、Coding Agent、Prompt、Token、Context Window、Reasoning、Subagent、Red/green TDD、Reflog、Cherry-pick 等核心术语。第三步，按章节进行 AI 初译，但必须设置约束：代码块、命令行、URL、引用格式、文件名、工具名默认不翻。第四步，人工精修句子，让中文读起来自然，不要保留英文长句结构。第五步，做技术复核，重点核对 Git 操作名词、LLM 机制描述、工具调用流程、提示词内容。第六步，做一致性和格式检查，尤其检查章节名、术语、内链、代码块和表格。第七步，再决定发布形态，是纯中文版本、双语对照版本，还是“中文精译 + 原文链接”的轻量版本。

## 代码、提示词、链接和引用应该怎么处理
代码块、shell 命令、函数名、配置名、标签名和路径，原则上都不翻。只翻代码注释和代码块外的说明文字。Git 命令如 git init、git log、git bisect、git stash、git reset --soft HEAD~1 必须保持原样，否则读者无法复现。

提示词是这套内容里最需要克制处理的部分。尤其 GIF optimization tool 这种案例里，提示词本身既是“被讲解对象”，也是“工程输入”。这类内容不适合完全翻成中文后替代原文，更稳妥的做法是保留英文提示词原文，并在其下给出逐段中文解释。这样既不破坏可执行性，也不损失教学价值。

链接层面，建议全部保留原始 URL。若将来制作中文版专题页，可以把目录里的内部链接映射到中文页面；但在第一版翻译中，即使正文中文化，也最好先保留指向原文的链接，避免因为章节还未全部完成而出现断链。引用来源同理，采用“中文说明 + 原文链接”的方式最稳。

## 单人执行方案
如果由一个人来做，这个项目是能落地的，但前提是不要试图一口气完成。比较合理的节奏是三批推进。第一批先做 3 到 5 篇概念和原则页，用两到三天锁定术语。第二批做核心工程页，用三到五天完成。第三批做案例和附录，再用两到三天。随后留出一到两天做总审校。

单人模式下，建议每篇文章都走一个固定模板：先抽取正文，再生成 AI 初稿，再人工修句，再检查术语，再核对格式与链接，最后补充译者说明。这样做的好处是流程稳定，不容易把质量波动带进后续页面。

## 小团队执行方案
如果有两到三个人，小团队模式会明显更稳。最佳分工是：一个人负责主译和术语落地，一个人负责中文审校和文风统一，必要时再由一个有工程背景的人负责技术复核。这里的关键不是加人，而是避免多译者各自发挥。只要多人参与，就必须先有术语表和风格指南，否则“智能体工程/智能体化工程/代理工程”这类用词会很快失控。

团队模式下，更适合做双语对照版本和专题化发布，因为有人可以专门维护目录、内链、更新日志和版本记录。

## 推荐交付物
如果目标是“翻译出来能长期使用”，我建议至少准备四样交付物。第一是中文版 Markdown 正文，作为主文本；第二是术语表，单独成页；第三是翻译说明，写清楚哪些内容保留原文、哪些采用首次释义；第四是更新日志，记录原文对应版本、翻译日期和修订内容。若条件允许，再做一个双语对照版本，尤其适合概念密集章节。

发布载体方面，GitHub 或知识库是最适合做“源版本管理”的地方；个人博客适合做完整正文和 SEO；公众号更适合发布精华节选、章节导读或系列连载，而不是直接承载所有长代码块和复杂格式。

## Recommended Execution Plan
如果你现在就要启动，我建议按下面这个顺序推进。先不翻全站，只翻“什么是 Agentic Engineering”“How coding agents work”“Using Git with coding agents”这三篇，拿它们做试翻样本。原因是这三篇足以覆盖定义、机制、工程实践三种最关键的翻译场景。做完这三篇后，再反过来修术语表和风格规范。只有这一步跑顺了，再批量推进剩余章节，效率和稳定性才会明显提升。

在质量标准上，第一版译文的目标不该是“文学性很强”，而应是“技术准确、术语稳定、读起来像成熟中文技术文章、并且能继续迭代”。对这类内容来说，可维护性比一版到位更重要。

## Conclusion
总结下来，翻译这组内容的最佳方案是：先把它当成一个结构化技术翻译项目，再用“术语先行、分批推进、AI 初译、人工精修、技术复核、逐步发布”的方式落地。核心推荐有三点。第一，主译名建议采用“智能体工程（Agentic Engineering）”，并建立统一术语表。第二，流程上采用混合翻译而不是纯机翻或纯人工。第三，发布上优先做 Markdown 源版本和分章节交付，而不是一次性成稿。

如果你愿意，我下一步可以直接继续两种方向：一种是我帮你先做这套内容的“术语表 + 风格指南模板”；另一种是我直接拿第一篇“什么是 Agentic Engineering”做一个示范性中译版本。

## Limitations
本方案基于公开网页结构、相关中文翻译实践、中文技术社区术语习惯和技术文档翻译流程研究形成。由于原站内容仍可能持续更新，后续正式翻译时仍需要以页面最新版本为准，并在发布时记录版本日期。

## References
1. [Agentic Engineering Patterns](https://simonwillison.net/guides/agentic-engineering-patterns/)
2. [What is agentic engineering?](https://simonwillison.net/guides/agentic-engineering-patterns/what-is-agentic-engineering/)
3. [How coding agents work](https://simonwillison.net/guides/agentic-engineering-patterns/how-coding-agents-work/)
4. [Using Git with coding agents](https://simonwillison.net/guides/agentic-engineering-patterns/using-git-with-coding-agents/)
5. [Subagents](https://simonwillison.net/guides/agentic-engineering-patterns/subagents/)
6. [Red/green TDD](https://simonwillison.net/guides/agentic-engineering-patterns/red-green-tdd/)
7. [GIF optimization tool using WebAssembly and Gifsicle](https://simonwillison.net/guides/agentic-engineering-patterns/gif-optimization/)
8. [机器翻译后编辑的最佳实践](https://www.linguise.com/zh-cn/%E5%8D%9A%E5%AE%A2/%E6%8C%87%E5%AF%BC/%E6%9C%BA%E5%99%A8%E7%BF%BB%E8%AF%91%E5%90%8E%E6%9C%9F%E7%BC%96%E8%BE%91/)
9. [技术科普 | 常见翻译质量保证工具一览](https://www.sohu.com/a/591912088_121292768)
10. [从新手到大师：翻译项目的全流程管理](https://developer.baidu.com/article/detail.html?id=2848323)
11. [01-什么是智能体工程？](https://foofish.net/what-is-agentic-engineering.html)
12. [什么是 Agentic Engineering？Simon Willison 给出最新定义](https://elasticsearch.cn/article/15728)
13. [Agentic Design Patterns 中文翻译项目在线版](https://adp.xindoo.xyz/)
14. [GitHub - xindoo/agentic-design-patterns](https://github.com/xindoo/agentic-design-patterns)
15. [程序员技术博客多平台发布攻略：写一次，发遍全网](https://www.wechatsync.com/blog/tech-blog-multi-platform-guide/)
16. [LLM领域的术语及其中文翻译](https://blog.yellster.top/p/llm-terminology-chinese-translations/)
17. [token为什么今天才叫词元？](https://sspai.com/post/107420)
18. [Context Engineering 中文翻译指南](https://xjthy001.github.io/Context-Engineering-CN/TRANSLATION_GUIDE.html)
