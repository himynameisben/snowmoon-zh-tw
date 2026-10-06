# 第 21 章 bible 摘錄（第二輪文學編輯用）

主 Agent 依 WORKFLOW「開始一章前」第 5 步建立；每個 chunk 的資料包都附上這份（`literary_edit.py packet --bible`）。
權威來源仍是 glossary／characters／worldbuilding；這裡只是本章會用到的部分，加上本章初譯已定的用詞。
段號為原文段號（`literary_edit.py plan 21` 的 pNNN；與 `translation/notes/chapter-21.md` 的段號相同）。

章節結構：p2 dateline（梅爾丹，霧季 20 日）｜p3–p39 晚餐：共養家庭圍桌（費布里克與赫蕾妲困在大梅港、維爾告分歧的官司、莉莉公民考、茲文的火箭、賽菈談掌舵會被操弄，茲文脫口「是北極人嗎？」）｜
p40 分隔｜p41–p107 賽菈在地下室等格拉迪亞斯醒來，打電話痛罵他，推理德爾瓦特是北極的人，逐條計分，談哲戈的影子軍隊與議會，「不再有祕密」。

chunk（`plan 21`）：01＝p3–p39｜02＝p41–p107（單一段群，2586 字，不能再切）。本章沒有 HTML 裝置畫面、沒有 `>` 引言。

## 一、全章固定用詞（editor 一次只看一個 chunk，看不到別處的叫法；這些不要換）

