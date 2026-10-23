import csv
from pathlib import Path

DATA = Path(__file__).parent / "data"


def read_csv(name):
    with open(DATA / name, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def pytest_configure(config):
    for m in ("smoke", "regression", "boundary", "ecp", "datadriven", "negative", "saba", "maryum"):
        config.addinivalue_line("markers", f"{m}: {m} group")
