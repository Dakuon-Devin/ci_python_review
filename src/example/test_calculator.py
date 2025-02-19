import pytest
from .calculator import add, subtract, multiply, divide


def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0.1, 0.2) == pytest.approx(0.3)


def test_subtract():
    assert subtract(5, 3) == 2
    assert subtract(1, 1) == 0
    assert subtract(0.3, 0.1) == pytest.approx(0.2)


def test_multiply():
    assert multiply(2, 3) == 6
    assert multiply(-2, 3) == -6
    assert multiply(0.1, 0.2) == pytest.approx(0.02)


def test_divide():
    assert divide(6, 2) == 3.0
    assert divide(5, 2) == 2.5
    assert divide(1, 3) == pytest.approx(0.3333333)


def test_divide_by_zero():
    with pytest.raises(ValueError):
        divide(1, 0)
