# Snowmoon 台灣繁中翻譯

Vitalik Buterin 小說《Snowmoon》（GPL v3）的社群翻譯。結構與流程見 README.md。

- 翻譯流程由 `/snowmoon-translate` skill 指揮，各階段 agent 定義在 `.claude/agents/`。
- 翻譯標準：`translation/style-guide.md`；專有名詞以 `translation/` 下的 glossary、characters、worldbuilding 為準。
- `zh-tw/chapter-NN.md` 與 `source/en/chapter-NN.md` 段落一對一，HTML 標籤一字不動；改完跑 `uv run tools/check.py chapter N`。
- `original/`、`source/en/` 不可手動修改（source/en 只能由 `tools/html2md.py` 重新產生）。
- 三個階段已全部完成（見 README「目前狀態」）。之後的人工校稿直接改 `zh-tw/`，不必再走 `/snowmoon-translate`；改完跑該章 `check.py chapter N`。
- 要改譯名：先改 bible（glossary／characters／worldbuilding），再全書搜尋替換，最後跑 `check.py terms` 與 `check.py chapter 1 … 32`。不要只改單章。
- 原作授權要求公開衍生作品的製作流程：prompt、腳本、術語表都要留在 repo 裡，不要放到 repo 外。
