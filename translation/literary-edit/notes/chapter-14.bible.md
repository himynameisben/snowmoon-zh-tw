# 第 14 章 bible 摘錄（第二輪文學編輯用）

主 Agent 依 WORKFLOW「開始一章前」第 5 步建立；每個 chunk 的資料包都附上這份（`literary_edit.py packet --bible`）。
權威來源仍是 glossary／characters／worldbuilding；這裡只是本章會用到的部分，加上本章初譯已定的用詞。
段號為原文段號（`literary_edit.py plan 14` 的 pNNN；與 `translation/notes/chapter-14.md` 的段號相同）。

章節結構：p3–p29 飯店早晨、白給建議｜p30 分隔｜p31–p52 準決賽開場、新規則、開局（p35、p38、p40、p42、p44 是哲戈語倒數）｜
p53 棋盤 SVG｜p54–p60 君的攻勢｜p61 棋盤 SVG｜p62–p68 潛伏、再造一艘｜p69 棋盤 SVG｜p70–p80 第六至第十個干預回合｜p81 棋盤 SVG｜
p82–p89 築牆、獲勝｜p90 分隔｜p91–p101 等候室看德盧因對考、兩人約喝茶｜p102 分隔｜p103–p108 庭園｜p109 象形文字菜單 SVG｜
p110–p131 哲戈語第九版、紅郡照片、自然之美。

## 一、全章固定用詞（editor 一次只看一個 chunk，看不到別處的叫法；這些不要換）

