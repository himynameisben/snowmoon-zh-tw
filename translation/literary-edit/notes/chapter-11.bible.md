# 第 11 章 bible 摘錄（第二輪文學編輯用）

主 Agent 依 WORKFLOW「開始一章前」第 5 步建立；每個 chunk 的資料包都附上這份（`literary_edit.py packet --bible`）。
權威來源仍是 glossary／characters／worldbuilding；這裡只是本章會用到的部分，加上本章初譯已定的用詞。
段號為原文段號（`literary_edit.py plan 11` 的 pNNN；與 `translation/notes/chapter-11.md` 的段號相同）。

章節結構：p3–p86 梅爾丹草地，茲文第一場旋翼球比賽（維爾的訴訟、教育、比賽）｜p87 分隔｜p88–p91 進包廂｜p92 裝置畫面（空氣品質）｜
p93–p121 空氣品質守律者小組｜p122 分隔｜p123–p124 下自駕巴士、海卓菲廣告｜p125 `>` 廣告文案｜p126–p151 賽菈抱住他、回家叫哲戈餐車。

## 一、全章固定用詞（editor 一次只看一個 chunk，看不到別處的叫法；這些不要換）

| 原文 | 本章用法 | 出現位置／說明 |
|---|---|---|
| large grass field | 一大片草地；草地中央 | p3、p21 |
| families | 家庭 | p3 |
| Helisport game | 旋翼球比賽 | p6、p22、p27 |
| first real Helisport game | 第一場正式的旋翼球比賽 | p6 |
| Order business | 掌舵會的事 | p8 |
| lawsuit against Divergent | 給分歧那件訴訟 | p11 |
| Jump | 跳躍公司（後文簡稱「跳躍」） | p15–p18 |
| lost my job／went bankrupt | 丟了工作／破產 | p15 |
| the official story | 官方的說法 | p15 |
| last-ditch effort | 最後一搏 | p16 |
| risky bet on the financial markets | 在金融市場上下了一筆高風險的賭注 | p16 |
| derivative on property prices | 房價衍生性商品 | p16 |
| niche market | 小眾的市場 | p17 |
| insane slippage | 離譜的滑價 | p17 |
| hedge fund | 避險基金 | p17 |
| took the other side of the bet | 接了這場對賭的另一邊 | p17 |
| primary owners／majority share | 主要持有人／過半股份 | p17 |
| net zero | 淨值是零／一樣是零 | p18 |
| asymmetry | 不對稱 | p18 |
| end-of-year bonuses／a year of severance | 年終獎金／一年的資遣費 | p18 |
| free option on our backs | 踩著我們，替自己拿到了一個免費選擇權 | p18 |
| class action | 集體訴訟 | p19 |
| intimidate some media sites | 嚇得一些媒體網站不敢報導 | p19 |
| judges／tricks | 法官／把戲 | p19 |
| whistle | 哨音 | p20 |
| the instructor | 教練（稱謂表「旋翼球教練」） | p21 起 |
| large truck／back door／bottom hinge／ramp | 大卡車／後門／底部的鉸鏈／斜坡 | p21、p23 |
| personal copters | 個人旋翼機；旋翼機 | p24 起 |
| rotor blades／shielding | 旋翼／防護罩 | p24、p28 |
| strapping into them | 把自己綁進座椅／在旋翼機上綁好了 | p25、p28（譯者筆記：不寫「扣安全帶」） |
| yellow shirts／purple shirts | 黃色上衣／紫色上衣；穿黃衣、穿紫衣 | p25、p36 |
| team yellow／team purple | 黃隊／紫隊 | p46 起 |
| redball | 紅球 | p27 起 |
| limited game | 限定賽 | p27 |
| first team to get to six points | 先拿到六分的隊伍獲勝 | p27 |
| three quarters of the earth's gravity | 大約四分之三的地心引力 | p28 |
| blast off | 起飛 | p31 |
| rotor shield | 旋翼護罩 | p38 |
| the grid on top of the other copter's rotors | 對方旋翼頂上的護網 | p39 |
| The AI on these things | 這些東西上的 AI | p41 |
| full power | 全速 | p42 |
| safe maximum of five meters per tick | 安全上限每拍五公尺 | p45；p80「每拍五公尺的最高速度」 |
| Nice catch by X! N-th point for team Y | 「X 接得漂亮！Y 隊第 N 分。」 | p46、p52、p58、p62、p65、p67、p68、p70、p71、p83（譯者筆記統一句型） |
| Another nice catch by X | 「X 又接到一顆，漂亮！」 | p58、p62、p71 |
| And, nice catch by Zven | 「然後，茲文接得漂亮。」 | p83（保留刻意的停頓） |
| math competition | 數學競賽 | p50 |
| arithmetic／homework | 算術題／作業 | p51 |
| Order member | 掌舵會成員 | p54 |
| education committee, staffed by parliament | 教育委員會，委員是議會任命的 | p55 |
| private ones | 私立學校 | p55、p57 |
| rubric micro-nudging | 規準細部輕推 | p57 |
| whispering into her watch as a substitute for a neck band | 對著手錶低聲說，拿手錶權充頸帶 | p56 |
| three groups of three kids | 三組孩子，每組三人 | p59 |
| the fourth redball | 第四顆紅球 | p59、p69、p82 |
| broke his fall | 緩衝了他的墜落 | p60、p78 |
| solitary quest | 獨自尋找 | p69 |
| broken rotors | 旋翼已經壞了（v1「摔壞」，v2 依 reviewer 改，原文沒說損壞原因） | p82 |
| path less traveled／blazed a trail for all | 「他走上人跡較少的那條路，」「而那為眾人開出了一條道路。」 | p86（glossary；ch18 白會呼應） |
| old Veridian author | 一位維瑞迪亞古代作家 | p86 |
| barrier／booth | 隔門／包廂 | p88 |
| third circle of Keepers | 第三個守律者小組 | p90（glossary circle） |
| air quality | 空氣品質 | p90、p91、p98 |
| assigned number was two | 他的編號是二號 | p90 |
| secure booths／ventilation | 保密包廂／通風 | p93 |
| Filters | 過濾器 | p93、p96、p99 |
| behind standards | 遠遠達不到標準 | p94（保留 everyone 的模糊） |
| this bracket | 這個稅級 | p94 |
| CO₂ reading | CO₂ 讀數 | p95 |
| open and deployable | 夠不夠開放、夠不夠容易部署 | p96 |
| twice as cheap every two years for the past decade | 過去十年，每兩年就便宜一半 | p96 |
| indoor air quality tax rubrics | 室內空氣品質的稅務規準 | p98 |
| land tax component | 土地稅的一個成分 | p99 |
| average occupied room reads worse than a thousand | 有人使用的房間如果平均讀數比一千還差 | p99（譯者筆記已定「比一千還差」） |
| a third of a percent per year | 每年多課三分之一個百分點 | p99–p101 |
| UVC | 紫外線 C 燈 | p99 |
| theoretically perfect and abysmally bad | 理論上的完美到糟到極點 | p100 |
| land value | 土地價值 | p101 |
| a sixth of their revenue | 營收的六分之一 | p101 |
| Public aesthetics | 公共美觀 | p102 |
| Accessibility | 無障礙 | p102 |
| What percent of the lot you're building on | 建蔽率 | p102（譯者筆記） |
| ground-floor active use | 一樓活化使用 | p102、p104 |
| Emergency preparedness／Fire safety | 緊急應變準備／消防安全 | p102 |
| broad listen report | 廣聽報告 | p103 |
| indoor airborne disease resistance | 室內的空氣傳播疾病防治 | p103 |
| top ten concerns | 最關心的前十名 | p103 |
| walkability／congestion | 步行友善度／壅塞 | p104 |
| tail risk | 尾部風險 | p106、p107 |
| Super-pandemics | 超級大流行 | p108 |
| super opaque society | 超級不透明的社會 | p110 |
| sermons | 說教 | p110、p136（譯者筆記：兩處統一） |
| plans on the table | 檯面上有哪些可能的方案 | p111 |
| two thirds of a percent | 三分之二個百分點 | p112 |
| funding organs | 資助機構 | p112 |
| parliament allocations | 議會撥款 | p112 |
| that round is a mess | 那一輪現在一團亂 | p114 |
| social media polarization | 社群媒體極化 | p114 |
| zipcoins | 吉普幣 | p114 |
| bounded matching | 有上限的配對補助 | p114 |
| insider ... blew the whistle | 內部人士出來爆料 | p114 |
| dig holes and then fill them back up | 挖洞、再把洞填回去 | p116 |
| open platforms／open ecosystem | 開放平台／開放的生態系 | p116 |
| wins by default | 不戰而勝 | p116 |
| channels | 管道 | p117 |
| air filtering, cleaning, wastewater scanning | 空氣過濾、清淨、汙水監測 | p117 |
| cleartext | 明文 | p120 |
| autobus | 自駕巴士 | p123 |
| front face covering／strap／belt | 前方臉罩／束帶／帶子 | p123 |
| virus protection | 防病毒的效果 | p123 |
| restaurant where he had bumped into Febric | 幾個月前巧遇費布里克的那家餐廳 | p124（回溯前章） |
| Hydrafill mascot／yellow and green | 海卓菲的吉祥物／經典的黃綠配色 | p124 |
| jet of sludge-like green-colored water | 一道像汙泥般的綠色水柱 | p124 |
| Heavy water／deuterium | 重水／氘 | p125 |
| parts per million | ppm | p125 |
| NORTHERN ICE | 北方冰原 | p125 |
| post on urban economics in Freetown | 那篇談自由城都市經濟的文章 | p132 |
| gossip | 八卦 | p134 |
| spooked about the Arctics | 對北極越來越緊張 | p134 |
| nonchalant | 滿不在乎 | p135 |
| older ones／newer ones | 資深的那些／新進的那些 | p138、p140 |
| corporates | 企業 | p139 |
| circle（門上的感應點） | 圓圈 | p142 |
| Dzego food truck | 哲戈餐車 | p144、p148 |
| The usual | 老樣子 | p144 |
| food boxes | 餐盒 | p151 |

