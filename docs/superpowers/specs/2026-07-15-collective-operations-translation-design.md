# 翻译设计：Aleksa Gordić《Inside TPU and GPU Clusters: The Anatomy of Collective Communication》

**Date:** 2026-07-15 ｜ **Status:** approved ｜ **Type:** translation

## 一、目标与范围

将 Aleksa Gordić 2026-07-14 发表的博文《Inside TPU and GPU Clusters: The Anatomy of Collective Communication》翻译为中文，纳入本站 MkDocs Material 站点，作为「训练系统与集群」新栏目的开篇译文。

**完整范围**：引言、7 大节、尾声（Epilogue）、致谢（Acknowledgements）、参考文献（References）全部翻译。文末 subscribe CTA 译为一句话说明（原文无明确链接，不强加）。

**质量要求**：术语稳定、技术准确、中文自然、`mkdocs build --strict` 零警告。

## 二、原文基线

| 项目 | 内容 |
|---|---|
| 原文标题 | Inside TPU and GPU Clusters: The Anatomy of Collective Communication |
| 作者 | Aleksa Gordić |
| 原文 URL | https://www.aleksagordic.com/blog/collective-operations |
| 发布日期 | 2026-07-14 |
| 规模 | 7 大节 + 引言/尾声/致谢/参考文献；约 34 张配图；约 8,000 英文词 |
| 技术域 | TPU/GPU 集群拓扑、环面 ICI、胖树 NVSwitch、All-Gather/Reduce-Scatter/All-Reduce/All-to-All 环算法与树算法、SHARP 网内归约、分层集合通信 |
| 配图 | 34 张（png/jpg），均托管于 `https://www.aleksagordic.com/blog/collective-operations/`，可本地化下载 |

**小节结构：**
1. TPU cluster topology（超节点/切片/DCN/PCIe/ICI/带宽层级）
2. All-Gather（1D/2D 环与链）
3. Reduce-Scatter & All-Reduce（All-Gather 的对偶）
4. All-to-All（分片转置）
5. NVIDIA GPU cluster topology（节点/可扩展单元/胖树）
6. GPU Collectives Within the Node（环/树/SHARP）
7. GPU Collectives Across Nodes（基于 InfiniBand 的分层算法）
8. Epilogue + Acknowledgements + References（6 篇）

## 三、译文标题

**TPU 与 GPU 集群内部：集合通信剖析（Inside TPU and GPU Clusters: The Anatomy of Collective Communication）**

## 四、文件布局

```
docs/articles/collective-operations-zh.md                   ← 译文正文（新建）
docs/assets/images/articles/collective-operations/*.png|jpg ← 34 张配图（脚本下载，新建目录）
mkdocs.yml                                                  ← 新增「训练系统与集群」栏目 + 条目（修改）
docs/resources/agentic_engineering_translation_glossary_style_guide_template.md ← 追加本文术语（修改）
docs/resources/CHANGELOG.md                                  ← 追加条目（修改）
```

**不修改**：`index.md`（首页）—— 原文与首页已有内容无直接对应，暂不追加入口。

## 五、格式约定

### 5.1 头部
沿用本站译文既定格式：H1 直入正文，后接原文信息 blockquote + 译文说明：

```md
# TPU 与 GPU 集群内部：集合通信剖析（Inside TPU and GPU Clusters: The Anatomy of Collective Communication）

> 原文：[Inside TPU and GPU Clusters: The Anatomy of Collective Communication](https://www.aleksagordic.com/blog/collective-operations)  
> 作者：Aleksa Gordić · 发布时间：2026-07-14

译文版本：v0.1

## 译文说明

本文为 Aleksa Gordić 博文《Inside TPU and GPU Clusters: The Anatomy of Collective Communication》的中文翻译版。原文深度剖析 TPU 与 GPU 集群中的集合通信操作（All-Gather、Reduce-Scatter、All-Reduce、All-to-All），涵盖硬件拓扑、环/树算法、SHARP 网内归约以及分层通信策略。术语遵循项目统一术语表，链接保留原文地址。
```

