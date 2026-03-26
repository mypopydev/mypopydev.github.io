# 让智能体做手动测试

原文标题：Agentic manual testing
原文链接：https://simonwillison.net/guides/agentic-engineering-patterns/agentic-manual-testing/
原文作者：Simon Willison
访问日期：2026-03-25
原文发布日期：2026-03-06
原文最后修改：2026-03-06
译文版本：v0.1

## 译文说明

本文为 Simon Willison《Agentic Engineering Patterns》系列中《Agentic manual testing》的示范中文版。标题采用“让智能体做手动测试”，而不机械直译成更拗口的“智能体式手动测试”，因为这篇文章讲的不是“测试智能体”，也不只是某种抽象测试范式，而是更具体的工程实践：让编码智能体自己去执行那些原本常常需要人手完成的手动测试流程。正文继续沿用本项目既定术语约定，将 Coding Agent 统一译为“编码智能体”，并保留 Playwright、Rodney、Showboat、`python -c`、`curl`、`uvx`、`agent-browser`、`playwright-cli` 等高检索价值工具名、命令与产品名原文。

## 正文

> 所属主题：测试与质量保证
> 上一篇：[先跑测试](./first_run_the_tests_demo_zh.md)
> 下一篇：[线性讲解](./linear_walkthroughs_demo_zh.md)

编码智能体最有决定性的特征，就是它能执行自己写出来的代码。这也是为什么，相比那些只会吐出代码、却没有任何验证手段的 LLM，编码智能体要有用得多。

在那段代码真正执行之前，永远不要假设 LLM 生成的代码就是能工作的。

编码智能体可以确认自己产出的代码是否按预期工作；如果还不行，它也可以继续迭代，直到代码真正工作为止。

让智能体去写单元测试，尤其是采用测试优先的 TDD，是确保它们真的把自己正在写的代码跑过一遍的有力办法。

不过，这并不是唯一值得采用的方法。

代码通过了测试，并不等于它就真的按预期工作。凡是做过自动化测试的人，大概都见过这种情况：测试全都通过了，但代码本身仍然会在某些很明显的地方出问题——比如一启动就把服务器弄崩、没把某个关键 UI 元素显示出来，或者漏掉了测试根本没有覆盖到的某个细节。

自动化测试无法替代手动测试。我喜欢在把一个功能放进正式发布版本之前，先亲眼看到它确实能工作。

我也发现，让智能体自己去做手动测试同样很有价值，而且它经常能揭出自动化测试没有发现的问题。

## 让智能体做手动测试的几种机制

智能体该如何“手动”测试一段代码，取决于那段代码本身是什么。

对于 Python 库来说，一个很好用的模式是 `python -c "... code ..."`。你可以把一段 Python 代码字符串——包括多行字符串——直接传给 Python 解释器执行，其中也可以包含导入其他模块的代码。

各类编码智能体其实都很熟悉这个技巧，有时候你不提醒，它们自己也会这么干。不过，专门提醒它们用 `python -c` 来测试，通常还是很有效：

> Try that new function on some edge cases using `python -c`

其他语言也许有类似机制；就算没有，智能体临时写一个演示文件，然后编译并运行它，成本也很低。我有时还会特意鼓励它把这些文件放在 `/tmp` 里，纯粹是为了避免它们后来被误提交进仓库。

> Write code in `/tmp` to try edge cases of that function and then compile and run it

我做的很多项目都涉及带有 JSON API 的 Web 应用。对这类项目，我会直接让智能体用 `curl` 去跑：

> Run a dev server and explore that new JSON API using `curl`

告诉智能体去“explore”，往往会让它把一个新 API 的很多不同侧面都试一遍，很快就能覆盖掉大量场景。

如果智能体通过手动测试发现某些地方不工作，我喜欢让它用红/绿 TDD 去修。这能确保这个新场景最终会被纳入长期保留的自动化测试里。

## 用浏览器自动化测试 Web UI

如果项目里有交互式 Web UI，那么把手动测试流程建立起来，就会变得更有价值。

历史上，这类东西一直很难直接从代码层面测试；但过去十年里，自动化真实 Web 浏览器的系统已经有了相当明显的进步。用真实的 Chrome、Firefox 或 Safari 去跑一个应用，能在更贴近现实的环境里暴露出各种有意思的问题。

