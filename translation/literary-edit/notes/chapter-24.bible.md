# 第 24 章 bible 摘錄（第二輪文學編輯用）

主 Agent 依 WORKFLOW「開始一章前」第 5 步建立；每個 chunk 的資料包都附上這份（`literary_edit.py packet --bible`）。
權威來源仍是 glossary／characters／worldbuilding；這裡只是本章會用到的部分，加上本章初譯已定的用詞。
段號為原文段號（`literary_edit.py plan 24` 的 pNNN；與 `translation/notes/chapter-24.md` 的段號相同）。

章節結構：p2 dateline（帕佛蓋都，霧季 27 日）｜p3–p18 格拉迪亞斯徹夜未眠，打給茲文：保持和莉莉聯絡（媽已經交代過了）｜
p19 分隔｜p20–p29 走向圖書館：住在山體金字塔地底第八天、產業搬進金字塔、空氣清淨機與紫外線燈、餐廳的樹｜p30 哲戈語標語（dz-card，不送 editor）｜
p31–p63 圖書館：標語的意思、白抱他、北極的「有條件的愛」、白的童年、好奇心、沒有萬用公式、要當一兩成北極人｜
p64 分隔｜p65–p96 鄧的房間：格拉迪亞斯提議「監視我們」、三點理由、澤的看法、保全攝影機。

chunk（`plan 24`）：01＝p3–p18｜02＝p20–p29｜03＝p31–p63｜04＝p65–p96。本章沒有 device-view 裝置畫面。

### HTML 區塊（不送 editor，一字不動）

- p30：圖書館門頂的哲戈語標語（羅馬拼音）；p32 是它的英文釋義，照譯。

## 一、全章固定用詞（editor 一次只看一個 chunk，看不到別處的叫法；這些不要換）

