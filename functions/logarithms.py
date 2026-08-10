"""
=========================================================
File: logarithms.py
Folder: functions
=========================================================

Logarithmic functions for the scientific calculator.

Supported functions:

    LOG10
    LN

LOG10:
    The common logarithm, i.e., base 10.

LN:
    The natural logarithm, i.e., base e.

This file is independent of:

- Tokenizer
- Parser
- Expression Tree
- Evaluator
- Arabic language
- User Interface (UI)

This file does not parse mathematical expressions.
=========================================================
"""

import math


# =========================================================
# Base-10 Logarithm
# =========================================================

def log10(value):
    """
Calculate the common logarithm (base 10).

log10(x) = log(x) to the base 10

Parameters
----------
value:
    The number to calculate the logarithm for.

Returns
-------
float
    The common logarithm of the number.

Raises
------
ValueError
    If the number is less than or equal to zero.

Examples
--------
log10(100) -> 2.0
log10(1000) -> 3.0
"""

    return math.log10(value)


# =========================================================
# Natural Logarithm
# =========================================================

def ln(value):
    """
Calculate the natural logarithm.

ln(x) = log(x) to the base e

Parameters
----------
value:
    The number to calculate the natural logarithm for.

Returns
-------
float
    The natural logarithm of the number.

Raises
------
ValueError
    If the number is less than or equal to zero.

Examples
--------
ln(1) -> 0.0
ln(e) -> 1.0
"""

    return math.log(value)