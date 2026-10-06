# 第 23 章 bible 摘錄（第二輪文學編輯用）

主 Agent 依 WORKFLOW「開始一章前」第 5 步建立；每個 chunk 的資料包都附上這份（`literary_edit.py packet --bible`）。
權威來源仍是 glossary／characters／worldbuilding；這裡只是本章會用到的部分，加上本章初譯已定的用詞。
段號為原文段號（`literary_edit.py plan 23` 的 pNNN；與 `translation/notes/chapter-23.md` 的段號相同）。

章節結構：p2 dateline（帕佛蓋都，霧季 22 日）｜p3–p73 金字塔地底餐廳：澤打完無人機回來、談自由城與維瑞迪亞、汾拿哲戈語書考格拉迪亞斯（p22 書頁畫面）、
澤講網路極簡主義、澤背掌舵會與法院的規則、維爾的官司、白提醒鄧在等、搶著付帳｜p74 分隔｜p75–p100 格拉迪亞斯睡前接到賽菈的紅色通話請求（p76 畫面）：莉莉在聊天群組分享北極宣傳、出走、兩人爭吵、賽菈掛電話。

chunk（`plan 23`）：01＝p3–p21｜02＝p23–p73｜03＝p75（單句）＋p77–p100。

### HTML 區塊（不送 editor，一字不動）

- p22：哲戈語書頁（全是羅馬拼音，原樣保留）。p76：通知表（寄件者 賽菈／→／［請求通話］／91454，紅字）。散文不要替它們補解釋。

### ⚠ 第 26–51 段：格拉迪亞斯逐字硬翻哲戈語（最重要的限制）

- 格拉迪亞斯唸的句子（p26、p30、p32、p34、p36、p38、p40、p41、p43、p45、p47、p49、p51）是**刻意生硬的直譯**，是情節本身（他哲戈語不好，只會照字根拼）。**不可改通順、不可改用詞**：
  「從物質世界小思考，到網路小思考。」「包在綠色裡面，四十年前，全世界美思考的一個大的模式改變，是極簡主義。」
  「很多人認識到，擁有很多實體的東西不只是線心，也是一個上鎖的房間。」「複雜的房間意味著複雜的心。」
  「帶著擁有很少東西的暖心——快樂？——生活，是自由。」「這件事在四十年前發生，有一個邏輯——理由？」「電的機器和網路開始存在。」
  「這意味著很多人收集了實體的東西……等等，是很多人收集的實體東西，開始變得不被想要。」（「了／的」一字之差重現誤讀與自我更正）
  「手持裝置使不需要了聚合分組裝置、音樂裝置、聲音對話裝置，和以前一個人會有的其他十種裝置。」「它可以裝下沒有上蓋的書。」
  「我們全部活的許多部分，正在搬到電的世界。」「結果，實體世界的複雜停在了後面。」「在附近的幾年，我們正在尋找一個不同的模式改變。」
  這些句子**原樣保留**（editor 輸出時直接照抄初譯）。
- 汾的更正用正常中文（「小思考就是極簡主義。」「美思考就是美學。」「線心是一種簡單、或者說方便的感覺；上鎖的房間在這裡比較接近牢籠。」
  「這裡我會說『不需要』。」「聚合分組裝置應該是加和乘的裝置——計算機。聲音對話裝置是電話。」「無上限。」「我們所有人生活的許多部分。」「是被留在了後面。」），
  更正必須對得上被更正的生硬字眼（小思考、美思考、線心、上鎖的房間、不被想要→不需要、聚合分組裝置、聲音對話裝置、沒有上蓋→無上限、我們全部活的→我們所有人生活的、停在了後面→被留在了後面），所以這些字眼一個都不能換。
  汾的更正句可以小幅順口，但不要改掉被引用的那個詞。
- p31「開頭那句是固定說法，意思是『包括哲戈和維瑞迪亞』」：glossary Containing inside the green → 包在綠色裡面。
- 這一段一句一段、一人一輪，**不要合段**。

## 一、全章固定用詞（editor 一次只看一個 chunk，看不到別處的叫法；這些不要換）

