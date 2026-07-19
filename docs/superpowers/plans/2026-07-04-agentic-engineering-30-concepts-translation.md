# 翻译《30 Core Agentic Engineering Concepts Every Developer Should Know》实施计划

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** 将 Medium 文章《30 Core Agentic Engineering Concepts Every Developer Should Know》译为中文，按本项目翻译规范接入 MkDocs 站点，并放置在「智能体工程 > 综合概览」导航下。

**Architecture:** 单篇 Markdown 译文（含页头元信息 + 译文说明）+ 本地图片资源 + 导航/术语表/更新日志三处元数据同步。翻译以英文原文为准，遵循 `docs/resources/agentic_engineering_translation_glossary_style_guide_template.md`。

**Tech Stack:** MkDocs Material、Markdown、项目术语表与风格指南、mkdocs build 校验。

**源与已知缺口：**
- 主源：`https://medium.com/@Deep-concept/5066b3117f69`（访问日期 2026-07-04）
- 已取到 1–25、27、28、30 全文（Medium）。
- #26 **Observability（可观测性）**：Medium 仅取到引导句 *"Ready for the best part? Once agents start working on real tasks, we need to understand what they are doing."*，正文疑似极短（作为可观测性小节引导）。
- #29 **Replay（回放）**：Medium 截断缺失，已从镜像 `https://teamstation.dev/research/articles/30-core-agentic-engineering-concepts-every-developer-should-know` 补全（该镜像第 29 条即 Replay，编号一致，内容可信）。
- 注意：腾讯云中文版为**重写/重组稿**（拆成 6 层、缺少 #26/#29），不作为翻译底本，仅作术语参考。

---

## 文件结构

- Create: `docs/articles/30-core-agentic-engineering-concepts-zh.md` — 译文正文
- Create: `docs/assets/images/articles/30-core-agentic-engineering-concepts/*.png` — 下载的原文配图（本地化）
- Modify: `mkdocs.yml` — 在「智能体工程」下新增「综合概览」子项
- Modify: `docs/index.md` — 首页新增一条指向该文的链接（与现有列表风格一致）
- Modify: `docs/resources/agentic_engineering_translation_glossary_style_guide_template.md` — 在「可追加术语表」补 10 个新术语
- Modify: `docs/resources/CHANGELOG.md` — 追加本次新增记录
- Modify(可选): `docs/resources/BILINGUAL_LINK_MAP.md` — 底部追加一条非 SW 系列映射（若维护者希望集中追踪）

---

### Task 1: 归集并核对英文原文

**Files:**
- Create: `docs/articles/.src/30-concepts-en-raw.md`（临时工作稿，提交前可删除）

- [ ] **Step 1: 汇编英文底本**

将已取到的 1–25、27、28、30 全文 + #26 引导句 + #29 Replay 合并为一个英文工作稿，按 1–30 顺序排列。结构示例：

```md
# 30 Core Agentic Engineering Concepts Every Developer Should Know

## 1. Agent
...
## 25. Pre-Commit Gates
...
## 26. Observability
Ready for the best part? Once agents start working on real tasks, we need to understand what they are doing.
## 27. Tracing
...
## 28. Logging
...
## 29. Replay
Replay means taking a previous agent run and walking it again ...
## 30. Metrics
...
```

- [ ] **Step 2: 复核 #26 是否仍有遗漏正文**

Run: 重新对 Medium 原文做一次定向抓取，提示词聚焦 `## 26.` 与 `## Observability` 之后的段落。
Expected: 若 #26 仅有上述引导句，则按「极短小节」处理；若发现更多段落，补入工作稿。
Fallback: 若始终只能取到引导句，按现状翻译并在「译者注」中说明该节原文极简。

- [ ] **Step 3: 提取全部图片 URL**

Run:
```bash
grep -oE 'https://miro\.medium\.com/[^)]+' docs/articles/.src/30-concepts-en-raw.md \
  | sort -u > docs/articles/.src/image-urls.txt
wc -l docs/articles/.src/image-urls.txt
```
Expected: 列出所有 miro 图片链接（预计 20+ 张）。

---

### Task 2: 建立译文文件与页头

**Files:**
- Create: `docs/articles/30-core-agentic-engineering-concepts-zh.md`

