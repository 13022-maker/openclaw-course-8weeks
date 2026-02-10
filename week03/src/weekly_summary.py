#!/usr/bin/env python3
import argparse
from pathlib import Path


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--in", dest="in_dir", required=True)
    ap.add_argument("--out", dest="out_path", required=True)
    ap.add_argument("--max", type=int, default=50)
    args = ap.parse_args()

    in_dir = Path(args.in_dir)
    files = sorted(in_dir.glob("*.md"))[: args.max]

    titles = []
    summaries = []
    total_chars = 0

    for p in files:
        text = p.read_text(encoding="utf-8")
        total_chars += len(text)
        # TODO: 擷取標題（第一個 # 開頭）與第一段摘要
        titles.append(p.stem)
        summaries.append((p.stem, "（請擷取第一段）"))

    out = ["# 週摘要", "", "## 本週筆記"]
    for t in titles:
        out.append(f"- {t}")
    out += ["", "## 統計", f"- 篇數：{len(files)}", f"- 總字數：約 {total_chars}", "", "## 每篇摘要"]
    for t, s in summaries:
        out += [f"### {t}", s, ""]

    Path(args.out_path).write_text("\n".join(out), encoding="utf-8")
    print(f"Wrote: {args.out_path}")


if __name__ == "__main__":
    main()
