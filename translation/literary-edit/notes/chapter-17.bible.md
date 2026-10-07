# 第 17 章 bible 摘錄（第二輪文學編輯用）

主 Agent 依 WORKFLOW「開始一章前」第 5 步建立；每個 chunk 的資料包都附上這份（`literary_edit.py packet --bible`）。
權威來源仍是 glossary／characters／worldbuilding；這裡只是本章會用到的部分，加上本章初譯已定的用詞。
段號為原文段號（`literary_edit.py plan 17` 的 pNNN；與 `translation/notes/chapter-17.md` 的段號相同）。

章節結構：p1 標題、p2 日期行（梅爾丹，3724 年果月 11 日）｜p3–p42 議會大廈：格拉迪亞斯拜會韋爾多參議員（p6 邀請證明畫面）｜p43 場景分隔｜
p44–p82 貝爾戈講解圖譜募資（p55 空氣傳播疾病防治子圖 SVG、p74 紫外線子圖 SVG；說話者多半未標）｜p83 場景分隔｜
p84–p115 家中晚餐：第一次投票、北林交換、按鍵投票（p112 投票畫面）。
裝置畫面（p6、p55、p74、p112）是 HTML 區塊，不送編輯；本章尚未轉圖。

## 一、全章固定用詞（editor 一次只看一個 chunk，看不到別處的叫法；這些不要換）

