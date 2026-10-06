# 第 12 章 bible 摘錄（第二輪文學編輯用）

主 Agent 依 WORKFLOW「開始一章前」第 5 步建立；每個 chunk 的資料包都附上這份（`literary_edit.py packet --bible`）。
權威來源仍是 glossary／characters／worldbuilding；這裡只是本章會用到的部分，加上本章初譯已定的用詞。
段號為原文段號（`literary_edit.py plan 12` 的 pNNN；與 `translation/notes/chapter-12.md` 的段號相同）。

章節結構：p3–p41 抵達薩祖都（列車、蘇、黑色專車、市景、飯店；p6、p27 哲戈語招牌，p37 手錶畫面，其後是英文釋義段 p7、p28、p38）｜p42 分隔｜
p43–p63 早晨、車上讀雜湊函數（p51 教科書圖）、爆炸現場｜p64 分隔｜p65–p95 開幕：德盧因、蘇、金總督導、賽制｜p96 日期分隔（草季 25 日）｜
p97 通話畫面｜p98–p134 白來電、到等候室見柏｜p135 分隔｜p136–p161 進場、六角格規則、摸索｜p162 `>` 引言（教科書句）｜
p163–p190 時間反向推導、開戰｜p191 棋盤 SVG｜p192–p196 獲勝。

## 一、全章固定用詞（editor 一次只看一個 chunk，看不到別處的叫法；這些不要換）

