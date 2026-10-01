# 第二輪文學編輯流程

## 目的

這一輪處理的是已完成的繁中初譯。目標不是重譯，也不是替作者改寫，而是在完整保留英文原文
資訊與《Snowmoon》設定的前提下，讓譯文像原本就是為台灣讀者寫的小說。

一句話原則：**內容忠實，句法自由；局部可重組，全局受約束。**

角色分工：

- Literary Editor：負責「不要像翻譯」。
- Faithfulness Reviewer：負責「不要改過頭」。
- 主 Agent：負責切段、提供上下文、裁決衝突、套用修訂、全章銜接與機械驗收。

## 開始一章前

主 Agent：

1. 看 `git status --short`，保留使用者既有修改。
2. 讀完整英文原文與完整繁中初譯，先掌握章內伏筆、語氣與技術說明的作用。
3. 讀本章 synopsis、notes、QA，以及 bible 中與本章人物、場景、技術相關的條目。
4. 執行一次 `uv run tools/check.py chapter N`，確認基準檔案原本可通過檢查。
5. 依完整段落切 chunk。以 800–1,500 個中文字為常態，不為湊字數切開段落、HTML block、對話組或
   一段完整技術推演。必要時可略短或略長。為每個目標段落指定穩定 ID，例如 `ch01-p023`。

## 每個 chunk 的資料包

主 Agent 給 Literary Editor：

```text
章節：chapter-NN
目標範圍：第 A–B 段（只有這些段落可以改）

<paragraph_map>
chNN-pAAA = 本章第 A 段
chNN-pAAB = 本章第 A+1 段
</paragraph_map>

<source>
--- chNN-pAAA ---
對應英文原文第 A 段
--- chNN-pAAB ---
對應英文原文第 A+1 段
</source>

<draft>
--- chNN-pAAA ---
目前繁中初譯第 A 段
--- chNN-pAAB ---
目前繁中初譯第 A+1 段
</draft>

<context_before>
前文一至兩個完整段落；只供理解，不可改
</context_before>

<context_after>
後文一至兩個完整段落；只供理解，不可改
</context_after>

<relevant_bible>
只放這個 chunk 實際需要的固定譯名、人物口吻與設定
</relevant_bible>
```

subagent 必須先讀其角色 prompt、`examples.md` 與共通 style guide。不要把整份 glossary 每次貼進 task；
主 Agent 應選出相關條目，降低干擾。`--- chNN-pNNN ---` 是交接用定位標記，不屬於正文；editor 輸出時
必須保留相同標記，主 Agent 套用 patch 時移除標記。Reviewer 的 ISSUE 用同一 ID 定位。

## 實際派工方式

- Codex：使用 session 提供的 subagent／multi-agent spawn 工具建立獨立 agent，將角色 prompt 路徑與資料包
  一併交付；editor 完成後才派 reviewer。
- Claude Code：使用 Agent／Task 工具，分別載入兩份角色 prompt，仍採 editor → reviewer 串行。
- 若環境沒有 subagent 能力，不可在主 Agent 同一上下文裡假裝角色隔離，也不可跳過 reviewer；在修改正文前
  停止並告知使用者需要換到支援 subagent 的 session。

## 順序與裁決

### 1. Literary Editor

派工短 prompt：

```text
請先完整閱讀 translation/literary-edit/literary-editor.md、
translation/literary-edit/examples.md 與 translation/style-guide.md，
再依提供的章節與段落範圍進行 literary edit。
只輸出角色 prompt 規定的格式，不修改 repo 檔案。
```

主 Agent 收到輸出後，先確認段落數與 HTML／Markdown 結構沒有變動，再送 reviewer。

### 2. Faithfulness Reviewer

Reviewer 必須看到同一份英文原文、原始初譯、editor 的完整輸出、相關前後文與 bible。派工短 prompt：

```text
請先完整閱讀 translation/literary-edit/faithfulness-reviewer.md，
再逐項核對以下英文原文與編輯稿。只做忠實度審查，不潤飾，不修改 repo 檔案。
```

### 3. 主 Agent 整合

- Reviewer 回 `PASS`：主 Agent 仍需快速核對格式，再以最小 patch 套用。
- Reviewer 提 ISSUE：以英文原文與 bible 為準。修復問題時盡量保留 editor 已改善的自然中文。
- 任何「可能」「似乎」「應該」「只有」「仍然」「已經」等限定語被改強或改弱，都算實質問題。
- 技術直覺可以前置，但形式化資訊不可消失；所有重排限於同一原文段落。
- Reviewer 只是報告者，不直接改稿；最終決定由主 Agent 負責。

只要主 Agent 因 ISSUE 做了會影響語意、語氣、技術內容或句子關係的修訂，就再派 reviewer 複查該段，
直到 PASS。純標點或明確筆誤可由主 Agent 自行確認。

## 全章收尾

所有 chunk 完成後：

1. 從頭通讀繁中章節，專看 chunk 邊界：代名詞、重複主詞、時間銜接、語氣與術語是否突然改變，
   以及是否重複介紹同一個技術概念。
2. 不得以「全章更流暢」為由跨原文段落搬資訊。
3. 接縫通讀若造成任何實質修改，將受影響段落連同上下文重新送 Faithfulness Reviewer，直到 PASS。
4. 執行 `uv run tools/check.py chapter N`；所有 ERROR 必須歸零，WARN 要逐項判斷。
5. 執行相關術語搜尋；若動過 bible，再跑 `uv run tools/check.py terms` 並檢查全書影響。
6. 更新 `translation/literary-edit/progress.md`，並在
   `translation/literary-edit/notes/chapter-NN.md` 記錄：範圍、重要裁決、已接受的 reviewer issue、
  尚待人工決定的問題與 check 結果。

一章只有在所有 chunk 與接縫修改都通過 reviewer、沒有未解決 flag，而且機械檢查通過後，才能標成「已完成」。

## 不能由 chunk editor 自行決定的事

- 改固定譯名、角色名、地名、制度名或人物稱謂。
- 精確換算全書既定單位。例如「五公寸」改成「五十公分」在數值上正確、對台灣讀者也更直觀，
  但現有 bible 明定 `decimeter → 公寸`。主 Agent 必須先 flag 並取得使用者明確同意；獲准後才能另行更新
  style guide／worldbuilding 並確認全書用法，不能只改第一章一處。
- 修正疑似原文筆誤或替原文補充解釋。
- 跨段搬移資訊、合併段落或拆分段落。
- 為伏筆增加提示，或用後文揭露去改寫前文的模糊性。
