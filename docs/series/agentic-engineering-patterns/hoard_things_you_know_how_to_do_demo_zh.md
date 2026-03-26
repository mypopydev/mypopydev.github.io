# 把你会做的事囤起来

原文标题：Hoard things you know how to do
原文链接：https://simonwillison.net/guides/agentic-engineering-patterns/hoard-things-you-know-how-to-do/
原文作者：Simon Willison
访问日期：2026-03-25
原文发布日期：2026-02-26
原文最后修改：2026-03-16
译文版本：v0.1

## 译文说明

本文为 Simon Willison《Agentic Engineering Patterns》系列 1.3 篇《Hoard things you know how to do》的示范中文版。本文沿用本项目既定术语约定，将 Agentic Engineering 统一译为“智能体工程（Agentic Engineering）”，将 Coding Agent 统一译为“编码智能体”。标题中的 hoard 处理为“囤起来”，强调主动积累、持续留存和可复用性；文中的 Prompt、代码、命令、URL、路径、产品名默认保留英文原文。

## 正文

> 所属主题：核心原则
> 上一篇：[现在，写代码很便宜](./writing_code_is_cheap_now_demo_zh.md)
> 下一篇：[AI 应该帮助我们产出更好的代码](./ai_should_help_us_produce_better_code_demo_zh.md)

我那些关于如何高效使用编码智能体的建议，很多其实都是把我在没有它们的年代就觉得很有用的职业经验，顺着往前延伸了一步。这里就有一个很典型的例子：把你会做的事囤起来。

软件开发这门手艺里，很重要的一部分，是知道什么做得到、什么做不到，并且至少对这些事该怎么做，有一个大致判断。

这些问题有些很宽泛，有些则相当冷门。网页能不能只靠 JavaScript 就完成 OCR？一个 iPhone 应用在没有运行的时候，能不能和蓝牙设备完成配对？我们能不能在 Python 里处理一个 100GB 的 JSON 文件，而不先把整个文件全部载入内存？

你肚子里装着的这类问题答案越多，就越容易发现用技术解决问题的机会，而且常常能想到别人还没想到的做法。

要想真正对这些问题的答案有把握，最好的办法，是亲眼见过它们被“运行中的代码”证明出来。理论上可行，和你亲手见过它真的跑起来，不是一回事。作为软件从业者，你应该刻意培养的一项关键资产，就是一整套这类问题的答案，以及能证明这些答案的材料。