| 原文 | 本章用法 | 出現位置／說明 |
|---|---|---|
| train／station／passengers | 列車／車站／乘客 | p3–p13 |
| sign | 招牌 | p5、p26 |
| "Main city", helpfully-named capital | 「主城」——哲戈的首都，名字取得一目了然 | p7（譯者筆記） |
| maximize the quality of his time | 把這段時間的品質最大化 | p9（保留數理腔） |
| game of Minpentai against a bot | 跟 AI 把一局明盤台下完 | p9 |
| harness to fine-tune the AI | 訓練框架，好把 AI 微調 | p10 |
| custom rulesets／stock AI | 自訂規則／原版 AI | p10 |
| resigned | 投降 | p11、p92 |
| one-on-three／three-on-one | 以一敵三／三打一 | p11 |
| training data | 訓練資料 | p11 |
| cannibalized each other's negentropy | 互相蠶食彼此的負熵 | p11 |
| Minpentai priest robes | 明盤台祭司袍 | p14 |
| lead priest | 帶頭的祭司 | p15 |
| organizers of the nationals | 全國賽的主辦人之一 | p17 |
| itinerary | 行程 | p19 |
| hotel／orientation | 飯店／說明會 | p20 |
| thirty-two contestants | 三十二名選手 | p20、p92 |
| black car | 黑色專車 | p21、p48 |
| chip fab | 晶圓廠 | p21（回溯 ch09） |
| half a longhour | 半長時 | p22、p44 |
| electronics stores／medicine stores／health stores | 電子用品店／藥店／保健店 | p25、p29 |
| longevity package | 長壽套組（「長壽套組，本店有售」） | p28 |
| artistic furniture and other household items | 藝術家具和其他家居用品 | p29 |
| tea houses／medieval era | 茶館／中世紀 | p30 |
| mountain pyramids | 山體金字塔 | p31、p66、p90 |
| tunnel | 隧道 | p33、p65、p125 |
| green circle | 綠色圓圈 | p36、p68 |
| Reputation above 150 verified ... room number is 304 | 信譽 150 以上，已驗證。無需付款。核准，房號 304。 | p38（裝置畫面釋義） |
| room key | 房間鑰匙 | p39 |
| 30,003 | 30,003 | p44 |
| commencement ceremony | 開幕典禮 | p44 |
| room service menu | 客房服務選單 | p44 |
| fruit and vegetable juice | 蔬果汁 | p44、p123 |
| venue | 會場 | p46 |
| lobby | 大廳 | p48 |
| cryptography textbook | 密碼學教科書 | p49 |
| hash functions／hash algorithm | 雜湊函數／雜湊演算法 | p50–p57、p163 |
| "Conception of a hash algorithm" | 「雜湊演算法的構想」 | p52 |
| shrunken fingerprint | 縮小的指紋 | p54 |
| infeasibly hard | 難到實際上做不到 | p54 |
| paradox | 弔詭 | p55 |
| *entropy-preserving* transformation: a permutation | *保持熵*的變換：置換 | p55 |
| core building block | 核心的構件 | p56、p162 |
| one-to-one／forwards and backwards | 一對一／正向、反向 | p56、p162 |
| deletion, and an xor | 刪掉一部分，再……做一次 XOR | p56 |
| round function | 輪函數 | p57 |
| about half the entropy collapses | 大約一半的熵就會崩塌 | p57 |
| It's all entropy, isn't it | 一切都是熵，不是嗎？ | p59 |
| safety tape | 警戒膠帶 | p60 |
| advanced biology research lab | 高等生物研究實驗室 | p62 |
| Probably the Arctics, as usual | 八成又是北極人幹的 | p62 |
| hallway | 走廊 | p63、p126 |
| stone bricks／arch／two horizontal arms ... clashing fists | 石磚／拱形／兩條橫放的手臂在中間相會，拳頭相抵 | p66（回溯 ch02） |
| Minpentai room（帕佛蓋都） | 明盤台廳 | p66（譯者筆記） |
| contestants | 選手 | p69 起 |
| stage | 台上 | p69 |
| De lu hin／'A fork with the appearance of' | 保留拼音；「『有著……外表的叉子』」 | p79 |
| foreign contestant | 外國參賽者／外國選手 | p81、p89 |
| national Minpentai championship | 明盤台全國錦標賽 | p85 |
| Taskmaster Jin | 金總督導 | p86 |
| Minpentai museum | 明盤台博物館 | p90 |
| tourist excursions | 觀光行程 | p90 |
| qualifying games／round | 資格賽；一輪資格賽 | p91、p92 |
| semifinals | 準決賽 | p92 |
| geometric average／inverse | 幾何平均／倒數 | p92 |
| eight thousand turns | 八千回合 | p92 |
| temporary competitors | 暫時的對手 | p93 |
| shared project | 共同事業 | p93 |
| requesting to call | 想跟他通話 | p98 |
| Pafogai | 帕佛蓋（白的口語簡稱） | p106 |
| live stadium | 現場場館 | p114 |
| practice game | 練習賽 | p122 |
| entrance to the pyramid | 金字塔的一個入口 | p124 |
| large stone brick door | 大石磚門 | p126 |
| waiting room | 等候室 | p126 |
| elevator | 電梯 | p136 |
| giant room | 巨大的廳室 | p137 |
| giant console with a chair | 一座附有座椅的巨大主控台 | p137 |
| cheating equipment | 作弊用的設備 | p139 |
| automated voice | 自動語音 | p140、p151 |
| fourth qualifying match of the north stadium | 今天北場館的第四場資格賽 | p146 |
| Zei Leimin／Bo Zume | 澤・雷明／柏・祖美 | p146 |
| rule change | 規則變化 | p147 |
| hex grid／hexgrid | 六角格 | p147、p157、p166 |
| structures／spaceships／walls | 結構／太空船／牆 | p149 |
| serene battle over a field of snowflakes | 雪花原野上的寧靜之戰 | p149 |
| display | 顯示畫面 | p150 |
| hexagonal grid | 六角形網格 | p150 |
| The battle begins in N ticks | N 拍後開戰 | p151、p155、p158、p168、p178 |
| sandbox | 沙盒 | p152 起 |
| static structures | 靜態結構 | p152 |
| directly east | 往正東走 | p152 |
| see what sticks | 看看哪些管用 | p153（譯者筆記） |
| symbol | 印記 | p156 起 |
| intervention turn | 干預回合 | p156、p189、p193–p195 |
| rock formations | 岩塊 | p157 起 |
| offset | 位移 | p159 |
| fruitless exploration | 白忙 | p161 |
| truncate-and-xor wrapper | 一層截斷再 XOR 的外殼 | p163 |
| desired end state | 想要的最終狀態 | p163 |
| play it backwards | 倒著播放 | p163、p164 |
| internal permutation | 內部的置換 | p165 |
| invert each step | 把每一步反轉 | p165、p170 |
| timestep／time step | 時間步 | p167、p170 |
| triangles／tiling | 三角形／分割 | p169、p170 |
| clockwise／counterclockwise | 順時針／逆時針 | p169 |
| 120-degree／240 degrees | 一百二十度／兩百四十度 | p170 |
| A, B, A, B, B | A、B、A、B、B | p171 |
| video game cheat code | 電玩的作弊密技 | p171 |
| Basic test passed. | 基本測試通過。 | p174 |
| sampled（that particular history） | 取樣到的那段歷史 | p176 |
| bare rock formation | 光禿禿的岩塊 | p177 |
| glider factories | 滑翔機工廠 | p188 |
| home base | 主基地 | p189、p193、p194 |
| gliders that move vertically | 會垂直移動的滑翔機 | p192 |

