# 第 30 章 譯者筆記

## 新增詞條
無（adversarial attack、simulated environment、input modalities、classification results、visual input stream、proxy、endpoint、access keys、network addresses、scalar、time-to-detection、trial deviations、perpendicular directions、DOG、jie fe hen dzi、thermal cloak、sky drone 等，第零階段都已收錄，照表使用）

## 翻譯決定
- 第 5、30 段（德盧因的訊息）：只翻 `<p>` 裡的文字；十六進位金鑰字串與 `<span style=…>`、`<br/>` 一字不動。UI 小標「Network:」「Proxies:」照 glossary 譯「網路：」「代理：」。check.py 對這兩段的「英文字母偏多」WARN 都是金鑰字串造成的，屬正常。
- 第 5 段：「the next best thing」→「退而求其次的最好選擇」；「proxy through」→「透過其代理連線」。德盧因的訊息照人物卡維持正式、有禮的文體。
- 第 8 段：汾的「Alright Zei, what do you need?」→「好，澤，你需要什麼？」（人物卡：立刻進入狀況）。
- 第 10 段：汾的語言學玩笑「'language models' are quite connected to language!」→「『語言模型』跟語言的關係可深了！」，保留引號。
- 第 12 段：「not just a binary」→「而不只是有或沒有」（glossary scalar 條）。
- 第 14 段：「perpendicular directions」→「正交方向」、「trial deviations」→「試驗用的偏移」、「time-to-detection」→「被偵測所需時間」，照 glossary。
- 第 18 段：pipeline →「流程」（glossary）。
- 第 30 段：「the sentries might be able to as well」→「哨戒人員可能也看得到」。不用「哨兵」，以免和掌舵會的 Sentinel（哨兵）混淆；ch29 的 sentry units 也譯「哨戒部隊」。
- 第 33 段：「squiggles and messages that seemed simultaneously very recognizable and familiar but also completely alien」→「彎彎曲曲的線條和訊息，看起來既非常眼熟、似曾相識，又完全陌生」。
- 第 36 段：「Manual dexterity was still a major weakness of AI.」→「手部的靈巧度，仍然是 AI 的一大弱點。」
- 第 43–46 段：各路軍回報用簡短的軍事報告體（人物卡）：「北路軍回報：……」。
- 第 47 段：雷克托的「Action.」→「行動。」（人物卡）。
- 第 48 段：「**DOG**」→「**狗**」，粗體照原文（glossary／synopsis 的決定）；「in a giant font, the word」→「用巨大字體寫的一個字」。
- 第 50、71 段（SVG）：只有 Northglade 一個文字節點，譯「北林」；圓點與座標不動。
- 第 52 段：鄧在 ch26 說的話，沿用 ch26 譯文的用語（「跳出框框」「從你的控制台椅子上跳起來，跑過去一拳打在對手臉上」），本章原文只引了後半句，譯文也只引後半。
- 第 58 段：「one and a half to one in the Veridians' favor」→「只有一點五比一，維瑞迪亞僅略佔上風」。
- 第 60 段：原文 fear fewer 是 far fewer 的筆誤（synopsis），照「人數少得多」譯；thermal cloaks →「熱偽裝斗篷」（glossary）。
- 第 62 段：信末的哲戈語「jie fe hen dzi.」保留拼音，原文沒有釋義，不補（glossary）。
- 第 64 段：「Of course I trust you, Deluin, he thought.」→「當然信任你，德盧因，他心想。」——內心話，照 synopsis 的「當然信任你」。
- 第 75 段：Thaldur 照 worldbuilding 寫「薩杜爾」，原文同句的說明（北岸省以東、屬於北極本土的島）照譯。
- 第 77 段：「over fourteen longhours」→「十四個多長時」。

## 不確定之處
- 第 55 段：「casualty ratios」原文說「dropped to six to one」，指的是仍對維瑞迪亞有利、但比十比一下降；譯文照原文說「降到六比一」，沒有補「仍佔優」。
- 第 36 段：「Human Veridian soldiers were already tens of kilometers behind the robotic frontline」的 already 也可以理解成「人類士兵早就退到後方幾十公里」；譯成「原本待在……後方幾十公里處」，意思相近。

## 建議修改的譯名
無

## 交給第三階段
- check.py terms 對本章的命中：「刻」出自「立刻／此刻／片刻」，屬誤判。
- 「哨戒人員」（第 30 段）與 ch29「哨戒部隊」是一般詞，沒有收進 glossary；若第三階段希望固定，可補一條 sentry → 哨戒（避免：哨兵）。
