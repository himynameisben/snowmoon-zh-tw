# 第 18 章 bible 摘錄（第二輪文學編輯用）

主 Agent 依 WORKFLOW「開始一章前」第 5 步建立；每個 chunk 的資料包都附上這份（`literary_edit.py packet --bible`）。
權威來源仍是 glossary／characters／worldbuilding；這裡只是本章會用到的部分，加上本章初譯已定的用詞。
段號為原文段號（`literary_edit.py plan 18` 的 pNNN；與 `translation/notes/chapter-18.md` 的段號相同）。

章節結構：p2 dateline（帕佛蓋都，果月 18 日）｜p3–p53 黑色專車：澤與白接格拉迪亞斯（模擬窗、隧道換車廂、山體金字塔 96.7%），抵達飯店（p50 入住裝置畫面）｜
p54 分隔｜p55–p83 格拉迪亞斯獨自散步：高安全等級運貨（實體物品的混合網路）、第 17 街的店家、地下室招牌（p73 哲戈語標語 dz-card）、登坡俯瞰城市、沿林蔭步道繞回飯店｜
p84 分隔｜p85–p127 飯店大廳的餐廳：白給他看古詩（p89 裝置畫面）、汾現身並發表「哲戈語是協調訓練」的演說（p108–p127）。

chunk（`plan 18`）：01＝p3–p53（跨 p50 裝置畫面）｜02＝p55–p83（跨 p73 招牌）｜03＝p85–p88（只有 89 字，接 p89 畫面）｜04＝p90–p127。

### HTML 區塊與 check 的「英文字母偏多」WARN（p50、p73、p89）

三段都是刻意保留的哲戈語拼音，不是漏譯（譯者筆記與 QA 已確認）；三段都是 HTML 錨點，不送 editor，一字不動。

- p50（`device-view narrow-device-view`，飯店入住畫面）：全是哲戈語（sen hen zi li die fe 100／zo lia kin／man dun li jie hu／cau tie zen／ci fan zi li 448），原文沒有釋義，保留原樣、不翻、不在散文裡替它解釋。
- p73（`dz-card`，地下室招牌標語 pa jan li sun zo…）：哲戈語，原文沒附釋義，synopsis 註明「不要自行解釋」。p74 只寫「他好奇這些字是什麼意思」，不要補上意思或猜測。
- p89（`device-view wide-device-view`，古詩）：`<p>` 第一行已譯為「他走上人跡較少的那條路，而那為眾人開出了一條道路。」，必須與 ch11 賽菈引用的句子一字不差；`<pre>` 內的 jan jo san sia 六行哲戈語不動。古詩的意思由白在 p95 口頭說出。
- 本章目前還沒轉圖（CLAUDE.md：已轉圖章節為 1–15、30、31）。若之後把 p50、p89 轉成圖，改字要改 `zh-tw/devices/ch18-KK.html`；轉圖後 WARN 理應消失或照舊為拼音，判斷方式同上。

## 一、全章固定用詞（editor 一次只看一個 chunk，看不到別處的叫法；這些不要換）

