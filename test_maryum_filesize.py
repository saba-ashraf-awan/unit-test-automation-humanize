"""humanize.filesize - naturalsize (binary mode, negatives, invalid input).
Owner: Maryum Qayyum (24F-3045)"""
import pytest
import humanize

pytestmark = pytest.mark.maryum


@pytest.mark.smoke
@pytest.mark.order(2)
def test_naturalsize_binary_smoke():
    assert humanize.naturalsize(1024, binary=True) == "1.0 KiB"

@pytest.mark.boundary
@pytest.mark.regression
@pytest.mark.parametrize("b,exp", [(1023, "1023 Bytes"), (1024, "1.0 KiB"), (1048576, "1.0 MiB"),
                                   (1073741824, "1.0 GiB")])
def test_naturalsize_binary_boundaries(b, exp):
    assert humanize.naturalsize(b, binary=True) == exp

@pytest.mark.ecp
@pytest.mark.parametrize("b,exp", [(0, "0 Bytes"), (1, "1 Byte")])
def test_naturalsize_binary_small_values(b, exp):
    assert humanize.naturalsize(b, binary=True) == exp

@pytest.mark.negative
@pytest.mark.parametrize("b,exp", [(-1024, "-1.0 kB"), (-1, "-1 Byte")])
def test_naturalsize_negative(b, exp):
    assert humanize.naturalsize(b) == exp

@pytest.mark.negative
def test_naturalsize_negative_binary():
    assert humanize.naturalsize(-1024, binary=True) == "-1.0 KiB"

@pytest.mark.negative
def test_naturalsize_invalid_string_raises():
    with pytest.raises((ValueError, TypeError)):
        humanize.naturalsize("abc")

@pytest.mark.ecp
def test_naturalsize_accepts_numeric_string():
    assert humanize.naturalsize("1024") == "1.0 kB"

@pytest.mark.regression
def test_naturalsize_binary_and_gnu_together():
    assert humanize.naturalsize(1024, binary=True, gnu=True) == "1.0K"
