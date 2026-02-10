# Week 05｜自動化：每週固定產出報表（模擬排程）

## 目標
- 學會把工作流程包成一個 "一鍵執行" 的腳本
- 了解排程（cron）的概念（本週先用模擬，不需要真的設 cron）

## 範例檔案
- `data/config.json`：設定檔（輸入檔路徑、輸出路徑）
- `src/run_weekly_job.py`：主程式

## 作業要求
- 讀取 `data/config.json`
- 自動執行 Week04 的報表產生流程（你可以直接 import Week04 的程式，或複製邏輯）
- 產出 `weekly_report.md`

## 驗收
```bash
python3 src/run_weekly_job.py --config data/config.json
```

## 加分
- 支援 `--dry-run`（只印出會做什麼，不真的寫檔）
