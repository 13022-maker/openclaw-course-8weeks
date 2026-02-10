#!/usr/bin/env python3
import argparse, csv, sys


def die(msg: str):
    print(f"[ERROR] {msg}", file=sys.stderr)
    raise SystemExit(1)


def read_csv(path):
    try:
        with open(path, "r", encoding="utf-8") as f:
            return list(csv.DictReader(f))
    except FileNotFoundError:
        die(f"找不到檔案：{path}")


def to_int(val, field, row_hint=""):
    try:
        return int(val)
    except Exception:
        die(f"欄位 {field} 應為數字，但讀到 '{val}'。{row_hint}")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--attendance", required=True)
    ap.add_argument("--grades", required=True)
    ap.add_argument("--out", required=True)
    args = ap.parse_args()

    att = read_csv(args.attendance)
    grd = read_csv(args.grades)

    # TODO: 檢查必要欄位是否存在（student_id/name）
    # TODO: 轉換分數欄位為 int，若失敗要 die()

    out = "# 校園週報（安全版）\n\n（請完成作業要求後輸出）\n"
    open(args.out, "w", encoding="utf-8").write(out)
    print(f"Wrote: {args.out}")


if __name__ == "__main__":
    main()
