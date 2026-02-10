# Week 08｜期末整合：校園助教小幫手（專題樣板）

## 目標
- 把前 7 週的能力整合成一個小專案
- 交付可用的 README + Demo

## 範例檔案
- `data/handout.md`：講義
- `expected/output.md`：示例輸出
- `src/assistant_project.py`：起始骨架

## 作業要求（期末專題最小可交付）
輸入：`data/handout.md`
輸出：`output.md`，包含：
- 3 行 TL;DR
- 10 個重點（條列）
- 5 題小測（JSON 或 Markdown 皆可，但格式要固定）

## 驗收
```bash
python3 src/assistant_project.py --in data/handout.md --out output.md
```
