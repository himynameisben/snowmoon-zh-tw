# 第 27 章 bible 摘錄（第二輪文學編輯用）

主 Agent 依 WORKFLOW「開始一章前」第 5 步建立；每個 chunk 的資料包都附上這份（`literary_edit.py packet --bible`）。
權威來源仍是 glossary／characters／worldbuilding；這裡只是本章會用到的部分，加上本章初譯已定的用詞。
段號為原文段號（`literary_edit.py plan 27` 的 pNNN；與 `translation/notes/chapter-27.md` 的段號相同）。

章節結構：p2 dateline（維瑞迪亞，梅爾丹 · 霜季 7 日）｜p3–p27 旅館房間：格拉迪亞斯道歉、賽菈的新主意（銀聊民調、共同知識、說服艾維洛由公司出錢）｜
p28 分隔｜p29–p97 走過卡利馬區、進人造小山見艾維洛：民調、一百萬吉普幣、預測市場的兩個弱點、可驗證兩方計算、混淆電路、送茶機器人、艾費里昂的複利論與三人的反駁｜
p98 scene-break dateline（霜季 8 日）｜p99–p132 政府旅館會議室：倒數發布問卷、圓餅圖（p118、p120、p125 是 SVG 圓餅圖）｜p133 分隔｜p134–p142 AI 回答（p136 是 AI 重點摘要畫面）。

chunk（`plan 27`）：01＝p3–p27｜02＝p29–p97（單一長段群）｜03＝p99–p117、p119、p121–p124、p126–p132｜04＝p134–p135、p137–p142。

### HTML 區塊（不送 editor，一字不動）

- p118 圓餅圖：你對維瑞迪亞軍方有多少信心？完全沒有 39%、一點點 25%、一些 15%、很多 12%、完全信任 9%。
- p120 圓餅圖：你比較希望由誰來領導維瑞迪亞軍方？現任領導層 13%、（由議會選出的）新領導層 21%、銀聊 10%、北極帝國 16%、昆高派 38%、亞圖利亞軍事顧問 2%。
- p125 同上，僅限與北岸省有淵源者：6%、8%、16%、13%、昆高派 52%、5%。
- p136 AI 重點摘要：一般情境 20%；改由昆高派掌控 26%；主要下行風險是組織轉換成本；昆高派參與但降低轉換衝擊時最高可達 50%；以上指一年後「維持不變或更大」，嚴格更大的機率一律低得多。
- 散文不要替這些畫面補數字或解釋。

## 一、全章固定用詞（editor 一次只看一個 chunk，看不到別處的叫法；這些不要換）

