"""
=========================================================
File: complex_numbers.py
Folder: functions
=========================================================

Complex number operations in the scientific calculator.

This file is independent of:

- Tokenizer
- Parser
- Expression Tree
- Evaluator
- Arabic language
- User Interface (UI)

Supports:

- Creating complex numbers
- Addition
- Subtraction
- Multiplication
- Division
- Power

Imaginary unit:

    I = sqrt(-1)

In Python, the imaginary unit is represented using:

    1j

However, the core uses the internal symbol:

    I

And this file is only responsible for the mathematical implementation.
=========================================================
"""


# =========================================================
# Complex Conversion
# =========================================================

def to_complex(value):
    """
Convert the value to a complex number.

Parameters
----------
value:
    A real or complex numerical value.

Returns
-------
complex
    The value as a complex number.

Examples
--------
to_complex(5) -> (5+0j)
to_complex(2.5) -> (2.5+0j)
to_complex(3 + 4j) -> (3+4j)
"""

    return complex(value)


# =========================================================
# Addition
# =========================================================

def complex_add(a, b):
    """
Add two real or complex numbers.

Examples
--------
complex_add(2, 3) -> (5+0j)
complex_add(2 + 3j, 4 + 5j) -> (6+8j)
"""

    return complex(a) + complex(b)


# =========================================================
# Subtraction
# =========================================================

def complex_subtract(a, b):
    """
Subtract the second number from the first number.

Examples
--------
complex_subtract(5, 2) -> (3+0j)
complex_subtract(2 + 3j, 1 + 2j) -> (1+1j)
"""
    return complex(a) - complex(b)


# =========================================================
# Multiplication
# =========================================================

def complex_multiply(a, b):
    """
Multiply two real or complex numbers.

Examples
--------
complex_multiply(2, 3) -> (6+0j)
complex_multiply(2 + 3j, 4 + 5j) -> (-7+22j)
"""

    return complex(a) * complex(b)


# =========================================================
# Division
# =========================================================

def complex_divide(a, b):
    """
Divide one number by another.

Raises
------
ZeroDivisionError
    If the denominator is zero.

Examples
--------
complex_divide(6, 2) -> (3+0j)
"""

    return complex(a) / complex(b)


# =========================================================
# Power
# =========================================================

def complex_power(base, exponent):
    """
Calculate the power of a real or complex number.

Python handles the calculation in the complex domain.

Examples
--------
complex_power(2, 3) -> (8+0j)
complex_power(1j, 2) -> (-1+0j)
"""

    return complex(base) ** complex(exponent)