## 二、本章出現的 bible 譯名（`uv run tools/literary_edit.py terms 12` 產生）

- 人名：Zei → 澤（避免：賊）；Zei Leimin → 澤・雷明；Fin → 汾；Bai → 白；Mu → 穆；Den → 鄧；Su → 蘇；Jin → 金；Deluin → 德盧因；Bo → 柏；Bo Zume → 柏・祖美
- 地名：Sadzu Du → 薩祖都；Pafogai Du → 帕佛蓋都；Pafogai → 帕佛蓋；Dzego → 哲戈（避免：澤戈）；Redshire → 紅郡（避免：雷德郡）
- 組織與制度：Minpentai → 明盤台；priests → 祭司（避免：牧師、神父）；Taskmaster → 總督導；qualifying games → 資格賽；Bansunpei → 班順派；
  Minpentai museum → 明盤台博物館；north stadium → 北場館
- 技術：entropy → 熵；negentropy → 負熵；hash → 雜湊（避免：哈希）；hash function → 雜湊函數（避免：哈希函數）；permutation → 置換；xor → XOR（避免：異或）；
  round function → 輪函數；entropy-preserving → 保持熵（避免：熵保持）；time step → 時間步（避免：時間步驟）；hex grid → 六角格；geometric average → 幾何平均；
  training data → 訓練資料（避免：訓練數據）；harness → 訓練框架；reputation → 信譽（避免：聲譽、名聲）；fab → 晶圓廠
- 物品：hand device → 手持裝置（避免：手機）；watch → 手錶；green circle → 綠色圓圈；black car → 黑色專車（避免：黑色車子）；longevity package → 長壽套組
- 明盤台：glider → 滑翔機（避免：滑翔翼）；rock formation → 岩塊；symbol → 印記；intervention turn → 干預回合；sandbox → 沙盒；home base → 主基地（避免：大本營）
- 時間：longhour → 長時（避免：長小時）；tick → 拍；Grasstime → 草季（避免：草月）
- 哲戈語：Dze go ba fau gie、MU GU GEI FA、LE MU GEI FA、PA GU GEI FA、LE FI SHI GEI TAU FA、PA MU GU GU GEI TAU FA、FI SHI GEI TAU FA、MU FI LE GEI TAU FA、
  FI LE GEI TAU FA、MU GU GEI TAU FA、PA GU……SO……BI……ZE……HA……MU……FO……SHI……LE……PA……、TAU FA、De lu hin——全部保留拼音；
  原文有附英文釋義的才譯；原文倒數後有句點的保留「。」，沒有的不加（譯者筆記）。

