# 第 2 章 bible 摘錄（第二輪文學編輯用）

主 Agent 依 WORKFLOW「開始一章前」第 5 步建立；每個 chunk 的資料包都附上這份（`literary_edit.py packet --bible`）。
權威來源仍是 glossary／characters／worldbuilding；這裡只是本章會用到的部分，加上本章初譯已定的用詞。
段號為原文段號（`literary_edit.py plan 2` 的 pNNN）。

## 一、全章固定用詞（editor 一次只看一個 chunk，看不到別處的叫法；這些不要換）

| 原文 | 本章用法 | 出現位置／說明 |
|---|---|---|
| gie fe kiu kai ci bin hu／grow roots, no head | 「gie fe kiu kai ci bin hu」＋「扎根，無首」 | p9 與 p129 呼應；ch18 也用「扎根，無首」，拼音與四字譯都不可改 |
| Dze go ba fau gie／Dzego will rise again | Dze go ba fau gie／哲戈必將再起 | p131–132；ch07 同句，不可改 |
| anti-transmission foil | 阻訊箔 | p5、p39、p105（DU 的防範措施三項之一） |
| the Arctic Empire／the Arctics | 北極帝國／北極人 | p29、p105、p124 |
| Arctic Emperor | 北極皇帝 | p94 |
| boring school | 無聊學校 | p15，汾對一般學校的戲稱；p16「我猜，很無聊？」接著抬槓 |
| critical governance studies | 批判治理研究 | p19、p21 |
| co-governance percentages | 共同治理比例 | p17 |
| DU／Decentralized University／dzu hu sun du | DU／「去中心化大學」／*dzu hu sun du* | p22；之後一律「DU」 |
| Time just hit sixty-nine thousand | 剛到六萬九千 | p23；時刻原文念出來的用中文數字，原文阿拉伯數字（70,001）照用 |
| classroom location … decrypted and broadcasted | 解密廣播 | p23 |
| cryptographic proof system | 密碼學證明系統 | p27 |
| sync our codes | 同步一下我們的代碼 | p27；codes 原文未說明，不要限定成金鑰或驗證碼 |
| lesson／class | 上課／課 | p27、p32、p44 |
| floor -1 | 地下一樓 | p36；先下兩段樓梯、再上一段，動線不可改 |
| the instructor | 講師（敘事）；學生口中「老師」 | 全章；講師對學生稱「你／你們」，kid→「同學」（p96） |
| jar／bottles | 罐（「兩罐氣體」「左邊那罐」）；p80 原文 bottles 初譯「瓶子」 | 講課段落；p80 的 bottles 照原文用詞差異保留「瓶子」或統一為「罐子」皆可，但不要再換成第三種叫法 |
| digits | 位數 | 講課全段：「六百萬位數」「八百萬位數」「一千一百四十萬位數」「三百四十萬位數」「每個分子大約是五點七位」 |
| the information that you do not know／unknown | 不知道的資訊／未知（「未知位數」「未知的總量」） | p62、p66、p73、p79–80；這是整堂課的核心概念，叫法要一致 |
| we have lost knowledge／know less | 失去了知識／知道的比以前少 | p79；p117 澤的笑話「我們對這面牆的了解，比兩分鐘前少多了」回扣這裡，兩處都要讓讀者聽得出呼應 |
| time-reversible／time-irreversible | 時間可逆／時間不可逆 | p88–95 |
| prove by contradiction | 反證法 | p84 |
| un-mix／un-mixing procedure | 分離（程序） | p91–92 |
| temperature equalization | 溫度均衡 | p89 |
| unlimited data compression | 無限的資料壓縮 | p90 |
| enough entropy for one day | 今天的熵已經夠多了 | p121 講師的冷笑話，回扣整堂課 |
| air quality monitor／air quality alarms | 空氣品質監測器／空氣品質警報 | p5（店裡賣的）、p109、p115 |
| air filters | 空氣過濾系統 | p116（QA 已定，不用「空氣清淨機」） |
| debris | 殘骸 | p123 |
| their game … our counter-game | 他們的打算……我們的反制 | p128–129；game 不譯「遊戲」，避免和明盤台混淆；但 p105 的 not just a game 譯「不只是遊戲」 |
| distributed manufacturing | 分散式製造 | p129 |
| exposed individual leaders at the helm | 暴露在外的領導人掌舵 | p129 |
| centralized heavy industry | 集中式重工業 | p130 |
| ticks／milli-ticks／a fraction of a tick | 拍／毫拍／不到一拍 | p11、p32、p100 |

## 二、本章出現的 bible 譯名（`uv run tools/literary_edit.py terms 2` 產生）

