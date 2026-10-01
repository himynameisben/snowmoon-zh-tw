# 第三階段：terms

## 修改摘要
- 修改章節：ch09, ch23, ch26
- 修改處數：3（譯文）；bible 34 條（glossary 30、characters 3、worldbuilding 1）

`check.py terms` 從 28 項降到 5 項，殘留全是英文字面比對的誤判（見「殘留與理由」）。原本報出的「避免譯法」經逐筆檢查，**全是誤判**（子字串命中一般詞），譯文中沒有真正用錯的定案譯名；所以這部分改的是 bible 的避免欄，不是譯文。

## bible 變更
| 檔案 | 詞條 | 舊 | 新 | 理由 |
|---|---|---|---|---|
| glossary | co-father | 譯名 共養父親 | 譯名 共養孩子的；避免 共養父親 | 「我的共養父親維爾」易讀成維爾是格拉迪亞斯的父親（ch23 譯者、QA 皆提）。全書只出現在 ch23 |
| glossary | Man was not made for categories | 人不是為分類而生 | 人不是為了分類而生 | 與備註全句、ch25 譯文一致（ch25 譯者、QA 建議） |
| glossary | copter | 小型旋翼機 | 旋翼機 | 全書實際用法（ch11、16、28、29 都只寫「旋翼機」）；ch05 首見寫「小型旋翼機」仍合規 |
| glossary | hash | 雜湊值 | 雜湊值／雜湊 | 涵蓋雜湊函數、雜湊式簽章等複合詞 |
| glossary | signature | 簽章；避免 簽名 | 簽章／招牌；避免 數位簽名 | 形容詞 signature（招牌隱私袍、招牌戰術）；表格上簽名是一般用法 |
| glossary | node | 節點 | 節點／據點 | ch22 企業分支據點 |
| glossary | thermal | 熱像 | 熱像／熱偽裝 | thermal cloak（ch26、ch30） |
| glossary | derivative | 衍生性商品 | 衍生性商品／導數 | ch29 微積分語境 |
| glossary | reputation | 信譽 | 信譽／聲望 | ch31 德盧因父母在北極帝國的一般名望，不是信譽系統 |
| glossary | tax nudges | 稅的輕推 | 稅的輕推／用稅輕推 | 備註原已規定口語寫「用稅輕推」 |
| glossary | shelter | 避難所 | 避難所／避難 | 備註原已規定 emergency shelter functionality→緊急避難功能 |
| glossary | tick | 避免 刻 | 避免 幾刻、毫刻 | 單字「刻」命中立刻、此刻、片刻等（31 章全是誤判）；規則移到備註 |
| glossary | pipeline | 避免 管道 | 避免 - | 「管道」是 channel 的正確譯法；規則移到備註 |
| glossary | permutation | 避免 排列 | - | arrange→排列 的一般用法誤報；規則移到備註 |
| glossary | anonymity set | 避免 匿名集 | - | 是正確譯名的子字串 |
| glossary | weight-preserving | 避免 保重 | - | 誤報 ch13「保重」 |
| glossary | least-significant bit | 避免 最低有效位 | - | 是正確譯名的子字串 |
| glossary | endpoint | 避免 終端 | - | 誤報「電腦終端機」 |
| glossary | Tier | 避免 層級 | - | 誤報「原子層級」 |
| glossary | circle (Keeper group) | 避免 圈子 | - | 誤報社交圈、繞圈子 |
| glossary | pin | 避免 針、別針 | 避免 別針 | 誤報針對、順時針 |
| glossary | steering (Minpentai) | 避免 操縱 | - | manipulate→操縱 是正確譯法 |
| glossary | air filter | 首見 ch03 | 首見 ch02；備註界定 | 獨立擺放的機器→空氣清淨機；ch02 教室內建→空氣過濾系統（ch02、ch06 QA） |
| glossary | Number Ten | 首見 ch19 | 首見 ch06 | ch06 譯者、QA |
| glossary | jie fe hen dzi | 首見 ch30；「原文無釋義」 | 首見 ch04；註明 ch04 原文下一段即「Wish you luck」 | ch04 譯者、QA。仍保留拼音、不加解釋 |
| glossary | cabin | - | 備註補：飛機 cabin→包廂 | ch26 用法 |
| glossary | channel (route) | （新增） | 管道／頻道／通道 | 記錄依語境的三種譯法，與 pipeline 區分；英文欄加括號以免 check.py 比對 |
| glossary | open source | （新增） | 開源；避免 開放原始碼 | 全書 11 處一致用「開源」，補成定案 |
| glossary | black car | （新增） | 黑色專車；避免 黑色車子 | ch09、ch12、ch18 等多章出現（ch09、ch12 譯者與 QA 提出） |
| glossary | sentry | （新增） | 哨戒 | ch29–30；不可與 Sentinel（哨兵）混淆（ch30 譯者、QA 建議） |
| characters | Zei | 避免 賊、齊 | 避免 賊 | 「齊」是法官齊文（Zevin）的定案用字，造成 14 章誤報；規則移到備註 |
| characters | Fin | 避免 芬 | - | 誤報「塔芬德爾」；規則移到備註 |
| characters | Bai | 避免 拜 | - | 誤報「拜託」「拜訪」；規則移到備註 |
| worldbuilding | Pafogai | 首見 ch15 | 首見 ch12 | ch12 譯者、QA |