| 原文 | 本章用法 | 出現位置／說明 |
|---|---|---|
| alarm | 鬧鐘（p3）／警報（p87） | |
| room service menu | 客房服務選單 | p4 |
| fruit and vegetable juice | 蔬果汁（之後簡稱「果汁」） | p4、p6、p11 |
| lobby／lobby restaurant | 大廳／大廳餐廳 | p7 |
| jie mo kai tu jie hei ja ma? | 保留拼音與半形問號 | p10、p107 |
| in a cute voice … making fun of the restaurant robots | 用的是一種裝可愛的聲音，擺明了在取笑餐廳的機器人 | p10 |
| semi-final(s) | 準決賽 | p13、p29、p31、p33 |
| *illicit* | *不正當*（強調保留） | p16 |
| Arctic spy | 北極間諜 | p17 |
| practice sessions／practice game | 練習／練習賽 | p17、p24 |
| rolled his eyes slightly | 微微翻了個白眼 | p18 |
| Basic social skills. I needed to learn them to survive growing up. | 基本的社交技巧。我是為了活下去，從小就得學會。 | p19（譯者筆記；不加情緒） |
| I appreciate you | 有你真好 | p20 |
| way too impatient | 太沒耐心了 | p23 |
| *definitely* Gun | 君*絕對*是 | p23（強調保留） |
| scoring system of the qualifying rounds | 資格賽的計分方式 | p24 |
| eight thousand turn threshold | 八千回合的門檻 | p24 |
| fast for the sake of being fast | 為了快而快 | p24 |
| vegetable and rice dish | 菜飯 | p28 |
| announcer voice | 播報的聲音 | p31 |
| qualifiers | 資格賽 | p32 |
| average win time of 5,047 turns | 平均獲勝時間 5,047 回合（阿拉伯數字） | p32 |
| best-two-out-of-three | 三戰兩勝 | p33 |
| national champion | 全國冠軍 | p33 |
| rule change | 規則變化 | p34 |
| resources … allocate／reduced by eighty percent | 可以配置的資源／減少百分之八十 | p34、p36 |
| shrine(s) | 神壇（避免：神社、神龕）；中央／南方／東方／西方／北方神壇 | p34 起 |
| center of each edge of the board | 棋盤四邊的中央 | p34 |
| applied as an XOR | 以 XOR 的方式套用 | p34 |
| reset to being a default rock formation | 重置成預設的岩塊 | p34 |
| mass conservation | 質量守恆 | p36 |
| decreases entropy | 讓熵減少 | p36 |
| weight-preserving／reversible | 保持權重／可逆 | p36 |
| *steering* | *掌舵*（強調保留；呼應維瑞迪亞掌舵制度） | p36 |
| walls, gliders and spaceships | 牆、滑翔機和太空船 | p37 |
| steerable symbol-carrying spaceship | 可轉向載印記太空船 | p37 |
| intervene in only a few cells | 只要干預其中幾格 | p37 |
| eternal glider factory | 永恆滑翔機工廠 | p39 起 |
| glider storm(s) | 滑翔機風暴 | p41 起 |
| sacrifice the west | 放棄西邊 | p41 |
| optimizing his structures | 最佳化他的結構 | p43 |
| fleet | 艦隊 | p47 |
| symbol-carrying spaceship／ship | 載印記太空船／載印記船 | p47 起 |
| flew past each other | 擦身而過 | p48 |
| attack／defend／set up | 攻擊／防禦／建立 | p49 |
| heading | 航向 | p51 |
| collision course | 碰撞航線 | p55 |
| mobile structure | 可移動的結構 | p57、p92 |
| steered（that spaceship） | 引導（避開「操縱」） | p57 |
| visual range／visual field | 視野範圍／視野 | p57、p71、p83 |
| northeastern base／southwest base | 東北基地／西南基地 | p57、p59 |
| northern rock shrine | 北方的岩石神壇 | p57 |
| advantage in material | 物資上的優勢 | p62 |
| lay low | 低調 | p63 |
| five-intervention-turn-long quest | 為期五個干預回合的任務 | p63 |
| sandbox | 沙盒 | p64、p84 |
| wreak havoc | 大肆破壞 | p64 |
| sitting duck | 活靶 | p68 |
| barrage of gliders | 滑翔機齊射 | p70 |
| judiciously ignored | 審慎地不去管 | p73 |
| debris | 殘骸 | p73、p80、p85、p94 |
| steering instruction | 轉向指令 | p74 |
| breach the walls | 突破牆壁 | p76 |
| wreck could still coast west | 殘骸仍然可以繼續往西滑行 | p78 |
| stray glider(s) | 亂飛的滑翔機 | p83、p85、p94 |
| mirror image | 鏡像版本 | p84 |
| Hunker down, play defense, outlast. | 蹲低、防守、撐到最後。（三短句節奏保留；ch15 p101 鄧會呼應「蹲低防守，撐得比對手久」） | p85 |
| four layers of walls | 四層牆 | p86 |
| waiting room | 等候室 | p91 |
| fortified | 固守 | p92 |
| reflect it | 反射回去 | p92 |
| Ten thousand two hundred turns into the game | 比賽進行到第一萬零兩百回合 | p95 |
| elevator | 電梯 | p96 |
| courtyard | 庭園 | p103 |
| menu | 菜單 | p108 |
| A/B testing | A／B 測試（初譯寫「A/B 測試」，保留初譯字面） | p112 |
| Dzegoban version nine | 哲戈語第九版 | p112、p114 |
| roots | 字根 | p115、p119 |
| hieroglyphs | 象形文字 | p115 |
| pronunciation perfectly readable from the glyph | 光看字形就能完全讀出發音 | p115 |
| grammar look more like math | 文法看起來更像數學 | p115 |
| pronunciation markers／consonant／vowel | 發音標記／子音／母音 | p116 |
| vein(s) | 葉脈 | p117 |
| 'ja'／'kai' | 『ja』／『kai』 | p116、p117 |
| 256 roots | 256 個字根 | p119 |
| in a lecturing tone | 用說教的語氣 | p119 |
| last-minute tutoring／top players | 賽前最後衝刺的指導／頂尖選手 | p121 |
| castles, pine forests, large pristine grasslands, red-colored mountains …, giant icy waterfall | 城堡、松林、大片未經開發的草原、山頂積雪的紅色山脈、一座巨大的冰瀑 | p125 |
| back-handed compliment | 明褒暗貶 | p127 |
| orbital dynamics and biology and tectonics | 軌道力學、生物學和板塊構造 | p127 |
| strip-mining | 露天開採 | p128 |
| championship winnings | 冠軍獎金 | p131 |

