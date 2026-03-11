from typing import Union

Number = Union[int, float]


class Calculator:
    """A simple calculator supporting basic arithmetic operations."""

    def add(self, a: Number, b: Number) -> Number:
        return a + b

    def subtract(self, a: Number, b: Number) -> Number:
        return a - b

    def multiply(self, a: Number, b: Number) -> Number:
        return a * b

    def divide(self, a: Number, b: Number) -> float:
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            raise TypeError("Operands must be numeric")
        if b == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        return a / b

    def __repr__(self) -> str:
        return "Calculator()"