## 三、人物口吻與稱謂

- 澤：數理腦、條理分明，內心帶冷幽默（p9「把這段時間的品質最大化」、p59「一切都是熵，不是嗎？」、p171「而在某種意義上，這裡還真的就是」）；
  對初見面的長輩蘇用「您」（稱謂表）；對德盧因、柏、白用「你」；p101 對白抱怨口吻。
- 蘇：年長女性、接待人員式的親切，事務性；對澤用「你」。
- 金總督導：致詞口吻，正式、莊重，用「各位」「你們」。
- 德盧因：開朗自嘲的少年口吻；「我從紅郡來的。名字讓我露餡了，對吧？」。
- 柏：**全章沒有代名詞**，譯文也完全避開他／她（譯者筆記）。
- 白：口吻已轉為關心、仍帶點損人（p115「你讓我進去不就好了。」）。
- 司機（p62）：平實口語。
- 自動語音（p140 起）：哲戈語保留拼音，後面的英文釋義譯成中文短句。p146–p149 是主持播報，正式口吻。
- 一個說話輪次一段。說話者：p15 蘇、p16 澤、p17 蘇、p18 澤、p19 澤、p20 蘇、p22 蘇、p23 澤；p61 澤、p62 司機；p72 德盧因、p74 澤、p75 澤（問德盧因從哪來）、
  p76 德盧因——**原文未標說話者的輪次一律照初譯，不補標籤**；p79 德盧因、p80 澤、p81 德盧因、p82 澤、p83 德盧因；
  p85–p86 蘇、p88–p93 金總督導、p94 選手齊聲、p95 金總督導；p100 白、p101 澤、p103 澤、p104 白、p105 澤、p106 澤、p107 白、p109 澤、p110 白、p111 白、
  p112 澤、p113 白、p114 澤、p115 白、p117 白、p118 澤、p119 白、p120 澤、p121 白、p122 白；p128 蘇、p129 柏、p130 澤、p131（未標，可能蘇或柏，不補）、p133 澤、p134 蘇。

## 四、伏筆與資訊邊界（不可加暗示）

