#!/usr/bin/env python3
import argparse


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--in", dest="in_path", required=True)
    ap.add_argument("--out", dest="out_path", required=True)
    args = ap.parse_args()

    raw = open(args.in_path, "r", encoding="utf-8").read()

    # TODO: 解析 raw 內容，萃取：TL;DR、今日完成、今日卡點、明日計畫
    # 提示：你可以用 splitlines() + 關鍵字判斷

    report = """# 今日學習日報

## TL;DR（3 行）
- （請從 raw log 萃取）

## 今日完成
- （請從 raw log 萃取）

## 今日卡點
- （請從 raw log 萃取）

## 明日計畫
- （請從 raw log 萃取）
"""

    open(args.out_path, "w", encoding="utf-8").write(report)
    print(f"Wrote: {args.out_path}")


if __name__ == "__main__":
    main()
