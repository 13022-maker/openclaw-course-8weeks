#!/usr/bin/env python3
import argparse, json
from pathlib import Path
import subprocess


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--config", required=True)
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    cfg = json.loads(Path(args.config).read_text(encoding="utf-8"))
    attendance = cfg["attendance"]
    grades = cfg["grades"]
    out = cfg["out"]

    cmd = [
        "python3",
        "../week04/src/build_report.py",
        "--attendance",
        attendance,
        "--grades",
        grades,
        "--out",
        out,
    ]

    if args.dry_run:
        print("DRY RUN:", " ".join(cmd))
        return

    subprocess.check_call(cmd)
    print("Done")


if __name__ == "__main__":
    main()