## 二、本章出現的 bible 譯名（`uv run tools/literary_edit.py terms 11` 產生）

- 人名：Gladias → 格拉迪亞斯；Glad → 格拉德（賽菈叫他）；Seila → 賽菈；Zven → 茲文；Lily → 莉莉；Febric → 費布里克；Hreda → 赫蕾妲；
  Vil → 維爾；Daia → 黛亞；Jahn → 楊恩；Delwart → 德爾瓦特；Ephelion → 艾費里昂（Lord Ephelion → 艾費里昂勳爵）
- 旋翼球的孩子：Dommus → 多穆斯；Gale → 蓋爾；Dela → 黛拉；Plat → 普拉特；Meny → 梅妮；Egardo → 艾加多
- 地名：Veridia → 維瑞迪亞；Meldan → 梅爾丹；Freetown → 自由城；Redshire → 紅郡；Northglade → 北林；Dzego → 哲戈；Iptak → 伊普塔克；Arctics → 北極人／北極
- 企業與平台：Divergent → 分歧；Jump → 跳躍（公司）；Bluewhale → 藍鯨；Hydrafill → 海卓菲
- 制度：Order → 掌舵會；Keeper → 守律者（避免：守護者）；Steering → 掌舵；rubric → 規準（避免：評分標準）；land tax → 土地稅（避免：地價稅）；
  Quadratic Funding → 平方募資（避免：二次方募資、二次融資）；Graph Funding → 圖譜募資（避免：圖表募資、圖形融資）；co-governance → 共同治理；
  education committee → 教育委員會；funding organs → 資助機構；bounded matching → 有上限的配對補助；ground-floor active use → 一樓活化使用；
  broad listen report → 廣聽報告
