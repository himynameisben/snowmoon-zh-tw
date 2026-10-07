# 第 18 章 文學編輯紀錄

狀態：**已完成**（v2，2026-10-06）。4 個 chunk 全部經 reviewer 一次 PASS，沒有補畫面，沒有待決事項，裝置畫面已轉圖。
使用者事先授權：沒有待決事項就直接標已完成並 commit。

## v2：正式設定（2026-10-06）

- 設定：Opus editor（附底稿、可補畫面）→ `validate --report` → Opus reviewer（附用詞差異表）；4 個 chunk 平行，
  同一 chunk 串行。底稿為當時 commit 的 `zh-tw/chapter-18.md`（＝ v1）。bible 摘錄：`chapter-18.bible.md`。
- chunk（`literary_edit.py plan 18`）：

  | chunk | 範圍 | 字數 | 結果 |
  |---|---|---|---|
  | 01 | p3–49、p51–53（空港、黑色專車、入住飯店） | 1273 | PASS |
  | 02 | p55–72、p74–83（帕佛蓋都街頭、山坡步道） | 1348 | PASS |
  | 03 | p85–88（飯店餐廳與澤、白會合） | 89 | PASS |
  | 04 | p90–127（汾解釋班順派與哲戈的轉變） | 1560 | PASS |

- 結果：段數 127（v1）→ 130（v2），全部變動在段群內，錨點不動。與 v1 字元相似度：p74–83（0.82）、p85–88、p90–127（0.87）、
  p55–72（0.89）；其餘 0.90 以上。拆段：p69 等；合段：p64＋p65、p99＋p100（都是同一串動作，中間沒有對話）。

## 重要裁決

- p123 "Instead, the Bansunpei just released…"：editor 維持初譯把 just 讀成「只是」（前句已有「三天前」交代時間；
  本段論點是班順派沒有強制、只發建議，與 p127「沒有由上而下的強制」一致），並用「卻」補出 Instead 與「等第九版」的對比。
  reviewer 判定站得住；讀成「剛剛」文法也通，但讀者理解不會不同。
- p18 "seemed somewhat unnatural"：初譯漏 seemed，補「看起來」，程度不變。
- p79 "much less green than Veridia"：改為「比自由城綠得多，卻還是遠遠比不上維瑞迪亞」，「綠」由前半句管到後半句。reviewer 同意。
- p82 原文 "seemed to surrounding" 為 surround 筆誤，照 seemed 譯「似乎」。
- p123「三天前」與紅郡遇襲約一個月前對不上：原文問題，譯者筆記與 QA 已定照譯。

## reviewer issue

無（4 個 chunk 都一次 PASS）。

## 補畫面

無。

## editor flags

- chunk 01：p18 補「看起來」。
- chunk 02：p82 原文筆誤；p79 改寫。
- chunk 04：p123 just／Instead；p99＋p100 合段。
- chunk 03：NONE。

## 接縫通讀

chunk 邊界（p49→裝置畫面→p51、p53→分隔→p55、p72→招牌→p74、p83→分隔→p85、p88→裝置畫面→p90）銜接自然，無修改。

## 裝置畫面

- 2 張：`ch18-01.png`（飯店入住，哲戈語）、`ch18-02.png`（古詩：英文一行已譯，與 ch11 賽菈的引句一字不差；哲戈語六行保留）。
- check 對原文第 50、73、89 段的「英文字母偏多」WARN 都是刻意保留的哲戈語，不是未譯。
- 沒有截斷、溢出；本章沒有改 CSS（第 17 章的 SVG 裁切修改不影響本章）。

## 待決事項

無。

## check

`uv run tools/check.py chapter 18`：PASS（3 個哲戈語 WARN，見上），段數 127/130，錨點對齊，字詞比 1.43。
