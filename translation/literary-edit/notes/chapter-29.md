# 第 29 章 文學編輯紀錄

狀態：**已完成**（v2，2026-10-07）。5 個 chunk 都經 reviewer PASS（chunk 01、03 各一項 MINOR；chunk 05 一項 MINOR 修正後複查 PASS），1 處補畫面（reviewer 判符合規則），沒有待決事項，裝置畫面已轉圖。

## v2：正式設定（2026-10-07）

- 設定：Opus editor（附底稿、可補畫面）→ `validate --report` → Opus reviewer（附用詞差異表）；5 個 chunk 平行，
  同一 chunk 串行。底稿為當時 commit 的 `zh-tw/chapter-29.md`（＝ v1）。bible 摘錄：`chapter-29.bible.md`。
- chunk（`literary_edit.py plan 29`）：

  | chunk | 範圍 | 字數 | 結果 |
  |---|---|---|---|
  | 01 | p3–p20（雪丘上：澤、穆、白；作戰計畫） | 557 | ISSUE 1 → 修正 |
  | 02 | p22–p34、p36–p37（雷克托的簡報） | 417 | PASS |
  | 03 | p39–p53、p55–p58、p60–p67、p69–p73（出擊、第一場勝利） | 1480 | ISSUE 1 → 修正（退回初譯） |
  | 04 | p75–p77、p79–p80、p82–p107、p109–p113（主戰、戰術失效、鄧陣亡） | 1163 | PASS |
  | 05 | p115–p140（德盧因的訊息、白的提議、梯度下降） | 1032 | 主 Agent 先修一處 → ISSUE 1 → 修正 → 複查 PASS |

- 結果：段數 140（v1）→ 157（v2），拆段都在段群內，錨點不動。與 v1 字元相似度（只比散文）：0.86。
- reviewer 核對了四路軍任務、三長時、拍數與時間（一拍、一百拍、二十／三十拍、二十／四十分鐘、一個半長時）、無人機數字（十架、幾十架、一百、幾百）、
  戰術編號（一至六號、尾數 0 或 5、八種裡第七種）、p65 北極雪地無人機的改良與代價、p104 兩處登陸、p134–p138 梯度下降與模擬器的論證，全部一致。

## 重要裁決

- p8：editor 補「靴子陷進深雪裡」，reviewer MINOR（多了具體裝備，與 p47 的雪鞋對不上）；改為「腳陷進深雪裡，一聲一聲」，保留聲音的補充。
- p56 "had easily defeated a few small Arctic sentry units"：editor「只碰上幾支……」多出「沒遇到別的敵軍」的斷定，reviewer MINOR；退回初譯句型「三路主力輕鬆擊潰了幾支小型的北極哨戒部隊」。
- p63 "on top of the few dozen that had already been lost to stationary Arctic traps"：editor 改成不指明損失屬於哪一方（「在這之前，還有幾十架早就折損在……」），reviewer 判比初譯「這還不算」更貼近原文的保留；採用。
- p127 "Delwart had planted evidence for months against Gladias and Mov"：editor 改成「陷害」並 flag；主 Agent 依 synopsis 第 21 章（莫夫偷聽到的「銀聊會面」是德爾瓦特故意布的局，用來誤導兩人）改回「騙過了格拉迪亞斯和莫夫」，送 reviewer，reviewer 引第 21 章原文確認正確。
- p119、p121：editor「對手若不會，反而會敗得更快」「這套戰術只會敗得更快」主詞不清、漏了 much，reviewer MINOR；改為「對手若沒有這個弱點，用的一方反而會敗得快得多」「用這套戰術的一方會敗得更快」，複查 PASS。
- 照原文：p136–p139 原文未標說話者（可能是澤，也可能是白繼續說），照初譯不點名。

## reviewer issue

- chunk 01 ISSUE 1（MINOR，增譯）：p8「靴子」，見上。
- chunk 03 ISSUE 1（MINOR，增譯）：p56「只碰上」，見上。
- chunk 05 ISSUE 1（MINOR，語氣／誤譯）：p119、p121，見上。

## 補畫面

- ch29-p003~p020（p3）：「冷風迎面颳來，又強又冷，刮得臉頰生疼」——身體感受，與原文強冷風迎面、身體其他部位有外套相容，reviewer 判符合規則；保留。
- ch29-p003~p020（p8）：「腳陷進深雪裡，一聲一聲」——聲音與 fighting the deep snow，修正後保留（見上）。

## editor flags

- chunk 01：補畫面兩處。chunk 02、04：NONE。chunk 03：p63 損失歸屬（見上）。chunk 05：p127 德爾瓦特（見上）；p136–p138 說話者。

## 接縫通讀

接縫（p20→分隔→p22、簡報→作戰圖→p36、p37→分隔→p39、p53→dateline→p55、各作戰圖前後、p107→基地被毀訊息→p109、p113→德盧因訊息→p115）銜接自然，無修改。

## 裝置畫面

- 8 張：`ch29-01.png`（作戰圖：北路軍／中路軍／南路軍／海路軍、北林）、`ch29-02.png`、`ch29-05.png`、`ch29-06.png`（作戰圖，標北林）、`ch29-03.png`、`ch29-04.png`（局部戰況，只有圓點）、
  `ch29-07.png`（第三後方基地被毀、鄧生還機率低於 10%）、`ch29-08.png`（德盧因的訊息）。沒有動畫。
- 轉圖前對照正文：四路軍名稱、北林、第三後方基地、鄧與南路軍、10%、德盧因訊息的內容（南翼、海岸以北約二十公里、收復北林）都與正文、bible 一致，沒有修改。
- 檢查：沒有斷字、截斷、溢出；作戰圖的「北路／軍」照原稿兩行。本章沒有改 CSS 或 render 工具。
- 已轉圖章節更新為「第 1–20、22、23、25–27、29–31 章」：CLAUDE.md、AGENTS.md、TRANSLATION.md（兩處）。

## 待決事項

無。

## check

`uv run tools/check.py chapter 29`：PASS（無 WARN），段數 140/157，錨點對齊，字詞比 1.50。