- 金融：derivative → 衍生性商品（避免：衍生品）；slippage → 滑價（避免：滑點）；hedge fund → 避險基金（避免：對沖基金）；
  free option → 免費選擇權（避免：免費期權）；class action → 集體訴訟；severance → 資遣費（避免：遣散費）；tail risk → 尾部風險
- 技術：open source → 開源（避免：開放原始碼）；wastewater scanning → 汙水監測（避免：污水掃描）；cleartext → 明文；deuterium → 氘；PM2.5
- 物品：hand device → 手持裝置（避免：手機）；watch → 手錶；neck band → 頸帶；privacy robe → 隱私袍；autobus → 自駕巴士（避免：公共汽車）；
  copter → 旋翼機（避免：直升機）；redball → 紅球
- 運動：Helisport → 旋翼球（避免：直升機運動）
- 時間：tick → 拍；Bloomtime → 花季（避免：花月）

## 三、人物口吻與稱謂

- 格拉迪亞斯：理性、溫和，帶冷幽默；心算數字是他的思考方式（p93 讀數）。對賽菈、黛亞、維爾用「你」。
- 賽菈：溫暖、輕快；叫格拉迪亞斯「格拉德」（p54）；p54 及時打住不說「守律者」；p86 吟誦古句。
- 黛亞：熱情、細心的家長口吻，留意孩子課業。
- 維爾：平實的家長口吻，客氣、怕麻煩別人（p13）；講訴訟時條理分明、帶點疲憊。
- 教練：播報口吻，句型統一（見一）；對孩子用「你」「大家」。
- 空氣品質小組：成員都**沒有編號、沒有性別**，譯文一律「另一位守律者」，**不用他／她**（譯者筆記）。
- 一個說話輪次一段。原文很多對話沒標說話者，editor 不可自行補標籤或改變初譯指涉：
  - p5 黛亞、p6 格拉迪亞斯、p7（未標，推測黛亞）、p8 格拉迪亞斯、p9（未標，推測格拉迪亞斯反問）、p11 維爾、p12（未標）、p13 維爾、p14（未標）、p15 維爾、
    p16（未標，打斷維爾複述新聞）、p17–p19 維爾（連續三段）。
  - p22、p27、p29、p31 教練；p30 孩子們；p33 格拉迪亞斯對賽菈、p34 賽菈（推測）、p35「在哲戈。」（未標，譯者筆記：不補）；p41 格拉迪亞斯。
  - p49 格拉迪亞斯問黛亞、p50 黛亞、p51（未標，推測黛亞，不補）；p52 教練；p54 賽菈、p55 格拉迪亞斯、p56 賽菈。
  - p93 格拉迪亞斯、p94 某人、p96 另一位守律者、p97 格拉迪亞斯、p98–p106 未標（p100、p103、p105 疑似同一位懷疑者）、p107 格拉迪亞斯、
    p108–p112 未標、p113–p114 另一位守律者、p115–p121 未標。
  - p129 格拉迪亞斯、p130 賽菈、p131 格拉迪亞斯、p132 賽菈、p133 格拉迪亞斯、p134 賽菈、p135 格拉迪亞斯、p136 賽菈、p138–p140 格拉迪亞斯（連續三段）、
    p144 賽菈、p145 格拉迪亞斯。
