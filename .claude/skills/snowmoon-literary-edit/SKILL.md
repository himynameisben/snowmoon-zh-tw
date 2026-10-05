---
name: snowmoon-literary-edit
description: Snowmoon 第二輪（v2）逐章文學編輯的總指揮：照 translation/literary-edit/WORKFLOW.md 的正式設定，派 Opus Literary Editor → Opus Faithfulness Reviewer 改寫一章，套用、接縫通讀、機械驗收，再把該章的裝置畫面（device-view HTML）轉成圖片，最後整理改寫最大段落、補畫面與待決事項交給使用者校稿。使用時機：要做下一章或指定章節的 v2 文學編輯、literary edit、小說化。參數：章節號 N；不帶參數則從 progress.md 第一個「待處理」的章節開始。
---

# Snowmoon 第二輪文學編輯

規則都寫在 repo 裡，這份 skill 只負責「照什麼順序讀、做到哪裡停」。規則衝突時以 `AGENTS.md` 與
`translation/literary-edit/WORKFLOW.md` 為準；這裡沒寫到的細節一律回去查 WORKFLOW。

不要用 `/snowmoon-translate`（第一輪已結束），也不要讓 subagent 直接寫正文。

## 0. 決定章節

- 參數給 N 就做第 N 章；沒給就讀 `translation/literary-edit/progress.md`，取第一個「文學編輯＝待處理」的章節。
- 若該章不是「待處理」（已完成或編輯中），先問使用者要重做、接續還是換一章，不要直接覆蓋。
- 一次只做一章，除非使用者明確要求多章。

## 1. 開工前要讀的

依序讀完再動手：

1. `AGENTS.md`
2. `translation/literary-edit/WORKFLOW.md`（流程本體）
3. `translation/literary-edit/literary-editor.md`、`faithfulness-reviewer.md`、`examples.md`
4. 上一章的 `notes/chapter-(N-1).md` 與 `chapter-(N-1).bible.md`，當作格式與裁決的範例
5. `notes/chapter-NN.md` 若已存在且有「交接」段落，照交接做（交接優先於本 skill 的預設）

## 2. 文學編輯（照 WORKFLOW）

照 WORKFLOW「開始一章前」→「順序與裁決」→「全章收尾」第 1–6 步做。重點：

- 先看 `git status --short`，保留使用者未提交的修改；底稿是目前 commit 的 `zh-tw/chapter-NN.md`。
  `zh-tw-v1/`、`original/`、`source/en/` 不可動。
- 跑一次 `uv run tools/check.py chapter N` 確認基準可通過。
- 建立 `translation/literary-edit/notes/chapter-NN.bible.md`（含全章固定用詞，寫初譯實際字面）。
- `uv run tools/literary_edit.py plan N` 切 chunk；每個 chunk 用 `packet --bible` 產資料包，放 session 暫存區，不進 repo。
- 派工：Agent 工具，`subagent_type: general-purpose`、`model: opus`。同一 chunk 先 editor、後 reviewer；
  不同 chunk 可以平行（一則訊息送出多個 editor）。
- editor 輸出 → `literary_edit.py validate N 輸出檔 --bible … --report 差異表.md`，ERROR 先處理，
  差異表連同 editor 輸出交給 reviewer。
- ISSUE 的修正寫成副本（`chunk-KK.final.md`），有實質修訂就再送 reviewer 複查到 PASS，再 `literary_edit.py apply`。
- 全部套用後做接縫通讀，接縫有實質修改就再送 reviewer；跑 `check.py chapter N`，ERROR 歸零、WARN 逐項判斷。
- 更新 `notes/chapter-NN.md`（範圍、chunk 表、reviewer issue、補畫面位置、editor flag、待決事項、check 結果）
  與 `progress.md`（待決事項還沒裁定時標「待人工決定」）。

## 3. 裝置畫面轉圖片

文學編輯不碰 HTML 區塊；正文定稿後，才把本章的 `class="device-view"` 轉成圖片。

