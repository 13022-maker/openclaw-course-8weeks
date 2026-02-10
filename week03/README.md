# Week 03｜資料整理：把多份筆記整理成週摘要

## 目標
- 讀取資料夾中的多個 Markdown 檔
- 輸出一份「週摘要」Markdown（含統計）

## 範例檔案
- `data/notes/`：多份筆記
- `expected/weekly_summary.md`：範例輸出
- `src/weekly_summary.py`：起始骨架

## 作業要求
1) 讀取 `data/notes/*.md`
2) 產出 `weekly_summary.md`：
- 列出每篇筆記的標題
- 統計總字數
- 擷取每篇的第一段當摘要

## 驗收
```bash
python3 src/weekly_summary.py --in data/notes --out weekly_summary.md
```

## 加分
- 支援只摘要最近 N 篇（`--max`）
