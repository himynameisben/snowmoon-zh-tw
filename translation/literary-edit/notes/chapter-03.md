# 第 3 章 文學編輯紀錄

狀態：**已完成**（v2）。5 個 chunk 全部經 reviewer PASS，待決事項已由使用者裁定（見文末），未 commit。

## v2：正式設定（2026-10-04，已套用，未 commit）

- 設定：Opus editor（附底稿、可補畫面）→ `validate --report` → Opus reviewer（附用詞差異表）；5 個 chunk 平行，
  同一 chunk 串行。底稿為當時 commit 的 `zh-tw/chapter-03.md`（＝ v1）。bible 摘錄：`chapter-03.bible.md`。
- chunk（`literary_edit.py plan 3`）：

  | chunk | 範圍 | 字數 |
  |---|---|---|
  | 01 | p3–9（2 個段群） | 244 |
  | 02 | p11–33 | 1114 |
  | 03 | p35–67（4 個段群＋p47 海卓菲引言） | 1230 |
  | 04 | p69–84（2 個段群） | 800 |
  | 05 | p86–129 | 1305 |

- 結果：段數 130（v1）→ 146（v2），全部變動在段群內，錨點不動。與 v1 字元相似度最低的段群：
  p69–75（0.66，進大梅港）、p3–5（0.69）、p7–9（0.69）、p35–37（0.71）、p39–46（0.74）。
  對話為主的 p11–33（0.87）與 p86–129（0.83）改動較小。
- reviewer 結果：chunk 01、02、04、05 一次 PASS；chunk 03 兩個 MINOR ISSUE，修正後複查 PASS。
- 已接受的 reviewer issue（chunk 03）：
  - p48 "He vastly preferred looking at Hydrafill advertisements *or* Veridian virtue posters to construction cranes…"：
    editor 寫成「起重機……他實在看不下去」，把偏好寫成厭惡 → 改為「同樣是看，海卓菲的廣告*或*維瑞迪亞的美德海報，
    隨便哪一種，都比起重機和蓋到一半的水泥樓好看得多。」
  - p60 "Oof"：editor 寫「嘖」帶貶意，與兩人同情大梅港的立場不合 → 改回「哇」。
- 主 Agent 修正（不另送複查）：p4 "but not more"：editor「再亮一點都沒有」不通順 → 「再亮就沒有了」（同初譯）。
- 補畫面（共 2 處，reviewer 皆判符合規則）：
  - p35「有點刺眼」（身體感受，走出隧道時戶外的光照進眼裡）
  - p74「四周都是腳步聲」（聲音，地下人潮處）
- editor flag 處理：
  - p79 "Six out of fifty five"：p76 裝置畫面是已認證 55、未知 6（合計 61），原文敘事寫「五十五台裡有六台」。
    照原文譯，不修正原文（WORKFLOW：疑似原文筆誤不由 editor 決定）。見待決 2。
  - p36 "he liked their Helisport team"：editor 解讀 their＝北林（那家人剛去的地方），寫「那邊的旋翼球隊」；
    reviewer 同意，認為初譯「他們的」反而容易讀成那家人或那兩個孩子。見待決 1。
  - p80 "the maze"：v1「迷宮般的通道」→「這座迷宮」，避免和全章的「隧道」混淆。
- 接縫通讀：p9/p11、p33/p35、p37/p39（中間是手錶訊息畫面）、p67/p69、p84/p86 的主詞、時間、術語銜接無問題，
  沒有接縫修改。全章「隧道」（p4、p7、p35、p74）、「海報／看板」、「綠色圓圈」、「手錶就震動了」、
  「信譽 200 的匿名朋友」「那位神祕紳士」一致；p33 莫夫「快要加入我們、成為哨兵的人」照人物卡定案；
  p128 跟蹤者未點明身分。
- 機械檢查：`check.py chapter 3` PASS（段數 130/146，錨點對齊，字詞比 1.52，無 WARN）；`check.py terms` 第 3 章無警告；
  避免用語（彷彿、沉默地、灑落、說不上來、手機、面罩、隱私長袍、評分標準）全章 0 次。

## 使用者裁定（2026-10-04）

1. ~~p36 "their Helisport team"~~：使用者同意「那邊的旋翼球隊」（2026-10-04）。原題：採 editor／reviewer 的「那邊的旋翼球隊」（指北林），還是回到 v1 較含糊的「他們的旋翼球隊」？
2. ~~p79 "Six out of fifty five"~~：原文敘事與 p76 裝置畫面（已認證 55、未知 6，合計 61）不一致。使用者裁定（2026-10-04）：
   兩個數字分開講、不寫包含關係，改為「已認證的五十五台，沒認證的卻有六台，比例高得不尋常。」（人工裁定，不送 reviewer）
3. ~~p98~~：使用者同意「聽起來很過癮」（2026-10-04）。原題："They're a nice band, they're great fun, right?"：v2「他們是不錯的樂團，聽起來很過癮，對吧？」，
   「聽起來」把 great fun 限縮到聽覺（v1「很好玩」）。reviewer 未列 ISSUE，主 Agent 覺得可接受，請使用者確認。
