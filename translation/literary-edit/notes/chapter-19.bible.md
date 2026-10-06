# 第 19 章 bible 摘錄（第二輪文學編輯用）

主 Agent 依 WORKFLOW「開始一章前」第 5 步建立；每個 chunk 的資料包都附上這份（`literary_edit.py packet --bible`）。
權威來源仍是 glossary／characters／worldbuilding；這裡只是本章會用到的部分，加上本章初譯已定的用詞。
段號為原文段號（`literary_edit.py plan 19` 的 pNNN；與 `translation/notes/chapter-19.md` 的段號相同）。

章節結構：p2 dateline（帕佛蓋都，葡萄季 15 日）｜p3–p75 山體金字塔深處的餐廳：等鄧、保全無人機觸發格拉迪亞斯手錶警示（p8 畫面）、
澤的手錶（p13、p15 畫面）與哲戈語教學、傳檔更新手錶（p33、p38 畫面）、CO2 對話、十號餐、美植美食街的匿名廣播（p60 畫面）、決定去數位典藏節點｜
p76 分隔｜p77–p153 帕佛蓋都大圖書館：門上的畫與標語（p80）、書架迷宮、館員、下載（p102 畫面）、密封杯、建築書、重建資料、
問題畫面（p118）、澤回想火月 10 日（p130–p141 一行一段的清單式短段）、思考中（p143）、技術解說（p144–p152）、德盧因的信（p154 畫面，HTML，不送 editor）。

chunk（`plan 19`）：01＝p3–p59（跨 p8、p13、p15、p33、p38 畫面）｜02＝p61–p75｜03＝p77–p117（跨 p80 標語、p102 畫面）｜04＝p119–p153（跨 p127、p143 畫面）。

### HTML 區塊（不送 editor，一字不動）與 check 的「英文字母偏多」WARN（p15、p60、p80、p102）

- p8、p38：格拉迪亞斯的手錶（空氣／裝置／已認證 ✓／未知，風險升高！）；p13、p15：澤的手錶（哲戈語）；p33：收檔畫面（哲戈語）；
  p60：匿名廣播（哲戈語）；p80：門上標語（哲戈語，意思由 p81 澤口頭翻譯）；p102：下載進度（雜湊值、sho hei dai）；
  p118：問題畫面；p127：餐廳地址（哲戈語）；p143：思考中；p154：德盧因的信（已譯）。
- WARN 全是刻意保留的哲戈語與雜湊值，不是漏譯。散文裡不要替這些畫面補解釋。

## 一、全章固定用詞（editor 一次只看一個 chunk，看不到別處的叫法；這些不要換）

