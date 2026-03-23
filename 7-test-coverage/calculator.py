def add(a, b):
    """Add two numbers"""
    return a + b


def subtract(a, b):
    """Subtract b from a"""
    return a - b


def multiply(a, b):
    """Multiply two numbers"""
    return a * b


def divide(a, b):
    """Divide a by b"""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


def power(base, exponent):
    """Calculate base raised to exponent"""
    if exponent < 0:
        raise ValueError("Negative exponents not supported")
    return base**exponent


def square_root(n):
    """Calculate square root"""
    if n < 0:
        raise ValueError("Cannot square root negative number")
    return n**0.5


def modulo(a, b):
    """Calculate a modulo b"""
    if b == 0:
        raise ValueError("Cannot modulo by zero")
    return a % b


def is_even(n):
    """Check if number is even"""
    return n % 2 == 0


def is_positive(n):
    """Check if number is positive"""
    return n > 0


def factorial(n):
    """Calculate factorial"""
    if n < 0:
        raise ValueError("Negative factorial not defined")
    if n == 0 or n == 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result
