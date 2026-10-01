# Snowmoon 台灣繁中翻譯

Vitalik Buterin 小說《Snowmoon》（GPL v3）的社群翻譯。README.md 是給讀者看的；目錄結構與翻譯流程見 TRANSLATION.md，修正建議的規則見 CONTRIBUTING.md。

- 翻譯流程由 `/snowmoon-translate` skill 指揮，各階段 agent 定義在 `.claude/agents/`。
- 翻譯標準：`translation/style-guide.md`；專有名詞以 `translation/` 下的 glossary、characters、worldbuilding 為準。
- `zh-tw/chapter-NN.md` 與 `source/en/chapter-NN.md` 依錨點（標題、HTML 區塊、分隔線、`>` 引言、清單）對齊，HTML 標籤一字不動；錨點之間的散文段在第二輪文學編輯可拆段、合段（初譯為段落一對一）。改完跑 `uv run tools/check.py chapter N`。
- `original/`、`source/en/` 不可手動修改（source/en 只能由 `tools/html2md.py` 重新產生）。`zh-tw-v1/` 是凍結的初譯快照，也不可修改；所有修訂都改 `zh-tw/`。
- 三個階段已全部完成（見 TRANSLATION.md「概況」）。之後的人工校稿直接改 `zh-tw/`，不必再走 `/snowmoon-translate`；改完跑該章 `check.py chapter N`。
- 若工作是第二輪「小說化／文學編輯」，改走 `translation/literary-edit/WORKFLOW.md`，依序使用
  Literary Editor 與 Faithfulness Reviewer；不要重用已結束的 `/snowmoon-translate`，也不要讓 subagent 直接寫正文。
- 要改譯名：先改 bible（glossary／characters／worldbuilding），再全書搜尋替換，最後跑 `check.py terms` 與 `check.py chapter 1 … 32`。不要只改單章。
- 原作授權要求公開衍生作品的製作流程：prompt、腳本、術語表都要留在 repo 裡，不要放到 repo 外。