### 5.2 数学公式
全部使用 KaTeX 渲染（`$...$` 行内 / `$$...$$` 独立），与 `transformer-math-101` 等现有译文一致。

原文 `code span` 风格公式（如 `T_total ≈ D / BW_node`）统一改为 KaTeX 格式：

| 原文表达 | 译文 KaTeX |
|---|---|
| `T_total ≈ D / BW_node = D / 400e9` | `$T_{\text{total}} \approx D / \text{BW}_{\text{node}} = D / 4 \times 10^{11}$` |
| `T_total ≈ max( D/ BW_gpu, D/ BW_node )` | `$T_{\text{total}} \approx \max(D / \text{BW}_{\text{gpu}}, D / \text{BW}_{\text{node}})$` |
| `log₂(N)` | `$\log_2(N)$` |
| `N - 1` | `$N - 1$` |
| `45 GB/s × 1 μs = 45 KB` | `$45\,\text{GB/s} \times 1\,\mu\text{s} = 45\,\text{KB}$` |

矩阵维度保持 `code span`（如 `` `(2048, 2048)` ``、`` `(128 * 1024, 128 * 1024)` ``），不倒装为公式渲染——它们不是数学表达式而是尺寸标记。

### 5.3 调用注释（💡…）
原文使用 `> 💡标题：` GitHub 风格 blockquote。译文**转换为 Material admonition**（`!!! tip "标题"`），利用站点已启用的 admonition + emoji 扩展，获得更好的视觉效果：

```markdown
!!! tip "Boardfly 拓扑"
    Google 的新推理 TPU 芯片 `8i` 并未采用 2D/3D 环面，而是……
```

### 5.4 链接
全部保留原始 URL（§6.4）。锚文本中文化，链接目标不改为不存在的中文页面。参考文献同。

### 5.5 参考文献
文末 `## 参考文献`，6 篇顺序与原一致，描述性文字中文化，URL 保留：

```markdown
## 参考文献

1. "TPU 8t and TPU 8i 技术深度解析"，https://cloud.google.com/blog/products/compute/tpu-8t-and-tpu-8i-technical-deep-dive
2. "TPU 拓扑可视化工具"，https://tpu-visualizer.uc.r.appspot.com/
...
```

正文中的 `[1]`..`[6]` 标记保留为字面引用。

### 5.6 图注
每张图使用 `![中文图注](...)` 并指向本地路径，如 `![TPU 连接类型。](../assets/images/articles/collective-operations/tpu_classes.png)`。确保图序与原文一致（需执行时建映射表）。

## 六、关键术语表（执行时写入项目术语表「可追加术语表」）