| 原文 | 本章用法 | 出現位置／說明 |
|---|---|---|
| air harbor | 空港 | p3、p12 |
| sealed opening | 密封的出口 | p3 |
| large black car／black car(s) | 大型黑色專車／黑色專車 | p3、p15、p29、p30、p59、p122 |
| backward-facing／forward-facing seat | 背對車頭的座位／面向車頭的座位 | p4 |
| You must be Zei and Bai. | 你們一定就是澤和白了。 | p5 |
| right-side window | 車子右側的窗戶 | p11 |
| a series of stores | 一整排商店 | p12 |
| something was off | 有什麼不對勁 | p13 |
| real window | 真的窗戶 | p14 |
| heightened security protocols | 提高了安全規格 | p15 |
| bi-directional | 雙向的 | p15 |
| simulated window | 模擬窗 | p15 |
| it's picking me | 它選了我 | p16 |
| Huh. | 喔。 | p17 |
| colors and the depth | 顏色和景深 | p18 |
| surprisingly normal | 意外地正常 | p18 |
| cartoon animals／speech bubbles | 卡通動物／對話框 | p19、p72 |
| Dzegoban | 哲戈語 | p19、p72、p75、p93、p108 起 |
| hand devices, compute boxes, lamps, drones, sensors | 手持裝置、運算盒、燈具、無人機、感測器 | p20 |
| "MIN KUI"／"GUI SAU" | 「MIN KUI」／「GUI SAU」（招牌，保留拼音加「」） | p21、p22 |
| long cylinders | 長圓筒形 | p22 |
| one or two storeys | 一、兩層樓高 | p24 |
| hun fe bin jin zo de jan li gi | 「hun fe bin jin zo de jan li gi」（保留拼音） | p26 |
| wondered aloud | 喃喃自語 | p26 |
| neck band(s) | 頸帶 | p28、p52、p122 |
| a privacy thing | 是為了隱私 | p30 |
| barely half as many | 還不到現在的一半 | p31 |
| tunnel | 隧道 | p33、p36 |
| a gentle bump, some mechanical noises | 輕輕一震，聽見一些機械聲 | p33 |
| the procedure | 程序 | p33 |
| swap cars?／Swapped cabins. | 換了車？／換了車廂。 | p34、p35 |
| Like a mixnet, but for people. | 就像混合網路，只是換成人。（glossary 定句） | p35 |
| mountain pyramid | 山體金字塔（後文單稱「金字塔」） | p36、p70；p77 起「金字塔」 |
| impressive structure／impressive | 壯觀的建築／壯觀（p37、p39、p43 刻意重複「壯觀」，三處一致） | p37、p39、p43 |
| pre-existing mountain | 一座原本就在那裡的山 | p38 |
| ninety or ninety-nine percent／solid rock | 九成或九成九／實心岩石 | p39 |
| ninety-six point seven | 百分之九十六點七 | p40 |
| one over thirty open space | 空間只占三十分之一 | p41 |
| three times smaller in each dimension | 長、寬、高各縮小三倍 | p41 |
| You got it! | 答對了！ | p42 |
| It *is* the largest | 它*確實*是全哲戈最大的一座 | p43 |
| This is your hotel | 這就是你的飯店 | p45 |
| bag | 包包 | p46 |
| So what's the plan? | 那接下來怎麼安排？ | p47 |
| longhour | 長時 | p48 |
| watch | 手錶 | p49、p51、p58 |
| green circle | 綠色圓圈 | p49 |
| room key | 房間鑰匙 | p51 |
| *Almost everyone* | *幾乎每個人* | p52 |
| front door of the hotel | 飯店正門 | p55 |
| 1565 Tan Kai | 譚凱街 1565 號 | p56 |
| "unknown" | 「未知」裝置（初譯補「裝置」，ch19 手錶把哲戈裝置當未知威脅） | p58 |
| Veridian watch／Dzego electronics | 維瑞迪亞手錶／哲戈的電子產品 | p58 |
| large box | 大箱子 | p59、p60 |
| much smaller white boxes／white boxes | 小得多的白色盒子／白盒子 | p61、p62 |
| tray／top row／second topmost row | 托盤／最上層／第二層 | p62、p63 |
| staircase（p62、p68 的台階） | 一道樓梯的台階／台階上 | p62、p68 |
| two-dimensional codes | 二維條碼 | p62 |
| the man from the store | 店裡出來的男人／店裡的男人 | p62、p63 |
| Shipping／High security. | 運貨。／高安全等級。 | p67 |
| A mixnet for physical objects | 實體物品的混合網路 | p69 |
| carriers | 運送者 | p69 |
| source and the destination | 起點和終點 | p69 |
| *everyone's* device | *所有人*的裝置 | p69 |
| 17th street／0th street | 第 17 街／第 0 街（阿拉伯數字） | p70、p82 |
| pathway leading up to it | 通往金字塔的步道 | p70 |
| neon lights | 霓虹燈管 | p71 |
| flower shop／clothing shop | 花店／服飾店 | p71 |
| privacy robes | 隱私袍 | p71、p77、p122 |
| hastily-added | 倉促補進來的 | p71 |
| unmarked staircase leading to a basement | 沒有標示、通往地下室的樓梯 | p71 |
| two teenage boys and one girl | 兩個少年和一個少女 | p71 |
| electronic gadgets and chemistry lab equipment | 電子小玩意和化學實驗器材 | p72 |
| motto | 標語 | p72 |
| 256 Dzegoban roots／five Dzegoban roots | 256 個哲戈語字根／五個哲戈語字根 | p75、p93 |
| underground tea shop | 地下茶館 | p76 |
| Dzego's medieval era | 哲戈中世紀 | p76 |
| Zin Go／Dzai Gun | 辛戈街／載君街 | p77、p78、p82 |
| tree cover | 樹蔭濃密 | p77 |
| inclined walkway | 斜坡步道 | p77 |
| the incline／the hill | 坡上／山坡 | p78 |
| towering over Pafogai Du | 俯瞰著整座帕佛蓋都 | p79 |
| much more green than Freetown, but still much less green than Veridia | 比自由城綠得多，但還是比維瑞迪亞少綠得多（譯者筆記：保留對比句式；可潤順，但兩端比較都要在） | p79 |
| the path（tree-covered perimeter path） | 綠樹成蔭的美麗步道／步道 | p82、p83 |
| lobby restaurant | 大廳的餐廳 | p85 |
| ten minutes early | 早到了十分鐘 | p85 |
| He took the path less traveled, and that blazed a trail for all. | 他走上人跡較少的那條路，而那為眾人開出了一條道路。（HTML 內，與 ch11 一字不差） | p89 |
| from a Veridian | 一個維瑞迪亞人寫的 | p91 |
| Two percent of the language | 這個語言的百分之二 | p94 |
| People should dream. … pain will fear them. | 人應該做夢。一個人做夢，就不怕痛。十萬人做十萬個夢，痛就怕他們。（glossary 定句） | p95 |
| old poem | 古詩 | p96 |
| blazing trails／fighting here to survive | 開路／在這裡為了活下去而奮戰 | p98 |
| Gladias, meet Fin. | 格拉迪亞斯，這是汾。 | p101 |
| Anyone Zei brings is a friend to me. | 澤帶來的人，就是我的朋友。（譯者筆記定句） | p103 |
| almost half a month | 差不多有半個月 | p105 |
| a worthy answer | 一個像樣的答案 | p106 |
| Bansunpei | 班順派 | p108、p109、p117、p118、p123 |
| optimizing Dzegoban, optimizing the measurement units | 最佳化哲戈語、最佳化度量單位 | p108 |
| education, defense, economic development | 教育、國防、經濟發展 | p108 |
| the day Redshire was attacked | 紅郡遇襲那天（兩處一致） | p109、p118 |
| Dzegoban is coordination training. | 哲戈語是協調訓練。（glossary 定句） | p111 |
| new iteration of Dzegoban | 新一版的哲戈語 | p113 |
| A/B test | A/B 測試 | p114 |
| public feedback | 大眾的回饋（兩處一致） | p115、p116 |
| final product | 最後的成品 | p115 |
| from all walks of life | 各行各業 | p117 |
| *bonuses* | *獎勵* | p117 |
| digitally convened | 在線上召開會議 | p118 |
| unprecedented decision | 前所未有的決定 | p118 |
| Dzegoban version nine | 哲戈語第九版（兩處一致） | p118、p123 |
| basic highlighting changes | 基本的標示調整（譯者筆記：與 worldbuilding「基本標示調整」一致） | p118 |
| audibly sighed with relief | 鬆了一口氣，嘆息聲清晰可聞（譯者筆記定句） | p119 |
| the exact same machinery | 一模一樣的機制 | p121 |
| physical-delivery mixnets | 實體配送混合網路 | p122 |
| ten times more meaningful | 重要十倍 | p122 |
| Bluewhale Messenger | 藍鯨通訊 | p122 |
| almost disappeared … overnight | 幾乎一夜之間就消失了 | p122 |
| three days ago | 三天前（照原文，見第四節） | p123 |
| privacy and security recommendations | 隱私與安全建議 | p123 |
| About five percent of the population／two and a half percent | 大約百分之五的人口／百分之二點五 | p123 |
| start a trend that's now sweeping across all of Dzego | 帶起一股風潮，現在正席捲全哲戈 | p123 |
| Intelligence Score／Emotional Intelligence Scores | 智力分數／情緒智力分數 | p125 |
| nodding along | 點頭稱是 | p125 |
| Coordination Score | 協調分數（p126 兩次） | p126 |
| not a property of a person - it's a property of an entire community | 不是一個人的屬性——而是整個社群的屬性 | p126 |
| positive-sum／zero-sum | 正和／零和 | p126 |
| bad equilibria into better ones | 跳出不良均衡、走向更好均衡 | p126 |
| a strong leader that everyone bows down to | 一個人人都對他俯首稱臣的強勢領袖 | p127 |
| we Dzegojan | 我們哲戈人（兩處一致） | p127 |
| NO | 不！（全大寫→驚嘆號，譯者筆記） | p127 |
| 'gie fe kiu kai ci bin hu' - grow roots, no head | 『gie fe kiu kai ci bin hu』——扎根，無首（與 ch02 口號一致） | p127 |
| no head（句中） | 沒有首腦（兩處；避免「首領」） | p127 |
| no top-down coercion | 沒有由上而下的強制 | p127 |
| improved and perfected our language eight times | 把我們的語言改良、完善了八次 | p127 |
| And we are going to WIN. | 而且我們一定會贏！（全大寫→驚嘆號，譯者筆記） | p127 |

