# Contributing

感謝你願意改進這套教材！

## 提交方式
1. Fork 這個 repo
2. 建立分支：`git checkout -b feat/<name>`
3. 修改後提交：`git commit -m "..."`
4. 開 PR（Pull Request）

## 建議規範
- 每週資料夾結構請維持：`README.md / data / expected / src / tests / rubric.md`
- 若更新輸出格式，請同步更新 `expected/`
- 程式請保持可在乾淨環境執行（盡量用標準庫；若需要套件請寫清楚）

## CI
- GitHub Actions 會跑每週的 tests（使用 pytest）。
