import subprocess
from pathlib import Path

def test_runs(tmp_path: Path):
    out = tmp_path / "weekly.md"
    subprocess.check_call(["python3", "src/weekly_summary.py", "--in", "data/notes", "--out", str(out)])
    assert out.exists()