| 原文 | 本章用法 | 出現位置／說明 |
|---|---|---|
| cafeteria | 餐廳 | p3–p6、p73 |
| mountain pyramid | 山體金字塔 | p3 |
| vines／large mirrors／endlessly-repeating infinitely large space | 藤蔓／大片鏡子／無限重複、無邊無際的空間 | p4 |
| entrance tunnel／shrubs | 入口隧道／灌木 | p4、p6 |
| air filters | 空氣清淨機 | p5 |
| downward-pointed fans and violet lights | 朝下吹的風扇和紫光燈 | p5（譯者筆記：不補遠紫外線） |
| private area | 隱密的區域 | p6 |
| simulating the sound of cicadas buzzing in a forest in the morning | 模擬著清晨森林裡的蟬鳴 | p6 |
| ambushed by some Arctic drones | 中了一群北極無人機的埋伏 | p8 |
| swarm | 機群 | p8 |
| chips … training data | 晶片……訓練資料 | p8 |
| the Freetown folks | 自由城那邊的人 | p9 |
| Kungaupei | 昆高派 | p11 |
| quick wins | 速效成果 | p12 |
| legitimacy by performance | 以績效建立正當性 | p12 |
| defense corps | 國防企業 | p13 |
| work around their institutions | 繞過他們的體制 | p13、p14 |
| scale | 規模 | p14 |
| bring … institutions onto your side | 把一些比較大的體制拉到你這邊來 | p14 |
| Verdow's contact／senator | 韋爾多的聯絡方式／參議員 | p16 |
| robot | 機器人 | p17 |
| Dzegoban | 哲戈語 | p20 |
| roots／shrinking the roots down | 字根／縮減字根的計畫 | p28、p29 |
| minimalism／internet minimalism／physical minimalism | 極簡主義／網路極簡主義／實體極簡主義 | p27、p30、p57 |
| mental health | 心理健康 | p55 |
| public discourse | 公共話題 | p55 |
| privacy technology | 隱私技術 | p56 |
| location tracking, behavior profiling | 位置追蹤、行為側寫 | p56 |
| addictive as drugs | 像毒品一樣讓人上癮 | p56 |
| Disconnect. Do things on your own device. | 斷開連線。在自己的裝置上做事。 | p57 |
| AI and local software | AI 和本地軟體 | p57 |
| Order of Steering's governance rules | 掌舵會的治理規則 | p60 |
| tax rubrics | 稅務規準 | p61 |
| twenty one Keepers／seven added in each year／three year term | 二十一名守律者／每年補進七人／任期三年 | p61 |
| sub-groups of seven | 三個七人的子小組 | p61 |
| first, second and third years | 第一年、第二年和第三年的成員 | p61 |
| at least thirteen out of twenty one | 二十一票中至少有十三票贊成 | p61 |
| Sentinels／audit individual businesses／three groups of three | 哨兵／稽核個別企業／三組、每組三人 | p62 |
| tier on each rubric | 在每條規準上屬於第幾級 | p62 |
| Acolytes, Order members in training | 見習生，也就是受訓中的掌舵會成員 | p62 |
| Senate committee approval | 參議院委員會的核准 | p62 |
| top ten percent by prediction score | 預測分數要排在前一成 | p62 |
| Courts／five judges instead of nine | 法院／法官是五個人，不是九個 | p63–p64 |
| civil cases／criminal cases／the defense | 民事案件／刑事案件／被告方 | p64 |
| no hierarchy | 沒有上下級 | p64 |
| common law rule／bad-faith／penalty judgement | 普通法規則／惡意／懲罰性判決 | p64 |
| denial of service attacks | 我們所說的『阻斷服務攻擊』 | p64 |
| My co-father, Vil | 和我們家共養孩子的維爾 | p65（glossary：co-father→共養孩子的；避免「共養父親」） |
| severance | 資遣費 | p65 |
| struck down … declared it bad faith, and tripled | 駁回……判定那是惡意上訴……提高成三倍 | p65 |
| Parliament hearings approving new Keepers and Sentinels | 議會核准新任守律者和哨兵的聽證會 | p67 |
| private room | 私人房間 | p70 |
| small green circle on the corner of the table | 桌角的小綠色圓圈 | p72 |
| slapped his watch against the circle | 一掌把手錶拍在圓圈上 | p72 |
| shade of red | 這種深淺的紅色 | p77 |
| Emerald | 翡翠 | p78 |
| chat group | 聊天群組 | p85 |
| Arctic propaganda | 北極帝國的宣傳 | p85 |
| Lord Ephelion's messages | 艾費里昂勳爵的那些文章 | p85 |
| come to the rest of Veridia | 來到維瑞迪亞其他地方 | p85（中性，不寫成「打到」） |
| I snapped. I called her out on it | 我當場就爆了。我當面質問她 | p87 |
| a thousand kilometers away | 一千公里外 | p87 |
| unconditional love was poison | 無條件的愛是毒藥 | p89 |
| appreciation and love only as reward for success | 只把欣賞和愛當成成功的獎賞 | p89 |
| out of her hole | 從谷底拉了出來 | p89 |
| longhour | 長時 | p92 |
| autobus | 自駕巴士 | p94 |
| brainwashed | 洗腦 | p96 |
| philosopher mood | 擺出那副哲學家的樣子 | p96 |
| negligent | 失職 | p97 |

## 二、固定譯名

