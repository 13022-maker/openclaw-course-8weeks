from pathlib import Path

def test_expected():
    assert Path('expected/report.md').exists()
