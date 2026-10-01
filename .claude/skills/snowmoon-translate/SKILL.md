---
name: snowmoon-translate
description: Snowmoon 小說翻譯流程的總指揮。依序派 subagent 執行第零階段（建立 bible）、第一階段（文學翻譯）、第二階段（雙語 QA）、第三階段（全書一致性），驗收每個 agent 的產出、管理 agent 的上下文用量與換手、記錄進度並 commit。使用時機：要開始或繼續翻譯 Snowmoon、查看翻譯進度、執行某個階段或某個章節範圍。參數：status | stage0 | stage1 [N-M] | stage2 [N-M] | stage3 [terms|voice|world]；不帶參數則從目前進度繼續。
---

# Snowmoon 翻譯總指揮

你（主 session）是總指揮。你**不翻譯、不審稿、不評論譯文品質**——原則上相信 agent 的翻譯。
你的工作只有：派工、驗收「任務有沒有完成」、決定 agent 要接續還是換手、記錄、commit。

專案根目錄就是這個 repo 的根目錄，所有指令在根目錄執行。

## 流程總覽

| 階段 | agent（subagent_type） | 工作單位 | 產出 | 完成條件 |
|---|---|---|---|---|
| 0 建立 bible | `snowmoon-bible-builder` | 4 章一批 | `translation/{glossary,characters,worldbuilding,synopsis,open-questions}.md` | 5 個檔案都存在；synopsis 有該批每一章 |
| — 使用者決策 | 你自己 | — | open-questions 已決 | 使用者回答完或明確說先用暫定譯名 |
| 1 文學翻譯 | `snowmoon-translator` | 1 章 | `zh-tw/chapter-NN.md`、`translation/notes/chapter-NN.md` | `check.py chapter N` 無 ERROR 且筆記存在 |
| 2 雙語 QA | `snowmoon-qa` | 1 章 | 修正後譯文、`translation/qa/chapter-NN.md` | `check.py chapter N` 無 ERROR 且 QA 紀錄存在 |
| 3 一致性 | `snowmoon-consistency` | 1 個焦點 | `translation/consistency/<焦點>.md` | 報告存在且全書 `check.py chapter` 無 ERROR |

階段三依序執行 `terms` → `voice` → `world`，**每個焦點一個全新的 agent**。
各階段的 agent 彼此獨立：第二階段不接續第一階段的 agent，第三階段也不接續第二階段的。

## 鐵則

1. **不並行。** 同一時間只有一個 agent 在工作。等它的完成通知回來、驗收完，才派下一個工作。
2. **不讀譯文、不提翻譯意見。** 你只看 `check.py` 的結果和 agent 的回報。WARN 不退件（第二階段會處理），
   只有 ERROR 或產出檔案缺漏才退回。
3. **不替 agent 做它的工作。** 驗收失敗就退回給 agent 修，不要自己改譯文。

## 開始時

1. 跑 `uv run tools/check.py status`，確認目前進度。
2. 決定要跑的階段與範圍：
   - 參數 `status`：印出進度與 `translation/log.md` 最後幾筆，結束。
   - 參數指定階段／範圍：照參數。
   - 沒有參數：從最早未完成的階段接續。階段 0 → 1 之間一定要先做「使用者決策」。
3. 載入 `SendMessage`（它是 deferred tool：`ToolSearch` 查詢 `select:SendMessage`），接續 agent 時要用。

## 派工與接續規則（上下文管理）

每個 agent 完成時，完成通知的 usage 會附上 `total_tokens`，這就是該 agent 目前的上下文大小，記為 **T**。

派下一個工作單位（下一章／下一批）時：

| T | 動作 |
|---|---|
| T ≤ 150k | 用 `SendMessage` 把下一個工作單位交給**同一個 agent** |
| 150k < T < 300k | 預估下一單位會再增加 ΔT（見下）；若 T + ΔT ≤ 300k 就接續，否則換新 agent |
| T ≥ 300k | 換新 agent（`Agent` 工具，新的 subagent） |

ΔT 的估法：這個 agent 上一個工作單位讓 T 增加了多少，再乘上「下一章英文詞數 ÷ 上一章英文詞數」。
agent 剛開的第一個單位包含讀 bible 的固定成本，要扣掉：第一單位的增量用 T × 0.6 估即可。
如果通知裡沒有 usage，改用 **每個英文詞 8 tokens ＋ 新 agent 固定成本 40k** 粗估。

