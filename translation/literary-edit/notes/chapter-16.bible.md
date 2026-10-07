# 第 16 章 bible 摘錄（第二輪文學編輯用）

主 Agent 依 WORKFLOW「開始一章前」第 5 步建立；每個 chunk 的資料包都附上這份（`literary_edit.py packet --bible`）。
權威來源仍是 glossary／characters／worldbuilding；這裡只是本章會用到的部分，加上本章初譯已定的用詞。
段號為原文段號（`literary_edit.py plan 16` 的 pNNN；與 `translation/notes/chapter-16.md`、`translation/qa/chapter-16.md` 的段號相同）。

章節結構：p2 日期線（梅爾丹，3724 年火月 25 日）｜p3–p30 包廂：格拉迪亞斯質問德爾瓦特、德爾瓦特認錯並建議去哲戈｜p31 分隔｜
p32–p50 走過卡利馬區、打給莫夫｜p51 分隔｜p52–p104 餐廳：與費布里克看旋翼球（p63、p67 計分板裝置畫面）、
社交恢復測試（p94 交易請求、p100 賽菈的安全提問、p102 格拉迪亞斯的回覆，皆為裝置畫面）｜p105 分隔｜p106–p119 回家告訴賽菈。
本章沒有 `>` 引言；裝置畫面（p63、p67、p94、p100、p102）不送編輯。

## 一、全章固定用詞（editor 一次只看一個 chunk，看不到別處的叫法；這些不要換）

