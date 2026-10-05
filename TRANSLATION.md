# 翻譯製作流程

這份文件說明《雪月》繁中譯本是怎麼做出來的。原作以 GPL v3 釋出，作者要求衍生作品
公開製作流程（AI prompt、腳本、客製化工具等非通用素材），讓其他人能在此基礎上繼續創作，
所以整套流程都留在這個 repo 裡。想看小說請回 [README](README.md)。

## 概況

譯本分兩輪：

| 輪次 | 版本 | 內容 | 狀態 |
|---|---|---|---|
| 第一輪 | v1 初譯 | AI 翻譯 → 英中逐段 QA → 全書一致性；段落與原文一對一 | 2026-10-01 全書完成，凍結在 `zh-tw-v1/`（tag `zh-tw-v1`） |
| 第二輪 | v2 閱讀版 | 逐章 AI 文學編輯（editor／reviewer 交叉把關），同時人工校稿 | 逐章進行中，進度見 `translation/literary-edit/progress.md` 與 README |

- 工具：[Claude Code](https://claude.com/claude-code)，由主 session 擔任總指揮，派 Claude Opus subagent 執行各角色。
- 第一輪結果：32 章全部通過機械驗收，沒有退件；雙語 QA 修正 14 處；一致性階段修改譯文 11 處、bible 51 條。
- `zh-tw/` 永遠是讀者看到的版本：完成 v2 的章節是 v2，其餘仍是 v1。

## 目錄結構

```
original/            原站下載的 HTML，保持原樣不修改
  index.html         首頁（目錄、授權與 AI 使用聲明）
  html/chapter-N.html
source/en/           由 original/ 轉出的英文原文 Markdown，作為翻譯底稿
  chapter-01.md … chapter-32.md
zh-tw/               台灣繁體中文譯文，永遠是每章目前最好的版本（與 source/en/ 依錨點對齊）
zh-tw/devices/       裝置畫面的 HTML 原稿（已轉圖的章節；目前第 1–6 章），章節檔裡以圖片呈現
zh-tw-v1/            v1：初譯定稿快照（commit 060e9ee、tag zh-tw-v1），凍結不修改，供對照
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
  literary-edit/     第二輪（v2）文學編輯流程、subagent prompt、正反例、每章紀錄與進度
  log.md             總指揮的執行紀錄
.claude/
  agents/            各階段 subagent 的完整 prompt
  skills/snowmoon-translate/SKILL.md
                     第一輪總指揮的流程 prompt
  skills/snowmoon-literary-edit/SKILL.md
                     第二輪逐章文學編輯（含裝置畫面轉圖）的流程 prompt
assets/
  cover.webp         封面圖（AI 生成，PNG 原稿轉 WebP q90）
  devices/           裝置畫面圖片（render_devices.py 產生，勿手改）
tools/
  html2md.py         original/ → source/en/ 的轉檔腳本
  check.py           譯文結構檢查、進度、英中對照、術語掃描
  literary_edit.py   第二輪文學編輯：切 chunk、產生資料包、驗證 editor 輸出（含用詞差異表）、套用
  render_devices.py  裝置畫面 HTML → 圖片（用原站 CSS 與系統 Chrome 渲染），讓 Markdown viewer 也看得到原站樣式
```

## 翻譯流程

### 第一輪：初譯（v1，已完成）

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
無簡體字、無佔位標記），每章通過後 commit 一次。第一輪已結束，`/snowmoon-translate` 不再使用。

原文本身的筆誤：作者原意可以確定的照意思譯並在譯者筆記說明，不能確定的照原文譯並在筆記存疑。

### 第二輪：文學編輯＋人工校稿（v2，逐章進行）

v1 讀得懂，但句子骨架、資訊順序與分段都照著英文走。第二輪的原則是「內容忠實 100%，句法與分段忠實 0%」：
段落改以錨點對齊（標題、HTML 區塊、分隔線、引言、清單不動），錨點之間可以拆段、合段、重寫。

在 Claude Code 裡打 `/snowmoon-literary-edit N`（不帶 N 就接著做下一章「待處理」的章節）開始一章。
每一章的步驟（完整規格見 `translation/literary-edit/WORKFLOW.md`）：

1. 主 Agent 建立本章 bible 摘錄，用 `tools/literary_edit.py` 切 chunk、產生資料包。
2. Literary Editor（Opus）重寫，可補少量感官畫面；不同 chunk 平行。
3. `literary_edit.py validate --report` 驗證結構並產生用詞差異表。
4. Faithfulness Reviewer（Opus）對照英文逐項審查，只回 PASS 或 ISSUE；有實質修正就再審到 PASS。
5. 主 Agent 套用、做 chunk 接縫通讀、跑 `check.py chapter N`，再用 `render_devices.py N` 把本章裝置畫面轉成圖片並逐張檢查，
   把 editor flag 與待決事項整理給使用者。
6. **人工校稿**：使用者裁定待決事項並通讀全章，直接修改 `zh-tw/`；改完跑 `check.py chapter N`。
7. 更新 `translation/literary-edit/progress.md` 與 README 的進度表。

文學編輯完成（全部 PASS、待決事項已裁定）的章節，在 README 標為 v2；人工校稿可以在之後持續進行，
另欄記錄。第二輪不回寫第一輪的 notes／qa 紀錄，改記在 `translation/literary-edit/notes/`。

## 封面

`assets/cover.webp` 由 AI 生成，原圖 1024×1536 PNG，以 `cwebp -q 90 -m 6` 轉成 WebP。
2026-10-02 換成第二版（左側冰雪中的白色塔樓城市，右側工業廢墟）；下面是第一版的 prompt，第二版的 prompt 待補。

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
uv run tools/render_devices.py 1      # 第 1 章裝置畫面 HTML 原稿 → 圖片
```

已知限制：

- `check.py terms` 以字面比對，會固定出現幾筆誤報（如動詞 watch、句首 Glad、數字 Zero），可以忽略。
- 英文詞數會把 SVG 標記算進去（第 4 章尤其明顯），用來估算工作量時會偏高。

## 原文 Markdown 格式

`source/en/*.md` 由 `tools/html2md.py` 產生，規則如下：

- 一般內文（段落、強調、引言、清單、分隔線）轉為 GitHub Flavored Markdown。
- 下列結構化區塊**原樣保留為 HTML**，翻譯時只改標籤內的文字，不要動標籤與屬性：
  - `<div class="dateline …">`：章節開頭或場景切換的地點與日期
  - `<div class="device-view …">`：書中裝置畫面（表格、按鈕、選單等）。已轉圖的章節（目前第 1–6 章）
    在譯文裡是 `<img>`，HTML 原稿放在 `zh-tw/devices/`
  - `<svg>`：圖表，其中 `<text>` 的內容需要翻譯
- 原站的導覽列、深色模式按鈕與 script 已移除，之後重建網站時由模板補回。

重新產生原文：

```sh
uv run tools/html2md.py
```

需要 [uv](https://docs.astral.sh/uv/) 與 [pandoc](https://pandoc.org/)。