| 原文 | 本章用法 | 出現位置／說明 |
|---|---|---|
| The time just hit 20,000 | 時間剛到 20,000 | p3（初譯用阿拉伯數字，保留） |
| three of the four children he loved dearly | 他深愛的四個孩子裡，有三個 | p4 |
| in the hands of the Arctics | 落在北極人手裡 | p4 |
| vote of non-confidence | 投下不信任票 | p5 |
| He could not go to sleep… ×3 | 「他怎麼也睡不著」「這樣他也睡不著」「那他就*更*不可能睡得著了」 | p4–p6（譯者筆記：排比放句尾，層層加碼，第三段斜體） |
| redeeming himself in Seila's eyes | 在賽菈眼中挽回自己 | p7 |
| unorthodox | 不太尋常 | p7、p75 |
| icon went green | 圖示……變綠了 | p11 |
| my sister | 我姊 | p14 |
| *exactly* | *完全* | p18 |
| longhour | 長時 | p18、p23 |
| hotel area／tunnel | 飯店區／隧道 | p20、p65 |
| mountain pyramid | 山體金字塔 | p21、p22、p25 |
| "important business" | 「重要業務」 | p21 |
| de-facto Kungaupei advisor | 昆高派的實質顧問 | p21 |
| perimeter halfway up | 半山腰一圈 | p22 |
| library | 圖書館 | p22、p24、p28、p33 |
| Verdow | 韋爾多 | p22、p87 |
| Veridian military | 維瑞迪亞軍方 | p22、p74 |
| side rooms | 側室 | p24 |
| High-tech industry … biomedical, chip manufacturing, car production | 高科技產業——生醫、晶片製造，甚至部分汽車生產 | p25 |
| successful Arctic attack | 北極人對哲戈得手的攻擊 | p25 |
| annexed | 被併吞 | p25 |
| air filters and ultraviolet lamps | 空氣清淨機和紫外線燈 | p26 |
| Dzegojan manufacturers and the Bansunpei | 哲戈的製造商和班順派 | p26 |
| cafeteria | 餐廳 | p27 |
| clay pots | 陶盆 | p27 |
| triple role | 身兼三職 | p27 |
| slogan at the top of the door | 門頂上的標語 | p29 |
| admonishment | 告誡 | p33 |
| green circle | 綠色圓圈 | p33、p65 |
| computer terminals | 電腦終端機 | p34 |
| I'm fine | 沒事（p38 白接「你不是沒事」） | p37（style guide 已定） |
| the source of your darkness | 心情低落的原因 | p38 |
| Arctic propaganda | 北極的宣傳 | p41 |
| Lord Ephelion's sermons | 艾費里昂勳爵的那些說教 | p41 |
| ran away from home | 離家出走 | p41 |
| unconditional love | 無條件的愛 | p43、p49 |
| constant background radiation | 持續存在的背景輻射 | p43（glossary） |
| reward for winning | 勝利的獎賞 | p43、p49 |
| equal humanity | 同等的人性 | p44 |
| my aunt | 阿姨 | p49（ch09 已定） |
| social skills | 社交技巧 | p49 |
| second place in the Pafogai Du Minpentai games | 帕佛蓋都的明盤台比賽拿到第二名 | p49 |
| Curiosity. | 好奇心。 | p53 |
| poison／Love as a reward for weakness | 毒藥／把愛當成軟弱的獎賞 | p55 |
| false god of greed … true religion | 貪婪這個假神……真正的宗教 | p58 |
| resentment | 反感（p58）／怨恨（p61） | 初譯兩處用字不同，各自保留 |
| master formula／bags of tricks／one size fits all | 萬用公式／一套方法／適用所有人 | p61 |
| at least ten or twenty percent Arctic | 至少一兩成北極人 | p63 |
| *she*／*will* | *她*／*能* | p63 |
| sealed door | 密封的門 | p65 |
| shadowy cloak | 暗色斗篷 | p66 |
| mi cin pin fe lo kin do | mi cin pin fe lo kin do（哲戈語，原樣） | p69 |
| Spy on us. | 監視我們。 | p77 |
| infiltration／intrusion | 滲透 | p80、p81、p93 |
| corrupted | 收買 | p80（兩次，排比保留） |
| the Order of Steering, Graph Funding and the Courts | 掌舵會、圖譜募資和法院 | p80 |
| spy on the spies | 監視那些間諜 | p81 |
| central institutions | 中央體制 | p81 |
| late in the game | 這盤棋已經下到很後面了 | p85 |
| A ninth intervention turn | 第九個干預回合 | p85（glossary） |
| one-word suggestion 'spy' | 『監視』這兩個字的建議 | p86 |
| Keepers | 守律者 | p86 |
| cryptographers | 密碼學家 | p90 |
| Freetown corps | 自由城國防企業 | p90 |
| fabs | 晶圓廠 | p91 |
| security cameras | 保全攝影機 | p92 |
| cryptographically enforced limits | 以密碼學強制限制 | p92 |
| watered down | 放寬 | p92 |
| administrative change by the Transportation Ministry | 交通部的一項行政變更 | p92 |
| backdoor | 植入後門 | p92 |
| Yes? | 對啊？ | p94、p96（保留問號的語氣） |

## 二、固定譯名

- 人物：Gladias → 格拉迪亞斯；Seila → 賽菈；Zven → 茲文；Lily → 莉莉；Febric → 費布里克；Hreda → 赫蕾妲；Bai → 白（女）；Zei → 澤；Den → 鄧；Verdow → 韋爾多；Ephelion → 艾費里昂（勳爵）
- 地名：Pafogai Du → 帕佛蓋都；Dzego → 哲戈；Veridia → 維瑞迪亞；Northglade → 北林；Freetown → 自由城
- 組織／制度：Kungaupei → 昆高派；Bansunpei → 班順派；Order of Steering → 掌舵會；Graph Funding → 圖譜募資；Courts → 法院；Keeper → 守律者；
  Transportation Ministry → 交通部；intervention turn → 干預回合
