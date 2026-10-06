# 第二輪文學編輯流程

## 目的

這一輪處理的是已完成的繁中初譯。目標不是重譯，也不是替作者改寫，而是在完整保留英文原文
資訊與《Snowmoon》設定的前提下，讓譯文像原本就是為台灣讀者寫的小說。

版本：v1＝初譯定稿，凍結在 `zh-tw-v1/`（tag `zh-tw-v1`），不可修改；第二輪直接改 `zh-tw/`，
完成的章節就是 v2。`zh-tw/` 永遠是讀者看到的「每章目前最好的版本」。比對可用
`diff zh-tw-v1/chapter-NN.md zh-tw/chapter-NN.md` 或 `git diff zh-tw-v1 -- zh-tw/chapter-NN.md`。

一句話原則：**內容忠實 100%，句法與分段忠實 0%；段群內可重組，錨點不可動；場景可補少量畫面。**

### 正式設定（2026-10-01 使用者決定，依第一章試跑結果）

| 項目 | 設定 | 理由 |
|---|---|---|
| Literary Editor | **Opus**，**附初譯**（改稿模式），重寫句法與分段，**開放少量補畫面** | Sonnet 改寫幅度不足；不給初譯時改寫幅度沒有明顯變大，用詞漂移卻變多 |
| Faithfulness Reviewer | **Opus**，附 `literary_edit.py` 產生的**用詞差異表** | Opus 抓增譯與弱化比 Sonnet 準；兩者都抓不到用詞漂移，交給工具 |
| 主 Agent | 準備每章 bible 摘錄（含全章固定用詞）、切 chunk、裁決、套用、接縫通讀、機械驗收 | |

Claude Code 派工時，在 Agent 工具指定 `model: opus`。試跑紀錄見 `experiments/2026-10-01-ch01-p042-067.md`。

### 對齊單位：錨點與段群

- **錨點**：標題、HTML 區塊、分隔線、`>` 引言、清單。種類、數量、順序與原文一致，HTML 標籤一字不動；
  `>` 引言內的文字可以改寫，但不拆合。
- **段群**：兩個錨點之間的所有散文段。段群內可以拆段、合段、重排句子與段落，資訊可以在段群內的段落間搬移；
  資訊不可跨出段群。
- `tools/check.py chapter N` 在段數與原文不同時自動改用錨點對齊檢查：錨點必須一一對上，
  原文有內容的段群譯文不可為空，字數比例改以段群為單位提示。

角色分工：

- Literary Editor：負責「不要像翻譯」。
- Faithfulness Reviewer：負責「不要改過頭」。
- 主 Agent：負責切段、提供上下文、裁決衝突、套用修訂、全章銜接與機械驗收。

## 開始一章前

主 Agent：

1. 看 `git status --short`，保留使用者既有修改。
2. 讀完整英文原文與完整繁中初譯，先掌握章內伏筆、語氣與技術說明的作用。
3. 讀本章 synopsis、notes、QA，以及 bible 中與本章人物、場景、技術相關的條目。
4. 執行一次 `uv run tools/check.py chapter N`，確認基準檔案原本可通過檢查。
5. 建立本章 bible 摘錄 `translation/literary-edit/notes/chapter-NN.bible.md`（範例：`chapter-01.bible.md`），
   所有 chunk 共用。內容：
   - 本章出現的固定譯名（glossary／characters／worldbuilding，含「避免」欄）與人物口吻、稱謂。
   - **全章固定用詞**：同一事物在本章初譯裡的叫法（例如「語音課程」「隔音牆」「臉罩」「一條規準」），
     以及刻意前後呼應的句子（例如兩處「系統會記分」）。editor 一次只看一個 chunk，看不到這些。
   - 譯者筆記與 QA 已定的取捨（`translation/notes/`、`translation/qa/`），例如 shut down→「被封殺」。
   - 為了讓 `validate` 也能比對，詞要寫出初譯實際用的字面。
6. 用工具切 chunk 並產生資料包：

   ```sh
   uv run tools/literary_edit.py plan N
   uv run tools/literary_edit.py packet N --chunk K --out 暫存目錄 --bible translation/literary-edit/notes/chapter-NN.bible.md
   ```

   切法：分隔線（場景切換）一律切開；其餘以約 1,500 字為上限，不切開段群。
   單位 ID 以原文段號表示：段群用 `ch01-p023~p031`（原文起訖段號），`>` 引言用 `ch01-p052`。
   HTML 區塊、分隔線、標題不送編輯，只放進資料包當上下文。資料包放在 session 暫存區，不進 repo。