- [ ] **Step 1: 写入页头元信息与译文说明（遵循风格指南模板第八章）**

```md
# 每个开发者都该知道的 30 个智能体工程核心概念

原文标题：30 Core Agentic Engineering Concepts Every Developer Should Know
原文链接：https://medium.com/@Deep-concept/5066b3117f69
原文作者：Deep concept（Let’s Code Future）
译文版本：v0.1
译者：（填写）
审校：（填写）

## 译文说明

本文为 Medium 文章《30 Core Agentic Engineering Concepts Every Developer Should Know》的中文翻译。术语使用遵循本项目统一术语表（见 `docs/resources/agentic_engineering_translation_glossary_style_guide_template.md`）。代码、命令、URL、文件名默认保留原文；Prompt 如为可执行输入，一般保留英文并补充中文解释。其中第 26 节（可观测性）与第 29 节（回放）部分内容依据镜像站补全，已在对应节末以译者注标注。

## 正文
```

- [ ] **Step 2: 写入 30 个中文小节标题（结构骨架）**

在 `## 正文` 之后按以下标题逐节翻译（标题译法遵循术语表，保留高辨识度英文于括号）：

```md
## 1. 智能体（Agent）
## 2. 执行模型（Execution Model）
## 3. 智能体状态（Agent State）
## 4. 常见智能体模式（Common Agent Patterns）
## 5. 智能体配置文件（Agent Config Files）
## 6. 可复用工作流文件（Reusable Workflow Files）
## 7. 工作流框架（Workflow Frameworks）
## 8. Prompt 缓存（Prompt Caching）
## 9. 上下文腐烂（Context Rot）
## 10. 模型上下文协议（MCP）
## 11. 实时文档检索（Live Document Retrieval）
## 12. AI 原生网页搜索（AI-Native Web Search）
## 13. 可视化输出生成（Visual Output Generation）
## 14. 持久化记忆（Persistent Memory）
## 15. 知识搜索（Knowledge Search）
## 16. 子智能体（Subagents）
## 17. 智能体循环（Agent Loops）
## 18. 编排工具（Orchestration Tools）
## 19. 托管 / 云端智能体（Managed / Cloud-Hosted Agents）
## 20. 沙箱（Sandboxing）
## 21. 权限（Permissions）
## 22. 钩子（Hooks）
## 23. Prompt 注入防御（Prompt Injection Defense）
## 24. 结构化代码检查（Structural Code Linting）
## 25. 提交前门禁（Pre-Commit Gates）
## 26. 可观测性（Observability）
## 27. 追踪（Tracing）
## 28. 日志（Logging）
## 29. 回放（Replay）
## 30. 指标（Metrics）
```

---

### Task 3: 翻译正文（逐节）

**Files:**
- Modify: `docs/articles/30-core-agentic-engineering-concepts-zh.md`

- [ ] **Step 1: 逐节翻译 1–30，遵守风格指南**

翻译规则（摘自术语表/文风指南）：
- 术语统一：`智能体`、`子智能体`、`编码智能体`、`沙箱`、`钩子`、`可观测性`、`追踪`、`日志`、`指标`、`回放`、`编排`、`MCP`、`Prompt`、`Token`、`Context Window` 等按术语表处理，首次出现括注英文。
- 代码块、命令、URL、文件名、产品名（Claude Code、GitHub、Figma、draw.io、Remotion、Context7、DeepWiki、Exa、Conductor、Tirith 等）保留原文。
- 短句优先、主动句优先，不硬搬英文长句；长段落按「定义/原因/例外/示例」拆段。
- 列表平行、加粗仅标关键。
- 第 26 节若仅引导句，译为中文后以 `[译者注] 原文此节仅一段引导语，细节由后续追踪/日志/回放/指标展开。` 标注。
- 第 29 节（Replay）译文末加 `[译者注] 本节依据 teamstation.dev 镜像补全，原文在 Medium 抓取时缺失。`

- [ ] **Step 2: 通读自检（对照风格指南第九章清单）**

- [ ] 术语全篇统一，无「代理工程/编程智能体」混用
- [ ] 代码/命令/URL/文件名未被中文化
- [ ] 中文自然、长句已拆、标题清楚
- [ ] 记录原文链接与访问日期、译文版本