## 二、本章出現的 bible 譯名（`uv run tools/literary_edit.py terms 14` 產生）

- 人名：Zei → 澤（避免：賊）；Zei Leimin → 澤・雷明；Bai → 白；Deluin → 德盧因；Gun Caibai → 君・采百；Gun → 君；Kau Seiza → 考・世薩；Kau → 考
- 地名：Redshire → 紅郡（避免：雷德郡）；Dzego → 哲戈（避免：澤戈）；Pafogai Du → 帕佛蓋都；Sadzu Du → 薩祖都；Dzundei → 尊德；Geijaken → 紀嘉肯
- 明盤台：glider → 滑翔機（避免：滑翔翼）；spaceship → 太空船（避免：飛船）；rock formation → 岩塊；symbol → 印記；intervention turn → 干預回合；
  sandbox → 沙盒；shrine → 神壇；eternal glider factory → 永恆滑翔機工廠；symbol-carrying spaceship → 載印記太空船；glider storm → 滑翔機風暴；
  debris → 殘骸；sitting duck → 活靶
- 技術：entropy → 熵；xor → XOR（避免：異或）；mass conservation → 質量守恆；weight-preserving → 保持權重；A/B testing → A／B 測試
- 其他：best-two-out-of-three → 三戰兩勝；national champion → 全國冠軍；hand device → 手持裝置（避免：手機）；watch → 手錶；
  Dzegoban → 哲戈語；hieroglyphs → 象形文字；Firemoon → 火月
- 哲戈語：jie mo kai tu jie hei ja ma?、FI LE GEI TAU FA、MU GU GEI TAU FA、PA GU……、SO……BI……ZE……HA……MU……FO……SHI……LE……PA……、TAU FA——
  全部保留拼音；原文倒數後有句點的保留「。」，沒有的不加（初譯 p35「FI LE GEI TAU FA。」、p38「MU GU GEI TAU FA。」、p44「TAU FA。」）。

## 三、人物口吻與稱謂

- 澤：數理腦，比賽中的內心推理冷靜、條理分明；對白、德盧因用「你」。p99 自嘲「我的打法比你難看多了」；p130 開玩笑。
- 白：對澤的語氣已從挑釁轉為關心、仍帶點損人；p10 裝可愛學機器人；p19 坦白成長，不加情緒；p25「所以能不急就別急，好嗎，澤？」。
- 播報（p31–p34）：主持播報，正式、熱烈（「史詩對決」）。
- 德盧因：開朗、同輩口吻；p119 說教語氣；p127–p128 一段真誠、稍帶說教的長篇感想；p131 俏皮回嘴（QA 定：是德盧因自己贏冠軍、替澤付旅費）。
- 說話者（**原文未標說話者的輪次一律照初譯，不補標籤**）：p10 白、p11 澤、p12 澤（未標）、p13 白、p14 澤、p16 澤、p17 白、p19 白、p20 澤、p22 澤、
  p23–p25 白、p27 澤；p31–p34 播報；p88 播報；p97 澤、p98 德盧因、p99 澤、p100（未標，可能任一方）、p101（未標）；
  p104 澤、p107 機器人、p110 澤、p111 德盧因、p112 澤、p114 澤、p115 德盧因、p116 澤、p117 德盧因、p118 澤、p119 德盧因、p120 澤、p121 德盧因、
  p122–p123 澤、p124 德盧因、p126 澤、p127–p128 德盧因、p129 澤、p130 澤（「他開玩笑說」，譯文用「他」不點名）、p131 德盧因。
- 君、考：只在比賽敘述中出現。考性別未明，初譯在 p94「德盧因的牆讓他比考安全得多」的「他」指德盧因——不要替考補代名詞。

