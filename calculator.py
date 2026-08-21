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
    # BUG 2: int() raises on non-numeric input without a message
    return int(text)


def average(values):
    # BUG 3: empty list crashes with ZeroDivisionError
    return sum(values) / len(values)
