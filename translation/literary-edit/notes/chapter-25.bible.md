# 第 25 章 bible 摘錄（第二輪文學編輯用）

主 Agent 依 WORKFLOW「開始一章前」第 5 步建立；每個 chunk 的資料包都附上這份（`literary_edit.py packet --bible`）。
權威來源仍是 glossary／characters／worldbuilding；這裡只是本章會用到的部分，加上本章初譯已定的用詞。
段號為原文段號（`literary_edit.py plan 25` 的 pNNN；與 `translation/notes/chapter-25.md` 的段號相同）。

章節結構：p2 dateline（帕佛蓋都，霜季 1 日）｜p3–p95 封閉房間：澤和格拉迪亞斯在桌面螢幕上玩取圓圈的遊戲（Nim，原文沒有名字，不補）、
XOR 和的必勝法、後手有利、熵與不可逆、轉到「為維瑞迪亞而戰」是先手還是後手有利、說服法院、說真話的優勢｜
p96 分隔｜p97–p122 打給韋爾多參議員（p98 通話畫面）：澤報告攝影機後門、韋爾多的瘋狂主意（依第十四條基本法撤換軍方與議會）、法律與彈性、怎麼說服法官。

chunk（`plan 25`）：01＝p3、p5–p9、p11、p13、p15、p17–p18、p20–p34、p36–p40、p42–p46（盤面畫面之間的短段，9 個單位）｜02＝p48–p95｜03＝p97、p99–p122。

### HTML 區塊（不送 editor，一字不動）

- p4、p10、p12、p14、p16、p19：SVG 盤面（四個虛線方框，藍色圓圈）；p35、p41、p47：二進位方格（0011／0100／1010／1101 → 0010… → …1100）。圖內沒有文字。
- p98：撥出通話（訊息／收件者／時間：［請求通話］→ 韋爾多參議員，78145）。散文不要替它們補解釋。

### 遊戲與數學（技術說明，一項都不能少）

- 規則：先走的人挑一堆，從那堆拿走「至少一個」圓圈；可以拿更多，但只能從同一堆拿；拿走最後一個圓圈的人贏。
- 盤面數字：3、4、10、13；二進位 11、100、1010、1101；補零成 0011、0100、1010、1101。
- 走法順序（敘事）：格拉迪亞斯點左上一個（3→2）→ 澤點右下最上面一個（13→12）→ 格拉迪亞斯點左下三個 → 澤把右下點到只剩一個 → 格拉迪亞斯點掉左下剩下的、澤點右上一個 →
  格拉迪亞斯點掉左上剩下的、澤點右上剩下三個中的兩個 → 剩兩個方框各一個，格拉迪亞斯認輸。p21 的推理（只能拿掉其中一個，剩一個給澤拿）保留。
- 用詞：pile→堆；box→方框；circle→圓圈；tap→點；board→盤面；count→數量／圓圈數；base 2／binary→二進位；XOR sum→XOR 和；
  lowest-order digit→最低位；highest-order digit→最高位；lower-order→比它低；N XORed with the XOR sum→N 和 XOR 和做 XOR 的結果；first／second player→先手／後手；
  first-player-favoring／second-player-favoring→先手有利／後手有利。
- p49、p51、p53–p54 的論證鏈（你走只能變非零；非零時我一定有*某一步*變回零；為什麼一定是減少；最後清空盤面那步讓 XOR 和為零；所以致勝那步永遠是我的；
  一開始不是零則先手贏，是零則後手保證贏）每一環都要在。
- p73 規則之塔三層：最底層不可逆（每步至少拿一個）／上一層 XOR 和可逆／再上一層「輪到你走時 XOR 和平衡」不可逆；一旦滑進去、對方懂訣竅，就再也出不來。

## 一、全章固定用詞（editor 一次只看一個 chunk，看不到別處的叫法；這些不要換）