| 原文 | 本章用法 | 出現位置／說明 |
|---|---|---|
| booth／barrier | 包廂／隔門 | p3（拉開隔門、再把隔門拉上） |
| sat down angrily | 氣沖沖地……坐下 | p3 |
| You have a lot of explaining to do. | 你有很多事得解釋清楚。 | p4（譯者筆記：開門見山地質問） |
| with a sorry expression | 一臉歉意 | p5 |
| you were right, I was wrong | 你是對的，我錯了 | p6 |
| interventionism | 干預主義 | p6 |
| defense | 國防 | p6 |
| That's not why I'm angry. | 我生氣不是為了這個。 | p7 |
| the primary | 最主要的 | p9、p10（「遠遠不是最主要的」→「那最主要的是什麼？」承接） |
| What the hell is going on? Who are you? Who are you working with? | 到底是怎麼回事？你到底是誰？你在跟誰合作？ | p11 |
| Fine, I will explain. | 好，我解釋。 | p13 |
| ideologue | 憑著理念單打獨鬥的人 | p14（譯者筆記：避免「理想主義者」的褒義） |
| working for Silverchat | 替銀聊工作 | p14、p37（「他一直都在替銀聊工作」，刻意呼應） |
| rubric(s) | 規準 | p15、p23、p47 |
| crude jokes | 粗俗的笑話 | p15 |
| refuge | 避風港 | p15 |
| blandness | 平淡（p15）／平淡化（p17） | 譯者筆記：與人物卡「對抗平淡化」一致 |
| take matters into our own hands | 自己動手 | p16 |
| organized effort | 有組織地努力（p16）／有組織的行動（p37） | p37 莫夫的推測得到證實，呼應 p16 與 ch15「組織程度」 |
| Appeal to the Keepers directly | 直接去遊說守律者 | p16 |
| naive | 天真 | p17 |
| ruinous | 會帶來毀滅 | p17（譯者筆記） |
| a dose of sympathy | 一點同情 | p18 |
| salad, a rectangular nutrition bar and water | 沙拉、長方形營養棒和水 | p19（ch13 德爾瓦特固定吃「長方形營養棒」） |
| What do you want me to do now? | 你現在要我怎麼做？ | p22 |
| make the rubric exclude military | 讓規準把軍事排除在外 | p23 |
| tax brackets | 稅級 | p23（呼應 ch15「調高稅級」） |
| levers | 槓桿 | p23（譯者筆記） |
| Graph Funding | 圖譜募資 | p23、p115、p117 |
| Study them. Learn from them. See what you can bring back to Veridia. | 去研究他們。向他們學習。看看有什麼能帶回維瑞迪亞的。 | p28，三個短句保留 |
| a lot to learn from them | 有很多要向他們學的（p42）／有很多東西要向那邊正在發生的事學習（p113） | 刻意呼應 p28「向他們學習」：德爾瓦特的建議→格拉迪亞斯轉述給莫夫→再轉述給賽菈（說成莫夫的想法） |
| untrustworthy | 不可信 | p29 |
| closest friends and advisors | 最親近的朋友和顧問 | p30 |
| Kalimar | 卡利馬區 | p32 |
| covered with trees／tree cover | 綠樹成蔭／樹蔭 | p32 |
| stone houses | 石砌的房子 | p32 |
| traditional Veridian food products | 維瑞迪亞傳統食品 | p33 |
| hastily taped on | 匆匆貼上去的紙條 | p33 |
| preserved food … sufficient for thirty days of survival | 保存食品，份量足夠撐過三十天 | p33（譯者筆記：與 glossary「三十天份」一致） |
| tapped his watch, and called Mov | 點了點手錶，打給莫夫 | p34 |
| at least he now says | 至少他現在是這麼說的 | p37（保留這層保留語氣） |
| evil company, like Bluewhale | 更邪惡的公司，像藍鯨之類的 | p38 |
| overheard a month and a half ago | 一個半月前我偷聽到的那場對話 | p39（呼應 ch15「我一個半月前發現的事」） |
| a Silverchat guy | 銀聊的人 | p39 |
| the day Redshire got taken over | 紅郡被佔領那天 | p43 |
| secret societies | 祕密社團 | p43 |
| Minpentai ranks／nationals | 明盤台的排名／全國賽 | p44 |
| institutions | 體制裡的人（p45）／整個體制（p113） | |
| the Order, the Courts, the parliament | 掌舵會、法院、議會 | p45；parliament 一律「議會」（p115、p117） |
| Give me a few days to think through this. | 給我幾天想清楚。 | p46 |
| eight, twelve and sixteen days | 八天、十二天和十六天後 | p47（三場規準投票） |
| I'll think about it too | 我也會想想。 | p50 |
| face cover | 臉罩 | p52 |
| partially unzipped the front | 把前襟的拉鍊拉開一半 | p52 |
| uncle Glad | 格拉德叔叔 | p53（原文小寫 uncle，照稱謂表） |
| Helisport | 旋翼球 | p55 |
| actively broadcasting | 正在直播 | p55 |
| the screen（following／shifted view） | 畫面跟著／畫面切到 | p56、p58、p59 |
| player wearing a yellow／purple shirt | 穿黃色球衣／穿紫色球衣的球員（p56–p58），之後簡稱黃衣球員／紫衣球員（p59–p61） | |
| redball／blueball／greenball／pins | 紅球／藍球／綠球／球瓶 | p56–p74 |
| regained his bearings about five meters further down | 往下掉了大約五公尺才自動恢復平衡 | p57（QA 修正，不可再改回「在五公尺外」） |
| ten yellow standing pins arranged in a triangle on a circular board mounted on a pole | 十支黃色球瓶，排成三角形立在一個圓盤上，圓盤架在一根桿子頂端 | p59 |
| zoomed into position | 飛速擋到 | p59 |
| about five meters over | 頭頂上方大約五公尺處 | p61 |
| knocked three of the pins down | 擊倒了三支球瓶 | p61 |
| scoreboard adjusted／score adjusted again | 計分板更新了（p62）／分數又更新了（p66） | |
| 計分板欄位（裝置畫面） | 黃隊／紫隊、搶下紅球、綠球擊中球員、藍球擊倒球瓶、總分 | p63、p67（譯者筆記，ch11 一致） |
| blueball score／combined score | 藍球分數／總分 | p64（20→23、1540→1771） |
| splatted its paint over him | 顏料濺了他一身 | p65 |
| scoring system | 計分制度 | p68 |
| ratios | 比例 | p69、p70 |
| the rational thing | 理性的做法 | p69 |
| strategies adjusted／lopsided | 戰術就會跟著調整／一面倒 | p70 |
| multiplicative／additive | 相乘／相加 | p71、p73（**兩詞全章與 ch28 一致，不可換成「乘法／加法」或「加總」**） |
| the only way out | 唯一的出路 | p71 |
| all three of the point types | 三種得分 | p71 |
| interjected | 插話 | p72 |
| Holding onto redballs for more than thirty ticks | 持紅球超過三十拍 | p73 |
| a good cheat | 很好用的作弊手段 | p73 |
| People on copters | 坐旋翼機的人 | p74（copter 一律「旋翼機」） |
| sitting duck | 活靶 | p74 |
| The math | 那些數學 | p76 |
| seventy on her latest civics test | 公民考試考了七十分 | p79 |
| that game on her hand device | 她手持裝置上的那個遊戲 | p79、p80（「什麼遊戲」），不猜是什麼遊戲 |
| She doesn't show me either. | 她也不給我看。 | p81 |
| zipcoins | 吉普幣 | p83、p95 |
| I may make lots of mistakes, but I don't make the same mistake twice | 我是會犯很多錯，但同樣的錯我不會犯兩次 | p84（呼應 ch06 付帳的事） |
| snapped back | 回嘴 | p84 |
| recovery procedure | 恢復程序 | p85 |
| whispered through／into his neck band | 透過頸帶低聲說（p85）／對著頸帶低聲說話（p92）／對著頸帶低聲回覆（p101） | |
| test operation／the operation | 測試交易（p86）／發起交易（p91） | operation 本章都譯「交易」 |
| Straight out of a life savings wallet? | 直接從存畢生積蓄的錢包扣？ | p89（glossary） |
| Those ads really have been getting to you too | 那些廣告真的也把你洗腦了 | p89 |
| incredulously | 不可置信地 | p89 |
| Okay fine ... | 好啦好啦…… | p91 |
| watch buzzed | 手錶震了一下（p93、p98）／手錶又震了（p99、p103） | |
| A few ticks later | 幾拍之後 | p93、p95 |
| [Wallet 0x8f62... social recovery mode transaction request] | ［錢包 0x8f62... 社交恢復模式交易請求］ | p94 裝置畫面（全形方括號，地址原樣） |
| a more detailed view of the transaction | 更詳細的交易內容 | p95 |
| asked Emerald | 請翡翠 | p95（Q7：翡翠是通用 AI 服務，不寫成格拉迪亞斯專屬） |
| receiving address | 收款地址 | p95 |
| the Hydrafill purchase address | 海卓菲的購買地址 | p95 |
| shipping | 運費 | p95 |
| transaction data field | 交易資料欄位 | p95 |
| standard online shopping protocol | 標準網路購物協定 | p95 |
| cryptographic network | 密碼學網路 | p96 |
| clicked "Confirm" | 按下「確認」 | p97 |
| Security question: | 安全提問： | p100 裝置畫面（glossary） |
| the evening the kids came back from Vil and Daia's | 孩子們從維爾和黛亞家回來那天晚上 | p100 |
| Lord Ephelion's speech | 艾費里昂勳爵的演說 | p102 裝置畫面（ch13 賽菈拔螢幕插頭一事） |
| Three signatures done, including his own. One to go. | 三份簽章完成，包括他自己的。還差一份。 | p103 |
| vault／second key | 保險庫／第二把金鑰 | p103 |
| I'm home! | 我回來了！ | p106 |
| interesting news | 有個有趣的消息 | p108 |
| a strong hand guide them | 一隻強而有力的手來引導 | p114（譯者筆記） |
| make good use of a Dzego trip／a trip | 善用哲戈之行（p114）／好好利用這趟旅程（p115） | 賽菈的話被格拉迪亞斯接過去反用，刻意呼應 |
| do your homework first | 先做好功課 | p117 |
| think hard about this | 好好想清楚 | p118（與 p46「給我幾天想清楚」、p47「好好想」同一條「想清楚」線） |
| introduce you to Zei. And Bai too. | 介紹澤給你認識。還有白也是。 | p119（回應 p115「如果你介紹我認識澤」） |