- 人物：Gladias → 格拉迪亞斯；Bai → 白（女）；Fin → 汾（男）；Zei → 澤（男）；Seila → 賽菈；Lily → 莉莉；Febric → 費布里克；Hreda → 赫蕾妲；Vil → 維爾；Daia → 黛亞；
  Mov → 莫夫；Delwart → 德爾瓦特；Ephelion → 艾費里昂（勳爵）；Verdow → 韋爾多；Den → 鄧；Emerald → 翡翠（賽菈家的本地 AI）
- 地名：Pafogai Du → 帕佛蓋都；Dzego → 哲戈；Veridia → 維瑞迪亞；Freetown → 自由城；Northglade → 北林
- 組織／制度：Kungaupei → 昆高派；Order of Steering → 掌舵會；Keeper → 守律者（避免：守護者）；Sentinel → 哨兵；Acolyte → 見習生（避免：侍僧）；rubric → 規準（避免：評分標準）；
  sub-group → 子小組；audit → 稽核（避免：審計）；prediction score → 預測分數；Senate committee → 參議院委員會；Parliament → 議會（避免：國會）；Courts → 法院；
  bad faith → 惡意；common law → 普通法；legitimacy → 正當性（避免：合法性）；severance → 資遣費（避免：遣散費）
- 物品：hand device → 手持裝置（避免：手機）；watch → 手錶；autobus → 自駕巴士；green circle → 綠色圓圈
- 單位：longhour → 長時

## 三、人物口吻與稱謂

- 稱謂：全章沒有「您」，不要加。
- 格拉迪亞斯：對澤是導師口吻（p11–p14 給建議）；唸哲戈語時笨拙、自嘲；被賽菈罵時先自責（p95），再冷靜回嘴、要求共同承擔（p98）。
- 汾：像嚴格又帶笑的語言老師（「來嘛，試試看。」「很好！」「太好了！」）。
- 澤：剛打完仗、累壞；講網路極簡主義與制度規則時像背課文，條理分明。
- 白：p69 正式、肯定兩人。
- 賽菈：⚠ 情緒最激烈的段落之一（與 ch21「白痴」同級，不要軟化）。全大寫處用「？！」「！」與「吼道」，不加字；生氣時叫全名「格拉迪亞斯」。
  p96「你敢給我擺出那副哲學家的樣子，跟我說他們講得有道理試試看！」p97「你怎麼可以這麼失職？！」p99「你根本一點都不懂，對不對？！」
- 說話者（**原文未標說話者的輪次一律照初譯，不補標籤**）：
  - p8 澤；p9–p16 全部未標（譯者筆記判斷：p9、p11、p12、p14、p16 格拉迪亞斯，p10、p13、p15 澤；p12 也可能是白），**不點名**。
  - p20 汾；p23 格拉迪亞斯；p24 汾（未標）；p25 格拉迪亞斯（未標）；p26 起格拉迪亞斯唸、汾更正交替（全部未標）；p53 格拉迪亞斯；p55–p57 澤；p58 格拉迪亞斯（未標）；
    p59（未標，汾或澤，不點名）；p60 格拉迪亞斯（未標）；p61–p62 澤（未標）；p63 格拉迪亞斯（未標）；p64 澤（未標）；p65 格拉迪亞斯（未標）；p66（未標，不點名）；
    p67 格拉迪亞斯（未標）；p69 白；p70（未標，不點名）；p71 澤。
  - p80 賽菈；p81 格拉迪亞斯（未標）；p82–p83 賽菈；p84 格拉迪亞斯；p85 賽菈；p86 格拉迪亞斯；p87 賽菈；p88 格拉迪亞斯；p89 賽菈；p90 格拉迪亞斯；p91–p92 賽菈；
    p93 格拉迪亞斯；p94 賽菈；p95 格拉迪亞斯；p96–p97 賽菈；p98 格拉迪亞斯；p99 賽菈（全部未標，除 p80 screamed）。
  - 不同說話者不要合段；同一人連續兩段（p82–p83、p91–p92、p96–p97、p55–p57、p61–p62）也照原文分段。

## 四、伏筆與資訊邊界（不可加暗示）

