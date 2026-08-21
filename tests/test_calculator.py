from calculator import add, divide, format_price, parse_int, average

def test_add():
    assert add(2, 3) == 5

def test_divide_by_zero():
    assert divide(5, 0) == "Cannot divide by zero"

def test_average():
    assert average([1, 2, 3]) == 2

def test_average_empty():
    assert average([]) == 0
