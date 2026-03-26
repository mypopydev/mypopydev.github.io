# 先跑测试

原文标题：First run the tests
原文链接：https://simonwillison.net/guides/agentic-engineering-patterns/first-run-the-tests/
原文作者：Simon Willison
访问日期：2026-03-25
原文发布日期：2026-02-24
原文最后修改：2026-02-28
译文版本：v0.1

## 译文说明

本文为 Simon Willison《Agentic Engineering Patterns》系列中《First run the tests》的示范中文版。本文沿用本项目既定术语约定，将 Coding Agent 统一译为“编码智能体”，并继续保留 Prompt、`pyproject.toml`、`uv run pytest` 等高检索价值英文术语、配置名与命令原文。标题采用“先跑测试”，对应原文并不是一句泛泛的建议，而是一条短 Prompt，也是一种把“先建立测试基线、再开始改代码”压缩进四个词里的工程模式。

## 正文

> 所属主题：测试与质量保证
> 上一篇：[红/绿 TDD](./red_green_tdd_demo_zh.md)
> 下一篇：[让智能体做手动测试](./agentic_manual_testing_demo_zh.md)

在与编码智能体协作时，自动化测试已经不再是可有可无的东西了。

过去那些不写测试的老借口——比如它们既耗时，又因为代码库快速演进而需要不断重写、成本很高——在智能体几分钟就能把它们整理到可用状态的前提下，已经站不住脚。

它们对于确保 AI 生成的代码真像它自己声称的那样工作，也同样 _至关重要_。如果一段代码从来没有真正执行过，那么它部署到生产环境以后到底能不能工作，基本只能靠运气。

测试还是帮助智能体迅速熟悉现有代码库的极佳工具。你去问 Claude Code 或类似工具某个现有功能时，留意它接下来会做什么——它很大概率会找到并阅读相关测试。

智能体本来就天然偏向测试；而一旦项目里已经有现成的测试套件，这几乎肯定会进一步推动它去测试自己刚做出的那些新改动。

每次我在一个现有项目上开启新的智能体会话时，通常都会先给出下面这种 Prompt 变体：

> First run the tests

对于我的 Python 项目，我会先把 [`pyproject.toml` 配好](https://til.simonwillison.net/uv/dependency-groups)，这样我就可以改用下面这条 Prompt：

> Run "uv run pytest"

这类四个词的 Prompt 有几个作用：

1. 它会告诉智能体：这里有一套测试，而且还会逼着它先弄清楚这些测试该怎么跑。这样几乎就能确保智能体在后续也会继续运行测试，确认自己没有把什么东西弄坏。
2. 大多数测试执行框架都会让智能体大致知道一共有多少个测试。这可以作为项目规模和复杂度的一个替代指标，也是在暗示它：如果想进一步理解这个项目，最好直接去搜测试本身。
3. 它会把智能体带进一种“测试思维”里。既然已经跑过测试，它后面很自然就会继续补上自己写的新测试。

和 [“Use red/green TDD”](./red_green_tdd_demo_zh.md) 类似，“First run the tests” 也是一个四词 Prompt，但它背后其实压缩了大量已经被模型内化的软件工程纪律。
