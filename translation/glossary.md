# 術語表

本書的專有名詞與固定譯法。第零階段建立，第一階段譯者遇到新詞時**只能新增、不能改動**既有列；
既有譯名的修改只在第三階段進行。

## 表格格式（`tools/check.py terms` 會解析，請勿改表頭）

| 欄位 | 說明 |
|---|---|
| English | 原文寫法（大小寫照原文；小寫詞條比對時不分大小寫） |
| 譯名 | 定案譯法。依語境有多種合法譯法時用「／」分隔，例如 `證明／證據` |
| 類別 | 技術／制度／組織／物品／自創詞／一般詞 |
| 首見 | 首次出現的章節，例如 `ch01` |
| 避免 | 不可使用的譯法，用「、」分隔；沒有就填 `-` |
| 備註 | 選這個譯名的理由、語境差異、需要注意的地方 |

狀態標記：在備註開頭加 `【待決】` 表示需要使用者拍板，詳見 `open-questions.md`。

## 技術與密碼學

| English | 譯名 | 類別 | 首見 | 避免 | 備註 |
|---|---|---|---|---|---|
| zero-knowledge proof | 零知識證明 | 技術 | ch03 | 零知識證據 | ch01 先出現 zero-knowledge authentication protocol；ch03 出現 zero-knowledge proof 本詞 |
| zero-knowledge authentication protocol | 零知識驗證協定 | 技術 | ch01 | 零知識認證協議 | protocol 一律譯「協定」（台灣資訊圈用法），不用「協議」 |
| authentication protocol | 驗證協定 | 技術 | ch02 | 認證協議 | authentication＝驗證；attestation＝認證（見下），兩者要分開 |
| cryptographic attestation | 密碼學認證 | 技術 | ch01 | - | attestation 指「由製造商／檢驗方簽發、證明某裝置屬實」的認證 |
| attestation | 認證 | 技術 | ch01 | - | 動詞 attest＝認證、出具認證；UI「Attested ✓」→「已認證 ✓」；unattested→未認證 |
| cryptographic proof | 密碼學證明 | 技術 | ch01 | - | proof 一律「證明」；「Proof verified」→「證明已驗證」 |
| cryptographic proof system | 密碼學證明系統 | 技術 | ch02 | - | |
| cryptographic sortition | 密碼學抽籤 | 技術 | ch01 | 加密抽籤 | sortition＝抽籤（以隨機方式選出公民）；cryptographic 譯「密碼學」而非「加密」，因為重點是可驗證的隨機，不是加密 |
| cryptographic network | 密碼學網路 | 技術 | ch01 | 加密網絡 | 管理掌舵會運作的去中心化網路；也可視語境寫「密碼網路」，但首選「密碼學網路」 |
| credential | 憑證 | 技術 | ch01 | - | 「valid and unused credential」→ 有效且尚未使用的憑證 |
| verify | 驗證 | 技術 | ch01 | - | UI「Verified」→「已驗證」；閘門語音「Verified, welcome」→「驗證完成，歡迎」 |
| two-party garbled circuit | 兩方混淆電路 | 技術 | ch03 | 亂碼電路 | 密碼學術語 garbled circuit，台灣通行「混淆電路」 |
| trust list | 信任名單 | 技術 | ch03 | - | 本地 AI 據此決定可與誰分享位置等資料 |
| location sharing | 位置分享 | 技術 | ch03 | - | |
| contextual intimacy | 情境親密度 | 自創詞 | ch03 | - | Gladias 說是「新流行語」，口吻帶點揶揄 |
| API | API | 技術 | ch03 | 接口 | 保留英文；API restrictions→API 限制 |
| alternative client | 第三方用戶端 | 技術 | ch03 | 客戶端 | alternative interface→替代介面 |
| entropy | 熵 | 技術 | ch02 | - | 物理與資訊理論通用 |
| negentropy | 負熵 | 技術 | ch04 | - | Minpentai 術語「從岩石萃取可用的負熵」 |
| second law of thermodynamics | 熱力學第二定律 | 技術 | ch02 | - | |
| time-reversible | 時間可逆 | 技術 | ch02 | - | time reversibility→時間可逆性；time-irreversible→時間不可逆 |
| price of anarchy | 無政府代價 | 技術 | ch04 | - | 賽局理論術語；敘事中可補成「無政府狀態的代價」 |
| A/B testing | A/B 測試 | 技術 | ch04 | - | |
| compression | 壓縮 | 技術 | ch02 | - | data compression→資料壓縮 |
| air quality monitor | 空氣品質監測器 | 技術 | ch02 | 空氣質量 | |
| PM2.5 | PM2.5 | 技術 | ch03 | - | 裝置畫面保留 |

