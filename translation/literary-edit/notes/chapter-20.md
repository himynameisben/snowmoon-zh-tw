# 第 20 章 文學編輯紀錄

狀態：**已完成**（v2，2026-10-06）。5 個 chunk 經 reviewer PASS（chunk 05 一項 MINOR issue 修正後複查 PASS），沒有補畫面，沒有待決事項，裝置畫面已轉圖。
使用者事先授權（延續第 19 章的指示）：沒有需要確認的地方就直接標已完成並 commit。

## v2：正式設定（2026-10-06）

- 設定：Opus editor（附底稿、可補畫面）→ `validate --report` → Opus reviewer（附用詞差異表）；5 個 chunk 平行，
  同一 chunk 串行。底稿為當時 commit 的 `zh-tw/chapter-20.md`（＝ v1）。bible 摘錄：`chapter-20.bible.md`。
- chunk（`literary_edit.py plan 20`）：

  | chunk | 範圍 | 字數 | 結果 |
  |---|---|---|---|
  | 01 | p3–5、p6（引言）、p7–8、p9（引言）、p10、p12（入侵新聞、孩子們的訊息） | 505 | PASS |
  | 02 | p14–18、p20–52（莫夫來訪、地下室談話、出發） | 1456 | PASS |
  | 03 | p54–86（泰爾羅伊） | 1175 | PASS |
  | 04 | p88–124（芭爾梅） | 1410 | PASS |
  | 05 | p126–132、p134–180（列克托比、推理） | 1190 | ISSUE 1 → 修正 → PASS |

- 結果：段數 180（v1）→ 188（v2），全部變動在段群內，錨點不動（p6、p9 引言的 `>` 結構不變）。與 v1 字元相似度：p3–5（0.75）、p10（0.76）、
  p126–132（0.83）、p9（0.86）、p20–52、p88–124（0.87）、p12（0.88）、p134–180（0.89）；其餘 0.90 以上。
  拆段：p3、p7（「不……」獨立）、p12（哭了起來獨立）、p61（腳步聲／莫夫拿下兜帽／賽菈拿下兜帽）、p80、p88、p126 等。

## 重要裁決

- p178 最後一問 "not make any effort at all on the rubric that Silverchat cared the most about, getting properly rewarded for being so effective at openness and interoperability"：
  初譯「讓它在開放性和互通性上做得這麼好，能得到應有的獎勵」的「它」指涉不清。editor 拆成問句＋說明句，但說明句「做得這麼好，靠的就是這條規準」把規準讀成銀聊做得好的原因；
  reviewer 列 MINOR，改為「銀聊在開放性和互通性上做得這麼好，要拿到應有的獎勵，就看這條規準了啊。」，複查 PASS。
- p112 "get guarantees about what purpose the data is being used for"：初譯「確保資料只被用在什麼用途上」的「只」沒有原文依據，editor 拿掉；reviewer 同意。
- p31 "Maybe I'll tell you what I know"：初譯漏 Maybe，編輯稿補回「那也許換我跟你說說」。
- p9 「大梅港與北林其他地區之間」照字面（譯者筆記與 QA 已定，原文可能有誤，照譯）；especially in the first longhour 改為「尤以第一個長時內為多」，比初譯「大多是」貼近原文。
- p175、p179 原文兩次寫「站起來」，兩處都保留。
- p85–p86 兩段都是泰爾羅伊，照原文分段、不點名。

## reviewer issue

- chunk 05 ISSUE 1（MINOR，誤譯／因果）：p178 說明句。已修正，複查 PASS。

## 補畫面

無（reviewer 確認 p126「沒有跟過來」、p136「腳步聲又響起」只是改寫原文資訊，不算補畫面）。

## editor flags

- chunk 01、02：NONE。
- chunk 03：p85–p86 同一說話者分兩段保留。
- chunk 04：p112 主詞不點出、拿掉「只」。
- chunk 05：p178 長問句拆分；p175／p179 兩次站起來。

## 接縫通讀

chunk 邊界（p5→引言→p7、p8→新聞→p10→訊息畫面→p12、p12→分隔→p14、p18→驗證畫面→p20、p52→分隔→p54、p86→分隔→p88、
p124→分隔→p126、p132→燒幣畫面→p134）銜接自然，無修改。

## 裝置畫面

- 3 張：`ch20-01.png`（費布里克與赫蕾妲的訊息）、`ch20-02.png`（格拉迪亞斯的常用聯絡人／證明已驗證）、`ch20-03.png`（剛剛燒掉了 50 吉普幣）。
- 轉圖前對文字：時間 19867～20077、50 吉普幣與正文一致；譯名一致。沒有截斷、溢出；本章沒有改 CSS 或 render 工具。

## 待決事項

無。

## check

`uv run tools/check.py chapter 20`：PASS（無 WARN），段數 180/188，錨點對齊，字詞比 1.51。
