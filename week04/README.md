# Week 04｜校園資料報表：出席 + 成績

## 目標
- 讀取 CSV
- 計算指標（出席率、平均分數）
- 產出一份 Markdown 報表

## 範例檔案
- `data/attendance.csv`
- `data/grades.csv`
- `expected/report.md`
- `src/build_report.py`

## 作業要求
- 產出 `report.md`，包含：
  - 全班平均出席率
  - 缺席次數最多的前三名
  - 全班平均分
  - 需要補救（<60）的名單

## 驗收
```bash
python3 src/build_report.py --attendance data/attendance.csv --grades data/grades.csv --out report.md
```