| 原文 | 本章用法 | 出現位置／說明 |
|---|---|---|
| enclosed room | 封閉房間 | p3 |
| tabletop functioning as a screen | 桌面本身就是一面螢幕 | p3 |
| four piles of circles | 四堆圓圈 | p3 |
| top left／bottom right／bottom left／top right box | 左上／右下／左下／右上方框 | p9–p18 |
| Okay fine, I lost | 好啦，我輸了 | p20（characters 引用） |
| Minpentai | 明盤台 | p23 |
| secret sauce | 獨門祕訣 | p24、p25（glossary） |
| mental math | 心算 | p25 |
| the trick | 訣竅 | p71、p73 |
| hand device | 手持裝置 | p34 |
| grid shape | 排成方格 | p34 |
| along the columns | 沿著每一直行 | p36 |
| *some*／*you*／*I*／*not*／*based on*／*that* | *某一步*／*你*／*我*／*不是*／*根據*／*那* | p49、p53、p54、p66、p73（斜體保留在對應詞上） |
| territory | 地盤 | p59 |
| counter-move／counter-strategy | 反制／反制策略 | p66、p78、p80 |
| back into balance／in balance | 恢復平衡／處於平衡 | p66、p73 |
| desirable state／locked in forever | 理想的狀態／永遠鎖定 | p71 |
| chaos | 一團混亂 | p71 |
| Entropy is always in the eye of the beholder. | 熵，永遠存乎觀者之眼。 | p72（glossary） |
| a tower of different kinds of rules | 一座由不同種規則疊成的塔 | p73 |
| irreversible／reversible | 不可逆／可逆 | p73 |
| warmup／line of questioning | 暖身／提問 | p74 |
| the fight for Veridia | 為維瑞迪亞而戰的這場仗 | p75 |
| spying infrastructure | 監控基礎設施 | p78 |
| pressured, bribed or threatened | 施壓、行賄或威脅 | p78 |
| highly coordinated campaign | 高度協調的行動 | p78 |
| do their bidding／nudge | 聽他們使喚／輕推 | p78 |
| important positions | 重要的位置 | p78 |
| On the field of battle | 在戰場上 | p80 |
| the battle for the institutions | 爭奪體制的這一局 | p80 |
| manipulating | 操弄 | p80、p81 |
| Convincing. | 說服。 | p83 |
| influence campaign | 影響行動 | p89 |
| tailor-made | 量身打造 | p92 |
| a lie is essentially a simulated virtual universe | 謊言本質上是一個模擬出來的虛擬宇宙 | p92 |
| self-consistency for free | 真相天生就自洽，不用額外花力氣 | p92 |
| our ask | 請求 | p92、p93 |
| ping Den | 問一下鄧 | p95 |
| spying in Veridia | 在維瑞迪亞的監視 | p95 |
| Senator | 參議員 | p101 |
| admins running the cameras | 管理那些攝影機的管理員 | p105 |
| called home | 回傳 | p105（glossary backdoor 備註） |
| backdoors | 後門 | p105 |
| breaking our cover | 讓掩護……露出破綻 | p105 |
| pull something together | 搞出點名堂 | p108 |
| crazy idea／crazy judgement／crazy time | 瘋狂的主意／瘋狂的判決／瘋狂的時代 | p111、p119（「瘋狂」重複是刻意的，保留） |
| the fourteenth Ground Law | 第十四條基本法 | p112（glossary） |
| lawbreakers | 違法者 | p113 |
| fire them | 撤換 | p113、p120 |
| collective head of the military | 軍隊的集體首長 | p113 |
| philosophical tangent | 哲學性的題外話 | p116 |
| computer program sitting inside a cryptographic network | 放在密碼學網路裡的電腦程式 | p117 |
| re-litigate | 重新爭訟 | p117 |
| programmatic | 程式化 | p118 |
| legally-defined act of fraud | 法律定義的詐欺行為 | p118 |
| settled case law | 已有定論的判例法 | p118 |
| latent flexibility | 潛藏的彈性 | p119 |
| Man was not made for categories. Categories were made for man. | 人不是為了分類而生，分類是為了人而設。 | p119（glossary） |
| sacred duty | 神聖職責 | p119 |
| 'try harder'／outright surrender | 『更努力一點』／乾脆投降 | p122 |

## 二、固定譯名