| 原文 | 本章用法 | 出現位置／說明 |
|---|---|---|
| path covered with trees on both sides | 兩旁綠樹夾道的小徑 | p3 |
| large circular parliament building | 巨大的圓形議會大廈（後文簡稱「大廈」） | p3、p4 |
| tapped his watch on the green circle | 把手錶貼上綠色圓圈（p8「又把手錶貼了上去」呼應） | p4、p8 |
| The circle buzzed. | 圓圈嗡地響了一聲。 | p5 |
| instructions that were being relayed by his watch | 照著手錶傳來的指示 | p7 |
| The door opened. | 門開了。（p7、p9 刻意重複，兩處字面一致） | p7、p9 |
| Veridian parliament robe | 維瑞迪亞的議會長袍 | p10 |
| the senator／Senator Verdow | 參議員／韋爾多參議員 | p11、p12 |
| A robot slid into the room | 一個機器人滑進了房間（p22「悄悄滑開」） | p14、p22 |
| jie mo kai tu jie hei ja ma? | jie mo kai tu jie hei ja ma?（保留拼音，不解釋、不加譯文） | p15 |
| briefly stared in surprise | 一愣，盯著它看了一下（譯者筆記；不另加表情） | p16 |
| a few months ago | 幾個月前（呼應 ch32 用哲戈語點茶） | p18 |
| a reminder that other countries exist and that they matter | 小小的提醒：世界上還有其他國家，而且它們很重要 | p18 |
| the robot's screen | 機器人的螢幕 | p19 |
| Dzegoban | 哲戈語 | p20 |
| 'ja'／'kai ja'／'plant water' | 『ja』『kai ja』『植物水』（對話內用『』，p22 敘事中用「」：點了「kai ja」；譯者筆記） | p21、p22 |
| get acclimated | 適應 | p22 |
| beeped, signaling acceptance of the order | 嗶了一聲，表示收到點單 | p22 |
| secret meetings | 祕密會議 | p24 |
| the hearing | 聽證會（ch08 遴選聽證） | p24 |
| original application to the Order years ago | 幾年前最初向掌舵會提出的申請 | p24 |
| a good and smart person | 正直又聰明的人 | p24 |
| one of over a thousand | 守律者超過一千人，你只是其中一個 | p24 |
| first-hand experience | 第一手經驗 | p24 |
| intentionally omitted any mention of Zei | 刻意隻字不提澤 | p26 |
| indirect connection | 這層間接的關係（p29「間接的」呼應） | p26、p29 |
| a fully independent answer | 一個完全獨立的答案 | p26 |
| my strongest connections | 我交情最深的 | p27 |
| authors and musicians | 作家和音樂家 | p27 |
| security and health ministry | 安全與衛生部門（照 worldbuilding） | p27 |
| give them a heads up | 先跟他們打聲招呼 | p27 |
| I wouldn't stop with them | 換作是我，不會只找他們（譯者筆記：理解為建議） | p27 |
| a chance meeting in the Economics Institute in Freetown | 在自由城的經濟研究所偶然碰上 | p29 |
| they were in Minpentai | 他們有在打明盤台 | p29 |
| a better lead | 門路 | p30 |
| top-notch | 頂尖的 | p30 |
| the actual Dzego army | 真正的哲戈軍隊 | p30 |
| championships | 冠軍賽 | p31 |
| semi-finals／finals | 準決賽／決賽（與 ch15 一致） | p32、p33 |
| municipal level／National | 市級／全國的 | p33、p34 |
| a mix of surprise and joy | 又驚又喜 | p35 |
| Your connections | 你的人脈 | p36 |
| get more than one perspective／getting more perspectives | 多聽幾種觀點（p37、p39 刻意呼應，兩處字面一致） | p37、p39 |
| Graph Funding steward | 圖譜募資管理人 | p39 |
| privacy robe but without the face cover and hood | 維瑞迪亞隱私袍，卻沒戴臉罩，也沒戴兜帽 | p44 |
| he's a Keeper | 他是守律者 | p47 |
| How familiar…／Honestly, not very.／Great. | 有多熟／老實說，不太熟。／太好了。（p53 是貝爾戈的小玩笑，保留反差） | p51–p53 |
| hand device | 手持裝置 | p54 |
| subgraph | 子圖 | p56 |
| airborne disease resistance | 空氣傳播疾病防治（與 p55 SVG 標籤一致） | p56 |
| node／edges／weights | 節點／各條邊／權重 | p56 |
| the cryptographic network | 密碼學網路 | p56 |
| committee | 委員會 | p56 起全場 |
| secure in the same way the Courts and the Order of Steering are | 跟法院、掌舵會一樣安全（p60「法院、掌舵會」並列呼應） | p57、p60 |
| Quadratic Funding | 平方募資 | p57 |
| the same attack…that Bluewhale did but at ten times the scale | 跟藍鯨當初一模一樣的攻擊，只是規模大了十倍 | p57 |
| more traditional style of allocation | 比較傳統的分配方式 | p57 |
| secrecy and internal communication barriers | 層層保密和內部的溝通屏障 | p58 |
| the system is holding | 這套制度還撐得住 | p58 |
| both of these things | 這兩者（指法院與掌舵會） | p59 |
| citizens' assemblies／Heralds | 公民會議／傳令官 | p59 |
| public accountability | 公共問責（p72「問責」呼應） | p59、p72 |
| Good to hear.（p59）／Glad to hear.（p93） | 那就好。（兩處字面相同，不同人說） | p59、p93 |
| specialization／specialize | 專業分工／分工分得越細 | p60、p68 |
| UVC lamps | 紫外線 C 燈（glossary） | p61、p62 |
| 'what percent of all Veridian public funding…' | 『維瑞迪亞全部的公共資金裡，該拿百分之幾給這項紫外線 C 燈的研究』 | p61 |
| health／airborne diseases | 健康／空氣傳播疾病 | p61 |
| and so on | 依此類推 | p61 |
| a tree／a proper directed acyclic graph | 一棵樹／一張名副其實的有向無環圖 | p62 |
| multiple parents／paths／adds up | 好幾個父節點／所有路徑／加總起來 | p62 |
| direct children／children | 直接子節點／子節點 | p63、p65 |
| This is fascinating. | 真有意思。 | p67 |
| captured by special interests | 被特殊利益團體把持 | p68 |
| tradeoff | 取捨（p69「這永遠是個取捨」、p70「還有另一個取捨」呼應） | p69、p70 |
| bad／good／great projects | 爛計畫／好計畫／卓越的計畫 | p70 |
| lower levels of the graph | 圖的下層 | p70 |
| randomize at the top end | 在頂端隨機分配 | p70 |
| top ten percent | 前一成 | p70 |
| ninety one or ninety nine／above ninety | 九十一分還是九十九分／高出九十 | p70、p71 |
| optimizing for the committee | 迎合委員會 | p71 |
| intrinsic motivation | 內在動機 | p72 |
| randomize-above-cutoff | 門檻以上隨機分配 | p72 |
| freedom from incentives | 擺脫誘因 | p72 |
| with barely any effort at all | 幾乎不費吹灰之力（譯者筆記：全場只用這一個成語） | p72 |
| level／granularity | 這一層／層次（譯者筆記：避開「層級」） | p73、p75 |
| randomly-selected Graph Funding committees | 隨機選出的圖譜募資委員會 | p75 |
| evolve without changing the structure | 在不改變結構的情況下演進 | p76 |
| VNU Materials Science Lab | 國立大學材料科學實驗室（與 p74 SVG 一致） | p76 |
| 'ownership' | 『所有權』 | p76 |
| open source social media analysis | 社群媒體開源分析（與 p55 SVG 一致） | p76 |
| eighty percent | 八成 | p76 |
| so closed and proprietary with everything | 什麼都要封閉、什麼都要專有 | p77 |
| air filters／ultraviolet lights | 空氣清淨機／紫外線燈（glossary） | p79 |
| getting paranoid | 疑神疑鬼 | p79 |
| deliberately-released pandemic | 故意散播一場大流行病 | p79 |
| bounce right back to them | 反彈回北極自己身上 | p80 |
| anti-pandemic technology | 防疫技術 | p81 |
| open-source | 開源 | p81 |
| the defensive things | 防禦性的那些 | p81 |
| level playing field | 公平的立足點 | p81 |
| light a fire…fireproof suits | 放了火，卻只有自己穿著防火衣 | p81 |
| public health | 公共衛生 | p82 |
| your first vote | 第一次投票 | p86 |
| the in-person part | 要親自到場的部分 | p89 |
| key registration | 金鑰登記（p114 呼應） | p89、p114 |
| Keeper discussion group online | 守律者的線上討論小組 | p90 |
| chat automatically cut off／the cutoff | 聊天室……自動關閉／關閉（p90、p91 呼應） | p90、p91 |
| seven days before the vote | 投票前七天 | p90 |
| quiet period | 靜默期 | p90 |
| independent thought | 獨立思考 | p90 |
| Oof | 唉 | p91 |
| got annexed | 被併吞 | p91 |
| military hardware | 軍事硬體 | p92 |
| the best tiers in the rubric | 規準最優惠幾級（譯者筆記；對照 p112 第 1、2 級的動議） | p92 |
| amendment | 修正案 | p92 |
| tax brackets | 稅級（p112 畫面「將稅級由」呼應） | p92、p112 |
| I'll probably vote for that. | 我大概會投贊成。（p115 按下「贊成」呼應） | p92 |
| Parliament meetings | 在議會的會面 | p94 |
| the Senator and the Graph Funding person | 參議員和那位圖譜募資的人 | p95 |
| contact | 聯絡人 | p95 |
| the official Dzego government | 哲戈官方政府 | p96 |
| interesting action | 有意思的事 | p96 |
| put you two in touch | 讓你們兩個聯絡上 | p97 |
| exchange trip／winter term | 交換學習／冬季學期 | p100 |
| Northglade | 北林 | p100、p102、p106 |
| almost at the Arctic border | 都快到北極的邊界了 | p101 |
| ski off mountains wearing a copter and then glide back down | 揹著小型旋翼機從山上滑雪衝出去，再滑翔下來（glossary copter） | p102 |
| over two hundred kilometers inland | 內陸兩百多公里 | p102 |
| Veridia's best math university | 維瑞迪亞最好的數學大學 | p104 |
| top five percent | 前百分之五 | p104 |
| special education | 特別課程（glossary：資優課程，不是特殊教育） | p104 |
| computer science | 資訊科學 | p105 |
| washroom | 洗手間 | p107 |
| seventy-five percent | 七十五分（ch08、ch16 慣例） | p108 |
| hand device buzzed | 手持裝置震動了一下 | p110 |
| hardware openness rubric | 硬體開放性規準 | p111 |
| Motion／Vote／Yes／No／Tier 1 | 動議／投票／贊成／反對／第 1 級（畫面，不送編輯） | p112 |
| anti-climactic | 虎頭蛇尾 | p113 |
| ceremony, in-person meetings, debate and work | 儀式、當面的會議、辯論和工作 | p113 |
| just … tapping buttons on a screen | 就只是……在螢幕上按幾個按鈕（刪節號保留） | p113 |
| on his own hardware at home | 在自己家裡、用自己的硬體 | p114 |
| fifteen-longhour voting window | 十五長時的投票時段 | p114 |
| the one registered | 登記過的那一把 | p114 |
| a distraction | 幌子 | p114 |
| nonchalantly pressed: `No`, `Yes`, `Yes` | 若無其事地按下：`反對`、`贊成`、`贊成`（反引號保留，與畫面按鈕一致） | p115 |

