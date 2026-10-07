# 第 22 章 bible 摘錄（第二輪文學編輯用）

主 Agent 依 WORKFLOW「開始一章前」第 5 步建立；每個 chunk 的資料包都附上這份（`literary_edit.py packet --bible`）。
權威來源仍是 glossary／characters／worldbuilding；這裡只是本章會用到的部分，加上本章初譯已定的用詞。
段號為原文段號（`literary_edit.py plan 22` 的 pNNN；與 `translation/notes/chapter-22.md` 的段號相同）。

章節結構：p2 dateline（自由城，霧季 22 日）｜p3–p30 楊恩搭計程車：街景、投影機、避難所廣告（p7、p9 `>` 引言）、修路、車資表（p12 畫面）、和司機聊國防稅與避難所卡特爾｜
p31 分隔｜p32–p66 研究所餐廳和烏塔庫談自由城的國防、聯合城邦早期歷史、自由城與亞圖利亞的篩選、基因與自由、軍事機密｜
p67 分隔｜p68–p146 楊恩做籌款方案表；澤來電，用閱後即焚檔案即時展示紅郡的祕密殺傷鏈（p82、p89、p93、p98、p109、p127 六張 SVG 畫面），談隱寫術與綁架北極無人機的計畫，請楊恩介紹另一家國防企業。

chunk（`plan 22`）：01＝p3–p30（含 p7、p9 引言，跨 p12 車資表）｜02＝p32–p66｜03＝p68–p126（跨 p82、p89、p93、p98、p109 畫面）｜04＝p128–p146。

### `>` 引言（p7、p9）

- 廣告文體：簡短、推銷口吻；數字用阿拉伯數字（地下 10 公尺、325,000 吉普幣、50,000 吉普幣）。`>` 段落與空 `>` 行結構不變，不可拆合。
- p7：「豪華避難所房間」「自由城中心區北緣」「最高等級的物理、生物與資訊過濾及隔絕」「只要 325,000 吉普幣！」
- p9：「平民也住得起的避難所，各種形式、大小應有盡有」「只要 50,000 吉普幣起，提供分期貸款方案！」

### HTML 區塊（不送 editor，一字不動）

- p12 計程車車資表（基本車資 3.69、每分鐘 9 分鐘 1.89、每公里 5.65 公里 1.26、加減速 113 m/s Δv 1.03、三列道路壅塞費 1.50／1.00／2.25、總計 12.52）。
- p82、p89、p93、p98、p109、p127：澤傳來的戰場示意圖（SVG）。紅色方塊＝北極無人機；藍色圓圈＝我方七架干擾無人機，排成六角形；圓圈外的虛線圈＝正在干擾；藍色三角形＝兩架攻擊無人機；紅色 x＝擊中。
  散文不要替圖補解釋，也不要描述圖上沒寫進正文的位置變化。

## 一、全章固定用詞（editor 一次只看一個 chunk，看不到別處的叫法；這些不要換）

