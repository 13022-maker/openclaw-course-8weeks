#!/usr/bin/env python3
import argparse, json


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--in", dest="in_path", required=True)
    args = ap.parse_args()

    obj = json.loads(open(args.in_path, "r", encoding="utf-8").read())
    assert isinstance(obj.get("title"), str)
    qs = obj.get("questions")
    assert isinstance(qs, list) and len(qs) > 0

    for i, q in enumerate(qs):
        assert isinstance(q.get("q"), str) and q["q"].strip()
        choices = q.get("choices")
        assert isinstance(choices, list) and len(choices) == 4
        ans = q.get("answer")
        assert isinstance(ans, int) and 0 <= ans < 4
        assert isinstance(q.get("explain"), str)

    print("OK")


if __name__ == "__main__":
    main()
