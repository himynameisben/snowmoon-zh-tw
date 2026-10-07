# 第 28 章 bible 摘錄（第二輪文學編輯用）

主 Agent 依 WORKFLOW「開始一章前」第 5 步建立；每個 chunk 的資料包都附上這份（`literary_edit.py packet --bible`）。
權威來源仍是 glossary／characters／worldbuilding；這裡只是本章會用到的部分，加上本章初譯已定的用詞。
段號為原文段號（`literary_edit.py plan 28` 的 pNNN；與 `translation/notes/chapter-28.md` 的段號相同）。

章節結構：p2 dateline（維瑞迪亞，梅爾丹 · 霜季 15 日）｜p3–p52 會議室：韋爾多帶來將軍雷克托，鄧坦承營救是昆高派做的，雷克托反駁「接管軍隊」，
白提出由雷克托出面接掌，穆提供過時的漏洞攻擊與收賄將軍的證據｜p53 分隔｜p54–p89 賽菈房間：茲文報告莉莉在公民課上用旋翼球計分反駁老師、被關禁閉、
想回家；格拉迪亞斯罵老師、賽菈制止；澤當莉莉的榜樣｜p90 scene-break dateline（霜季 18 日）｜p91–p100 格拉迪亞斯轉述雷克托在祕密會議中成為最高將領。

chunk（`plan 28`）：01＝p3–p52｜02＝p54–p89｜03＝p91–p100。本章沒有裝置畫面。

## 一、全章固定用詞（editor 一次只看一個 chunk，看不到別處的叫法；這些不要換）

