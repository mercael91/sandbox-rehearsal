"""Simple calculator with intentional bugs for rehearsal."""

def add(a, b):
    return a + b


def divide(a, b):
    if b == 0:
        return "Cannot divide by zero"
    return a / b


def format_price(amount):
    # BUG 1: typo VAHCAR-like — returns "RU" instead of currency symbol
    return f"{amount:.2f} RU"


def parse_int(text):
    # BUG 2: int() raises on non-numeric input without a message
    return int(text)


def average(values):
    # BUG 3: empty list crashes with ZeroDivisionError
    if not values:
        return 0
    return sum(values) / len(values)
