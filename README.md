# Snowmoon 台灣繁體中文社群翻譯

這是 Vitalik Buterin 的小說《Snowmoon》的台灣繁體中文社群翻譯專案。

- 原作：<https://vitalik.eth.limo/snowmoon/>
- 原作者：Vitalik Buterin
- 原作授權：[GPL v3](https://www.gnu.org/licenses/gpl-3.0.html)

本翻譯為非官方的社群譯本，與原作者無關。

## 授權

原作以 GPL v3 釋出，本翻譯屬衍生作品，同樣以 **GPL v3** 釋出，全文見 [LICENSE](LICENSE)。

原作者在授權說明中特別要求：以本作品為基礎產出衍生作品時，須一併公開製作流程
（AI prompt、腳本、客製化工具等非通用素材），讓其他人能在此基礎上繼續創作。
因此本專案使用到的轉檔腳本、翻譯 prompt 與術語表都會放在這個 repo 裡。

## 目錄結構

```
original/            原站下載的 HTML，保持原樣不修改
  index.html         首頁（目錄、授權與 AI 使用聲明）
  html/chapter-N.html
source/en/           由 original/ 轉出的英文原文 Markdown，作為翻譯底稿
  chapter-01.md … chapter-32.md
tools/
  html2md.py         original/ → source/en/ 的轉檔腳本
```

## 原文 Markdown 格式

`source/en/*.md` 由 `tools/html2md.py` 產生，規則如下：

- 一般內文（段落、強調、引言、清單、分隔線）轉為 GitHub Flavored Markdown。
- 下列結構化區塊**原樣保留為 HTML**，翻譯時只改標籤內的文字，不要動標籤與屬性：
  - `<div class="dateline …">`：章節開頭或場景切換的地點與日期
  - `<div class="device-view …">`：書中裝置畫面（表格、按鈕、選單等）
  - `<svg>`：圖表，其中 `<text>` 的內容需要翻譯
- 原站的導覽列、深色模式按鈕與 script 已移除，之後重建網站時由模板補回。

重新產生原文：

```sh
uv run tools/html2md.py
```

需要 [uv](https://docs.astral.sh/uv/) 與 [pandoc](https://pandoc.org/)。
