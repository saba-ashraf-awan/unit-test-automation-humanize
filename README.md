# Assignment 3 – Unit Test Automation for `python-humanize`

**Group members**
| Name | Roll No. | Module work |
|---|---|---|
| Saba Ashraf | 24F-3064 | number (intcomma, intword, ordinal), filesize (decimal/GNU), lists (boundaries, CSV) |
| Maryum Qayyum | 24F-3045 | number (apnumber, fractional, scientific, metric), filesize (binary/negative/invalid), lists (iterable types) |

Project: https://github.com/python-humanize/humanize – library that converts numbers, file sizes and lists to human-readable text.

## 1. Environment setup (Task 1 – record in the setup video)
```bash
git clone https://github.com/python-humanize/humanize.git
cd humanize
python3 -m venv .venv && source .venv/bin/activate      # Windows: .venv\Scripts\activate
pip install -e .
pip install -r assignment/requirements.txt
cd assignment && pytest --version
```
## 2. Repository structure
- `notes/test_design_notes.md` – ECP / BVA / decision-table notes
- `tests/test_saba_{number,filesize,lists}.py` – Saba Ashraf (24F-3064)
- `tests/test_maryum_{number,filesize,lists}.py` – Maryum Qayyum (24F-3045)
- `data/*.csv` – external test data; `Test_Cases.xlsx` – Excel test case sheet (Task 3)
- `pytest.ini`, `conftest.py`, `run_tests.sh` – configuration (Task 4)
- `docs/summary_report.md` – summary report

## 3. Running tests
| Command | Purpose |
|---|---|
| `pytest` | all 117 tests |
| `pytest -m smoke` / `regression` / `boundary` / `ecp` / `datadriven` / `negative` | run one group |
| `pytest -m saba` / `pytest -m maryum` | one member's tests |
| `pytest -n auto --dist loadfile` | parallel (pytest-xdist) |
| `./run_tests.sh parallel` | parallel + HTML report |

Execution order: `@pytest.mark.order(1/2/3)` runs smoke tests of number → filesize → lists first (pytest-order).
Parameterization: `@pytest.mark.parametrize`; CSV-driven tests read `data/*.csv` through `conftest.read_csv`.
