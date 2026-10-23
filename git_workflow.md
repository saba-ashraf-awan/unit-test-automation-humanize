# Git workflow (so commit history shows each member's work)
Each member commits ONLY her own files from her own account:
```bash
# Saba
git add assignment/tests/test_saba_*.py && git commit -m "Saba: unit tests for number/filesize/lists"
# Maryum
git add assignment/tests/test_maryum_*.py && git commit -m "Maryum: unit tests for number/filesize/lists"
```
Suggested split of other files: Saba – notes, CSV data, README; Maryum – Test_Cases.xlsx, pytest.ini/conftest/run_tests.sh, summary report.
Make several small commits instead of one big one.