| 原文 | 本章用法 | 出現位置／說明 |
|---|---|---|
| waiting for dinner to arrive | 等著晚餐送來 | p3（外送，p24–p25 機器人送到門口） |
| zipcoins | 吉普幣 | p6 |
| refugees | 難民 | p6 |
| reunify everyone | 讓大家團圓 | p8（反諷） |
| lawsuit against Divergent | 告分歧的官司 | p11（Divergent＝避險基金「分歧」） |
| original trial／appealed／appeal | 一審／上訴 | p13–p16 |
| a whole different group of judges got selected | 另外抽了一整組法官 | p13 |
| sortitioned in | 抽……進來 | p14（五個法官） |
| settle for like a quarter of the money | 拿個四分之一的錢和解 | p14 |
| Veridian common law rules | 維瑞迪亞的普通法規則 | p15 |
| bad faith／bad-faith appeal | 惡意／惡意上訴 | p15、p16 |
| frivolous appeals | 濫訴性的上訴 | p15 |
| Jump's internal monitoring systems | 跳躍公司內部監控系統 | p16 |
| genuine appeal | 正當的上訴 | p16 |
| defense statement | 答辯書 | p16 |
| hedge funds | 避險基金 | p17 |
| anonymized, randomly selected and split into two and a half groups | 匿名的、隨機抽選的，每一輪還分成兩組半 | p18（worldbuilding 法院） |
| threaten or bribe | 威脅或收買 | p18 |
| civics test | 公民考試（八十一分） | p20；p63 civics education→公民教育；p84 teach people Veridian civics→教維瑞迪亞的公民課（v2 加「課」：初譯「教維瑞迪亞的公民」會讀成教公民這些人） |
| your trip to Northglade | 北林之旅 | p22 |
| United Cities／Mabuli | 聯合城邦／馬布利 | p23 |
| Helisport game | 旋翼球（比賽） | p27、p96 |
| physics exam | 物理考試（九十五分） | p28 |
| mini rocket | 小火箭 | p30；p31 build a rocket→造火箭 |
| the Order／Order members | 掌舵會／掌舵會成員 | p35、p37、p78、p89 |
| manipulate | 操弄 | p37（兩次） |
| spying powers／spying ability／spying capabilities | 諜報能力 | p37、p66、p87 |
| hand device | 手持裝置 | p41 |
| hit her palm against her face for a fifth time | 第五次拍了自己的額頭 | p43（譯者筆記已定） |
| secret meetings | 祕密會議 | p43 |
| shadowy friend Mov | 神祕兮兮的朋友莫夫 | p43 |
| hoodwinked／hoodwinked *again* | 耍得團團轉／*再一次*被……騙了 | p44 |
| pretense／mask／ruse | 偽裝／面具／幌子 | p44、p45 |
| from Silverchat／working for Silverchat | 銀聊的人／替銀聊工作 | p44、p58、p65 |
| When you have eliminated the impossible… | 排除一切不可能之後，剩下的不管多麼難以置信，都一定是真相。 | p45（glossary 定譯，一字不改） |
| idiot／double idiot／incredibly naive idiot | 白痴／白痴中的白痴／天真到不行的白痴 | p50、p56、p58、p66（譯者筆記：賽菈真的在罵人，不軟化） |
| naive | 天真 | p58、p75、p99 |
| tracked down | 找到 | p62–p64 |
| rubric for data retention in environmental sensors | 環境感測器資料保存的規準 | p62（ch20 同） |
| privacy preservation | 隱私保護 | p62 |
| rubric for education | 教育方面的規準 | p63 |
| incentives for private schools to have proper Veridian civics education | 對私立學校好好上維瑞迪亞公民教育的獎勵 | p63 |
| social media openness and interoperability | 社群媒體開放性與互通性 | p64、p85 |
| corrupt Silverchat | 腐化銀聊 | p65 |
| up-boost | 推送 | p65 |
| planted that seed | 布了那個局 | p66 |
| cover story | 掩護說詞 | p66 |
| unrestricted surveillance | 毫無限制的監控 | p68、p83 |
| anti-war | 反戰 | p68 |
| three Keeper groups, they don't talk to each other | 守律者小組有三個，彼此不交談 | p69、p85 |
| PREPONDERANCE OF EVIDENCE | 優勢證據（p70「重點是優勢證據！」、p80「優勢證據！」） | glossary：大寫用驚嘆號處理，不加字 |
| probability update formula | 機率更新公式 | p70（不補「貝氏定理」） |
| odds ratio／by a factor of two or three／eight to twenty seven | 勝算比／變成兩、三倍／八倍到二十七倍 | p70 |
| propagandists／intellectuals | 宣傳家／知識分子 | p76 |
| discourse environment | 言論環境 | p76 |
| To turn bystanders into friends, and enemies into bystanders. | 把旁觀者變成朋友，把敵人變成旁觀者。 | p76 |
| the Arctic cause | 北極的陣營（join）／北極理念（a version of） | p77 |
| break down the Order／ineffective | 瓦解掌舵會／失靈 | p78 |
| pro-Arctic／pro-freedom／pro-peace | 親北極／支持自由／支持和平 | p78 |
| open source defense hardware | 開源國防硬體 | p82 |
| X points for … | 「自由加一分」「和平零分」「北極加一分」「銀聊零分」「扣一分」「扣半分」 | p82–p88（譯者筆記：句式統一，分數照原文，不替作者重算） |
| multiply this one by half | 這一條我們可以乘以一半 | p85 |
| blew his cover | 身分一被拆穿 | p86 |
| Sum it up | 加總起來 | p88 |
| discussion group | 討論小組 | p89 |
| The military, the parliament, media platforms | 軍方、議會、媒體平台 | p89 |
| the Order, the Courts, the graph funding | 掌舵會、法院、圖譜募資 | p89 |
| Privacy isn't a luxury, it's why we're still here. | 隱私不是奢侈品，它是我們到現在還撐得住的原因。 | p89（收束句） |
| I'm sorry, Seila. | 對不起，賽菈。 | p91 |
| not just your heart, but also your mind | 不只是你的心，還有你的頭腦 | p92 |
| enclave surrounded by Arctics | 被北極人包圍的飛地 | p95 |
| clean up your mess | 替你收拾爛攤子 | p95 |
| shadow military | 影子軍隊 | p96 |
| compromised | 被滲透 | p96 |
| Minpentai championship | 明盤台錦標賽 | p96 |
| secret army training ground | 祕密的軍隊訓練場 | p96 |
| drone war | 無人機戰爭 | p96 |
| Dzegojan | 哲戈人 | p99 |
| only half the battle | 只是成功了一半 | p99 |
| subcommittee | 委員會（QA：與 ch08「議會委員會」一致） | p99 |
| eleven to ten | 十一比十 | p99（譯者筆記：照原文，不改成 ch08 的 10 比 10） |
| magic foresight | 神奇的先見之明 | p99 |
| No more secrets, okay? | 不再有祕密了，好嗎？ | p105 |
| I promise. | 我保證。 | p104、p107（前後呼應） |

## 二、固定譯名

- 人物：Seila → 賽菈；Gladias → 格拉迪亞斯；Vil → 維爾；Daia → 黛亞；Lily → 莉莉；Zven → 茲文；Febric → 費布里克；Hreda → 赫蕾妲；
  Mov → 莫夫；Delwart → 德爾瓦特；Ephelion → 艾費里昂（Lord Ephelion → 艾費里昂勳爵，男性「他」）
