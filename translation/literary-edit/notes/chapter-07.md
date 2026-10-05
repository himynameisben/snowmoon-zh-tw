# 第 7 章 文學編輯紀錄

狀態：**已完成**（v2）。4 個 chunk 全部經 reviewer PASS，裝置畫面已轉圖，待決事項已由使用者裁定（見文末）。

## v2：正式設定（2026-10-05，已套用，未 commit）

- 設定：Opus editor（附底稿、可補畫面）→ `validate --report` → Opus reviewer（附用詞差異表）；4 個 chunk 平行，
  同一 chunk 串行。底稿為當時 commit 的 `zh-tw/chapter-07.md`（＝ v1）。bible 摘錄：`chapter-07.bible.md`。
- chunk（`literary_edit.py plan 7`）：

  | chunk | 範圍 | 字數 |
  |---|---|---|
  | 01 | p3–53（3 個段群：庭院、上山與晶片廠、後台舉杯） | 1232 |
  | 02 | p55–96（2 個段群：開賽、對角線陷阱） | 1404 |
  | 03 | p98–121（3 個段群：翻盤、十二比六） | 1222 |
  | 04 | p123–144（2 個段群：穆的「隱藏思考」、深紫色的信） | 717 |

- 結果：段數 144（v1）→ 160（v2），全部變動在段群內，錨點不動。與 v1 字元相似度：
  p88–96（0.83，對角線陷阱）、p98–111（0.83，觸發式工廠翻盤）、p55–86（0.86）、p113–117（0.86）、p123–141（0.86）；
  對話為主的 p8–21（0.91）改動最小。
- reviewer 結果：chunk 01、04 一次 PASS；chunk 02、03 各一個 MINOR ISSUE，修正後複查 PASS。
- 已接受的 reviewer issue：
  - chunk 02，p58 "in the aggregate he could make out more excitement than he saw in both of his previous two games"：
    editor 拿掉了做判斷的人，補上的人聲又夾在「看不清」和「整體看下來」之間，像是判斷的依據 →
    「大多數人他幾乎看不清楚，但整體看下來，他看得出這次的興奮比前兩場都要高。整片觀眾席嗡嗡地響著人聲。」
  - chunk 03，p116 "without attempting to be particularly clever"：editor「沒打算耍什麼聰明」拿掉 particularly →
    「沒打算特別耍什麼聰明」。
- 補回初譯漏掉的強調：p108 "A few hundred turns after *that*"，v1 沒有強調，v2「*又*過了幾百回合」（reviewer 判意思一致）。
  全章強調數量現在與原文相同（6 處：*你*、*和*、*第一個*、*第二個*、*又*、*真實*）。
  為此修改 `tools/literary_edit.py` 的 `validate`：強調數量和初譯**或英文原文**一致都算通過（原本只比初譯，會把補回強調判成 ERROR）。
- 補畫面（共 2 處，reviewer 皆判符合規則）：
  - p44「腳步聲在隧道裡迴響」
  - p58「整片觀眾席嗡嗡地響著人聲」（見上方 chunk 02 issue，已移到判斷句之後）
  - （p9「嗶了一聲」、p55／p68 響亮的自動語音、p121 歡聲雷動是原文，不算補畫面。）
- editor flag 處理：
  - p89 "targeted so that one would pass right after the other, to strike both of Bai's home bases"：初譯「分別打擊」多下了
    一條對角線打一座基地的判斷；v2 拿掉「分別」，reviewer 同意。
  - p94 "unless his AI decided to ignore Zei's instruction"：白在本章一律用 she／her，his 只能是澤，v2 明寫「澤自己的 AI」，reviewer 同意。
  - p33 high vantage point →「居高臨下」，位置資訊提到看見煙霧之前，「地面忽然微微一震」獨立一段，reviewer 同意。
  - p123 穆「站在等候室裡」、p139「穆站了起來」：原文前後不一（待決 1，使用者裁定照原文）。
- 照原文、不修正（沿用譯者筆記與 QA）：p109「那四種」（前文沒交代四種）；p113 穆「凝重的搖頭」（p98 沒寫她搖頭）；
  p123–p124 不補說話者。
- 避免用語：全章「彷彿、沉默地、灑落、說不上來、手機、飛船、滑翔翼、大本營」0 次。
- 接縫通讀：p6/p8（評分畫面）、p21/p23（日期分隔）、p53/p55、p86/p88、p96/p98、p111/p113、p117/p119（戰況圖）、
  p121/p123、p141/p143（信封卡片）的主詞、時間、術語銜接無問題，沒有接縫修改。全章「載印記太空船」「干預回合」
  「思考紀錄／紀錄」「主基地／基地」「岩塊」「印記」一致。

## 裝置畫面轉圖

- 5 個裝置畫面：`zh-tw/devices/ch07-01.html`～`ch07-05.html`，圖片 `assets/devices/ch07/ch07-01.png`～`ch07-05.png`。
  01 餐廳機器人的評分滑桿（哲戈語提問、按鈕「選定」）、02–05 決賽戰況圖（SVG，無文字）。
- 文字與原文一致，未修改。逐張數過戰況圖的印記，和正文相符：03 澤 17、白 22（p98）；04 澤 14、白 11（p114）；
  05 澤 12、白 6（p119），05 澤西南基地的印記已全部消失（p117）。
- p142 的信封卡片是 `<center>` 區塊，不是 device-view，照原樣保留 HTML。
- 未改 `EXTRA_CSS`，舊章節圖片不受影響。

## 機械檢查

- `check.py chapter 7`：PASS（段數 144/160，錨點對齊，字詞比 1.38）。

## 使用者裁定（2026-10-05）

1. ~~p123／p139~~：使用者選 (a) 照原文（2026-10-05）。原題：原文先寫穆「standing in the waiting room」，後面又寫「Mu stood up」，中間沒交代她坐下。選項：(a) 照原文；
   (b) 改 p139 為「穆轉身」之類，避開矛盾（等於替原文修正）。主 Agent 建議 (a)：原文問題，譯本不修正。
