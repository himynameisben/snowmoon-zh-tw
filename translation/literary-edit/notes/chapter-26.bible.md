# 第 26 章 bible 摘錄（第二輪文學編輯用）

主 Agent 依 WORKFLOW「開始一章前」第 5 步建立；每個 chunk 的資料包都附上這份（`literary_edit.py packet --bible`）。
權威來源仍是 glossary／characters／worldbuilding；這裡只是本章會用到的部分，加上本章初譯已定的用詞。
段號為原文段號（`literary_edit.py plan 26` 的 pNNN；與 `translation/notes/chapter-26.md` 的段號相同）。

章節結構：p2 dateline（維瑞迪亞，霜季 5 日）｜p3–p42 飛機上：哲戈語廣播（`>` 引言，保留拼音）與格拉迪亞斯的逐句口譯、澤的更正、
Pafogai＝「十四石」｜p43 分隔｜p44–p77 下機、通關閘門、黑色專車上見韋爾多：找到莉莉、北極開放北岸省、診所、「綜合」、旅館裡賽菈出現｜
p78 scene-break dateline（維瑞迪亞，梅爾丹 · 霜季 6 日）｜p79–p151 澤、鄧、穆遠端指揮營救塔芬德爾（p103、p115、p129、p139 是 SVG 戰況畫面）｜
p152 分隔｜p153–p160 事後檢討：澤自責、鄧「歡迎來到真正的戰爭」、穆說明做法｜p161 分隔｜p162–p195 格拉迪亞斯在包廂遊說五名法官，失敗。

chunk（`plan 26`）：01＝p3–p42（廣播引言之間的短段群，27 個單位）｜02＝p44–p77｜03＝p79–p102、p104–p114、p116–p128｜04＝p130–p138、p140–p151｜05＝p153–p160｜06＝p162–p195。

### 錨點（不送 editor，一字不動）

- `>` 引言：p5、p9、p11、p13、p16、p18、p20、p22、p24、p26、p28、p31、p33 是哲戈語廣播的羅馬拼音，**原樣保留，不翻譯、不改大小寫**（這些單位若在 draft 裡，輸出時照抄）。
- SVG 戰況畫面（p103、p115、p129、p139）：只有圓點、虛線、✓ 與 x 標記，沒有文字。散文不要替它們補解釋。

## 一、全章固定用詞（editor 一次只看一個 chunk，看不到別處的叫法；這些不要換）

### 飛機與口譯（chunk 01）

| 原文 | 本章用法 | 說明 |
|---|---|---|
| small enclosed cabin | 封閉的小包廂 | p3；p47 的 cabin 也是「包廂」 |
| announcement alarm | 廣播提示音 | p4 |
| trance-like state | 出神的狀態 | p4 |
| Meldan | 梅爾丹（the city of Meldan→梅爾丹市） | |
| Gelebor mountains | 葛勒博山脈 | |
| a row of small mountains | 一排小山 | p3 |
| **格拉迪亞斯的口譯（p8、p10、p12、p14、p17、p19、p21、p23、p25、p27、p29、p32、p34、p38）** | 照初譯保留學習者的生硬：「飛的機器」「看外面美麗的好時間」「美麗綠色植物大地之布」「首都城市」「健康保護」「很多去看的地方」「走路爬上去是快樂和美麗的」 | **這些是刻意的直譯腔，是情節（他在練口譯）。不要潤成通順中文，也不要改字面**；只有引號外的敘事可以改寫 |
| Landscape of green plants／Tourist attractions | 「綠色植物的景觀。」／「觀光景點。」 | 澤的更正，用正常中文 |
| 74,000 | 74,000 | p10，時刻，照原文數字 |
| 1.1 million | 110 萬 | p21 |
| Kalimar district | 卡利馬區 | |
| Well done. Only two months… | 翻得好。才兩個月，你就差不多是個本地人了。 | p35 |
| ci jie fe lo cin pin fe di pa fo gai du | 照抄拼音 | p37 |
| I enjoyed Pafogai Du very much. | 我非常享受帕佛蓋都。 | p38，略帶直譯味，保留 |
| Pafogai means 'fourteen stone' | Pafogai 的意思是『十四石』 | p41，保留英文拼寫 Pafogai |
| Think of the periodic table. | 想想週期表。 | p42，不補「矽」 |