- p72「He began to fly closer to the ground.」指茲文（初譯寫明「茲文」，譯者筆記），不可改回「他」。

## 四、伏筆與資訊邊界（不可加暗示）

- p4：黛亞「遠遠就」看見；格拉迪亞斯看到、帶著笑、加快腳步。
- p8：「不能公開講」；「不過還算順利！」
- p11：「過去兩個月」大半的時間（a big part）。
- p13：維爾怕拿細節煩他們。
- p15：「大概半年前」；「一個月後」；「官方的說法一直是——」被打斷。
- p16：「最後一搏」；他們「正準備宣布」要開始在那個地區提供服務；在乎的人不夠多、接著運氣不好、房價下跌。
- p17：「唯一的原因」（The only reason）；「悄悄」用「極低的價格」買下「過半股份」。
- p18：四個條件分支逐一保留：漲→跳躍賺、分歧虧、淨零；跌（確實跌了）→跳躍虧、分歧賺、淨零；不對稱：跳躍虧（確實虧了）→破產→不必付年終獎金＋一年資遣費；「免費選擇權」。
- p19：「甚至」嚇得一些媒體網站不敢報導；「我覺得到目前為止」法官都看穿了；「所以我還滿樂觀的」。
- p23：門「緩緩」打開；「幾拍之後」。
- p24：旋翼機「自動」滾出來；描述：簡單的椅子、頂上裝旋翼、四周防護罩。
- p25：「大約十到十二歲」；一半黃、一半紫；茲文在黃衣那群。
- p26：「小得多的盒子」；四架鮮紅色無人機，幾公分寬的球形，柔軟、像羽毛的旋翼。
- p28：十個孩子；轉速「剛好足以抵銷大約四分之三的地心引力」；「兩公尺左右」；慢慢滑翔落回。
- p33：「我很意外」；「一定會說太危險」（definitely）。
- p34：「不到十年前」才發明。p35「在哲戈。」照原文不補說話者。
- p38：兩架互相彈開，「誰也沒受傷」（harmlessly）。
- p39：落後的位置關係、第三個孩子到他正下方、氣流把他往下吸、腳彈到護網——空間關係照原文。
- p40：往下翻滾「幾公尺」才穩住。
- p42：另一個孩子「沒能及時」發現，於是茲文領先。
- p44：Thinking quickly（反應很快）；踢回、往前移、伸手、掌心接住。
- p45：旋翼慢下來但「沒有完全停住」；下降速度到「安全上限每拍五公尺」時旋翼加速；相當於從「略低於兩公尺」高度摔下的落地速度。技術說明，不補畫面。
- p47：紅球往「和茲文站的地方相反」的方向衝。
- p49：賽菈聽到問題，把頭「微微」轉向他們。
- p50：「一直想讓莉莉」對藝術多一點興趣，「到現在都不太成功」。
- p51：「我有點意外」；算術題「好像」（seemed）比費布里克在他這個年紀時「稍微……淺了一點」——遲疑的停頓與問句保留。
- p54：她及時打住，「想起」就連說出守律者都不妥（briefly remembering）。
- p55：學校不歸掌舵會管；公立學校由教育委員會負責；「一直有人在想辦法」多支持私立學校、用圖譜募資、設計規準給正確誘因。
- p56：賽菈的內心：與其每個字小心挑選免得洩漏格拉迪亞斯的職位，不如私下談——「她心想」（she thought）。
- p57：格拉迪亞斯的內心：德爾瓦特「會支持」；「更會支持」*完全不*附帶規準細部輕推的私立學校。強調保留。
- p59：「他們認定」是不同的紅球（assumed must be）；茲文「像是」（seemed）在隨意閒晃；想找第四顆紅球「可能」在哪裡。
- p60：翻落、AI 自動緩衝、摔到地上、幾拍之後站起來回到空中。
- p69：其他孩子「似乎」（seemed）都完全忘了第四顆的存在。
- p72：主詞是茲文（見三）。
- p75：另一個孩子撞上蓋爾、往右偏了「好幾公尺」；紅球掉頭往後飛、從兩人中間穿過；兩人都撲空。
- p76：兩個對手「至少」落後十公尺。
- p77：五公尺、四公尺、三公尺——倒數節奏保留。
- p78：out of nowhere、茲文「好像」（seemed）掉到地上，AI「照例」緩衝。
- p79：「得意地」（triumphantly）。
- p81：「突然」格拉迪亞斯和賽菈的目光轉向茲文。
- p82：蓋爾還在「大約三十公尺」的空中；茲文交出的是「在地上找到的」、「旋翼已經摔壞」的第四顆紅球。
- p84：格拉迪亞斯「鬆了一口氣」；p85 賽菈滿臉笑容、為茲文驕傲——不加強。
- p89：「另外三位，格拉迪亞斯想，一定還在路上」（must）。
- p93：「看來他們還沒想出」（I guess）。
- p96：「我覺得大家自己會想辦法解決」；「只看技術夠不夠開放、夠不夠容易部署」（just a matter of）。
- p97：「我覺得我們得再推得用力一點」。
- p99：零／三分之一個百分點／平均讀數比一千差／裝過濾器或紫外線 C 燈門檻上調——條件逐項保留。
- p101：「對很多企業來說」大概相當於營收的六分之一（like a sixth）。
- p102：無障礙的兩種意義，*以及* 強調保留；一樓活化使用「有爭議」「有些人覺得」。
- p103：「看看我們一個月前做的廣聽報告」；「根本不在」前十名。
- p104：被打斷（——）。p105「好吧，不過我覺得……」。
- p106：QA 已改：「那條規準不歸我們決定。我們管的是空氣品質。」
- p108：「比如說，北極人故意散播的那種」（Like）。
- p110：「唯一能證明北極人知道有維瑞迪亞」的證據，是一天到晚得聽艾費里昂勳爵說教——反諷保留。
- p112：被打斷（——）。
- p114：QA 已改：「看來（apparently）整件事都是他們幹的」——不可改成確定。「其實不是很好的計畫」插入保留；十／二十／一百的數字關係。
- p116：「錢流到哪裡根本不重要」；目標是抽乾跟開放平台「接軌」的資金。
- p118：反問語氣；搬了家也一樣；每個人何時健康、何時生病。
- p119：反諷：「我還以為一直說沒有證據……的人，是你？」
- p120：「難道沒有什麼密碼學的方法」——**不暗示澤**（澤此時在哲戈讀密碼學，讀者會自己聯想；不加提示）。
- p121：「要是你找得到……的天才，記得告訴我們。」
- p123：鼻子上下之間的帶子「不再勒緊」；防病毒效果差了一些——離開格外擁擠的巴士後他已不需要——但比較舒服、呼吸順。
- p124：幾個月前巧遇費布里克；廣告左右兩側的描述照原文。
- p125：廣告的全大寫（NORTHERN ICE、TEN PERCENT LESS TOXIC、WE）比照前幾章不加符號；145 ppm、132 ppm、三十公里、一成；「勇敢地／英勇開採」的誇張口吻保留；**廣告的偽科學推論（含量少一成＝毒性低一成）照原文，不修正**。
- p126：Gladias smiled.——不加評論。
- p135：「好像都這麼……滿不在乎」的停頓。
- p136：「我猜」（I guess）；「出於好奇」看一看、聽一聽。
- p137：「哀嘆了一聲」（groaned）。
- p138：資深的「好像」明白；新進的「不是全部，但很多人」都覺得乾脆別管？——問句語氣保留。
- p139：自由城的企業「好像」比較不受影響；「幾乎是唯一」——除了紅郡和透過共同治理部分由紅郡議會管理的城市。
- p140：「我想最主要的是」（I guess more than anything）；新進守律者「好像」懷疑掌舵、平方募資、圖譜募資、政府能做成什麼事。
- p142：手錶貼上圓圈、門開。
- p148：家門「還沒關上」，賽菈「已經」看得到幾百公尺外的餐車。

