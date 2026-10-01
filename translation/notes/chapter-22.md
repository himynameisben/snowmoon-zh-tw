# 第 22 章 譯者筆記

## 新增詞條
無（shelter、cartel、maximum budget rule、unified defense grid、conscientiousness、legitimacy、defense corps、threat model、view-once file、kill chain、ground drone、chip and memory-kill、training data、noise-tolerant、Taxi fare、calling booth、Chief、seaborne drone、Freetown Economics Institute director 等，第零階段都已收錄，照表使用）

## 翻譯決定
- 第 7、9 段（廣告）：數字照廣告體用阿拉伯數字（地下 10 公尺、325,000 吉普幣、50,000 吉普幣）；「for the common man」→「平民也住得起的」；mortgage plans →「分期貸款方案」。
- 第 12 段（車資表）：欄位照 glossary「Taxi fare」；原文三列重複的 Road congestion toll 照留三列；「9 min」「5.65 km」譯成「9 分鐘」「5.65 公里」，「113 m/s Δv」保留。
- 第 21 段：「cartel」照 glossary 寫「卡特爾」，前後文已說明是幾家公司聯合，沒有另加括號解釋。
- 第 23 段：「not *quite* that clean」→「沒有*那麼*乾淨」，保留斜體位置。
- 第 24–26 段：原文三段連續引號都沒標說話者。依語意判斷前兩段是楊恩、「And at defending itself.」較可能是司機接話，但譯文照原文不點名。單引號 'maintenance'、'free' 在對話中改用『』。
- 第 28–29 段：司機的「boss」照 glossary 譯「老闆」；楊恩的 Chief 譯「大哥」。
- 第 41 段：「average indoor CO2 levels dropped by over a hundred points」→「室內二氧化碳平均濃度就降了一百多點」。原文寫 points 不寫 ppm，照原文不補單位。
- 第 59 段：「register all that as being "free"」的內層引號改『自由』。
- 第 60 段：「but not at the expense of leaving each other space to be in peace」字面邏輯有點擰（應是 not at the expense of *not* leaving），照意思譯成「但不能因此就不給彼此清靜的空間」。
- 第 25 段：原文 node（in Northglade）是大梅港的分部，不是技術上的節點，譯「據點」。
- 第 80 段：view-once file 照 glossary「閱後即焚檔案」；「Politeness dictated not interfering with these defaults」→「基於禮貌，大家都不會去動這些預設」。
- SVG：只有 `<text>` 裡的「x」，是擊中標記，不譯；敘事中「red X」→「紅色的 X」，對應圖上的標記。
- 第 92 段：「And ... action.」→「然後……動手。」取下指令的語感；「拍電影的『開拍』」太戲謔，沒有用。
- 第 104 段：italic *survive*／*活*、第 105 段 *活下來* 保留斜體。
- 第 114 段：澤對 AI 下令「Circles」→「圓圈」，直接用圖上干擾無人機的圖形來稱呼它們，與人物卡「對 AI 下指令簡短如軍令」一致；「northwest square」→「西北方的方塊」（圖上的紅色方塊是敵機）。「Goal: all comms and memory dead」照 glossary。
- 第 117–118 段：「No-」「Wha-」→「不——」「怎——」，都是話說到一半被打斷。依下一段「楊恩話說到一半就停住了」判斷「Wha-」是楊恩；「No-」較可能是澤看到斷線時的反應。譯文照原文不點名。
- 第 121 段：「our AI against the Arctics, AI plus human」→「我們的 AI 對上北極人的 AI 加真人」：理解成北極那邊是 AI 加上人類操作員（我方則已斷線、只剩 AI）。
- 第 136、138 段：楊恩接澤的「one of our other big projects」問「One of ...」，譯為「其他幾個大計畫之一」／「其中之一……」，保留這個接話。
- 第 137 段：「anyone or any bot spying on the call」→「任何監聽通話的人或 AI」，bot 照 glossary 不譯「機器人」。

## 不確定之處
- 第 40–41 段：「So ... somehow the market incentives seem to be working.」以及之後「You know, I've been talking to Zei...」的說話者：依上下文（楊恩替澤牽過線）判斷是楊恩，但原文沒標。第 60 段「I think there might be a core...」可能是楊恩，也可能是烏塔庫在反駁；第 62 段提到貝爾帕基，應是烏塔庫。譯文都不點名，不影響理解。
- 第 92 段：「And ... action.」是澤說的，但也可能是楊恩在湊熱鬧（前一句「我好興奮」是楊恩）；依語氣判斷是澤。
- 第 117–118 段：「Wha-」若是楊恩、「No-」是澤，順序上是澤先叫；但也可能兩句都是楊恩開口又打住。譯文的中文不受影響。

## 建議修改的譯名
無

## 交給第三階段
- check.py terms 對本章的命中都是誤判：「簽名」（在表格上簽名，非密碼學簽章）、「圈子」（those circles＝社交圈，非守律者小組）、「刻」（立刻、此時此刻）、「拜」（拜託）；node 譯「據點」是刻意的（見上）。
- 楊恩在本章話變多、帶經濟學家的長篇說理，與人物卡「話不多」的初始描述不同；人物卡已有 ch22 補充，口吻可在第三階段跨章檢查。
