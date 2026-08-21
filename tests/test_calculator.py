from calculator import add, divide, format_price, parse_int, average


def test_add():
    assert add(2, 3) == 5


def test_divide_by_zero():
    assert divide(5, 0) == "Cannot divide by zero"


def test_format_price():
    assert format_price(123.456) == "123.46₽"


def test_average():
    assert average([1, 2, 3]) == 2
