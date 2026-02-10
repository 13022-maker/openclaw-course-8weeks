#!/usr/bin/env python3
import argparse
from pathlib import Path


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--in", dest="in_path", required=True)
    ap.add_argument("--out", dest="out_path", required=True)
    args = ap.parse_args()

    text = Path(args.in_path).read_text(encoding="utf-8")

    # TODO: 解析講義，輸出 TL;DR、重點、與小測（固定格式）
    out = """# 校園助教小幫手輸出

## TL;DR
- （3 行）

## 10 個重點
- （條列）

## 小測
1) （題目）
"""

    Path(args.out_path).write_text(out, encoding="utf-8")
    print(f"Wrote: {args.out_path}")


if __name__ == "__main__":
    main()
