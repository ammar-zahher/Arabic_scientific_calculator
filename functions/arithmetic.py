"""
=========================================================
File: arithmetic.py
Folder: functions
=========================================================

Basic arithmetic operations for the calculator.

This file is independent of:

- Tokenizer
- Parser
- Expression Tree
- Evaluator
- Arabic language
- User Interface (UI)

This file does not contain expression parsing logic.
Its sole function is to execute basic arithmetic operations.
=========================================================
"""

# =========================================================
# Addition
# =========================================================

def add(a, b):
    """
Add two numbers.

Examples
--------
add(2, 3) -> 5
add(2.5, 1.5) -> 4.0
"""

    return a + b


# =========================================================
# Subtraction
# =========================================================

def subtract(a, b):
    """
Subtract the second number from the first number.

Examples
--------
subtract(5, 2) -> 3
subtract(2, 5) -> -3
"""
    return a - b


# =========================================================
# Multiplication
# =========================================================

def multiply(a, b):
    """
Multiply two numbers.

Examples
--------
multiply(3, 4) -> 12
multiply(2.5, 4) -> 10.0
"""

    return a * b


# =========================================================
# Division
# =========================================================

def divide(a, b):
    """
Divide the first number by the second number.

If the denominator is zero, Python raises
a ZeroDivisionError.

Examples
--------
divide(10, 2) -> 5.0
divide(5, 2) -> 2.5
"""
    return a / b


# =========================================================
# Modulo
# =========================================================

def modulo(a, b):
    """
Find the remainder of dividing the first number by the second number.

Examples
--------
modulo(10, 3) -> 1
modulo(20, 5) -> 0
"""

    return a % b
