# /// script
# requires-python = ">=3.11"
# dependencies = ["beautifulsoup4"]
# ///
"""把 original/html/chapter-N.html 轉成 source/en/chapter-NN.md。

- 一般內文（段落、強調、引言、清單、分隔線）交給 pandoc 轉成 GFM。
- 裝置畫面（div.device-view）、章首地點日期（div.dateline）、SVG 等
  結構化區塊原樣保留為 HTML，翻譯時直接改裡面的文字即可。
- 導覽列、深色模式按鈕、script 會移除，重建網站時再由模板補回。

用法：uv run tools/html2md.py
"""

import re
import subprocess
from pathlib import Path

from bs4 import BeautifulSoup, NavigableString, Tag

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "original" / "html"
DST = ROOT / "source" / "en"

DROP = {"script", "style", "nav", "button"}


def is_raw_block(el: Tag) -> bool:
    if el.name in {"svg", "table", "center", "input"}:
        return True
    if el.name == "div":
        return True
    return False


def pandoc(html: str) -> str:
    out = subprocess.run(
        ["pandoc", "-f", "html", "-t", "gfm-raw_html", "--wrap=none"],
        input=html,
        capture_output=True,
        text=True,
        check=True,
    ).stdout
    return out.strip()


def convert(path: Path) -> str:
    soup = BeautifulSoup(path.read_text(encoding="utf-8"), "html.parser")
    body = soup.body
    for el in body.find_all(DROP):
        if el.name == "button" and "dark-toggle" not in (el.get("class") or []):
            continue  # 裝置畫面裡的按鈕要保留
        if el.name == "nav" and "chapter-nav" not in (el.get("class") or []):
            continue
        el.decompose()

    # 內容可能包在 div.document-page 之類的外層
    container = body
    while True:
        kids = [c for c in container.children if isinstance(c, Tag)]
        if len(kids) == 1 and kids[0].name == "div" and not kids[0].get("class", [""])[0].startswith(("device-view", "dateline")):
            container = kids[0]
        else:
            break

    blocks: list[str] = []
    prose: list[str] = []

    def flush():
        if prose:
            md = pandoc("".join(prose))
            if md:
                blocks.append(md)
            prose.clear()

    for node in container.children:
        if isinstance(node, NavigableString):
            if node.strip():
                prose.append(str(node))
            continue
        if node.name == "br":
            continue
        if is_raw_block(node):
            flush()
            blocks.append(str(node).strip())
        else:
            prose.append(str(node))
    flush()

    text = "\n\n".join(blocks) + "\n"
    return re.sub(r"\n{3,}", "\n\n", text)


def main():
    DST.mkdir(parents=True, exist_ok=True)
    files = sorted(SRC.glob("chapter-*.html"), key=lambda p: int(re.search(r"\d+", p.stem).group()))
    for f in files:
        n = int(re.search(r"\d+", f.stem).group())
        out = DST / f"chapter-{n:02d}.md"
        out.write_text(convert(f), encoding="utf-8")
        print(f"{f.name} -> {out.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