| 原文 | 本章用法 | 出現位置／說明 |
|---|---|---|
| cafeteria | 餐廳 | p3、p17、p75、p128（p128 指美植美食街，原文用 cafeteria，照譯「餐廳」） |
| mountain pyramid | 山體金字塔 | p3、p71、p112 |
| screens … pretend to be windows | 大螢幕……假裝成窗戶 | p3 |
| thirty meters below ground | 地底下三十公尺 | p3 |
| High Council member of the Kungaupei | 昆高派最高議會成員 | p5 |
| Arctic shadow campaign | 北極暗中攻勢 | p5（譯者筆記已定） |
| official government | 官方政府 | p5 |
| drones | 無人機（p6）；robot(s) → 機器人（p21、p25、p27、p47、p105、p111） | 原文 p6 叫 drones、p21 起叫 robots，照各處用字 |
| cheating equipment | 作弊裝置 | p6 |
| Minpentai championships | 明盤台錦標賽 | p6 |
| watch buzzed | 手錶震動／震了一下 | p7、p32、p36、p54、p74 |
| threat／hostile devices | 威脅／有敵意的裝置 | p10、p28 |
| not been updated yet／up to date | 還沒更新 | p10、p28 |
| He clicked on the green | 他點了綠色那一欄 | p14（譯者筆記：指綠字那一列） |
| 'mo fan' is eating room | 「mo fan」是吃飯的房間 | p17（哲戈語字根教學，字面直譯，不要改成「餐廳」） |
| security | 保全 | p23、p25「保全機器人」 |
| interface | 介面 | p26 |
| shrinking the vocabulary | 縮減字彙 | p26 |
| protocols stepped up | 協定加強了 | p29 |
| speak the language | 聽不懂這套語言 | p29 |
| one tick | 一拍 | p32 |
| air sensors／smoke detection and poisons | 空氣感測器／煙霧和毒物 | p42 |
| parts per million | ppm | p43 |
| aerosol particles／airborne viruses | 氣溶膠微粒／經由空氣傳播的病毒 | p43 |
| industrial pollution | 工業汙染 | p44 |
| pandemic prevention | 預防大流行病 | p45 |
| Number Ten | 十號餐 | p48（glossary） |
| Dzego food trucks | 哲戈餐車 | p48 |
| courtyard | 庭園 | p56、p58、p59、p64、p125、p126、p137（glossary：美植美食街的別稱，照原文用字） |
| Beautiful Plants food court | 美植美食街 | p62 |
| Len Su street | 連蘇街 | p62 |
| burned four hundred zipcoins | 燒掉了四百吉普幣 | p62、p64 |
| message envelope | 訊息信封 | p62 |
| 'is successful'／18 years old | 『是成功人士』／18 歲 | p62（worldbuilding） |
| well-calibrated description | 描述……拿捏得真準 | p63 |
| broadcast | 廣播 | p64 |
| sixty gigabytes／eighty percent | 六十 GB／八成 | p69 |
| digital archive node | 數位典藏節點 | p71 |
| green circle | 綠色圓圈 | p74 |
| network of tunnels | 四通八達的隧道 | p75 |
| ornamented door | 裝飾華麗的大門 | p77 |
| river horse／hamster | 河馬／倉鼠 | p78 |
| Outside of a dog … Inside of a dog … | 「在狗之外，書是人類最好的朋友。」……「在狗之內，太暗了，沒法讀。」 | p81（glossary 定句，一字不改） |
| shelf／walkway | 書架／走道 | p83 |
| book-lined hallways | 書廊 | p84 |
| T-shaped intersection | T 字路口 | p84 |
| maze | 迷宮 | p85 |
| computer terminals | 電腦終端機 | p86、p99 |
| robe | 長袍 | p87 |
| Pafogai Du grand library | 帕佛蓋都大圖書館 | p89 |
| the archive | 典藏 | p90（譯者筆記／QA 已定，與數位典藏節點一致） |
| librarian | 館員 | p91、p99、p101、p116 |
| a quest | 一場探險 | p95 |
| hashes | 雜湊值 | p98 |
| data cable | 傳輸線 | p99 |
| hand device | 手持裝置 | p100、p123、p124、p153 |
| stodgy librarians | 我們這些老古板館員 | p104（characters 定） |
| physical spaces | 實體空間 | p104 |
| sealed cup／straw | 密封杯／吸管 | p111 |
| open-faced | 開口的 | p111 |
| basement rooms, shelters and underground rooms | 地下室、避難所，以及山體金字塔內部地下房間 | p112 |
| imitation windows | 仿窗 | p113（glossary） |
| progress bar | 進度條 | p115 |
| script | 腳本 | p115、p117 |
| Reconstructing data... estimated time remaining 175 | 「正在重建資料……預估剩餘時間 175」——不是哲戈語 | p115（譯者筆記已定） |
| timer counting down | 倒數的計時器 | p116 |
| sandbox／journaling file system | 沙盒／日誌式檔案系統 | p123 |
| revert it back to start | 還原到起點／還原重來 | p123 |
| privacy leak | 隱私外洩 | p123 |
| semifinal against Gun | 對君的準決賽 | p125 |
| punchline | 用他的本地 AI 最愛說的話，這就是「笑點」 | p129（glossary 定句） |
| A/B testing the new proposed hieroglyphs | 替哲戈語新提案的象形文字做 A/B 測試 | p138 |
| gently trolling line | 半開玩笑的逗弄 | p141 |
| "I'll use my championship winnings to pay for you to go." | 「我會用我的冠軍獎金替你出旅費。」 | p141（譯者筆記與 QA 已定，人稱不可顛倒） |
| send | 「送出」 | p142 |
| language model | 語言模型 | p144 起 |
| data reconstruction | 資料重建 | p144 |
| overhead | 額外開銷 | p145、p151、p152 |
| background thread | 背景執行緒 | p145 |
| secret key | 祕密金鑰 | p145 |
| health data | 健康資料 | p145 |
| Arctic sermons | 北極的說教 | p145 |
| recombination algorithm／five-of-six erasure code | 重組演算法／六取五抹除碼 | p146（glossary） |
| steganographic encoding | 隱寫編碼 | p146 |
| bits to flip | 可以翻轉的位元 | p146、p151「位元翻轉」 |
| plaintext／ciphertext | 明文／密文 | p146、p150 |
| cryptographic pad | 密碼本 | p146、p147 |
| pseudorandomly … repeatedly hashing | 偽隨機……反覆做雜湊 | p147 |
| throw people off | 混淆視聽 | p148（譯者筆記已定） |
| obfuscated language model | 經混淆的語言模型 | p150（不要寫「混淆語言模型」） |
| level two／level four obfuscation | 二級混淆／四級 | p150–p152 |
| cryptographic-grade parameters | 密碼學等級的參數 | p150 |
| cryptographic networks for voting | 投票用的密碼學網路 | p150 |
| weights／tensors | 權重／張量 | p151 |
| fine-tuned | 微調 | p152 |
| wrapper program | 包裝程式 | p152 |
| tens to low hundreds on size, high hundreds to low thousands on compute | 大小上是幾十倍到一兩百倍，運算上是好幾百倍到一兩千倍 | p152（譯者筆記已定） |

