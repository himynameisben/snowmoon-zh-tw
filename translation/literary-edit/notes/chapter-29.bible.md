# 第 29 章 bible 摘錄（第二輪文學編輯用）

主 Agent 依 WORKFLOW「開始一章前」第 5 步建立；每個 chunk 的資料包都附上這份（`literary_edit.py packet --bible`）。
權威來源仍是 glossary／characters／worldbuilding；這裡只是本章會用到的部分，加上本章初譯已定的用詞。
段號為原文段號（`literary_edit.py plan 29` 的 pNNN；與 `translation/notes/chapter-29.md` 的段號相同）。

章節結構：p2 dateline（維瑞迪亞，艾勒納森林 · **3725 年**雪月 29 日）｜p3–p20 雪丘上：澤、穆、白；作戰計畫｜p21 分隔｜p22–p37 雷克托的簡報（p35 作戰圖）｜
p38 分隔｜p39–p53 日落出擊前的雪丘、回掩體、任務開始｜p54 scene-break dateline（雪月 30 日）｜p55–p113 指揮螢幕前的戰況（p59、p68、p74、p78、p81 作戰圖；
p108 第三後方基地被毀的訊息）｜p114 德盧因的訊息（裝置畫面）｜p115–p140 驗證訊息、白的提議（原始權重、梯度下降）。

chunk（`plan 29`）：01＝p3–p20｜02＝p22–p34、p36–p37｜03＝p39–p53、p55–p58、p60–p67、p69–p73｜04＝p75–p77、p79–p80、p82–p107、p109–p113｜05＝p115–p140。

### HTML 區塊（不送 editor，一字不動）

- p35、p59、p78、p81：作戰圖（北路軍／中路軍／南路軍／海路軍、北林）。p68、p74：作戰圖，沒有文字。
- p108：第三後方基地遭北極飛彈高精準命中，似已完全摧毀；最可能原因是內部叛徒洩漏基地位置；幾乎所有人員未生還；南路軍指揮官鄧的生還機率低於 10%。
- p114：德盧因的訊息（贏得北極信任、成為北極指揮官之一；受嚴密監視；布下可利用的弱點；針對他掌控的南翼的戰術；海岸以北約二十公里突破；從南邊包圍、收復北林）。
- 散文不要替這些畫面補內容或解釋。

## 一、全章固定用詞（editor 一次只看一個 chunk，看不到別處的叫法；這些不要換）

