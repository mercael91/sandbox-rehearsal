from calculator import add, divide, format_price, parse_int, average, multiply, subtract
import pytest

def test_add():
    assert add(2, 3) == 5

def test_multiply():
    assert multiply(2, 3) == 6

def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError, match="Cannot divide by zero"):
        divide(5, 0)

def test_divide_precision():
    assert divide(1, 3) == 0.333333
    assert divide(2, 3) == 0.666667

def test_parse_int():
    assert parse_int("123") == 123
    with pytest.raises(ValueError, match="Invalid input: could not convert string to integer"):
        parse_int("abc")

def test_format_price():
    assert format_price(123.456) == "123.46₽"

def test_format_price_rounding():
    assert format_price(2.675) == "2.68₽"

def test_average():
    assert average([1, 2, 3]) == 2
    assert average((1, 2, 3)) == 2
    with pytest.raises(ValueError, match="Cannot calculate average of an empty list"):
        average([])

def test_subtract():
    assert subtract(5, 3) == 2
    assert subtract(5, -3) == 8
    assert subtract(-5, -3) == -2
