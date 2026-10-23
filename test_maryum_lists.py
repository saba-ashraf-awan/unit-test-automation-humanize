"""humanize.lists - natural_list (iterable types, formatting rules).
Owner: Maryum Qayyum (24F-3045)"""
import pytest
import humanize

pytestmark = pytest.mark.maryum


@pytest.mark.smoke
@pytest.mark.order(3)
def test_natural_list_two_items_smoke():
    assert humanize.natural_list(["red", "blue"]) == "red and blue"

@pytest.mark.ecp
def test_natural_list_accepts_generator():
    assert humanize.natural_list(i for i in "abc") == "a, b and c"

@pytest.mark.ecp
def test_natural_list_accepts_range():
    assert humanize.natural_list(range(4)) == "0, 1, 2 and 3"

@pytest.mark.ecp
def test_natural_list_accepts_tuple():
    assert humanize.natural_list(("x", "y")) == "x and y"

@pytest.mark.ecp
def test_natural_list_accepts_single_item_set():
    assert humanize.natural_list({"only"}) == "only"

@pytest.mark.regression
def test_natural_list_no_oxford_comma():
    assert ", and" not in humanize.natural_list(["a", "b", "c", "d"])

@pytest.mark.regression
@pytest.mark.boundary
@pytest.mark.parametrize("items,exp", [([], ""), (["solo"], "solo")])
def test_natural_list_zero_and_one(items, exp):
    assert humanize.natural_list(items) == exp

@pytest.mark.negative
def test_natural_list_mixed_types():
    assert humanize.natural_list([1, "two", 3.0]) == "1, two and 3.0"
