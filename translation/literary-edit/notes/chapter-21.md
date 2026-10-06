# 第 21 章 文學編輯紀錄

狀態：**已完成**（v2，2026-10-06）。2 個 chunk 經 reviewer PASS（chunk 01 一項 MINOR、chunk 02 一項 MAJOR＋三項 MINOR，修正後複查 PASS），沒有補畫面，沒有待決事項，本章沒有裝置畫面。
使用者事先授權（2026-10-06：「處理接下來的五個章節，每個章節處理完就 commit」）：沒有需要確認的地方就直接標已完成並 commit。

## v2：正式設定（2026-10-06）

- 設定：Opus editor（附底稿、可補畫面）→ `validate --report` → Opus reviewer（附用詞差異表）；2 個 chunk 平行，
  同一 chunk 串行。底稿為當時 commit 的 `zh-tw/chapter-21.md`（＝ v1）。bible 摘錄：`chapter-21.bible.md`。
- chunk（`literary_edit.py plan 21`）：

  | chunk | 範圍 | 字數 | 結果 |
  |---|---|---|---|
  | 01 | p3–39（晚餐：官司、莉莉的公民考、茲文的火箭、「是北極人嗎？」） | 1213 | ISSUE 1 → 修正 → PASS |
  | 02 | p41–107（地下室：電話裡痛罵格拉迪亞斯、推理與計分、哲戈的影子軍隊、不再有祕密） | 2586 | ISSUE 1–4 → 修正 → PASS |

- 結果：段數 107（v1）→ 110（v2），全部變動在段群內，錨點不動。與 v1 字元相似度：p3–39（0.83）、p41–107（0.90）。
  拆段：p43（拍額頭／半年來什麼都沒問）、p45（看穿銀聊幌子／想過北極人／拼圖湊起來）。

## 重要裁決

- p84 "push for Veridian schools to not teach people Veridian civics"：初譯「不要教維瑞迪亞的公民」會讀成教「公民」這些人。editor flag、reviewer 列 MINOR；
  主 Agent 裁定改「不教維瑞迪亞的公民課」（civics 仍譯「公民」，只加「課」），章內 bible 同步更新。
- p89 "And notice what it took"：初譯「你注意他花了什麼力氣就做到了」讀不通；editor 改「你看看他是靠什麼辦到的」，reviewer 指出原文講的是代價（有隱私保護的地方他費盡工夫只換到三分之一個小組，對比軍方、議會、媒體長驅直入），
  改為「你注意看他得費多大的工夫」，複查 PASS。
- p45 "none of Delwart's lines seemed anything like"：初譯漏 seemed，編輯稿補回「似乎」。
- p82–p88 計分與加總照原文（原文加總與逐條不完全相符，譯者筆記與 QA 已定不修正）。
- p99「十一比十」照原文（與 ch08 的 10 比 10 不同，譯者筆記已定）。

## reviewer issue

- chunk 01 ISSUE 1（MINOR，誤譯／因果）：p30 "So a few days ago he took me" 的 So 承接老師很佩服，editor 改成「然後」失去因果，改回「所以」。
- chunk 02 ISSUE 1（MAJOR，誤譯）：p95 編輯稿「我在這邊為了孩子困在……飛地裡哭」會讀成賽菈自己被困，恢復「因為孩子困在……而哭」。
- chunk 02 ISSUE 2（MINOR，誤譯）：p44 "just a kindly man" 的 just 修飾好心人，不是「只關心」；改「是說自己只是一個關心和平與自由的好心人」。
- chunk 02 ISSUE 3（MINOR，語氣）：p89，見上。
- chunk 02 ISSUE 4（MINOR，bible 用詞）：p84，見上。

## 補畫面

無。

## editor flags

- chunk 01：p26 "How was your time in school been" 原文文法有誤，照意思譯；p16 "Here," 譯「你看，」不補動作。
- chunk 02：p45 補 seemed；p84、p89 見上；原文筆誤 p62 多一個 the、p76 so suit（不影響譯文）。

## 接縫通讀

唯一的接縫 p39→分隔→p41 銜接自然，無修改。

## 裝置畫面

本章沒有裝置畫面。

## 待決事項

無。

## check

`uv run tools/check.py chapter 21`：PASS（無 WARN），段數 107/110，錨點對齊，字詞比 1.55。