## 制度與治理

| English | 譯名 | 類別 | 首見 | 避免 | 備註 |
|---|---|---|---|---|---|
| social impact of public performances | 公開演出社會影響 | 制度 | ch01 | - | 規準名稱：tax rubric for social impact of public performances→公開演出社會影響稅務規準 |
| hardware and software openness rubric | 軟硬體開放性規準 | 制度 | ch03 | - | |
| Steering | 掌舵 | 制度 | ch01 | - | 【待決】Q5。Veridia 以稅與補貼「引導」社會的整套機制。Steering system→掌舵制度；Steering mechanism→掌舵機制；Veridian Steering taxes／Steering taxes→掌舵稅 |
| Steering taxes | 掌舵稅 | 制度 | ch01 | - | 【待決】Q5。見 Steering |
| tax rubric | 稅務規準 | 制度 | ch01 | 評分標準、量規 | rubric 一律「規準」（台灣教育界對 rubric 的譯法之一，簡潔且有「依準則評級」之意）。rubric 單用→規準；openness rubrics→開放性規準；environment and biology rubrics→環境與生物規準 |
| rubric | 規準 | 制度 | ch01 | 評分標準 | 見 tax rubric；UI「Other rubric taxes」→「其他規準稅」 |
| Tier | 級 | 制度 | ch01 | 層級 | Tier 3→第三級（敘事）／第 3 級（UI）；UI 表頭「Tier」→「級別」 |
| precedent | 前例 | 制度 | ch01 | 先例 | UI「View relevant precedents」→「查看相關前例」 |
| audit | 稽核 | 制度 | ch01 | 審計 | Sentinel 對個別企業的評級工作；動詞 audit→稽核 |
| prediction score | 預測分數 | 制度 | ch01 | - | Acolyte 的考核分數：抽查的一成稽核與 Sentinel 判定相符的程度；須保持 90 以上 |
| track decision | 路線選擇 | 制度 | ch03 | - | Acolyte 結業後選 Sentinel 或 Keeper 的決定；「final track decision」→最終路線選擇 |
| aesthetics tax | 美觀稅 | 制度 | ch01 | 美學稅 | public aesthetics tax→公共美觀稅。由抽籤選出的公民替建築投票決定 |
| land tax | 土地稅 | 制度 | ch01 | 地價稅 | composite land tax→綜合土地稅；Base land tax→基本土地稅；Total land tax→土地稅合計。不用台灣實際稅目「地價稅」以免混淆 |
| sales tax | 營業稅 | 制度 | ch03 | 銷售稅 | 台灣慣稱；Emerald 報數用 |
| tax bracket | 稅級 | 制度 | ch03 | 稅階 | max tax bracket→最高稅級 |
| subsidy | 補貼 | 制度 | ch01 | 補助金 | |
| quadratic voting | 平方投票 | 制度 | ch01 | 二次方投票、平方根投票 | 台灣 g0v／唐鳳推廣時的通行譯名 |
| Quadratic Funding | 平方募資 | 制度 | ch01 | 二次方募資、二次融資 | 台灣通行譯名（總統盃黑客松採用）。Veridian national Quadratic Funding→維瑞迪亞國家平方募資 |
| Graph Funding | 圖譜募資 | 制度 | ch01 | 圖表募資、圖形融資 | 【待決】Q10。自創制度，以關係圖（graph）分配公共資金；「圖譜」取「社交圖譜」之意 |
| citizens' assembly | 公民會議 | 制度 | ch03 | 公民大會 | 台灣審議民主慣用「公民會議」；citizens' advisory assemblies→公民諮詢會議 |
| co-governance | 共同治理 | 制度 | ch01 | 共治理 | 聯合城邦各城互持投票權的制度；co-governance percentages→共同治理比例 |
| civics | 公民 | 一般詞 | ch01 | - | civics lessons→公民課；civics lore→公民傳統；civics test→公民考試 |
| bounty | 賞金 | 制度 | ch01 | - | 揭發掌舵會成員任務者可得被扣薪資的一半 |
| deposit | 保證金 | 制度 | ch01 | 押金 | 送出猜測時附上的小額保證金 |
| reputation | 信譽 | 制度 | ch01 | 聲譽、名聲 | Rep score→信譽分數；UI「Rep score ≥ 200 Verified」→「信譽分數 ≥ 200 已驗證」；「200 rep anon」→信譽 200 的匿名者；reputation points（ch04 哲戈）→信譽點數 |
| visa | 簽證 | 制度 | ch03 | - | 進入大梅港需要簽證 |
| sortition | 抽籤 | 制度 | ch01 | - | 見 cryptographic sortition |

