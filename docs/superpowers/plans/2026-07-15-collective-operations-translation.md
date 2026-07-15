# 《TPU 与 GPU 集群内部：集合通信剖析》中文翻译 Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** 将 Aleksa Gordić 博文《Inside TPU and GPU Clusters: The Anatomy of Collective Communication》（2026-07-14）翻译为中文，纳入 MkDocs 站点「训练系统与集群」新栏目。

**Architecture:** 单篇译文 `docs/articles/collective-operations-zh.md`，34 张配图落地本地 `docs/assets/images/articles/collective-operations/`，术语追加项目术语表，导航接入 `mkdocs.yml`「训练系统与集群」新栏目 + CHANGELOG 更新。KaTeX 公式渲染、Material admonition 调换 💡 调用注释、参考文献编号列表保留原文 URL。

**Tech Stack:** MkDocs Material（KaTeX/arithmatex、admonition、emoji）、curl（下载图片）、WebFetch（二次精确抓取原文关键段落）、Git。

## Global Constraints

- 导航新增顶层栏目「训练系统与集群」，位于「智能体工程」与「深度学习」之间。
- 图片全部下载到本地 `docs/assets/images/articles/collective-operations/`，不得外链。
- 数学公式使用 KaTeX（`$...$` 行内 / `$$...$$` 独立），keep code-span dimensions as code.
- 保留所有原始 URL，锚文本可中文化（§6.4）。
- 💡 调用注释转 Material `!!! tip` admonition。
- 产品/协议名保留原文：ICI、DCN、PCIe、NVLink、NVSwitch、SHARP、HBM、NCCL、FSDP。
- 首现术语括注英文，全文统一不再重复括注。
- `mkdocs build --strict` 必须零警告通过。

---

### Task 1: 图片下载（34 张）

**Files:**
- Create: `docs/assets/images/articles/collective-operations/*.png|jpg`

- [ ] **Step 1: 创建目录并下载全部图片**

```bash
BASE="https://www.aleksagordic.com/blog/collective-operations"
DEST="docs/assets/images/articles/collective-operations"
mkdir -p "$DEST"

IMAGES=(
  tpu_classes.png torus.jpg topo_3d.png
  tpu_topology1.png tpu_topology2.png pyramid.png
  tpu_example1.png tpu_example2.png
  gather_motivation.png ring.png representation.png
  all_gather1.png all_gather2.png all_gather3.png all_gather4.png
  reduce_scatter_motivation.png rs1.png all_reduce.png rs2.png rs3.png
  ata1.png ata2.png ata3.png totaltime.png
  gpu_topology.png gpu_ring.png sharp.png gpu_ata.png
  ag_tree.png rs_tree.png
  ag_hierarchy.png ar_hierarchy.png ar_shard_hierarchy.png ata_hierarchy.png
  totaltime_gpu.png
)

for f in "${IMAGES[@]}"; do
  curl -sL "$BASE/$f" -o "$DEST/$f" && echo "✓ $f"
done
```

- [ ] **Step 2: 验证数量**

```bash
ls docs/assets/images/articles/collective-operations/ | wc -l
# Expected: 34
```

- [ ] **Step 3: Commit（图片单独提交，避免混入翻译 diff）**

```bash
git add docs/assets/images/articles/collective-operations/
git commit -m "feat(assets): download 34 figures for collective-operations translation"
```

---

### Task 2: 术语表追加

**Files:**
- Modify: `docs/resources/agentic_engineering_translation_glossary_style_guide_template.md`（「可追加术语表」尾部）

在 `## 四、可追加术语表模板` 表格末尾追加以下行：

