"""Simple calculator with intentional bugs for rehearsal."""

from decimal import Decimal, ROUND_HALF_UP

def add(a, b):
    return a + b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return round(a / b, 6)

def subtract(a, b):
    return a - b


def format_price(amount):
    value = Decimal(str(amount)).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
    return f"{value:.2f}₽"


def parse_int(text):
    if isinstance(text, str):
        text = text.strip()
    try:
        return int(text)
    except ValueError:
        raise ValueError("Invalid input: could not convert string to integer") from None


def average(values):
    # Convert to list to support any iterable input.
    values = list(values)
    if not values:
        raise ValueError("Cannot calculate average of an empty list")
    return sum(values) / len(values)