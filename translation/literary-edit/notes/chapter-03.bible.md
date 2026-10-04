# 第 3 章 bible 摘錄（第二輪文學編輯用）

主 Agent 依 WORKFLOW「開始一章前」第 5 步建立；每個 chunk 的資料包都附上這份（`literary_edit.py packet --bible`）。
權威來源仍是 glossary／characters／worldbuilding；這裡只是本章會用到的部分，加上本章初譯已定的用詞。
段號為原文段號（`literary_edit.py plan 3` 的 pNNN）。

## 一、全章固定用詞（editor 一次只看一個 chunk，看不到別處的叫法；這些不要換）

| 原文 | 本章用法 | 出現位置／說明 |
|---|---|---|
| tunnel／the Veridian tunnels | 隧道／維瑞迪亞的隧道 | p4 走進隧道、p7、p35「隧道往上爬升」走出來、p74 大梅港的隧道入口；前後呼應，不要改叫「地道」「通道」 |
| poster | 海報 | p5、p7 艾費里昂的海報；p44 美德海報、p48「這兩張海報」；p51 大海報 |
| billboard | 看板 | p55、p59；就是 p51 那張大海報，初譯在長椅段改叫「看板」，維持 |
| Arctic propaganda | 北極的宣傳 | p7 |
| the Arctics | 北極人 | p31、p65、p125 |
| barriers（construction） | 圍籬 | p43–p45「第一道圍籬」「第二道圍籬」 |
| Veridian virtue posters | 維瑞迪亞的美德海報 | p48；原文 *or* 的強調保留一處 |
| Hydrafill water bottle | 海卓菲水瓶 | p45；ch01 是「瓶子」，兩者都可，不要換成第三種叫法 |
| privacy robe | 隱私袍 | 全章；不用「隱私長袍」 |
| face cover／hood／strap | 臉罩／兜帽／束帶 | p78、p81、p93；p78「把鼻子以上和以下隔開」呼應 ch01 p137「把鼻子以下和鼻子以上隔了開來」，動作照原文 |
| watch buzzed | 手錶（就）震動了 | p37、p75、p81 |
| green circle | 綠色圓圈 | p69 入口閘門、p82 與 p93 桌子中央 |
| Proof verified, welcome | 「證明已驗證，歡迎。」 | p70 機器的話，照用 |
| attested／unattested | 認證／未認證 | p79；「用零知識證明確認它出自某家製造商的某個批次」 |
| air filter | 空氣清淨機 | p81（glossary 本章定案；ch02 的 air filters 是「空氣過濾系統」，本章不要改） |
| Steering／Steering system／Steering mechanism | 掌舵／掌舵制度／掌舵機制 | p25「投入掌舵的工作」、p27「整個掌舵機制」、p96「掌舵制度」、p118「我的重點是掌舵」、p122「掌舵」 |
| Steering taxes | 掌舵稅 | p104、p105、p122 |
| rubric／openness rubric | 規準／開放性規準 | p18「網路媒體的其中一條開放性規準」、p25「軟硬體開放性規準」、p113「看到任何規準，就投票刪掉」；不用「評分標準」 |
| Keeper group | 守律者小組 | p18 |
| citizens' assembly／the assembly | 公民會議／會議 | p18、p20 |
| citizens' advisory assemblies | 公民諮詢會議 | p59 |
| alternative interfaces | 替代介面 | p20 |
| alternative client | 第三方用戶端 | p25 |
| max tax bracket | 最高稅級 | p22 |
| cryptographic networks | 密碼學網路 | p24 |
| 200 rep anon friend | 信譽 200 的匿名朋友 | p26；ch01 UI 是「信譽分數 ≥ 200」 |
| the mysterious gentleman | 那位神祕紳士 | p14 |
| Sentinel status | 哨兵資格 | p29 |
| get accepted | 獲准轉正 | p111 |
| final track decision | 最終路線選擇 | p126 |
| Tier 3／Tier 4 | 第三級／第四級 | p100、p102；敘事與對話用中文數字 |
| Acolytes | 見習生 | p102 |
| GPH／Greater Plum Harbor | 大梅港 | 全章；GPH 也譯「大梅港」 |
| a country inside a country | 國中之國 | p58 |
| enclave | 飛地 | p116「一塊紫色用得太多的飛地」 |
| their wall（GPH） | 牆 | p49「像城牆一樣的牆」、p65「假裝他們的牆很醜」 |
| I haven't broken your wall yet | 看來你的心防我還沒攻破 | p98；譯者筆記已定，不用「牆」，避免和大梅港的牆混淆 |
| nutrition bar | 營養棒 | p93、p121 |
| tick | 拍 | p69「大約一拍」、p123「幾拍」 |
| Quadratic Funding／Graph Funding | 平方募資／圖譜募資 | p63、p65、p117–p119、p122 |
| Emerald | 翡翠 | p61–p63；代名詞「它」 |
| neck band | 頸帶 | p61 |
| hand device | 手持裝置 | p55、p60；不用「手機」 |
| Bluewhale／Silverchat | 藍鯨／銀聊 | p20、p24、p25、p125 |

