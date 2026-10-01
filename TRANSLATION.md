# 翻譯製作流程

這份文件說明《雪月》繁中譯本是怎麼做出來的。原作以 GPL v3 釋出，作者要求衍生作品
公開製作流程（AI prompt、腳本、客製化工具等非通用素材），讓其他人能在此基礎上繼續創作，
所以整套流程都留在這個 repo 裡。想看小說請回 [README](README.md)。

## 概況

- 翻譯完成：2026-10-01，全書 32 章。
- 工具：[Claude Code](https://claude.com/claude-code)，由主 session 擔任總指揮，依序派 Claude Opus subagent 執行各階段。
- 結果：32 章全部通過機械驗收，沒有退件；雙語 QA 修正 14 處；一致性階段修改譯文 11 處、bible 51 條。
- 尚未經過人工通讀校稿。
- 2026-10-01 新增第二輪文學編輯流程；正文尚未開始套用，進度見
  `translation/literary-edit/progress.md`。

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
  literary-edit/     第二輪文學編輯流程、subagent prompt、正反例與進度
  log.md             總指揮的執行紀錄
.claude/
  agents/            各階段 subagent 的完整 prompt
  skills/snowmoon-translate/SKILL.md
                     總指揮的流程 prompt
assets/
  cover.webp         封面圖（AI 生成，PNG 原稿轉 WebP q90）
tools/
  html2md.py         original/ → source/en/ 的轉檔腳本
  check.py           譯文結構檢查、進度、英中對照、術語掃描
```

## 翻譯流程

總指揮（`/snowmoon-translate`）同一時間只派一個 agent 工作；agent 的上下文還夠用
（約 150k tokens 以內）時接續處理下一章，超過 300k 就換新的 agent。

| 階段 | 內容 | agent |
|---|---|---|
| 0 | 通讀全書，建立術語、人物、世界觀、每章摘要；列出需要人工拍板的譯法 | `snowmoon-bible-builder` |
| — | 使用者決策：逐題決定 `open-questions.md` 裡的譯法 | 人工 |
| 1 | 文學翻譯：英文 → 台灣繁中，忠實與自然一次完成 | `snowmoon-translator` |
| 2 | 雙語 QA：英中逐段檢查，只找翻譯錯誤 | `snowmoon-qa` |
| 3 | 全書一致性：術語、人物語氣與稱謂、世界觀，各一個 agent | `snowmoon-consistency` |

總指揮不審閱譯文，只用 `tools/check.py` 做機械驗收（段數對齊、HTML 標籤未被改動、
無簡體字、無佔位標記），每章通過後 commit 一次。

上述限制只適用於已完成的初譯流程。第二輪文學編輯需要主 Agent 實際閱讀原文、初譯、editor 候選稿與
reviewer issues，再做最終整合；完整規格見 `translation/literary-edit/WORKFLOW.md`。這一輪不取代或回寫
既有的第一至第三階段紀錄。

原文本身的筆誤：作者原意可以確定的照意思譯並在譯者筆記說明，不能確定的照原文譯並在筆記存疑。

## 封面

`assets/cover.webp` 由 AI 生成，原圖 1024×1536 PNG，以 `cwebp -q 90 -m 6` 轉成 WebP。

基礎 prompt：

```
Book cover illustration, split composition divided by a diagonal line of falling snow, left side: a calm green futuristic city with orderly towers under a cold winter moon, a man in his thirties in a dark coat seen from behind; right side: a dense neon-lit electronics market street with hanging signs and antennas, a teenage boy with his arm in a sling looking up at the sky; both figures facing away from each other, the same pale moon above both halves, subtle glowing geometric patterns like encryption in the snowflakes, cinematic lighting, muted teal and warm orange contrast, semi-realistic digital painting, space at top for title, vertical 2:3
```

negative prompt：

```
text, letters, watermark, logo, blurry, deformed hands, extra fingers, oversaturated, cartoonish, gore, explosions, cluttered composition
```

生成時追加的要求：

- 畫面中加上標題「雪月」「Snowmoon」，小字「繁中社群版」；下方放上作者「Vitalik Buterin」。
- 用色要冷一些，這是一部未來戰爭烏托邦風格的小說。
- 不要出現以太坊（ETH）logo。

## 檢查工具

```sh
uv run tools/check.py status          # 進度
uv run tools/check.py chapter 3       # 檢查第 3 章譯文結構
uv run tools/check.py pair 3          # 第 3 章英中逐段對照
uv run tools/check.py terms           # 術語一致性掃描
```

已知限制：

- `check.py terms` 以字面比對，會固定出現幾筆誤報（如動詞 watch、句首 Glad、數字 Zero），可以忽略。
- 英文詞數會把 SVG 標記算進去（第 4 章尤其明顯），用來估算工作量時會偏高。

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