| 英文 | 推荐译法 | 保留英文 | 使用说明 |
|---|---|---|---|
| collective operation | 集合通信（collective operation） | 首现括注 | 本文核心词 |
| All-Gather | 全收集（All-Gather） | 首现括注 | 四大集合操作之一 |
| Reduce-Scatter | 归约散布（Reduce-Scatter） | 首现括注 | |
| All-Reduce | 全归约（All-Reduce） | 首现括注 | |
| All-to-All | 全互换（All-to-All） | 首现括注 | |
| ring | 环（ring） | 一般不保留 | ring algorithm → 环形算法 |
| tree | 树（tree） | 一般不保留 | tree algorithm → 树形算法 |
| torus | 环面（torus） | 首现括注 | 2D/3D torus → 二维/三维环面 |
| mesh | 网格（mesh） | 首现括注 | |
| wraparound | 环绕（wraparound） | 一般不保留 | 环面回绕特性 |
| superpod | 超级 Pod（superpod） | 首现括注 | 也作"超节点"，取 Google 原生术语 |
| slice | 切片（slice） | 一般不保留 | TPU slice |
| pod | Pod | 保留 | 谷歌产品术语 |
| ICI | ICI（芯片间互联） | 保留 | inter-chip interconnect |
| DCN | DCN（数据中心网络） | 保留 | |
| PCIe | PCIe | 保留 | |
| NVLink | NVLink | 保留 | |
| NVSwitch | NVSwitch | 保留 | |
| SHARP | SHARP | 保留 | 网内归约计算单元 |
| fat tree | 胖树（fat tree） | 首现括注 | |
| Scalable Unit (SU) | 可扩展单元（Scalable Unit，SU） | 保留缩写 | |
| bisection bandwidth | 二分带宽（bisection bandwidth） | 首现括注 | |
| oversubscription | 超额订阅（oversubscription） | 首现括注 | |
| leaf switch / spine switch | 叶子交换机 / 脊交换机 | 一般不保留 | |
| hierarchical collectives | 分层集合通信（hierarchical collectives） | 首现括注 | |
| recursive doubling / halving | 递归倍增 / 递归折半 | 一般不保留 | |
| in-network reduction | 网内归约（in-network reduction） | 首现括注 | SHARP 核心概念 |
| nearest-neighbor | 近邻（nearest-neighbor） | 一般不保留 | |
| bandwidth hierarchy | 带宽层级 | 一般不保留 | |
| throughput-bound / latency-bound | 吞吐受限 / 延迟受限 | 一般不保留 | |
| injection bandwidth | 注入带宽 | 一般不保留 | |
| scale-up / scale-out | 纵向扩展（scale-up）/ 横向扩展（scale-out） | 首现括注 | |
| data / tensor / model / expert parallelism | 数据/张量/模型/专家并行 | 一般不保留 | |
| FSDP / MoE / NCCL | 保留原文 | 保留 | MoE 首现括注"混合专家" |

## 七、图片下载策略

34 个文件列表（从 HTML `<img>` 提取）：

```
tpu_classes.png  torus.jpg  topo_3d.png  tpu_topology1.png  tpu_topology2.png
pyramid.png  tpu_example1.png  tpu_example2.png  gather_motivation.png
ring.png  representation.png  all_gather1.png  all_gather2.png  all_gather3.png
all_gather4.png  reduce_scatter_motivation.png  rs1.png  all_reduce.png  rs2.png
rs3.png  ata1.png  ata2.png  ata3.png  totaltime.png  gpu_topology.png
gpu_ring.png  sharp.png  gpu_ata.png  ag_tree.png  rs_tree.png
ag_hierarchy.png  ar_hierarchy.png  ar_shard_hierarchy.png  ata_hierarchy.png
totaltime_gpu.png
```

下载命令（执行时使用，单行循环）：

```bash
BASE="https://www.aleksagordic.com/blog/collective-operations"
DEST="docs/assets/images/articles/collective-operations"
mkdir -p "$DEST"
for f in $(cat /tmp/collective-files.txt); do
  curl -sL "$BASE/$f" -o "$DEST/$f" && echo "✓ $f"
done
```

**图序映射**：执行时需将 HTML 中 image 顺序与 WebFetch 提取的 35 个 Figure 标题一一对应，确保翻译时图注不串位。

## 八、风险与边界

| 风险 | 缓解 |
|---|---|
| 图序错位 | 执行时建映射表，逐一对应 Fig1→file1, Fig2→file2... |
| 公式渲染 `--strict` 报错 | 译后用 `mkdocs build --strict` 验证，逐条修复 |
| 尾声语气翻译过度书面化 | 保留口语化调性。作者原话 "Phew, that was a long one!" 等需用自然中文传达 |
| BILINGUAL_LINK_MAP 仅 Simon 项目 | 不动原有内容。在文件末尾新增独立映射段（非 Simon 项目），或仅在 CHANGELOG 登记而不写入 LINK_MAP |

## 九、实现路径决策

已与用户确认：
- **配图**：下载到本地（`docs/assets/images/articles/collective-operations/`）
- **导航**：新建「训练系统与集群」顶层栏目
- **结构**：单文件译文（`docs/articles/collective-operations-zh.md`），与本站全部现有译文一致
- **范围**：全量翻译（含尾声、致谢、参考文献）
