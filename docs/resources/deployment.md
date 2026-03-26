# GitHub Pages 发布与本地预览说明

这套站点骨架默认采用 `GitHub Pages + MkDocs Material + GitHub Actions`。仓库里已经准备好了 `mkdocs.yml`、`requirements-docs.txt` 和 `.github/workflows/deploy-pages.yml`，所以后续真正上线时，主要只剩 GitHub 仓库设置和本地预览两个动作。

## 本地预览

如果你想先在本机看效果，推荐在仓库根目录执行下面这组命令：

```bash
python3 -m venv .venv-docs
source .venv-docs/bin/activate
pip install -r requirements-docs.txt
mkdocs serve
```

默认会启动一个本地站点，通常地址是 `http://127.0.0.1:8000`。如果只是想检查能否成功构建，也可以执行：

```bash
mkdocs build --strict
```

## GitHub Pages 设置

把仓库推到 GitHub 之后，进入仓库的 `Settings -> Pages`，在发布来源里选择 `GitHub Actions`。这一步很关键，因为当前项目不是用分支里的静态文件直接发布，而是通过工作流构建后再部署。

当前工作流的触发条件是：推送到 `main` 分支，或者手动触发。也就是说，正常情况下你只要把改动 push 到 `main`，GitHub 就会自动安装依赖、构建 MkDocs 站点，并把 `site/` 目录发布到 Pages。

## 目录与内容维护建议

当前专题内容已经放在 `docs/series/agentic-engineering-patterns/`，后续不相关的新文章优先放在 `docs/articles/`。站点级说明和辅助文档放在 `docs/resources/`。共享图片放在 `docs/assets/images/`。只要继续遵守这个分层，后面站点越长越大也不容易乱。

## 常见检查点

如果页面打不开，先检查 Pages 是否已启用并绑定到 `GitHub Actions`。如果构建失败，优先看 Actions 日志里是不是依赖安装失败、导航里引用了不存在的文件，或者正文里写了错误的相对链接。图片和内部链接尽量继续使用相对路径，不要随手写站点根绝对路径。
