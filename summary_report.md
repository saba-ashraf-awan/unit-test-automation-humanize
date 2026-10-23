# Summary Report – Assignment 3
Group: Saba Ashraf (24F-3064), Maryum Qayyum (24F-3045)
Project: python-humanize (modules: number, filesize, lists)

## Work done
- Task 1: Cloned the project, created a virtualenv, installed dependencies, recorded setup video.
- Task 2: Applied ECP, BVA, decision table and error guessing (notes/test_design_notes.md). Wrote 117 automated pytest tests (Saba 75, Maryum 42 test runs incl. parametrized cases).
- Task 3: Test_Cases.xlsx (14 documented cases) + 3 CSV files feeding data-driven tests.
- Task 4: pytest.ini markers for groups, pytest-xdist for parallel runs, pytest-order for execution order, parametrization throughout.

## Results
All 117 tests pass in sequential and parallel mode (~0.2 s / ~2 s).
Observation: `intcomma(None)` returns the string "None" rather than None.
Tools: Python 3.12, pytest, pytest-xdist, pytest-order, pytest-html, openpyxl.
