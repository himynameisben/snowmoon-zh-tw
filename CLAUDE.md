# Snowmoon 台灣繁中翻譯

Vitalik Buterin 小說《Snowmoon》（GPL v3）的社群翻譯。README.md 是給讀者看的；目錄結構與翻譯流程見 TRANSLATION.md，修正建議的規則見 CONTRIBUTING.md。

- 翻譯流程由 `/snowmoon-translate` skill 指揮，各階段 agent 定義在 `.claude/agents/`。
- 翻譯標準：`translation/style-guide.md`；專有名詞以 `translation/` 下的 glossary、characters、worldbuilding 為準。
- `zh-tw/chapter-NN.md` 與 `source/en/chapter-NN.md` 依錨點（標題、HTML 區塊、分隔線、`>` 引言、清單）對齊，HTML 標籤一字不動；錨點之間的散文段在第二輪文學編輯可拆段、合段（初譯為段落一對一）。改完跑 `uv run tools/check.py chapter N`。
- 裝置畫面（`class="device-view"`）在已轉圖的章節（目前第 1–20、22、23、30、31 章）是 `<img>`：要改文字就改 `zh-tw/devices/chNN-KK.html`，再跑 `uv run tools/render_devices.py N` 重新產圖與 alt，不要直接改章節檔裡的 `<img>`。
- `original/`、`source/en/` 不可手動修改（source/en 只能由 `tools/html2md.py` 重新產生）。`zh-tw-v1/` 是凍結的初譯快照，也不可修改；所有修訂都改 `zh-tw/`。
- 譯本分兩輪：第一輪 v1 初譯（`/snowmoon-translate` 的三個階段，已全部完成、凍結在 `zh-tw-v1/`）；第二輪 v2 ＝ 逐章 AI 文學編輯＋人工校稿（見 TRANSLATION.md「翻譯流程」）。人工校稿直接改 `zh-tw/`，改完跑該章 `check.py chapter N`。
- 章節進度記在 `translation/literary-edit/progress.md`，README 的「目錄與翻譯進度」表同步更新（「版本」「人工校稿」兩欄）。
- 若工作是第二輪「小說化／文學編輯」，用 `/snowmoon-literary-edit N` skill（含裝置畫面轉圖），流程本體是 `translation/literary-edit/WORKFLOW.md`，依序使用
  Literary Editor 與 Faithfulness Reviewer；不要重用已結束的 `/snowmoon-translate`，也不要讓 subagent 直接寫正文。
- 要改譯名：先改 bible（glossary／characters／worldbuilding），再全書搜尋替換，最後跑 `check.py terms` 與 `check.py chapter 1 … 32`。不要只改單章。
- 原作授權要求公開衍生作品的製作流程：prompt、腳本、術語表都要留在 repo 裡，不要放到 repo 外。
