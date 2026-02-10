#!/usr/bin/env python3
import argparse, csv


def read_csv(path):
    with open(path, "r", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--attendance", required=True)
    ap.add_argument("--grades", required=True)
    ap.add_argument("--out", required=True)
    args = ap.parse_args()

    att = read_csv(args.attendance)
    grd = read_csv(args.grades)

    # TODO: 計算出席率與缺席排名
    # TODO: 計算平均分與補救名單

    out = """# 校園週報

## 出席
- 全班平均出席率：（待計算）
- 缺席最多前三名：（待計算）

## 成績
- 全班平均分：（待計算）
- 需要補救（<60）：（待計算）
"""

    open(args.out, "w", encoding="utf-8").write(out)
    print(f"Wrote: {args.out}")


if __name__ == "__main__":
    main()