| 原文 | 本章用法 | 說明 |
|---|---|---|
| government hotel (room)／government-run hotel | 政府旅館（房間）／政府經營的旅館 | p3、p99 |
| I've failed our whole family | 我辜負了我們全家 | p6 |
| no path to rescuing any of them | 沒有任何辦法把他們救出來 | p6 |
| Arctics | 北極（本章初譯多用「北極」指北極人／北極帝國，例如「北極把我們整個征服」「北極就不會知道」） | 全章；不要改成別的稱呼 |
| make it democratic | 讓它變得民主 | p12 |
| Silverchat | 銀聊 | |
| making our way up the ladder | 一層一層往上找人談 | p15 |
| a longhour in advance | 提前一長時 | p15（longhour→長時，自創時間單位） |
| polling feature／poll | 民調功能／民調 | p16 起 |
| burn zipcoins | 燒掉吉普幣（燒的吉普幣越多……） | p16 |
| large cross-section of people | 一大群涵蓋各類族群的人 | p16 |
| decoy questions／decoys | 誘餌題／誘餌 | p17、p51 |
| priority level | 優先級 | p18、p22 |
| social signal with strong legitimacy | 具有強大正當性的社會訊號 | p18 |
| common knowledge | 共同知識 | p18、p53（遞迴定義逐層保留，兩處斜體保留） |
| breadth | 觸及範圍 | p22 |
| Evelor | 艾維洛 | 銀聊創辦人 |
| publishing proofs onto a cryptographic network | 把證明公布到密碼學網路上 | p24 |
| set of readable messages | 可讀訊息的集合 | p24 |
| viewers' clients | 讀者的用戶端 | p24 |
| algorithm hash | 演算法雜湊值 | p24 |
| twenty-day delay | 延遲二十天 | p24 |
| sales taxes | 營業稅 | p25 |
| rubric changes | 規準調整 | p26（rubric→規準，全書） |
| algorithmic transparency／interoperability | 演算法透明／互通性 | p26 |
| Kalimar | 卡利馬區 | p29、p34 |
| car-free zone | 無車區 | p29 |
| privacy robes | 隱私袍 | |
| neck band | 頸帶 | p31 |
| stone houses | 石屋 | |
| land taxes | 土地稅 | p33 |
| mountain pyramids | 山體金字塔 | p34 |
| hand device | 手持裝置 | |
| green circle | 綠色圓圈 | p35 |
| hood／face covering | 兜帽／臉罩 | p37、p48 |
| robot | 機器人（送茶的） | p46、p72、p132 |
| bot／bots | AI（**不是**機器人） | p62、p67、p100、p102、p135、p139 |
| Emerald | 翡翠 | p51、p104、p105 |
| master plan | 整個計畫 | p52 |
| Kungaupei | 昆高派 | |
| Arturian military advisors | 亞圖利亞軍事顧問 | p55 |
| A: its current leadership… | A：現任領導層。B：由議會選出的新領導層。C：銀聊的領導層。D：北極帝國。E：昆高派（……）。F：亞圖利亞軍事顧問。 | p55（與圓餅圖用同一套名稱） |
| three million／one million zipcoins | 三百萬／一百萬吉普幣 | p57、p58 |
| unprecedented | 前所未見 | p58 |
| *work* | *行得通* | p60（斜體） |
| Silverchat Predict | 銀聊預測 | p62 |
| prediction markets | 預測市場 | p63、p66 |
| manipulate | 操縱 | p63、p64（預測市場語境） |
| arbitrageurs | 套利者 | p63、p64 |
| risk-neutral | 風險中立 | p64 |
| underlying variable | 標的變數 | p64 |
| private information | 私密資訊 | p65、p67 |
| leaderboard | 排行榜 | p67 |
| verifiable two-party computation | 可驗證的兩方計算 | p67 |
| ephemeral virtual private sandbox | 臨時的虛擬私有沙盒 | p67 |
| garbled circuits／verifiable garbled circuits | 混淆電路／可驗證的混淆電路 | p68、p104、p115 |
| Overhead | 額外開銷 | p68 |
| large language model | 大型語言模型 | p69、p123 |
| linear／nonlinear | 線性／非線性 | p69 |
| a tenth of a percent | 千分之一 | p69 |
| nine months of studying cryptography | 學了九個月的密碼學 | p70 |
| Ephelion's debate with Sylka | 艾費里昂和希爾卡的那場辯論 | p75 |
| 'softer' traits | 『比較軟』的特質 | p77 |
| move in circles | 繞圈子 | p77 |
| Disaster to heroism to prosperity to complacency to disaster | 從災難到英雄氣概，到繁榮，到安逸，再到災難 | p77（ch08 用語） |
| Technocracy to democracy to chaos to strongman | 從技術官僚到民主，到混亂，到強人，再回到技術官僚 | p77 |
| compounding | 複利 | p77、p78 |
| *wrong* | *錯* | p77（斜體） |
| eigenvector／largest eigenvector | 特徵向量／最大特徵向量 | p79–p81、p86 |
| whitepaper | 白皮書 | p81 |
| longevity clinics | 長壽診所 | p83 |
| eternal life elixirs | 長生不老的靈藥 | p85 |
| longevity science | 長壽科學 | p85 |
| maximizing economic output | 最大化經濟產出 | p89 |
| fragile world | 脆弱的世界 | p92、p95 |
| reversible／irreversibly | 可逆／不可逆 | p92、p95 |
| *anyone* | *任何人* | p92（斜體） |
| lock their power in. Irreversibly. Forever. | 把權力鎖死。不可逆。永遠。 | p92 |
| entropy - the dimensionality of the space of humanity's future possibilities | 熵——也就是人類未來可能性所構成的空間的維度 | p93（呼應 ch25 熵） |
| permanently constricted | 永久收縮 | p93 |
| superweapons | 超級武器 | p94 |
| multiplied by zero forever | 永遠乘以零 | p95 |
| fighting against／fighting for | 值得與之對抗／值得為之奮戰 | p96，成對 |
| timer／questionnaire | 計時器／問卷 | p99 |
| 150 ticks／fifty ticks | 150 拍／五十拍 | p99、p106（tick→拍，不可寫「秒」「刻」） |
| package for the bots | 給 AI 的資料包 | p100 |
| machine-checkable mathematical proof | 可由機器檢查的數學證明 | p104 |
| correctness and privacy properties | 正確性與隱私性質 | p104 |
| end-to-end | 端到端 | p104 |
| Zero information leakage unless hashes are broken | 除非雜湊被破解，否則零資訊外洩 | p104 |
| a fresh instance | 一個全新的實例 | p105 |
| Minpentai announcer voice | 明盤台播報員的聲音 | p107 |
| MU GU GEI HUI ZIU FA／LE MU GEI HUI ZIU FA／PA GU … HUI ZIU FA! | 照抄全大寫拼音 | p108、p110、p114；p114 的「……」照初譯 |
| Beat you! | 搶先你了！ | p112 |
| progress bars／pie charts | 進度條／圓餅圖 | p115、p130、p131 |
| Restrict to people who are from Northshore | 只看北岸省出身的人 | p121 |
| self-declared most recent senator votes | 自報最近投給的參議員 | p123 |
| personality type axes | 人格類型軸 | p123 |
| given the game away | 把底牌都亮給北極看了 | p127 |
| Hydrafill | 海卓菲 | p128 |
| lawsuit／file the case | 訴訟／提告 | p129、p142 |
| too coordinated | 太像事先串通好的 | p129 |
| conservative temperament | 性子……保守 | p139 |
| status quo and Kungaupei scenarios | 維持現狀和交給昆高派 | p140 |