## 二、本章出現的 bible 譯名（`uv run tools/literary_edit.py terms 16` 產生）

- 人名：Gladias → 格拉迪亞斯（避免：格拉迪斯、葛拉迪亞斯）；Glad → 格拉德；Seila → 賽菈（避免：塞拉、席拉）；Zven → 茲文；Lily → 莉莉（避免：百合）；
  Febric → 費布里克；Vil → 維爾；Daia → 黛亞；Mov → 莫夫；Delwart → 德爾瓦特；Ephelion → 艾費里昂；Emerald → 翡翠（避免：祖母綠）；
  Zei → 澤（避免：賊）；Bai → 白；Pelow → 佩洛
- 地名：Veridia → 維瑞迪亞（避免：韋里迪亞）；Meldan → 梅爾丹；Kalimar → 卡利馬（區）；Redshire → 紅郡（避免：雷德郡）；Dzego → 哲戈（避免：澤戈）
- 組織／制度：Arctic Empire → 北極帝國（避免：北極圈帝國）；Bluewhale → 藍鯨；Silverchat → 銀聊；Hydrafill → 海卓菲；Dreadknot → Dreadknot；
  Courts → 法院；the Order → 掌舵會；Keeper → 守律者；Graph Funding → 圖譜募資（避免：圖表募資、圖形融資）；rubric → 規準（避免：評分標準）；
  civics → 公民；interventionism → 干預主義；Minpentai → 明盤台