### 下機與專車（chunk 02）

| 原文 | 本章用法 | 說明 |
|---|---|---|
| autobuses and cars | 自駕巴士和車子 | p44 |
| for our privacy | 為了隱私 | p45 |
| carry-on bags | 隨身行李 | p47 |
| passage gates | 通行閘門 | p48 |
| green circle | 綠色圓圈 | p49 |
| A few ticks later | 幾拍之後 | p49（tick→拍，不可寫「刻」「秒」） |
| Welcome to Veridia. | 歡迎來到維瑞迪亞。 | p49 |
| large black cars | 大型黑色專車 | p50 |
| boarding school | 寄宿學校 | p64 |
| GPH | 大梅港（北林那座；不保留縮寫） | p64、p66 |
| Arctic-occupied territory | 北極佔領區 | p63 |
| security cameras | 保全攝影機 | p64 |
| Dzegojan | 哲戈人 | p64 |
| clinics／longevity／performance enhancement | 診所／延長壽命／強化能力 | p67 |
| shiny technology | 亮晶晶的科技 | p67（保留揶揄） |
| Arctic Empire | 北極帝國 | |
| Manipulating…is just convincing | 操弄……只是說服 | p69（呼應 ch25「說服。」） |
| hidden cost | 隱藏的代價 | p70 |
| proprietary Arctic medicine | 北極的專利藥物 | p70 |
| slave／slavery | 奴隸／奴役 | p70 |
| synthesis | 綜合之道 | p71 |
| north star | 北極星 | p71（保留原文字面，與「北極帝國」相撞是原文的趣味） |
| social fabric | 社會紐帶 | p71 |
| breathing room | 喘息的空間 | p72 |
| learn from the outside | 向外學習 | p73 |
| government-run hotel | 政府經營的旅館 | p74 |
| a big day | 一場硬仗 | p75 |
| big plans | 大計畫 | p75 |
| Veridia ba fau gie | Veridia ba fau gie | p75，保留拼音，不加釋義 |

### 營救行動（chunk 03、04、05）

| 原文 | 本章用法 | 說明 |
|---|---|---|
| console | 控制台 | p79、p154 |
| anti-cheating detection drones | 偵測作弊的無人機 | p79 |
| earpiece／glasses／microphone／headset | 耳機／眼鏡／麥克風／頭戴裝置 | |
| soundproofing | 隔音 | p86 |
| the whole operation | 整個行動 | p87 |
| presidential residence | 總統官邸 | |
| target | 目標人物 | 全章 |
| our man on the inside | 內應 | p88、p132 |
| rope | 繩子 | |
| balcony | 陽台 | |
| mainline plan | 主計畫 | glossary |
| contingency plans | 應變計畫 | glossary |
| backup plan | 備案 | p90 |
| combat drones | 戰鬥無人機 | p90 |
| backup drones | 備用無人機 | p90 |
| dangerous window | 危險的時間窗口 | p90 |
| Supervising | 監督 | p92、p94、p96 |
| surveillance（Mu 負責的） | 偵察 | p96「監督偵察」 |
| Arctic surveillance was more powerful | 北極的偵察能力 | p118 |
| extent of Arctic surveillance | 北極監控的程度 | p156（初譯兩處用字不同，各自照初譯） |
| Privacy precautions. | 隱私上的預防措施。 | p98 |
| Fi le gei tau fa／mu gu gei tau fa | 照抄拼音（初譯「Fi le gei tau fa」「mu gu gei tau fa」） | p101、p107 |
| Battle starts in fifty ticks. | 五十拍後開戰。 | p107 |
| parliament building | 議會大廈 | p104，原文如此（實際目標是總統官邸），照原文 |
| dark yellow triangle／brighter yellow checkmark | 暗黃色三角形／比較亮的黃色勾勾 | p105、p109 |
| checkmark | 勾勾 | 全章 |
| video feed／visual feed／raw visual feed／the visual | 影像畫面／影像畫面／原始影像／影像 | |
| display map | 地圖畫面 | p119 |
| Evasive action, return fire at hostiles | 閃避，對敵機還擊 | p117 |
| play dead | 裝死 | p117、p123 |
| evasion tricks | 閃避招數 | p120 |
| Kungaupei | 昆高派 | |
| credibility | 信譽 | p120 |
| a trick up my sleeve | 我還有一招藏在袖子裡 | p122 |
| crash at these coordinates | 在這個座標撞一下 | p126 |
| thermal cloaks | 熱偽裝斗篷 | p132（不是保暖斗篷） |
| Good job Den | 幹得好，鄧 | p132 |
| against all odds | 在所有不利的情況下 | p133 |
| NOT the road closest to them | 可不是離他們最近的那條 | p137（強調用語氣，不加粗體） |
| sea drone／seaborne drone | 海上無人機 | |
| Pickup successful. | 接送成功。 | p142 |
| Dolinar | 多利納 | p144 |
| shopping complex | 購物中心 | p144 |
| manhunt | 搜捕 | p144 |
| Arturia | 亞圖利亞 | p151 |
| real life warfare | 真正的戰爭 | p154 |
| think completely outside the box | 完全跳出框框思考（後兩個 outside the box 都用「跳出框框」，保留排比） | p154 |
| glider structure | 滑翔機結構 | p154（明盤台術語） |
| admin passwords | 管理員密碼 | p156 |
| commandeer a few dozen automated cars | 接管了幾十輛自駕車 | p156 |
| decoys | 誘餌 | p156 |
| the planes stopped and restarted | 飛機……停下又重新起飛 | p156，照原文（指涉不明，不改成無人機） |
| defense companies | 國防企業 | p160 |
| take its share of the credit | 領受自己那一份功勞 | p160 |
| the defense that it deserves | 它應得的國防 | p160 |

