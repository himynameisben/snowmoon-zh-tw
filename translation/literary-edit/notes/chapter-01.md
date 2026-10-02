# 第 1 章 文學編輯紀錄

狀態：**已完成**（v2）。正式設定已套用到 `zh-tw/`，所有 chunk 經 reviewer PASS，待決事項已由使用者裁定。

版本名稱：v1＝初譯定稿（凍結在 `zh-tw-v1/`）；試編版＝下面的保守修稿；v2＝第二輪正式設定的成果（寫進 `zh-tw/`）。

## 試編版：保守修稿（2026-10-01，已套用，將被 v2 取代）

- 規則：逐段一對一、Sonnet editor／reviewer、舊版 `literary-editor.md`（修稿模式）。
- 底稿：開工時 `zh-tw/chapter-01.md` 第 3–6 段已有使用者未 commit 的人工修訂，視為較新的底稿交給 editor，
  並要求在這幾段保守修改。
- 結果：5 個 chunk（p3–10、p12–38、p39–68、p69–88、p90–141），reviewer 全 PASS；141 段中改了 57 段，
  多為換字，句子骨架與分段未動。使用者認為不夠，因此改走 v2。
- 主 Agent 裁決：
  - p3：恢復使用者原句「寫著有衣物、花卉或食物出售」。
  - p39：恢復初譯「投下一場影響更重大的票」。
  - p66：統一為「系統會記分」，與 p39 呼應。
- 之後的變動：
  - p5「五公寸」改成「五十公分」（使用者決定，bible 已同步）。
  - p10 editor flag：density 譯「人口密度」帶有推論；維持現譯，留給人工決定。

## 規則變更（2026-10-01）

- 段落改為錨點對齊（`check.py` 支援），段群內可拆段、合段、重排。
- editor 改為重寫模式，開放少量補畫面；editor 與 reviewer 都用 Opus；reviewer 附用詞差異表。
- 決策依據：`../experiments/2026-10-01-ch01-p042-067.md`（p42–p67 的七種版本比較）。

## v2 交接（給下一個 session）

1. 先看 `git status --short`。本章目前的 `zh-tw/chapter-01.md` 就是 v2 的底稿，內容為試編版、使用者第 3–6 段修訂與「五十公分」。對照初譯請看 `zh-tw-v1/chapter-01.md`。
2. bible 摘錄已備好：`chapter-01.bible.md`（全章固定用詞、本章 bible 譯名、人物口吻、伏筆邊界、哪些段落適合補畫面）。
3. 切 chunk：`uv run tools/literary_edit.py plan 1`，目前切成 8 個 chunk：

   | chunk | 範圍 | 字數 |
   |---|---|---|
   | 01 | p3–10 | 625 |
   | 02 | p12–31 | 1163 |
   | 03 | p33–40 | 434 |
   | 04 | p42–67 | 1319 |
   | 05 | p69–74 | 443 |
   | 06 | p76–88 | 749 |
   | 07 | p90–99 | 389 |
   | 08 | p101–140 | 969 |
4. 依 `../WORKFLOW.md` 逐 chunk 跑：Opus editor → `validate --report` → Opus reviewer → 修正 → `apply`。
   chunk 04 已有試跑稿，但試跑時沒有全章 bible 摘錄、補畫面規則也還沒定案，正式跑請重新產生，不要沿用。
5. 全部套用後做接縫通讀，跑 `check.py chapter 1`，更新本檔與 `../progress.md`。

## v2：正式設定（2026-10-02，已套用，未 commit）

- 設定：Opus editor（附底稿、可補畫面）→ `validate --report` → Opus reviewer（附用詞差異表）；8 個 chunk 平行，
  同一 chunk 串行。底稿為當時 commit 的 `zh-tw/chapter-01.md`（試編版＋使用者 p3–6 修訂＋五十公分）；chunk 04 試跑稿未沿用。
- 結果：段數 141（v1）→ 183（v2），全部變動在段群內，錨點不動。改寫幅度最大（與 v1 字元相似度最低）的段群：
  p94–95、p53–55、p20–23、p33–40、p3–10、p57–59、p69–74（p69–74 由 6 段拆成 13 段）。
- reviewer 結果：chunk 03、05、06、07、08 一次 PASS；01、02、04 各 1 個 MINOR，修正後複查 PASS。
  - chunk 01（p3–10）：「夠密，也夠安靜，靜到他差點忘了」把原因縮成只有安靜 → 改「夠密，四下也夠安靜，讓他差點忘了」。
  - chunk 02（p12–18）：「自然景色」弱化 natural world／human world 的對照 → 恢復「自然世界」。
  - chunk 04（p42–51）：「聽完之後」只剩時間先後，丟了 primed him 的因果 → 改「課程讓他格外留意」。
- editor 主動修正 v1 的兩處，reviewer 判定較貼近原文，已採用：
  - p57 painfully murdered：「慘遭殺害」→「被虐殺」（保留「痛苦地被殺」；列入待人工決定，看語感）。
  - p66 not quite sure if A, or if B：v1「究竟是 A，還是 B」讀成二選一 → 拆成兩個獨立疑問。
- 補畫面（共 4 處，reviewer 皆判符合規則）：
  - p3–10「吸了一口帶著草木味的空氣」（嗅覺，附在 breathed in）
  - p12–18「車聲一陣陣從橋下傳上來」（聲音，busy road）
  - p42–51「低音一下一下震在胸口」（身體感受，the noise became louder）
  - p101–138「咚咚咚的腳步聲，又重又響，一路往下」（聲音，loud footsteps coming down the stairs）
- editor flag 處理：
  - p90、p105 起 autobus 簡稱「巴士」：p90 已以「自駕巴士」首次介紹，沿用初譯簡稱，不改。
  - p83 snatched … from his arm：v1 與 v2 都作「手中」（前文男人正拿裝置對著他的臉）；列入待人工決定。
- 接縫通讀：8 個 chunk 邊界的代名詞、主詞、時間銜接、術語無問題，未做接縫修改（不需複查）。
  兩處「系統會記分」（p39、p66）、兩處「——除此之外，什麼也不知道。」（p5、p44）都保留。
- 機械檢查：`check.py chapter 1` PASS（段數 141/183，錨點對齊，字詞比 1.53）；`check.py terms` 第 1 章無警告；
  避免用語（面罩、商家、隔音屏障、節目、一份規準、勒令、彷彿、沉默地、灑落等）全章 0 次。

## 使用者裁定（2026-10-02，照主 Agent 建議）

- p10 density：維持「人口密度」。單說「建築物的密度」在中文會讀成材料或建築量體密度；流行病脈絡下指的是人的密度。
- p57 painfully murdered：採用 v2「被虐殺」。
- p83 from his arm：維持「從他手中」（前文男人正拿裝置對著他的臉）。