| 原文 | 本章用法 | 出現位置／說明 |
|---|---|---|
| taxi／driver | 計程車／司機 | 全章前段 |
| highway | 高架道路（p6「另一條高架道路」）；p4 after the highway→一過高架 | p4、p6 |
| projector, hidden under a bench | 投影機——藏在公園的一張長椅底下 | p4 |
| Graph Funding or rubrics | 圖譜募資……規準 | p4 |
| public goods | 公共財 | p4 |
| the amount of activity on the streets | 街上的人車 | p5 |
| shelter(s) | 避難所 | p7、p9、p10、p19、p21、p22、p23 |
| construction of roads | 修路 | p10；p23 build roads→修路 |
| hand device | 手持裝置 | p11 |
| Chief／boss | 大哥／老闆 | p13、p28（楊恩叫司機）；p29（司機叫楊恩） |
| congestion charges／tolls | 壅塞費／費用 | p15；p59 congestion tolls→壅塞費 |
| bumping up every tax and toll | 能漲的稅、能漲的費全都在漲 | p16 |
| Funding defense | 充實國防 | p16 |
| gossip | 八卦 | p19、p64 |
| defense companies | 國防企業 | p21、p63、p72、p75；p143 defense corp→國防企業 |
| annexed | 被併吞 | p21、p39 |
| cartel | 卡特爾 | p21 |
| modernize their armor and weapons | 把裝甲和武器大幅翻新了一輪 | p21 |
| their property, their rules | 人家的財產，人家說了算 | p22 |
| rationed | 用配給的 | p22 |
| the polite story | 好聽的說法 | p23 |
| not *quite* that clean | 沒有*那麼*乾淨 | p23 |
| collusion | 勾結 | p23 |
| retroactive reward | 事後獎勵 | p23 |
| private property | 私有財產 | p23、p24、p59 |
| public work | 公共工程 | p23 |
| maximum budget rule | 預算上限規定 | p23 |
| 'maintenance'／'free' | 『維修』／『自由』 | p24、p25（單引號改『』） |
| node in Northglade | 北林的據點 | p25（譯者筆記：不是技術節點） |
| Freetown Economics Institute | 自由城經濟研究所 | p27、p32；p73、p143 Economics Institute director／Institute director→（經濟）研究所所長 |
| turnstile(s) | 旋轉閘門 | p32、p59 |
| unified defense grid between the aks | 克城之間建立聯防網 | p37 |
| more theater than anything substantive | 比較像在作秀，沒什麼實質 | p37；p38「實質的事」 |
| big corps／insurance／rates tripled／doubled again／dropped back down by a quarter | 大企業／保險／費率變成原來的三倍／又翻了一倍／回落了四分之一 | p39（QA 已改「變成原來的三倍」，不可改回「漲了三倍」） |
| defense packages | 國防方案 | p39 |
| market incentives | 市場誘因 | p40 |
| bio safety | 生物安全 | p41 |
| average indoor CO2 levels dropped by over a hundred points | 室內二氧化碳平均濃度就降了一百多點 | p41（不補單位） |
| a much more sensible distance and time system | 一套合理得多的距離與時間制度 | p41 |
| economic freedom | 經濟自由 | p43 |
| co-governance system | 共同治理制度 | p49 |
| a percent of the votes in its parliament | 自己議會的一定比例票數 | p50 |
| swapping homes and citizenships | 交換住所和公民身分 | p51 |
| change their allegiance | 把效忠的對象換成 | p51 |
| new constitution | 新憲法 | p52 |
| personality test／compatible result | 性格測驗／『合得來』結果 | p52 |
| conscientiousness and test scores | 盡責性和考試成績 | p54 |
| legitimacy／buying in | 正當性／自願認同 | p55 |
| selection | 篩選 | p56 |
| genetically more freedom-loving | 在基因上就比別人更熱愛自由 | p58 |
| honestly self-report | 誠實地自己表明 | p59 |
| forager freedom of the great outdoors | 採集者在廣闊野外的那種自由 | p60 |
| within your own box you are the master | 在自己的小盒子裡，你就是主人 | p60 |
| intellectual culture | 知識文化 | p62 |
| threat model | 威脅模型 | p63 |
| those circles | 那種圈子 | p65 |
| Freedom of speech … military secrets | 言論自由……軍事機密 | p66 |
| economic collateral damage | 對經濟造成多少附帶損害 | p68 |
| less ... free | 不那麼……自由 | p68 |
| calling booth | 通話亭 | p70 |
| connection you made | 牽線 | p72、p73 |
| hunting down Arctic drones | 獵殺北極的無人機 | p77 |
| view-once file | 閱後即焚檔案 | p80、p88 |
| clandestine kill chain／ground drone | 祕密殺傷鏈／地面無人機 | p84 |
| red square／blue circles／hexagon／jam communications／dormant | 紅色方塊／藍色圓圈／六角形／干擾通訊／休眠 | p85 |
| jammer drones／red X／main antenna／legs／attack drones／blue triangles | 干擾無人機／紅色的 X／主天線／腿／攻擊無人機／藍色三角形 | p96 |
| dancing | 跳舞 | p102–p103 |
| *survive* | *活*（p104）／*活下來*（p105） | 斜體保留 |
| target practice | 當靶子 | p105 |
| fry the target's circuits／training data | 燒毀目標的電路／訓練資料 | p105、p133 |
| Arctic reinforcements | 北極的援軍 | p110 |
| play dead／lure | 裝死／引到中間 | p111 |
| play by play | 實況轉播 | p112 |
| Circles／northwest square／Goal: all comms and memory dead | 圓圈／西北方的方塊／目標：通訊與記憶體全部摧毀 | p114（對 AI 的指令，簡短如軍令） |
| No-／Wha- | 不——／怎——（不點名說話者） | p117、p118 |
| ticks | 拍 | p88、p97、p123–p125 |
| download icon | 下載圖示 | p126 |
| chip and memory-kill | 銷毀晶片與記憶體 | p130、p132 |
| ten centimeters | 十公分 | p132 |
| salvage training data | 救回任何訓練資料 | p133 |
| un-backdoored electronics | 沒被植入後門的電子裝置 | p136、p137 |
| watches, hand devices and compute boxes | 手錶、手持裝置和運算盒 | p136 |
| steganography | 隱寫術 | p136 |
| erasure code that's highly noise-tolerant | 高度抗雜訊抹除碼 | p137 |
| anyone or any bot | 任何人或 AI | p137（bot 不譯機器人） |
| kidnap an Arctic drone | 綁架一架北極無人機 | p139 |
| seaborne／airborne | 海上作戰／空中作戰 | p145 |
| screwing you over | 被坑 | p146 |