## 二、本章出現的 bible 譯名（`uv run tools/literary_edit.py terms 17` 產生）

- 人名：Gladias → 格拉迪亞斯（避免：格拉迪斯、葛拉迪亞斯）；Seila → 賽菈（避免：塞拉、席拉）；Zven → 茲文；Lily → 莉莉（避免：百合）；Febric → 費布里克；
  Hreda → 赫蕾妲；Vil → 維爾；Mov → 莫夫；Delwart → 德爾瓦特；Zei → 澤（避免：賊）；Bai → 白；Verdow → 韋爾多；Eighteen → 十八號；Belgor → 貝爾戈；
  SVG 研究者：Dalias → 達利亞斯；Poppe → 波普；Mawart → 馬瓦特；Vidrik → 維德里克；Bonne → 波恩；Kudlin → 庫德林；Melana → 梅拉娜；Pov → 波夫；Imerry → 伊梅莉
  （Glad → 格拉德：本章未出現暱稱；p87「glad you remembered」是一般語意，譯者筆記）
- 地名：Veridia → 維瑞迪亞（避免：韋里迪亞）；Meldan → 梅爾丹；Freetown → 自由城（避免：弗里敦）；Redshire → 紅郡（避免：雷德郡）；Northglade → 北林；
  Dzego → 哲戈（避免：澤戈）；Dzegoban → 哲戈語
