"""
=========================================================
File: powers.py
Folder: functions
=========================================================

Power and root operations in the calculator.

This file is independent of:

- Tokenizer
- Parser
- Expression Tree
- Evaluator
- Arabic language
- User Interface (UI)

Current responsibilities:

- Power
- Square Root
- Cube Root

This file does not parse mathematical expressions.
=========================================================
"""

import math


# =========================================================
# Power
# =========================================================

def power(base, exponent):
    """
Calculate the power.

Parameters
----------
base:
    The base.

exponent:
    The exponent.

Returns
-------
The resulting number from:
    base ** exponent

Examples
--------
power(2, 3) -> 8
power(5, 2) -> 25
power(2, -3) -> 0.125
"""

    return base ** exponent


# =========================================================
# Square Root
# =========================================================

def square_root(value):
    """
Calculate the square root.

Parameters
----------
value:
    The number to calculate the square root of.

Returns
-------
The square root of the number.

Raises
------
ValueError
    If the number is negative in the real domain.

Examples
--------
square_root(25) -> 5.0
square_root(9) -> 3.0
"""

    return math.sqrt(value)


# =========================================================
# Cube Root
# =========================================================

def cube_root(value):
    """
Calculate the cube root.

Also supports negative numbers.

Examples
--------
cube_root(27) -> 3.0
cube_root(8) -> 2.0
cube_root(-8) -> -2.0
"""

    return math.cbrt(value)