- p3：「深埋地底」，山體金字塔內部。
- p4：餐桌與牆之間「四面」都是綠樹；兩面藤蔓、兩面鏡子；鏡子讓房間「彷彿」（seem like）是無限空間的一部分（初譯「彷彿」是原文 seem 的對應，不是套語）；唯一入口在「其中一個角落」，兩側各一叢灌木擋住通往入口隧道的視線。
- p5：另一個角落、以及餐廳中央離他們「幾公尺遠」的地方；空氣清淨機「顯然是最近才添的」，還沒怎麼花心思讓它們融入。
- p6：三人在隱密區域；灌木擋住餐廳其他「大部分」地方；蟬鳴蓋過其他桌的談話——「他們知道」，這也保護了自己的談話。
- p7：澤「看得出累壞了」。
- p8：「差一點就打不贏」（just barely managed to beat）；「整整五分鐘」；「我想我們應該都毀掉了」（I think）。
- p11：「我就說吧」；讓昆高派「慢慢習慣」（warm … up to）更多國際合作。
- p12：「盡快」；讓大家信任你走下一步。
- p13：「我猜」（suspect）下一步更難；自由城的國防企業「是想合作的」；維瑞迪亞要繞過體制「難多了」。
- p16：「說她會想想辦法」；韋爾多「到目前為止」是他「唯一真正信任」的參議員；「所以，再看看吧」。
- p17：四人份；安靜地吃。p18：汾和格拉迪亞斯先吃完，休息「幾分鐘」喝茶。
- p21：「隨手」翻到一頁。
- p23：「不敢置信地」問。
- p28：光知道字根「根本」讀不通。p29：整個縮減字根的計畫，「在我們接受這種情況免不了之後，才終於成功」。
- p52：停頓了「一會兒」（a few moments）。
- p55：社群媒體「不見得都是」好事；人們關心隱私「不只是」因為害怕北極人，更是因為人人議論別人「量多到驚人」，以及私生活小事變成公共話題的「不可預測」。
- p56：在隱私技術沒那麼強、也沒那麼被了解的「其他國家」更是如此；「不只是」隱私。
- p57：「慢慢」看到；類比（實體極簡主義靠數位世界的能力、網路極簡主義靠 AI 與本地軟體的能力）兩邊都要在；「整個世界」放在自己的裝置上。
- p61–p62、p64：制度數字一個不漏（二十一、七、三年、三個七人子小組、十三票、三組三人、前一成、五個、九個）；
  p61 各子小組「彼此不知道其他子小組是誰」；p62 預測分數＝被「隨機抽出、由哨兵重做」的那一小部分與哨兵結果的吻合度；
  p64 民事雙方、刑事只有被告方可上訴；沒有上下級，只是再抽一組；毫無理由「到構成惡意的程度」→「可能不只」敗訴，「甚至」懲罰性判決。
- p65：「基本上就是」他的前雇主；財務花招開除他、想不付「事先談好的」資遣費；第一回合贏、公司上訴又輸、再上訴；「就在昨天」駁回第二次上訴、判惡意、金額提高成三倍（付給維爾和其他員工）。
- p67：聽證會「到現在幾乎已經完全不管用了——至少我是這麼看」。
- p69：「這麼快」就摸熟；跟軍事那一面「一樣重要」。
- p70：「我想」鄧應該在等。
- p72：兩人「同時」搶著貼手錶，互相把對方手腕推太遠、都沒感應到；汾一掌拍上；「片刻之後」他的手錶震了一下——不補說明誰付帳。
- p75：躺在床上「正準備」睡覺；「突然」。
- p77：這種紅色他「以前只見過兩次」：北林遭攻擊時賽菈的訊息、她為德爾瓦特的事打來。
- p78：翡翠在傳達重要程度和賽菈的情緒——「格拉迪亞斯知道」，光這些就已經是訊息的一大部分。
- p79：心跳加速，接起電話。
- p81：「我只記得聽說」八十一分。
- p82：「一邊講話，一邊在手持裝置上打字」；「從鏡子裡」看得到她在讀什麼、說什麼。
- p83：「有好幾分鐘」只是盯著看。
- p85：「某個」聊天群組；分享宣傳、替文章叫好、「盼著」北極人「很快」也會來到維瑞迪亞其他地方。
- p87：「當面質問」；費布里克和赫蕾妲「因為他們」被困在一千公里外。
- p89：莉莉的說法照轉述（她的論點，不加作者評價）：有些人較差、有些較好、較好的人應統治其他人、人生最重要的是努力成為較好的人——這激勵了她、給她理由讀書用功；
  無條件的愛是毒藥；只把欣賞和愛當成功的獎賞——「真的」把她從谷底拉出來，而我們做的一切「連一點點」忙都沒幫上。
- p91：吼了「十分鐘」，然後把門關上。p92：哭了「一長時」；再打開門時，窗戶開著，她已經不見了——不補她怎麼離開。
- p94：「我已經找莫夫查過了」；她把手錶丟上「一輛不知道開去哪裡的」（some random）自駕巴士。
- p95：「我們真的從來沒有做過什麼，去真正激勵她、鼓勵她」。
- p98：「沒看穿德爾瓦特，那是我的錯」；三個時期（她去維爾和黛亞家之前、住在他們家那段時間我們去探望時、她回來以後）一個不漏；「跟我一樣」兩次對稱。
- p100：賽菈掛斷了電話。
