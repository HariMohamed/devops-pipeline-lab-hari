import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
from src.cal import Calculator


@pytest.fixture
def calc():
    """Create a fresh calculator instance for each test."""
    return Calculator()


# ---------- ADD ----------
@pytest.mark.parametrize(
    "a,b,expected",
    [
        (2, 3, 5),
        (-2, 3, 1),
        (2.5, 3.5, 6.0),
        (0, 0, 0),
    ],
)
def test_add(calc, a, b, expected):
    assert calc.add(a, b) == expected


# ---------- SUBTRACT ----------
@pytest.mark.parametrize(
    "a,b,expected",
    [
        (5, 2, 3),
        (2, 5, -3),
        (5.5, 2.5, 3.0),
    ],
)
def test_subtract(calc, a, b, expected):
    assert calc.subtract(a, b) == expected


# ---------- MULTIPLY ----------
@pytest.mark.parametrize(
    "a,b,expected",
    [
        (4, 3, 12),
        (-4, 3, -12),
        (2.5, 2, 5.0),
        (0, 100, 0),
    ],
)
def test_multiply(calc, a, b, expected):
    assert calc.multiply(a, b) == expected


# ---------- DIVIDE ----------
@pytest.mark.parametrize(
    "a,b,expected",
    [
        (10, 2, 5),
        (9, 3, 3),
        (7.5, 2.5, 3),
    ],
)
def test_divide(calc, a, b, expected):
    assert calc.divide(a, b) == expected


# ---------- DIVIDE BY ZERO ----------
def test_divide_by_zero(calc):
    with pytest.raises(ZeroDivisionError, match="Cannot divide by zero"):
        calc.divide(5, 0)


# ---------- TYPE ERROR ----------
@pytest.mark.parametrize(
    "a,b",
    [
        ("a", 2),
        (2, "b"),
        ("a", "b"),
    ],
)
def test_divide_type_error(calc, a, b):
    with pytest.raises(TypeError):
        calc.divide(a, b)


# ---------- REPR ----------
def test_repr(calc):
    assert repr(calc) == "Calculator()"