#!/usr/bin/env python3
import subprocess, time


def main():
    # TODO: 確保你已經編譯出 ./wordcount
    start = time.time()
    p = subprocess.run(
        ["./wordcount"],
        input=open("data/big_text.txt", "rb").read(),
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=True,
    )
    elapsed = time.time() - start

    print(p.stdout.decode("utf-8", errors="replace"))
    print(f"elapsed_sec={elapsed:.6f}")


if __name__ == "__main__":
    main()
