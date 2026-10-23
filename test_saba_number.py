"""humanize.number - intcomma, intword, ordinal.
Owner: Saba Ashraf (24F-3064)"""
import pytest
import humanize
from conftest import read_csv

ROWS = read_csv("number_cases.csv")
FUNCS = {"intcomma": humanize.intcomma, "intword": humanize.intword, "ordinal": humanize.ordinal}
pytestmark = pytest.mark.saba


@pytest.mark.smoke
@pytest.mark.order(1)
def test_intcomma_basic():
    assert humanize.intcomma(1234567) == "1,234,567"

@pytest.mark.boundary
@pytest.mark.regression
@pytest.mark.parametrize("value,expected", [(0, "0"), (999, "999"), (1000, "1,000"), (-1000, "-1,000")])
def test_intcomma_boundaries(value, expected):
    assert humanize.intcomma(value) == expected

@pytest.mark.ecp
def test_intcomma_float_keeps_decimals():
    assert humanize.intcomma(1234.5678) == "1,234.5678"

@pytest.mark.negative
@pytest.mark.parametrize("bad,exp", [("abc", "abc"), (None, "None")])
def test_intcomma_invalid_returned_as_string(bad, exp):
    assert humanize.intcomma(bad) == exp

@pytest.mark.boundary
@pytest.mark.parametrize("value,expected", [(999, "999"), (1000, "1.0 thousand"),
                                            (1_000_000, "1.0 million"), (1_000_000_000, "1.0 billion")])
def test_intword_boundaries(value, expected):
    assert humanize.intword(value) == expected

@pytest.mark.negative
def test_intword_non_numeric():
    assert humanize.intword("abc") == "abc"

@pytest.mark.smoke
@pytest.mark.parametrize("n,exp", [(1, "1st"), (2, "2nd"), (3, "3rd"), (4, "4th")])
def test_ordinal_basic_suffixes(n, exp):
    assert humanize.ordinal(n) == exp

@pytest.mark.boundary
@pytest.mark.parametrize("n,exp", [(11, "11th"), (12, "12th"), (13, "13th"), (111, "111th"), (21, "21st")])
def test_ordinal_teen_exceptions(n, exp):
    assert humanize.ordinal(n) == exp

@pytest.mark.ecp
def test_ordinal_zero():
    assert humanize.ordinal(0) == "0th"

@pytest.mark.datadriven
@pytest.mark.regression
@pytest.mark.parametrize("row", ROWS, ids=[f"{r['func']}-{r['input']}" for r in ROWS])
def test_number_csv_driven(row):
    assert str(FUNCS[row["func"]](int(row["input"]))) == row["expected"]
