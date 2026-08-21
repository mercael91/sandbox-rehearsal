from calculator import add, divide, format_price, parse_int, average
import pytest

def test_add():
    assert add(2, 3) == 5

def test_divide_by_zero():
    assert divide(5, 0) == "Cannot divide by zero"

def test_parse_int():
    assert parse_int("123") == 123
    with pytest.raises(ValueError, match="Invalid input: could not convert string to integer"):
        parse_int("abc")

def test_average():
    assert average([1, 2, 3]) == 2
    with pytest.raises(ValueError, match="Cannot calculate average of an empty list"):
        average([])