刻意前後呼應（要留住兩端）：

- p28「好多人戴著頸帶」（澤）→ p52「澤說得沒錯。這裡*幾乎每個人*都已經戴著頸帶了」→ p122 汾「戴著頸帶、透過頸帶交談的人變多了多少」。
- p29–p31 黑色專車暴增、p35「就像混合網路，只是換成人」、p69「實體物品的混合網路」、p71 隱私袍 → p122 汾逐項點名（頸帶、隱私袍、黑色專車、實體配送混合網路）：汾的演說是在解釋格拉迪亞斯一路看到的現象，用詞要對得上。
- p23「只有少數幾家店看起來有開」→ p122「不去店裡」。
- p37／p39／p43「壯觀」三處重複（p43 是讓步：「也許你說得對，我們是該覺得壯觀」）。
- p75「256 個哲戈語字根」→ p93「五個哲戈語字根」→ p94「百分之二」（5／256 ≈ 2%，數字不改）。
- p89 古詩第一行＝ch11 賽菈的引句；p97「跟我們那句」、p98「你們是在開路，我們是在這裡為了活下去而奮戰」呼應 trail／blazed a trail。
- p109「紅郡遇襲那天」＝p118「紅郡遇襲那天」。
- p127「扎根，無首」與 ch02 口號一致；「沒有首腦」兩次是口號「無首」的展開。

