// Mermaid 图表初始化：与 katex.js 同一模式，在 DOMContentLoaded 前完成配置，
// 由 superfences 的 fence_div_format 渲染出的 .mermaid 容器交给 mermaid 绘制。
if (window.mermaid) {
  window.mermaid.initialize({
    startOnLoad: true,
    theme: "neutral",
    fontFamily: "ui-monospace, SFMono-Regular, Menlo, Consolas, monospace",
    flowchart: { useMaxWidth: true },
  });
}