- 人物：Gladias → 格拉迪亞斯；Zei → 澤；Den → 鄧；Verdow → 韋爾多（Senator Verdow → 韋爾多參議員）；Delwart → 德爾瓦特
- 地名：Pafogai Du → 帕佛蓋都；Dzego → 哲戈；Veridia → 維瑞迪亞；Redshire → 紅郡；Northglade → 北林
- 組織／制度：Order of Steering → 掌舵會；Courts → 法院；parliament → 議會；Ground Law → 基本法；case law → 判例法
- 技術：XOR → XOR（避免：異或）；XOR sum → XOR 和（避免：互斥或和、異或和）；entropy → 熵；cryptographic network → 密碼學網路；backdoor → 後門
- 物品：hand device → 手持裝置（避免：手機）；watch → 手錶
- 日期：Frostime → 霜季

## 三、人物口吻與稱謂

- 稱謂：全章沒有「您」，不要加（格拉迪亞斯叫韋爾多「參議員」，仍用「你」）。
- 澤：當老師，蘇格拉底式反問（「你來告訴我。」「說下去。」）；講數學條理分明；「你學得很快，格拉迪亞斯。」
- 格拉迪亞斯：當學生，好奇、肯認輸（「好啦，我輸了。」「所以現在是你要告訴我獨門祕訣的時候了嗎？」）；半懂時「我……大概懂了？」
- 韋爾多：參議員，熱情（「格拉迪亞斯，你好嗎！」），說理時沉穩、長段、帶哲學味；結尾冷靜評估成功機率。
- 說話者（**原文未標說話者的輪次一律照初譯，不補標籤**）：
  - p5 格拉迪亞斯、p6–p7 澤、p20 格拉迪亞斯、p22 格拉迪亞斯、p23 澤、p24 格拉迪亞斯、p25 澤、p26 格拉迪亞斯、p27 澤、p28 格拉迪亞斯、p29 澤、p30 格拉迪亞斯、
    p31 澤、p32 格拉迪亞斯、p33 澤、p34「他打開手持裝置」（He＝澤，譯者筆記：不點名）、p36 澤、p37 格拉迪亞斯、p38 澤、p39 格拉迪亞斯、p40 澤、p42 澤、p43 格拉迪亞斯、
    p44 澤、p45 格拉迪亞斯、p46 澤。
  - p48 格拉迪亞斯、p49 澤、p50 格拉迪亞斯、p51 澤、p52 格拉迪亞斯、p53–p54 澤、p55 格拉迪亞斯、p57 格拉迪亞斯、p58 澤、p59（未標，不點名）、p60 澤、p61 格拉迪亞斯、
    p62 澤、p64 格拉迪亞斯、p65 澤、p66 格拉迪亞斯、p67 澤、p69 格拉迪亞斯、p70 澤、p71 格拉迪亞斯、p72 澤、p73 澤、p75 澤、p77 格拉迪亞斯、p78 澤、p79 格拉迪亞斯、
    p80–p81 澤、p82–p83（未標，照初譯不點名）、p84–p85（未標）、p87 格拉迪亞斯、p88 澤、p89 格拉迪亞斯、p90–p91 澤、p92 格拉迪亞斯、p93 澤、p94 格拉迪亞斯、p95 澤。
  - p100 韋爾多、p101 格拉迪亞斯、p102 韋爾多、p103 格拉迪亞斯、p105–p106 澤、p108–p109 韋爾多、p111–p113 韋爾多、p114 格拉迪亞斯（或澤，不點名）、p115 韋爾多、
    p117–p120 韋爾多、p121（未標，不點名）、p122 韋爾多。
  - 不同說話者不要合段；同一人連續的段落也照原文分段。

## 四、伏筆與資訊邊界（不可加暗示）

