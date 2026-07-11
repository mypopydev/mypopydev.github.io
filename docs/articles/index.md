# 独立文章栏目说明

`articles/` 用来放与任何现有专题都没有强绑定关系的内容，例如单篇技术随笔、工具实践、翻译方法笔记、站点维护笔记，或者未来某些只需要单独发布、暂时不值得做成专题的文章。

一个简单的判断方法是：如果某篇文章需要和前后文一起读、需要专题页承接、需要专题内上一篇/下一篇导航，那它更适合放到 `series/`；如果它本身就是独立完整的内容，那就更适合放到 `articles/`。

建议后续新增独立文章时，直接使用清晰的英文 slug 命名文件，例如 `articles/mkdocs-notes.md`、`articles/translation-workflow.md`。如果文章有专属配图，可以把图片放到 `assets/images/articles/<article-slug>/`。

## 当前已纳入的独立文章

- [反向传播：想法、数学原理、思想史与最值得读的 5 篇文献](./backpropagation-ideas-math-history-5-readings.md)

  这是一篇面向机器学习学习者与工程实践者的长文，系统梳理反向传播的核心直觉、链式法则与计算图、reverse-mode automatic differentiation、历史发展脉络，以及最值得读的 5 篇论文或文章。文中配有 7 张示意图，适合作为学习笔记、讲解材料或后续专题扩展的入口。

- [计算图上的微积分：反向传播](./calculus-on-computational-graphs-backpropagation-zh.md)

  这是一篇对 Christopher Olah 经典文章《Calculus on Computational Graphs: Backpropagation》的中文整理稿，重点从标量计算图出发解释链式法则、路径因式分解，以及为什么 reverse-mode automatic differentiation 能高效求出“一个输出对所有输入”的导数。文中配套收录了原文相关示意图，适合作为理解反向传播直觉与自动微分基础的入门材料。

- [Transformer Math 101：训练计算量与显存需求速查](./transformer-math-101-zh.md)

  这是一篇对 EleutherAI《Transformer Math 101》的中文翻译，集中整理了 Transformer 训练中的 FLOPs 估算、推理与训练显存公式、激活值重计算、ZeRO/FSDP，以及 3D 并行下的内存近似公式。文中保留了原文关键示意图与公式，适合作为做模型规模规划、显存预算和分布式训练前的速查材料。

- [Transformer 推理算术：用少量公式理解大语言模型推理性能](./transformer-inference-arithmetic-zh.md)

  这是一篇聚焦 LLM 推理性能估算的中文译文，系统梳理 KV Cache、显存容量、张量并行通信、decode 延迟公式、batch size 权衡、中间激活值带宽成本，以及与公开 benchmark 的对照。它和《Transformer Math 101》偏训练侧的内容刚好互补，适合作为推理侧容量规划与延迟估算的入门速查。

- [LLM 优化面试笔记：训练与推理](./llm-optimization-interview-notes-training-and-inference-zh.md)

  这是一篇基于 X Article 整理的中文译文，从内存优化、计算优化、推理优化到训练并行策略，概览了 Flash Attention、KV Cache、量化、ZeRO、Pipeline Parallelism、Tensor Parallelism、MoE 等主题。内容偏高层总结，适合作为准备大模型系统设计面试或快速回顾优化版图的提纲。

- [量化神经网络：你只需要这一篇指南](./quantized-neural-networks-the-only-guide-you-need-zh.md)

  这是一篇面向工程实践者的量化综述译文，系统梳理权重量化与激活值量化、均匀网格与对数量化、块级缩放、敏感层、PTQ 与 QAT、KV Cache 量化，以及硬件演进方向。正文以中文整理稿为主，并收录原文配图，适合作为后续阅读模型压缩与推理优化资料前的总览入口。

- [量化可视化指南：大语言模型压缩入门](./a-visual-guide-to-quantization-zh.md)

  这是一篇围绕 LLM 量化基础概念的可视化入门译文，重点解释位宽、动态范围、对称与非对称量化、裁剪与校准、PTQ、QAT、GPTQ、GGUF，以及 BitNet/1.58 bit 路线。正文保留了原文的 60 余张示意图，适合作为量化领域的第一遍系统扫盲材料。

- [什么是扩散模型？](./what-are-diffusion-models-zh.md)

  这是一篇对 Lilian Weng《What are Diffusion Models?》的中文翻译，系统梳理前向/反向扩散、DDPM 损失、NCSN、classifier guidance、DDIM、progressive distillation、consistency models、latent diffusion、ControlNet 与 DiT 等主题。文中保留原文 19 张关键配图与主要公式，适合作为扩散模型发展脉络与方法总览的长篇入门资料。

- [Diffusion Transformer（DiT）模型：初学者指南](./diffusion-transformer-models-beginners-guide-zh.md)

  这是一篇面向入门读者的 DiT 综述译文，重点解释扩散模型、U-Net、ViT、LDM 与 DiT 之间的关系，并结合 DiT-XL/2、Sora、Stable Diffusion 3、PixArt-α 等案例说明 Transformer 主干在生成模型中的应用。文中收录了原文 5 张关键配图与对应资料链接，适合作为从扩散模型过渡到 DiT 的第一篇阅读材料。

- ["齐次"是怎么成为中文数学术语的？](./homogeneous-chinese-translation-etymology-zh.md)

  - [循环工程设计模式（10 Loop Engineering Design Patterns）](./loop-engineering-design-patterns-zh.md)

  这是一篇对 Data Science Dojo《10 Loop Engineering Design Patterns for AI Builders (2026)》的中文翻译，系统梳理从基础 ReAct 循环到生产加固模式的十种 Agent 循环设计模式。全文按三个层级组织——基础模式（1-4）、实践者模式（5-7）、生产加固模式（8-10），并附模式选型指南与常见问题解答。

- [如何与 AI 协作并实现复利增长（Working with AI）](./working-with-ai-zh.md)

  这是一篇对 Eugene Yan《How to Work and Compound with AI》的中文翻译，系统阐述与 AI 高效协作的五大原则：提供良好上下文、将品味编码为配置、让验证变得简单、委托更大任务、形成闭环。文章以 Claude Code 为主要实践场景，涵盖 CLAUDE.md 配置、技能系统、验证阶梯、并行会话、会话转录挖掘等实操方法论。

- [智能体循环详解：从 ReAct 到循环工程（Agentic Loops Explained）](./agentic-loops-explained-zh.md)

  这是一篇对 Data Science Dojo《Agentic Loops Explained: From ReAct to Loop Engineering (2026 Guide)》的中文翻译，系统梳理从 AutoGPT（2023）到 ReAct、OODA、Ralph 循环、/goal 命令四代智能体循环的演变。全文涵盖循环内部机制、记忆类型、六种失败模式、护栏体系、循环选型决策表与常见问题解答。

- [Ralph Wiggum 当"软件工程师"（Ralph Loop 技术）](./ralph-wiggum-zh.md)

  这是一篇对 Geoffrey Huntley《Ralph Wiggum as a "software engineer"》的中文翻译。作者是 Ralph 循环（Bash `while` 循环驱动智能体）的发明者，本文是该技术的原始阐述——从核心定义、游乐场比喻，到单体架构、子智能体调度、反压机制、测试驱动，再到完整 CURSED 语言构建的 Prompt 实战。全文保留原文口语化、幽默的叙事风格。
