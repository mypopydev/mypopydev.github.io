# 《Floating point from scratch: Hard Mode》中文翻译 Implementation Plan

**Goal:** 将 Julia Desmazes 的技术长文《Floating point from scratch: Hard Mode》（2026-04-03，约 9,355 词）译为中文，纳入本 MkDocs 站点。本文属硬件浮点 / bfloat16 / ASIC 流片领域，与智能体工程无关。需处理 LaTeX 数学、C/C++/Verilog/汇编代码块、约 18 张配图、术语一致性。遵循项目「保留原始 URL / 代码命令不翻」总原则，并通过 `mkdocs build --strict`。

**Architecture:** 单篇译文。译文存 `docs/articles/floating-point-from-scratch-hard-mode-zh.md`；标题《从零实现浮点运算：困难模式》；图片本地化至 `docs/assets/images/articles/floating-dragon/`；新建顶层导航板块「浮点与芯片设计」；术语在文末「术语对照」统一（不污染智能体工程术语表）；`mkdocs build --strict` 通过 0 警告。

**Tech Stack:** MkDocs Material、`pymdownx.arithmatex`（generic: true，支持 `$…$`/`$$…$$`）、KaTeX 渲染、WebFetch（取原文）、curl（下载配图）、Git。

---

## 原文基线（已抓取确认）

- 标题：Floating point from scratch: Hard Mode · Tales on the wire
- 作者：Julia Desmazes ｜ 日期：2026-04-03 ｜ 约 9,355 词 ｜ 英文
- 领域：浮点运算从零实现（IEEE-754 背景 → C 加法器 → ASIC 硬件设计 → 验证 → 两次硅流片）
- 结构：H1 标题 + 导语 + 三类懂浮点的人；第一章 Descent into madness（浮点原理、+0/-0、NaN、∞、次正规数/渐进下溢、舍入模式含表格、边界行为、无序、C 加法器示例）；第二章（打造困难部分、ASIC 规则、优化、需要什么→选 bfloat16、双路径加法器架构）；第三章 Theory meets reality（验证、stdfloat 行为、x86 反汇编、被 C++ 背叛、1 ulp、实现、Tiny Tapeout ihp26a、Yosys/LZC、Combo ihp0p4、454.545 MHz 乘法器）；收尾 + Waffle House + P.S。
- 数学：KaTeX 渲染；公式如 $(-1)^S \times 2^{E-b} \times (1+T\cdot2^{1-p})$、$\text{ulp}(x)=2^{-p+1}$、$\text{error}(x)=\frac{x_{model}-x_{hw}}{x_{model}}$。原始 Markdown 在 `github.com/Essenceia/essenceia.github.io`（main, `projects/floating_dragon/`），因 GitHub API 限流未能取原文 markdown，改用 WebFetch 全文 + 渲染 HTML 还原数学与图片。
- 代码：C（`bf16_add` 加法器）、C++（rounding 示例）、Verilog（`pmux`/LZC）、x86 汇编（反汇编）、plain text。全部保留原文。
- 配图：18 张（ieee_layout.png、denorm0/1.png、rounding.png、ko.jpeg、sky130 svg×2、adder.png、adder_edit*.jpg、my_adder.jpg、placement.gif、systolic_array_v2_floorplan.png、ihp26a_chip.png、ihp0p4_chip.png、my_mul.jpg、fast_mul_floorplan.png、waffles.webp），均 `<figure><img src=/projects/floating_dragon/...>`。
- 表格：1 个（舍入模式→结果）。

## 决策点（已与用户确认，采用推荐默认）

1. 导航位置：**新建顶层板块「浮点与芯片设计」**（与智能体工程 / 深度学习并列）。
2. 标题：**《从零实现浮点运算：困难模式》**。
3. 配图：**本地化**（下载至 `docs/assets/images/articles/floating-dragon/`），与 agentic-code-review 译文一致。
4. 交付粒度：**单文件整篇**。

## Task 1: 下载配图

- [x] 下载 18 张图到 `docs/assets/images/articles/floating-dragon/`，markdown 图片路径改为 `../assets/images/articles/floating-dragon/NAME`。

## Task 2: 翻译正文

- [x] 写入 `docs/articles/floating-point-from-scratch-hard-mode-zh.md`（H1 直入，不写元信息块）。
- [x] 逐节翻译；数学包 `$…$`/`$$…$$`；代码块原样；图片本地路径；外链保留原文。
- [x] 文末加「术语对照」表（浮点领域术语，不污染智能体工程术语表）。
- [x] 移除原文标题后的自引用锚点 `[\#](#...)`（MkDocs 自带锚点，避免断链警告）。

## Task 3: 导航接入与首页

- [x] `mkdocs.yml` 新增顶层「浮点与芯片设计」板块并加条目。
- [x] `docs/index.md` 新增「浮点与芯片设计」区块入口。

## Task 4: 严格构建

- [x] `mkdocs build --strict` 通过，0 真实警告（仅 Material 横幅）。

## Task 5: CHANGELOG 与提交

- [x] CHANGELOG 顶部追加条目。
- [x] `git commit`（不自动 push）。

## Self-Review

1. Spec coverage：配图（T1）、翻译（T2）、导航（T3）、构建（T4）、CHANGELOG+提交（T5）全覆盖。
2. 一致性：数学由 arithmatex 渲染；代码/URL/文件名保留英文；外链 31 条 + mailto 全部保留；术语对照独立成节，未动智能体工程术语表。