- p8：格拉迪亞斯「覺得自己」對遊戲沒什麼策略上的心得，決定邊玩邊學。
- p11：澤「馬上」回應。p13：「決定換個方式試試」。p17：澤「只」點了一個（simply）。
- p23：小時候「常玩」；「尤其是」在明盤台這種比較現代的東西出現之前。
- p25：「確實有」；簡單的演算法；需要心算；「只要學會了，計算又不出錯」「只要能讓你選先手還是後手」——兩個條件，一定會贏。
- p32：「還有……等一下，1101？」——遲疑保留。
- p37：「每一位都是零，所以就是零？」——推論語氣。
- p43：「所以是 1？」。p45：「抱歉，我忘了。」
- p52：「我……大概懂了？」（maybe get it）。
- p56：往後一靠，想了「一會兒」（a few moments）。
- p57：「我從來沒看過」後手有利的遊戲。
- p58：「不一定是」；「只有在」初始盤面 XOR 和為零時；後手有利的賽局「比你以為的還常見」。
- p59：「通常」都會有。
- p60：「可能」（might）讓一個賽局變成後手有利的根本原因。
- p63、p68、p74、p86：停頓／沉默——不補表情。
- p69：「大概也會贏」（probably）。
- p74：「換了個坐姿，表示暖身結束，真正的提問要開始了」（signaling）。
- p76：「睜大了眼睛，看得出很驚訝」（visibly）。
- p78：北極人的四件事依序：監控基礎設施／施壓、行賄或威脅官員／協調行動「甚至」想拿下掌舵會、讓它聽使喚、輕推社會「別費心抵抗」／攻打紅郡、接著北林。
- p80：現在「是他們佔優勢」；「甚至跟先手無關——純粹是」技術比較好；我們佔優勢，因為我們追求的目標是「大多數」會被我們操弄的人「真正想要的」。
- p81：「方法只是讓他看清」（by just showing them）。
- p82：「這聽起來答案很簡單」（sounds like）。
- p89：「德爾瓦特和其他不知道是誰」（whoever else）；說服他們去做「……某件能扭轉整個局面的事」——停頓保留。
- p92：「真的」對維瑞迪亞有好處；德爾瓦特三件事：每個人不同論點、量身打造（價值觀和弱點）、「暗示或直接」威脅；我們「只要」清楚提出一件請求、直接照實說；
  說謊「很容易」露出破綻；「不把整個宇宙真的模擬一遍，很難」讓它前後一致。
- p95：「快速」問一下鄧；「目前」狀況。
- p99：「過了一會兒」。
- p105：「大部分」管理員「剛剛」裝上更新；更新「也會」回傳每台攝影機「原本的」狀態；「結果發現，有一大堆早就被北極人接管了」；「已經」找出「十幾位」（over a dozen）法官；
  「順便」清掉了「一些」北極人的後門——「不過這也代表」現在得更小心，別讓掩護「再」露出破綻；「甚至可能」玩得更好；法官「真正應該想要的」。
- p107：韋爾多「似乎」笑了（seemed），笑聲裡「主要是」佩服（more with admiration than anything else）。
- p110：「一陣沉默」（For a few moments）；「慢慢」開口。
- p112：「最基本的法律之一」；「白紙黑字寫在文件裡」；在北林「完全」沒能保衛國家，事後「也幾乎沒有試著」做任何認真的改革。
- p113：兩個「所以」的推論鏈；「如果議會想阻止」；議會「在法律上」是軍隊的集體首長。
- p115：「原則上」（In principle）。
- p117：原文 Gather 是 Rather 的筆誤，照意思「而是」；更可預測、更集中；每個案子「不必」重新爭訟根本問題。
- p118：「往往相當接近」程式化（often does approach being quite）；「這正是重點所在」；「任何」特殊案件；「很大的」彈性；「事實上，任何」今天已有定論的判例法，在過去某個時候也都是未知、有彈性的。
- p119：「關鍵」；「我認為」從來沒有人嘗試過「任何稍微類似的事」（anything remotely like it）。
- p120：要贏「不只是」把論點廣播出去；四項：坐下來談／解釋不只是站得住腳的法律論點、也對維瑞迪亞有好處／解釋撤換軍方領導層（必要時連議會）會拯救而非陷入更大混亂／
  讓他們相信夠多其他法官會跟進、大眾也會跟進；先悄悄做、再突然出手（原文 than＝then 筆誤），讓北極人來不及反應。
- p121：「連……都不用」。
- p122：「只有兩種」；「我判斷」兩者的成功機率「比這個還低」（even lower）。