- authentication protocol → 驗證協定；避免：認證協議
- cryptographic proof → 密碼學證明
- cryptographic proof system → 密碼學證明系統
- entropy → 熵
- second law of thermodynamics → 熱力學第二定律
- time-reversible → 時間可逆
- compression → 壓縮
- air quality monitor → 空氣品質監測器；避免：空氣質量
- co-governance → 共同治理；避免：共治理
- hand device → 手持裝置；避免：手機
- watch → 手錶
- drone → 無人機
- autobus → 自駕巴士；避免：公共汽車
- anti-transmission foil → 阻訊箔；避免：防傳輸箔紙
- Snowmoon → 雪月；避免：雪之月
- tick → 拍；避免：幾刻、毫刻
- Minpentai → 明盤台
- debris → 殘骸；避免：碎片垃圾
- boring school → 無聊學校
- critical governance studies → 批判治理研究
- zui fia kun zun → 保留拼音，釋義「地下安全處」
- Arctic Emperor → 北極皇帝；避免：北極大帝
- Arctic Empire → 北極帝國；避免：北極圈帝國
- Zei → 澤；避免：賊
- Fin → 汾
- Freetown → 自由城；避免：弗里敦
- United Cities → 聯合城邦；避免：聯合城市
- Devanvil → 德文維爾
- Redshire → 紅郡；避免：雷德郡
- Dzego → 哲戈；避免：澤戈
- Dzegoban → 哲戈語
- Pafogai Du → 帕佛蓋都
- Hun Min → 洪民街（門牌「1990 Hun Min」→「洪民街 1990 號」）
- Mun Gui → 孟桂街（「Mun Gui 1842」→「孟桂街 1842 號」）
- DU → DU／去中心化大學；避免：分散式大學

## 三、人物口吻與稱謂

- 澤：哲戈高中生，數理腦，講解清楚、條理分明；緊張時開冷笑話（p117）。青少年口語，不用台語詞。
  p94 想喊「就跟北極皇帝一樣！」卻忍住，原文是他覺得講破明顯的笑話太沒格調——不要改成別的理由。
- 汾：澤的死黨，在一般學校讀地理；輕鬆、愛調侃，講義氣（p114「我帶你去」）。
- p20「就跟化學要到高中才會教一樣？」是澤回嘴的挖苦（依對話輪次，p21 才是「汾笑了」），照字面，不加解釋。
- 講師：男性、未具名。課堂上蘇格拉底式提問、熱情；危機中冷靜幽默（p121）；談政治時嚴肅（p126 起）。
  對學生用「你／你們」，學生對他代名詞能省則省。
- 其他學生、年輕女子、帶路的男人：本章未具名，不要補身分。

## 四、伏筆與資訊邊界（不可加暗示）

- p36 臨時換教室的男人：原文沒說他是誰、為什麼知道要換。p104 澤只想起他「最後一刻改帶到別間」，p125 也只說
  「不管是誰」；不可暗示他事先知情或身分。
- p105 澤的頓悟：限於原文三項（密碼學、臨時更換地點、阻訊箔）與「北極帝國不只是地理課上的一個單元」，不要多加推論。
- 爆炸：原文只說附近房間一聲巨響、牆和地板塌了一部分，沒說是炸彈；p124 汾才說「北極人」。不可在 p99–101 先寫成「炸彈」「攻擊」。
- 講師 p126「只會越來越糟」與 p128–130 的戰略說明：照原文強度，不加情緒形容。
- p110 講師用 AI 掃描手臂：只說「AI 生成的結果填滿螢幕下方」，不要補診斷內容（診斷是 p113 講師說的）。

## 五、技術段落（p57–p95 講課）

- 數值全部照原文：一百萬個分子；0–999,999（六位數）；右罐「六位數，從零到 99」（原文如此，譯者筆記與 QA 已決定照譯，不改正）；
  六百萬、兩百萬、八百萬；混合後 0–五十萬；每個分子約五點七位；一千一百四十萬；失去三百四十萬位數；
  八百萬位數、八位數。
- p70 講師的三個保留（能量正比於速度平方、速度的表示法可以爭論、完全忽略位置）一項都不能少。
- p80 推理鏈：每一小份熱，加熱冷的東西增加的未知位數＞讓熱的東西冷卻同樣一份減少的未知位數 → 總未知上升；
  每個可能的動作「平均來說」讓總未知不變或上升，「只要做了任何有用的事或犯了任何錯」就上升。「平均來說」不可省。
- p88–92 澤的反證：時間可逆 → 若能把中溫分成高溫與低溫 → 能無限壓縮資料 → 不可能。步驟順序與「時間反轉的過程，輸出一定等於原本過程的輸入」不可省。
- p95 講師：從不知道我們在乎的事，變成不知道我們不在乎的事；投影機排出的廢熱裡分子的速度。
- 這段可以為了口語自然重組句子，但不要把「位數」改成「位元」，也不要補充原文沒有的物理解釋。

## 六、補畫面注意

- 適合補的場景：p3–p11 洪民街（街景、無人機）、p34–p39 下樓梯與教室、p99–p101 巨響、p103–p121 爆炸後的教室、
  p123 掃殘骸。
- 不補：p44–p95 講課與技術說明、p32 澤的心算、p128–p130 講師的戰略說明、所有對話內容、裝置畫面相關敘述。
- 爆炸後段落已經有煙、嗶嗶聲、警報；補畫面不能新增傷者、血、火、新的破壞範圍或人物情緒。
