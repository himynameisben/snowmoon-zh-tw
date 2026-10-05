# 第 5 章 文學編輯紀錄

狀態：**已完成**（v2）。5 個 chunk 全部經 reviewer PASS，裝置畫面已轉圖，待決事項已由使用者裁定（見文末）。

## v2：正式設定（2026-10-05，已套用，未 commit）

- 設定：Opus editor（附底稿、可補畫面）→ `validate --report` → Opus reviewer（附用詞差異表）；5 個 chunk 平行，
  同一 chunk 串行。底稿為當時 commit 的 `zh-tw/chapter-05.md`（＝ v1）。bible 摘錄：`chapter-05.bible.md`。
- chunk（`literary_edit.py plan 5`）：

  | chunk | 範圍 | 字數 |
  |---|---|---|
  | 01 | p3–24（2 個段群：到飯店、入住） | 721 |
  | 02 | p26–37（飯店大廳、囚犯困境） | 337 |
  | 03 | p39–46（經濟研究所） | 381 |
  | 04 | p48–88（共同治理課程、與賽菈和楊恩同桌） | 1321 |
  | 05 | p91–118（賽菈與格拉迪亞斯通話） | 435 |

- 結果：段數 118（v1）→ 125（v2），全部變動在段群內，錨點不動。與 v1 字元相似度：
  p39–46（0.74，研究所收費與螺旋樓板）、p26–37（0.81）、p3–22（0.83）、p91–118（0.83）、p48–88（0.87，對話為主）。
- reviewer 結果：chunk 01、02、03 一次 PASS；chunk 04 一個 MAJOR、chunk 05 三個 MINOR，修正後複查 PASS。
- 已接受的 reviewer issue：
  - chunk 04，p65 "My husband's and my turn to take care of our children just finished, they're with our co-parents now"：
    editor 寫「我先生和我輪流照顧孩子，我們這一輪剛結束」，會讀成夫妻兩人彼此輪流；原意是夫妻這一方與共養父母輪流 →
    「前一陣子輪到我先生和我照顧孩子，這一輪剛結束，孩子現在在我們的共養父母那裡」。
  - chunk 05，p92 "She could make out Gladias's face"：editor「格拉迪亞斯的臉出現了，她看得清楚」把 make out 加強成清楚 →
    「她看得出那是格拉迪亞斯的臉。」
  - chunk 05，p96 "one of the two got his arm injured"：editor「其中一個男孩」會讓人以為兩個孩子都是男孩（另一個是白）→
    「兩個孩子裡的一個」（同 v1 範圍）。
  - chunk 05，p107 "to really make sure that the rubrics themselves are set right"：editor 只剩「規準本身定得對不對」，
    really make sure 的把關動作不見 → 「真正確保規準本身定得對，對維瑞迪亞來說才是更重要的事。」
- 補畫面（共 2 處，reviewer 皆判符合規則）：
  - p19「光線一下子暗下來」（駛進車庫）
  - p43「旋轉閘門喀噠一聲轉開」（閘門轉動的聲音）
  - （p13「嗡嗡」、p22「嗶了一聲」、p24「震了一下」是原文，p21「啪地」是 slapped 的擬聲，不算補畫面。）
- editor flag 處理：
  - p21–p22：slapped 與 one tick 都落在「拍」字（「往圓圈上啪地一拍。」「過了一拍，圓圈嗶了一聲。」）。reviewer 判「過了」已標出時間，
    不會誤讀；改「按」會弱化 slapped，保留。
  - p42 "if you had failed to pay back loans or trashed hotel rooms multiple times"：v1 只讓「好幾次」修飾弄亂房間，
    v2 寫成「除非好幾次借錢不還，或好幾次把飯店房間搞得一團亂」。reviewer 判 multiple times 修飾整個 or 結構是最自然的讀法，保留；待決 2，使用者裁定維持 v2。
  - p43 glowing green circles 複數 →「幾個發著綠光的圓圈」，reviewer 同意。
  - p105–p107：原文「你覺得呢？」之後寫格拉迪亞斯停下來想「他的回答」，接著是格拉迪亞斯說明想當守律者的理由，說話者標示疑似錯位；
    依 bible 照原文，不補說話者、不修正。
  - p109：「楊恩沒多久也去開會了」提到「這五十分鐘左右」之前，時間關係不變，reviewer 同意。