## 五、數值（照原文）

- p11 過去兩個月；p15 大概半年前、一個月後；p18 一年的資遣費。
- p22 五分鐘後；p23 幾拍之後；p25 大約十到十二歲；p26 四架、幾公分寬；p27 一分、六分；p28 十個孩子、四分之三、兩公尺左右。
- p31 五……四……三……二……一；p34 不到十年前；p40 幾公尺；p42 幾公尺；p43 一公尺；p45 每拍五公尺、略低於兩公尺。
- p59 三組、每組三人、第四顆；p60 幾拍之後；p61 一分鐘後；p64 兩分鐘；p66 一分鐘；比分：黃 1、紫 2、黃 2、紫 3、黃 3、黃 4、紫 4、紫 5、黃 5、黃 6。
- p73 一公尺；p75 好幾公尺；p76 至少十公尺；p77 五、四、三公尺；p80 每拍五公尺；p82 大約三十公尺。
- p90 第三個小組、二號；p89 三位、另外三位；p92 906、PM2.5 4.4、已認證 16、未知 0（裝置畫面）；p93 四個人、906；p95 918。
- p96 過去十年、每兩年便宜一半；p99 三分之一個百分點、一千；p101 六分之一；p103 一個月前、前十名；p112 三分之二個百分點。
- p114 十吉普幣、二十、一百。
- p123–p125 145 ppm、132 ppm、三十公里、一成。
- p142 幾分鐘後；p144 一分鐘；p148 幾百公尺。

## 六、補畫面注意

- 適合補的場景：p3–p4 草地、家庭（人群聲、光線；不新增擺設或天氣事實）；p20–p26 哨音、卡車後門、旋翼機滾出、無人機飛出（聲音、動態）；
  p28、p32 旋翼轉動、起飛（聲音、風）；p36–p48、p59–p83 比賽過程（觀眾聲、旋翼聲；**不改變任何空間位置、順序或比分**）；
  p88 拉隔門；p123–p124 下巴士走路；p127 被抱住；p142、p148–p151 回家、餐車。
- 不補：所有對話內容；p15–p19 訴訟說明；p45 速度說明；p54、p56、p57 內心；p93–p121 守律者討論（純對話與制度說明）；p125 廣告文案（引言錨點，只改寫文字）。
- 不補任何預示：不暗示澤（p120 密碼學）、不暗示德爾瓦特的真實身分（p57）、不暗示莉莉後來出走（p50）、不暗示北極入侵（p108、p138）。
- p86 吟誦是一場的落點；p126 「格拉迪亞斯笑了笑」接廣告的反諷，不加評論。
