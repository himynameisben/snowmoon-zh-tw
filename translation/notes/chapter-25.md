# 第 25 章 譯者筆記

## 新增詞條
無（XOR sum、first-player-favoring／second-player-favoring、backdoor、Ground Law、case law、secret sauce、Entropy is always in the eye of the beholder、Man was not made for categories、Frostime 等都已收錄，照表使用）

## 翻譯決定
- 第 4、10、12、14、16、19 段（SVG 盤面）與第 35、41、47 段（二進位方格）：圖內沒有文字，整段從原文原樣複製。
- 第 3–19 段：遊戲原文沒有名字（就是 Nim），照 synopsis 不補「尼姆」。pile→「堆」，box→「方框」（螢幕上的四個虛線框），circle→「圓圈」，tap→「點」。
- 第 6 段：「It's your turn first」→「你先走」；第 25 段「choose if you're going first or second」→「選要先手還是後手」，之後一律用「先手／後手」（glossary）。
- 第 27 段：「base 2」→「二進位」；XOR sum 照 glossary →「XOR 和」。
- 第 36–37 段：「count up along the columns」→「沿著每一直行數一數」；「They all have two ones」→「每一行都有兩個 1」。
- 第 43 段：「Lowest-order digit」→「最低位」；第 51 段「highest-order digit」→「最高位」、「lower-order」→「比它低」。「N XORed with the XOR sum」→「N 和 XOR 和做 XOR 的結果」。
- 第 49、53、54、66、73 段：斜體 *some*、*you*、*I*、*not*、*based on*、*that* 都保留在對應的中文詞上。
- 第 72 段：照 glossary「熵，永遠存乎觀者之眼」。
- 第 75 段：「the fight for Veridia」→「為維瑞迪亞而戰的這場仗」；synopsis 寫「保衛維瑞迪亞」，意思相同，取較貼原文的說法。
- 第 81 段：澤的反問句（manipulating … by just showing them how it's in their interest）重組成「操弄別人去做……方法只是讓他看清……——這叫什麼？」，讓答案「說服」落在下一句的位置。
- 第 85 段：「You tell me.」→「你來告訴我。」，保留蘇格拉底式的反問口吻。
- 第 92 段：「the truth gives you self-consistency for free」→「真相天生就自洽，不用額外花力氣」。
- 第 98 段：撥出通話的表頭 Message／To／Time →「訊息／收件者／時間」，比照 ch15、ch16；「[requesting call]」→「［請求通話］」（ch08）；「Senator Verdow」→「韋爾多參議員」。
- 第 105 段：「It also called home」照 glossary backdoor 備註譯「回傳」。
- 第 112 段：「the fourteenth Ground Law」→「第十四條基本法」（glossary）。
- 第 117 段：原文「Gather, the goal is to structure it」的 Gather 是 Rather 的筆誤，照意思譯「而是」（synopsis 已註明）。
- 第 119 段：「Man was not made for categories. Categories were made for man.」→「人不是為了分類而生，分類是為了人而設。」照 glossary 備註建議的全句，不加註出處。
- 第 120 段：「do all that first quietly than suddenly」的 than 應是 then 的筆誤，照意思譯「先悄悄地做，再突然出手」。

## 不確定之處
- 第 34 段：「He opened up his hand device, and wrote down…」的 He 依上文（上一句是澤說「寫下來」）應是澤，譯文不點名。
- 第 59 段：「Normally there's some position…」原文沒標說話者，接在澤的話之後、在澤的提問之前，可能是格拉迪亞斯的回應，也可能是澤自己補充。譯文不點名。

## 建議修改的譯名
- Man was not made for categories：譯名欄是「人不是為分類而生」，備註卻建議全句「人不是為了分類而生，分類是為了人而設」，兩者差一個「了」，check.py terms 因此報「找不到譯名」。本章用備註的全句；建議第三階段把譯名欄統一成「人不是為了分類而生」。

## 交給第三階段
- check.py terms 對本章的其他命中都是誤判：「管道」出自 channels（不是 pipeline）；「針」出自「針對」；「刻」出自「立刻」「此時此刻」。