## 二、固定譯名

- 人物：Jahn → 楊恩（男）；Utaku → 烏塔庫（女，貝爾帕基出身、研究所博士生）；Zei → 澤（男，哲戈 18 歲）
- 地名：Freetown → 自由城；United Cities → 聯合城邦；Redshire → 紅郡；Northglade → 北林；Greater Plum Harbor → 大梅港；Dzego → 哲戈；
  Arturia → 亞圖利亞；Belpaki → 貝爾帕基；the aks → 克城
- 組織：Freetown Economics Institute → 自由城經濟研究所；Arctic(s) → 北極（北極人）
- 制度：Graph Funding → 圖譜募資；rubric → 規準；co-governance → 共同治理；maximum budget rule → 預算上限規定；unified defense grid → 聯防網；
  legitimacy → 正當性（避免：合法性）；conscientiousness → 盡責性（避免：責任心）
- 技術：kill chain → 殺傷鏈（避免：擊殺鏈）；view-once file → 閱後即焚檔案；erasure code → 抹除碼（避免：糾刪碼）；training data → 訓練資料（避免：訓練數據）；
  noise-tolerant → 抗雜訊；backdoored → 植入後門；threat model → 威脅模型；bot → AI
- 物品：hand device → 手持裝置（避免：手機）；watch → 手錶；drone → 無人機；calling booth → 通話亭（避免：電話亭）
- 單位：longhour → 長時；tick → 拍；zipcoin → 吉普幣

## 三、人物口吻與稱謂