1. 確認本章有沒有裝置畫面：`grep -c 'class="device-view' zh-tw/chapter-NN.md`。0 個就跳過本節。
2. 轉圖前先把每個裝置畫面的文字和正文對一遍：數字、名稱、按鈕字、譯名要與正文和 bible 一致。
   不一致時先查英文原文：原文本身就不一致（例如第三章 55／61）是原文問題，列入待決事項，不自行修正；
   是譯文造成的就修裝置畫面的文字（只改文字，HTML 標籤一字不動）。
3. `uv run tools/render_devices.py N`：第一次執行會把區塊抽成 `zh-tw/devices/chNN-KK.html`，章節檔裡換成
   `<img>`（alt＝畫面全文），圖片寫到 `assets/devices/chNN/chNN-KK.png`（含 SVG `<animate>` 動畫的畫面寫成循環 GIF `chNN-KK.gif`，逐格固定截圖、重跑結果不變；發布平台只收圖片，GIF 也算圖片）。之後要改文字一律改 `zh-tw/devices/`，
   再重跑同一指令，不要直接改章節檔裡的 `<img>`。
4. 用 Read 工具逐張看 `assets/devices/chNN/`，檢查（GIF 只會看到第一格；要看動畫內容，另外抽幾格出來看）：
   - 中文是否被拆成一字一行（表頭、按鈕、窄欄）
   - 數字或代碼是否被切斷（60259、10%、MUN GUI 1842）
   - 有沒有溢出、截掉、空白圖
   有問題就改 `tools/render_devices.py` 的 `EXTRA_CSS`，不要改 HTML 原稿去遷就排版。
   改了 CSS 等於所有已轉圖章節都受影響：重跑所有已轉圖章節（`render_devices.py 1 2 … N`），
   用 `git status --short assets/devices` 看哪些舊圖變了，變了的也要看過。
5. 再跑一次 `uv run tools/check.py chapter N`（check 會改讀 `zh-tw/devices/` 的原稿比對錨點）。
6. 把「已轉圖的章節（目前第 1–X 章）」更新到包含第 N 章，四處都要改：
   `CLAUDE.md`、`AGENTS.md`、`TRANSLATION.md`（兩處）。用
   `grep -n "目前第 1–" CLAUDE.md AGENTS.md TRANSLATION.md` 找。
   若已轉圖的章節不再連續（例如跳過某章），改寫成列舉，不要寫成區間。

## 4. 交給使用者（停在這裡）

不自行 commit。回報內容（WORKFLOW「全章收尾」第 7 步）：

- 改寫幅度最大的幾個段群：v2 全文與 `zh-tw-v1/chapter-NN.md` 對應段落並列，附英文要點。
- 所有補畫面：位置、補了什麼、reviewer 判定。
- 待決事項：每項給出選項與你的建議，一項一項讓使用者裁定。
- 裝置畫面：轉了幾張、有沒有改 CSS、有沒有影響舊圖；請使用者看過 `assets/devices/chNN/`。
- `check.py chapter N` 結果（段數 v1 → v2）。

## 5. 使用者裁定之後

- 依裁定修改 `zh-tw/`（裝置畫面改 `zh-tw/devices/` 再跑 `render_devices.py N`），涉及語意的修改再送 reviewer
  複查；使用者親自指定的寫法是最終決定，不必送 reviewer。
- 動到譯名：先改 bible，再全書替換，跑 `check.py terms` 與全書 `check.py chapter`。
- 更新 notes（待決事項標上裁定與日期）、`progress.md` 標「已完成」、README 進度表該章「版本」改成 **v2**
  （格式跟前面幾章一致）。
- 跑 `check.py chapter N`，通過後等使用者說要 commit 才 commit。commit 訊息格式參考
  `git log --oneline -5`（例：「第二輪文學編輯：第三章 v2；第三章裝置畫面轉圖片；…」）。
