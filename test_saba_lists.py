"""humanize.lists - natural_list (length boundaries, CSV data).
Owner: Saba Ashraf (24F-3064)"""
import pytest
import humanize
from conftest import read_csv

ROWS = read_csv("lists_cases.csv")
pytestmark = pytest.mark.saba


@pytest.mark.smoke
@pytest.mark.order(3)
def test_natural_list_smoke():
    assert humanize.natural_list(["a", "b", "c"]) == "a, b and c"

@pytest.mark.boundary
@pytest.mark.regression
@pytest.mark.parametrize("items,exp", [([], ""), (["x"], "x"), (["a", "b"], "a and b"),
                                       (["a", "b", "c"], "a, b and c")])
def test_natural_list_length_boundaries(items, exp):
    assert humanize.natural_list(items) == exp

@pytest.mark.ecp
def test_natural_list_non_string_items():
    assert humanize.natural_list([1, 2, 3]) == "1, 2 and 3"

@pytest.mark.ecp
def test_natural_list_five_items():
    assert humanize.natural_list(list("abcde")) == "a, b, c, d and e"

@pytest.mark.negative
def test_natural_list_none_raises():
    with pytest.raises(TypeError):
        humanize.natural_list(None)

@pytest.mark.datadriven
@pytest.mark.regression
@pytest.mark.parametrize("row", ROWS, ids=[f"len{len(r['items'].split('|')) if r['items'] else 0}" for r in ROWS])
def test_lists_csv_driven(row):
    items = row["items"].split("|") if row["items"] else []
    assert humanize.natural_list(items) == row["expected"]
