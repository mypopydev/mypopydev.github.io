# 我常用的 Prompt

原文标题：Prompts I use
原文链接：https://simonwillison.net/guides/agentic-engineering-patterns/prompts/
原文作者：Simon Willison
访问日期：2026-03-25
原文发布日期：2026-02-28
原文最后修改：2026-03-07
译文版本：v0.1

## 译文说明

本文为 Simon Willison《Agentic Engineering Patterns》系列附录页《Prompts I use》的示范中文版。标题采用“我常用的 Prompt”，保留了 Prompt 的英文形式，也尽量保留原文那种“这是作者个人正在持续维护的一组实战输入”的语气，而不是把它译成太书面、太像理论总览的标题。正文继续沿用本项目既定术语约定，将 Coding Agent 统一译为“编码智能体”，并保留 Prompt、Artifacts、Canvas、React、Claude、Claude Opus、HTML、JavaScript、CSS、Helvetica、Sentence case、alt text 等高检索价值术语与产品名原文。文中三段 Prompt / 自定义指令继续保留英文原文，以保留其可复制、可直接复用的输入属性。

## 正文

> 所属主题：参考资源
> 上一篇：[用 WebAssembly 和 Gifsicle 构建 GIF 优化工具](./gif_optimization_tool_using_webassembly_and_gifsicle_demo_zh.md)
> 下一篇：无

本指南这一节会持续更新，收录我自己实际在用的 Prompt；在合适的地方，我也会从其他章节链接到这里。

## Artifacts（工件）

我经常会用 Claude 的 Artifacts 功能来做原型，也会拿它来搭一些小型 HTML 工具。所谓 Artifacts，就是普通的 Claude 对话直接构建出一个 HTML 和 JavaScript 应用，然后把它直接显示在 Claude 的聊天界面里。OpenAI 和 Gemini 也有一个类似功能，它们都把它叫做 Canvas。

模型特别爱在这种场景里用 React。我不喜欢 React 需要额外的构建步骤；那会让我没法直接把 artifact 里的代码复制出来，再粘贴到别的静态托管环境里。所以我会在 Claude 里建一个 project，并给它下面这组 custom instructions：

> Never use React in artifacts - always plain HTML and vanilla JavaScript and CSS with minimal dependencies.
>
> CSS should be indented with two spaces and should start like this:
>
> ```html
> <style>
> * {
>   box-sizing: border-box;
> }
> ```
>
> Inputs and textareas should be font size 16px. Font should always prefer Helvetica.
>
> JavaScript should be two space indents and start like this:
>
> ```html
> <script type="module">
> // code in here should not be indented at the first level
> ```
>
> Prefer Sentence case for headings.

## Proofreader（校对）

我不会让 LLM 给我的博客代写正文。我的硬性底线是：凡是表达观点，或者用了第一人称 “I” 的内容，都必须是我自己写的。我可以接受 LLM 去更新代码文档；但如果一段内容挂着我的名字、带着我的个人风格，那就必须由我亲自来写。

不过，我确实会用 LLM 给自己准备发布的文字做校对。下面是我当前在用的 proofreading prompt；我把它作为 Claude project 里的 custom instructions：

> You are a proofreader for posts about to be published.
>
> 1. Identify spelling mistakes and typos
> 2. Identify grammar mistakes
> 3. Watch out for repeated terms like "It was interesting that X, and it was interesting that Y"
> 4. Spot any logical errors or factual mistakes
> 5. Highlight weak arguments that could be strengthened
> 6. Make sure there are no empty or placeholder links

## Alt text（替代文本）

我会把下面这段 Prompt 和图片一起使用，用它先生成一版面向无障碍用途的 alt text 初稿。

```markdown-copy
You write alt text for any image pasted in by the user. Alt text is always presented in a fenced code block to make it easy to copy and paste out. It is always presented on a single line so it can be used easily in Markdown images. All text on the image (for screenshots etc) must be exactly included. A short note describing the nature of the image itself should go first.
```

我通常会把它和 Claude Opus 一起用；在我看来，它在写 alt text 这件事上有非常好的品味。它经常会自己做出一些“编辑判断”，比如只突出图表里最有意思的那几个数字。

但这些判断并不总是对的。alt text 应该传达的是图片真正想传递的关键信息。所以我经常还会自己再改一遍这段 Prompt 产出的文字，或者继续追加 Prompt，让它扩写某些描述，或者删掉多余信息。

有时候，我还会把多张图片丢进同一个由这段 Prompt 驱动的对话里。这样一来，模型在描述后面的图片时，就可以参考前面那张图已经传达过的信息。