```markdown
| collective operation | 集合通信（collective operation） | — | 首现括注 | 分布式训练中 GPU/TPU 协同的通信原语 | 集合通信剖析 |
| All-Gather | 全收集（All-Gather） | — | 首现括注 | N 个分片聚合为完整张量 | 集合通信剖析 |
| Reduce-Scatter | 归约散布（Reduce-Scatter） | — | 首现括注 | 先归约再散布分片，All-Gather 的对偶 | 集合通信剖析 |
| All-Reduce | 全归约（All-Reduce） | — | 首现括注 | Reduce-Scatter + All-Gather 组合 | 集合通信剖析 |
| All-to-All | 全互换（All-to-All） | — | 首现括注 | 分布式转置/令牌路由 | 集合通信剖析 |
| ring / ring algorithm | 环 / 环形算法（ring） | — | 首现括注 | 集合通信常用实现 | 集合通信剖析 |
| tree / tree algorithm | 树 / 树形算法（tree） | — | 首现括注 | log₂ 步数通信 | 集合通信剖析 |
| torus | 环面（torus） | — | 首现括注 | 含环绕的网格拓扑 | 集合通信剖析 |
| mesh | 网格（mesh） | — | 首现括注 | 无环绕的网格 | 集合通信剖析 |
| wraparound | 环绕（wraparound） | — | 一般不保留 | 环面边界回绕特性 | 集合通信剖析 |
| superpod | 超级 Pod（superpod） | — | 首现括注 | 最大 ICI 连接域 | 集合通信剖析 |
| slice | 切片（slice） | — | 首现括注 | TPU slice / ICI 岛 | 集合通信剖析 |
| ICI | ICI | 芯片间互联 | 保留 | inter-chip interconnect | 集合通信剖析 |
| DCN | DCN | 数据中心网络 | 保留 | data center networking | 集合通信剖析 |
| NVLink / NVSwitch | NVLink / NVSwitch | — | 保留 | NVIDIA 高带宽互联 | 集合通信剖析 |
| SHARP | SHARP | — | 保留 | 网内归约计算单元 | 集合通信剖析 |
| fat tree | 胖树（fat tree） | — | 首现括注 | 层次化交换网络拓扑 | 集合通信剖析 |
| Scalable Unit (SU) | 可扩展单元（Scalable Unit，SU） | — | 保留缩写 | DGX 集群的 32 节点分组 | 集合通信剖析 |
| bisection bandwidth | 二分带宽（bisection bandwidth） | — | 首现括注 | 对半切分的集群间带宽 | 集合通信剖析 |
| hierarchical collectives | 分层集合通信（hierarchical collectives） | — | 首现括注 | 跨层级拓扑的通信算法 | 集合通信剖析 |
| recursive doubling / halving | 递归倍增 / 递归折半 | — | 一般不保留 | 树形 All-Gather/Reduce-Scatter | 集合通信剖析 |
| in-network reduction | 网内归约（in-network reduction） | — | 首现括注 | 由交换机直接完成归约 | 集合通信剖析 |
| leaf / spine switch | 叶子交换机 / 脊交换机 | — | 一般不保留 | 胖树中的两级交换机 | 集合通信剖析 |
| scale-up / scale-out | 纵向扩展 / 横向扩展 | — | 首现括注 | NVLink 域内 vs InfiniBand 跨节点 | 集合通信剖析 |
| injection bandwidth | 注入带宽 | — | 一般不保留 | 设备向网络注入数据的带宽 | 集合通信剖析 |
| oversubscription | 超额订阅（oversubscription） | — | 首现括注 | 下游注入超过上游承载 | 集合通信剖析 |
| throughput-bound / latency-bound | 吞吐受限 / 延迟受限 | — | 一般不保留 | 通信性能瓶颈判别 | 集合通信剖析 |
| nearest-neighbor | 近邻（nearest-neighbor） | — | 一般不保留 | TPU 芯片互连的物理相邻 | 集合通信剖析 |
| data / tensor / expert parallelism | 数据并行 / 张量并行 / 专家并行 | — | 一般不保留 | 分布式并行策略 | 集合通信剖析 |
| FSDP | FSDP | — | 保留 | Fully Sharded Data Parallelism | 集合通信剖析 |
| MoE | MoE | 混合专家 | 保留 | Mixture of Experts | 集合通信剖析 |
```