## 二、本章出現的 bible 譯名（`uv run tools/literary_edit.py terms 18` 產生）

- 人名：Gladias → 格拉迪亞斯（避免：格拉迪斯、葛拉迪亞斯）；Zei → 澤（避免：賊）；Bai → 白；Fin → 汾；Seila → 賽菈（避免：塞拉、席拉）；Gun → 君（terms 命中，但本章原文 Gun 只出現在街名 Dzai Gun，不是人名）
- 地名：Pafogai Du → 帕佛蓋都；Pafogai → 帕佛蓋；Dzego → 哲戈（避免：澤戈）；Dzegoban → 哲戈語；Dzegojan → 哲戈人／哲戈的；Veridia → 維瑞迪亞（避免：韋里迪亞）；Veridian → 維瑞迪亞人／維瑞迪亞的；
  Freetown → 自由城（避免：弗里敦）；Redshire → 紅郡（避免：雷德郡）；Tan Kai → 譚凱街；Zin Go → 辛戈街；Dzai Gun → 載君街；air harbor → 空港
- 組織：Bansunpei → 班順派；Bluewhale Messenger → 藍鯨通訊（Bluewhale → 藍鯨）；the Arctics → 北極人
- 技術：mixnet → 混合網路（避免：混合網絡）；physical-delivery mixnet → 實體配送混合網路；simulated window → 模擬窗（避免：虛擬窗戶）；two-dimensional code → 二維條碼（避免：二維碼）；cabin → 車廂；
  coordination training → 協調訓練；Coordination Score → 協調分數；Intelligence Score → 智力分數（避免：智商）；Emotional Intelligence Score → 情緒智力分數；positive-sum → 正和；bad equilibria → 不良均衡
