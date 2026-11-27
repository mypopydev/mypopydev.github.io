"""Check that articles in the MkDocs navigation are linked from 专题阅读."""

import posixpath
import sys
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit

import markdown
from mkdocs.config import load_config


def is_article(path):
    return isinstance(path, str) and path.startswith("articles/") and path.endswith(".md")


def nav_articles(entries):
    """Yield (title, path) in nav order, including nested groups."""
    for entry in entries:
        if isinstance(entry, dict):
            for title, child in entry.items():
                if isinstance(child, list):
                    yield from nav_articles(child)
                elif is_article(child):
                    yield title, child
        elif is_article(entry):
            yield entry, entry


class TopicLinks(HTMLParser):
    def __init__(self):
        super().__init__()
        self.in_topics = False
        self.heading = None
        self.links = set()

    def handle_starttag(self, tag, attrs):
        if tag in ("h1", "h2"):
            self.heading = []
            self.in_topics = False
        elif tag == "a" and self.in_topics:
            href = dict(attrs).get("href")
            if href:
                url = urlsplit(href)
                if not url.scheme and not url.netloc and not url.path.startswith("/"):
                    self.links.add(posixpath.normpath(unquote(url.path)))

    def handle_data(self, data):
        if self.heading is not None:
            self.heading.append(data)

    def handle_endtag(self, tag):
        if tag in ("h1", "h2") and self.heading is not None:
            self.in_topics = tag == "h2" and "".join(self.heading).strip() == "专题阅读"
            self.heading = None


def find_missing_articles(nav, homepage):
    parser = TopicLinks()
    parser.feed(markdown.markdown(homepage, extensions=["fenced_code"]))
    parser.close()
    return [(title, path) for title, path in nav_articles(nav) if path not in parser.links]


def main():
    root = Path(__file__).resolve().parents[1]
    config = load_config(config_file=str(root / "mkdocs.yml"))
    homepage = Path(config.docs_dir, "index.md").read_text(encoding="utf-8")
    missing = find_missing_articles(config.nav, homepage)
    if missing:
        print("docs/index.md 的「专题阅读」缺少以下导航文章链接：", file=sys.stderr)
        for title, path in missing:
            print(f"  - {title}: ./{path}", file=sys.stderr)
        return 1

    print("首页「专题阅读」包含导航中的全部文章链接。")
    return 0


if __name__ == "__main__":
    sys.exit(main())
