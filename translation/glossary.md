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
| nullifier | 作廢碼 | 技術 | ch06 | 空值器、無效器 | 由信譽評價以確定性但不可連結的方式產生的偽隨機雜湊值，公開後可防止同一份信譽被重複使用。UI「Nullifier:」→「作廢碼：」。ch06 掌舵會成員以作廢碼開頭「372f」稱呼 Gladias（three-seven-two-eff→「三七二 F」） |
| social recovery | 社交恢復 | 技術 | ch06 | 社會恢復 | 加密錢包術語：由事先指定的親友持有金鑰，湊足門檻（六取四）即可找回資產 |
| combined signatures | 聯合簽章 | 技術 | ch06 | 聯合簽名 | |
| hash | 雜湊值 | 技術 | ch05 | 哈希 | 動詞 hash→雜湊；hash-based trie→雜湊字典樹 |
| pseudorandom | 偽隨機 | 技術 | ch06 | 偽任意 | |
| unlinkable | 不可連結 | 技術 | ch06 | - | |
| collateralize | 抵押 | 技術 | ch05 | - | zero-knowledge-collateralize→以零知識方式抵押；loan collateralized by his reputation→以信譽抵押借款 |
| wallet | 錢包 | 技術 | ch06 | - | |
| transaction | 交易 | 技術 | ch06 | - | |
| hardware attestation | 硬體認證 | 技術 | ch05 | - | |
| counter-surveillance network | 反監控網路 | 技術 | ch05 | 反監視網絡 | |
| infrared scanning | 紅外線掃描 | 技術 | ch05 | - | randomized infrared scanning→隨機紅外線掃描 |
| subvocalization | 默唸 | 技術 | ch06 | 亞發聲 | subvocalization neck band→默唸頸帶（只動喉部肌肉、不出聲說話） |
| earpiece | 耳機 | 物品 | ch06 | - | |
| far-UVC | 遠紫外線 C | 技術 | ch06 | - | far-UVC disinfection lights→遠紫外線 C 消毒燈；敘事中也可只寫「紫光燈」當 Gladias 猜測時 |
| elastomeric respirator | 彈性體呼吸防護具 | 技術 | ch06 | - | |
| prisoner's dilemma | 囚犯困境 | 技術 | ch05 | 囚徒困境 | 台灣通行譯名 |
| surplus | 剩餘 | 技術 | ch05 | - | 經濟學的 surplus；Bai 回嘴時的「surplus」是同一詞，雙關要保留 |
| geometric average | 幾何平均 | 技術 | ch05 | - | |
| superlinearly | 超線性 | 技術 | ch05 | - | |
| eigenvector | 特徵向量 | 技術 | ch08 | 本徵向量 | largest eigenvector→最大特徵向量 |
| self-play | 自我對弈 | 技術 | ch07 | 自我博弈 | self-play finetune→自我對弈微調 |
| finetune | 微調 | 技術 | ch07 | - | |
| pipeline | 流程 | 技術 | ch07 | 管道 | |
| thought transcript | 思考紀錄 | 技術 | ch07 | 思維轉錄 | 明盤台決賽中 AI 的推理過程，雙方可互相讀取 |
| fab | 晶圓廠 | 技術 | ch07 | - | distributed underground fabs→分散式地下晶圓廠 |
| trie | 字典樹 | 技術 | ch06 | - | hash-based trie→雜湊字典樹；bounded-depth trees→有限深度樹 |
| factoring | 因數分解 | 技術 | ch09 | 因式分解 | 「cube modulo n」→「對 n 取模的立方」；p times q→p 乘以 q |
| elliptic curves | 橢圓曲線 | 技術 | ch09 | - | |
| quantum computer | 量子電腦 | 技術 | ch09 | 量子計算機 | |
| obfuscation | 混淆 | 技術 | ch09 | - | obfuscation protocols→混淆協定；指程式混淆 |
| meta-program | 元程式 | 技術 | ch09 | 元程序 | |
| linear transformations | 線性變換 | 技術 | ch09 | - | 「adding errors on top」→再加上誤差 |
| physical unclonable function | 物理不可複製函數 | 技術 | ch09 | - | PUF |
| public key | 公鑰 | 技術 | ch09 | 公共密鑰 | secret key→私鑰／秘密金鑰（依語境） |
| signature | 簽章 | 技術 | ch09 | 簽名 | 動詞 sign→簽署；hash-based signatures→雜湊式簽章；stateless tree-of-tree-based→無狀態、以樹中樹為基礎的 |
| public inspectors | 公共檢驗員 | 技術 | ch09 | - | destructively inspect→破壞性檢驗 |
| supply chain | 供應鏈 | 技術 | ch09 | - | |
| mixnet | 混合網路 | 技術 | ch09 | 混合網絡 | 三層加密、隨機節點轉送；ch09 延伸為實體物流的「混合網路」 |
| node | 節點 | 技術 | ch09 | - | |
| payload | 酬載 | 技術 | ch09 | 有效載荷 | 台灣資訊圈用法 |
| collude | 共謀 | 技術 | ch09 | - | counter-colluding（ch10）→反制共謀 |
| tamper-proof | 防竄改 | 技術 | ch09 | 防篡改 | |
| latency | 延遲 | 技術 | ch09 | - | |
| lightfoot | 光呎 | 自創詞 | ch09 | 光腳 | 光在一拍內走十億光呎；1 光呎 ≈ 259.02 公釐，接近英格沃爾舊單位；「呎」點出它接近英尺 |
| formal verification | 形式驗證 | 技術 | ch10 | - | |
| nonlinear junction detector | 非線性節點探測器 | 技術 | ch10 | - | 偵測竊聽器的真實工具 |
| thermal | 熱像 | 技術 | ch10 | - | 「picking up any powered electronics with thermal」→用熱像偵測通電中的電子裝置 |
| game tree | 賽局樹 | 技術 | ch10 | 博弈樹 | |
| negative-sum game | 負和賽局 | 技術 | ch10 | 負和博弈 | |
| war of attrition | 消耗戰 | 技術 | ch10 | - | |
| deterrence | 嚇阻 | 技術 | ch10 | 威懾 | |
| derivative | 衍生性商品 | 技術 | ch11 | 衍生品 | 金融語境 |
| slippage | 滑價 | 技術 | ch11 | 滑點 | |
| hedge fund | 避險基金 | 技術 | ch11 | 對沖基金 | |
| free option | 免費選擇權 | 技術 | ch11 | 免費期權 | |
| class action | 集體訴訟 | 制度 | ch11 | - | |
| severance | 資遣費 | 制度 | ch11 | 遣散費 | |
| tail risk | 尾部風險 | 技術 | ch11 | - | |
| wastewater scanning | 汙水監測 | 技術 | ch11 | 污水掃描 | |
| cleartext | 明文 | 技術 | ch11 | - | |
| hash function | 雜湊函數 | 技術 | ch12 | 哈希函數 | hash algorithm→雜湊演算法 |
| permutation | 置換 | 技術 | ch12 | 排列 | 密碼學語境 |
| xor | XOR | 技術 | ch12 | 異或 | 保留英文；truncate-and-xor→截斷再 XOR |
| round function | 輪函數 | 技術 | ch12 | - | |
| hex grid | 六角格 | 自創詞 | ch12 | - | 明盤台全國賽的新規則；hexgrid 同 |
| deuterium | 氘 | 技術 | ch11 | - | heavy water→重水；parts per million→ppm |

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
| Herald | 傳令官 | 制度 | ch06 | 使者、傳令員 | 【待決】Q6。從守律者、哨兵中隨機抽出退任、負責對大眾說明的前成員 |
| selection hearing | 遴選聽證會 | 制度 | ch08 | - | acceptance hearing→入會聽證會；admissions test→入會考核 |
| Acceptance voting | 認可投票 | 制度 | ch08 | - | UI「Acceptance vote: Gladias」→「認可投票：格拉迪亞斯」 |
| Senator | 參議員 | 制度 | ch08 | - | Senator Verdow→韋爾多參議員；the Chairman→主席 |
| Chairman | 主席 | 制度 | ch08 | - | 議會委員會主席 |
| Court judges | 法官 | 制度 | ch07 | - | |
| broad listen reports | 廣聽報告 | 制度 | ch08 | 廣泛聆聽報告 | 取自「廣聽」（Broad Listening）的台灣用法 |
| co-parents | 共養父母 | 制度 | ch05 | - | 見 co-family |
| sales tax payments | 營業稅繳納 | 制度 | ch06 | - | 零知識營業稅，見 worldbuilding |
| ground-floor active use | 一樓活化使用 | 制度 | ch06 | - | 規準名稱 |
| Emergency preparedness in physical spaces | 實體空間緊急應變準備 | 制度 | ch06 | - | 規準名稱（UI） |
| Openness in hardware | 硬體開放性 | 制度 | ch06 | - | 規準名稱（UI）；right to repair→維修權 |
| Clean indoor air | 室內空氣潔淨 | 制度 | ch06 | - | 規準名稱（UI） |
| academic and intellectual reputation score | 學術與知識信譽分數 | 制度 | ch05 | - | 大小寫不一，比對時不分大小寫 |
| High Council | 最高議會 | 制度 | ch09 | - | 昆高派的領導機構；High Council member→最高議會成員；councilor（ch10）→議員 |
| circle (Keeper group) | 小組 | 制度 | ch10 | 圈子 | 僅指守律者討論小組（"in this circle"、"third circle of Keepers"）；一般的 green circle 仍譯「圓圈」。third circle→第三個小組 |
| third-year | 第三年 | 制度 | ch10 | - | 守律者的年資；second-year、first-year 同理 |
| number Four | 四號 | 制度 | ch10 | - | 守律者在小組內以編號互稱（One、Four、Six、Nine、Eleven、Eighteen、Twenty、Zero、Two），一律譯「X 號」或直接「X 號」當稱呼；Zero→零號 |
| defense budgets | 國防預算 | 制度 | ch10 | - | |
| bounded matching | 有上限的配對補助 | 制度 | ch11 | - | 平方募資的配對資金 |
| education committee | 教育委員會 | 制度 | ch11 | - | 由議會任命，管理公立學校 |
| funding organs | 資助機構 | 制度 | ch11 | - | |
| Taskmaster | 總督導 | 制度 | ch12 | - | 明盤台全國賽主辦的頭銜 |
| qualifying games | 資格賽 | 制度 | ch12 | - | 全國賽：32 人、六輪資格賽、每輪間隔八天，勝場最多的四人進準決賽 |

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
| surveillance bat | 監視蝙蝠 | 物品 | ch06 | - | 莫夫用的小型偵察裝置，可丟在角落監聽或發出聲響 |
| copter | 小型旋翼機 | 物品 | ch05 | 直升機 | 自由城上空載人載貨的小型飛行器 |
| scratch-off one-time-scannable code | 刮開式一次性掃描碼 | 物品 | ch07 | - | 明盤台獎品，內含密碼學代幣與憑證 |
| cryptographic tokens | 密碼學代幣 | 物品 | ch07 | 加密貨幣 | |
| ozone-based electric water disinfection pen | 臭氧電解淨水筆 | 物品 | ch07 | - | 獎品之一 |
| personal copter | 個人旋翼機 | 物品 | ch11 | - | 旋翼球用的座椅式飛行器，有防護罩，AI 會自動緩衝墜落 |
| longevity package | 長壽套組 | 物品 | ch12 | - | 哲戈招牌「Get your longevity package here」 |
| harness | 訓練框架 | 技術 | ch12 | - | 指微調 AI 的程式框架 |
| green circle | 綠色圓圈 | 物品 | ch01 | - | 全書常見的感應點（閘門、桌面、門邊），手錶或手持裝置貼上去即可驗證、付款；glowing green outline→發綠光的外框 |

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
| zipcoin | 吉普幣 | 自創詞 | ch06 | 拉鍊幣 | 【待決】Q11。貨幣；UI 縮寫 zc 保留原樣 |
| Colorball | 彩球 | 自創詞 | ch08 | - | 學校遊戲，旋翼球（Helisport）的前身。ch11 出現的 redball 建議譯「紅球」以成套 |
| re-spec | 轉換專長 | 一般詞 | ch05 | - | 電玩用語，指重新分配技能點；Bai 用來說澤轉讀密碼學 |
| DU chapter | DU 分部 | 一般詞 | ch05 | 章節 | chapter 此處是分部，不是書的章節 |
| Order, please | 請遵守秩序 | 一般詞 | ch08 | - | 辯論主持人在希爾卡剛說出「The Order members」時打斷，Order（掌舵會／秩序）是巧合雙關，中文難以保留，照「秩序」譯並在譯者筆記說明；ch08 主席的 "Order!"→「肅靜！」 |
| redball | 紅球 | 自創詞 | ch11 | - | 旋翼球的球：會飛的紅色小型無人機球 |
| Veridia ba 'fun' gie | Veridia ba 'fun' gie | 自創詞 | ch10 | - | 賽菈把「Dze go ba fau gie」改成玩笑，想用英文 fun 取代，卻換錯字（fau 只是「再」）。保留拼音與引號；Gladias 的解釋照譯，「Veridia will be fun again」→「維瑞迪亞必將再次好玩」 |
| jia dzu lie | jia dzu lie | 自創詞 | ch09 | - | 哲戈語「黑心果」＝酪梨（avocado）；汾以此解釋文法。例句 giu jan li mo fe jia dzu lie（那個人吃酪梨）等全保留拼音；li、fe、lo、zo、ji 等虛詞說明照譯 |
| Great Book | 經典名著 | 一般詞 | ch10 | - | 維瑞迪亞學校必讀的經典；epic poems→史詩 |
| path less traveled | 人跡較少的那條路 | 一般詞 | ch11 | - | 賽菈引用「維瑞迪亞古作家」；呼應佛洛斯特〈未行之路〉的台灣常見譯法 |
