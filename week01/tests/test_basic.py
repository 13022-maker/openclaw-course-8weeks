import subprocess
from pathlib import Path


def test_runs(tmp_path: Path):
    out = tmp_path / "daily_report.md"
    subprocess.check_call([
        "python3",
        "src/make_daily_report.py",
        "--in",
        "data/learning_log_raw.txt",
        "--out",
        str(out),
    ])
    text = out.read_text(encoding="utf-8")
    assert "# 今日學習日報" in text