- 物品：hand device → 手持裝置（避免：手機）；watch → 手錶；compute box → 運算盒（避免：計算盒）；neck band → 頸帶；privacy robe → 隱私袍（避免：隱私長袍）；black car → 黑色專車（避免：黑色車子）；green circle → 綠色圓圈
- 時間：longhour → 長時（避免：長小時）；1 長時＝100 分鐘（p55「四十分鐘＋六十分鐘」＝一個長時，數字自洽，不改）
- 哲戈語拼音（一律保留原樣、大小寫不改）：gie fe kiu kai ci bin hu（扎根，無首）；jan jo san sia（古詩，p89）；hun fe bin jin zo de jan li gi（p26）；MIN KUI、GUI SAU（p21、p22）；p50、p73 的畫面文字
- 一般詞：path less traveled → 人跡較少的那條路
- terms 列出但本章不用：pin → 球瓶（本章無此詞，是誤命中）；dun（誤命中 man dun li jie hu 的拼音）

## 三、人物口吻與稱謂

- 稱謂：本章沒有鄧、蘇、穆出場，**不適用**澤對鄧／蘇用「您」的規則。本章全章沒有「您」，也不要加。
  - 澤、白、汾 → 格拉迪亞斯：直呼「格拉迪亞斯」，用「你」（characters 稱謂表：哲戈青少年對外國大人，隨和有禮，不用「您」）。
  - 格拉迪亞斯 → 澤、白：「你們」（初見面的年輕人，隨和）；→ 汾：「你」。
  - 澤、白、汾之間：互用「你」；白 → 汾「你」（p105）；汾 → 眾人「你們」（p106、p108、p122）。
  - 運貨的男人 → 格拉迪亞斯：只有兩個短句，不用代名詞（p67）。
- 格拉迪亞斯：初到哲戈，好奇、愛觀察、愛用數學想事情（p41 心算容量）；對話簡短隨和；內心記事帶自嘲（p75「真的得學起來了」）；p93 自嘲只認得五個字根，笑著說。
- 澤：當導遊，解說清楚、帶點技術腔（p15–p16 模擬窗、p35 換車廂）；p40 精確糾正「百分之九十六點七」；p119 鬆一口氣（他在意明盤台／語言改版的負擔）。
- 白：禮貌而活潑（p6「沒錯！」）；p94 俏皮算比例；p98 以「我們在這裡為了活下去而奮戰」回應，語氣成熟；女性（p99 she）。
- 汾：久違現身，先道歉（p106），演說從說理（p108–p117 條列）一路推到激昂（p124 起越講越激動，p127 宣言）；保留由長句轉短句的節奏，大寫 NO／WIN 用驚嘆號，不加斜體。
- 運貨的男人：極簡、匆忙（「運貨。」「高安全等級。」）。
- 說話者（**原文未標說話者的輪次一律照初譯，不補標籤**）：
  - p5 格拉迪亞斯（未標）、p6 白、p7 格拉迪亞斯（未標）、p8 澤或白（未標，初譯不點名）；
  - p14 格拉迪亞斯、p15 澤、p16 澤（續上段，未標）、p17 格拉迪亞斯（未標）；
  - p26 澤（自言自語）、p27 格拉迪亞斯、p28 澤（未標，解釋自己剛說的話）；p30 格拉迪亞斯、p31 澤或白（未標，初譯不點名）；
  - p34 格拉迪亞斯（未標）、p35 澤或白（未標）；p37 格拉迪亞斯、p38 澤或白（未標）、p39 格拉迪亞斯（未標）、p40 澤或白（未標）、p41 格拉迪亞斯（未標）、p42 澤或白（未標）、
    p43 澤或白（未標；譯者筆記與 QA 都定為「不點名」）；p45 澤或白（未標）、p47 格拉迪亞斯（未標）、p48 澤或白（未標）；
  - p66 格拉迪亞斯、p67 運貨的男人；
  - p87 格拉迪亞斯、p90 白（未標，她剛把螢幕拿給他看）、p91 格拉迪亞斯（未標）、p92 白（未標）、p93 格拉迪亞斯、p94 白、p95 白（未標，說出古詩釋義）、p96 白（未標；也可能是澤，初譯不點名）、
    p97 格拉迪亞斯（未標，「我們那句」＝維瑞迪亞的句子）、p98 白（未標；p99「她話才剛說完」確認）；
  - p101 澤（未標，他認出汾並拉椅子）、p102 格拉迪亞斯（未標）、p103 汾（未標）、p104 格拉迪亞斯（未標）、p105 白、p106 汾（未標）；
  - p108–p109 汾、p110 澤、p111 汾（未標）、p113–p118 汾（未標）、p121–p123 汾（未標）、p125–p127 汾（未標）。