- 照原文、不修正：p96 賽菈說手臂「受了傷」（p73 澤說「斷了」）；p59「我的……朋友」只保留停頓。
- 避免用語：全章「彷彿、沉默地、灑落、說不上來、手機、飛船、哈希、囚徒、聲譽」0 次。
- 接縫通讀：p22/p24（入住畫面）、p24/p26、p37/p39、p46/p48（共同治理地圖）、p88/p91（來電畫面）的主詞、時間、術語銜接無問題，
  沒有接縫修改。全章「剩餘」（p33、p36）「共同治理」「規準」「守律者」「學術與知識信譽分數」一致。

## 裝置畫面轉圖

- 3 個裝置畫面：`zh-tw/devices/ch05-01.html`～`ch05-03.html`，圖片 `assets/devices/ch05/ch05-01.png`～`ch05-03.png`。
  01 飯店入住（信譽分數 ≥ 100、付款成功、房號 714、715、716）、02 共同治理地圖（SVG，15 個城市名與連線權重）、03 格拉迪亞斯來電（58130）。
- 畫面文字和英文原文、正文、bible 地名表一致，未修改。03 表頭沿用第三章訊息畫面的「寄件者／訊息／時間」。
- 排版修正（改 `tools/render_devices.py`）：
  - 02：SVG 的地名位置是照英文排的，中文較寬，最右邊的「伊普塔克」超出 viewBox 被切 → `.device-view svg { overflow: visible; }`。
    副作用：「彼得斯維」的標籤底色是原稿替英文 Petersvil 量的寬度，英文版本來就超出 viewBox（被切掉看不見），
    現在在地圖右緣露出一小截藍色（待決 1，使用者裁定接受）。
  - 03：「格拉迪亞斯」被拆成「格拉迪／亞斯」 → `.device-view td > center, .device-view td > span { word-break: keep-all; }`
    （比照表頭：中文詞不從中間斷，空格與標點處照樣可換行）。
  - 03：名字與「［來電中］」都不斷之後，表格比窄版畫面寬約 20px，時間欄被切 → 截圖前偵測，只有內容真的溢出的畫面才放寬到剛好容得下
    （05-03 寬 342px，其他畫面寬度不變）。
- 改 CSS 後重跑第 1–5 章，變動的舊圖：
  - `ch01-07`、`ch01-08`（匿名訊息）：長訊息改在逗號處換行（「我在演唱會上看到你了，／我知道你是掌舵會的人。」），舊圖是「掌舵會／的人。」。
  - `ch03-02`（賽菈傳來［4 張圖片］）：舊圖「［4 張圖／片］」，新圖「［4／張圖片］」。
  - 圖片寬度與 alt 都沒變，章節檔不受影響。`ch04-02` 曾在一次重跑出現肉眼看不出的像素差，再連跑三次都和 commit 版相同，是偶發的截圖時序差異。

## 機械檢查

- `check.py chapter 5`：PASS（段數 118/125，錨點對齊，字詞比 1.54）。
- `check.py chapter 1`～`4`：PASS（第 2、4 章的 WARN 與先前相同）。

## 使用者裁定（2026-10-05）

1. ~~ch05-02~~：使用者選 (a) 接受（2026-10-05）。原題：ch05-02 地圖右緣露出「彼得斯維」標籤底色的一小截。選項：(a) 接受（原稿的標籤底色本來就超出，只是英文版被切掉）；
   (b) 拿掉 `svg overflow: visible`，改讓「伊普塔克」的「克」被切掉；(c) 另寫 CSS 把 SVG 內標籤底色裁在 viewBox 內（要多一層處理，也會影響其他 SVG）。
   主 Agent 建議 (a)。
2. ~~p42~~：使用者選維持 v2（2026-10-05）。原題："failed to pay back loans or trashed hotel rooms multiple times"：v2「除非好幾次借錢不還，或好幾次把飯店房間搞得一團亂」
   讓「好幾次」修飾兩者；v1 是「只有借錢不還，或好幾次把飯店房間搞得一團亂」。reviewer 判兩者皆修飾較自然。
   主 Agent 建議維持 v2。
3. ~~p116~~：使用者未另提修改，維持現狀（2026-10-05）。原題："Gladias stared in response, his eyes wide open"：v1、v2 都是「睜大眼睛，愣愣地看著她」。譯者筆記曾提「愣愣地」略偏驚訝，
   可改「睜大眼睛看著她」；QA 判 stared…eyes wide open 本有驚訝意，保留。主 Agent 建議維持現狀。