---

### Task 4: 本地化图片

**Files:**
- Create: `docs/assets/images/articles/30-core-agentic-engineering-concepts/*.png`

- [ ] **Step 1: 建目录并下载**

Run:
```bash
mkdir -p docs/assets/images/articles/30-core-agentic-engineering-concepts
i=1
while read -r url; do
  printf -v n "%02d" "$i"
  curl -fsSL "$url" -o "docs/assets/images/articles/30-core-agentic-engineering-concepts/concept-$n.png" \
    && echo "saved concept-$n.png" || echo "FAILED $url"
  i=$((i+1))
done < docs/articles/.src/image-urls.txt
```

- [ ] **Step 2: 替换正文图片引用为相对路径**

将译文中的 `![](https://miro.medium.com/...)` 依次替换为 `![](../assets/images/articles/30-core-agentic-engineering-concepts/concept-01.png)` …（按顺序对应）。
下载失败的项保留原始远程 URL 并加 `[译者注] 原图未能本地化。`。

- [ ] **Step 3: 校验图片引用**

Run:
```bash
grep -nE '!\[[^]]*\]\((.*)\)' docs/articles/30-core-agentic-engineering-concepts-zh.md \
  | grep -E 'miro\.medium|assets/images' | head
```
Expected: 所有图片引用要么指向本地 `assets/...`，要么保留 `miro.medium.com` 并已加译者注。

---

### Task 5: 更新术语表（追加新术语）

**Files:**
- Modify: `docs/resources/agentic_engineering_translation_glossary_style_guide_template.md`

- [ ] **Step 1: 在「四、可追加术语表模板」的表格中追加以下行**

| 英文原词 | 推荐译法 | 可接受替代 | 是否保留英文 | 使用说明 | 所在页面 |
|---|---|---|---|---|---|
| Observability | 可观测性 | — | 视语境 | 首次写法「可观测性（Observability）」 | 30 概念 |
| Tracing | 追踪 | 调用追踪 | 一般不保留 | 指 agent 运行路径记录 | 30 概念 |
| Logging | 日志 | — | 一般不保留 | 指运行原始记录 | 30 概念 |
| Metrics | 指标 | 度量 | 一般不保留 | 指延迟/成本/次数等信号 | 30 概念 |
| Replay | 回放 | 重放 | 一般不保留 | 指重现历史运行以调试 | 30 概念 |
| Hook | 钩子 | — | 一般不保留 | 指工作流特定点的检查点 | 30 概念 |
| Permission | 权限 | — | 一般不保留 | 指工具调用授权规则 | 30 概念 |
| Orchestration | 编排 | — | 一般不保留 | 指多 agent 协同管理 | 30 概念 |
| Prompt Caching | Prompt 缓存 | — | 建议保留英文 | 首次写法「Prompt 缓存」 | 30 概念 |
| Context Rot | 上下文腐烂 | 上下文劣化 | 一般不保留 | 指长上下文导致质量下降 | 30 概念 |

---

### Task 6: 更新导航 mkdocs.yml

**Files:**
- Modify: `mkdocs.yml:73-95`

- [ ] **Step 1: 在「智能体工程」下新增「综合概览」子项（置于专题导读之后）**

找到：
```yaml
  - 智能体工程:
      - 专题导读: series/agentic-engineering-patterns/index.md
```
改为：
```yaml
  - 智能体工程:
      - 专题导读: series/agentic-engineering-patterns/index.md
      - 综合概览:
          - 每个开发者都该知道的 30 个智能体工程核心概念: articles/30-core-agentic-engineering-concepts-zh.md
```

- [ ] **Step 2: 校验 YAML 缩进**

Run: `python3 -c "import yaml,sys; yaml.safe_load(open('mkdocs.yml')); print('mkdocs.yml OK')"`
Expected: 输出 `mkdocs.yml OK`

---

### Task 7: 更新首页 index.md

**Files:**
- Modify: `docs/index.md`

- [ ] **Step 1: 在「智能体工程」专题块内新增一条链接**

在 `docs/index.md` 的 `### 🤖 智能体工程` 区块中，于现有列表后追加：

```md
- [每个开发者都该知道的 30 个智能体工程核心概念](./articles/30-core-agentic-engineering-concepts-zh.md)
```