- 稱謂：全章沒有「您」，不要加。楊恩 ↔ 司機：你，「大哥」「老闆」；楊恩 ↔ 烏塔庫、澤：你（平輩）。
- 楊恩：本章視角人物；觀察冷靜，帶經濟學家的分析；長段說理（p23、p59）仍是口語；守得住軍事機密。
- 司機：市井口吻，樂天、務實（「不過嘛，他們也是在努力」）；不加台語詞。
- 烏塔庫：研究生平輩口吻，消息靈通，保留懷疑（「作秀」）。
- 澤：興奮、像在做技術簡報；對 AI 下指令簡短如軍令（p114–p116）。
- 說話者（**原文未標說話者的輪次一律照初譯，不補標籤**）：
  - p13 楊恩、p14 司機、p15 楊恩（未標）、p16 司機（未標）、p17 楊恩（未標）、p18 司機、p19 楊恩、p20 司機（未標）、p21 楊恩（未標）、p22 司機（未標）、
    p23–p25 楊恩（未標，譯者筆記：不點名）、p26（未標，較可能是司機，不點名）、p28 楊恩（未標）、p29 司機。
  - p34 楊恩、p35 烏塔庫（未標）、p36 楊恩、p37 烏塔庫、p38 楊恩、p39 烏塔庫、p40–p42 楊恩（未標，不點名）、p43 烏塔庫、p44 楊恩、p45 烏塔庫、p46 楊恩、
    p47 烏塔庫、p48 楊恩、p49 烏塔庫、p50–p52 楊恩、p53 烏塔庫、p54–p55 楊恩、p56 烏塔庫、p57 楊恩、p58 烏塔庫、p59 楊恩、p60（未標，可能是楊恩或烏塔庫，不點名）、
    p61（未標）、p62 烏塔庫（提到貝爾帕基）、p63 烏塔庫、p64 楊恩、p65 烏塔庫、p66 楊恩。全部未標（除 p66「楊恩嘆了口氣」）。
  - p71 楊恩、p72 澤、p73–p74 楊恩（兩段）、p75 澤、p76 楊恩、p77 澤、p78 楊恩、p79 澤；p83 楊恩、p84–p85 澤、p86 楊恩、p87 澤；p90 澤、p91 楊恩、p92 澤（譯者筆記）；
    p94 澤、p95 楊恩、p96 澤；p99 楊恩、p100 澤、p101 楊恩、p102 澤、p103 楊恩、p104–p105 澤、p106 澤、p107 楊恩、p108 澤；p110 楊恩、p111 澤、p112 楊恩、
    p113–p116 澤、p117–p118 不點名、p120–p121 澤；p128 澤、p129 楊恩、p130 澤、p131 楊恩、p132–p134 澤、p135 楊恩、p136–p137 澤、p138 楊恩、p139 澤、p140 楊恩、
    p141 澤、p142 楊恩、p143 澤、p144 楊恩、p145–p146 澤。
  - 不同說話者不要合段；同一人連續的段落（例如 p50–p52、p104–p105）也照原文分段。

## 四、伏筆與資訊邊界（不可加暗示）

- p3：建築的列舉（玻璃鋼骨、水泥、石造；高、矮；漂亮、醜）一項不漏。
- p4：路邊堆著「沒人收的」垃圾；「一過高架」幾乎馬上（almost immediately）；牆上投影「有字幕的」電影；楊恩「又轉頭看向左邊」找投影來源；
  「就在計程車快開遠、再也看不見之前」找到投影機；他心想（thought）——就算沒有圖譜募資或規準，「總還是會有人」提供公共財。
- p5：整體「看來」一切如常（seemed）；楊恩「隱約」（just barely）察覺人車「似乎」比平常少。
- p10：往西；「在他看來」過去半年「一直有增無減」（seemed to have been steadily increasing）的修路；避難所也很多，但修路「緊追在後」；「尤其」城北。
- p15：路上「明明比平常空很多」（seems quite a bit less congested）。
- p16：「說是」（they say）充實國防——司機轉述，不表示他相信。
- p19：「其實不是政府」「至少不是直接」；「我聽到一些挺有意思的八卦」。
- p21：「本來是」幾家國防企業的；「紅郡被併吞後沒多久」；賣掉「很多」避難所空間。
- p22：「我想」；「比起乾脆用配給的」少了點；「他們也是在努力」；「我們到頭來根本用不著避難所的機會也就更大」。
- p23：「我總覺得」（getting the feeling）；政府「好像」（seems）特別賣力；「沒有任何勾結的證據」——真有的話法院會狠狠打下來；「我的理論是」——楊恩的推測，不改成斷言；
  「一種」事後獎勵；「付錢給人，卻不用真的直接付錢給他們」。
