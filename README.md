# Barry's Tech Notes

个人技术笔记站——AI 工程、深度学习与技术翻译。

🔗 **在线阅读**：[mypopydev.github.io](https://mypopydev.github.io/)

## 当前内容

**智能体工程** — Simon Willison《Agentic Engineering Patterns》系列 15 篇中文译文，涵盖核心原则、协作工作流、测试实践、代码理解与实战案例。

**深度学习** — 反向传播的核心直觉、数学推导、计算图与思想史梳理。

## 本地预览

```bash
pip install -r requirements-docs.txt
mkdocs serve
```

打开 http://127.0.0.1:8000 预览。

## 技术栈

- [MkDocs Material](https://squidfunk.github.io/mkdocs-material/) — 静态站生成
- [KaTeX](https://katex.org/) — 数学公式渲染
- [GitHub Actions](https://github.com/features/actions) — 自动构建与部署到 GitHub Pages

## 部署故障排查：Pages 卡在 `syncing_files`

`deploy-pages` 工作流的 `build` 全绿、但 `deploy` 在约 10 分钟后失败，日志末尾出现：

```text
Current status: syncing_files
##[error]Timeout reached, aborting!
Canceling Pages deployment...
```

这不是构建问题：`build` 里的 `mkdocs build --strict` 已通过，失败发生在 GitHub Pages 把 artifact 同步到 CDN 的阶段。站点会停在上一版，新页面返回 404。

**根因**：`actions/deploy-pages@v4`（v5 同样）在 `src/internal/deployment.js` 里把等待上限硬编码为 `MAX_TIMEOUT = 600000`（10 分钟），`timeout` 输入超过该值会被钳制并告警。一旦 Pages 侧同步超过 10 分钟，action 会主动取消 deployment 并把状态写成 `failure`；`gh run rerun <run-id> --failed` 只会再开一次同样卡住的 deployment，因此会复现失败。

### 恢复步骤

1. **确认症状**（构建绿、部署卡住）：

   ```bash
   gh run view <run-id> --json status,conclusion,jobs
   gh run view <run-id> --log | grep -E "Current status|Reported success|Timeout reached"
   ```

   出现 `syncing_files` / 空状态且没有 `Reported success!` 即可确认。deployment 状态也可查：
   `gh api repos/mypopydev/mypopydev.github.io/deployments/<deployment-id>/statuses`。

2. **不要用 `--failed` 重跑**，改用 `workflow_dispatch` 起一次全新 run（`github-pages` 环境的 branch policy 只允许 `main`）：

   ```bash
   gh workflow run deploy-pages.yml --ref main
   ```

3. **等待并确认成功**：

   ```bash
   gh run watch <new-run-id> --exit-status
   ```

   成功时日志应有 `Reported success!`，deployment 状态为 `success`。

4. **验证站点已更新**（替换为实际文章 slug）：

   ```bash
   curl -sL -o /dev/null -w "%{http_code}\n" \
     https://mypopydev.github.io/articles/<article-slug>/
   ```

   返回 `200` 即发布完成；若仍是 `404`，说明部署未完成。

5. **仍然卡住时**：查看 https://www.githubstatus.com 的 Pages / Actions 组件，或过一会儿再重试一次全新 dispatch；长期可压缩 `site/` 中的大文件（大尺寸 PNG、PDF、`search_index.json`）以缩短同步时间。

### 注意事项

- 工作流设了 `concurrency: group: pages, cancel-in-progress: true`：push 到 main 会自动起一个 run，随后会被 `workflow_dispatch` 的新 run 取消，这是预期行为，不用处理。
- 不要试图给 `deploy-pages` 传更大的 `timeout`：v4/v5 都会钳到 600000 ms，只是多一条 warning。
- 2026-11-07 曾连续两次 10 分钟超时，用第 2 步的一次全新 `workflow_dispatch` 即恢复（28 秒完成部署）。

> 完整的工作流定义见 `.github/workflows/deploy-pages.yml`。