- p4：先看到樹、建築越來越密、幾分鐘後看到車站——順序保留。
- p9：「決定不急著搶第一個下車」；「大約兩分鐘」。
- p10：汾「一直沒抽出空」寫訓練框架（never gotten around to）。
- p11：「就在這時」；他「把對局調成」只佔一個角落；「即使如此」；他「發現」三打一「根本沒多大幫助」（did not even help that much）。
- p13：「幾乎都下車了」。
- p15：蘇「年紀和穆差不多」——不暗示兩人有關（ch31 穆：「Don't you dare mix me up with Su」）。
- p16：「這才是我第二次來首都」（Only my second time）。
- p21：和幾個月前鄧載他去晶圓廠的那輛「一模一樣」。
- p25：「有些地方看起來跟帕佛蓋都差不多」；電子用品店較少、店家種類多；幾家藥店。
- p31：右手邊建築「一度完全中斷」（For a moment）；金字塔「大約只有」帕佛蓋都南邊那座的一半高。
- p34：車門緊貼另一扇門，把澤完全遮住——不論車外還是他要走進的建築外。
- p46：「至少足夠讓他撐到會場」的自我修正保留。
- p54–p57：教科書說明文體。p55「弔詭」、*保持熵* 強調；p56 *有效率地* 強調；p57「大約一半」「最好還是」；p57 原文 "going that" 是 "doing that" 筆誤，照意思譯（譯者筆記）。技術說明，不補畫面。
- p61：刻意放大音量，讓司機「絕對聽得出」是在問他。
- p62：「八成又是北極人幹的」（Probably, as usual）——推測語氣保留；「好幾天」。
- p67：明顯大得多、維護得更好、裝飾更氣派。
- p69：「大約」五十張椅子、「大約」二十名選手。
- p71：「年紀稍大的少年」（older teenage boy）。
- p73：澤心想「這名字不太像哲戈人」——內心。
- p85：「我深感榮幸」。
- p88：「數百萬名」收看的哲戈人。
- p90：今天參觀博物館；明天觀光、晚上休息；「再過兩天」第一批對局開始。
- p91：六輪資格賽，每場之間休息八天。
- p92：tie-break 規則的數學內容（幾何平均、落敗前撐過的回合數、贏下所需回合數的倒數、上限八千回合、因此八千回合前投降沒有好處、仍同分加一輪）一項都不能少；可以先給直覺再補細節。
- p93：「不是敵人，只是暫時的對手」；「同樣重要的是」。
- p101：「離我的鬧鐘響還有十九分鐘」。
- p102：澤「頓了一下」，決定還是回答。
- p103：三天前的展覽「很精彩」（Very fascinating）；隔天逛薩祖都；認識一個紅郡來的人。
- p107：「過去這一個長時」都在河對岸盯著金字塔。
- p109：「你在*這裡*？」（原文全大寫，譯者筆記改用強調）。
- p110：「鄧的人」找上她、要她記下所有選手的戰術——不加解釋。
- p114：「我……應該不用吧」（I... think I'm fine）；「我想你也買不到」（I doubt）。
- p117：「我們都替你加油！」（We）。
- p119：「大概」（I guess）在忙班順派的事。
- p126：幾百公尺、幾個彎；三天前「根本沒注意到」的走廊。
- p133：不能上網、等其他人比完、不會提前知道新規則——推測問句。
- p137：四分之一分鐘；比帕佛蓋都那間「大得多」；「看起來大約」五千到一萬人（seemed）。
- p138：「隱約看得到」柏的身影（could make out）。
- p139：「大約是三倍多」、形狀和大小更多樣、「大約二十拍」。
- p140：聲音「這次聽起來比較像女聲」（more female）。
- p141：內心推理：這場不是決定性的；但換個角度，這點讓他更害怕——有了「輸了也沒關係」的藉口，腦子還會有足夠動力嗎？問句保留。不補畫面。
- p147：「對觀眾來說或許已經聽太多次了」（perhaps one time too many）。
- p148：驚訝得張大了嘴。
- p152：「不到一分鐘」；「讓他意外的是」跑最快的滑翔機……是往正東走的（停頓保留）。
- p156：*點什麼* 強調保留；不然只能在每個干預回合一再建新印記，進展非常緩慢。
- p157：「猜了幾種」岩塊「可能」長什麼樣子。
- p159：開始冒汗；「到目前為止，一無所獲」；滑翔機、看似合理的岩塊形狀、位移三者組合都沒用。
- p161：「又白忙了兩分鐘」；「不到兩長時前」讀的教科書。
- p162：`>` 引言照 p56 譯文前兩句，但**原文引言整句是斜體、沒有另外強調 efficiently**，譯文不另加強調（譯者筆記）。
- p163：和雜湊函數「不同的是」沒有截斷再 XOR 的外殼；「只要他知道……他只需要……」的停頓。
- p166：「澤生平第一次接觸的」六角格規則。
- p167：翻轉、旋轉六十度、晚一個時間步再發射——「全都不行」。
- p169：每一步分割成三角形；一格填滿順時針、兩格填滿逆時針。
- p170：反轉步驟逐項保留：讓每個時間步發生兩次（一百二十度的反向＝兩次一百二十度）；分割每步位移的問題；往前一步→時間往回一步→往前第二步（總旋轉兩百四十度）→時間往回*兩*步→換回*前一種*分割。兩處強調保留。技術說明，可以先給直覺、可以拆段，但不可少一步。
- p171：一個按鈕往前播一步、兩個按鈕調整時間（往前或往後）；A、B、A、B、B；「而在某種意義上，這裡還真的就是」。
- p173：過程很累人、手指很快就痠了；但成功了。
- p176：第一次失敗的情況照原文（相撞、同一個印記在幾步之外重新成形、滑翔機飛走；所以那段歷史裡印記本來就在）。
- p177：換一架滑翔機成功；越過相撞那一刻後「岩塊加印記」變回光禿禿的岩塊、兩架滑翔機飛出去。
- p179：完全不理會倒數；直到另外兩種「最自然」的岩塊形狀也找到。
- p182：對自己的速度有點意外；「心底幾乎立刻」明白：想出要部署什麼才是難的，部署只是複製貼上。
- p186：起初，什麼事也沒發生。
- p187：五百回合後。
- p189：第一個干預回合時「還沒想出來」；又從主基地送出好幾架；也從新印記附近往東送。
- p190：觀眾、河對岸的白、遠方的汾、穆和鄧都在看——不加情緒。
- p192：觀眾「這才發現」兩名選手都沒找出會垂直移動的滑翔機（they realized）。
- p195：朝三個看得見的印記發射，另外往附近多送一些「以防萬一」。
- p196：不到三百回合。
- 不預示：德盧因 ch15 受困紅郡、ch19 父母同情北極；穆與蘇的關係；白替鄧做事的後續。