- 物品：watch → 手錶；green circle → 綠色圓圈；shadowy cloak → 暗色斗篷
- 其他：Minpentai → 明盤台；background radiation → 背景輻射；longhour → 長時

## 三、人物口吻與稱謂

- 稱謂：全章沒有「您」，不要加。茲文叫格拉迪亞斯「爸」，提到賽菈說「媽」，莉莉是「我姊」。
- 格拉迪亞斯：徹夜未眠、低落；對白話少（「沒事。」低聲、語氣平板）；p41 一口氣說出三件事；對鄧提議時回到理性、有條理（第一、第二、第三）。
- 茲文：孩子口吻，熱心（「當然！為了我姊，什麼都願意。」）；p18 有點得意又無奈。
- 白：成熟、說理的長段；坦白自己的童年，不煽情；用「好奇心」「怨恨」等詞時冷靜。
- 鄧：沉穩、刻意不露情緒（p78）；客氣地考驗人（p79「不過我想聽聽你的理由」）。
- 澤：像技術報告。
- 說話者（**原文未標說話者的輪次一律照初譯，不補標籤**）：
  - p9 茲文、p10 格拉迪亞斯、p11 茲文、p12–p13 格拉迪亞斯、p14 茲文、p15 格拉迪亞斯、p16 茲文、p17 格拉迪亞斯、p18 茲文（全部未標）。
  - p36 白、p37 格拉迪亞斯、p38–p39 白（未標）、p41 格拉迪亞斯（未標）、p42 白、p43–p44 格拉迪亞斯、p45 白、p46 格拉迪亞斯、p47 白、p48 格拉迪亞斯、p49 白、p50 格拉迪亞斯、
    p51 白、p52 格拉迪亞斯、p53 白、p55 格拉迪亞斯、p56 白、p57 格拉迪亞斯（未標，譯者筆記）、p58 白、p59 格拉迪亞斯、p60 格拉迪亞斯或白（未標）、p61 白、p62 格拉迪亞斯、p63 白。
  - p67 鄧、p68 澤、p69 格拉迪亞斯、p70–p71 鄧（兩段）、p73 鄧、p74–p75 格拉迪亞斯、p76 鄧、p77 格拉迪亞斯、p79 鄧、p80–p81 格拉迪亞斯、p82 鄧、p83 格拉迪亞斯、p84 鄧、
    p85–p87 格拉迪亞斯、p88 鄧、p89 澤、p90 鄧、p91 澤、p92（未標：格拉迪亞斯或澤，不點名）、p93 鄧、p94 格拉迪亞斯、p95 鄧、p96 格拉迪亞斯（p93–p96 未標，不點名）。
  - 不同說話者不要合段；同一人連續的段落也照原文分段。

## 四、伏筆與資訊邊界（不可加暗示）