## 二、固定譯名（glossary／characters／worldbuilding）

- 人物：Gladias → 格拉迪亞斯；Zei → 澤；Den → 鄧；Fin → 汾（不要寫「芬」）；Bai → 白；Gun → 君；Deluin → 德盧因；the librarian → 館員
- 組織與制度：Kungaupei → 昆高派；High Council → 最高議會；Bansunpei → 班順派；Order of Steering → 掌舵會；DU → DU（對話中保留）；Minpentai → 明盤台；Arctic Empire／the Arctic(s) → 北極帝國／北極（北極人）
- 地名：Pafogai Du → 帕佛蓋都；Sadzu Du → 薩祖都；Redshire → 紅郡；Veridia → 維瑞迪亞；Dzego → 哲戈；Dzegoban → 哲戈語
- 曆法與時間：Firemoon 10th → 火月 10 日；longhour → 長時（half a longhour → 半個長時）；tick → 拍
- 貨幣：zipcoin → 吉普幣（對話中英文數字寫中文數字：四百吉普幣）；burn → 燒掉
- 技術：local AI → 本地 AI；hand device → 手持裝置（避免：手機）；hash → 雜湊值；gigabyte → GB；erasure code → 抹除碼（避免：糾刪碼）；
  steganographic → 隱寫；obfuscation → 混淆；plaintext／ciphertext → 明文／密文；cryptographic pad → 密碼本（避免：加密墊）；
  tensor → 張量；wrapper program → 包裝程式；journaling file system → 日誌式檔案系統；sandbox → 沙盒；fine-tune → 微調
- 物品：green circle → 綠色圓圈；sealed cup → 密封杯；data cable → 傳輸線（避免：數據線）；Number Ten → 十號餐
- 哲戈語拼音一律保留原樣（mo fan、min、jan、kun gau、jo sun fe zin ten lai de cau tie dai、be、jie hei ja ma?、zui fia pai dan）

## 三、人物口吻與稱謂

