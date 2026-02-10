# Week 01｜課程日誌：把需求寫清楚 + 產出固定格式

## 目標
- 學會用固定格式寫「學習日誌」
- 學會用 Python 讀取文字檔並輸出整理後的 Markdown

## 範例檔案
- `data/learning_log_raw.txt`：原始日誌（亂的）
- `expected/daily_report.md`：目標輸出（範例）
- `src/make_daily_report.py`：起始骨架

## 作業要求
1) 讀取 `data/learning_log_raw.txt`
2) 生成 `daily_report.md`，格式如下：

```md
# 今日學習日報

## TL;DR（3 行）
- ...

## 今日完成
- ...

## 今日卡點
- ...

## 明日計畫
- ...
```

## 驗收方式
- 執行：
  ```bash
  python3 src/make_daily_report.py --in data/learning_log_raw.txt --out daily_report.md
  ```
- `daily_report.md` 格式正確，且內容有從 raw log 萃取出重點。

## 加分
- 支援 `--date` 參數，把日期寫到標題
- 若 raw log 沒有某一段資訊，輸出要顯示「（無）」而不是程式崩潰