- 錢包／密碼學：cryptographic network → 密碼學網路（避免：加密網絡）；social recovery → 社交恢復（避免：社會恢復）；wallet → 錢包；transaction → 交易；
  receiving address → 收款地址（避免：接收地址）；transaction data field → 交易資料欄位（避免：交易數據字段）；recovery procedure → 恢復程序；
  security question → 安全提問（避免：密保問題）；life savings wallet → 存畢生積蓄的錢包；vault → 保險庫（避免：金庫）
- 旋翼球：Helisport → 旋翼球（避免：直升機運動）；redball → 紅球；greenball → 綠球；blueball → 藍球（避免：籃球）；pin → 球瓶（避免：別針）；
  copter → 旋翼機（避免：直升機）；sitting duck → 活靶（避免：坐著的鴨子）
- 其他：hand device → 手持裝置（避免：手機）；watch → 手錶；neck band → 頸帶；privacy robe → 隱私袍（避免：隱私長袍）；face cover → 臉罩（避免：面罩）；
  nutrition bar → 營養棒（避免：營養條）；preserved food → 保存食品；zipcoin → 吉普幣；tick → 拍；Firemoon → 火月

## 三、人物口吻與稱謂

- **本章沒有澤、鄧、蘇出場**（澤、白只在 p44、p115、p119 被提到），characters 稱謂表「澤對鄧、對蘇用『您』」不適用；初譯全章沒有「您」，也不要加。
- 格拉迪亞斯：對德爾瓦特用「你」，開門見山、怒氣壓著（p4、p7、p11 三連問、p29 直說「你一直這麼不可信」）；p18 起怒氣摻進同情，但不軟化成和解。
  對莫夫用「你」，報告式、簡短。對費布里克用「你」，俏皮回嘴（p84）、不可置信地吐槽（p89）。對賽菈用「你」，p110 試探、p115 討價還價（「說不定我就能好好利用這趟旅程？」）。
