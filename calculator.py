"""Simple calculator with intentional bugs for rehearsal."""

def add(a, b):
    return a + b


def divide(a, b):
    if b == 0:
        return "Cannot divide by zero"
    return a / b


def format_price(amount):
    return f"{amount:.2f}₽"


def parse_int(text):
    try:
        return int(text)
    except ValueError:
        raise ValueError("Invalid input: could not convert string to integer") from None


def average(values):
    # BUG 3: empty list crashes with ZeroDivisionError
    if not values:
        raise ValueError("Cannot calculate average of an empty list")
    return sum(values) / len(values)