- p3：整夜沒睡；試著睡了「兩次」，每次「二十分鐘」就放棄。
- p4：四個孩子裡有三個「以這樣或那樣的方式」（in one way or another）落在北極人手裡（費布里克、赫蕾妲困在大梅港，莉莉被宣傳吸引）。
- p5：賽菈投下不信任票，「然後」切斷聯絡，「連道歉都來不及」。
- p6：*更*（definitely，斜體）；兩件事「同時」；能抱一抱、給他安慰的人「都」遠在幾千公里外。
- p7：挽回自己與女兒安危「分量不相上下」（thinking as much about … as about）——原文的自嘲誠實，不改成單純擔心女兒。
- p8：「馬上」就接了。
- p11：「大概」四十分鐘前；「我想」是新的裝置。
- p15：四件事：保持聯絡、主動問近況、不表現不贊成、甚至表示同情；目的：弄清楚她在哪裡。
- p18：*完全*；媽「一個長時前」；「很多」該說、不該說的好建議。
- p21：「第八天」；「完全」住在地底；剛到哲戈「不久」就被遷來；新的「建議」（recommendations，不是命令）；「當然」符合資格。
- p22：「兩個多月」；每天散步二十分鐘；「有時」走得更遠；「過去幾天」每天待在圖書館；「幾乎每天」和韋爾多通話。
- p23：「昨晚的事」；只睡了「一長時」；完全提不起勁「出門」（go outside）。
- p24：走得很慢，停下來好多次，盯著牆與經過的側室。
- p25：「他注意到」；自從他住進來以後；「這麼一想」，自從北林被併吞以來，新聞上沒有「任何一次」北極人對哲戈「得手」的攻擊。
- p26：「多了十倍以上」；「至少」……做得很好，他想。
- p27：「約」兩公尺高；綠意「似乎」身兼三職（seemed），三項一項不漏。
- p28：「大約」十五分鐘。
- p33：「出乎意料」；「一小股」力氣；足以抬手按綠色圓圈開門。
- p38：兩個「我也夠了解」的對稱；硬逼你說只會讓你「更」難受。
- p41：「這一年來」；說教讓她覺得被重視、被欣賞「比我給過她的都多」；「不到一分鐘後」；「再過一分鐘」。
- p43–p44：北極論點照轉述（格拉迪亞斯轉述，不加評價）。
- p45：「我有點同意」（kind of）。
- p47：「絕對不是」；「如果你真這麼想」——原文 If you think it does 的推論鏈保留；「比較是」（more）。
- p49：父母死於北極人「引起的」爆炸；阿姨「基本上就是」不理她；「十二歲」；社交技巧「都是」從那裡學來的；別人的欣賞「只有在」……的時候；第二名「就是因為這樣」。
- p51：澤的動力「更純粹，也更美」——比較對象是白想證明自己值得被愛（因為我很強）。
- p54：對話停了「一會兒」。
- p56：「換作一年前」。
- p58：「我很想說」；「就連這也不是真的」；「大概」就會直接問。
- p61：「也許」真的沒有；「我不會說……全都一樣好」；「幾乎永遠」；怨恨「可能」是最糟的；「我不認為」有一套適用所有人。
- p63：「也許」；「至少」一兩成；「只要我們能贏」；*她*唯一能快樂起來的方法；光靠情感支持和愛「沒辦法」；唯一*能*帶回來的是你贏——幫維瑞迪亞打贏北極人。
- p65：「幾分鐘後」；密封的門；門「慢慢」打開。
- p66：長形房間，盡頭一張大桌子，桌邊一個人披著暗色斗篷——鄧在 p67 才點名，p66 不要提前點名。
- p70：「連」你的口音都變好了。
- p74：「到目前為止」「還沒想出什麼絕妙的計畫」。
- p75：「在這段期間」（in the interim）；「不太尋常」。
- p78：鄧「一時」驚訝地盯著；表情「幾乎立刻」恢復平靜，「彷彿」（as though）想起公然流露情緒不符合自我形象——原文的 as though，保留揣測語氣。
- p79：「我想我看得出」。
- p80：「非常深」；「很多」政治人物；「似乎」還在抵抗的（seem）；「就連」掌舵會內部，也「相當深」。
- p81：「或許」（might）；「盡可能」；「甚至」試著反制；「說不定還能」（Maybe even）。
- p83：信任「大量」流失；「徹底」分裂。
- p85：「已經」很後面；局勢很危急。
- p86：「不只是」一個字的建議；「非常詳細」；「一大群」守律者。
- p87：「我認為」；萬一曝光，說是「我們提議、甚至是我們主導的」（along with me）。
- p90：「最好的密碼學家之一」。
- p91：「這十五年來」；監視「主要」是實體世界的事；「很久以前」帶我看的那一間；「才不會太惹人注意」（reasonably unobtrusive）。
- p92：「我想」；「已經」裝在很多地方、「還想」裝到其他所有地方；「以前」規定；「幾年前」放寬；「沒有人注意到」；「乾脆」。
- p93：「一定早就」大舉滲透了吧（surely … must）——鄧的反問。