**新 agent 的 prompt**（Agent 工具，`subagent_type` 用上表名稱）：

- 階段 0：`處理第 A–B 章。`（最後一批加上 `這是最後一批，完成後做收尾。`）
- 階段 1：`翻譯第 N 章。`
- 階段 2：`QA 第 N 章。`
- 階段 3：`焦點：terms。`（或 voice／world）

**接續的訊息**（SendMessage 給同一個 agent）：

- 階段 0：`接著處理第 A–B 章。`
- 階段 1：`接著翻譯第 N 章。`
- 階段 2：`接著 QA 第 N 章。`

agent 的行為規格都寫在 `.claude/agents/*.md` 裡，prompt 不需要重複說明，也不要夾帶翻譯建議。

## 驗收（每個工作單位完成後）

1. 階段 1／2：跑 `uv run tools/check.py chapter N --max-warn 5`，確認產出檔（筆記或 QA 紀錄）存在。
   階段 0：確認 5 個 bible 檔案存在、`synopsis.md` 有該批每一章的標題（`grep '^## 第' translation/synopsis.md`）。
   階段 3：確認報告存在，並跑 `uv run tools/check.py chapter 1 2 … 32 --max-warn 0`。
2. **通過** → 記錄、commit、派下一個工作單位。
3. **不通過** → 把 ERROR 輸出（或缺少的檔案）原樣交回：
   - 該 agent T < 300k：`SendMessage` 請它修正。
   - 否則開新 agent：`第 N 章已有譯文，但 check 回報以下 ERROR，請修正（不要重譯整章）：<貼上輸出>`。
   - 同一單位最多退回 2 次；第 3 次仍失敗就**停下來向使用者報告**，不要繼續往下。
4. agent 回報無法完成、或回報內容明顯異常（例如說它翻的是別的章）→ 停下來向使用者報告。

## 記錄：`translation/log.md`

檔案不存在就建立，表頭：

```
| 時間 | 階段 | 單位 | agent | 模式 | T（完成時） | 結果 | 備註 |
|---|---|---|---|---|---|---|---|
```

每個工作單位完成（無論成敗）追加一列。模式填「新開」或「接續」；agent 填 agent ID 的前 8 碼。
結果填 PASS／PASS+nW／退回／失敗。

## Commit

每個工作單位通過驗收後 commit 一次（讓進度可回溯、可從中斷處接續）：

```sh
git add zh-tw translation
git commit -m "<訊息>"
```

訊息格式：`bible：第 A–B 章`、`譯：第 N 章`、`QA：第 N 章`、`一致性：<焦點>`、`bible：使用者決策`。
結尾加上 Claude Code 目前規定的 Co-Authored-By 署名行。不要 push。

## 使用者決策（階段 0 完成後、階段 1 開始前）

1. 讀 `translation/open-questions.md`（這是你唯一需要讀的內容檔）。
2. 用 `AskUserQuestion` 把「狀態：待決」的題目問使用者，一次最多 4 題，建議選項放第一個並標 (Recommended)，
   選項說明寫上理由。題目多就分幾輪問。
3. 依回答更新：
   - open-questions.md 該題改為 `狀態：已決`，加一行 `- 決定：<譯法>（使用者，YYYY-MM-DD）`。
   - 對應 bible 詞條的「譯名」改成決定的譯法、刪掉備註的 `【待決】`；若決定和暫用不同，把暫用譯法放進「避免」欄。
4. commit `bible：使用者決策`，然後進入階段 1。

使用者說「先用暫定的」就保留待決狀態直接開始階段 1——之後由第三階段 terms 焦點統一改正。

## 階段之間

- 階段 0 → 1：必須經過使用者決策。
- 階段 1 → 2 → 3：全部章節通過後自動進入下一階段，進入前跑一次 `check.py status` 並用一句話告知使用者。
- 跑完指定範圍或全部完成時，用簡短摘要回報：完成了哪些單位、用了幾個 agent、退回幾次、
  WARN 最多的幾章、第二階段修正數（從 QA 回報加總）、還剩什麼。

## 中斷後繼續

所有進度都能從檔案推回來：`check.py status` 告訴你每一章做到哪裡，`translation/log.md` 告訴你最後發生什麼。
重新呼叫這個 skill 時一律開新 agent（先前的 agent 不會跨 session 保留）。
若發現某章譯文存在但筆記不存在（agent 中途被中斷），把它視為未完成，派新 agent 重新翻譯該章。
