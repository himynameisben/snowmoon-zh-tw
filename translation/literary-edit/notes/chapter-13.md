# 第 13 章 文學編輯紀錄

狀態：**已完成**（v2，2026-10-06 使用者確認）。4 個 chunk 全部經 reviewer 一次 PASS，沒有補畫面，沒有待決事項，裝置畫面已轉圖。

## v2：正式設定（2026-10-06，已套用，未 commit）

- 設定：Opus editor（附底稿、可補畫面）→ `validate --report` → Opus reviewer（附用詞差異表）；4 個 chunk 平行，
  同一 chunk 串行。底稿為當時 commit 的 `zh-tw/chapter-13.md`（＝ v1）。bible 摘錄：`chapter-13.bible.md`。
- chunk（`literary_edit.py plan 13`）：

  | chunk | 範圍 | 字數 | 結果 |
  |---|---|---|---|
  | 01 | p3–23（大梅港包廂，與德爾瓦特會面） | 762 | PASS |
  | 02 | p25–27、p29–47（走出大梅港、莫夫來電） | 578 | PASS |
  | 03 | p49–64、p66–70（家庭晚餐、艾費里昂插播、莉莉玩遊戲） | 685 | PASS |
  | 04 | p72–102（硬體開放性規準小組會議） | 982 | PASS |

- 結果：段數 102（v1）→ 107（v2），全部變動在段群內，錨點不動。與 v1 字元相似度：p25–27（0.79）、p49–64（0.80）、
  p66–70（0.81）、p3–23（0.86）、p29–47（0.91）、p72–102（0.91）。
  拆段：p3（布簾／布置）、p15（想了一下／內心判斷／不能說出口的原因，三段）、p26–27（右轉、手錶各一段）、p59（「莉莉一動也不動」自成一段）、
  p67（「莉莉則只是盯著那段文字」自成一段）、p90（起疑／想出計畫）。合段：p19＋p20、p44＋p45。

## 重要裁決

- p12：「北極人也沒替自己說什麼好話」→「北極人自己也沒替自己加分」。採 QA（`translation/qa/chapter-13.md`）的建議：原文 making a case 指的是行為，不是言語。
- p42：初譯「反抗北極」→「反抗北極人」，照 worldbuilding（the Arctics＝北極人；ch17、ch18 也作「對抗北極人」）。reviewer 確認。
- p39：原文 "The whole point of splitting the discussion groups is to force people to think independently, to have them all taking cues from the same person!" 疑似漏了 not（應為 *not* to have them…）。
  `original/html/chapter-13.html` 字面相同，是原文本身的問題。照初譯與譯者筆記用反諷譯出（「結果他讓大家全都看同一個人的臉色！」），意思就是作者的本意，與第 12 章 p57 筆誤的處理方式相同，不列為待決事項。

## reviewer issue

無（4 個 chunk 都一次 PASS）。

## 補畫面

無。四個 editor 都沒有補畫面。

## editor flags

- chunk 02：p42「北極人」、p39 疑似漏 not、p44–45 合段——都已在上方裁決。
- 其餘 chunk：NONE。

## 裝置畫面

- 2 張：`ch13-01.png`（莫夫訊息）、`ch13-02.png`（艾費里昂〈平等主義的死亡之手，與強者之路〉）。
- 轉圖前比對過文字：與正文、英文一致。署名「領事」（consul）與 ch08「大使」不同，是原文如此（譯者筆記已記）。
- 沒有斷字、截斷、溢出；沒有改 CSS，不影響舊圖。Dreadknot 以 Courier New 呈現，與全書裝置畫面的拉丁字一致。

## 待決事項

無。

## check

`uv run tools/check.py chapter 13`：PASS，段數 102/107，錨點對齊，字詞比 1.48。
