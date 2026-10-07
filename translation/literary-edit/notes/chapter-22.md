# 第 22 章 文學編輯紀錄

狀態：**已完成**（v2，2026-10-07）。4 個 chunk 經 reviewer PASS（chunk 02 一項 MINOR 修正後複查 PASS；chunk 03 主 Agent 小修一句，複查 PASS），沒有補畫面，沒有待決事項，裝置畫面已轉圖。
使用者事先授權（2026-10-06：「處理接下來的五個章節，每個章節處理完就 commit」）：沒有需要確認的地方就直接標已完成並 commit。

## v2：正式設定（2026-10-07）

- 設定：Opus editor（附底稿、可補畫面）→ `validate --report` → Opus reviewer（附用詞差異表）；4 個 chunk 平行，
  同一 chunk 串行。底稿為當時 commit 的 `zh-tw/chapter-22.md`（＝ v1）。bible 摘錄：`chapter-22.bible.md`。
- chunk（`literary_edit.py plan 22`）：

  | chunk | 範圍 | 字數 | 結果 |
  |---|---|---|---|
  | 01 | p3–6、p7（引言）、p8、p9（引言）、p10–11、p13–30（計程車：街景、避難所廣告、車資、和司機聊國防稅與卡特爾） | 1191 | PASS |
  | 02 | p32–66（研究所餐廳：烏塔庫、聯合城邦歷史、自由城與亞圖利亞的篩選、基因與自由） | 1888 | ISSUE 1 → 修正 → PASS |
  | 03 | p68–81、p83–88、p90–92、p94–97、p99–108、p110–126（澤的即時殺傷鏈展示） | 1202 | PASS（p104 主 Agent 小修，複查 PASS） |
  | 04 | p128–146（收尾、隱寫術、綁架無人機、再介紹一家國防企業） | 567 | PASS |

- 結果：段數 146（v1）→ 152（v2），全部變動在段群內，錨點不動（p7、p9 引言的 `>` 結構不變）。與 v1 字元相似度：p3–30（0.76）、p32–66（0.87）；
  p68–146 因裝置畫面換成 `<img>` 無法直接比（正文改寫幅度與 chunk 01–02 相近）。
  拆段：p4（垃圾／公園與工業建築／找投影機／心想）、p10（往西／修路）、p68（點餐查資料／做表）、p80（下載／檔案行為）。

## 重要裁決

- p48 "keeping that spirit together through the easy times, the boring times, the times when the founding generation dies out…"：editor 把第三項寫成「撐到……的時候」，
  reviewer 列 MINOR（through 是撐過整段時期，不是撐到某個時間點），改「也撐過……的那段時期」，複查 PASS。
- p60 "I think there might be a core"：初譯漏 might，編輯稿補「可能」。
- p63 "of course I know why they would never tell either of us"：初譯漏 why，編輯稿改「我當然明白他們為什麼絕對不會告訴我們兩個」；bible 摘錄同步更正（原寫「三個問句」，實為四個）。
- p104 "trying any kind of trick to avoid getting killed"：編輯稿「什麼花招都可以試，只要不被殺掉」，reviewer 判可接受但接近門檻（讀成「前提是不被殺」）；
  主 Agent 改為「用盡各種花招，就是不要被殺掉」，複查 PASS。
- p138 "One of ..."：楊恩接 p136 澤的 one of our other big projects，editor 改「大計畫之一……」，比初譯「其中之一……」好懂；reviewer 同意。
- p143：初譯「再介紹我認識另一家」的「再」原文沒有，one more time 只在 p141，editor 把「再」留在 p141；reviewer 同意。
- p68 點的是茶、p70 拿的是 glass of water：原文本身如此，照原文。

## reviewer issue

- chunk 02 ISSUE 1（MINOR，誤譯）：p48，見上。

## 補畫面

無。

## editor flags

- chunk 01：NONE。
- chunk 02：p60 補 might；p63 補 why。
- chunk 03：茶／水杯原文不一致，照原文；p80 拆段。
- chunk 04：p138「大計畫之一……」；p143 刪「再」。

## 接縫通讀

接縫（p6→廣告→p8→廣告→p10、p11→車資表→p13、p30→分隔→p32、p66→分隔→p68、p81→畫面→p83 … p126→畫面→p128）銜接自然，無修改。

## 裝置畫面

- 7 張：`ch22-01.png`（計程車車資表）、`ch22-02.png`～`ch22-07.png`（澤傳來的紅郡戰場示意圖，SVG）。
- 轉圖前對文字：車資表「道路壅塞費」×3 與正文「壅塞費」一致，數字（3.69、9 分鐘、5.65 公里、113 m/s Δv、12.52 等）照原文；SVG 只有擊中標記「x」，不譯（正文「紅色的 X」對應）。
- 檢查：沒有斷字、截斷、溢出。SVG 畫面靠左是原稿的 `margin-left:35px`，照原站排版。本章沒有改 CSS 或 render 工具。
- 已轉圖章節更新為「第 1–20、22、30、31 章」（第 21 章沒有裝置畫面，改寫成列舉）：CLAUDE.md、AGENTS.md、TRANSLATION.md（兩處）。

## 待決事項

無。

## check

`uv run tools/check.py chapter 22`：PASS（無 WARN），段數 146/152，錨點對齊，字詞比 1.55。
