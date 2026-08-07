import pytest
from calc import add, subtract, divide

def test_add():
    assert add(2, 3) == 5
    assert add(-2, 2) == 0

def test_subtract():
    assert subtract(10, 4) == 6
    assert subtract(3, 5) == -2

def test_divide():
    assert divide(10, 2) == 5
    assert divide(5, 2) == 2.5

def test_divide_by_zero():
    with pytest.raises(ValueError):
        divide(10, 0)