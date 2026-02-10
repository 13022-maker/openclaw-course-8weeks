#!/usr/bin/env python3
import argparse, json


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--in", dest="in_path", required=True)
    ap.add_argument("--out", dest="out_path", required=True)
    ap.add_argument("--n", type=int, default=2)
    args = ap.parse_args()

    _notes = open(args.in_path, "r", encoding="utf-8").read()

    # TODO: 根據 notes 內容，產生 args.n 題選擇題
    quiz = {
        "title": "Python CLI 入門小測",
        "questions": [
            {
                "q": "（請產生題目）",
                "choices": ["A", "B", "C", "D"],
                "answer": 0,
                "explain": "（請填解釋）",
            }
        ],
    }

    open(args.out_path, "w", encoding="utf-8").write(json.dumps(quiz, ensure_ascii=False, indent=2))
    print(f"Wrote: {args.out_path}")


if __name__ == "__main__":
    main()