- 組織／制度：Order of Steering → 掌舵會（避免：導向修會）；Steering → 掌舵；Keeper → 守律者（避免：守護者）；Bluewhale → 藍鯨；Silverchat → 銀聊；
  VNU → 維瑞迪亞國立大學／國立大學；Parliament → 議會（避免：國會）；Veridian Parliament → 維瑞迪亞議會；Courts → 法院；Senator → 參議員；committee → 委員會；
  special interests → 特殊利益團體；quiet period → 靜默期；key registration → 金鑰登記；voting window → 投票時段；Motion → 動議；rubric → 規準（避免：評分標準）；
  Tier → 級（「層級」是 Tier 的避免譯法，p73、p75 用「這一層」「層次」）；exchange trip → 交換學習；Minpentai → 明盤台；citizens' assembly → 公民會議（避免：公民大會）；
  Herald → 傳令官（避免：使者、傳令員）
- 圖譜募資：Quadratic Funding → 平方募資（避免：二次方募資、二次融資）；Graph Funding → 圖譜募資（避免：圖表募資、圖形融資）；node → 節點／據點（本章用「節點」）；
  subgraph → 子圖；directed acyclic graph → 有向無環圖；randomize-above-cutoff → 門檻以上隨機分配；portfolio → 組合（避免：投資組合）；intrinsic motivation → 內在動機；
  accountability → 問責；cryptographic network → 密碼學網路（避免：加密網絡）；open source → 開源（避免：開放原始碼）
