"""humanize.filesize - naturalsize (decimal + GNU modes, CSV data).
Owner: Saba Ashraf (24F-3064)"""
import pytest
import humanize
from conftest import read_csv

ROWS = read_csv("filesize_cases.csv")
pytestmark = pytest.mark.saba


@pytest.mark.smoke
@pytest.mark.order(2)
def test_naturalsize_smoke():
    assert humanize.naturalsize(1024) == "1.0 kB"

@pytest.mark.boundary
@pytest.mark.regression
@pytest.mark.parametrize("b,exp", [(0, "0 Bytes"), (1, "1 Byte"), (999, "999 Bytes"),
                                   (1000, "1.0 kB"), (1023, "1.0 kB")])
def test_naturalsize_decimal_boundaries(b, exp):
    assert humanize.naturalsize(b) == exp

@pytest.mark.ecp
@pytest.mark.parametrize("b,exp", [(1, "1B"), (1024, "1.0K"), (3_000_000, "2.9M")])
def test_naturalsize_gnu(b, exp):
    assert humanize.naturalsize(b, gnu=True) == exp

@pytest.mark.ecp
def test_naturalsize_megabyte_decimal():
    assert humanize.naturalsize(1_000_000) == "1.0 MB"

@pytest.mark.ecp
def test_naturalsize_custom_format():
    assert humanize.naturalsize(1536, format="%.2f") == "1.54 kB"

@pytest.mark.datadriven
@pytest.mark.regression
@pytest.mark.parametrize("row", ROWS, ids=[f"{r['bytes']}-b{r['binary']}-g{r['gnu']}" for r in ROWS])
def test_filesize_csv_driven(row):
    out = humanize.naturalsize(int(row["bytes"]), binary=row["binary"] == "True", gnu=row["gnu"] == "True")
    assert out == row["expected"]