| 原文 | 本章用法 | 說明 |
|---|---|---|
| conference room | 會議室 | p3 |
| the door buzz | 門口傳來嗡嗡聲 | p4（呼應 ch27） |
| One of the generals | 一位將軍 | p8 |
| ran an analysis through Emerald | 請翡翠做了一份分析 | p8 |
| the ongoing case | 那件進行中的案子 | p10；後文 legal case／court case→官司 |
| Lektor | 雷克托 | |
| traditional Veridian military attire | 維瑞迪亞傳統軍裝 | p14 |
| fire high-ranking government officials | 開除政府高官 | p20（雷克托用語；fire the entire military leadership→開除整個軍方領導層） |
| madness | 簡直是瘋了 | p20 |
| competent military | 有能力的軍隊 | p20 |
| Silverchat polls | 銀聊民調 | p22 |
| the operation that rescued Tafindel | 營救塔芬德爾的那次行動 | p25 |
| Kungaupei | 昆高派 | |
| Freetown defense companies | 自由城的國防企業 | p27 |
| *here* | *在這裡* | p29 |
| Dozens of us | 幾十個 | p30 |
| High Council members | 最高議會的成員 | p30 |
| drone fleet | 無人機隊 | p33、p38 |
| take back Northshore | 奪回北岸省 | p33、p87 |
| *polite* | *禮貌* | p34 |
| desperate | 走投無路 | p34 |
| United Cities | 聯合城邦 | p34 |
| Messalia／Haragmir | 梅薩利亞／哈拉米爾 | p34 |
| take a stand. Together, now. | 我們必須表態。一起，就是現在。 | p34 |
| commandeer a military | 把一支軍隊徵用過去 | p35 |
| logistics | 後勤 | p35、p38 |
| Helisport copters | 旋翼球的旋翼機 | p35；*those*→*那些* |
| drone pilots／support staff | 無人機操作員／後勤人員 | p35 |
| fly on AI alone | 只能交給 AI 自己飛 | p35 |
| command structure | 指揮體系 | p36 |
| zero out the top three levels of the … hierarchy | 把……前三層階級全部清空 | p38、p42（zero out the military→把軍方清空） |
| top thousand Minpentai players | 排名前一千的明盤台選手 | p38 |
| *could*／*was*／*can* | *真能*／*到底*／*確實* | p38、p39、p42（斜體） |
| over three months to finalize | 三個多月才能定案 | p38 |
| step in and help／step up | 站出來幫忙／站出來 | p40、p43（兩處呼應） |
| irredeemable and talentless | 無可救藥、毫無人才 | p42 |
| shift paradigms from peacetime to wartime | 從平時的思維轉換到戰時的思維 | p42 |
| bribed or blackmailed | 收買或勒索 | p42、p94、p96 |
| surveillance cameras that we backdoored | 我們植入後門的保全攝影機 | p42 |
| political persuasions | 政治立場 | p43 |
| take over and run things | 接掌、主持大局 | p43、p46 |
| inside your structure | 在你的體制裡面 | p43 |
| blow your cover | 讓你們曝光 | p46 |
| closed door session | 閉門會議 | p46 |
| exploits against Arctic drones | 針對北極無人機的漏洞攻擊（第二次起可簡稱「漏洞」） | p48、p95 |
| *better* | *更好* | p48 |
| keep their guard down | 繼續鬆懈 | p48 |
| damaged drone … recover from Northshore two months ago | 兩個月前從北岸省回收的那架受損無人機 | p48、p49 |
| take the credit | 功勞你們可以拿去 | p48 |
| taking bribes | 收賄 | p50、p94 |
| Arctic spy | 北極間諜 | p50、p94 |
| wrong kind of booth | 挑錯了包廂 | p51 |
| dump of the info | 資料整包 | p52 |
| *your* army／*your* plan | *你的*軍隊、*你的*計畫 | p52 |
| Mom／Mom, Dad | 媽／媽、爸 | p56、p83 |
| Arctic civics class | 北極的公民課 | p64 |
| instructor | 老師 | p64–p66、p70 |
| Helisport／scoring rules | 旋翼球／計分規則 | p64、p65 |
| adding／multiply | 相加／相乘 | p65（ch16 用語，不可換） |
| type of ball | 種球 | p65 |
| detention | 關禁閉 | p68 |
| lame and stupid／lame | 又遜又蠢／很遜 | p69、p88 |
| striving for the best | 追求最好 | p69 |
| total loser／a loser that happened to be born on a winning team | 徹頭徹尾的魯蛇／剛好生在贏家隊伍裡的魯蛇 | p70、p71（保留尖酸，不軟化） |
| a pathetic shell | 一副可悲的空殼 | p71 |
| Glad | 格拉德 | p72、p74、p88（賽菈的暱稱） |
| self-righteous | 理直氣壯 | p73 |
| a little bit Arctic | 有一點點北極 | p75、p77 |
| surveiling everything | 什麼都監視 | p77 |
| unrestricted camera surveillance | 毫無限制地用攝影機監視 | p79 |
| get the good without the bad | 只要好處、不要壞處 | p79 |
| mentor／role model／real winner | 導師／好榜樣／真正的贏家 | p82 |
| lord over others | 騎在別人頭上 | p82 |
| boarding school | 寄宿學校 | p85 |
| special closed session | 特別祕密會議 | p93 |
| reforming the military leadership | 改組軍方領導層 | p94 |
| detractors | 反對者 | p94 |
| top general／head general | 最高將領 | p94、p96 |
| flipped over his cards | 把底牌翻開 | p94 |
| dependence on AI | 對 AI 的依賴 | p95 |
| explained it away | 搪塞過去 | p95 |
| path of least resistance | 阻力最小的一條路 | p96 |
| preserving continuity | 保住了延續性 | p97 |
| forecaster bots | 預測 AI | p97（不可譯「機器人」） |
| The battle for the halls of Meldan… The battle of Northshore… | 梅爾丹的廳堂之戰結束了。北岸省之戰即將開始。 | p100 |

## 二、固定譯名

- 人物：Zei → 澤；Den → 鄧；Bai → 白；Mu → 穆；Verdow → 韋爾多；Lektor → 雷克托；Gladias → 格拉迪亞斯（Glad → 格拉德）；Seila → 賽菈；Zven → 茲文；
  Lily → 莉莉；Febric → 費布里克；Tafindel → 塔芬德爾
