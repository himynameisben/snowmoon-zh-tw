# Snowmoon 台灣繁體中文社群翻譯

這是 Vitalik Buterin 的小說《Snowmoon》的台灣繁體中文社群翻譯專案。

- 原作：<https://vitalik.eth.limo/snowmoon/>
- 原作者：Vitalik Buterin
- 原作授權：[GPL v3](https://www.gnu.org/licenses/gpl-3.0.html)

本翻譯為非官方的社群譯本，與原作者無關。

## 目前狀態

全書 32 章已於 2026-10-01 完成三個階段：文學翻譯、雙語 QA（修正 14 處）、全書一致性（terms／voice／world）。
尚未經過人工通讀校稿，歡迎回報問題。

- 執行紀錄：`translation/log.md`；各章譯者筆記與 QA 紀錄見 `translation/notes/`、`translation/qa/`。
- 原文本身的筆誤：作者原意可以確定的照意思譯並在筆記說明，不能確定的照原文譯並在筆記存疑。
- 已知限制：`check.py terms` 以英文字面比對，會固定出現幾筆誤報（如動詞 watch、句首 Glad、數字 Zero），可以忽略。

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
zh-tw/               台灣繁體中文譯文（段落與 source/en/ 一對一）
translation/         翻譯基準文件與過程紀錄
  style-guide.md     翻譯風格指南（含正反例）
  glossary.md        術語表
  characters.md      人物、說話風格、稱謂
  worldbuilding.md   地名、曆法、制度、科技設定
  synopsis.md        每章摘要（第零階段產出）
  open-questions.md  需要人工拍板的譯法決策
  notes/             第一階段譯者筆記（每章一份）
  qa/                第二階段 QA 紀錄（每章一份）
  consistency/       第三階段全書一致性報告
  log.md             總指揮的執行紀錄
.claude/
  agents/            各階段 subagent 的完整 prompt
  skills/snowmoon-translate/SKILL.md
                     總指揮的流程 prompt
tools/
  html2md.py         original/ → source/en/ 的轉檔腳本
  check.py           譯文結構檢查、進度、英中對照、術語掃描
```

## 翻譯流程

使用 [Claude Code](https://claude.com/claude-code)，由主 session 擔任總指揮
（`/snowmoon-translate`），依序派 Claude Opus subagent 執行各階段。
同一時間只有一個 agent 在工作；agent 的上下文還夠用（約 150k tokens 以內）時接續處理下一章，
超過 300k 就換新的 agent。

| 階段 | 內容 | agent |
|---|---|---|
| 0 | 通讀全書，建立術語、人物、世界觀、每章摘要；列出需要人工拍板的譯法 | `snowmoon-bible-builder` |
| 1 | 文學翻譯：英文 → 台灣繁中，忠實與自然一次完成 | `snowmoon-translator` |
| 2 | 雙語 QA：英中逐段檢查，只找翻譯錯誤 | `snowmoon-qa` |
| 3 | 全書一致性：術語、人物語氣與稱謂、世界觀 | `snowmoon-consistency` |

總指揮不審閱譯文，只用 `tools/check.py` 做機械驗收（段數對齊、HTML 標籤未被改動、
無簡體字、無佔位標記），每章通過後 commit 一次。

```sh
uv run tools/check.py status          # 進度
uv run tools/check.py chapter 3       # 檢查第 3 章譯文結構
uv run tools/check.py pair 3          # 第 3 章英中逐段對照
uv run tools/check.py terms           # 術語一致性掃描
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