## 五、數值（照原文）

- p9 大約兩分鐘；p11 以一敵三、一個角落、三個角落；p14 六個人；p16 第二次；p20 三十二名；p22 半長時。
- p31 大約一半高；p32 一分鐘後；p34 幾分鐘、幾個轉彎。
- p37–p38 信譽 150、房號 304（裝置畫面與釋義）。
- p44 30,003、半長時；p46 三分鐘後。
- p57 大約一半的熵。p60 一分鐘後；p62 好幾天；p63 幾分鐘後。
- p69 大約五十張椅子、大約二十名；p70 十五分鐘；p81、p89 四名／四位外國選手；p88 數百萬名。
- p90 今天、明天、再過兩天；p91 六輪、八天；p92 三十二位、四位、八千回合。
- p97 23098（裝置畫面）；p101 十九分鐘；p103 三天前；p107 一個長時。
- p123 幾分鐘後；p124 二十分鐘後；p126 幾百公尺、三天前；p133 一個長時；p134 一分鐘後。
- p136 一長時後；p137 四分之一分鐘、五千到一萬人；p139 三倍多、大約二十拍；p140 五十拍。
- p149 二十分鐘；p151 兩千拍；p152 不到一分鐘；p155 一千五百拍；p158 一千拍；p161 兩分鐘、不到兩長時；p167 六十度；p168 五百拍；
  p170 一百二十度、兩百四十度、兩步；p178 一百拍；p187 五百回合；p193–p195 第二、第三個干預回合、三個印記；p196 三百回合。

## 六、補畫面注意

- 適合補的場景：p3–p5 列車減速（聲音、窗外光線）；p8 車門打開、乘客起身（聲音、動態）；p14 月台；p24–p33 車窗外市景（光線、動態；**不新增店家種類或建築**）；
  p35–p36 飯店；p43–p48 早晨、下樓上車；p60 爆炸現場（不新增車輛種類或傷亡）；p65–p70 隧道、石門、會場入座（人聲）；p84 鈴聲；
  p98–p99 被通話吵醒；p123–p127 前往等候室；p136–p139 電梯、巨大廳室、無人機（觀眾聲、無人機嗡嗡聲已在原文，不重複）；p186–p196 比賽過程（觀眾反應）。
- 不補：所有對話內容；p11 AI 推理；p54–p57 教科書；p141 內心；p152–p183 摸索與推導（技術與內心推理，連冒汗、手指痠都已是原文，不再加）；p92 賽制說明。
- 不補任何預示（見四）。
- p190「而在遠方，汾、穆和鄧也一樣」是一場的落點，不加補畫面去稀釋。