- 稱謂：本章鄧沒有出場，**不適用**澤對鄧用「您」的規則；全章沒有「您」，也不要加。
  - 澤 ↔ 格拉迪亞斯：互用「你」；澤說「我們」指哲戈人（p5、p45 的「你們」是格拉迪亞斯指哲戈人）。
  - 館員 → 澤（與格拉迪亞斯）：「你們」（p89）、「你」（p92、p97、p100、p104）。
  - 格拉迪亞斯 → 館員：「你們」（p109，指圖書館／哲戈）。
- 格拉迪亞斯：好奇、愛猜哲戈語字根（p17–p25，猜錯猜對都簡短，「呼，一點都不難嘛！」帶點得意）；談空氣品質時搬數字說教（p41、p43）；p147 一針見血指出密碼本可以偽隨機產生。
- 澤：導遊、老師，回應簡短肯定（「對！」「完全正確。」）；p26 調侃汾；p123 起講技術像報告，條理清楚、句子長，術語準確；p148 坦然承認想太多。
- 館員：風趣、愛挖苦的長輩（p93）；p95 把事情當冒險；p104 自嘲「老古板館員」反問。
- 說話者（**原文未標說話者的輪次一律照初譯，不補標籤**）：
  - p4 格拉迪亞斯、p5 澤（未標）；p9 澤、p10 格拉迪亞斯（未標）、p11 澤；
  - p16 格拉迪亞斯、p17 格拉迪亞斯（續，未標）、p18 澤、p19 格拉迪亞斯、p20 澤、p21 格拉迪亞斯、p22 澤、p23 格拉迪亞斯、p24 澤、p25 格拉迪亞斯、p26 澤（全部未標）；
  - p28 格拉迪亞斯、p29 澤（未標）；p31 澤（壓低聲音說的哲戈語）；p35 澤（未標）；
  - p39 澤或格拉迪亞斯（未標，初譯不點名）、p40 澤、p41 格拉迪亞斯、p42 澤、p43 格拉迪亞斯、p44 澤、p45 格拉迪亞斯、p46 澤（全部未標）；
  - p48 格拉迪亞斯、p49 澤（未標）、p50 格拉迪亞斯（未標）、p52 格拉迪亞斯；
  - p55 格拉迪亞斯、p56–p57 澤（未標）、p58 格拉迪亞斯（未標）、p59 澤（未標）、p61 格拉迪亞斯、p62 澤（未標）、p63 格拉迪亞斯（未標）、p64 澤（未標）、
    p65 格拉迪亞斯（未標）、p66 澤（未標）、p68 格拉迪亞斯、p69 澤、p70 格拉迪亞斯、p71 澤、p72 格拉迪亞斯、p73 澤（全部未標）；
  - p89 館員、p90 澤（未標）、p92–p93 館員、p94 澤（未標）、p95 館員（未標）、p97 館員（未標）、p98 澤（未標）、p100 館員（未標）、
    p103 澤或格拉迪亞斯（未標，初譯不點名）、p104 館員（未標）、p106 機器人、p109 格拉迪亞斯（未標，接 p108；也可能是澤，初譯不點名）；
  - p114 澤；p120 澤（未標）、p122 格拉迪亞斯（未標）、p123–p124 澤；p144 格拉迪亞斯（未標）、p145–p146 澤（未標）、p147 格拉迪亞斯（未標）、
    p148 澤（未標）、p149 格拉迪亞斯（未標）、p150–p152 澤（未標）。
- p136 後半是澤的內心回想（「我當時說了什麼來著……」，第一人稱），引號內是他當時說的話，原文沒有句號，照初譯不加。

## 四、伏筆與資訊邊界（不可加暗示）

