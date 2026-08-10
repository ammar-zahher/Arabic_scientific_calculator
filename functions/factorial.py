"""
=========================================================
File: factorial.py
Folder: functions
=========================================================

Factorial operations in the calculator.

This file is independent of:

- Tokenizer
- Parser
- Expression Tree
- Evaluator
- Arabic language
- User Interface (UI)

Current responsibility:

    n!

where n is a non-negative integer.

Examples
--------
5!  -> 120
0!  -> 1
"""

import math


# =========================================================
# Factorial
# =========================================================

def factorial(value):
    """
Calculate the factorial of a non-negative integer.

Parameters
----------
value:
    The number to calculate the factorial for.

Returns
-------
int
    The factorial value.

Raises
------
TypeError
    If the input is not an integer.

ValueError
    If the number is negative.

Examples
--------
factorial(5) -> 120
factorial(0) -> 1
"""

    # -----------------------------------------------------
    # The number must be an integer
    # -----------------------------------------------------

    if isinstance(value, bool) or not isinstance(value, int):

        raise TypeError(
            "Factorial is defined for integers only."
        )

    # -----------------------------------------------------
    # The factorial is not defined for negative numbers
    # -----------------------------------------------------

    if value < 0:

        raise ValueError(
            "Factorial is not defined for negative integers."
        )

    # -----------------------------------------------------
    # Calculate the factorial
    # -----------------------------------------------------

    return math.factorial(value)