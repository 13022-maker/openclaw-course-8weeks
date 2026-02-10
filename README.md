# OpenClaw 校園 AI×軟工工作坊（8 週）

給高中/高職「正在學程式設計」學生的作業素材包（繁體中文、校園情境）。

- 主軸：AI 應用 × 軟體工程（可驗收、可重現、可交付）
- 語言：Python 為主；C++ 作為工具/效能與系統觀念補充

---

## 快速開始（學生）
1) 進入當週資料夾（例：Week01）
```bash
cd week01
```

2) 照 README 執行（例：Week01）
```bash
python3 src/make_daily_report.py --in data/learning_log_raw.txt --out daily_report.md
```

3) 對照 `expected/` 確認輸出格式

（可選）跑測試
```bash
python3 -m pip install pytest
python3 -m pytest -q
```

---

## 每週內容導覽
- Week01：課程日誌（固定格式輸出）
- Week02：模板化輸出（題庫 JSON + 驗證器）
- Week03：多檔筆記 → 週摘要（批次處理）
- Week04：CSV 報表（出席 + 成績）
- Week05：自動化 Job（讀 config.json 一鍵產生週報）
- Week06：軟體工程（錯誤處理 + 可觀測）
- Week07：C++ 小工具 + Python 串接（效能觀念）
- Week08：期末整合（校園助教小幫手樣板）

> 注意：CI（GitHub Actions）目前會跑 week01/02/03/04/05/06/08 的 tests；Week07 因需編譯 C++，預設不在 CI。

---

## 作業資料夾結構（每週固定）
每週都包含：
- `README.md`：作業目標、步驟、驗收標準
- `data/`：範例輸入檔案
- `expected/`：範例輸出（對照用）
- `src/`：起始骨架程式
- `tests/`：測試/驗證腳本
- `rubric.md`：評分重點

---

## 教師資源（Teacher Pack）
如果你有拿到老師包（投影片大綱/解答/期末評分表），可放在本 repo 的 `teacher/`（本 repo 目前未包含老師包，以避免學生直接看到解答）。

---

## Teacher Pack（私有）
- Teacher Pack（投影片大綱、解答、評分表、老師講義）已獨立為私有 repo，避免學生直接取得解答。
- 如需存取，請由課程教師/助教向維護者申請權限。
- Repo：https://github.com/13022-maker/openclaw-course-8weeks-teacher（需要權限）

## License
MIT（見 `LICENSE`）
