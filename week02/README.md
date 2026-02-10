# Week 02｜模板化輸出：小測題庫（JSON）

## 目標
- 用固定 JSON 格式輸出題庫
- 學會基本資料結構設計（list/dict）與輸入驗證

## 範例檔案
- `data/lesson_notes.md`：課堂筆記
- `expected/quiz.json`：題庫範例輸出
- `src/make_quiz.py`：起始骨架

## 作業要求
1) 讀取 `data/lesson_notes.md`
2) 產出 `quiz.json`，格式如下：

```json
{
  "title": "...",
  "questions": [
    {"q": "...", "choices": ["A...","B...","C...","D..."], "answer": 1, "explain": "..."}
  ]
}
```

## 驗收方式
```bash
python3 src/make_quiz.py --in data/lesson_notes.md --out quiz.json
python3 src/validate_quiz.py --in quiz.json
```

## 加分
- 題目數量可用 `--n` 控制
- `validate_quiz.py` 能檢查 choices 長度、answer 範圍