## 物品、裝置與 AI

| English | 譯名 | 類別 | 首見 | 避免 | 備註 |
|---|---|---|---|---|---|
| hand device | 手持裝置 | 物品 | ch01 | 手機 | 書中的隨身主力裝置，不要譯成手機 |
| watch | 手錶 | 物品 | ch01 | - | 可跑驗證協定、顯示訊息、監測空氣 |
| compute box | 運算盒 | 物品 | ch01 | 計算盒 | 以線接在手持裝置上的外接運算裝置 |
| neck band | 頸帶 | 物品 | ch03 | - | ch01 寫作 silken cloth band（絲質布帶）；讀取喉部肌肉動作，無聲下指令 |
| local AI | 本地 AI | 物品 | ch01 | 本地人工智能 | 在自己裝置上執行的 AI；Gladias 的本地 AI「Emerald（翡翠）」列在 characters.md |
| privacy robe | 隱私袍 | 物品 | ch01 | 隱私長袍 | Veridian Privacy Robe→維瑞迪亞隱私袍；深紫色、連帽及踝，附前臉罩與束帶 |
| face cover | 臉罩 | 物品 | ch01 | 面罩 | 隱私袍前方遮臉的部分 |
| drone | 無人機 | 物品 | ch01 | - | security drone→保全無人機 |
| autobus | 自駕巴士 | 物品 | ch01 | 公共汽車 | 自動駕駛的公車；首次可寫「自駕巴士」，後文可簡稱「巴士」 |
| autonomous delivery vehicle | 自動送貨車 | 物品 | ch01 | - | |
| anti-transmission foil | 阻訊箔 | 物品 | ch02 | 防傳輸箔紙 | 阻擋無線訊號的金屬箔，哲戈房間常見 |
| air filter | 空氣清淨機 | 物品 | ch03 | - | 桌邊白盒；air filters（教室設備）→空氣過濾系統 |
| sensor | 感測器 | 物品 | ch02 | 傳感器 | sensors designed to detect sensors→偵測感測器的感測器 |
| hieroglyphics | 象形文字 | 一般詞 | ch04 | - | |

## 自創詞與其他

