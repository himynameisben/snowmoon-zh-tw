# 第 1 章 bible 摘錄（第二輪文學編輯用）

主 Agent 依 WORKFLOW「開始一章前」第 5 步建立；每個 chunk 的資料包都附上這份（`literary_edit.py packet --bible`）。
權威來源仍是 glossary／characters／worldbuilding；這裡只是本章會用到的部分，加上本章初譯已定的用詞。

## 一、全章固定用詞（editor 一次只看一個 chunk，看不到別處的叫法；這些不要換）

| 原文 | 本章用法 | 出現位置／說明 |
|---|---|---|
| audio program（Emerald 的空氣傳播病毒講解） | 語音課程／課程 | p10 首次；p50 回扣同一個課程，不可改叫「節目」 |
| the system would be / was keeping score | 系統會記分 | p39 與 p66 刻意同句呼應，兩處用同一句 |
| "... - and nothing else." | ——除此之外，什麼也不知道。 | p5（手錶）、p44（閘門），全書招牌收尾句式 |
| foot path／walking path | 步道 | 與 sidewalk 區分 |
| sidewalk | 人行道 | |
| sky bridge | 天橋 | |
| soundproof barrier | 隔音牆 | p17 起；不可改叫「隔音屏障」 |
| face cover（隱私袍前方） | 臉罩（避免「面罩」） | p50 |
| strap／belt（臉罩上的） | 束帶 | p50 |
| collective（掌舵會） | 團體 | p57–58 |
| businesses（哨兵稽核對象） | 企業（避免「商家」） | p58 |
| rubric 的量詞 | 一條規準／這條規準／某條規準（避免「一份」） | |
| strictly banned | 被嚴格禁止（「嚴格」要保留） | p57 |
| shut down（樂團） | 被封殺（避免「勒令停演」） | p57，譯者筆記已定 |
| civics lessons／civics lore | 公民課／公民傳統 | p21、p64 |
| Select（投票按鈕） | 選定（敘事「他按下『選定』」同步） | p19、p32、p38 |
| Well deserved | 應得的（不用「活該」） | p30 |
| six choose three | 六取三的組合數 | p71 |
| Oh great. Actual responsibility. | 喔，太好了。這下是真的要負責任了。 | p71，人物卡口吻 |
| screed | 檄文 | p82 |
| decoy | 誘餌 | p78 |
| a longhour／a few ticks later | 一長時／幾拍之後 | p84、p85、p117、p140 |
| five decimeters | 五十公分 | p5（2026-10-01 改換算為公分） |
| Dzego food truck／number N | 哲戈餐車／N 號餐 | p105 起 |

## 二、本章出現的 bible 譯名（`uv run tools/literary_edit.py terms 1` 產生）

