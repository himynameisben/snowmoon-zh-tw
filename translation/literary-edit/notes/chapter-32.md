# 第 32 章 文學編輯紀錄

狀態：**已完成**（v2，2026-10-06 使用者確認）。2 個 chunk 全部經 reviewer PASS。本章沒有裝置畫面。

## v2：正式設定（2026-10-06，已套用，未 commit）

- 設定：Opus editor（附底稿、可補畫面）→ `validate --report` → Opus reviewer（附用詞差異表）；2 個 chunk 平行，
  同一 chunk 串行。底稿為當時 commit 的 `zh-tw/chapter-32.md`（＝ v1）。bible 摘錄：`chapter-32.bible.md`。
- chunk（`literary_edit.py plan 32`）：

  | chunk | 範圍 | 字數 | 結果 |
  |---|---|---|---|
  | 01 | p3–6、p7 引言（卡利馬區、拆攝影機、紅花、海卓菲廣告） | 329 | PASS |
  | 02 | p8–112（走到議會、韋爾多辦公室長談、屋頂眺望） | 4986 | PASS |

  chunk 02 是單一段群（p7 引言之後到章末沒有錨點），超過 1,500 字上限也不能切。
- 結果：段數 112（v1）→ 117（v2），全部變動在段群內，錨點不動。
  拆段集中在 p4（拆攝影機拆成四段：爬梯、拆下扔進箱子、哐啷聲、爬下梯子）、p5（記得這家店／這次是紅花）、p9（看手錶自成一段）；
  辦公室對話一個說話輪次一段不變，多為段內句法重排。
- reviewer 結果：2 個 chunk 都沒有 ISSUE。
- 改寫中涉及語意判斷、reviewer 確認可接受的兩處：
  - p63「can do the good of ordinary life but not the evil of empire」：v1「卻不去做」（意願）→ v2「卻做不出」（能力），較貼 can…but not。
  - p63「avoid becoming one」：v1「避免自己變成北極帝國」→ v2「避免自己變成那樣的帝國」（one＝一個那樣的帝國）。
  - reviewer 附註不列 ISSUE：p42「or maybe something even higher bandwidth」v2「或許還要頻寬更高的」，中文稍像兩者都要，理解不變。
- 初譯漏譯補回：p6 Taped →「用膠帶貼著」（v1 只寫「貼著」）。
- 補畫面（共 3 處，reviewer 皆判符合規則）：
  - p3「樹影一塊塊落在路面」
  - p8「車流聲從腳下一陣陣傳上來」（天橋）
  - p105「腳步聲在樓梯間迴響」
- 照原文、不修正：p47 原文 You've aligning 是 You're aligning 筆誤、p109 oversided 是 oversized 筆誤，照意思譯（同 v1）；
  p65「water and ice at the same time」的歧義沿用 v1 的模糊說法；p61 韋爾多的女兒不與佩萊連結；未標說話者的輪次不補；
  p75 說話標籤由句後移到句前（「格拉迪亞斯插了一句：」），未增刪標籤。
- 避免用語：全章「彷彿、沉默地、灑落、說不上來、手機」0 次。
- 接縫通讀：chunk 邊界落在 p7 `>` 引言上。p6「用膠帶貼著一張廣告：」→ 引言 → p8「路旁換成濃密的灌木叢」銜接無問題。
  全章「卡利馬區」「保全攝影機」「光呎」「規準」「晶體」「整齊劃一」「弱者要隱私，強者要透明」「AI 應該是玩家，而不是遊戲本身」一致；
  p8 與 p109 城堡塔樓的譯法呼應；最後一句「再說，梅爾丹是我的家。」與 v1 相同。沒有接縫修改。

## 機械檢查

- `check.py chapter 32`：PASS（段數 112/117，錨點對齊，字詞比 1.50）。

## 待決事項

無。