- 德爾瓦特：對格拉迪亞斯用「你」，p6 直呼「格拉迪亞斯」（稱謂表：認錯時直呼其名）。p6–p17 低姿態但條理分明；⚠ 自白是謊言（ch20 賽菈推翻、ch21 揭露他是北極的人），**譯文維持他誠懇認錯的人設，不露破綻、不加猶豫或閃爍的描寫**。p23–p30 給建議時恢復一點自信，但仍讓步（p30「當然別只聽我的」）。
- 莫夫：對格拉迪亞斯用「你」；簡短、口語、損友味（p38「我還以為會是更邪惡的公司」、p41「去幹嘛？」）；p43 的「*我*」斜體照原文保留。
- 費布里克：稱「格拉德叔叔」、用「你」；青少年口語、興奮地講計分歷史（p69–p74 一路講下去）；調皮（p83）；懂分寸（p104）。
- 賽菈：稱「格拉德」（p107）、用「你」；p114 先保留（停頓「……」保留），p117 有條件同意、務實叮嚀，p118–p119 收尾溫和。
- 翡翠：本章只被轉述（p95），不直接說話，代名詞「它」若需要時使用。
- 說話者（**原文未標說話者的輪次一律照初譯，不補標籤**）：
  - p3–p30：p4 格拉迪亞斯、p6 德爾瓦特、p7 格拉迪亞斯、p9 格拉迪亞斯（未標，接著 p7 補充）、p10 德爾瓦特、p11 格拉迪亞斯、p13–p17 德爾瓦特（連續四段自白）、
    p22 格拉迪亞斯（有標）、p23–p24 德爾瓦特、p25 格拉迪亞斯、p26 德爾瓦特、p27 格拉迪亞斯、p28 德爾瓦特、p29 格拉迪亞斯、p30 德爾瓦特。
  - p35–p50（通話）：p35 格拉迪亞斯、p36 莫夫、p37 格拉迪亞斯、p38 莫夫、p39 莫夫（未標，連續第二段；譯者筆記與 QA 判斷：overheard 指莫夫偷聽）、p40 格拉迪亞斯、p41 莫夫、
    p42 格拉迪亞斯、p43 莫夫、p44 格拉迪亞斯、p45 莫夫、p46 格拉迪亞斯、p47 莫夫、p50 格拉迪亞斯（原文只寫 he，初譯「他」，**不點名**；譯者筆記與 QA 判斷）。
    p46–p47 原文都未標：另一種讀法是 p46 莫夫、p47 格拉迪亞斯（投票是格拉迪亞斯的事，p50 的 too 也較順）。初譯兩段都不標、「你都有這段時間」兩種讀法皆通——**維持不標，不要寫死任何一方**。
  - p53–p104（餐廳）：p53 費布里克、p54 格拉迪亞斯、p68–p71 費布里克（p68 有標，p69–p71 未標、延續）、p72 格拉迪亞斯（有標）、p73–p74 費布里克、p75 格拉迪亞斯（有標）、p76 費布里克、
    p78 格拉迪亞斯、p79 費布里克、p80 格拉迪亞斯、p81 費布里克、p83 費布里克、p84 格拉迪亞斯、p85 格拉迪亞斯（透過頸帶低聲對費布里克說）、p86 費布里克（未標）、p87 格拉迪亞斯、
    p88 費布里克、p89 格拉迪亞斯、p90 費布里克、p91 格拉迪亞斯、p104 費布里克。
  - p106–p119（家）：p106 格拉迪亞斯、p107 賽菈、p108 格拉迪亞斯、p109 賽菈、p110 格拉迪亞斯、p112 賽菈、p113 格拉迪亞斯、p114 賽菈、p115 格拉迪亞斯、p117–p119 賽菈（連續三段）。
- p13–p17、p23–p24、p69–p71、p73–p74、p117–p119 都是同一人連續多段：可以保持分段，不要把對方的話併進來；合段時也不要讓下一段看起來換了說話者。

## 四、伏筆與資訊邊界（不可加暗示）

