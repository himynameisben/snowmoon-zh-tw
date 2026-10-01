# 第 27 章 譯者筆記

## 新增詞條
- car-free zone → 無車區（glossary.md）
- government-run hotel／government hotel → 政府經營的旅館／政府旅館（glossary.md；ch26 已出現、照 ch26 譯法，本章補登）

（common knowledge、prediction market、arbitrageur、two-party computation、verifiable garbled circuits、machine-checkable、whitepaper、bot、poll、Silverchat Predict、Evelor 等，第零階段都已收錄，照表使用）

## 翻譯決定
- 全章 bot／bots 照 glossary 譯「AI」（不用「機器人」，如第 62、67、100、102、135、139 段）；送茶的 robot 譯「機器人」（第 46、72、132 段），兩者在同一場景出現，譯文能分清楚。
- 第 6 段：「I've failed our whole family」→「我辜負了我們全家」，用「辜負」而不是「讓……失望」，較貼近自責的語氣。
- 第 18 段：common knowledge 的遞迴定義（知道、知道別人知道、知道別人知道別人知道）逐層照譯，不壓縮；兩處斜體保留。這一段原文沒標說話者，譯文不點名。
- 第 26 段：長句中的破折號插入語（說明演算法透明＝那套證明機制）照原文結構保留，後面幾項改用分號接續，讓列舉讀得清楚。
- 第 52 段：wince →「微微皺了一下眉」，沒有補其他動作。
- 第 67 段：「they feed the bot into the sandbox」的 they 指 AI 的擁有者，譯「對方把 AI 放進沙盒」，以免和前半句「我們」混淆。
- 第 69 段：「a tenth of a percent」→「千分之一」。
- 第 77 段：艾費里昂的循環論照 ch08 譯文的用語（技術官僚、民主、混亂、強人、最大特徵向量、複利），兩組循環都用「從……到……再到……」的排比。
- 第 81 段：whitepaper →「白皮書」；Evelor 的自嘲照原文停頓（……）。
- 第 85 段：原文 eternal life elixirs →「長生不老的靈藥」。
- 第 92 段：「Irreversibly. Forever.」→「不可逆。永遠。」保留短句節奏。
- 第 96 段：賽菈的結尾 fighting against／fighting for 用「值得與之對抗」「值得為之奮戰」成對處理。
- 第 97 段：原文說 sat back in his chair，前文其實是長椅（bench），照原文譯「往椅背一靠」。
- 第 99 段：計時器顯示的「150 ticks」視為畫面上的數值，用阿拉伯數字「150 拍」；第 106 段口語「fifty ticks」用中文數字「五十拍」。
- 第 108、110、114 段：哲戈語倒數保留全大寫拼音（glossary「MU GU GEI HUI ZIU FA」）；第 114 段原文的「 ... 」改成全形刪節號「……」。check.py 對這段的「英文字母偏多」WARN 屬正常。
- 第 112 段：「Beat you!」→「搶先你了！」——白搶在澤之前喊出更小的倒數數字。
- 第 118、120、125 段（SVG 圓餅圖）：只翻 title、desc 與 text；兩行標題拆成「你對維瑞迪亞軍方／有多少信心？」，「A new leadership／chosen by parliament」→「議會另選的／新領導層」，「Arturian military／advisors」→「亞圖利亞／軍事顧問」，保持原本的兩行結構。The Arctics →「北極帝國」（選項是指國家勢力）。數字與座標一字未動。
- 第 55 段（艾維洛念出的選項）與 SVG 的選項名稱用同一套譯法（現任領導層、北極帝國、昆高派、亞圖利亞軍事顧問）；只有 B 在敘事中寫「由議會選出的新領導層」，SVG 縮成「議會另選的新領導層」。
- 第 121 段：「Restrict to people who are from Northshore」→「只看北岸省出身的人」；SVG 副標的「people with Northshore ties」→「與北岸省有淵源者」，原文兩處說法本來就不同，照各自譯。
- 第 136 段（AI 摘要）：Executive summary →「重點摘要」；<em>same or greater</em> →<em>維持不變或更大</em>，標籤保留；「strictly greater」→「嚴格大於現在」。

## 不確定之處
- 第 126 段：韋爾多說「Congrats, Evelor」，但第 99 段列出的在場者沒有艾維洛（他也許是遠端連線，或只是韋爾多對著圖表開玩笑）。譯文照原文直接稱呼。
- 第 18 段：說話者沒有標明。從內容看可能是格拉迪亞斯邊聽邊推演，也可能是賽菈接著說；第 19 段「我估計要九十萬」應是賽菈。譯文兩段都不點名，口吻保持中性。

## 建議修改的譯名
無

## 交給第三階段
- check.py terms 對本章的命中都是誤判：「圈子」出自「繞圈子」（going in circles）；「針」出自「針對」；「刻」出自「立刻／時刻」；「操縱」是預測市場的 manipulate（不是明盤台的 steering）；「齊」出自「齊聲」；「芬」出自「塔芬德爾」；watch 在本章是動詞（盯著）；Zero 是「零資訊外洩」「乘以零」的數字零。
- 本章艾維洛口吻：直率、工程師式，用「你」不用「您」，照人物卡。