## 二、固定譯名

- 人物：Gladias → 格拉迪亞斯；Seila → 賽菈；Zei → 澤；Bai → 白；Verdow → 韋爾多；Den → 鄧；Mu → 穆；Mov → 莫夫；Evelor → 艾維洛；
  Lily → 莉莉；Febric → 費布里克；Hreda → 赫蕾妲；Tafindel → 塔芬德爾；Ephelion → 艾費里昂；Sylka → 希爾卡
- 地名：Meldan → 梅爾丹；Kalimar → 卡利馬；Dzego → 哲戈；Veridia → 維瑞迪亞；Northshore → 北岸省；Redshire → 紅郡；Arturia → 亞圖利亞
- 組織／物：Silverchat → 銀聊；Kungaupei → 昆高派；zipcoin → 吉普幣；Emerald → 翡翠；Hydrafill → 海卓菲；privacy robe → 隱私袍；neck band → 頸帶
- 單位：tick → 拍；longhour → 長時
- 日期：Frostime → 霜季

## 三、人物口吻與稱謂

- 全章沒有「您」，不要加。艾維洛直率、工程師式（p49「他直截了當、毫不修飾地脫口而出」），用「你」。
- 格拉迪亞斯：開頭自責（「我辜負了我們全家」）；和艾維洛談預測市場、特徵向量時是行家口吻。
- 賽菈：務實、有主見，計畫講得條理分明；p96 的回答樸素有力。
- 澤：密碼學口吻；被艾維洛比下去時的自嘲（p70，敘事）。p108 故意誇張的機器人腔。
- 白：搶先倒數鬥嘴（p110、p112）。
- 說話者（**原文未標說話者的輪次一律照初譯，不補標籤**）：
  - chunk 01：p5–p6 格拉迪亞斯；p9 賽菈；p11 格拉迪亞斯；p12 賽菈；p13 格拉迪亞斯；p14–p17 賽菈；p18 未標（不點名）；p19 未標；p20–p27 未標，照初譯不點名。
  - chunk 02：p38 艾維洛；p39 格拉迪亞斯；p40 澤；p42 艾維洛；p43 格拉迪亞斯；p44 澤；p45 賽菈；p46 艾維洛；p49 艾維洛；p50–p51 賽菈；p53 賽菈；p56 艾維洛；p57 賽菈；
    p58 艾維洛；p59 賽菈；p60 艾維洛；p61（未標）；p62 艾維洛；p63–p65 格拉迪亞斯；p66 艾維洛；p67（未標，不點名）；p68 澤；p69（未標）；p73 艾維洛；p74 格拉迪亞斯；
    p75 艾維洛；p76 格拉迪亞斯；p77 艾維洛；p78–p79 格拉迪亞斯；p80 艾維洛；p81 格拉迪亞斯；p83 艾維洛；p84 格拉迪亞斯；p85 艾維洛；p86 格拉迪亞斯；p87 艾維洛；
    p89 格拉迪亞斯；p91–p95 澤；p96 賽菈；p97 艾維洛。
  - chunk 03：p100 賽菈；p101 鄧；p102–p103（未標）；p104 澤；p105 穆；p106（未標）；p107 白；p108 澤；p110 白；p111 澤；p112（未標）；p116 韋爾多；p119、p121–p124（未標）；
    p126 韋爾多；p127 賽菈；p128 穆；p129（未標）；p131（未標）。
  - chunk 04：p134 澤；p137 韋爾多；p138 格拉迪亞斯；p139（未標）；p140–p142（未標）。
  - 不同說話者不要合段；同一人連續的段落照原文分段。

