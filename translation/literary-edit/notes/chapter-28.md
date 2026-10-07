# 第 28 章 文學編輯紀錄

狀態：**已完成**（v2，2026-10-07）。3 個 chunk 都經 reviewer PASS（chunk 01 一項 MINOR 退回初譯語氣；chunk 02 兩項 MINOR 修正後複查 PASS），沒有補畫面，沒有待決事項；本章沒有裝置畫面。

## v2：正式設定（2026-10-07）

- 設定：Opus editor（附底稿、可補畫面）→ `validate --report` → Opus reviewer（附用詞差異表）；3 個 chunk 平行，
  同一 chunk 串行。底稿為當時 commit 的 `zh-tw/chapter-28.md`（＝ v1）。bible 摘錄：`chapter-28.bible.md`。
- chunk（`literary_edit.py plan 28`）：

  | chunk | 範圍 | 字數 | 結果 |
  |---|---|---|---|
  | 01 | p3–p52（雷克托來訪、昆高派亮身分、白的提議、穆的漏洞攻擊） | 1900 | ISSUE 1 → 修正（退回初譯語氣） |
  | 02 | p54–p89（茲文報告莉莉、格拉迪亞斯罵老師、澤當榜樣） | 1124 | ISSUE 2 → 修正 → 複查 PASS |
  | 03 | p91–p100（雷克托成為最高將領） | 570 | PASS |

- 結果：段數 100（v1）→ 101（v2），拆段在段群內，錨點不動。與 v1 字元相似度（只比散文）：0.90。
- reviewer 核對了 p34 北極的征服順序與限定、p35 雷克托列舉的數字、p38 白的假設句與三個多月、p42–p43 限定語、p48 漏洞攻擊邏輯、p49 刪節號、
  斜體 9 處一一對應、p65 計分論證、p70–p75 格拉迪亞斯的尖酸強度、p94 祕密會議的步驟與兩件證據的歸屬、p96 兩類參議員的理由，全部一致。

## 重要裁決

- p48 "so if the Arctics find out, that's actually *better*"：editor「就算北極發現」變成讓步語氣，reviewer MINOR；改回條件句「要是北極發現了，其實*更好*」（退回初譯語氣，不另送複查）。
- p65 "adding those points up … if you multiply"：editor「加起來」與「相乘」不成對、和 ch16 用語接不上，reviewer MINOR；改回「相加」。複查 PASS。
- p67 "almost the whole day every day"：editor「幾乎每天都從早到晚」把「幾乎」挪去修飾「每天」，reviewer MINOR；改為「每天都幾乎從早到晚」。複查 PASS。
- p71：editor「誰要是剛好生在贏家隊伍裡的魯蛇，就是會這樣」語法不通，接縫通讀時退回初譯句型「一個剛好生在贏家隊伍裡的魯蛇，就是會這樣」（只改句型，不另送複查）。
- p79 "I'm sure"：editor「我很確定」比初譯「我相信」貼近原文，reviewer 同意。
- p91：editor 把「賽菈正在旅館房間裡替自己倒茶」移到場景開頭獨立一段，段群內重排，reviewer 同意。
- 照原文：p43 "while you and Zei were talking"（雷克托其實主要在和鄧說話），照原文；p82 him 泛指真正的贏家，照初譯「他」。

## reviewer issue

- chunk 01 ISSUE 1（MINOR，語氣）：p48，見上。
- chunk 02 ISSUE 1（MINOR，一致性）：p65，見上。
- chunk 02 ISSUE 2（MINOR，語氣）：p67，見上。

## 補畫面

無。

## editor flags

- chunk 01、03：NONE。
- chunk 02：p82 him 的指涉照初譯。

## 接縫通讀

接縫（p52→分隔→p54、p89→dateline→p91）銜接自然；唯一修改是 p71 退回初譯句型（見上）。

## 裝置畫面

本章沒有裝置畫面。

## 待決事項

無。

## check

`uv run tools/check.py chapter 28`：PASS（無 WARN），段數 100/101，錨點對齊，字詞比 1.53。