## 四、伏筆與資訊邊界（不可加暗示）

- p6：「三分鐘後」；「一刻也不耽擱」。
- p10：「擺明了」在取笑（unambiguously）。
- p17：每場都看、跟幾個選手交朋友、參加「一些」練習。
- p18：「微微」翻白眼，接著鬆一口氣。
- p21：停頓了一會兒。
- p23：君「絕對」是，但其實其他人也一樣；不只想贏，還想贏得快。
- p24：她「知道」計分方式會鼓勵這樣；過了八千回合門檻仍延續；連君和德盧因的練習賽也是。
- p29：「十分鐘後」。
- p32：四十天；四人戰績與平均獲勝回合數一個都不能錯。
- p33：「十五天後」三戰兩勝（ch15 決賽取消，不預示）。
- p34：干預回合資源減少百分之八十；五座神壇（四邊中央各一、正中心一）；每一千回合，神壇內容的變化以 XOR 套用到神壇四個角附近，然後重置成預設岩塊。技術說明，不補畫面。
- p36：神壇是「唯一」違反質量守恆的物件；但「即使」如此也沒有東西讓熵減少；XOR 不保持權重但可逆；棋盤會越來越滿、越來越亂；干預回合不是用來建造，是用來*掌舵*。
- p37：幾個月前開發的設計；「只要」干預其中幾格就能改變方向。
- p39：「剛好」兩個干預回合；「剛好對的方向」；兩座神壇變成一座永恆滑翔機工廠：來回反彈、每次碰撞撞碎岩石往更北邊噴出更多滑翔機、每一千回合岩石重置。
- p41：保護太空船前往中央、東邊和南邊；放棄西邊。
- p43：直到最後一刻都在最佳化。
- p46：「一千回合後」第一個干預回合。
- p47：重大弱點：做印記可以，但做載印記太空船或滑翔機工廠要四個干預回合；三艘就是全部艦隊。
- p48：「就在」第二個干預回合之前；他的一艘和君的兩艘在中央擦身而過；「顯然」君更執著於中央。
- p49：三個選項（攻擊／架牆／永恆工廠）。
- p50：中央–南、中央–東、南–東三組反彈。
- p51：君做了「一模一樣」的事；兩艘船也往南。
- p52：兩人都看不到全局，但觀眾看得到。
- p54：「幾百回合後」；君的攻勢更有效；中央–南、中央–西兩座工廠＋摧毀澤的載印記太空船。
- p55：其中一艘與澤的船在碰撞航線上；碰撞會在下一個干預回合之前發生。
- p56：只會剩東邊那艘。
- p57：最後一艘是君「完全不知道」的唯一可移動結構；最大優勢「或許」（might）就是維持這樣；暫時停在君東北基地視野外；「肯定存在的」印記（undoubtedly）；滑翔機不直接往北，從北方岩石神壇反彈。
- p58：東南的印記一個接一個消失：先被君的工廠，再被君那艘從南方往東移動的載印記太空船新射出的滑翔機。
- p59：「瞥見」（briefly saw）君的船出現在西南基地附近——緊接著它射出滑翔機把基地摧毀（譯者筆記：it 指基地）。
- p62：君在物資上有很大優勢，「澤知道」；唯一優勢是保持隱藏；東北角正南方是「比較安穩的地方之一」。
- p64：回想中央那艘被摧毀前看到的岩塊樣子 → 沙盒複製 → 中央–北方工廠攻君的西北。
- p65：「重創」西北基地——但澤沒辦法知道損害多少。
- p66：「不久之後」；東南最後一個印記被滑翔機風暴摧毀；最後一幕：君的船開始往北。
- p67：這次讓滑翔機淹沒西邊中央一帶。
- p68：沒移動，也沒辦法移動：接下來三千回合在造新船，是活靶。
- p70：君的船正被齊射擊中時第六個干預回合到來 → 君「幸運」擋下，多撐「一會兒」。
- p71：最後還是被摧毀，但已進入澤那艘船的視野範圍。
- p72：君看得到澤的船，但看不到正在建造的新船。
- p73：「唯一能做的事」；沿西邊和對角線多架牆；審慎地不管南邊：既有風暴＋君的船的殘骸本身就夠當屏障。
- p74：所有資源投入新船；「快好了」；下一回合剛好夠完成，並對兩艘船各下一道轉向指令。
- p76：一開始牆擋住；滑翔機源源不絕，很快開始突破。
- p77：「及時」到來；還沒被摧毀，但快了。
- p78：兩艘都往西；他「判斷」舊船的印記會在一百回合內被摧毀，殘骸仍可往西滑行、撞上北方神壇、往南釋放滑翔機風暴；新船*也*往西（強調保留），停在北方神壇正北邊，得到「一些」掩護。
- p79：利用快被打爛的岩塊反彈滑翔機往南、重新調整往南攻擊的工廠；沒時間計算、也沒辦法知道確切後果，但「希望」讓原本安全的地方變得不安全；再往西發動一波攻擊。
- p80：「似乎」什麼也沒發生，只有殘骸。越來越多的殘骸。（短句節奏保留）
- p83：「希望能」在南方製造更多混亂；其中一架還沒飛出視野就被撞毀。
- p84：最後一招：從自己的牆反彈往南、貼著神壇邊緣；沙盒模擬：撞上中央神壇的角就往北反彈；在中央和北方之間來回；每次撞中央同時放出一架往西的；*那架*撞西方神壇後往東南，「希望能」對南方造成損害；東邊做鏡像。技術說明，不補畫面。
- p85：殘骸和亂飛滑翔機密集到「不可能」進攻。
- p86：四層牆；牆終於開始崩塌得比他造得快。
- p87：「又過了幾百回合」，警報響起。
- p91：澤「既意外又佩服」；德盧因前期全副心思用北邊和東北邊岩塊的資源築牆；同時送滑翔機建朝南的工廠。
- p92：沒造任何可移動的載印記太空船；考的工廠作用有限：滑翔機會永遠來，但只在短時間內有效果；每當風暴來，德盧因都會想出辦法反射回去。
- p93：「看來」德盧因「也」想通了要更有耐心。
- p94：「七千回合後」考躲在南方神壇後；「只勉強」多撐了三千回合。
- p95：第一萬零兩百回合。
- p99：「基本上」也是靠防守贏的。
- p103：澤一看到他就跑過去。
- p112：「我想」這些是 A/B 測試的新符號。
- p113：他「馬上想到」自己在跟外國人說話。
- p115：「有幾個人」提過；三件事：視覺化／象形文字找回字根、看字形能讀發音／另一層讓文法像數學。
- p116–p117：推測語氣（「也許」「？」「不過……」）全部保留。
- p119：256 個字根、不到一個月、不會懂所有細微差別但到處走沒問題。
- p120：「幾乎」已經是本地人。
- p121：父母生日「只差幾天」；回紅郡（ch15 淪陷、ch19 揭露父母親北極——本章不預示）；頂尖選手的最後衝刺指導；半開玩笑的邏輯。
- p122：「實在沒有那個錢」；「也許過幾年」。
- p125：照片內容一項不少。
- p127：小時候的看法：明褒暗貶、「幾乎」算侮辱；那些東西不是人自己做的，是軌道力學、生物學、板塊構造隨機白送的；對那裡的人「相當」刻薄。
- p128：長大後明白完全不是這樣；三組「人力」排比（步道道路／政治制度：阻止汙染、砍森林、山坡蓋房子把山弄醜、露天開採，同時允許在看得到景色的地方蓋房子、維持可負擔、維持產業／修復在「夠有智慧、或者夠有錢」之前造成的破壞）——一項都不能少，排比節奏保留。
- p129–p131：「第一時間」；「希望」是在十五天後；用冠軍獎金替你付旅費。
