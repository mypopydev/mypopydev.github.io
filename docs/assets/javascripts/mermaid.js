// Mermaid 图表初始化：与 katex.js 同一模式，绑定在 Material 的 document$ 上，
// 这样首屏与站内跳转（instant loading）后都能把 .mermaid 容器绘制成 SVG。
(function () {
  function render() {
    if (!window.mermaid) {
      // 脚本缺失时不要静默留下源代码块，提示读者改用原文
      console.warn("[mermaid] mermaid runtime not loaded; diagrams left as source text");
      return;
    }
    window.mermaid.initialize({
      startOnLoad: false,
      theme: "neutral",
      fontFamily: "ui-monospace, SFMono-Regular, Menlo, Consolas, monospace",
      flowchart: { useMaxWidth: true },
    });
    // 只处理尚未渲染的容器；单张图出错不应连累其余图表
    window.mermaid
      .run({ querySelector: ".mermaid", suppressErrors: true })
      .catch(function (err) {
        console.error("[mermaid]", err);
      });
  }

  if (typeof document$ !== "undefined") {
    document$.subscribe(render);
  } else if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", render);
  } else {
    render();
  }
})();
