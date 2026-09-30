# Snowmoon 台灣繁中翻譯

Vitalik Buterin 小說《Snowmoon》（GPL v3）的社群翻譯。結構與流程見 README.md。

- 翻譯流程由 `/snowmoon-translate` skill 指揮，各階段 agent 定義在 `.claude/agents/`。
- 翻譯標準：`translation/style-guide.md`；專有名詞以 `translation/` 下的 glossary、characters、worldbuilding 為準。
- `zh-tw/chapter-NN.md` 與 `source/en/chapter-NN.md` 段落一對一，HTML 標籤一字不動；改完跑 `uv run tools/check.py chapter N`。
- `original/`、`source/en/` 不可手動修改（source/en 只能由 `tools/html2md.py` 重新產生）。
- 原作授權要求公開衍生作品的製作流程：prompt、腳本、術語表都要留在 repo 裡，不要放到 repo 外。