- zero-knowledge authentication protocol → 零知識驗證協定；避免：零知識認證協議
- authentication protocol → 驗證協定；避免：認證協議
- cryptographic attestation → 密碼學認證
- attestation → 認證
- cryptographic proof → 密碼學證明
- cryptographic sortition → 密碼學抽籤；避免：加密抽籤
- cryptographic network → 密碼學網路；避免：加密網絡
- credential → 憑證
- signature → 簽章／招牌；避免：數位簽名
- bot → AI／預測 AI
- social impact of public performances → 公開演出社會影響
- Steering → 掌舵
- Steering taxes → 掌舵稅
- tax rubric → 稅務規準；避免：評分標準、量規
- rubric → 規準；避免：評分標準
- Tier → 級
- audit → 稽核；避免：審計
- prediction score → 預測分數
- aesthetics tax → 美觀稅；避免：美學稅
- land tax → 土地稅；避免：地價稅
- quadratic voting → 平方投票；避免：二次方投票、平方根投票
- Quadratic Funding → 平方募資；避免：二次方募資、二次融資
- Graph Funding → 圖譜募資；避免：圖表募資、圖形融資
- co-governance → 共同治理；避免：共治理
- civics → 公民
- bounty → 賞金
- deposit → 保證金；避免：押金
- sortition → 抽籤
- number Four → 四號
- hand device → 手持裝置；避免：手機
- watch → 手錶
- compute box → 運算盒；避免：計算盒
- local AI → 本地 AI；避免：本地人工智能
- privacy robe → 隱私袍；避免：隱私長袍
- face cover → 臉罩；避免：面罩
- drone → 無人機
- autobus → 自駕巴士；避免：公共汽車
- Snowmoon → 雪月；避免：雪之月
- longhour → 長時；避免：長小時
- Acolyte → 見習生；避免：侍僧、助祭
- Keeper → 守律者；避免：守護者
- Sentinel → 哨兵；避免：哨衛
- Order member → 掌舵會成員
- decoy → 誘餌
- co-family → 共養家庭；避免：共同家庭
- anti-recommended substances → 不建議物質；避免：反推薦物質
- lifelong learning → 終身學習
- Gladias → 格拉迪亞斯；避免：格拉迪斯、葛拉迪亞斯
- Glad → 格拉德
- Seila → 賽菈；避免：塞拉、席拉
- Zven → 茲文
- Lily → 莉莉；避免：百合
- Febric → 費布里克
- Hreda → 赫蕾妲
- Vil → 維爾
- Daia → 黛亞
- Jahn → 楊恩；避免：揚恩
- Arctic Emperor → 北極皇帝；避免：北極大帝
- Emerald → 翡翠；避免：祖母綠
- Veridia → 維瑞迪亞；避免：韋里迪亞
- Meldan → 梅爾丹
- Kalimar → 卡利馬
- Badra St → 巴德拉街
- Clearhill Ave → 清丘大道
- Freetown → 自由城；避免：弗里敦
- United Cities → 聯合城邦；避免：聯合城市
- Dzego → 哲戈；避免：澤戈
- Order of Steering → 掌舵會；避免：導向修會
- Hydrafill → 海卓菲
- Dreadknot → Dreadknot

## 三、人物口吻與稱謂

- 格拉迪亞斯：理性、溫和、愛用數學想事情；內心獨白帶自嘲冷幽默。平實、口語但不油，不用台語詞。
  被逼急時變得頑皮、有點狡猾（p82「北極皇帝的新檄文」）。
- 賽菈：溫暖、輕快，母親的溫柔語氣，不過度撒嬌。
- 茲文：活潑、大聲、好勝；可用「耶」「我贏了」。叫格拉迪亞斯「爸」。
- 莉莉：簡短、悶悶的，青春期冷淡（「隨便啦……」）。
- 費布里克：直率，強調「維爾才是我爸」，再補貼心話。稱「格拉德叔叔」「賽菈阿姨」。
- 稱謂一律用「你」，不用「您」。閘門機器、翡翠不用代名詞；翡翠代名詞為「它」。
- 孩子視角稱「維爾叔叔和黛亞阿姨」（p126 敘事也照用）。

## 四、伏筆與資訊邊界（不可加暗示）

- p125 莉莉玩的遊戲：原文只說「某個遊戲」、格拉迪亞斯和賽菈看不清，不可暗示遊戲內容（後文揭露北極宣傳）。
- p135 賽菈要去自由城見楊恩：照字面，不加任何關係暗示。
- p139–141 匿名訊息（後文揭露為德爾瓦特）：不用性別詞，不暗示身分。
- p117、p132：原文未標說話者，譯文照樣不標。

## 五、補畫面注意

- 適合補的場景：p3–p10 林間步道、p12–p18 天橋、p42–p51 演唱會入場、p76–p88 追逐、p90–p99 巴士、p101 起晚餐。
- 不補：p20–p40 投票與稅制說明、p57–p59 掌舵會制度、p61–p74 稽核推理與預測分數、所有裝置畫面相關敘述。