| English | 譯名 | 類別 | 首見 | 避免 | 備註 |
|---|---|---|---|---|---|
| hydrogen hydroxide | 氫氧化氫 | 一般詞 | ch03 | 一氧化二氫 | 海卓菲廣告的惡搞：就是水。原文用 hydrogen hydroxide，不是常見梗的 dihydrogen monoxide，照字面譯 |
| enclave | 飛地 | 一般詞 | ch03 | - | 指大梅港 |
| basis points | 基點 | 一般詞 | ch03 | - | |
| anti-cheat | 反作弊 | 技術 | ch04 | - | |
| Snowmoon | 雪月 | 自創詞 | ch01 | 雪之月 | 【待決】Q1。月名兼書名。dateline「3724 Snowmoon 3」→「3724 年雪月 3 日」 |
| tick | 拍 | 自創詞 | ch01 | 刻 | 【待決】Q4。時間單位，一天 100,000 拍（約 0.864 秒）。a few ticks later→幾拍之後；milli-ticks→毫拍；time 顯示的數字（60259）是當天第幾拍 |
| longhour | 長時 | 自創詞 | ch01 | 長小時 | 【待決】Q4。100 分鐘＝10,000 拍（約 2.4 小時），一天 10 長時；half a longhour→半長時 |
| Acolyte | 見習生 | 制度 | ch01 | 侍僧、助祭 | 【待決】Q6。掌舵會的受訓成員 |
| Keeper | 守律者 | 制度 | ch01 | 守護者 | 【待決】Q6。投票決定稅務規準的掌舵會成員 |
| Sentinel | 哨兵 | 制度 | ch01 | 哨衛 | 【待決】Q6。稽核個別企業的掌舵會成員；Sentinel in full standing→正式哨兵 |
| Order member | 掌舵會成員 | 制度 | ch01 | - | 【待決】Q5。口語可簡作「掌舵會的人」 |
| decoy | 誘餌 | 一般詞 | ch01 | - | 替被揭發者引開注意的路人 |
| co-family | 共養家庭 | 自創詞 | ch01 | 共同家庭 | 兩家共同撫養四個孩子，孩子每半年輪住一家 |
| anti-recommended substances | 不建議物質 | 自創詞 | ch01 | 反推薦物質 | 官方勸阻使用的物質（菸酒藥物等）；Hydrafill 廣告也用此詞 |
| lifelong learning | 終身學習 | 一般詞 | ch01 | - | |
| Minpentai | 明盤台 | 自創詞 | ch02 | - | 【待決】Q3。哲戈的高中程式對戰遊戲（類似生命遊戲的細胞自動機對戰）；Minpentai tournaments→明盤台錦標賽 |
| glider | 滑翔機 | 自創詞 | ch02 | 滑翔翼 | 明盤台術語，沿用生命遊戲（Game of Life）台灣通行譯名；glider factory→滑翔機工廠 |
| spaceship | 太空船 | 自創詞 | ch04 | 飛船 | 明盤台術語，沿用生命遊戲譯名 |
| rock formation | 岩塊 | 自創詞 | ch04 | - | 明盤台棋盤上的靜態障礙；rocks→岩塊 |
| wall | 牆 | 自創詞 | ch02 | - | 明盤台術語；mirror wall→鏡牆；moving wall→移動牆（用引號時保留引號） |
| symbol | 印記／符號／標誌 | 自創詞 | ch04 | - | 明盤台語境一律「印記」：玩家專屬的點陣圖樣，棋盤上有其副本即可看見周圍 30 格（原文首次以斜體強調）。一般語境用「符號」（heart symbol→愛心符號）或「標誌」（門上的雙臂標誌） |
| intervention turn | 干預回合 | 自創詞 | ch04 | - | 明盤台中玩家可放置方格的回合 |
| initiation phase | 布局階段 | 自創詞 | ch04 | - | 明盤台開局放置方格的階段 |
| sandbox | 沙盒 | 技術 | ch04 | - | 明盤台中試驗陣型的區域 |
| home base | 主基地 | 自創詞 | ch04 | 大本營 | |
| quarter-finals | 八強賽 | 一般詞 | ch04 | 四分之一決賽 | semi-finals→準決賽；nationals→全國賽；championship→冠軍賽 |
| priests | 祭司 | 自創詞 | ch04 | 牧師、神父 | 班順派（Bansunpei）的成員，也決定明盤台規則；the dungeon→地窖 |
| Dzegoban romanization | 保留原文 | 自創詞 | ch02 | - | 哲戈語的羅馬拼音（如 gie fe kiu kai ci bin hu、MU GU GEI FA、dz-card 內文字、裝置畫面的 zan／tie／tei、MUN GUI、TEI）一律保留原樣、大小寫不改，只翻原文附的英文解釋。本列只作說明，check.py 不比對 |
| gie fe kiu kai ci bin hu | gie fe kiu kai ci bin hu | 自創詞 | ch02 | - | 保留拼音；英文釋義 Grow roots, no head →「扎根，無首」。哲戈的分散式自強戰略口號 |
| Dze go ba fau gie | Dze go ba fau gie | 自創詞 | ch02 | - | 保留拼音；英文釋義 Dzego will rise again →「哲戈必將再起」 |
