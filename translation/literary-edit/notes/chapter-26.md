# 第 26 章 文學編輯紀錄

狀態：**已完成**（v2，2026-10-07）。6 個 chunk 都經 reviewer PASS（chunk 02 一項 MAJOR、一項 MINOR，修正後複查 PASS；chunk 04 一項 MINOR，改回初譯用字），2 處補畫面（reviewer 判符合規則），1 項待決事項（使用者已裁定），裝置畫面已轉圖。

## v2：正式設定（2026-10-07）

- 設定：Opus editor（附底稿、可補畫面）→ `validate --report` → Opus reviewer（附用詞差異表）；6 個 chunk 平行，
  同一 chunk 串行。底稿為當時 commit 的 `zh-tw/chapter-26.md`（＝ v1）。bible 摘錄：`chapter-26.bible.md`。
- chunk（`literary_edit.py plan 26`）：

  | chunk | 範圍 | 字數 | 結果 |
  |---|---|---|---|
  | 01 | p3–p42（機上廣播，廣播引言之間的 14 個短段群） | 618 | PASS |
  | 02 | p44–p77（下機、閘門、專車上見韋爾多、賽菈） | 1418 | ISSUE 2 → 修正 → 複查 PASS |
  | 03 | p79–p102、p104–p114、p116–p128（營救行動前半） | 1346 | PASS |
  | 04 | p130–p138、p140–p151（營救後半、海上撤離） | 577 | ISSUE 1 → 修正（退回初譯用字） |
  | 05 | p153–p160（事後檢討） | 451 | PASS |
  | 06 | p162–p195（遊說法官） | 1372 | PASS |

- 結果：段數 195（v1）→ 203（v2），拆段都在段群內，錨點不動。與 v1 字元相似度（只比散文）：0.89。
- chunk 01 改動幅度小是預期的：格拉迪亞斯引號內的口譯是刻意的學習者直譯腔，照 v1 保留；`>` 哲戈語拼音 13 處經 reviewer 機械比對一字不差。
- reviewer 核對了所有拍數（二十／三十／五十／二十拍、一拍、不到十拍、四拍、十拍）、無人機架數（三架被擊中、第四架、四架倖存、一架裝死超過半分鐘、一百公尺）、
  撤離時間（一、十、三十、十、五十分鐘）與 p185 統計論證鏈，全部一致。

## 重要裁決

- p65 "so we can get them all together"：v1「我們可以讓他們全都待在一起」。reviewer 判 MAJOR 誤譯——get 承接前句 get her out，意思是三人在同一處、可以一次救出；
  改為「我們可以一次把他們全都弄出來。」複查 PASS。英文有一點歧義，列入待決事項，使用者裁定採用 A。
- p67 "Looks like they've decided to try to get Veridians to join…"：editor「打定主意」語氣過強且漏了 try to；reviewer MINOR，改為「看來他們決定……試著讓維瑞迪亞人自願加入北極帝國」。複查 PASS。
- p130：editor「一路停到總統官邸正前方」多出飛行過程，reviewer MINOR；退回初譯用字「就停在總統官邸正前方」（不另送複查）。
- p140 "Zei sat back down on his chair"：v1「往椅背一靠，又嘆了口氣」是誤譯（sat back down＝坐回椅子；原文沒有 again）；editor 改為「澤坐回椅子上，嘆了口氣」，reviewer 同意。
- p153 "Mu somehow saving us"：v1 漏了 somehow，editor 補成「不知怎麼地」，reviewer 同意。
- p160 "they think it's just Freetown's defense companies"→「以為這只是自由城那些國防企業的手筆」：reviewer 判沒有超出原文（下一句 credit 講的就是功勞歸誰）。
- 原文照舊不改：p104 parliament building→議會大廈；p156 the planes→飛機；p185 compacency→安於現狀；p165、p193 Northglade 與 p166、p180、p182、p185、p187 Northshore 各照原文譯（北林在北岸省內，不衝突）。

## reviewer issue

- chunk 02 ISSUE 1（MAJOR，誤譯）：p65，見上。
- chunk 02 ISSUE 2（MINOR，語氣）：p67，見上。
- chunk 04 ISSUE 1（MINOR，誤譯）：p130，見上。

## 補畫面

- ch26-p003~p004（p4）：「廣播提示音嗡嗡響起」的「嗡嗡」——把原文 buzzed 的聲音寫出來，reviewer 判符合規則；保留。
- ch26-p044~p077（p58）：「車子開始加速，身體微微往椅背一沉」——乘客被動的身體感受，reviewer 判符合規則；保留。

## editor flags

- chunk 01：補畫面一處。chunk 02：補畫面一處；p65 歧義（見上）。chunk 03：NONE。chunk 04：p140 v1 誤譯。chunk 05：p153 漏譯、p160 解讀。chunk 06：Northglade／Northshore 混用照原文。

## 接縫通讀

接縫（廣播段之間、p42→分隔→p44、p77→dateline→p79、各 SVG 戰況畫面前後、p138→畫面→p140 的兩次嘆氣（原文就是兩次）、p151→分隔→p153、p160→分隔→p162）銜接自然，無修改。

## 裝置畫面

- 4 張：`ch26-01.png`～`ch26-04.png`（SVG 戰況地圖：無人機圓點與虛線航跡、目標建築、暗黃三角形、紅色 x、黃色 ✓；圖內沒有文字，沒有動畫）。
- 轉圖前對照正文：01 三架無人機接近、暗黃三角形；02 三個 x（三架被擊中）；03 兩個 ✓（兩個明亮的黃色勾勾）、一個 x；04 兩個 ✓、撤離路線——與正文一致。
- 檢查：沒有截斷、溢出、空白圖；01 左緣的虛線航跡照原站 SVG 的 viewBox 裁切。本章沒有改 CSS 或 render 工具。
- 已轉圖章節更新為「第 1–20、22、23、25、26、30、31 章」：CLAUDE.md、AGENTS.md、TRANSLATION.md（兩處）。

## 待決事項

1. p65 "It's going to be difficult to get her out of Northglade, but at least that's also the place Febric and Hreda are, so we can get them all together."
   - A（目前採用，建議）：「我們可以一次把他們全都弄出來。」——get 承接前句的 get her out；ch24、ch27 的主題都是營救三個孩子。
   - B（v1）：「我們可以讓他們全都待在一起。」
   - **裁定（2026-10-07，使用者）：A。**

## check

`uv run tools/check.py chapter 26`：PASS（19 個 WARN，都是 `>` 哲戈語拼音錨點的「英文字母偏多／譯文偏短」，屬正常），段數 195/203，錨點對齊，字詞比 1.37。
