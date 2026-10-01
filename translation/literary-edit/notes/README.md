# 章節編輯紀錄

每章兩個檔案：

- `chapter-NN.bible.md`：開工前由主 Agent 建立的 bible 摘錄（全章固定用詞、本章譯名、人物口吻、伏筆邊界），
  每個 chunk 的資料包都附上（`tools/literary_edit.py packet --bible`）。
- `chapter-NN.md`：編輯紀錄，記錄：

- 實際處理的 chunk 與段落 ID
- Literary Editor flags
- Faithfulness Reviewer issues 與主 Agent 裁決
- 補畫面的位置
- 待人工決定事項
- 章節接縫檢查與 `check.py` 結果

這裡只記非顯而易見的決定，不逐句列出一般措辭修改。
