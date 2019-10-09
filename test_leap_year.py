import pytest
from leap_year import leap_year


def test_leap_year_expect_true() -> None:
    assert leap_year(2000)


def test_leap_year_expect_false() -> None:
    assert not leap_year(2001)


def test_leap_year_expect_exception_with_message() -> None:
    with pytest.raises(TypeError, match='Please provide proper year value'):
        leap_year('1234')