### 法官（chunk 06）

| 原文 | 本章用法 | 說明 |
|---|---|---|
| booth | 包廂 | p162、p164、p195 |
| backdoored by Dzego | 被哲戈植入後門 | p162 |
| surveillance cameras | 監視攝影機 | p162 |
| the first judge／another judge／a third judge | 第一位法官／另一位法官／第三位法官 | |
| open a case against | 提起訴訟 | p165 |
| Veridian military leadership | 維瑞迪亞軍方領導層 | |
| the fourteenth Ground Law／Twenty-first Ground Law | 第十四條基本法／第二十一條基本法 | glossary |
| fired／replace | 撤換／換掉 | |
| That's crazy／insane／crazy scheme | 這太瘋狂了／這太荒唐了／瘋狂的計畫 | |
| timeless principles | 永恆的原則 | p168 |
| daily news | 每日新聞 | p168 |
| Veridia is a democracy | 維瑞迪亞是民主國家 | p173、p190（瑟勒特重複兩次，保留重複） |
| corrupt | 腐敗 | p174、p175 |
| Arctic-engineered bubble of propaganda | 北極人打造的宣傳泡泡 | p174 |
| honestly, in good faith and without undue influence | 誠實、善意、不受不當影響地 | p176 |
| report and resign | 通報並辭職 | p176 |
| undue influence | 不當影響 | glossary |
| blockading | 封鎖 | p182 |
| co-parents | 共養父母 | p185 |
| misaligned | 不一致／偏向了 | p185 |
| compacency（complacency 的筆誤） | 安於現狀 | p185 |
| precedents | 前例 | p186（glossary：避免「先例」） |
| Plaintiffs／stake in the outcome | 原告／和判決結果有利害關係 | p188 |
| *standing* | *當事人適格* | p188，斜體保留 |
| Dzego-man whiz kids／a prince | 哲戈來的天才小鬼／一個王子 | p190，保留輕蔑 |
| stomp our feet over our democracy | 把我們的民主踩在腳下 | p190 |
| a minimum of thirty days | 最少要三十天 | p191 |
| appeal／third round | 上訴／第三輪 | p191 |
| chaos | 混亂 | p191 |
| sample of judges | 這一批抽出來的法官 | p194（維瑞迪亞法官是抽出來的） |

## 二、固定譯名