- 地名：Meldan → 梅爾丹；Veridia → 維瑞迪亞；Northshore → 北岸省；Redshire → 紅郡；Freetown → 自由城；United Cities → 聯合城邦；Messalia → 梅薩利亞；Haragmir → 哈拉米爾
- 組織：Arctic Empire → 北極帝國；Arctics → 北極（初譯常用「北極」指北極人）／北極人；Kungaupei → 昆高派；High Council → 最高議會；parliament → 議會；senators → 參議員
- 其他：Emerald → 翡翠；Silverchat → 銀聊；Helisport → 旋翼球；Minpentai → 明盤台；neck band → 頸帶；hand device → 手持裝置
- 日期：Frostime → 霜季

## 三、人物口吻與稱謂

- 雷克托：中年將軍，直率（「聽好」「你們到底在想什麼」），對昆高派一行人用「你們」，不用「您」。
- 鄧：坦白、沉重（p34 走投無路、必須表態）。
- 白：p37 起主導談話，說理冷靜、有策略；p52 收尾。
- 穆：p48 務實，p51 咧嘴一笑的俏皮。
- 茲文：小孩子的直白與興奮（「是我啦，媽！」）。
- 格拉迪亞斯：p70–p75 全書少見的尖酸、越說越理直氣壯（人物卡：不可軟化）。
- 賽菈：叫他「格拉德」制止；p77–p79 讓步但保留原則。
- 全章沒有「您」。
- 說話者（**原文未標說話者的輪次一律照初譯，不補標籤**）：
  - chunk 01：p6 韋爾多；p7 澤；p8 韋爾多；p9（未標）；p10 韋爾多；p11 白；p12 韋爾多；p13（未標）；p15 雷克托；p17 鄧；p19–p23 雷克托；p25 鄧；p26 雷克托；p27 鄧；
    p29 雷克托；p30 鄧；p31 雷克托；p33 雷克托；p34（未標，鄧）；p35–p36（未標，雷克托）；p38 白；p39 雷克托；p40 白；p42–p43（未標，白）；p46 雷克托；p48 穆；
    p50（未標）；p51 穆；p52 白。
  - chunk 02：p55 賽菈；p56 茲文；p57 賽菈；p59、p61、p63（未標）；p60、p62、p64–p69 茲文；p70–p71 格拉迪亞斯；p72 賽菈；p73 格拉迪亞斯；p74 賽菈；p75 格拉迪亞斯；
    p77 賽菈；p78（未標）；p79–p82（未標，照初譯不點名）；p83 茲文；p84（未標）；p85 茲文；p87 格拉迪亞斯；p88 賽菈。
  - chunk 03：p91 格拉迪亞斯；p92 賽菈；p93–p96（格拉迪亞斯）；p97–p100（未標，照初譯不點名）。
  - 不同說話者不要合段；同一人連續的段落照原文分段。

## 四、伏筆與資訊邊界（不可加暗示）

- p4：「立刻」停下談話。
- p8：「其實是」少數敬重的之一；得到的評價「全都非常正面」。
- p14：襯衫「看起來幾乎是精心設計過的」（seemed almost perfectly designed）：既像傳統軍裝、又舒服到可以日常穿。
- p16：澤「正要」開口，鄧示意他別出聲。
- p20：「維瑞迪亞有史以來第一次」；「看起來簡直是瘋了」。
- p21：「頓了一下」。p22「不過……」停頓保留。
- p26：「一直都在」拼湊。
- p28：嘴巴都張大了。
- p32：「沉默了一下」。
- p34：「顯然」打算先對付你們；你們技術比較先進、我們防禦準備比較周全；「一年內——也許更快——徹底」；一個一個拿下聯合城邦→南下清掉梅薩利亞和哈拉米爾「或者為了省時間，乾脆直接轟炸」；
  「就只剩他們和我們」；「憑我們現有的東西，我們守得很好，但說真的」非常依賴你們。