## 每個 chunk 的資料包

主 Agent 給 Literary Editor：

```text
章節：chapter-NN
目標範圍：原文第 A–B 段之間的段群與引言（只有 <draft> 列出的單位可以改）

<unit_map>
chNN-pAAA~pBBB = 段群（原文第 A–B 段，散文）
chNN-pCCC = `>` 引言錨點
</unit_map>

<source>
--- chNN-pAAA~pBBB ---
英文原文第 A–B 段（段落間空行）
--- chNN-pCCC ---
英文引言
</source>

<draft>
--- chNN-pAAA~pBBB ---
目前繁中譯文的對應段群（段落間空行）
--- chNN-pCCC ---
目前繁中引言
</draft>

<fixed_in_range>
範圍內的 HTML 區塊、分隔線；只供理解，不可改
</fixed_in_range>

<context_before>
前文一至兩個完整段落；只供理解，不可改
</context_before>

<context_after>
後文一至兩個完整段落；只供理解，不可改
</context_after>

<relevant_bible>
只放這個 chunk 實際需要的固定譯名、人物口吻與設定
</relevant_bible>
```

subagent 必須先讀其角色 prompt、`examples.md` 與共通 style guide。不要把整份 glossary 每次貼進 task；
主 Agent 應選出相關條目，降低干擾。`--- chNN-pNNN ---` 是交接用定位標記，不屬於正文；editor 輸出時
必須保留相同標記，主 Agent 套用 patch 時移除標記，並以 editor 輸出的段落取代該段群的所有原段落。
Reviewer 的 ISSUE 用同一 ID 定位。

## 實際派工方式

- Codex：使用 session 提供的 subagent／multi-agent spawn 工具建立獨立 agent，將角色 prompt 路徑與資料包
  一併交付；editor 完成後才派 reviewer。
- Claude Code：使用 Agent 工具（`subagent_type: general-purpose`、`model: opus`），分別載入兩份角色 prompt，
  仍採 editor → reviewer 串行。editor 把完整輸出寫到暫存區檔案，主 Agent 驗證後把同一個檔案路徑交給 reviewer。
  不同 chunk 之間可以平行。
- 若環境沒有 subagent 能力，不可在主 Agent 同一上下文裡假裝角色隔離，也不可跳過 reviewer；在修改正文前
  停止並告知使用者需要換到支援 subagent 的 session。

## 順序與裁決

### 1. Literary Editor

派工短 prompt：

```text
請先完整閱讀 translation/literary-edit/literary-editor.md、
translation/literary-edit/examples.md 與 translation/style-guide.md，
再依提供的章節與段落範圍進行 literary edit。
只輸出角色 prompt 規定的格式，不修改 repo 檔案。
```

主 Agent 收到輸出後執行：

```sh
uv run tools/literary_edit.py validate N editor輸出檔 --bible 本chunk的bible摘錄 --report 用詞差異表.md
```

ERROR（單位標記、錨點、`*強調*`、數字、HTML）必須先處理。WARN 是用詞漂移提示（bible 譯名消失、
出現避免用語、全章重複出現的初譯用詞不見了），大多是正常改寫，但模型 reviewer 很容易漏看這一類，
所以把 `--report` 產生的用詞差異表一併交給 reviewer 逐條判斷。

### 2. Faithfulness Reviewer

Reviewer 必須看到同一份英文原文、原始初譯、editor 的完整輸出、相關前後文、bible 與用詞差異表。派工短 prompt：

```text
請先完整閱讀 translation/literary-edit/faithfulness-reviewer.md，
再逐項核對以下英文原文與編輯稿，並逐條判斷用詞差異表。只做忠實度審查，不潤飾，不修改 repo 檔案。
```

### 3. 主 Agent 整合