- p24：「情況真的變糟的話，下一步『可能』就是……」；「不過我想，大家總是可以用飛的」。
- p25：大梅港「一直拒絕」資助任何「可能被看成」跟北極作對的事；「怕」北林的據點「可能」被關掉；「我想到時候就看得出來」。
- p27：沉默了一分鐘；計程車「慢慢停了下來」。
- p35：爸媽要他「回來」；「他們覺得」自由城比其他城市更認真看待國防。
- p37：「最近有一些動作」；「要是真的成了，我會樂觀一點」；「就算成了，我還是擔心」。
- p39：大企業替「所有的」資產保險；「後來……費率『好像』（apparently）又回落了四分之一」。
- p40：「不知怎麼的」（somehow），市場誘因「好像」（seem）有用。
- p41：「多快」；「現在又是」生物安全；「一個月內」；機制「據說」（supposedly）原本是為了升級語言才打造的。
- p42：「我越來越覺得，說不定幾乎任何制度都能……只要大家接受它、相信它」（maybe almost any）。
- p45：「大概知道」（Vaguely）；有些是城市之間打的，也有跟北極人打的。
- p47：「這是很大一部分原因」（a big part of why）。
- p50：「不至於威脅到各城的獨立和各自獨特的文化，但足以讓……沒有誘因完全無視」。
- p52：把政府管制和課稅的權力壓到「最低限度」；性格測驗「不說是做什麼用的」；「政府認為」合得來的結果。
- p54：「方向差不多相反」（somewhat opposite）；「有點像」一所大學；「越推越用力」；「其實」做出了不少好的科學研究。
- p56：「說不定」一個由亞圖利亞人組成的自由城會是災難。
- p57：「不過到目前為止，自由城都撐住了」。
- p59：「偶爾會提起」；「我覺得不太可能」；「我實在很懷疑」（somehow doubt）；技術說明三層（市場、自我表明價值、比政府禁止更好也更文明）一層不漏。
- p60：「我倒覺得，其中『可能』有個核心」（there might be）；「在城市裡尤其得不到」。
- p62：「我真的很喜歡」；「應該說是」整體的知識文化；「就算別人不同意」；貝爾帕基「大家馬上就認定你一定是北極人還是什麼的」。
- p63：「我當然明白他們為什麼絕對不會告訴我們兩個」（初譯漏 why，v2 補回）；四個問句一個不漏。
- p64：「我其實確實知道一些八卦」；「我想我不能跟你說」。
- p68：三個欄位：能籌到多少錢、經濟附帶損害、讓自由城變得不那麼……自由的風險。
- p69：「一長時後」。
- p80：檔案行為：楊恩「當然可以」偷偷存（作業系統）或拍螢幕；「預設」開啟後五分鐘可看、無法複製、時間到自動刪除；「基於禮貌」不去動預設。
- p84：「此時此刻正在發生」。p85：七架；六角形；休眠，等北極無人機「完全」進到裡面。
- p88：「大約」十拍。p96：「照理說要打中兩下」（supposed to be）——主天線與腿，讓它沒辦法離開干擾範圍。p97：「大約」二十拍。
- p100：「其實並不打算擊殺——真要殺的話，第一擊打重一點就解決了」。
- p104：「最好能」被誤認成北極無人機，「甚至」動物；「直到目標快要逃出陷阱時」才擊殺。
- p105：拿北極無人機練殺「代價太高」（expensive）；練活下來「這我們做得到」，「基本上只要兩個三角形裡還有一個活著」；收尾由七架完成，燒毀電路，讓北極拿不到訓練資料。
- p111：兩架「受了傷、但還能動的」干擾無人機「暫時」裝死。
- p119：楊恩話說到一半停住——「他想起自己不該讓澤分心」。
- p121：「我們的 AI 對上北極人的 AI 加真人」；「如果我們的干擾奏效，就是我們的 AI 對他們的 AI」（譯者筆記已定）。
- p122–p125：默默等；十拍／二十拍／三十拍各自成段，保留節奏。
- p130：「只剩一架完好的」；先北極的、再我們自己剩下的，「以防萬一」；趕在更多北極無人機來之前。
- p132：「它們動不了」；「還是可以攻擊」；「最好是」十公分內。
- p133：「沒辦法真的確定」；「只能往好處想了」（hope for the best）。
- p136：北極人沒收了「所有」沒被植入後門的電子裝置；「還藏著不少」；只要有裝置想傳送，北極人「都察覺得到」（will be able to tell）。
- p137：假裝講電話或視訊；裝置放在旁邊「小聲」播放；聽起來是隨機的；技巧是「之前跟你說過、用在健康資料上的」；「盡量多藏」；讓監聽者「都覺得一切正常」。
- p139：「真的」綁架一架北極無人機，帶回哲戈分析。
- p143：「最好不要」透過研究所所長，換一條路。
- p145：所長介紹的那家擅長海上；想找「其他幾家裡」比較擅長空中的。