- p3：螢幕「竭盡所能地」假裝成窗戶（doing the best job that they could）——語帶幽默，保留；彷彿餐廳在山頂，而不是地底下三十公尺。
- p5：鄧「參與管理」（helps run）昆高派，不是主管；「這十年來」一直替哲戈擋下北極暗中攻勢。
- p6：嗡嗡聲先微弱、很快變大；「幾乎馬上」；「幾架」小型無人機，與明盤台錦標賽檢查澤作弊裝置的那種「很像」（similar）。
- p10：「我想」「我猜」「只是還沒更新」——格拉迪亞斯的推測，保留不確定。「這幾天」一直這樣（for many days now）。
- p26：汾會花上「半個長時」，講每個字的來歷與縮減字彙時為何保留。
- p27：機器人飛近，停在他耳朵右邊「大約半公尺」懸著——不補他的反應。
- p29：「只是」每盞燈、無人機、攝影機在報身分；協定「這幾天加強了很多」；手錶「只是」還聽不懂。
- p30：澤「壓低聲音」（softer voice）。
- p32：「大約一拍之後」，是*格拉迪亞斯*的手錶？——原文 his watch，初譯「他的手錶」不點名，照初譯保留模糊（從 p33 畫面與 p34 看，應是澤的手錶收到資料）；不要自行點名。
- p36：兩支手錶「同時」震動，表示已連上；檔案從一支傳到另一支；格拉迪亞斯按按鈕接收。
- p41：十二公斤；比吃喝加起來還多；「全都低估了」。
- p43：數字 300 ppm、40,000 ppm、700 ppm、百分之一；「要嘛……要嘛——比較有可能——」保留 more likely；氣溶膠「停留很久」，「尤其是」病毒。
- p45：「其實我很意外」；「我還以為」——格拉迪亞斯的評論，不要加強成指責。
- p46：澤把問題推給鄧，語氣輕鬆。
- p47：格拉迪亞斯：沙拉和茶；澤：鋪滿蘑菇的蔬菜飯和茶。
- p48：「我覺得」就是十號餐（I think）。
- p52：「好吃太多了」，興奮。
- p53：「默默」吃了幾分鐘——只寫 silently，不補氣氛。
- p54：眼睛睜得大大的——不補心理。
- p56：「以前……吃過一次」（once）；「這真的很怪」。
- p57：「看起來」是直接寄給我的（seems）。
- p59：庭園「好像」寄給了過去半年的*所有*客人（seems，斜體保留）；標籤讓澤的本地 AI 接收，「幾乎」其他人的都過濾掉。
- p62：「其他我什麼都不知道」。
- p64：範圍夠寬→確保包含澤；燒四百→向庭園、本地 AI、我們三方表示值得花心思；範圍夠窄→*才*（could，斜體保留）只要四百就辦得到。三個理由的邏輯不可混淆。
- p65：格拉迪亞斯補一句：也夠窄，不會有太多人發現。
- p67：澤「又」震驚地瞪著——不補他看到什麼（p69 才說）。
- p69：「超過」六十 GB；「看來」（apparently）要下載其中八成。
- p71：無線「大約一天」；「看起來」數位典藏節點「已經」有足夠的檔案。
- p74：手錶貼綠色圓圈（付款），「片刻後」震了一下；澤先站，格拉迪亞斯「馬上」跟著站。
- p78：兩幅畫都在卡通俏皮與嚴肅神祕感之間「拿捏得恰到好處」（careful balance）。
- p79：*澤*看得懂標語（格拉迪亞斯看不懂）——主詞是澤。
- p83：五公尺高；上半部退後「大約一公尺」；下半部頂端當走道。
- p84：上層兩處、下層一處開口；「看起來」都往裡延伸三到六公尺（seemed）；右轉九十度、左轉九十度、下層 T 字路口——方向不可弄反。
- p85：「看起來」是刻意蓋成迷宮（It looked like），是格拉迪亞斯的想法。
- p87：澤看見穿長袍的女性，「馬上」跑過去（ran）。
- p91：館員笑了。
- p95：「就算最後只是個藉口」，也是她這一天裡新鮮有趣的事。
- p101：下載「幾乎立刻」開始。
- p103：「只要八分鐘」。
- p104：館員的反問：實體空間「終究」（after all）對追求知識還是很重要；「也許」更願意聽了——保留問句。
- p107：菜單沒有食物，有幾種飲料。
- p108：格拉迪亞斯「馬上」點茶；澤「跟著」點一樣的。
- p110：當下沒心情費力讀哲戈語，「尤其是」舊書的早期版本哲戈語他「一個字也看不懂」；所以看圖表和插圖。
- p111：「兩分鐘後」；密封杯只能用吸管喝；格拉迪亞斯「很意外」轉頭；澤坐在遠離所有書的桌邊，「已經」拿到茶；澤的杯子是開口的，幾乎沒什麼防灑——不要替讀者解釋原因（保護書），讓對照自己說話。
- p112：書大致按時間順序，從「百年前」與北極帝國那場戰爭後「不久」開始。
- p113：早期：實用，幾乎沒考慮舒適，「甚至」沒考慮防範非人為威脅；中期：像普通房間，最明顯的例外是沒窗；後期：裝潢好、舒適，「甚至比地面建築還舒適」；「大約一半」有仿窗；另一半沒窗，改擺植物、裝飾牆面與其他「看得出是精心挑選的」（seemed carefully chosen）物件，讓人看不到任何「會讓人覺得應該有扇窗」的空間。
- p115：他一走到，最後一條進度條就到 100%；另一個視窗「自動」開啟；腳本畫面「不是哲戈語」。
- p116：兩人啜茶盯著計時器；館員「很好奇」，靜靜在身後「大約兩公尺」處徘徊（hovered）。
- p117：「果然」準時（Right on schedule），「不到兩分鐘」。
- p119：澤盯著——不補心理。
- p120：「我有預感」（I have a feeling）。
- p123：沙盒→連不上網路、隨時可還原到起點→沒有隱私外洩風險、不滿意可重來；「那何樂而不為？」。
- p124：「還是說」直接問手持裝置。
- p125：最後一場明盤台比賽，對君的準決賽；「至少還算」正常的最後一天（at least somewhat normal）；比賽前起床、和白見面；比賽後和德盧因在庭園碰面。
- p128：「正是」最初那則訊息發出的那間餐廳（exact same）。
- p129：結合 AI 紀錄和自己「迅速恢復」的記憶。
- p130–p135、p138–p140：清單式短段，一行一段，保留這個節奏（不要合段成散文；段數照原文最好）。
- p136：澤當時那句話照本章原文，不去對齊 ch14（譯者筆記：記憶有落差）。
- p137：花在這件事上的篇幅「跟那一天其他所有事加起來一樣多」。
- p141：德盧因「半開玩笑的逗弄」（gently trolling）；人稱「我……替你」不可顛倒。
- p145：數字：10.7 GB、六倍、六分之一（電影）＋一半（健康資料）＋三分之一（AI 生成影片）＝1；「看起來」是 AI 生成（seemed）；*他們選了哪幾部電影*（斜體保留）「算是某種」祕密金鑰（of sorts）；北極說教講維瑞迪亞和哲戈文明有多「根本上」的缺陷。
- p146：五份各 10.7 GB；每四個位元密文承載一個位元明文（「非常大膽的比率」）；電影是「某種」密碼本；「就算」能完整還原明文，看起來也只是隨機資料。
- p147：格拉迪亞斯的反問保留問句。
- p148：「其實你說得對」；「也許……也許……」兩個也許都留。
- p150：二級混淆；參數比完整密碼學等級「弱得多」；後者用在 DU、班順派、「或者說」掌舵會投票的密碼學網路；但演算法是同一套。
- p151：二級是「正確的取捨」，理由兩個：模型又大又吃運算→承受不了四級的高額外開銷；模型「本身至少有一部分」是混淆的、能抵抗位元翻轉。挖出幾個權重、或能「穩定地」翻轉幾個張量裡的幾個值，也得不到有用的東西。
- p152：數字範圍照譯者筆記；「所以」這個模型「非常小」（pretty tiny）；「我猜」寄件人微調到只做這件事；「我也覺得」包裝程式一口氣把思考全部做完，來驗證答案能不能讓它滿意；「如果可以」，最後就直接交出訊息。
- p153：「彷彿算準了時機」（As though on cue）——原文自帶的比喻，保留；程式執行完畢；出現新訊息。
- 不要提前暗示信的內容（德盧因的父母、北極）；p145 的北極說教影片只是素材，不要解讀。
