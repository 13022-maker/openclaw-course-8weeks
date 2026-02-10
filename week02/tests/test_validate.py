import subprocess

def test_validator_on_expected():
    subprocess.check_call(["python3", "src/validate_quiz.py", "--in", "expected/quiz.json"])
