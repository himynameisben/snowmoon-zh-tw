# Snowmoon 編輯工作規範

本 repo 是 Vitalik Buterin 小說《Snowmoon》的台灣繁體中文社群譯本。英文原文已整理完成，
Claude 初譯、雙語 QA 與全書一致性檢查也已完成。現在若使用者要求「潤稿、小說化、重編、
literary edit」，預設指的是第二輪文學編輯，不是重新翻譯。

## 必讀文件與優先順序

開始正文工作前，依序讀：

1. `translation/literary-edit/WORKFLOW.md`：第二輪文學編輯的總指揮流程。
2. `translation/literary-edit/literary-editor.md`：Literary Editor subagent prompt。
3. `translation/literary-edit/faithfulness-reviewer.md`：Faithfulness Reviewer subagent prompt。
4. `translation/literary-edit/examples.md`：正反例；範例用來示範手法，但仍受英文原文與硬性規則約束。
5. `translation/style-guide.md`：全書共通文風與格式。
6. `translation/glossary.md`、`translation/characters.md`、`translation/worldbuilding.md`：固定譯名與設定。
7. 工作章節的 `translation/notes/chapter-NN.md`、`translation/qa/chapter-NN.md` 與
   `translation/synopsis.md` 對應段落。

若規則衝突，硬性結構與 bible 優先；第二輪的文學編輯方法則以
`translation/literary-edit/` 為準。

內容判斷的權威順序是：**英文原文 > glossary／characters／worldbuilding > 已確認的章節脈絡 >
現有初譯 > style examples**。初譯是底稿，不是事實來源；範例只示範手法，不能推翻原文。

## 不可違反的邊界

- `source/en/`、`original/`、`zh-tw-v1/`（凍結的初譯快照）不可修改。第二輪編輯直接改 `zh-tw/`。
- `source/en/chapter-NN.md` 與 `zh-tw/chapter-NN.md` 依**錨點**對齊：標題、HTML 區塊、分隔線、`>` 引言、
  清單的種類、數量與順序不變（`check.py` 檢查）。兩個錨點之間的散文段稱為**段群**，段群內可以拆段、合段、
  重排句子與段落；資訊不可跨錨點搬移。
- HTML 標籤、屬性不可改；錨點內只可編輯文字。
- 內容忠實，句法與分段不必忠實。段群內怎麼重寫都可以，但不得改變資訊、因果、語氣強度、
  不確定性、人物意圖、技術機制或敘事事實。
- 不得增加原文沒有的動作、心理、情緒、動機、象徵、比喻、情節事實或伏筆。唯一例外：第二輪場景敘事段落可補
  少量感官細節（聲音、光線、人群動態、空間感、身體感受），規則見 `translation/literary-edit/literary-editor.md`「補畫面」。
- 專有名詞依 bible。若自然化需要改固定譯名或單位，主 Agent 只提出 flag；取得使用者明確同意後，
  才能更新 bible 並另行做全書一致修改。不得因單章工作擅自擴大範圍。
- 不使用中國大陸用語，不把平實文字改成文青腔，也不把作者的工程師式冷靜語氣抹掉。

## Subagent 編排

使用者已明確要求由主 Agent 指揮 subagent。正文工作採順序流程，不可把同一 chunk 的兩個角色平行執行：

1. 主 Agent 建立本章 bible 摘錄（含全章固定用詞），用 `tools/literary_edit.py` 以完整段群切 chunk、產生資料包
   （英文、初譯、前後文與 bible 摘錄）。
2. Literary Editor（Opus，附初譯）重寫句法與分段，可補少量畫面，只提出編輯稿與必要 flags，不做事實裁決。
3. 主 Agent 用 `literary_edit.py validate --report` 驗證結構並產生用詞差異表。
   Faithfulness Reviewer（Opus）對英文逐項核對編輯稿與用詞差異表，只回 PASS 或具體 ISSUE，不直接改稿。
4. 主 Agent 決定並套用最小必要修正（`literary_edit.py apply`）。只要依 ISSUE 做了實質修訂，就送 reviewer 複查至 PASS。
5. 完成整章後做銜接通讀，並執行 `uv run tools/check.py chapter N`。

詳細步驟、模型選擇的理由與指令見 `translation/literary-edit/WORKFLOW.md`。

主 Agent 不可把 editor 的輸出直接視為定稿，也不可讓 reviewer 為了文筆偏好提出修改。

實際派工時，Codex 使用可用的 subagent／multi-agent 工具建立獨立 agent；Claude Code 使用其 Agent／Task
工具。把角色 prompt 的檔案路徑與 chunk 資料包交給 agent，角色不可在主 Agent 同一上下文中自行模擬。
若目前執行環境沒有 subagent 能力，停止在正文寫入之前，向使用者說明需要在支援 subagent 的 session 執行；
不可省略 reviewer 或由主 Agent 假扮兩個角色。

## 工作範圍與提交

- 除非使用者明確要求，先從一章或一個測試區段開始，不一次重編全書。
- 編輯正文時同步更新 `translation/literary-edit/progress.md`；重要取捨寫入該章紀錄。
- 不自行 commit。使用者要求 commit 時才提交。
- 不覆蓋使用者既有的未提交修改；開始前先看 `git status --short`。

## 驗收

每個完成章節至少確認：

- 結構檢查零 ERROR。
- 沒有漏譯、增譯、誤譯、數字或單位錯誤。
- 固定譯名、人物稱謂與技術設定一致。
- 沒有明顯英文句法、機械連接詞或不自然抽象動作。
- 沒有新增 AI 常見的文青套語，例如不必要的「彷彿」「沉默地」「灑落」「說不上來的感覺」。
- 所有 chunk 已由 reviewer 判為 PASS，章節接縫檢查造成的修改也已重新通過 review。