所有「避免」欄移除的規則，都完整搬到該列備註，不會遺失。

## 全書修改
- black car：ch09 首見「黑色車子」→「黑色專車」，與 ch12 起的用法統一，影響 ch09（1 處）、ch26（1 處，「大型黑色車子」→「大型黑色專車」）
- co-father：「我的共養父親維爾」→「和我們家共養孩子的維爾」，影響 ch23（1 處）

逐筆查核但不必修改：avoid 命中的「刻」「齊」「芬」「拜」「針」「管道」「排列」「終端」「圈子」「操縱」「簽名」「層級」「保重」「匿名集」「最低有效位」全部是一般詞或子字串（詳見各章譯者筆記與上表理由）。另外用 en/zh 逐章出現次數比對所有 glossary 詞條，rubric、longhour、Keeper 等高頻詞全書一致；pyramid→金字塔、tunnel→隧道、open source→開源 也一致。

## 殘留與理由
- watch → 手錶（ch27）：原文是動詞 watch（盯著），不是手錶。
- pin → 球瓶（ch18、23、26）：原文的 pin 都在哲戈語拼音裡（bia pin、lin pin 等），照規定保留拼音。
- Glad → 格拉德（ch05、10、17、19、23）：原文是形容詞「Glad to…」，不是暱稱。
- Zero → 零號（ch11、21、27）：原文是數字零（Zero if…、Zero points、Zero information leakage）。
- Parliament → 議會，避免「國會」（ch13）：命中「北極帝國會在多久之內」的「帝國會」，誤判。保留「國會」在避免欄，因為它是真實的高風險誤譯。
- 明盤台廳（ch12）／廳室（ch04、ch12）：刻意不統一。ch12 第 234 段是有名稱的「the Minpentai room」，譯「明盤台廳」；ch04、ch12 的「廳室」是描述「a huge room」，屬一般詞。

以上 5 項 check 殘留都是 `check.py terms` 以英文字面比對造成的結構性誤判，無法透過 bible 消除（改 English 欄會讓真正的用法失去檢查）。

## 其他觀察
- 工具：`check.py terms` 的避免欄用純子字串計數，單字或短詞（刻、齊、針）必然誤報。本階段已改 bible 繞過；若要根治，可考慮讓避免欄支援 regex 或排除清單。英文比對也不含複數（signatures、cabins、thermal cloaks 不會命中詞條），會漏報。
- ch01 投票介面 Select「選定」與 ch07 餐廳評分 Select「確定」並存（ch01、ch07 QA）——屬 world 焦點的 UI 用語。
- ch03 第 33 段莫夫「join me as a Sentinel」與 ch08「當不成守律者」的身分矛盾——屬人物／劇情，留給 voice 焦點或使用者。
- ch10 第 111 段「Eighteen and Nine watched silently as Eighteen did his scan」疑似原文筆誤（應為 Gladias），QA 建議改「格拉迪亞斯和九號」，未動。
- ch20 第 30 段「被收買、被勒索」與 ch28 的用語、ch20／ch21 德爾瓦特引言「learn to love Veridia」的措辭，譯者建議跨章對齊，屬文句潤飾，未動。
- ch13 第 12 段「北極人也沒替自己說什麼好話」，QA 建議改「也沒替自己加分」，未動。