- [ ] **Step 3: Commit**

```bash
git add docs/resources/agentic_engineering_translation_glossary_style_guide_template.md
git commit -m "chore(glossary): add collective-ops / hardware terminology for translation"
```

---

### Task 3: 译文正文 — 头部 + TPU 拓扑段（§引言 ～ §TPU cluster topology）

**Files:**
- Create: `docs/articles/collective-operations-zh.md`

**内容范围：** 从标题到第一段结束（"TPU cluster topology" 段完整翻译），对应原文：
- 引言段落（含 7-part 结构列表）
- §1 TPU cluster topology（整段，含带宽层级示例计算）

**术语与格式：**

- 首现括注：data parallelism → 数据并行（data parallelism），所有并行策略、集合操作、拓扑术语首次括注英文。
- 公式转 KaTeX：`45 GB/s × 1 μs = 45 KB` → `$45\,\text{GB/s} \times 1\,\mu\text{s} = 45\,\text{KB}$`
- 调用注释转 admonition：

```markdown
!!! tip "Boardfly 拓扑"
    Google 的新推理 TPU 芯片 `8i` 并未采用 2D/3D 环面，……

!!! tip "交互式可视化工具"
    这是我用来生成上图的一个小巧[可视化工具](https://tpu-visualizer.uc.r.appspot.com/)……

!!! tip "术语"
    TPU 切片（slice）是单个 TPU Pod 内通过 ICI 连接的一组芯片（"ICI 岛"）。

!!! tip "额外信息"
    TPU 还支持"扭转环面"（twisted torus）配置……
```

- 配图引用（按 HTML 顺序映射）：

```markdown
![TPU 连接类型。](../assets/images/articles/collective-operations/tpu_classes.png)
![2D 环面直觉：带环绕边界的网格。](../assets/images/articles/collective-operations/torus.jpg)
![3D 环面连接。](../assets/images/articles/collective-operations/topo_3d.png)
```

**关键译文片段（示例）：**

```markdown
# TPU 与 GPU 集群内部：集合通信剖析（Inside TPU and GPU Clusters: The Anatomy of Collective Communication）

> 深入解析 All-Gather、Reduce-Scatter、All-Reduce、All-to-All 在 TPU 与 GPU 集群中的实现。

在 2026 年，训练和 serving Transformer 模型本质上是一个大规模分布式系统问题。

……

## TPU 集群拓扑

我将从 TPU 讲起，因为它们的拓扑更均匀，所以比 GPU 集群拓扑更容易推理。
```

- [ ] **Step 1: 翻译引言 + 7-part 列表**
- [ ] **Step 2: 翻译 TPU 拓扑段（v5e 环面、ICI/DCN/PCIe、带宽层级、示例计算）**
- [ ] **Step 3: 插入配图（tpu_classes.png ~ pyramid.png）并按原文位置嵌引用**
- [ ] **Step 4: 公式转为 KaTeX、💡 转 admonition**
- [ ] **Step 5: Commit**

```bash
git add docs/articles/collective-operations-zh.md
git commit -m "feat(translation): add header and TPU topology section of collective-operations"
```

---

### Task 4: 译文 — All-Gather 段

**Files:**
- Append to: `docs/articles/collective-operations-zh.md`

内容：原文 `## Inside All-Gather: 1D/2D Rings, and Chains` 整段。

配图：`gather_motivation.png`、`ring.png`、`representation.png`、`all_gather1.png`～`all_gather4.png`（共 7 张）。

- [ ] **Step 1: 翻译全段正文**
- [ ] **Step 2: 插入配图交叉引用**
- [ ] **Step 3: Commit**

---

### Task 5: 译文 — Reduce-Scatter & All-Reduce 段

**Files:**
- Append to: `docs/articles/collective-operations-zh.md`

内容：`## Reduce-Scatter (and All-Reduce): The Dual of All-Gather` 整段。