- 物品：hand device → 手持裝置（避免：手機）；watch → 手錶；privacy robe → 隱私袍（避免：隱私長袍）；face cover → 臉罩（避免：面罩）；parliament robe → 議會長袍；
  copter → 旋翼機（避免：直升機）；green circle → 綠色圓圈；UVC lamp → 紫外線 C 燈（避免：UVC 燈）；ultraviolet lights → 紫外線燈；air filter → 空氣清淨機
- 其他：longhour → 長時（避免：長小時）；Fruitmoon → 果月；jie mo kai tu jie hei ja ma、kai ja、ja → 保留拼音

## 三、人物口吻與稱謂

- 格拉迪亞斯：拜會時謙虛、好問（p52「老實說，不太熟。」）；對韋爾多用「您」但能省則省（初譯 p12「也謝謝您撥空見我」、p23「所以您覺得」、p25「如果您覺得」「想請教您」；其他句不要新增「您」）；
  對貝爾戈用「你」（p48、p58）。在家對賽菈、孩子用「你」，語氣輕鬆。p113–p114 內心直述（「格拉迪亞斯心想」「格拉迪亞斯想」），帶一點失落的自嘲。
  ⚠ 稱謂表：對韋爾多的「您」只限本章（ch25 起改「你」），本章照用。
- 韋爾多：熱情、爽朗、愛自嘲，對格拉迪亞斯用「你」、直言稱讚（p24「你顯然很聰明」）；p24 一段長話，語氣是資深政治人物的輕鬆（「可是拜託」）。對貝爾戈直呼名字、用「你」。
- 貝爾戈：講解型技術官僚，清楚不賣弄、愛舉例；p53「太好了。」是小玩笑；p77「嘿」帶點揶揄。對格拉迪亞斯、韋爾多都用「你」。
- 賽菈：家常、溫暖、務實；p97 主動說要聯絡澤。
- 赫蕾妲：開朗、得意（p100「得意地大聲宣布」、p102「興奮地說」）；費布里克：簡短補一句（p105）。
- 茲文：p88 一句孩子的直白問題。
- 說話者（**原文未標說話者的輪次一律照初譯，不補標籤**）：
  p11 韋爾多（原文標 the senator）、p12 格拉迪亞斯、p13 韋爾多、p15 機器人、p18 韋爾多、p21 韋爾多、p23 格拉迪亞斯、p24 韋爾多、p25 格拉迪亞斯、p27 韋爾多、p28–p29 格拉迪亞斯、
  p30 韋爾多、p31 韋爾多、p32 格拉迪亞斯、p33 韋爾多、p34 格拉迪亞斯、p36–p37 韋爾多、p39 韋爾多、p40 格拉迪亞斯、p41 韋爾多、p42 格拉迪亞斯；
  p45 韋爾多、p46 貝爾戈、p47 韋爾多、p48 格拉迪亞斯、p49 貝爾戈、p50 韋爾多（以第三人稱談格拉迪亞斯）、p51 貝爾戈、p52 格拉迪亞斯、p53 貝爾戈、p56–p57 貝爾戈
  （p57 也可能是韋爾多接話，譯者筆記與 QA 判斷為貝爾戈）、p58 格拉迪亞斯（提到守律者遭攻擊）、p59–p62 貝爾戈、p63 格拉迪亞斯、p64 貝爾戈、p65 格拉迪亞斯、p66 貝爾戈、
  p67–p68 格拉迪亞斯、p69–p70 貝爾戈、p71 格拉迪亞斯、p72–p73 貝爾戈、p75 格拉迪亞斯、p76–p77 貝爾戈、p78 格拉迪亞斯、p79 貝爾戈、p80 格拉迪亞斯、p81–p82 貝爾戈
  （p82「回來時一定要告訴我……我很好奇」也可能是韋爾多；不點名）；
  p86 賽菈、p87 格拉迪亞斯、p88 茲文、p89–p90 格拉迪亞斯、p91 不點名（賽菈或費布里克，譯者筆記）、p92 格拉迪亞斯、p93–p94 賽菈、p95 格拉迪亞斯、p96–p97 賽菈（譯者筆記）、
  p99 賽菈（未標）、p100 赫蕾妲、p101 格拉迪亞斯、p102 赫蕾妲、p103 格拉迪亞斯、p104 赫蕾妲、p105 費布里克、p106 格拉迪亞斯或賽菈（未標）、p108–p109 未標（家中大人或孩子），
  p111 格拉迪亞斯。