- 人物：Gladias → 格拉迪亞斯；Zei → 澤；Bai → 白；Den → 鄧；Mu → 穆；Verdow → 韋爾多（Senator Verdow → 韋爾多參議員）；Seila → 賽菈；
  Lily → 莉莉；Zven → 茲文；Febric → 費布里克；Hreda → 赫蕾妲；Ephelion → 艾費里昂；Sylka → 希爾卡；Tafindel → 塔芬德爾；Mov → 莫夫；
  Caeron → 凱隆；Sewlert／Selwert → 瑟勒特（同一人）；Zevin → 齊文
- 地名：Veridia → 維瑞迪亞；Meldan → 梅爾丹；Pafogai Du → 帕佛蓋都；Gelebor → 葛勒博；Kalimar → 卡利馬；Northglade → 北林；Northshore → 北岸省；
  GPH → 大梅港；Redshire → 紅郡；Dolinar → 多利納；Arturia → 亞圖利亞；Freetown → 自由城；Dzego → 哲戈
- 組織：Arctic Empire → 北極帝國；Arctics → 北極人；Kungaupei → 昆高派；parliament → 議會；court → 法院
- 單位：tick → 拍（避免：刻）；minute → 分鐘
- 日期：Frostime → 霜季

## 三、人物口吻與稱謂

- 澤對韋爾多：p53「很榮幸見到您，參議員。」用「您」（稱謂表）。其餘人之間都用「你／你們」，不要加「您」。
- 韋爾多：熱情（「歡迎回家，格拉迪亞斯！」），說理時沉穩、長段。
- 澤：p35 調侃格拉迪亞斯；p83 調皮跺腳；作戰時簡短、命令句；事後自責（p153）。
- 鄧：作戰指揮冷靜；p154 用明盤台比喻教訓澤。
- 穆：p96「當然在」，自信、俐落；p156 解釋做法時承認自己也低估了北極監控。
- 法官：凱隆最強硬（性別未明，譯文能省則省）；瑟勒特以「民主國家」反駁；齊文同情但不敢表態。
- 說話者（**原文未標說話者的輪次一律照初譯，不補標籤**）：
  - chunk 01：p6 澤；p7–p8 格拉迪亞斯；廣播之間的口譯都是格拉迪亞斯；p15「綠色植物的景觀」澤；p30「觀光景點」（未標，澤）；p35 澤；p36–p37 澤；
    p38–p42 未標，照初譯不點名。
  - chunk 02：p45 鄧；p51 格拉迪亞斯；p52 韋爾多；p53 澤；p55 韋爾多；p56 白；p57 韋爾多；p59 韋爾多；p60 格拉迪亞斯；p61 韋爾多；p63–p64 韋爾多；
    p65 格拉迪亞斯；p66 韋爾多；p67–p73 未標，照初譯不點名、不補說話者；p75 韋爾多。
  - chunk 03–05：照初譯，未標的不點名。p92–p95「我負責什麼？」「你負責什麼？」未標，不點名。p158「But what matters is that we won.」未標（應是鄧），不點名。
  - chunk 06：p188–p189「這下你把法律搞錯了……」「而且沒錯，我有三個孩子在那裡。」是**格拉迪亞斯**說的（原告），譯文不點名；p190–p192 瑟勒特（p193 才點名）。
  - 不同說話者不要合段；同一人連續的段落照原文分段。

## 四、伏筆與資訊邊界（不可加暗示）