## 二、本章出現的 bible 譯名（`uv run tools/literary_edit.py terms 3` 產生）

- zero-knowledge proof → 零知識證明；避免：零知識證據
- attestation → 認證
- two-party garbled circuit → 兩方混淆電路；避免：亂碼電路
- trust list → 信任名單
- location sharing → 位置分享
- contextual intimacy → 情境親密度
- API → API；避免：接口
- alternative client → 第三方用戶端；避免：客戶端
- PM2.5 → PM2.5
- open source → 開源；避免：開放原始碼
- hardware and software openness rubric → 軟硬體開放性規準
- Steering → 掌舵；Steering taxes → 掌舵稅
- rubric → 規準；避免：評分標準
- Tier → 級
- track decision → 路線選擇
- land tax → 土地稅；避免：地價稅
- sales tax → 營業稅；避免：銷售稅
- tax bracket → 稅級；避免：稅階
- Quadratic Funding → 平方募資；避免：二次方募資、二次融資
- Graph Funding → 圖譜募資；避免：圖表募資、圖形融資
- citizens' assembly → 公民會議；避免：公民大會
- visa → 簽證
- hand device → 手持裝置；避免：手機
- watch → 手錶
- neck band → 頸帶
- privacy robe → 隱私袍；避免：隱私長袍
- face cover → 臉罩；避免：面罩
- air filter → 空氣清淨機
- nutrition bar → 營養棒；避免：營養條
- green circle → 綠色圓圈
- hydrogen hydroxide → 氫氧化氫；避免：一氧化二氫
- enclave → 飛地
- Keeper → 守律者；避免：守護者
- Sentinel → 哨兵；避免：哨衛
- Acolyte → 見習生；避免：侍僧、助祭
- tick → 拍；避免：幾刻、毫刻
- Gladias → 格拉迪亞斯；Glad → 格拉德
- Seila → 賽菈；避免：塞拉、席拉
- Mov → 莫夫
- Delwart → 德爾瓦特
- Arctic Emperor → 北極皇帝；避免：北極大帝
- Arctic Empire → 北極帝國；避免：北極圈帝國
- Emerald → 翡翠；避免：祖母綠
- Veridia → 維瑞迪亞；Meldan → 梅爾丹
- Greater Plum Harbor／GPH → 大梅港
- Freetown → 自由城；避免：弗里敦
- Devanvil → 德文維爾；Inglewore → 英格沃爾
- Northglade → 北林
- Dzego → 哲戈；避免：澤戈
- Bluewhale → 藍鯨；Silverchat → 銀聊
- Hydrafill → 海卓菲
- Dreadknot → Dreadknot（不譯）
- Helisport → 旋翼球；避免：直升機運動

## 三、人物口吻與稱謂

- 格拉迪亞斯：理性、溫和，內心獨白帶自嘲的冷幽默（p7「耶，又是北極的宣傳。」）；對話簡短、講理。
  p85 起和德爾瓦特周旋：問句短、不卑不亢。
- 莫夫：損友式調侃、口語隨性（"Nah"、"the gov"、"gotta"），可用「少來」「欸」，不用台語詞。
  p12「專程來吸走你的靈魂，不是比喻喔。」（literally 的玩笑，譯者筆記已定）；p31「我們的被害妄想得再升級一下」。
  ⚠ p33 "join me as a Sentinel" 已定案譯為「你不只是快要加入我們、成為哨兵的人」（characters.md 莫夫卡），
  不要改成「跟我一樣當哨兵」，也不要讓莫夫看起來是哨兵——他是守律者（p18「我們守律者小組」）。
