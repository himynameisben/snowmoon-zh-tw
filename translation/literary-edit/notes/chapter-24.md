# 第 24 章 文學編輯紀錄

狀態：**已完成**（v2，2026-10-07）。4 個 chunk 經 reviewer PASS（chunk 04 一項 MINOR，照 reviewer 建議補回初譯原字），沒有補畫面，沒有待決事項，本章沒有裝置畫面。
使用者事先授權（2026-10-06：「處理接下來的五個章節，每個章節處理完就 commit」）：沒有需要確認的地方就直接標已完成並 commit。

## v2：正式設定（2026-10-07）

- 設定：Opus editor（附底稿、可補畫面）→ `validate --report` → Opus reviewer（附用詞差異表）；4 個 chunk 平行，
  同一 chunk 串行。底稿為當時 commit 的 `zh-tw/chapter-24.md`（＝ v1）。bible 摘錄：`chapter-24.bible.md`。
- chunk（`literary_edit.py plan 24`）：

  | chunk | 範圍 | 字數 | 結果 |
  |---|---|---|---|
  | 01 | p3–18（徹夜未眠、打給茲文） | 393 | PASS |
  | 02 | p20–29（走向圖書館：地底第八天、產業搬進金字塔） | 535 | PASS |
  | 03 | p31–63（圖書館：白、有條件的愛、白的童年、好奇心） | 1264 | PASS |
  | 04 | p65–96（鄧的房間：「監視我們」、三點理由、保全攝影機） | 1063 | ISSUE 1 → 修正 → PASS |

- 結果：段數 96（v1）→ 99（v2），全部變動在段群內，錨點不動（p30 哲戈語標語原樣）。與 v1 字元相似度：p3–18（0.87）、p65–96（0.87）；
  p20–63 含哲戈語標語 HTML，整段比是 0.94，正文改寫幅度與前後相近。
  拆段：p3（看錶／一夜沒睡）、p21（第八天／遷來地下）、p26（清淨機／「至少……他想」）。

## 重要裁決

- p79 "But I want to hear yours."：editor 寫「不過，我想聽聽你的。」，reviewer 列 MINOR（拿掉「理由」會讀成「照你的意思辦」）；照 reviewer 建議補回初譯的「理由」（退回原字，不另送複查）。
- p7 "thinking as much about redeeming himself in Seila's eyes as about his daughter's safety"：editor 寫「為了女兒的安危，也同樣是為了在賽菈眼中挽回自己」，reviewer 確認兩者分量相等的自嘲沒有被淡化。
- p21–p23 時間線：原文 p21「完全住在地底下的第八天」、剛到哲戈「不久」就遷來，p22 卻說「兩個多月來」每天在金字塔半山腰散步，p23 今天才提不起勁出門——原文本身前後不太吻合。
  editor flag、reviewer 同意：照字面保留，不替作者圓（原文問題，不影響譯文，不列待決事項）。
- p47 "If you think it does"：原文 it does 指涉不清，editor 照 bible 保留「要是你真這麼想」的推論鏈，不另作解讀；reviewer 同意。
- p61 "I'm not going to say I'm fully unopinionated"：編輯稿「完全沒有立場」，比初譯「全都一樣好」貼近 unopinionated。
- p92–p96 說話者原文未標，照初譯不點名（p92 可能是格拉迪亞斯或澤）。

## reviewer issue

- chunk 04 ISSUE 1（MINOR，誤譯）：p79，見上。

## 補畫面

無。

## editor flags

- chunk 01、04：NONE。
- chunk 02：p21–p22 時間線，見上。
- chunk 03：p47 "If you think it does"，見上。

## 接縫通讀

接縫（p18→分隔→p20、p29→標語→p31、p63→分隔→p65）銜接自然，無修改。

## 裝置畫面

本章沒有 device-view 裝置畫面（p30 的哲戈語標語是 dz-card，原樣保留，不轉圖）。

## 待決事項

無。

## check

`uv run tools/check.py chapter 24`：PASS，段數 96/99，錨點對齊，字詞比 1.42。WARN 一項：p30（錨點）英文字母偏多——哲戈語標語的羅馬拼音，屬正常（譯者筆記已記）。