- 稱謂：Uncle Vil → 維爾叔叔；Aunt Daia → 黛亞阿姨；Mom → 媽（莉莉對賽菈）
- 地名：Veridia → 維瑞迪亞；Meldan → 梅爾丹；Greater Plum Harbor → 大梅港；Northglade → 北林；United Cities → 聯合城邦；Mabuli → 馬布利；Dzego → 哲戈
- 組織：the Order → 掌舵會；Silverchat → 銀聊；Divergent → 分歧（避險基金）；Jump → 跳躍（公司）；Arctic(s) → 北極（北極人）；Courts → 法院；graph funding → 圖譜募資
- 制度：Keeper → 守律者（避免：守護者）；rubric → 規準（避免：評分標準）；bad faith → 惡意；common law → 普通法；defense statement → 答辯書；
  preponderance of evidence → 優勢證據；odds ratio → 勝算比；data retention → 資料保存；interoperability → 互通性；open source → 開源
- 物品：hand device → 手持裝置（避免：手機）；watch → 手錶；drone → 無人機；mini rocket → 小火箭
- 其他：Helisport → 旋翼球（避免：直升機運動）；Minpentai → 明盤台；enclave → 飛地

## 三、人物口吻與稱謂

- 稱謂：全章沒有「您」，不要加。
- 前半（晚餐）：共養家庭的家常對話，溫和、輕鬆；茲文、莉莉是興奮的孩子口吻（「超好玩的！」）。維爾談官司時務實、略帶疲憊。
- 後半：賽菈⚠真的在罵人（譯者筆記）：「白痴」「白痴中的白痴」「天真到不行的白痴」，生氣時叫全名「格拉迪亞斯」；p50「？！！！！」保留標點力道；
  推理時條理分明、冷硬，大寫處用驚嘆號。p95 長句是氣話加諷刺，保留怨氣。p99 結尾的挖苦（「我很懷疑」）保留。
- 格拉迪亞斯：被罵後話少、低聲認錯；p96–p97 講哲戈影子軍隊時回到理性說明。
- 說話者（**原文未標說話者的輪次一律照初譯，不補標籤**）：
  - p4 賽菈；p5（未標，問費布里克和赫蕾妲的消息）、p6（未標，回答：匯吉普幣、請數學老師）、p7（未標）、p8（未標）、p9（未標）——初譯沒點名，照初譯不點名；
    p10 賽菈嘆氣、p11（未標，問維爾官司）、p12 這次換維爾嘆氣；p13 維爾（未標）、p14（未標，問「可以一直上訴下去嗎」）、p15–p16 維爾（未標，兩段同一人）、
    p17（未標）、p18（未標，應為維爾）；
  - p20 莉莉、p21 黛亞、p22 維爾、p23 賽菈；p26 黛亞、p27 茲文、p28 茲文（未標，接續）、p29 賽菈、p30–p31 茲文（未標）、p32 維爾；
    p34 黛亞（未標）、p35 賽菈（未標）、p36 黛亞（未標）、p37 賽菈（未標）、p38 茲文。
  - p48 格拉迪亞斯（未標）、p50 賽菈、p52 格拉迪亞斯、p53 賽菈、p55 格拉迪亞斯、p56 賽菈、p57 格拉迪亞斯、p58 賽菈、p59 格拉迪亞斯、p60 賽菈這邊沉默、
    p61 格拉迪亞斯、p62–p64 賽菈（三段）、p65 格拉迪亞斯、p66 賽菈、p67 格拉迪亞斯、p68 賽菈、p69 格拉迪亞斯、p70 賽菈、p71 格拉迪亞斯、p72 賽菈、
    p73 格拉迪亞斯（「什麼？！」）、p74 格拉迪亞斯（未標，「這實在很難相信」，接續）、p75–p78 賽菈、p79 格拉迪亞斯、p80–p89 賽菈、
    p91–p92 格拉迪亞斯、p94 格拉迪亞斯（「那我們該怎麼辦？」）、p95 賽菈、p96–p97 格拉迪亞斯、p98–p99 賽菈、p100 格拉迪亞斯、p101 賽菈、p102 格拉迪亞斯、
    p103 賽菈、p104 格拉迪亞斯、p105 賽菈、p106–p107 格拉迪亞斯（最後一句也可能是賽菈；譯者筆記：不點名）。
  - 這些全部未標；原文分段就是說話輪次，**不要合段**，也不要替讀者補「格拉迪亞斯說」。

## 四、伏筆與資訊邊界（不可加暗示）