- 德爾瓦特：表演性開場（「所以，我們終於見面了。」）、客氣自信、措辭有禮卻帶壓迫（p92「真是失禮了。」）、
  口號式短句（p109「自由。真正的自由。」）。對 Gladias 用「你」。
  ⚠ 他的台詞一律照原文、維持人設，不能露出 ch16／ch21 才揭露的身分（銀聊、北極），也不要把他寫得更陰險或更可疑。
- 翡翠：像導航語音的資料式回報，不加語氣詞（p63）。
- 長椅上的兩個男人：p55 只寫兩個人（其中一人 his lap）、p56「第一個男人」、p57「第二個人」、p60「第二個男人」。
  p65「我搞不懂……」與 p66「至少在這裡……」原文沒有標說話者，不要補。
- 連續同一說話者的段落（不要誤判成對話輪替，也不要補說話標籤）：p102–p103、p115–p116、p125–p126 都是德爾瓦特連說兩段。
  p122 是格拉迪亞斯（p121 是敘事）。

## 四、伏筆與資訊邊界（不可加暗示）

- p128：另一個穿隱私袍的人從隔壁包廂走出來、跟上德爾瓦特。原文沒說是誰；p130 裝置畫面的地圖才標出莫夫。
  敘事不可寫出或暗示「是莫夫」。
- p14：莫夫說要「暗中跟著你」去見神祕紳士；照原文，不要提前說他會跟蹤德爾瓦特。
- p33「趁現在還見得到的時候」（while we still can）：保留原文的含糊，不加強成不祥預感，也不弱化掉。
- p24：守律者的先生丟了工作，「不知道兩件事有沒有關係」——不確定性要保留。
- p25：「無疑是……至少在斤斤計較的財務人員面前，是拿這個當理由」——"or at least" 的退一步不可省。
- p79：未認證裝置的四種可能（孩子的科學作業／大梅港本來就正常／間諜攝影機／更糟的東西）全部保留，
  順序與「畢竟從維瑞迪亞的角度，這整塊地只是一家巨型企業的私有財產」的插入理由都要在；不要暗示和德爾瓦特有關。
- p31：莫夫只叫他換上新的隱私袍，原文沒寫 Gladias 換了；不要補。
- p125：德爾瓦特「我可以幫忙保護你。但我也需要你的幫忙。」半威脅半拉攏，照原文強度。
- p120「都快變成在資助一場可能的戰爭了」：QA 已確認語氣適中（cutting so close）。
- p122：「如果掌舵稅歸零，我們就非砍（圖譜募資）不可」——因果（圖譜募資靠掌舵稅）不可省。

## 五、數值（照原文）

- p5 Y 字形岔路口、四塊膠帶；p13 大約一百個人；p14 一年前；p18、p20 一個月前；p27 至少一成；p29 今年整年。
- p40 四張圖片（第一張市中心、第二張大公園入口閘門前，左邊告示是價目表）。
- p63 營業稅平均 5.2%，全市平均的一半；土地稅合計 1.48%，略高於全市平均；圖譜募資（尤其平方募資）約回收其中一半。
- p67 將近十年。p69 大約一拍。p73 高度大約五到十公尺；四分之一公尺寬的標誌。p74 五分鐘。
- p79 五十五台裡有六台未認證。p81 PM2.5 低於 1。p83 兩分鐘後；p84 五分鐘後；p93 幾分鐘、一分鐘後。
- p111 兩個月後；p115 每條規則大概二十個守律者；p123 幾拍；p126 大約一個月。

## 六、補畫面注意

- 適合補的場景：p3–p5 商店街與隧道、p35–p37 走出隧道、樹、孩子、p42–p46 都會區與工地、p49–p53 大梅港外牆、
  p55 長椅、p72–p75 大梅港內部與地下人潮、p80–p84 隱密庭院與包廂。
- 不補：p7 對海報的想法、p11–p33 與 p86–p128 的對話內容、p25 的回憶、p59 偷聽的理由、p77–p79 的推理、
  p63 翡翠的回報、所有裝置畫面相關敘述（p39–p41 看照片、p53 掃條碼、p75、p81 的讀數）。
- 對話段落中的敘事句（p30、p93、p121、p123、p127–p128）原則上不補；p93、p121 只是吃喝動作，不要加氣氛。
- 庭院、包廂已有布簾、燈、花、白色盒子；補畫面不能新增人物、可疑跡象、監視感，或改變誰看見了什麼。
