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
| anonymity set | 匿名集合 | 技術 | ch13 | 匿名集 | 十三號說透露性別「only cuts down my anonymity set by a factor of two」→只讓匿名集合縮小一半 |
| zero-sum game | 零和賽局 | 技術 | ch13 | 零和博弈 | 與負和賽局成套 |
| re-randomized AI-generated voice | 重新隨機化的 AI 合成語音 | 技術 | ch13 | - | 守律者小組以頸帶傳聲時的變聲處理 |
| mass conservation | 質量守恆 | 技術 | ch14 | - | 明盤台語境：神壇是唯一違反質量守恆的物件 |
| weight-preserving | 保持權重 | 技術 | ch14 | 保重 | 此處 weight 指格子中活細胞的數量（漢明權重）；「XOR is not weight-preserving, but it is reversible」→XOR 不保持權重，但可逆 |
| Key Allocation Group | 金鑰分配小組 | 制度 | ch15 | 密鑰分配組 | 守律者產生投票金鑰時要當面見的五人小組（五取三）。縮寫 KAG 譯文不保留，改寫「金鑰小組」或「金鑰分配小組」 |
| KAG | 金鑰小組／金鑰分配小組 | 制度 | ch15 | - | 見 Key Allocation Group |
| voting key | 投票金鑰 | 技術 | ch15 | 投票密鑰 | 「Only votes signed with a valid key count」→只有用有效金鑰簽署的票才算數 |
| blinded share | 盲化份額 | 技術 | ch15 | 盲分享 | 秘密分享的一份，經盲化處理；「each blinded share of the voting key」→投票金鑰的每一份盲化份額 |
| obfuscated circuit | 經混淆的電路 | 技術 | ch15 | - | 程式混淆（obfuscation）產物；**不要**寫成「混淆電路」，那是 garbled circuit 的譯名（ch03） |
| trusted hardware | 可信硬體 | 技術 | ch15 | 受信任硬件 | 莫夫的妙語「Humans - the ultimate trusted hardware.」→「人類——最終極的可信硬體。」 |
| steganographic encoding | 隱寫編碼 | 技術 | ch15 | 隱寫術編碼方式 | steganography→隱寫術 |
| least-significant bit | 最低有效位元 | 技術 | ch15 | 最低有效位 | higher-order bits→高位元；lowest-order binary digit→最低位的二進位數字。bit→位元（flip a bit→翻轉位元），不收成獨立詞條以免誤比對「a little bit」。澤後文加引號的「least significant」是雙關（LLM 判定「最不重要」的位元），照「最不重要」或「最低有效」皆可，要保留引號 |
| language model | 語言模型 | 技術 | ch15 | - | LLM 保留英文 |
| LLM | LLM | 技術 | ch15 | 大模型 | 保留英文 |
| bucket | 桶 | 技術 | ch15 | 存儲桶 | 雜湊／分組演算法的 bucket；「the i'th bucket」→第 i 個桶 |
| ciphertext | 密文 | 技術 | ch15 | - | 與 cleartext（明文）成對 |
| decryption key | 解密金鑰 | 技術 | ch15 | 解密密鑰 | |
| pseudorandom permutation | 偽隨機置換 | 技術 | ch15 | 偽隨機排列 | |
| happy-path algorithm | 一切順利時的演算法 | 技術 | ch15 | 快樂路徑演算法 | 程式設計俚語 happy path，指沒遇到例外的流程；台灣工程師口語常直接說 happy path，但正文用中文描述較好讀 |
| bandwidth | 頻寬 | 技術 | ch15 | 帶寬 | limited-bandwidth information channel→頻寬有限的資訊通道；higher-bandwidth channels→頻寬更高的通道 |
| cover traffic | 掩護流量 | 技術 | ch15 | - | |
| packet | 封包 | 技術 | ch15 | 數據包 | |
| jamming equipment | 干擾設備 | 技術 | ch15 | - | |
| receiving address | 收款地址 | 技術 | ch16 | 接收地址 | 加密錢包語境 |
| transaction data field | 交易資料欄位 | 技術 | ch16 | 交易數據字段 | |
| recovery procedure | 恢復程序 | 技術 | ch16 | - | 指社交恢復；「test my recovery procedure」→測試恢復程序 |
| security question | 安全提問 | 技術 | ch15 | 密保問題 | ch15 澤說還沒問德盧因 security question；ch16 賽菈的訊息開頭「Security question:」→「安全提問：」。用於確認對方身分 |
| subgraph | 子圖 | 技術 | ch17 | - | 圖譜募資的圖；node→節點；edge→邊；weights（邊的權重）→權重；parent／children→父節點／子節點 |
| directed acyclic graph | 有向無環圖 | 技術 | ch17 | - | 「the graph stops being a tree」→圖就不再是一棵樹 |
| randomize-above-cutoff | 門檻以上隨機分配 | 制度 | ch17 | - | 委員會評為前一成的計畫一律同機率入選 |
| portfolio | 組合 | 技術 | ch17 | 投資組合 | 圖譜募資 SVG：rest of portfolio→組合其餘部分；Air quality portfolio→空氣品質組合 |
| intrinsic motivation | 內在動機 | 一般詞 | ch17 | - | accountability→問責 |
| simulated window | 模擬窗 | 技術 | ch18 | 虛擬窗戶 | 黑色專車以攝影機投影的假窗，會追蹤眼睛調整視角；imitation windows（ch19 建築書）→仿窗 |
| two-dimensional code | 二維條碼 | 技術 | ch18 | 二維碼 | |
| physical-delivery mixnet | 實體配送混合網路 | 技術 | ch18 | - | 見 mixnet；「Like a mixnet, but for people」→就像混合網路，只是換成人 |
| journaling file system | 日誌式檔案系統 | 技術 | ch19 | 日誌文件系統 | |
| erasure code | 抹除碼 | 技術 | ch19 | 糾刪碼 | five-of-six erasure code→六取五抹除碼；recombination algorithm→重組演算法 |
| plaintext | 明文 | 技術 | ch19 | - | 同 cleartext |
| cryptographic pad | 密碼本 | 技術 | ch19 | 加密墊 | 源自 one-time pad（一次性密碼本） |
| level two obfuscation | 二級混淆 | 技術 | ch19 | 第二層混淆 | level four→四級；cryptographic-grade parameters→密碼學等級的參數；overhead→額外開銷 |
| obfuscated language model | 經混淆的語言模型 | 技術 | ch19 | 混淆語言模型 | 與 obfuscated circuit 一致用「經混淆的」 |
| tensor | 張量 | 技術 | ch19 | - | |
| wrapper program | 包裝程式 | 技術 | ch19 | - | |
| backdoored | 植入後門 | 技術 | ch19 | - | |
| non-transmitting room | 無訊號屋 | 技術 | ch19 | - | 不讓任何無線訊號進出的房間 |
| inert storage medium | 惰性儲存媒體 | 技術 | ch19 | 惰性存儲介質 | 本身沒有電路、不會連網的儲存媒體 |
| digital archive node | 數位典藏節點 | 技術 | ch19 | - | |
| gigabyte | GB | 技術 | ch19 | 吉字節 | 「sixty gigabytes」→六十 GB；「10.7 gigabytes」→10.7 GB |
| data retention | 資料保存 | 技術 | ch20 | 數據留存 | data retention in environmental sensors→環境感測器的資料保存 |
| tracker | 追蹤器 | 技術 | ch20 | - | 莫夫偷裝在守律者身上的 |
| micro-inspect | 顯微檢驗 | 技術 | ch20 | - | 見 destructively inspect（ch09） |
| interoperability | 互通性 | 技術 | ch20 | 互操作性 | social media openness and interoperability→社群媒體開放性與互通性 |
| odds ratio | 勝算比 | 技術 | ch21 | 賠率比 | 「shifting the odds ratio by a factor of two or three」→讓勝算比變成兩、三倍；probability update formula→機率更新公式（即貝氏定理，原文沒點名就不要補） |
| threat model | 威脅模型 | 技術 | ch22 | - | |
| view-once file | 閱後即焚檔案 | 技術 | ch22 | 一次性查看文件 | 開啟後五分鐘內可看、不能複製、時間到自動刪除 |
| kill chain | 殺傷鏈 | 技術 | ch22 | 擊殺鏈 | clandestine kill chain→祕密殺傷鏈 |
| ground drone | 地面無人機 | 技術 | ch22 | - | jammer drones→干擾無人機；attack drones→攻擊無人機；swarm→機群 |
| chip and memory-kill | 銷毀晶片與記憶體 | 技術 | ch22 | - | fry the target's circuits→燒毀目標的電路；「Goal: all comms and memory dead」→「目標：通訊與記憶體全部摧毀」 |
| training data | 訓練資料 | 技術 | ch22 | 訓練數據 | |
| noise-tolerant | 抗雜訊 | 技術 | ch22 | 抗噪聲 | highly noise-tolerant erasure code→高度抗雜訊的抹除碼 |
| behavior profiling | 行為側寫 | 技術 | ch23 | 行為畫像 | location tracking→位置追蹤 |
| denial of service attack | 阻斷服務攻擊 | 技術 | ch23 | 拒絕服務攻擊 | Zei 借資安術語形容濫訴；保留這個比喻 |

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
| best-two-out-of-three | 三戰兩勝 | 制度 | ch14 | - | 全國賽決賽賽制 |
| national champion | 全國冠軍 | 制度 | ch14 | - | national Minpentai champion→明盤台全國冠軍 |
| conditional surrender | 有條件投降 | 制度 | ch15 | - | |
| garrison | 駐軍 | 制度 | ch15 | - | Redshire garrisons→紅郡各地駐軍；garrison staff→駐軍人員 |
| President | 總統 | 制度 | ch15 | - | 紅郡總統 Albor→阿爾博總統 |
| Prime Minister | 總理 | 制度 | ch15 | 首相 | 紅郡總理 Celedil→塞勒迪爾總理 |
| interventionism | 干預主義 | 制度 | ch16 | - | 德爾瓦特用語 |
| shadow government | 影子政府 | 制度 | ch15 | - | 鄧：「The shadow society has to become the society. The shadow government has to become the government.」→影子社會必須成為社會本身，影子政府必須成為政府本身；排比要保留 |
| Graph Funding steward | 圖譜募資管理人 | 制度 | ch17 | - | 貝爾戈的身分 |
| committee | 委員會 | 制度 | ch17 | - | 圖譜募資每個節點由密碼學網路隨機選出一個委員會決定下層權重 |
| special interests | 特殊利益團體 | 制度 | ch17 | - | captured by special interests→被特殊利益團體把持 |
| quiet period | 靜默期 | 制度 | ch17 | - | 守律者小組線上討論在投票前七天自動關閉 |
| key registration | 金鑰登記 | 制度 | ch17 | - | 見 Key Allocation Group |
| voting window | 投票時段 | 制度 | ch17 | - | fifteen-longhour voting window→十五長時的投票時段 |
| Motion | 動議 | 制度 | ch17 | - | 投票畫面表頭；Vote→投票；按鈕 Yes／No→贊成／反對 |
| parliament robe | 議會長袍 | 物品 | ch17 | - | 參議員穿的袍子 |
| exchange trip | 交換學習 | 制度 | ch17 | - | winter term→冬季學期；special education→特別課程（此處是資優課程，不是特殊教育） |
| coordination training | 協調訓練 | 自創詞 | ch18 | - | 汾：「Dzegoban is coordination training.」→「哲戈語是協調訓練。」 |
| Coordination Score | 協調分數 | 自創詞 | ch18 | - | 與 Intelligence Score（智力分數）、Emotional Intelligence Score（情緒智力分數）並列；是社群而非個人的屬性 |
| Intelligence Score | 智力分數 | 自創詞 | ch18 | 智商 | 北極帝國的觀念；不要譯成「智商」 |
| positive-sum | 正和 | 技術 | ch18 | - | bad equilibria→不良均衡 |
| rubric group | 規準小組 | 制度 | ch20 | 規準組 | 守律者的討論小組；rubric group on cybersecurity→資安規準小組；rubric group for private schools→私立學校規準小組 |
| insider trading | 內線交易 | 制度 | ch20 | - | |
| noise taxes | 噪音稅 | 制度 | ch20 | - | 小型旋翼機的噪音稅極高 |
| tax nudges | 稅的輕推 | 制度 | ch20 | 稅收推動 | nudge 取行為經濟學「推力」之意，口語寫「用稅輕推」 |
| thumb on the scale | 在秤上動手腳 | 一般詞 | ch20 | 拇指壓秤 | 德爾瓦特批評掌舵會偏袒；敘事中也可寫「偏袒」 |
| peace dove | 鴿派 | 一般詞 | ch20 | 和平鴿 | extreme peace dove→極端鴿派 |
| neutral zone | 中立區 | 制度 | ch20 | - | 北林的大梅港 |
| performative outrage | 作秀式的憤慨 | 一般詞 | ch20 | - | senate hearing→參議院聽證會 |
| appeal (court) | 上訴 | 制度 | ch21 | - | 法律語境；ch16 的「see the appeal」是吸引力，不在此列。維瑞迪亞法院沒有上下級，上訴就是重新抽一組法官；民事雙方皆可上訴，刑事只有被告方可以（ch23） |
| bad faith | 惡意 | 制度 | ch21 | 壞信仰 | bad-faith appeal→惡意上訴；frivolous appeals→濫訴性的上訴；penalty judgement→懲罰性判決；settle→和解 |
| common law | 普通法 | 制度 | ch21 | - | Veridian common law rules→維瑞迪亞的普通法規則 |
| defense statement | 答辯書 | 制度 | ch21 | 辯護聲明 | appeal document→上訴狀 |
| preponderance of evidence | 優勢證據 | 制度 | ch21 | 證據的優勢 | 台灣法律用語。賽菈大吼「IT'S ABOUT THE PREPONDERANCE OF EVIDENCE」→「重點是優勢證據！」，大寫照原文用強調處理 |
| propagandist | 宣傳家 | 一般詞 | ch21 | - | 賽菈：「Ephelion and Delwart are not intellectuals, they are propagandists.」→艾費里昂和德爾瓦特不是知識分子，是宣傳家 |
| cover story | 掩護說詞 | 一般詞 | ch21 | - | pretense→偽裝；ruse→幌子 |
| shelter | 避難所 | 制度 | ch22 | 庇護所 | luxurious room in a shelter→豪華避難所房間；emergency shelter functionality（ch20）→緊急避難功能 |
| cartel | 卡特爾 | 制度 | ch22 | - | 敘事中可補成「卡特爾（聯合壟斷）」一次，之後只寫卡特爾 |
| maximum budget rule | 預算上限規定 | 制度 | ch22 | - | 自由城憲法限制政府預算 |
| unified defense grid | 聯防網 | 制度 | ch22 | 統一國防網格 | 「克城」之間的聯合防禦網 |
| conscientiousness | 盡責性 | 一般詞 | ch22 | 責任心 | 人格五大特質用語；personality test→性格測驗 |
| legitimacy | 正當性 | 制度 | ch22 | 合法性 | legitimacy by performance（ch23）→以績效建立正當性；quick wins→速效成果 |
| defense corps | 國防企業 | 組織 | ch22 | 國防軍團 | corps 這裡是 corporations 的縮寫，不是軍團；defense companies 同；seaborne／airborne→海上／空中 |
| sub-group | 子小組 | 制度 | ch23 | - | 每條規準 21 名守律者分成三個七人子小組 |
| Senate committee | 參議院委員會 | 制度 | ch23 | - | 澤說見習生轉正要通過 Senate committee；ch08 寫 Parliament committee（議會委員會），照原文各自譯 |
| co-father | 共養父親 | 制度 | ch23 | - | 見 co-family；Gladias 稱維爾「My co-father, Vil」→我的共養父親維爾（指同一共養家庭的另一位父親，譯文照字面） |
| Transportation Ministry | 交通部 | 組織 | ch24 | - | administrative change→行政上的變更 |
| de-facto advisor | 實質顧問 | 一般詞 | ch24 | - | de-facto Kungaupei advisor→昆高派的實質顧問 |

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
| nutrition bar | 營養棒 | 物品 | ch13 | 營養條 | rectangular nutrition bar→長方形營養棒；德爾瓦特固定點的餐點 |
| preserved food | 保存食品 | 物品 | ch16 | - | 紅郡淪陷後梅爾丹商家推出「三十天份」的長效保存食品組合 |
| vault | 保險庫 | 物品 | ch16 | 金庫 | Gladias 把第二把金鑰放在保險庫 |
| life savings wallet | 存畢生積蓄的錢包 | 物品 | ch16 | - | Gladias 驚呼「Straight out of a life savings wallet?」→「直接從存畢生積蓄的錢包扣？」 |
| blueball | 藍球 | 自創詞 | ch16 | 籃球 | 旋翼球的球：用來擊倒球瓶。注意別被輸入法換成「籃球」 |
| greenball | 綠球 | 自創詞 | ch16 | - | 旋翼球的球：擊中對方球員會爆出顏料（splatted its paint） |
| pin | 球瓶 | 自創詞 | ch16 | 針、別針 | 旋翼球：高處圓盤上排成三角形的十支黃色球瓶；pin knockdowns→擊倒球瓶 |
| green circle | 綠色圓圈 | 物品 | ch01 | - | 全書常見的感應點（閘門、桌面、門邊），手錶或手持裝置貼上去即可驗證、付款；glowing green outline→發綠光的外框 |
| cabin | 車廂 | 物品 | ch18 | - | 黑色專車的車廂可在隧道中與其他九輛隨機交換（Swapped cabins→換了車廂） |
| Bluewhale Messenger | 藍鯨通訊 | 物品 | ch18 | - | 藍鯨的通訊軟體 |
| Number Ten | 十號餐 | 物品 | ch19 | - | 維瑞迪亞哲戈餐車上的菜名（蘑菇蔬菜飯） |
| sealed cup | 密封杯 | 物品 | ch19 | - | 圖書館在書架旁只給附吸管的密封杯 |
| data cable | 傳輸線 | 物品 | ch19 | 數據線 | |
| Taxi fare | 計程車車資 | 物品 | ch22 | - | UI：Driver base fare→司機基本費；Per-minute toll→每分鐘費；Per-kilometer toll→每公里費；Acceleration and deceleration toll→加減速費（113 m/s Δv 保留）；Road congestion toll→道路壅塞費；Total→合計 |
| calling booth | 通話亭 | 物品 | ch22 | 電話亭 | |
| mini rocket | 小火箭 | 物品 | ch21 | - | 茲文的物理老師給他看的 |
| shadowy cloak | 暗色斗篷 | 物品 | ch24 | - | 鄧的斗篷（ch09 是祭司斗篷） |

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
| shrine | 神壇 | 自創詞 | ch14 | 神社、神龕 | 明盤台準決賽新規則：棋盤上五座神壇（四邊中央各一、中心一座），每一千回合把神壇內容的變化以 XOR 套用到四角附近區域，然後恢復成預設岩塊。northern rock shrine→北方的岩石神壇 |
| eternal glider factory | 永恆滑翔機工廠 | 自創詞 | ch14 | - | 滑翔機在兩座神壇間來回反彈、不斷噴出新滑翔機的結構 |
| symbol-carrying spaceship | 載印記太空船 | 自創詞 | ch14 | 攜帶符號的太空船 | 承載玩家印記的太空船；symbol-carrying ship→載印記船；steerable→可轉向 |
| steering (Minpentai) | 掌舵 | 自創詞 | ch14 | 操縱 | 「the intervention turns were not for building - they were for *steering*」→干預回合不是用來建造，而是用來*掌舵*。刻意呼應維瑞迪亞的 Steering（掌舵），保留斜體；steering instruction→轉向指令 |
| glider storm | 滑翔機風暴 | 自創詞 | ch14 | - | barrage of gliders→滑翔機齊射 |
| debris | 殘骸 | 自創詞 | ch14 | 碎片垃圾 | 明盤台中被摧毀結構留下的殘渣；wreck→殘骸 |
| sitting duck | 活靶 | 一般詞 | ch14 | 坐著的鴨子 | ch14、ch16 都出現 |
| hieroglyphs | 象形文字 | 一般詞 | ch14 | - | 同 hieroglyphics；glyph→字形；pronunciation markers→發音標記；veins（葉脈）→葉脈 |
| Special broadcast | 特別報導 | 一般詞 | ch15 | - | 新聞快報標題；「JUST IN:」→「最新消息：」 |
| Dead Hand of Egalitarianism | 平等主義的死亡之手 | 一般詞 | ch13 | - | 艾費里昂宣傳文標題〈The Dead Hand of Egalitarianism, and the Path of Strength〉→〈平等主義的死亡之手，與強者之路〉。dead hand 原指「死人之手（對後世的僵化控制）」 |
| Hope is not a strategy | 希望不是策略 | 一般詞 | ch15 | - | 莫夫語；Gladias 回「Indeed it's not.」→「確實不是。」 |
| dun | dun | 自創詞 | ch15 | - | 哲戈語裝置畫面欄位（澤手持裝置的「收件人」欄），保留拼音；同理 be（送出按鈕）保留。參見 Dzegoban romanization |
| jie mo kai tu jie hei ja ma | jie mo kai tu jie hei ja ma | 自創詞 | ch14 | - | 哲戈餐廳機器人的招呼語，保留拼音（小寫、問號照原文）；白用裝可愛的聲音模仿它 |
| FI LE GEI TAU FA | FI LE GEI TAU FA | 自創詞 | ch14 | - | 明盤台開局倒數（全大寫哲戈語），連同 MU GU GEI TAU FA、PA GU、TAU FA 全部保留原文 |
| kai ja | kai ja | 自創詞 | ch17 | - | 哲戈語「茶」，字面「植物水」（plant water）；ja＝水。保留拼音，照譯英文釋義 |
| mo fan | mo fan | 自創詞 | ch19 | - | 哲戈語「吃飯的房間」＝餐廳；min＝機器、jan＝人、min jan＝機器人、kun gau＝保全（安全）。畫面上的哲戈語保留，Gladias 的猜測照譯 |
| river horse | 河馬 | 一般詞 | ch19 | 河之馬 | 圖書館門邊的圖；中文「河馬」字面正好是 river horse |
| Outside of a dog, a book is man's best friend | 狗之外，書是人類最好的朋友 | 一般詞 | ch19 | - | 格魯喬・馬克思的名言，雙關 outside of（除了／在……外面）。建議：「在狗之外，書是人類最好的朋友；在狗之內，太暗了，沒法讀。」用「之外／之內」保留一點雙關，並在譯者筆記說明 |
| burn (zipcoins) | 燒掉 | 自創詞 | ch19 | - | 刻意銷毀吉普幣來表示誠意或付費廣播；UI「50 zipcoins have just been burned. 🔥」→「剛剛燒掉了 50 吉普幣。🔥」 |
| message envelope | 訊息信封 | 技術 | ch19 | - | 訊息外層、可供篩選的公開標記 |
| punchline | 笑點 | 一般詞 | ch19 | - | 「as his local AI liked to say, the punchline」→用他的本地 AI 最愛說的話，這就是「笑點」 |
| When you have eliminated the impossible | 排除一切不可能 | 一般詞 | ch21 | - | 福爾摩斯名言，原文少了 however：「When you have eliminated the impossible, whatever remains, how improbable, must be the truth.」→「排除一切不可能之後，剩下的不管多麼難以置信，都一定是真相。」用台灣讀者熟悉的說法 |
| minimalism | 極簡主義 | 一般詞 | ch23 | - | internet minimalism→網路極簡主義；physical minimalism→實體極簡主義 |
| Containing inside the green | 包在綠色裡面 | 自創詞 | ch23 | - | Gladias 逐字硬翻哲戈語的段落：small thinking→小思考（＝極簡主義）、beautiful thinking→美思考（＝美學）、line-heartedness→線心（＝簡單、方便）、locked room→上鎖的房間（＝牢籠）、warm-heartedness→暖心、aggregate-and-group devices→聚合分組裝置（＝計算機）、sound conversation devices→聲音對話裝置（＝電話）、books without an upper lid→沒有上蓋的書（＝無限）。譯文要保留逐字直譯的生硬感，汾、澤的更正則用正常中文。「Containing inside the green」是固定說法，意為「包括哲戈與維瑞迪亞」 |
| background radiation | 背景輻射 | 一般詞 | ch24 | - | 「Love has to come not as a constant background radiation, but as a reward for winning.」 |
| mi cin pin fe lo kin do | mi cin pin fe lo kin do | 自創詞 | ch24 | - | Gladias 用哲戈語打招呼，保留拼音 |
| Chief | 大哥 | 一般詞 | ch22 | 酋長、首領 | 楊恩叫計程車司機「Chief」→「大哥」或「司機大哥」；司機回「boss」→「老闆」 |

