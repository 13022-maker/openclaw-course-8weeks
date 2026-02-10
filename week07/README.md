# Week 07｜C++ 小工具 + Python 串接（效能觀念）

## 目標
- 用 C++ 寫一個小工具：讀 stdin、輸出統計結果
- 用 Python 呼叫 C++ 程式並比較執行時間

## 範例檔案
- `data/big_text.txt`：範例文字
- `src/wordcount.cpp`：C++ 起始骨架
- `src/run_cpp.py`：Python 呼叫範例

## 作業要求
1) 編譯：
```bash
clang++ -O2 -std=c++17 src/wordcount.cpp -o wordcount
```
2) 執行：
```bash
cat data/big_text.txt | ./wordcount
```
輸出格式（範例）：
```
lines=...
words=...
bytes=...
```
3) 用 Python `subprocess` 呼叫 `./wordcount`，並印出執行時間

## 加分
- 支援 `--json` 參數輸出 JSON