我会用很多不同方式来囤这种解决方案。我的[博客](https://simonwillison.net)和 [TIL 博客](https://til.simonwillison.net)里，塞满了我摸索出做法后的笔记。我在 GitHub 上有[一千多个仓库](https://github.com/simonw)，收集了我为不同项目写过的代码，其中很多都是展示某个关键想法的小型概念验证。

最近，我还开始借助 LLM 来扩充自己这套“有趣问题代码解法收藏”。

[tools.simonwillison.net](https://tools.simonwillison.net) 是我最大的 LLM 辅助工具和原型集合。我用它来收集我称之为 [HTML tools](https://simonwillison.net/2025/Dec/10/html-tools/) 的东西——也就是那些嵌入 JavaScript 和 CSS、专门解决某个具体问题的单页 HTML 工具。

我的 [simonw/research](https://github.com/simonw/research) 仓库里，则放着更大、更复杂的例子：我会让一个编码智能体去研究某个问题，然后让它带回可运行的代码，以及一份详细说明它查到了什么的书面报告。

## 重组你囤下来的东西

为什么要收集这么多东西？除了它们能帮助你建立和扩展自己的能力之外，你在这个过程中沉淀出来的这些资产，本身也会成为编码智能体极其强大的输入材料。

我最喜欢的一种 Prompt 模式，就是让智能体通过组合两个或更多已经能工作的现成例子，去做出一个新的东西。

有一个项目让我特别清楚地意识到，这种做法到底有多有效。那是我放进自己工具集合里的第一个项目：一个基于浏览器的 [OCR 工具](https://tools.simonwillison.net/ocr)。我还在[另一篇文章里](https://simonwillison.net/2024/Mar/30/ocr-pdfs-images/)更详细地写过它。

我当时想要的是一个简单、基于浏览器的工具，用来对 PDF 文件中的页面做 OCR——尤其是那种完全由扫描图像组成、根本没有文本层的 PDF。

我之前已经试过在浏览器里运行 [Tesseract.js OCR library](https://tesseract.projectnaptha.com/)，而且发现它相当能打。这个库提供了成熟的 Tesseract OCR 引擎的一个 WebAssembly 构建版本，让你可以从 JavaScript 调用它，从图像里提取文本。

但我不想处理图像，我想处理 PDF。然后我想起，自己以前也用过 Mozilla 的 [PDF.js](https://mozilla.github.io/pdf.js/)：这个库的功能之一，就是把 PDF 的单独页面渲染成图像。

而这两个库对应的 JavaScript 代码片段，我的笔记里刚好都有。

下面是我当时喂给模型的完整 Prompt（那时我用的是 Claude 3 Opus）。我把自己已有的两个示例拼在一起，再补上我想要的最终效果：

````text
This code shows how to open a PDF and turn it into an image per page:
```html
<!DOCTYPE html>
<html>
<head>
  <title>PDF to Images</title>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/pdf.js/2.9.359/pdf.min.js"></script>
  <style>
    .image-container img {
      margin-bottom: 10px;
    }
    .image-container p {
      margin: 0;
      font-size: 14px;
      color: #888;
    }
  </style>
</head>
<body>
  <input type="file" id="fileInput" accept=".pdf" />
  <div class="image-container"></div>

  <script>
  const desiredWidth = 800;
    const fileInput = document.getElementById('fileInput');
    const imageContainer = document.querySelector('.image-container');

    fileInput.addEventListener('change', handleFileUpload);

    pdfjsLib.GlobalWorkerOptions.workerSrc = 'https://cdnjs.cloudflare.com/ajax/libs/pdf.js/2.9.359/pdf.worker.min.js';

    async function handleFileUpload(event) {
      const file = event.target.files[0];
      const imageIterator = convertPDFToImages(file);

      for await (const { imageURL, size } of imageIterator) {
        const imgElement = document.createElement('img');
        imgElement.src = imageURL;
        imageContainer.appendChild(imgElement);

        const sizeElement = document.createElement('p');
        sizeElement.textContent = `Size: ${formatSize(size)}`;
        imageContainer.appendChild(sizeElement);
      }
    }

    async function* convertPDFToImages(file) {
      try {
        const pdf = await pdfjsLib.getDocument(URL.createObjectURL(file)).promise;
        const numPages = pdf.numPages;

        for (let i = 1; i <= numPages; i++) {
          const page = await pdf.getPage(i);
          const viewport = page.getViewport({ scale: 1 });
          const canvas = document.createElement('canvas');
          const context = canvas.getContext('2d');
          canvas.width = desiredWidth;
          canvas.height = (desiredWidth / viewport.width) * viewport.height;
          const renderContext = {
            canvasContext: context,
            viewport: page.getViewport({ scale: desiredWidth / viewport.width }),
          };
          await page.render(renderContext).promise;
          const imageURL = canvas.toDataURL('image/jpeg', 0.8);
          const size = calculateSize(imageURL);
          yield { imageURL, size };
        }
      } catch (error) {
        console.error('Error:', error);
      }
    }

    function calculateSize(imageURL) {
      const base64Length = imageURL.length - 'data:image/jpeg;base64,'.length;
      const sizeInBytes = Math.ceil(base64Length * 0.75);
      return sizeInBytes;
    }

    function formatSize(size) {
      const sizeInKB = (size / 1024).toFixed(2);
      return `${sizeInKB} KB`;
    }
  </script>
</body>
</html>
```
This code shows how to OCR an image:
```javascript
async function ocrMissingAltText() {
    // Load Tesseract
    var s = document.createElement("script");
    s.src = "https://unpkg.com/tesseract.js@v2.1.0/dist/tesseract.min.js";
    document.head.appendChild(s);

    s.onload = async () => {
      const images = document.getElementsByTagName("img");
      const worker = Tesseract.createWorker();
      await worker.load();
      await worker.loadLanguage("eng");
      await worker.initialize("eng");
      ocrButton.innerText = "Running OCR...";

      // Iterate through all the images in the output div
      for (const img of images) {
        const altTextarea = img.parentNode.querySelector(".textarea-alt");
        // Check if the alt textarea is empty
        if (altTextarea.value === "") {
          const imageUrl = img.src;
          var {
            data: { text },
          } = await worker.recognize(imageUrl);
          altTextarea.value = text; // Set the OCR result to the alt textarea
          progressBar.value += 1;
        }
      }

      await worker.terminate();
      ocrButton.innerText = "OCR complete";
    };
  }
```
Use these examples to put together a single HTML page with embedded HTML and CSS and JavaScript that provides a big square which users can drag and drop a PDF file onto and when they do that the PDF has every page converted to a JPEG and shown below on the page, then OCR is run with tesseract and the results are shown in textarea blocks below each image.
````

结果完美得离谱。模型直接吐出了一张概念验证页面，而且正是我想要的那个东西。

后来我又和它[继续迭代了几轮](https://gist.github.com/simonw/6a9f077bf8db616e44893a24ae1d36eb)，才得到最终版本。但整个过程只花了几分钟，我就做出了一个真正有用的工具，而且直到现在我都还在持续受益。

## 编码智能体会把这件事放得更大

我做那个 OCR 示例是在 2024 年 3 月，那几乎比 Claude Code 第一次发布还早了一整年。编码智能体让“囤积可运行示例”这件事变得更有价值了。

如果你的编码智能体能上网，你可以直接让它做这种事：

```text
Use curl to fetch the source of `https://tools.simonwillison.net/ocr` and `https://tools.simonwillison.net/gemini-bbox` and build a new tool that lets you select a page from a PDF and pass it to Gemini to return bounding boxes for illustrations on that page.
```

我之所以特地点名 `curl`，是因为 Claude Code 默认会用一个 WebFetch 工具，而那个工具会总结页面内容，而不是把原始 HTML 直接返回出来。

编码智能体非常擅长搜索。这意味着，你完全可以在自己的机器上运行它们，并明确告诉它们该去哪里找你想让它们模仿的那些例子：

```text
Add mocked HTTP tests to the `~/dev/ecosystem/datasette-oauth` project inspired by how `~/dev/ecosystem/llm-mistral` is doing it.
```

很多时候，这样就够了——智能体会自动拉起一个搜索子智能体去调查，再把完成任务真正需要的细节带回来。

由于我很多研究代码本来就是公开的，所以我也经常让编码智能体把我的仓库克隆到 `/tmp`，再把那些仓库当成输入来用：

```text
Clone `simonw/research` from GitHub to `/tmp` and find examples of compiling Rust to WebAssembly, then use that to build a demo HTML page for this project.
```

这里的关键想法是：有了编码智能体，我们只需要把一个有用的技巧搞明白一次。如果这个技巧随后在某个地方被记录下来，并且附带了一个可运行的代码示例，那么我们的智能体以后就能查阅这个示例，并把它拿来解决任何形状相近的未来项目。