| 原文 | 本章用法 | 說明 |
|---|---|---|
| snowy hill | 積雪的山丘／山丘 | p3、p39 |
| pine trees | 松樹／松林 | p3、p20、p39 |
| jackets … white and grey | 白灰相間的外套 | p3 |
| Arctics | 北極（本章初譯多用「北極」指北極人／北極方面） | 全章 |
| Last train to Eldil | 開往艾迪爾的最後一班火車 | p14 |
| large contingent | 某種大部隊 | p14 |
| strike tonight | 今晚出擊 | p14 |
| bypass Northglade … cut off and surround it | 完全繞過北林，再把它切斷、包圍 | p14 |
| makeshift bunker／bunker | 臨時搭建的掩體／掩體 | p20、p47 |
| generals and Kungaupei leaders | 將領與昆高派領袖 | p22 |
| Group North／Center／South／Naval | 北路軍／中路軍／南路軍／海路軍 | glossary；圖上拆兩行 |
| perimeter | 防線 | p24、p28 |
| peninsula | 半島 | p24 |
| southern flank／northern flank | 南翼／北翼 | p24、p67、p72 |
| reinforcements | 援軍 | p24 |
| primary Arctic drone group | 北極的主力無人機群 | p26 |
| No offensive positional objective | 沒有攻佔陣地的目標 | p26 |
| keep them occupied | 牽制 | p26、p30 |
| outskirts of Northglade | 北林外圍 | p28 |
| seaborne drones | 海上無人機 | p30、p104 |
| Stretch goal | 延伸目標 | p30 |
| Arctic core territory | 北極本土 | p30、p104 |
| Thaldur Island／Telten | 薩杜爾島／鐵爾登 | p30、p104 |
| Supervise all fronts | 監督所有戰線 | p33 |
| group leaders | 各路軍指揮官 | p36 |
| three longhours | 三長時 | p37 |
| We launch at sundown | 日落時出擊 | p37 |
| snowmobile-like contraptions | 類似雪上摩托車的機械 | p39 |
| snow drones | 雪地無人機 | 全章 |
| Fiber optic cables | 光纖纜線 | p39 |
| *printers* | *印表機* | p40 |
| stick-on paper and shirts | 貼紙和襯衫 | p41 |
| classroom equipment | 教室用品 | p41 |
| visual attacks | 視覺攻擊 | p41 |
| Fi le gei fa | 照抄拼音；釋義「一百拍後開始」 | p43 |
| command post | 指揮所 | p44 |
| snowshoes | 雪鞋 | p47 |
| robot | 機器人 | p48、p49、p106 |
| watch buzzed | 手錶震了一下 | p43、p51、p111 |
| The mission had begun. | 任務開始了。 | p53 |
| command screen | 指揮螢幕 | p55 |
| land army groups | 陸上三路軍 | p56 |
| sentry units | 哨戒部隊 | p56 |
| An alarm blared | 警報大作 | p57、p80 |
| chat | 通訊頻道 | p60 |
| defensive positions | 防禦陣形 | p61、p83 |
| encirclement | 被包圍 | p61、p67 |
| disabled | 失去作用 | p63、p75 |
| stationary Arctic traps | 固定陷阱 | p63、p65 |
| simulations of forest snow drone combat | 森林雪地無人機作戰（模擬） | p64 |
| detection, hiding, attacking and taking cover | 偵察、隱蔽、攻擊與掩護 | p64 |
| AI models | AI 模型 | p64、p132、p134 |
| fixed face-to-face combat | 定點正面作戰 | p65 |
| direct face-to-face combat with fixed battle lines | 戰線固定的直接正面作戰 | p65 |
| micro-tactics／micro-tactical | 細部戰術 | p66、p92 |
| casualty counts／casualty ratios | 損失數／戰損比 | p69、p72、p98、p110 |
| visual feeds | 影像畫面 | p70、p90、p96 |
| Helisport copters and delivery copters | 旋翼球的旋翼機和送貨旋翼機 | p70 |
| payloads | 酬載 | p70、p104 |
| civilian infrastructure | 民用設施 | p70 |
| command centers | 指揮中心 | p71 |
| airborne duels | 空中對決 | p71 |
| big-picture view | 全局 | p77 |
| one and a half longhours | 一個半長時 | p79 |
| offshoot | 小分隊 | p79 |
| This is the real deal. | 這才是真正的決戰。 | p82 |
| slow retreat／flanking | 緩慢撤退／包抄 | p75、p83 |
| For Veridia! | 為了維瑞迪亞！ | p85 |
| Dze go ba fau gie | 照抄拼音，不加釋義 | p86 |
| clandestine battles in Redshire | 紅郡祕密作戰 | p87 |
| now or never | 現在不用，就沒機會了 | p87 |
| tactics one … six | 一號……六號戰術 | p95、p97、p100 |
| Units with IDs ending in 0 or 5 | 編號尾數為 0 或 5 的單位 | p97 |
| random modifications | 隨機修改 | p97、p99 |
| mainline version | 主版本 | p100 |
| Do it. | 照做。 | p101 |
| ground craft | 地面載具 | p104 |
| second round of payloads | 第二波酬載 | p104 |
| energy drink | 能量飲料 | p106 |
| "do not disturb" | 「勿擾」 | p112 |
| neck band／glasses | 頸帶／眼鏡 | p113 |
| authenticity | 真實性 | p116 |
| signed by the same key | 簽章金鑰相同 | p117（signature→簽章，不用「簽名」） |
| Grapetime 15 | 葡萄季 15 日 | p117、p127 |
| unorthodox, but plausible | 看似非正統，但可信 | p119 |
| discovered or planted | 被發現的／被刻意布置的 | p121 |
| all that we have to go on is his word | 唯一的依據就是他的一面之詞 | p127 |
| planted evidence | 布置假證據 | p127 |
| take the first leap of faith | 先跨出信任的第一步 | p130 |
| raw weights | 原始權重 | p132、p134 |
| safety properties | 安全性質 | p134 |
| unpredictable beasts | 難以預測的野獸 | p134 |
| grown, not forged | 長出來的，不是鍛造出來的 | p134 |
| They don't have walls, they have immune systems | 它們沒有城牆，只有免疫系統 | p134 |
| run simulations in parallel | 同時跑大量模擬 | p134、p136 |
| gradient descent／take the derivative | 梯度下降／求導數 | p136 |
| one in a million to two in a million | 從百萬分之一提高到百萬分之二 | p136 |
| robust across different simulators | 在各種模擬器裡都站得住 | p137 |
| a million rounds | 一百萬輪 | p137 |
| squiggles | 彎曲線條 | p137 |
| a magical snake with a deadly stare | 一條有致命凝視的魔蛇 | p137（不點名巴西利斯克） |
| shoot their own feet | 射到自己的腳 | p138 |
| steganographic channel | 隱寫通道 | p140 |

## 二、固定譯名