编码智能体非常擅长使用这类工具。

当下其中最强大的，是微软开发的开源库 Playwright。Playwright 提供了功能完整的 API，也给多种流行编程语言提供了绑定，几乎可以自动化所有主流浏览器引擎。

很多时候，你只要直接告诉智能体“用 Playwright 测一下那个”，可能就已经够了。它接下来会自己选一个最合适的语言绑定，或者直接使用 Playwright 的 `playwright-cli` 工具。

专用 CLI 和编码智能体的配合通常非常好。Vercel 的 `agent-browser` 就是一个围绕 Playwright 的完整 CLI 封装，专门给编码智能体使用。

我自己的项目 Rodney 也在做类似的事，只不过它是通过 Chrome DevTools Protocol 直接控制一个 Chrome 实例。

下面是我用 Rodney 来测试东西时常用的一条 Prompt：

> Start a dev server and then use `uvx rodney --help` to test the new homepage, look at screenshots to confirm the menu is in the right place

这条 Prompt 里其实藏了三个技巧：

1. 说“use `uvx rodney --help`”会让智能体通过 `uvx` 这个包管理工具去运行 `rodney --help`，而 Rodney 会在第一次调用时自动安装。
2. `rodney --help` 这个命令本来就是专门为智能体设计的，目的是把理解和使用这个工具所需的信息一次性都给它。那份帮助文本本身就是说明书。
3. 说“look at screenshots”是在暗示智能体：它应该去用 `rodney screenshot` 命令，同时也在提醒它，它可以调用自己的视觉能力来检查生成出来的图片文件，从而判断页面视觉外观是否正确。

这么短的一条 Prompt，里面其实已经塞进了大量手动测试工作。

Rodney 以及类似工具能提供的能力非常多，从在已经加载的网站里运行 JavaScript，到滚动、点击、输入，甚至读取页面的可访问性树，都包括在内。

和其他形式的手动测试一样，通过浏览器自动化发现并修复的问题，后续同样可以被补进长期保留的自动化测试里。

过去很多开发者不愿意写太多自动化浏览器测试，因为这类测试一直以脆弱著称——页面 HTML 只要稍微改一点点，就可能引来一波令人沮丧的测试失效。

如果把这些测试长期交给编码智能体维护，那么当 Web 界面的设计发生变化时，要让它们保持最新状态，摩擦成本就会小很多。

## 让它们用 Showboat 做笔记

让智能体手动测试代码，不光能多抓出一些问题，还能顺手产出一些工件，用来帮助记录代码，也帮助展示这段代码究竟是怎么被测试过的。

我一直很着迷于一个挑战：怎么让智能体把它的工作过程展示出来。能够看到演示，或者看到那些被记录下来的实验，是判断智能体是否真正把它接到的挑战完整解决掉的一种非常有用的方式。

我做了 Showboat，专门帮助生成能够捕捉这种智能体手动测试流程的文档。

下面是一条我经常使用的 Prompt：

> Run `uvx showboat --help` and then create a `notes/api-demo.md` showboat document and use it to test and document that new API.

和上面的 Rodney 一样，`showboat --help` 会教会智能体 Showboat 是什么、该怎么用。那份帮助文本本身就已经把用法说清楚了。

Showboat 里最关键的三个命令是 `note`、`exec` 和 `image`。

- `note`：往 Showboat 文档里追加一段 Markdown 笔记。
- `exec`：先记录一条命令，再运行它，并把输出也一起记下来。
- `image`：把图像添加到文档里——这对插入用 Rodney 截下来的 Web 应用截图尤其有用。

这里面最重要的是 `exec`，因为它会把命令和最终输出一起捕捉下来。这样你就能看到智能体到底做了什么，结果又是什么；它的设计目的之一，就是尽量防止智能体“作弊”，避免它把自己以为会发生、或者希望发生的事情直接写进文档。

我越来越觉得，Showboat 这种模式非常适合拿来记录智能体会话期间完成的工作。我也希望未来能在更广泛的一批工具里看到类似模式被采纳。