- p35：「多年來」；「瞭若指掌」；「上千名」操作員、「數千名」後勤人員；「幾十個」顧問；「幾乎每一架」；「一有機會就會」被騙。
- p36：「徹底失敗」；「好多年」。
- p37：白「覺得」話題越來越偏、看準機會。
- p38：「就算我們*真能*……也不知怎麼地全都自己解決了」——假設；「三個多月」；「從來都不是」。
- p41：雷克托沒有回答（silence）。
- p42：「從來不會像社群媒體上說的那樣」；「*確實*可能」；「最艱難」；「偏偏就在這個時候」；「很多將軍大概都」（probably）；「已經抓到好幾個」。
- p43：「我覺得」；「一律都很高」；「應該考慮」。
- p44：「立刻」點頭；「並不在他們原本的計畫裡」，但「都看得出來」這正是應該改走的。
- p45：「想了一會兒」。
- p46：「每個人都覺得那只是幻想」；「如果議會真的像你們說的那麼腐敗」。
- p48：「已經過時了」；「其實*更好*」；「效果會非常好」。
- p49：雷克托的內心句（又愣愣地盯著；連那架受損的無人機都知道？怎麼滲透得這麼……徹底？如果昆高派做得到，那北極……）——刪節號保留，不補完。
- p50：「確鑿的證據」。p51「咧嘴一笑」。
- p58：「跑過去」開門；茲文「衝了進來」、「興奮地」跳上沙發。
- p62：「開始覺得」自己「現在」想回來了。
- p64：老師說計分規則很蠢、是維瑞迪亞人「喜歡把事情搞得太複雜」的例子。
- p65：莉莉「一直」透過頸帶跟茲文講話；把費布里克也拉進通話；論證：相加→「幾乎永遠」只專攻一種球最好；相乘→一種球的得分隨另一種球「已經拿到的分數」一起變多→平衡才合理。
- p66：老師兩手一攤；「現實生活裡只專注一件事才會贏」；北極懂、維瑞迪亞不懂，所以北極才會贏。
- p67：「幾乎每天整天」；「只有在不工作的時候」才能享受房子；「一模一樣的數學」。
- p69：「嘴上說」追求最好，「其實只在乎」自己的權威。
- p70：「有些」北極人很聰明；技術「確實」做得非常好；老師「聽起來」就是個魯蛇。
- p71：「就是會這樣」；整個自我認同押在隊伍上；全盤接受；你屬於哪一隊代表你有多少價值；「根本沒發現」；「一點也沒有」。
- p73：「語氣越來越理直氣壯」；在掙扎或不懂→幫他、對他好；拿「根本不配擁有」的權威往別人頭上猛敲→直接打回去。
- p75：「有時候」；「至少有一點點」。
- p77：「大概也能理解」；「靠的正是」北極那一套。p78「我想算吧」。
- p79：「我相信」；「差一點」把我們擊垮；澤「早就知道」有什麼更好的辦法。
- p82：「可能是」最完美的導師。
- p85：北岸省邊界「是開放的」，但寄宿學校不讓她走。
- p86：哀嘆了一聲（groaned）。p87「至少」（if nothing else）；「三個孩子就都能回來」。
- p88：她「現在知道」北極很遜、想回家；「在我們把她接回來之前」；「不會害死她的」建議。
- p89：「無可奈何地」咕噥，算是接受。
- p93：「昨天」召開；韋爾多也在場。
- p94：「採用了白給的一些建議」；先讓反對者「自己」替現任最高將領辯護，「再」提名另一位（「萬一非換人不可」）；「然後」才把底牌翻開：最高將領「一直定期」和某人見面，那人「後來證實」是北極間諜；替代人選「正遭到勒索」。
- p95：利用北極對 AI 的依賴；「其中包括」昆高派在紅郡拍到的畫面；「解釋說」是紅郡認識的間諜傳給他的。
- p96：「比他和白預料的容易得多」；懶散、疲憊的參議員→阻力最小（官司「會立刻結束」）；被勒索的參議員「只需要一個藉口」——論點加上官司「遲早可能」挖到自己身上；「所以現在」雷克托是最高將領。
- p97：「聽起來是」最完美的結局；「大部分」原本的體制還在；「正是」預測 AI 想要的。