## 四、伏筆與資訊邊界（不可加暗示）

- p3–p9：走向議會大廈、側門、綠色圓圈、手錶指示的路線（往前，右轉，再往前，左手邊第三扇門）——動作照原文，不補議會的景色或心情。
- p6（畫面）：邀請證明已驗證——不送編輯。
- p10：只說穿議會長袍的男人，下一段才知道是參議員；不要提前點名。
- p16：「briefly」一愣——不另加表情（譯者筆記）。
- p18：「幾個月前」改設定；提醒「其他國家存在而且重要」——不延伸到北極或紅郡。
- p20：螢幕全是哲戈語；視線「茫然地」游移（with confusion）。
- p21：『植物水』是 kai ja 的字面意思；不要替 p15 機器人的整句補譯文。
- p22：「既然要在哲戈待上幾個月」——原文 If he's going to be；他其實還在徵詢（p23），語氣不要變成已決定。
- p24：韋爾多「完全不知道」祕密會議內容；依據是聽證會的發言和幾年前的申請；守律者「超過一千人」；去哲戈「說不定更有意義」（could be even more meaningful）。
- p26：刻意不提澤——「並不是想隱瞞」這層間接關係，而是想先聽完全獨立的答案。理由只有這一個，不加。
- p27：輕笑（gently laughing）；交情最深的是作家和音樂家；政府裡「也認識幾個人」；「換作是我，不會只找他們」。
- p29：只認識兩個人，「間接的」；賽菈在自由城的經濟研究所「偶然」碰上。
- p30：睜大了眼睛；「可能」比我的還好；「幾乎會」信任他們勝過真正的哲戈軍隊（almost）。
- p32：「賽菈上次跟我說的是」——資訊是轉述；澤贏了準決賽、紅郡被入侵決賽就取消（ch15）。
- p33–p35：市級？全國的。韋爾多又驚又喜——不加台詞或評論。
- p36：「肯定」比我的好（definitely）。
- p39：圖譜募資管理人「正好在這裡，等一下要來找我」。
- p44：「幾分鐘後」；穿維瑞迪亞隱私袍但沒戴臉罩、沒戴兜帽——不解釋原因。
- p50：「最近在考慮」去哲戈；「也許」你可以（maybe）。
- p55、p74（SVG）：百分比與「...」不動，不送編輯；敘事中不要複述圖上的數字。
- p56：每個節點由密碼學網路「隨機」選出委員會，決定「正下方」各條邊的權重。
- p57：北極人「剛剛」對平方募資發動跟藍鯨相同的攻擊，規模「十倍」；任何比較傳統的分配方式「也一樣會想辦法插手」。
- p58：「最近」連守律者都受到攻擊；「至少目前」制度還撐得住（at least for now）——不要說得更樂觀或更悲觀。
- p59：遺憾「還沒有好辦法」讓這兩者更民主；公民會議、傳令官「很好」但取代不了真正的公共問責。
- p61–p62：拆成小塊、從健康往下問；p62「某種燈不知怎麼地既對紫外線 C 燈有用、又對國防有用」照原文（見疑點），不要自行改成更合理的例子。
- p66：「當然可以」；圖「一開始就是這樣建起來的」。
- p68：問句語氣（right?…?）——是格拉迪亞斯的推論，不要變成斷言。
- p70：委員會分得出好壞「並不難」（fairly easy），分得出好與卓越「非常難」；「最近有一股風潮」（a movement lately）；只在「圖的下層」；前一成內「入選機率都一樣」。
- p71：「基本上」不用費心迎合委員會（basically）。
- p72：「有時候」不想要問責；頂端的人「說不定」比委員會聰明（may even）；兩半句對仗（沒有問責就成不了事的人／最優秀的人）保留。
- p75：「這樣明智嗎？」——疑問，不要變成批評。
- p76：「我自己也不確定」；委員會「大可以」把一整個類別交給實驗室；社群媒體開源分析「基本上」就是這樣，八成給銀聊。
- p77：藍鯨「不太高興」；「是他們自己選擇」封閉、專有。
- p79：「有不少」技術流到哲戈；「開始比較認真看待」；「有幾個人」越來越疑神疑鬼，擔心北極人「哪天」會故意散播——這是哲戈部分人的擔憂，不要寫成事實或預告。
- p80：問句：有沒有可能打擊對方而不反彈回自己。
- p81：條件句：「要是」北極防疫技術遠遠領先「那就有可能」；開源「至少是防禦性的那些」；放火／防火衣的比喻保留。
- p84–p85：回家時賽菈和孩子們「已經」在吃晚餐。
- p86：今天是「第一次」投票。
- p89：要親自到場的是「幾個月前」的討論與金鑰登記；金鑰登記是在議會開完會之後「馬上」辦的（right after）——即今天稍早。
- p90：「最近」小組也還有討論；投票前「七天」自動關閉；靜默期的理由是「說是」（the argument goes）——引述別人的說法，不要變成格拉迪亞斯的立場。
- p91：「所以關閉是在紅郡被併吞之後」——推論語氣；不點名說話者。
- p92：「我想」（I think）主張把軍事硬體排除的人「全都安靜下來了」；十八號「後來」提新修正案、調高稅級；「大概」會投贊成（probably）。
- p95：參議員和圖譜募資的人「好像」都很支持（seemed）；「他們說」澤「可能」比他們認識的任何人都更適合——原文如此（實際只有韋爾多說），不要替他更正。
- p96：「大家都知道」有意思的事不在哲戈官方政府——賽菈的看法，不補細節。
- p100–p102：北林交換是 ch20 北林淪陷、兩人受困大梅港的伏筆；p101「都快到北極的邊界了」、p102「又不是就在邊界上」「內陸兩百多公里」「第一次去」照原文，**不加任何不祥暗示**。
- p104：數學班上「前百分之五」；獲選上「一些」特別課程。
- p107：莉莉在洗手間，沒辦法回答——不加莉莉的反應或其他暗示（ch21–ch23 莉莉線，照原文）。
- p108：「如果」考到七十五分，夏天就帶她去。
- p109：比較喜歡夏天，沒那麼喜歡冷。
- p112（畫面）：三項動議——第 1、2 級新增軍事等用途排除條款；稅級 0/6/12/18/24 → 0/10/20/26/32；第 4、5 級第 4 行加「或軟體」——不送編輯。
- p113：「感覺有點」虎頭蛇尾；投票前「那幾個月」；「就只是……」刪節號保留。
- p114：「這也合理」（supposed）；「只要」金鑰登記是安全的；「就算」德爾瓦特真的找上門、在「整整十五長時」的投票時段站在背後盯著，也無法證明裝置上的金鑰是登記過的那一把；「說不定」那只是幌子，真正的票是莫夫、賽菈「甚至」茲文投的——延續 ch15 投票機制，技術條件不可省略或弱化，不補畫面。
- p115：「最後」看一眼；「若無其事地」按下：反對、贊成、贊成——不補他的感想。