- Reviewer 回 `PASS`：主 Agent 仍需快速核對格式，再以最小 patch 套用。
- Reviewer 提 ISSUE：以英文原文與 bible 為準。修復問題時盡量保留 editor 已改善的自然中文。
- 任何「可能」「似乎」「應該」「只有」「仍然」「已經」等限定語被改強或改弱，都算實質問題。
- 技術直覺可以前置，但形式化資訊不可消失；所有重排限於同一段群。
- 主 Agent 不得為了「保險」把 editor 的重寫退回初譯句型；要退，只退有 ISSUE 的那一句。
- Reviewer 只是報告者，不直接改稿；最終決定由主 Agent 負責。
- 補畫面：reviewer 判「超出規則」的一律拿掉或改回原文資訊；判「符合規則」的由主 Agent 決定是否保留，
  全章合計仍以少量為原則。
- 修正寫成 editor 輸出的副本（例如 `chunk-04.final.md`），不要直接改 editor 原檔，方便日後對照。
- 定稿後套用：`uv run tools/literary_edit.py apply N 最終稿檔案`（會先重跑結構驗證）。
  apply 以目前 `zh-tw` 檔案的段群切分為準，所以同一章的 chunk 可以依任意順序逐一套用。

只要主 Agent 因 ISSUE 做了會影響語意、語氣、技術內容或句子關係的修訂，就再派 reviewer 複查該段，
直到 PASS。純標點或明確筆誤可由主 Agent 自行確認。

## 全章收尾

所有 chunk 完成後：

1. 從頭通讀繁中章節，專看 chunk 邊界：代名詞、重複主詞、時間銜接、語氣與術語是否突然改變，
   以及是否重複介紹同一個技術概念。
2. 不得以「全章更流暢」為由把資訊搬過錨點。
3. 接縫通讀若造成任何實質修改，將受影響段落連同上下文重新送 Faithfulness Reviewer，直到 PASS。
4. 執行 `uv run tools/check.py chapter N`；所有 ERROR 必須歸零，WARN 要逐項判斷。
   本章若有裝置畫面（`class="device-view"`）且尚未轉圖：先對照正文與原文檢查畫面文字（數字、名稱、譯名），
   再跑 `uv run tools/render_devices.py N` 轉成圖片，逐張看 `assets/devices/chNN/`（含 SVG 或 CSS 動畫的畫面輸出成循環 GIF，其餘是 PNG）有無斷字、數字被切、溢出
   （排版問題改 `render_devices.py` 的 CSS，改了就重跑所有已轉圖章節），然後再跑一次 `check.py chapter N`，
   並把 CLAUDE.md、AGENTS.md、TRANSLATION.md 的「已轉圖的章節（目前第 1–X 章）」更新。
5. 執行相關術語搜尋；若動過 bible，再跑 `uv run tools/check.py terms` 並檢查全書影響。
6. 更新 `translation/literary-edit/progress.md`，並在
   `translation/literary-edit/notes/chapter-NN.md` 記錄：範圍、重要裁決、已接受的 reviewer issue、
   所有補畫面的位置、尚待人工決定的問題與 check 結果。
7. 把改寫幅度最大的段落、所有補畫面與待決事項，連同和 `zh-tw-v1/` 的對照交給使用者，進入人工校稿。

一章只有在所有 chunk 與接縫修改都通過 reviewer、待決事項經使用者裁定，而且機械檢查通過後，
「文學編輯」才能標成「已完成」；此時同步把 README 進度表的「版本」改成 **v2**。

## 人工校稿

v2 ＝ AI 文學編輯＋人工校稿，兩者同時進行：

- 使用者裁定主 Agent 整理的待決事項，並通讀全章，直接修改 `zh-tw/`（裝置畫面改 `zh-tw/devices/` 再跑
  `render_devices.py N`）；改完跑 `check.py chapter N`。
- 人工修改是最終決定，不需送 reviewer；涉及譯名時仍依 CLAUDE.md 先改 bible 再全書替換。
- `progress.md` 與 README 的「人工校稿」欄：開始校稿標 `進行中`，使用者確認通讀完標 `已完成`。

## 不能由 chunk editor 自行決定的事

- 改固定譯名、角色名、地名、制度名或人物稱謂。
- 改動全書既定單位或換算方式。主 Agent 必須先 flag 並取得使用者明確同意；獲准後先更新
  style guide／worldbuilding，再確認全書用法，不能只改一章。（先例：2026-10-01 使用者同意 decimeter 改換算為公分。）
- 修正疑似原文筆誤或替原文補充解釋。
- 把資訊搬過錨點，或增刪、拆合錨點。
- 為伏筆增加提示，或用後文揭露去改寫前文的模糊性。