- p3：四人「靜靜」望著窗外；「大致平坦」；最顯眼的是一排小山，「再過去遠方」是梅爾丹市。
- p7：格拉迪亞斯想「趕在下一句開始前」聽懂並說出答案；「過了一會兒」；「脫口而出」。
- p15：澤「溫和地」更正。
- p36：澤「停了一下」，「慢慢地」說。
- p44：「十幾輛」（over a dozen）。
- p47：「大約十分鐘後」；門「自動」打開；「立刻」起身；其他包廂門「都已經」打開、空無一人；「許多」桌上、座位上。
- p48：狹窄的房間「看得出這裡其實也是」一輛自駕巴士的內部（clearly also）；兩道閘門擋在中間。
- p49：「幾乎同時」（almost in unison）。
- p52：神情和語氣比格拉迪亞斯「以往聽過的都要」溫暖；「馬上」看向他身旁。
- p54 澤「已經」聽到白和鄧的腳步聲。p58「幾乎立刻」感覺到車子加速。
- p61：「看來」（Looks like）我們知道莉莉在哪了。
- p63：賽菈「拚了命」（pushed really hard）；茲文「一直」跟莉莉保持聯絡；她「向他承認了」。
- p64：「你很聰明地建議」哲戈人駭進去；「幾天後」；「某種」寄宿學校；「大約一公里」。
- p65：「至少」×2；「會很困難」。
- p66：「如果你真的想去，現在甚至可以去北林」；「不過」大梅港的門「還是」關著。
- p67：北極人「最近」開始允許雙向通訊、往來；「一些」最先進的療程；「看來」他們決定……「自願」加入。
- p70：「肯定」（definitely）；希爾卡「會」不高興；艾費里昂「會說」——假設語氣保留；「不只對一個人成立，對一個文明也一樣」。
- p71：「可以是」健康的（can be）；「不能只是」維持現狀。
- p74：車子「慢慢」停下；「看起來像是」政府經營的旅館。
- p76：「幾乎是馬上」；「房間遠處的角落」；張開雙臂奔過來。
- p79：「出奇地像」；「他看得出的」主要差別。
- p82：「我想」我就在你正下方的房間。
- p90：「甚至」其他戰鬥無人機「也可能」把目標人物接回來，「只是」設計不太適合；「唯一」危險的時間窗口。
- p105：二十拍後；「完全照著時間表」。p106 又過了三十拍。p107：「某種意義上」戰鬥早就開始了；「他想」真正的挑戰會從那時開始。p108 又過了二十拍。
- p118：「他這才發現」北極的偵察能力比他想的還要強。
- p120：「看來」任務就要失敗了——昆高派的信譽「可能」也會跟著賠進去（perhaps）。
- p123：「不到十拍」；「四架倖存且功能完好」；另一架受損的「已經」在地面「超過半分鐘」。
- p124：「搞不清楚」對手在哪裡（confused）。
- p127：「四拍後」。p128：「十拍後」兩個勾勾。
- p130：澤「一頭霧水」，但「立刻」做了「唯一合理的事」。
- p133：「不知怎麼地」，「在所有不利的情況下」，「好像」辦到了？——問號保留。
- p137：「很快」；「運氣好的話」；「幾十公里外」。
- p140：對自己「深深失望」。
- p144：「希望」搜捕能拖得越久越好。
- p149：「緩慢而吃力地」（slow grinding）向西前進。
- p153：「要不是穆用一個全新的計畫救了我們」；「大概」（probably）其他一切也都會失敗。
- p154：「有時候」，「唯一的」勝利方法。
- p156：「很多人默默支持」；「還沒完全」轉到北極控制；「目前」還有可能駭進「一些」東西；「先」控制路燈，「再」接管；誘餌「其實有好幾個」；「我跟你一樣」低估了。
- p160：「目前，他們以為這只是」自由城的國防企業；「然後再看看」維瑞迪亞人願不願意。
- p162：「被哲戈植入後門的監視攝影機幫了大忙」（with significant help）。
- p166：「我們甚至不知道要拿什麼標準來比較——」（話被打斷，破折號保留）。
- p170：「幾乎立刻」。
- p182：「唯一還在」封鎖。
- p185：數字鏈：百分之六／每人約十個親近家人（六類列舉）／五人共五十個／統計上應有三個／一個都沒有→感受不到／利益不一致／偏向安於現狀／難道不也是不當影響？——每一環都要在。
- p191：「最少」三十天；「這還是在法官不認為需要更久的情況下」；可以上訴「好幾次」；上訴「可以比較短，但只有從第三輪開始」；「好幾個月」。
- p193：三位跟著點頭；齊文「似乎」同情得多——「無疑有很大一部分是因為」他也有兒子困在北林——但「似乎」不太敢表達。
- p194：「幾乎可以肯定」也會「相當」有敵意。
- p195：「慢慢」走了出去。