## 四、伏筆與資訊邊界（不可加暗示）

- p3：「還來不及應聲」就聽到嗡嗡聲，門開了。
- p5：「幾乎立刻」開口，一臉難過；「我看」（I don't think）。
- p6：「除非北極把我們整個征服」。
- p8：「有好一會兒」兩人都沒說話；她退開一步、臉上綻出笑容。
- p10：眼睛一亮。
- p12：法官不願意做「他們覺得」非常不民主的事。
- p14：「某種意義上」正是這樣。
- p15：一開始「沒什麼辦法」引起注意；「大約十天前」韋爾多加入「幫了很大的忙」，「但即使這樣」還是沒當一回事；「冒了個險」；「結果當然發生了」。
- p16：「好吧，其實是」付給公司（自我更正）。
- p18：「我想」這得付很多；兩處斜體（全國人口中很大一部分／非常多）。
- p21：所有積蓄加起來，連莫夫的也算，「也只有一半」。
- p24：「根本不可能」違反規則；「唯一*能*做的」（斜體）。
- p26：稅「已經降到零」；列舉：演算法透明（＝那套證明機制）、互通性、尊重使用者隱私、配合研究人員。
- p29：大半路程搭黑色專車「為了安全起見」；車子「只能」開到無車區邊界；「希望」隱私袍夠用，格拉迪亞斯心想。
- p30：寒意讓他們精神一振，風正好推著往前，加快腳步。
- p31：她「幾乎已經和格拉迪亞斯一樣」習慣。
- p32：約一百公尺；「大約五十公尺後」；「看似」茂密的森林；「像是」小山。
- p33：「似乎」是小山內部；「幾乎」不用繳土地稅；「近乎完美」；從「短短一百公尺外」看起來未被碰過。
- p34：「很可能完全是」人造的；「說不定」防護效果更好（probably even better）。
- p36：路線順序：左轉→右轉上坡→右轉→上樓梯→另一扇門→上樓梯→圓形空間中央；兩人「這才發現」在山頂。
- p41：「大約十拍後」。
- p45：「稍微」環顧。
- p51：「大約一千道」題目；「只有一小部分」。
- p52：「微微」皺眉；「他覺得」太快；昆高派「絕不會」；「也許」……「又或許」……「甚至向全維瑞迪亞」。
- p53：如果順利，論據「會有力得多」：人民真正想要、「不會因此暴動」。
- p54：「大略」捲了捲。
- p58：「我會說」三百萬太多；「比以往任何一次」都多；「還是排得進前三」；「不算前所未見」。
- p60：「當然，也可能」我們會發現判斷大錯特錯。
- p62：「到目前為止」表現最好的是 AI（話被打斷，破折號保留）。
- p63：「理論上」；「平均而言」獲利；實務上「幾乎還沒經過驗證」（very untested）。
- p64：「除非」完全風險中立「或」錢多到無限，「總能」讓價格「至少偏移一些」；一百年來世界上「第二場」對北極的勝利。
- p66：「希望」能隨時間改善；「現在還很新」；第二點「比較難」解決。
- p68：「大概會想用」；額外開銷「相當嚇人——」（被打斷）。
- p69：「幾乎所有東西」都是線性的；只佔「千分之一」。
- p70：「在這個特定的專門題目上」被比下去；「看來」九個月還沒能「在每件事上都比每個人聰明」。
- p72：機械聲「越來越響」；「幾拍之後」看見機器人的「頭頂」；每一階先抬升、再滑動；四杯茶；「先」遞給格拉迪亞斯。
- p77：「似乎」都在繞圈子；「我還是說不上來」錯在哪。
- p79：「其實大多數特徵向量本來就是這樣」。
- p83：「確實」在乎健康；「但那仍然是健康」。
- p85：活得更久「本來就等於」（by default）活得更健康；最容易的時機是「剛開始的那一刻」。
- p86：「我猜」；「幾乎不懂」音樂和詩；「本來就是」會進入最大特徵向量的部分。
- p88：看得出賽菈皺著眉、不自在；他腦子飛快地轉。
- p89：戰爭「可以」摧毀經濟「好幾十年」；「恰恰相反」。
- p92：「以前沒有這麼脆弱」；「任何帝國統一得夠久，最後都會垮掉」；「只要*任何人*成功」。
- p93：「某一種」熵；「唯一可能」的未來世界。
- p94：「這還不是最糟的」；「可能會」徹底毀掉。
- p95：「總有一天」；「在接下來十年內」；北極「就會是原因」。
- p96：「可能會」殺死幾十萬、甚至幾百萬人；「光是這樣，就已經」。
- p97：啜了一口茶，往椅背一靠（原文 chair，前文是長椅，照初譯），陷入沉思。
- p99：「此刻剩下 150 拍」。
- p104：讀過它證明的命題；請翡翠和「另外兩個」AI 檢查；「相當紮實」。
- p105：「以防萬一」證明系統或定義「其實已經壞了十幾年卻沒人發現」；「完美無瑕」。
- p113：「一到十」就齊聲喊。
- p115：選票「很快」開始湧進來。
- p122：投票是匿名的。p123「確實有」分組。
- p126：「挖苦地」（wryly）；「看來」更適合。
- p127：「有點」怕；「是不是」（反問）。
- p128：「我想」沒關係；「居然」有兩成。
- p129：「當然」北極一定會注意；「延後幾天」；「不管怎麼做」。
- p130：「停了一下」。p131「還要等一陣子」。
- p134：「得意地」。
- p139：「肯定」比我保守，「但說得還算公道」。
- p140：「大致差不多」（vaguely similar）。p141「大致相同」。p142「我想」；「幾天後」提告。
