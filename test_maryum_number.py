"""humanize.number - apnumber, fractional, scientific, metric.
Owner: Maryum Qayyum (24F-3045)"""
import pytest
import humanize

pytestmark = pytest.mark.maryum


@pytest.mark.smoke
@pytest.mark.order(1)
def test_apnumber_smoke():
    assert humanize.apnumber(5) == "five"

@pytest.mark.boundary
@pytest.mark.regression
@pytest.mark.parametrize("n,exp", [(0, "zero"), (1, "one"), (9, "nine"), (10, "10")])
def test_apnumber_boundaries(n, exp):
    assert humanize.apnumber(n) == exp

@pytest.mark.negative
def test_apnumber_non_numeric_unchanged():
    assert humanize.apnumber("x") == "x"

@pytest.mark.ecp
@pytest.mark.parametrize("v,exp", [(0, "0"), (3, "3"), (0.5, "1/2"), (1.5, "1 1/2")])
def test_fractional(v, exp):
    assert humanize.fractional(v) == exp

@pytest.mark.ecp
@pytest.mark.regression
@pytest.mark.parametrize("v,exp", [(12345, "1.23 x 10⁴"), (0.00012, "1.20 x 10⁻⁴"), (1, "1.00 x 10⁰")])
def test_scientific(v, exp):
    assert humanize.scientific(v) == exp

@pytest.mark.ecp
def test_scientific_custom_precision():
    assert humanize.scientific(12345, 1) == "1.2 x 10⁴"

@pytest.mark.negative
def test_scientific_non_numeric_unchanged():
    assert humanize.scientific("abc") == "abc"

@pytest.mark.boundary
@pytest.mark.parametrize("v,unit,exp", [(1500, "V", "1.50 kV"), (0.0015, "A", "1.50 mA"),
                                        (1, "W", "1.00 W"), (0, "", "0.00")])
def test_metric(v, unit, exp):
    assert humanize.metric(v, unit) == exp

@pytest.mark.ecp
def test_metric_mega_no_unit():
    assert humanize.metric(1e6) == "1.00 M"