## SVG 標籤建議譯法（ch17 圖譜募資圖，不列入比對）

SVG 空間小，中文盡量短；研究者人名見 characters.md。

- 圖一（Airborne disease resistance 子圖）：Airborne disease resistance→空氣傳播疾病防治；Air quality→空氣品質；Early detection→早期偵測；Treatment→治療；Individual non-pharmaceutical prevention→個人非藥物預防（三行可拆成「個人／非藥物／預防」）；Prophylactics→預防用藥；Ventilation→通風；Filtration→過濾；Ultraviolet light→紫外線；Wastewater scanning→汙水監測；Social media open-source analysis→社群媒體開源分析；Individual testing→個人檢測；Airborne environment scanning→空氣環境監測；Antivirals→抗病毒藥物；Supportive care→支持性療法；Immuno-modulators→免疫調節劑；Masks→口罩；Nose sprays→鼻噴劑；Saline nasal rinsing→食鹽水洗鼻；Vaccines→疫苗；Passive immunization→被動免疫；Chemo-prophylaxis→化學預防；rest of portfolio→組合其餘部分。
- 圖二（Ultraviolet light 子圖）：222nm lamp efficiency improvements→222nm 燈具效率改良；222nm safety testing→222nm 安全測試；222nm upper-room deployment→222nm 上層空間部署；Krypton chloride lamps→氯化氪燈；Research into alternative lamp designs→替代燈具設計研究；VNU Materials Science Lab→國立大學材料科學實驗室；VNU Aeronautics Lab→國立大學航空實驗室；effects on household chemicals→對家用化學品的影響；Air quality portfolio→空氣品質組合；「et al」→「等人」。