配图：`reduce_scatter_motivation.png`、`rs1.png`、`all_reduce.png`、`rs2.png`、`rs3.png`（5 张）。

- [ ] **Step 1: 翻译全段**
- [ ] **Step 2: 插入配图**
- [ ] **Step 3: Commit**

---

### Task 6: 译文 — All-to-All + TPU 总结

**Files:**
- Append to: `docs/articles/collective-operations-zh.md`

内容：`## All-to-All: A Sharded Transpose` + TPU 成本总结段。

配图：`ata1.png`、`ata2.png`、`ata3.png`、`totaltime.png`（4 张）。

- [ ] **Step 1: 翻译全段**
- [ ] **Step 2: 翻译 TPU 成本总结表/图注**
- [ ] **Step 3: Commit**

---

### Task 7: 译文 — GPU 集群拓扑段

**Files:**
- Append to: `docs/articles/collective-operations-zh.md`

内容：`## NVIDIA GPU cluster topology: Nodes, Scalable-Units, Fat Tree` 整段。

配图：`gpu_topology.png`（1 张）。

- [ ] **Step 1: 翻译全段**
- [ ] **Step 2: Commit**

---

### Task 8: 译文 — GPU Intra-Node Collectives 段

**Files:**
- Append to: `docs/articles/collective-operations-zh.md`

内容：`## GPU Collectives Within the Node: Rings, Trees, and SHARP` 整段。

配图：`gpu_ring.png`、`sharp.png`、`gpu_ata.png`、`ag_tree.png`、`rs_tree.png`（5 张）。

- [ ] **Step 1: 翻译全段**
- [ ] **Step 2: Commit**

---

### Task 9: 译文 — GPU Inter-Node Collectives 段

**Files:**
- Append to: `docs/articles/collective-operations-zh.md`

内容：`## GPU Collectives Across Nodes: Hierarchical Algorithms over InfiniBand` 整段。

配图：`ag_hierarchy.png`、`ar_hierarchy.png`、`ar_shard_hierarchy.png`、`ata_hierarchy.png`、`totaltime_gpu.png`（5 张）。

- [ ] **Step 1: 翻译全段**
- [ ] **Step 2: Commit**

---

### Task 10: 译文 — Epilogue + Acknowledgements + References

**Files:**
- Append to: `docs/articles/collective-operations-zh.md`

- [ ] **Step 1: 翻译尾声（保留口语/自嘲语气）**

作者原句 example："Phew, that was a long one! … What originally started as 'let me maybe just make four figures … it shouldn't take more than a day, right, right' somehow turned into this."

参考译法：
> 呼，这篇写得真长！……最初不过是想"画四张图，把 All-Gather、Reduce-Scatter、All-Reduce 和 All-to-All 各画一张就行，一天肯定能搞定吧？对吧？"，结果一步步搞成了现在这个样子。

- [ ] **Step 2: 翻译致谢（保留人名/链接）**

保留原文人名拼写与 GitHub/Twitter 链接，感谢语中文化。

- [ ] **Step 3: 翻译参考文献**

```markdown
## 参考文献

1. "TPU 8t and TPU 8i 技术深度解析"，[https://cloud.google.com/blog/products/compute/tpu-8t-and-tpu-8i-technical-deep-dive](https://cloud.google.com/blog/products/compute/tpu-8t-and-tpu-8i-technical-deep-dive)
2. "TPU 拓扑可视化工具"，[https://tpu-visualizer.uc.r.appspot.com/](https://tpu-visualizer.uc.r.appspot.com/)
3. "How to Scale Your Model"（如何扩展你的模型），[https://jax-ml.github.io/scaling-book/](https://jax-ml.github.io/scaling-book/)
4. "NVSwitch Hot Chips 2022"，[https://hc34.hotchips.org/assets/program/conference/day2/Network%20and%20Switches/NVSwitch%20HotChips%202022%20r5.pdf](https://hc34.hotchips.org/assets/program/conference/day2/Network%20and%20Switches/NVSwitch%20HotChips%202022%20r5.pdf)
5. "How to Scale Your Model: GPUs / intra-node collectives"，[https://jax-ml.github.io/scaling-book/gpus/#intra-node-collectives](https://jax-ml.github.io/scaling-book/gpus/#intra-node-collectives)
6. Axel 在 32-GPU H100 InfiniBand 环境上用 NCCL 2.29.7 重跑了基准测试，印证了~1.3× 加速的结果。Pranjal 也报告了相同结果。Arun 认为这更多是 NCCL 的问题而非 SHARP 本身的问题。
```