（与现有 `- [反向传播：…](./articles/...)` 风格保持一致，放在「智能体工程」相关入口附近。）

---

### Task 8: 更新 CHANGELOG 与双语映射

**Files:**
- Modify: `docs/resources/CHANGELOG.md`
- Modify(可选): `docs/resources/BILINGUAL_LINK_MAP.md`

- [ ] **Step 1: 在 CHANGELOG 顶部追加本次记录**

```md
## 2026-07-04

**新增「智能体工程 > 综合概览」**

- 收录《30 Core Agentic Engineering Concepts Every Developer Should Know》中文译文，置于 `docs/articles/30-core-agentic-engineering-concepts-zh.md`
- 导航新增「综合概览」子项，首页新增入口
- 术语表追加 Observability / Tracing / Logging / Metrics / Replay / Hook / Permission / Orchestration 等 10 个术语
- 备注：第 26 节（可观测性）与第 29 节（回放）部分内容依据 teamstation.dev 镜像补全
```

- [ ] **Step 2（可选）: 在 BILINGUAL_LINK_MAP.md 底部追加非 SW 系列映射**

```md
### 7. 其他外部译文（非 Simon Willison 系列）

| 序号 | 中文文件 | 中文标题 | 原文标题 | 原文 URL |
| --- | --- | --- | --- | --- |
| 1 | `30-core-agentic-engineering-concepts-zh.md` | 每个开发者都该知道的 30 个智能体工程核心概念 | 30 Core Agentic Engineering Concepts Every Developer Should Know | `https://medium.com/@Deep-concept/5066b3117f69` |
```

---

### Task 9: 本地构建校验

**Files:**
- 无新增，校验全站

- [ ] **Step 1: 安装文档依赖（若未装）**

Run: `pip install -r requirements-docs.txt` （或确认 `mkdocs` 已可用：`mkdocs --version`）

- [ ] **Step 2: 严格构建**

Run: `mkdocs build --strict`
Expected: 无报错、无断开链接、无缺失图片警告。若出现图片 404，回到 Task 4 修正路径；若出现导航报错，回到 Task 6 修正缩进。

- [ ] **Step 3: 本地预览抽查（可选）**

Run: `mkdocs serve` 后浏览器打开 `http://127.0.0.1:8000`，确认新文章渲染、图片加载、目录锚点正常。

---

### Task 10: 提交

**Files:**
- 新增：`docs/articles/30-core-agentic-engineering-concepts-zh.md`、`docs/assets/images/articles/30-core-agentic-engineering-concepts/*.png`
- 修改：`mkdocs.yml`、`docs/index.md`、术语表、`CHANGELOG.md`、（可选）`BILINGUAL_LINK_MAP.md`
- 可删除：`docs/articles/.src/`（临时工作稿）

- [ ] **Step 1: 清理临时稿**

Run: `rm -rf docs/articles/.src`

- [ ] **Step 2: 提交**

```bash
git add docs/articles/30-core-agentic-engineering-concepts-zh.md \
        docs/assets/images/articles/30-core-agentic-engineering-concepts \
        mkdocs.yml docs/index.md \
        docs/resources/agentic_engineering_translation_glossary_style_guide_template.md \
        docs/resources/CHANGELOG.md docs/resources/BILINGUAL_LINK_MAP.md
git commit -m "docs: 翻译《30 Core Agentic Engineering Concepts》并接入导航"
```

---

## 自审（Self-Review）

1. **覆盖度**：源文 30 节全部映射到译文骨架（Task 2 Step 2）；#26/#29 缺口已有明确补全与译者注方案（Task 1、Task 3）。
2. **占位符扫描**：各 Task 均给出具体文件、具体 YAML/Markdown 片段与具体命令；无 TBD/TODO。图片下载用脚本骨架，执行时按 `image-urls.txt` 具体化，属可操作步骤而非占位。
3. **一致性**：术语译法在 Task 2 标题、Task 3 规则、Task 5 术语表三处统一；导航条目标题与 `docs/index.md` 链接标题一致；文件名 `30-core-agentic-engineering-concepts-zh.md` 在 mkdocs.yml、index.md、CHANGELOG、BILINGUAL_LINK_MAP 四处一致。