- 人物：Zei → 澤；Mu → 穆；Bai → 白；Den → 鄧；Lektor → 雷克托；Gallowar → 加洛瓦；Telpo → 特爾坡（性別未明，省略代名詞）；Vakaria → 瓦卡里亞（性別未明）；
  Deluin → 德盧因；Delwart → 德爾瓦特；Gladias → 格拉迪亞斯；Mov → 莫夫；Emerald → 翡翠（AI，不用代名詞）
- 地名：Elenar Forest → 艾勒納森林；Eldil → 艾迪爾；Northshore → 北岸省；Northglade → 北林；Thaldur → 薩杜爾島；Telten → 鐵爾登；Redshire → 紅郡；Freetown → 自由城；Dzego → 哲戈
- 組織：Arctic(s) → 北極；Kungaupei → 昆高派；Freetown defense companies → 自由城國防企業
- 其他：Minpentai → 明盤台；Helisport → 旋翼球；tick → 拍；longhour → 長時；Snowmoon → 雪月；Grapetime → 葡萄季

## 三、人物口吻與稱謂

- 穆：平靜、格言感（「有意義的事，從來不會在人們準備好的時候發生。」）；對機器人也溫柔道謝。
- 白：p9 的告白式擁抱，句式與澤的回應「很高興認識了你」對稱；p127–p138 冷靜、技術性強。
- 澤：p16 坦承沒有信心；戰況中簡短命令；p109 哭泣——不加深情緒。
- 雷克托：簡報幹練；p82–p85 激勵。
- 翡翠：精簡的報告體（「分析中……」「照做。」由澤說）。
- 全章沒有「您」。
- 說話者（**原文未標說話者的輪次一律照初譯，不補標籤**）：
  - chunk 01：p4 穆；p5 澤；p6 穆；p7（未標，穆接著說）；p9 白；p11 澤；p13（未標）；p14（未標，不點名）；p15（未標）；p16（未標，澤）；p18（白）；p19 穆。
  - chunk 02：p23 雷克托；p24 加洛瓦；p25 雷克托；p26 特爾坡；p27 雷克托；p28 鄧；p29 雷克托；p30 瓦卡里亞；p32 雷克托；p33 澤；p37 雷克托。
  - chunk 03：p40 白；p41（未標）；p42（未標）；p44 穆；p46（未標）；p49 穆。
  - chunk 04：p61 加洛瓦；p62 特爾坡；p82–p85 雷克托；p86 鄧；p92 澤；p93、p95 翡翠；p97 澤；p99 澤；p100 翡翠；p101 澤。
  - chunk 05：p116 澤；p117 翡翠；p118 澤；p119、p121 翡翠；p123 澤；p125、p127–p128 白；p129 澤；p130 白；p131 澤；p132 白；p134 白；p136–p138（未標，照初譯不點名）；
    p139（未標）；p140 澤。
  - 不同說話者不要合段；同一人連續的段落照原文分段。

## 四、伏筆與資訊邊界（不可加暗示）

