# 欢迎

这是我的个人技术笔记站。这里记录我在 AI 工程和深度学习领域的学习、翻译与实践。

---

## 专题阅读

### 🤖 智能体工程

Simon Willison《Agentic Engineering Patterns》系列的 15 篇中文译文，按六大主题组织——从核心原则到协作工作流、测试实践、代码理解和实战案例。

[开始阅读 :octicons-arrow-right-24:](./series/agentic-engineering-patterns/index.md){ .md-button }

- [每个开发者都该知道的 30 个智能体工程核心概念](./articles/30-core-agentic-engineering-concepts-zh.md)
- [循环工程（Loop Engineering）](./articles/loop-engineering-zh.md)
- [智能体式代码审查（Agentic Code Review）](./articles/agentic-code-review-zh.md)
- [循环入门（Getting started with loops）](./articles/getting-started-with-loops-zh.md)
- [面向自我提升的 Harness 工程（Harness Engineering for Self-Improvement）](./articles/harness-engineering-zh.md)
- [循环工程设计模式（10 Loop Engineering Design Patterns）](./articles/loop-engineering-design-patterns-zh.md)
- [如何与 AI 协作并实现复利增长（Working with AI）](./articles/working-with-ai-zh.md)
- [智能体循环详解：从 ReAct 到循环工程（Agentic Loops Explained）](./articles/agentic-loops-explained-zh.md)
- [Ralph Wiggum 当"软件工程师"（Ralph Loop 技术）](./articles/ralph-wiggum-zh.md)
- [软件工厂为何失败（Why Software Factories Fail）](./articles/why-software-factories-fail-zh.md)
- [构建 AI 智能体实用指南（A practical guide to building agents）](./articles/a-practical-guide-to-building-agents-zh.md)
- [Jev 带来了一种新形态的 LLM——System One，也就是决策模型](./articles/jev-decision-models-zh.md)
- [Harness 工程手册（The Harness Playbook）](./articles/harness-playbook-zh.md)
- [大象、金鱼与软件工程的黄金新时代（EGM）](./articles/elephants-goldfish-model-zh.md)

### 🖥️ 训练系统与集群

TPU 与 GPU 集群内部的集合通信（All-Gather、All-Reduce、All-to-All 等）原理剖析。

- [TPU 与 GPU 集群内部：集合通信剖析（Inside TPU and GPU Clusters）](./articles/collective-operations-zh.md)

### 🧠 深度学习

反向传播、自动微分、模型量化、扩散模型与推理优化等基础主题的学习笔记与译文整理，兼顾原理解释与工程实践。

- [苦涩的教训（The Bitter Lesson）](./articles/bitter-lesson-zh.md)
- [反向传播：想法、数学原理、思想史与最值得读的 5 篇文献](./articles/backpropagation-ideas-math-history-5-readings.md)
- [计算图上的微积分：反向传播](./articles/calculus-on-computational-graphs-backpropagation-zh.md)
- [Transformer Math 101：训练计算量与显存需求速查](./articles/transformer-math-101-zh.md)
- [Transformer 推理算术：用少量公式理解大语言模型推理性能](./articles/transformer-inference-arithmetic-zh.md)
- [引导式解码在 vLLM 与 SGLang 上的性能（Guided Decoding）](./articles/guided-decoding-performance-vllm-sglang-zh.md)
- [LLM 优化面试笔记：训练与推理](./articles/llm-optimization-interview-notes-training-and-inference-zh.md)
- [量化神经网络：你只需要这一篇指南](./articles/quantized-neural-networks-the-only-guide-you-need-zh.md)
- [量化可视化指南：大语言模型压缩入门](./articles/a-visual-guide-to-quantization-zh.md)
- [NumPy einsum 基础指南（A basic introduction to NumPy's einsum）](./articles/basic-guide-to-einsum-zh.md)
- [理解 NumPy 的 einsum（Understanding Numpy's einsum）](./articles/understanding-numpys-einsum-zh.md)
- [什么是扩散模型？](./articles/what-are-diffusion-models-zh.md)
- [Diffusion Transformer（DiT）模型：初学者指南](./articles/diffusion-transformer-models-beginners-guide-zh.md)
- [用 SynthID 标记 AI 生成图像（Tagging AI-generated images with SynthID）](./articles/tagging-ai-generated-images-with-synthid-zh.md)

### 🔌 浮点与芯片设计

从零实现浮点运算（bfloat16）、ASIC 硬件设计与流片的硬件向技术长文翻译。

- [从零实现浮点运算：困难模式](./articles/floating-point-from-scratch-hard-mode-zh.md)

### 📄 研究论文

大模型相关前沿研究论文的中文翻译与解读，覆盖推理优化、模型压缩等方向。

- [TurboQuant — KV Cache 压缩算法](./articles/research-papers/turboquant-kv-cache-compression-zh.md)

### 🧩 编程语言与 AI

编程语言研究与 AI 辅助探索的前沿观点。

- [编程语言探索的时代已经到来（The Era of Programming Languages Exploration）](./articles/the-era-of-pl-exploration-zh.md)

### ✨ 智能时代（Intelligence Age）

关于 AI 时代人与机器如何分工的思考。

- [永恒的互补（The eternal complement）](./articles/the-eternal-complement-zh.md)

### 🔢 数学与 AI

AI 对纯数学研究影响的讨论。

- ["AI 时代，纯数学研究的未来是什么？"](./articles/pure-math-research-in-the-age-of-ai-zh.md)

### 📜 数学考证

近代数学术语汉译、书证考据与定名过程的研究笔记。

- ["齐次"是怎么成为中文数学术语的？](./articles/homogeneous-chinese-translation-etymology-zh.md)

---

## 关于这个站

站点由 [MkDocs Material](https://squidfunk.github.io/mkdocs-material/) 驱动，支持数学公式渲染（KaTeX）和代码高亮。推送到 `main` 分支后由 GitHub Actions 自动构建发布。

如有勘误或建议，欢迎到 [GitHub 仓库](https://github.com/mypopydev/mypopydev.github.io) 提 Issue。