- [ ] **Step 4: Commit**

---

### Task 11: 导航接入 + CHANGELOG

**Files:**
- Modify: `mkdocs.yml`
- Modify: `docs/resources/CHANGELOG.md`

- [ ] **Step 1: mkdocs.yml 新增栏目**

在 `nav:` 下、「智能体工程」与「深度学习」之间插入：

```yaml
  - 训练系统与集群:
      - TPU 与 GPU 集群内部：集合通信剖析: articles/collective-operations-zh.md
```

修改位置：`mkdocs.yml` 中 nav 区的「智能体工程」段后（约第 105 行）、「深度学习」段前（约第 106 行）。

- [ ] **Step 2: CHANGELOG 追加条目**

在 `docs/resources/CHANGELOG.md` 顶部追加：

```markdown
### 2026-07-15
- 新增译文：TPU 与 GPU 集群内部：集合通信剖析（Aleksa Gordić, 2026-07-14）
- 导航新增「训练系统与集群」栏目
- 术语表追加 32 项集合通信/硬件术语
- 保留原文所有外链；配图落地本地化
```

- [ ] **Step 3: Commit**

```bash
git add mkdocs.yml docs/resources/CHANGELOG.md
git commit -m "chore(nav): register collective-operations translation in「训练系统与集群」section

- Add new top-level nav section between 智能体工程 and 深度学习
- Update CHANGELOG with new entry"
```

---

### Task 12: 构建校验

- [ ] **Step 1: 构建并修复到零警告**

```bash
cd /Users/barryjzhao/Sources/AI/mypopydev-web && mkdocs build --strict 2>&1 | tail -30
```

预期结果：`Built site to site/` 且无任何 WARNING 输出。

常出问题：
- 图片路径拼写/大小写 → 对照 `ls docs/assets/images/articles/collective-operations/` 逐张检查
- 断链 → 确认所有 `[text](url)` 的括号配对
- Markdown 语法 → 确认 admonition 格式（`!!! tip\n    content` 需缩进）

- [ ] **Step 2: 修复后重跑直到通过**

---

### Task 13: 最终提交

- [ ] **Step 1: 提交译文**

```bash
git add docs/articles/collective-operations-zh.md
git commit -m "feat(translation): 新增《TPU 与 GPU 集群内部：集合通信剖析》中文译文

- Aleksa Gordić 原文翻译，涵盖 TPU/GPU 拓扑、四大集合操作、环/树算法、SHARP 与分层通信
- 34 张配图落地本地化；公式用 KaTeX 渲染；💡 调用注释转 Material admonition
- 术语表追加 32 项硬件/分布式术语
- 导航接入「训练系统与集群」新栏目"
```

- [ ] **Step 2: 推送确认**

推送不自动执行。提交后告知哈希，待确认后再：

```bash
git push origin main
```

---

## 自审

1. **Spec coverage:** 翻译正文（Tasks 3-10）覆盖原文全部 7 节 + 尾声/致谢/参考文献。图片下载（Task 1）。术语（Task 2）。导航（Task 11）。构建（Task 12）。提交（Task 13）。
2. **Placeholder scan:** 各 Task 含确切文件路径、命令、术语对照、配图文件列表，无 TBD。
3. **一致性:** 术语与 spec §六 完全一致。配图路径使用相对路径 `../assets/images/articles/collective-operations/`，与现有 deep-learning 译文相同。Nav 插入位置精确到行号。