- p3：外套「厚到足以」讓他們欣賞四周，「卻刻意沒厚到」讓他們覺得暖和——兩面並陳，不補理由；太陽「剛從東方升起」。
- p4：「平靜地」。p7「我們只希望」北極比我們更沒準備好。
- p8：每一步間隔「大約一拍」、和深雪搏鬥；「過了一會兒」。
- p10：把她拉上最後一步，讓她和自己、和穆站在同樣的高度。
- p12：「有好一會兒」默默等著；雪在東邊的樹林間、樹梢上紛飛。
- p14：「北極不可能不知道」；「我相信」已經開始調動；「很難穿越，但也不是難到無法穿越」；「最好的機會」。
- p16：「徹底搞砸」；「不，我沒有信心」；「最好的機會」。
- p17：白「又」從側邊抱住澤。p19：穆「打破了沉默」。
- p20：「又默默望著」五分鐘；「慢慢」走下山。
- p22：「幾十名」；「擁擠的」房間。
- p24：一路往東北推進到海岸、建立防線、切斷整座半島；南翼包圍北岸省的北極部隊、北翼擋住援軍。
- p30：「盡我所能」；延伸目標是「再往東」的薩杜爾島。
- p31：「安靜了一下」。p34「再看了一眼」。p36「看來都」相符（seemed）。
- p39：太陽「就掛在……上方一點點」、「再過幾分鐘」就要落下；「數千台」；「許多」看得出裝著武器；「大量」細細的銀線；「許多最大型」雪地無人機；「他這才明白」；「幾百公里」。
- p41：「以防」需要。
- p43：「過去十年」；「他從沒察覺」；「唯一真正重要的那場比賽：今晚」。
- p44：「輕聲說」。p45：太陽「已經有一半」。
- p49：「溫柔地低聲說」；拍了拍機器人的頭；機器人「輕輕」嗶了一聲。
- p55：「相鄰但分開的」房間；「剛過午夜」。
- p56：海路軍「延後」出發，好讓攻勢在主戰開打後「不久」發動；「到目前為止」「輕鬆」擊潰「幾支小型」哨戒部隊。
- p63：「十架」；「幾十架」；「到目前為止」主要交戰還沒開始。
- p64：「過去一個半月」；「幾百次」；「已經」載入。
- p65：「略有不同」；「他這才明白」北極「早就預料」；代價是定點正面作戰效能較差；維瑞迪亞也做了類似修改「但幅度小得多」；「似乎是……」（刪節號保留）。
- p66：「不妙」；北極無人機隊規模「比較大」；細部戰術彌補。
- p67：「幾分鐘後」；「先」砍倒大量樹木，「北翼尤其如此」；「大約二十分鐘後」；「可望」（hopefully）包圍、擊潰。
- p69：「很快」；「突破了一百」。
- p70：「看起來都改裝過」（seemingly）；「啊，對了」。
- p71：指揮中心「安全地」設在遠離前線的後方；「悄悄」用飛機送來；「一些」維瑞迪亞最頂尖的旋翼球選手。
- p72：「目前看來」；「確切的戰損比很難判定」；「明顯」維瑞迪亞佔優。
- p73：「四十分鐘後」；「真正重要的」好消息。
- p75：「幾乎完全」包圍；「無處可去」。
- p76：「充分」擊潰；「避免」殘存的半損無人機或陷阱造成損害；全速往東北。
- p79：「一個半長時」；「只有」加洛瓦留下的小分隊例外。
- p80：中路軍和南路軍「同時」受到威脅。
- p84：「過了一會兒」。p86「緊接著」。
- p87：「幾個月前」；「他知道」只會有「一小段時間」有效。
- p88：「幾分鐘後」；損失「很快都衝上幾百」。
- p89：北路軍「突然」由撤退轉為推進。
- p90：「屏住呼吸」。p91「不對勁，他察覺到」。
- p94、p120：「大約二十拍後」；p126「大約三十拍後」。
- p95：效果中等；零或略為負面；北極「似乎」已完全適應。
- p96：「儘管已盡了全力」；北極「一定還是至少」拿回「一部分」影像畫面。
- p98：「有幾分鐘」；「緩慢卻無可避免地」（slowly but surely）。
- p100：嘗試「八種」；「只有第七種」。
- p102：「急得開始冒汗」（sweat with consternation）；「沒料到」。
- p104：「看來」成功了，「至少在攻勢的初期階段」；兩處登陸（北林以東；再往東幾百公里的鐵爾登）；「已經開始」返回基地。
- p105：「有那麼一下子」欣慰；「還遠遠不夠」。
- p106：「悄悄」滑到；喝掉「大約一半」；「不一會兒」；「唯一的作用似乎只是」讓他更加絕望。
- p107：「把澤眼中僅剩的光都抽乾了」——原文比喻，照譯，不加強。
- p109：「哭了起來」。p110：「心不在焉地」；穆「已經立刻」接掌；「他心裡知道」這一仗已經輸了。
- p112：「不是一般的」軍事通訊頻道；翡翠「判定」重要到足以無視「嚴格的」勿擾指令。
- p115：「幾乎立刻」；為鄧哀悼「只能留待另一天」。
- p119：「極具攻擊性」；「看似」非正統但可信；對有此弱點的對手「非常有效」，對沒有的「導致更快落敗」。
- p121：效果「完全取決於」德盧因的判斷是否正確；弱點「可能是被發現的，也可能是被刻意布置的」。
- p122：「想了一下」，決定找人幫忙（human help）。
- p124：「幾乎立刻」。
- p127：「我不知道」能不能信任；「就連」葡萄季的訊息「也可能是」安排好的；「完全有能力」；「好幾個月」。
- p130：沒有好理由信任他／他有「充分的」理由信任我們；「這是他的責任」。
- p134：不能像一般軟體那樣「用數學證明它是安全的」；拿到原始權重就能同時跑大量模擬、最佳化出騙得過它們的攻擊。
- p136：「其實比……簡單得多」；變數舉例：貼在側面的圖案、無人機的動作方式；「自動」找出「最能提高」沒注意到的機率的小改變；「就算只是一小步」也能「馬上」找出來。
- p137：「記住」最後攻擊發生在真實世界；「我們能做的最多就是」篩選；「希望」一百萬輪後效果「相當好」；人類看「大概」是一堆彎曲線條。
- p138：「大概沒辦法」說服倒戈或自行關機；「但可以」讓它們注意不到；「說不定還能」射到自己的腳、過熱失靈。
- p140：「希望」德盧因看得懂。