- p3：拉開隔門、走進去、再把隔門拉上；「氣沖沖地」坐下。
- p5：低頭看著桌面、一臉歉意——這是德爾瓦特的表演或真心，譯文不判斷。
- p6：「你是對的，我錯了」；恨意蒙蔽；有些事「一直」是政府該做的，國防是其中之一。
- p8：抬起頭，嚇了一跳（startled）——只寫這個反應，不補「心虛」之類。
- p9：「原因之一，但遠遠不是最主要的」。
- p12：嘆氣、「沉默了片刻」（a few moments）、身子往前傾。不補他在盤算什麼。
- p14：「不只是一個」憑理念單打獨鬥的人；「我，還有另外一群人——我不認識他們——」（插入語與破折號保留）；替銀聊工作。⚠ 謊言，照字面誠懇地譯。
- p15：不滿的原因只有一個：「只因為一堆人在我們平台上講粗俗的笑話」就調高稅；目標：避風港、躲開「正在吞沒維瑞迪亞其他大部分地方」的平淡；連海卓菲、「甚至」Dreadknot 都受歡迎。
- p16：有組織地努力、「試著」把政治往更好的方向拉、直接遊說守律者。
- p17：「現在我才明白」多天真；條件句「如果……代價卻是……」；先紅郡、之後全世界；「不只是不值得，而是會帶來毀滅」。
- p18：「還是非常」生氣；怒氣裡「現在也摻進了一點」同情（a dose）。不要寫成原諒。
- p19–p21：機器人送沙拉、長方形營養棒和水；先把盤子放到桌上；格拉迪亞斯一口氣喝「大約半杯」，德爾瓦特也一樣；「默默」吃；「過了幾分鐘」。
- p23：「當然」現在別讓規準把軍事排除在外；「甚至可以」調高稅級，但「只能幫上一點點」；最重要的槓桿在圖譜募資那邊。
- p28：「顯然」比我們想得透徹多了。
- p29–p30：格拉迪亞斯質疑他「一直這麼不可信」；德爾瓦特「當然別只聽我的」，要他問最親近的朋友和顧問——不要讓德爾瓦特顯得狡猾或真誠，照字面。
- p32：「平常會走的那條路」；「跟往常一樣」綠樹成蔭、兩旁石砌房子；「但那天異常炎熱」；「有些」陽光穿過樹蔭；「微微」出汗。
- p33：他「記得」是賣維瑞迪亞傳統食品的房子；「這次」海報上多了「匆匆」貼上的紙條；組合包：美味、營養完整、可長期保存、三十天份。戰爭陰影只靠這張紙條帶出，不另加評論或格拉迪亞斯的感想。
- p37：「你說對了」；「至少他現在是這麼說的」——格拉迪亞斯對自白保留懷疑，這句要留著。
- p38：莫夫原本以為會是「更邪惡的」公司，像藍鯨。
- p39：「我想這說得通」；「大概」（probably）就是銀聊的人；「一個半月前」。
- p43：紅郡被佔領「那天」；有朋友也提過「類似的事」；覺得「*我*」應該去；看看他們的祕密社團「是怎麼運作的之類的」（or something，口語含糊保留）。不暗示這個朋友是誰。
- p44：賽菈「現在」有個那裡的朋友（澤，不點名）；「上次」跟他說；「一路往上爬」、已打進全國賽；「說不定」真的能學到一些東西。
- p45：「當然看得出這有什麼好處」；「尤其是」體制裡的人。
- p47：規準的投票在「八天、十二天和十六天後」；「不管怎樣」都有這段時間。
- p48–p50：「停頓了一會兒」；「那時」正經過家附近常去的餐廳；「透過窗戶」看到費布里克在吃飯；「終於」說「我也會想想」，結束通話。
- p52：「幾乎一進門」就摘下臉罩、前襟拉鍊拉開「一半」；理由兩個：「反正吃東西時也沒辦法那麼隱密」「剛剛在大太陽底下一直流汗」。
- p55：注意到費布里克「一直在看」螢幕；正在直播旋翼球。
- p56：「讓自己」看了「一分鐘」（let himself，小小的放縱）。
- p57：「不知從哪裡冒出來」；撞到一旁；翻滾；往下掉了「大約五公尺」才「自動」恢復平衡（AI 緩衝，不另解釋）。
- p58：「另外兩名」黃衣球員；「在他們趕到之前」傳給隊友；隊友「順利」接住。
- p59：「十支」黃色球瓶、三角形、圓盤、桿子頂端、高高離地。
- p60：「突然」高拋，「就在這時」另一名黃衣球員撞上他。
- p61：「大約五公尺」；擊倒「三支」。
- p63–p67：計分數字照原文，不可改。總分＝三項相乘：黃 6×9×31＝1674、紫 11×7×23＝1771；p64 紫隊藍球 20→23、總分 1540→1771，「足以」超前；p65 綠球擊中背部；p67 黃隊綠球 9→10、總分 1860（6×10×31）。散文不要替讀者算出乘法（原文沒有算式）。
- p68：「你得承認」；「現在的」計分制度。
- p69：「我小很多的時候」；「一直在調整」比例；「就是擺脫不了」——理性的做法是把全部心力集中在「其中一項」。
- p70：「就算」調對了，「不到一年」又一面倒。
- p71：「我覺得」相乘是「唯一的」出路；「幾乎非得」三種都兼顧。
- p72：格拉迪亞斯補「或是拚命讓對手某一種分數一分都拿不到」（相乘的另一面：一項為零則總分為零），不替他解釋。
- p73：「一開始有些人最先試的」；持紅球超過「三十拍」「早就被禁止很久了」；那招在「分數還是相加的時候」對紅球較弱那隊好用；「有一隊確實試過」：一開始先擊倒一大堆球瓶、剩下比賽派「大部分」球員守球瓶。
- p74：「結果根本沒用」；擠得多密「也有限」；「總是能偷塞幾顆」藍球；圍成一團就成了綠球的活靶。
- p76：「沒有」；「剛跟茲文聊了好多這個」；數學「幾乎」跟比賽一樣好玩。
- p79：「這兩個月」「其實開始好一點了」；「幾天前」說；公民考「七十分」；「看起來」比較開心（seems）；「更投入」玩那個遊戲。⚠ 那個遊戲與北極宣傳有關（ch23 揭露），**照原文不加暗示**，不要讓格拉迪亞斯或費布里克顯得起疑。
- p80–p81：格拉迪亞斯只問「是什麼遊戲」；「她也不給我看」（either：她也沒給格拉迪亞斯看）。不補反應。
- p82：「又繼續吃」；「幾分鐘後」都吃完。
- p83：「這次」有記得帶吉普幣嗎（呼應 ch06），「調皮地」問。
- p85：「謝謝你提醒我」——是被吉普幣的玩笑提醒；「低聲」透過頸帶說。
- p86：費布里克主動提「幫你簽一筆測試交易」——他是社交恢復的金鑰持有人之一，原文沒有明說，不補說明。
- p88–p90：海卓菲是費布里克隨口提的；格拉迪亞斯吐槽廣告「也」把他洗腦了（too：不只別人）。
- p92：眼角餘光瞥見費布里克「跑去某個地方」，但「忙得沒空去想」他去哪裡——不補理由（不要寫成去找隱密處）。
- p93：「幾拍之後」，費布里克的手錶震了一下。
- p95：交易細節的檢查順序：請翡翠查收款地址→「幾拍之後」翡翠確認「確實」是海卓菲的購買地址→金額 5.5 吉普幣，「似乎」合理（seemed），「大部分肯定」是運費→交易資料欄位「看起來」（looked like）是格拉迪亞斯家地址的編碼、格式符合標準網路購物協定。順序與語氣都保留。
- p96：密碼學網路裡這些資料「當然」全都加密（作者旁白，一句，不擴寫）。
- p98：「立刻」震了一下（費布里克的簽章）。p99：「不到一分鐘」又震了（賽菈的安全提問）。
- p100：安全提問只問「最不尋常的一件事」，答案在 p102（ch13 賽菈拔掉播放艾費里昂演說的餐廳螢幕插頭）；散文不要提前說出答案或解釋。
- p101：「立刻」低聲回覆。
- p103：「過了一會兒」（a few moments）；「三份」簽章完成、「包括他自己的」；「還差一份」；莫夫「或」佩洛「都行」；「當然，真的不得已的話」也可以自己跑去保險庫拿「第二把」金鑰。社交恢復門檻（六取四）不在本段寫出，不補。
- p104：「當然不會問」那是誰、也不會問還需要誰——呼應 ch06「這些人彼此都不知道其他恢復人是誰」，不要補說明。
- p110：「可能」（there's some chance）「很快」要去哲戈——語氣是可能，不是已決定。
- p111：賽菈「愣愣地看著他」（stared），不補表情或情緒。
- p113：⚠ 格拉迪亞斯說是「我跟莫夫談過了。他覺得……」——事實上是德爾瓦特提議（莫夫只在 p45 附和「維瑞迪亞人需要多了解外面的世界」）。**照原文，不替他圓，也不加心虛描寫**；他沒提德爾瓦特。
- p114：「我不太確定……」（停頓保留）；it's a difficult time 是「時局艱難」（戰爭陰影），初譯「現在這個時機很難說」容易讀成「時機對不對很難說」，可改成時局艱難的意思，但不要加戰爭細節；「其實不是最能」善用哲戈之行的人；「接下來這幾個月」守律者會需要強而有力的手引導。
- p115：北極的事「其實比較是」軍方和議會的責任，「也許還有」圖譜募資；「而且……」（停頓保留）；「說不定」——條件句「如果你介紹我認識澤」。
- p116：「陷入沉思片刻」（a few moments）。
- p117：條件同意：「如果莫夫覺得這是個好主意，那好吧」；「拜託你先做好功課」；「找個人，隨便誰都好」，圖譜募資或議會裡；兩個目的：知道這趟有沒有用、真要去怎麼發揮最大用處。
- p118：「不過說真的」，好好想清楚。
- p119：「如果你去」，「當然」介紹澤；「還有白也是」。