- p119–p120 是敘事插段（澤鬆一口氣、格拉迪亞斯的理解），汾的話在 p121 接續；不要把 p120 寫成汾的話，也不要把 p121 併進敘事。

## 四、伏筆與資訊邊界（不可加暗示）

- p3：穿過「密封的出口」，出口另一頭「直接」連著專車——乘客不暴露（worldbuilding 門對門密合），不補說明。
- p4：澤和白「已經」坐在車裡；座位方向照原文。
- p6：白「沒錯！」——原文 indeed，活潑。
- p11：格拉迪亞斯越過澤看右側窗戶（伏筆：p16 模擬窗只追蹤一個人的眼睛，選了澤）。
- p13：「馬上」察覺；景色隨車子動、不隨他的身子動——只寫現象，不先說破。
- p15：「可以是」；提高了安全規格、黑色專車「改了設定」；就算調暗光還是雙向的，「好一點的」攝影機就看得到；所以「現在」是模擬窗。
- p16：「其實」一個人的時候效果很好；也會追蹤眼睛；兩個人時「它選了我」。
- p18：挪了幾次身子試試；顏色和景深「有點不太自然」（原文 seemed somewhat unnatural，初譯省了 seemed，可補「看起來」，不可加強）；除此之外「意外地正常」；仔細留意外頭一切。
- p19：格拉迪亞斯「一個字也看不懂」（could not understand at all）——對照 p75、p93 他還不懂哲戈語。
- p20：「短暫」瞥見（briefly）。
- p23：「出乎他意料」；「只有少數幾家店看起來有開」（seemed）——不要說成「都關了」，也不先解釋原因（p122 由汾揭曉）。
- p24：一、兩層樓高；「許多」樓梯通往地下（伏筆 ch24 轉入地下，不補）。
- p25：人比維瑞迪亞「少」，「儘管」帕佛蓋都看得出來比他家鄉密集得多（visibly greater density）。
- p26：澤 wondered aloud——自言自語，不補他的心情。
- p29：「一大堆一模一樣的」黑色專車。
- p31：「現在想想，不是」；「已經有一陣子」；這麼多人用「倒是最近的事」；「就在幾天前」還「不到現在的一半」（barely half as many）——與 p123「三天前」呼應，不要改數字。
- p32：三人「默默地」繼續坐車——原文只寫 silently，不補氣氛。
- p33：「幾分鐘後」；開到一半慢下、停住；輕輕一震、機械聲、車子「似乎」朝各方向移動（往上、往旁邊，再往下）；朝窗外看「什麼也看不到」；「大約半分鐘後」程序結束；車子「似乎」又開始加速（appeared）。
- p34：格拉迪亞斯的猜測帶刪節號「我們剛才……換了車？」，保留遲疑。
- p35：系統等「十輛車」到齊、「隨機」交換車廂、大家再開出去；在出口盯著的人「誰也不知道」我們在哪一輛。
- p36：「不到一分鐘」駛出隧道；「不久」金字塔出現；山體金字塔在帕佛蓋都「南邊」。
- p37：「那……真是壯觀的建築」——刪節號是格拉迪亞斯一時語塞，保留。
- p38：「嘿，大家都這麼說」；是從一座原本就在那裡的山鑿出來的。
- p39：「大概」也比較安全吧，「如果」裡面有九成或九成九是實心岩石的話——格拉迪亞斯的推測。
- p40：精確「百分之九十六點七」。
- p41：數字照原文（1/30 空間；一般建築一成實心；長寬高各縮小三倍＝27 倍＝3³），問句語氣（格拉迪亞斯在心算求證）保留。
- p43：「也許」你說得對；*確實*是全哲戈「最大」的一座。說話者不點名。
- p44：「不久」停下；車門「直接」通進飯店。
- p48：「先休息一個長時」，再回這裡碰面。
- p50（HTML）：入住畫面全為哲戈語，不解釋。
- p51：手錶震動；拿到房間鑰匙——只寫這兩件事。
- p52：「他這才發現，澤說得沒錯」；*幾乎每個人*（斜體保留）「已經」戴著頸帶。
- p55：「只」休息了四十分鐘；還有「六十分鐘」；「至少」親眼看看這「一小塊」地方。
- p58：「幾乎才剛起步」；「未知」裝置的數目「到了兩位數」；他「猜」只是維瑞迪亞手錶跟不上哲戈電子產品，決定不理會——不要暗示危險，也不要先說出真相（ch19 才由澤解釋是保全無人機等哲戈裝置）。
- p59：一輛黑色專車「幾乎馬上」慢慢停下；男人抱一個大箱子。
- p60：司機是女性（her、she）；她的箱子「大小一模一樣」。
- p61：「幾公尺外」；最上層「大約三十個」小得多的白色盒子。
- p62：男人「似乎一次就」掃描了所有白盒子的二維條碼（seemed…simultaneously）。
- p64：「又重複了五次」（共七層，不要改成「五層」）；然後司機打開男人的箱子，也一層一層掃描。
- p65：每掃完一層就放進自己的箱子；最後搬回車上開走。
- p68：「匆匆」走回店裡、「鎖上了門」——不補他的心理。
- p69：「這才明白」；「澤跟他提過一次」；每件物品經過「好幾個」運送者；「沒有任何一個人」同時知道起點和終點；想破壞某一人的裝置「就只能」破壞*所有人*的裝置——而真要這麼做「很快」就會被抓到。
- p70：第 17 街右轉；金字塔「就在前方」；「再過兩條街」就是步道起點（譚凱→辛戈→載君，p78、p83 吻合）。
- p71：開著的店「多得多」；招牌「大約一半」精緻專業、另一半霓虹燈管臨時手工拼成；花店客人「依舊」絡繹不絕；「大約二十公尺」（兩次）；服飾店海報「還在」打夾克廣告，「大約一半」空間改擺「倉促補進來的」隱私袍；沒有標示的地下室樓梯，兩個少年和一個少女往下走——不要猜他們去做什麼。
- p72：招牌畫可愛卡通動物玩電子小玩意和化學器材，綠樹藍天背景；正中間一句哲戈語標語（p73 不解釋）。
- p74：只是「好奇」這些字的意思。
- p75：心裡記一筆：256 個字根，「既然人都來了」真的得學——冷面自嘲，不加戲。
- p76：「大約二十公尺」；「看起來像是」地下茶館（seemed like）；裝飾風格讓他想起小時候看過描繪哲戈中世紀的圖畫。
- p77：「不久之後」到辛戈街；樹蔭濃密到看不見前方的金字塔；路口暫時打斷樹列；「許多人」沿斜坡步道上上下下，「大多數」穿隱私袍；他「好奇」這些人在忙什麼——不要給答案。
- p78：載君街是山坡開始之前的「最後一條街」。
- p79：「大約五分鐘後」；「幾乎所有」建築的屋頂；比自由城綠得多、比維瑞迪亞少綠得多（兩端都保留）。
- p80–p81：坐在大石頭上欣賞風景；「幾分鐘後」往下走——不補心境。
- p82：左轉，沿城市邊緣走到「最西端」；環繞整座城市的「似乎」是一條林蔭步道（seemed）；「許多人」散步、跑步；第 0 街在西緣，步道轉向北方。
- p83：往北走「兩條街」回到譚凱街，往東回飯店。
- p85：一進門就「左轉」；早到「十分鐘」；澤和白「已經」坐著看一台手持裝置；白抬頭揮手。
- p89（HTML）：古詩，`<pre>` 不動。
- p91：「第一句是一個維瑞迪亞人寫的」——不點名作者（ch11 是「維瑞迪亞古代作家」）。
- p93：「還不知道」（Not yet）；「大概只認得五個」字根，笑著說。
- p94：「已經」是百分之二。
- p95：古詩釋義照 glossary 定句，不改句式（「人應該做夢」「痛就怕他們」）。
- p97：「沒有差太多」——保留低調的說法。
- p98：「確實」；「只不過」你們是在開路、我們是在這裡為了活下去而奮戰——不加悲情形容。
- p99：「話才剛說完」；澤和白「同時」轉身，朝「正跑向這桌的人」揮手。
- p100：澤「馬上」認出他，把「剩下的那張椅子」拉出來。
- p102：賽菈「跟我說過」澤講了汾很多好話（Seila mentioned）——轉述鏈不要簡化。
- p105：「差不多有半個月」沒見到你了「吧」（I think）。
- p106：「真的很抱歉」這麼久都沒理你們；「我終於覺得」我能給一個像樣的答案。
- p107：三人「全都」轉頭盯著汾。
- p108：「你們也許一直在想」（might have been wondering）；列舉「教育、國防、經濟發展」。
- p109：「好幾年來」自己也在想；「直到」紅郡遇襲那天的班順派會議「才終於」找到答案。
- p112：澤和白「都張開了嘴」——只寫動作，不補「驚訝」。
- p114–p116：兩件事的論證每一步都要在（大眾回饋→成品根據真實的人實際這樣做後「哪些做法真的行得通」；許多人在不同面向、許多選項之間選擇→更容易接受；「沒有人會被嚇到」；不同意的人身邊「幾乎都」認識更喜歡的人，「至少」可以聽聽觀點）。
- p117：「刻意」從各行各業吸收；招募到「組織裡其他人都不認識的人」「還真的」會拿到*獎勵*（*bonuses* 斜體保留）。
- p118：「前所未有」；「至少在目前」（At least for the time being）暫停第九版；只發布幾項基本標示調整，「一年多前」就已達成共識；除此之外什麼都不發布。
- p119：澤鬆一口氣，嘆息聲「清晰可聞」——不補理由。
- p120：格拉迪亞斯「能理解」；「過去這一個月」每個人都很緊繃；「實在不是好時機」——原文 hardly a good time。
- p121：「一模一樣的機制」；「只是」因為情況特殊、時間緊迫，大眾參與「比較少」、保密「比較高」；在全哲戈協調「一套完全不同的改變」。
- p122：問句清單（頸帶、隱私袍、黑色專車、實體配送混合網路網購）一項不少；比這些「重要十倍」的是「你們看不到的部分」——敏感會議「乾脆」改到線上，網路上用的工具也「安全多了」；藍鯨通訊「幾乎一夜之間」就消失了。
- p123：「三天前」這些事「都還沒有發生」——與 p31「幾天前」吻合，但與紅郡遇襲（火月 17 日，約一個月前）及 p120「過去這一個月」不完全吻合；譯者筆記與 QA 定為照原文譯「三天前」，不要改、不要調和。「大約百分之五」同時看到；他們很意外，但讀了、理解了道理、尊重做決定的人；「過半數」已經「至少在一件大事上」改變做法；「光是這百分之二點五」就足以帶起風潮。
- p124：汾「越講越激動」（grew even more excited）。
- p125：北極人「老是在講」智力分數、社會應交給分數最高的人；「有幾個」維瑞迪亞學者說也應該認真看待情緒智力分數——「只不過」他們「向來很難」讓大家除了點頭稱是之外真的做點什麼（反諷保留，不加重）。
- p126：第三種「完全漏掉了」；協調分數三個能力（集體決定；選正和合作而非零和競爭，「就算」對個人有風險；跳出不良均衡走向更好均衡）一項不少。
- p127：北極人「認為」只有強勢領袖做得到；「不！」；口號照 glossary；「改良、完善了八次」（第九版尚未發布，八次不改）；「沒有由上而下的強制、沒有首腦」；「而且我們一定會贏！」——宣言口吻保留，不加斜體、不加原文沒有的煽情詞。
