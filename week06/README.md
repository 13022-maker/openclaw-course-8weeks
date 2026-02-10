# Week 06｜軟體工程：錯誤處理 + 日誌 + 可測試

## 目標
- 讓程式在資料缺漏/格式錯誤時，不會直接崩潰
- 加入 logging（印出清楚的錯誤訊息）

## 範例檔案
- `data/bad_grades.csv`：故意做壞的資料
- `src/safe_build_report.py`：起始骨架

## 作業要求
- 讀取 attendance + grades
- 若遇到：缺欄位、分數不是數字，必須：
  1) 印出清楚錯誤訊息
  2) 程式以非 0 結束碼結束（raise SystemExit(1)）

## 驗收
```bash
python3 src/safe_build_report.py --attendance ../week04/data/attendance.csv --grades data/bad_grades.csv --out report.md
# 應該要失敗，但錯誤訊息要清楚
```