- p6：「幾天前」又匯了「一些」吉普幣當零用；「能怎麼過就怎麼過」；學校都滿了；難民裡「有一位」是數學老師，「非正式地」上課，對象是他們和「另外幾個」孩子。
- p8：「到了這個地步」「開始懷疑」——反諷的揣測，不改成斷言。
- p13：時間：幾個月前一審贏；一個月前上訴也贏；「就在幾天前」才知道要第二次上訴。
- p14：五個法官；「拿個四分之一的錢」（like a quarter）。
- p15：法官「可以」判定惡意；濫訴性的上訴「常常」會被這樣判（often）。
- p16：影像「當然」全都加密；「有個前員工」有權限交出去；「讓我們有些人看起來不太好」；影片「其實根本跟案子沒有關係」；「我希望」；「運氣好的話，應該」很快結案。
- p18：「要不是……我敢說」——條件句與推測。
- p25：機器人送來兩袋；五個人各自找到自己那一盒。
- p28：「一個月前」物理考九十五分。p30：「幾天前」老師「私下」帶他去車庫。p31：「說不定」有一天能去月球。
- p35：「基本上一直在想」（basically nonstop）；最近跟其他掌舵會成員見面。
- p37：「感覺」（it feels like）有很有組織的操弄；目標「看起來甚至」跟商業無關（don't even seem）。
- p38：茲文脫口而出，「像偵探小說裡破了案的主角」——原文的比喻，保留，不另加。p39：整桌安靜下來——不補誰的表情。
- p42：「隨時都該醒了」（any minute now）。
- p43：「第五次」；懊惱自己盲目；半年；她「什麼都沒問」，以為他在掌握之中——以及格拉迪亞斯搞不懂的，莫夫也搞得懂。
- p44：「從頭到尾」；原本的偽裝：只是個關心和平與自由的好心人；*再一次*（斜體）。
- p45：「不到一天」看穿，「才幾分鐘」就起疑；但沒有「夠快地」往下追；「想過可能是」北極人，但打消了；德爾瓦特的話「似乎」都不像（seemed）；福爾摩斯名言照定譯。
- p49：「一開始，她只想尖叫」——只是想，沒有真的尖叫；p51「一開始是一陣沉默」。
- p56：「幾乎立刻」看穿；拖著莫夫「自己去」查。
- p60：沉默是賽菈這邊，她在想下一句要說什麼。
- p63：*她*（斜體）。
- p64：「只是為了確認」；「完全沒去找過」那一組的任何一個人（neither Delwart nor anyone else）。
- p66：「他一定在某個時候察覺」——賽菈的推論（must have），保留推論語氣；「故意」；「讓掩護說詞更可信」。
- p69：「他隨時都可能已經滲透了另外兩組」（could always have）。
- p70：每項證據「也許只能」讓勝算比變兩、三倍（might only）；三個「獨立的」因素；八倍到二十七倍。
- p77：「某個版本的」北極理念；維瑞迪亞「有些」聰明、但病態又扭曲的人。
- p78：*能*（斜體）；「有時候……有時候……有時候別的什麼」，看規準和對象而定。
- p82–p88：逐條分數與加總照原文；原文加總與逐條不完全相符（譯者筆記、QA 已定：照原文，不修正、不加註）。
  p84 德爾瓦特的引語「人們應該自己看到維瑞迪亞有多好，自然學會愛它」保留『』。p86「兩種都有可能。所以每一種可能都加一分。」
  p87「超越任何一家企業，更遠遠超過什麼理想主義者組成的非營利團體」。p88「我甚至會把……乘以二」。
- p89：「他和他的同夥長驅直入」；「唯一攻不破的那幾道門，是他找不到鑰匙的那幾道」——原文的門／鑰匙意象，保留，不另加比喻。
- p90：「有好一會兒」（for a few moments），格拉迪亞斯沒說話。
- p95：「我希望」德爾瓦特錯了；兩件事：你在哲戈不是沒用的人、能拿出了不起的成果；同時賽菈在哭、還要收拾爛攤子。
- p96：「我想」；「或者說」影子軍隊；官方軍隊跟我們的「一樣」被滲透，政府其他部分「也一樣」；「基本上」；「一種」祕密的軍隊訓練場；「一直以來都押注」無人機戰爭——「比起旋翼球之類的東西，更像明盤台」。
- p97：「盡力說服」；我們在「可能」威脅到他們的科技與產業上領先（初譯「威脅到北極」，原文是 threat to them——指北極；可以保留），國防上「幾乎完全沒有思考」；先來這裡幫我們。
- p99：「勉強」十一比十；「明明沒有任何正當理由」；「除非……我很懷疑」。
