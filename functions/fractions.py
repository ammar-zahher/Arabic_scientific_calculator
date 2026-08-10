"""
=========================================================
File: fractions.py
Folder: functions
=========================================================

Fraction operations in the scientific calculator.

This file is independent of:

- Tokenizer
- Parser
- Expression Tree
- Evaluator
- Arabic language
- User Interface (UI)

Uses Fraction from the Python standard library to maintain
the arithmetic precision of fractions.

Examples
--------
1/2
3/4 + 1/4
2/3 * 3/5
"""

from fractions import Fraction


# =========================================================
# Conversion
# =========================================================

def to_fraction(value):
    """
Convert a value to a Fraction.

Parameters
----------
value:
    An integer, Fraction, or a value that can be converted
    to a Fraction.

Returns
-------
Fraction

Examples
--------
to_fraction(5) -> Fraction(5, 1)
to_fraction(0.5) -> Fraction(1, 2)
to_fraction("3/4") -> Fraction(3, 4)
"""

    if isinstance(value, Fraction):
        return value

    if isinstance(value, int):
        return Fraction(value, 1)

    if isinstance(value, float):
        return Fraction(str(value))

    if isinstance(value, str):

        return Fraction(value)

    raise TypeError(
        "Value cannot be converted to Fraction."
    )


# =========================================================
# Numerator
# =========================================================

def numerator(value):
    """
Return the numerator of the fraction.

Examples
--------
numerator(Fraction(3, 4)) -> 3
numerator(5) -> 5
"""

    fraction = to_fraction(value)

    return fraction.numerator


# =========================================================
# Denominator
# =========================================================

def denominator(value):
    """
Return the denominator of the fraction.

Examples
--------
denominator(Fraction(3, 4)) -> 4
denominator(5) -> 1
"""

    fraction = to_fraction(value)

    return fraction.denominator


# =========================================================
# Addition
# =========================================================

def fraction_add(a, b):
    """
Add two fractions.

Examples
--------
1/2 + 1/3 = 5/6
"""

    return to_fraction(a) + to_fraction(b)


# =========================================================
# Subtraction
# =========================================================

def fraction_subtract(a, b):
    """
Subtract the second fraction from the first.

Examples
--------
3/4 - 1/4 = 1/2
"""

    return to_fraction(a) - to_fraction(b)


# =========================================================
# Multiplication
# =========================================================

def fraction_multiply(a, b):
    """
Multiply two fractions.

Examples
--------
2/3 × 3/4 = 1/2
"""

    return to_fraction(a) * to_fraction(b)


# =========================================================
# Division
# =========================================================

def fraction_divide(a, b):
    """
Divide a fraction by a fraction.

Raises
------
ZeroDivisionError
    If the divisor is zero.
"""

    return to_fraction(a) / to_fraction(b)


# =========================================================
# Reciprocal
# =========================================================

def reciprocal(value):
    """
Calculate the reciprocal of the fraction.

Examples
--------
reciprocal(2/3) = 3/2
reciprocal(5) = 1/5
"""

    fraction = to_fraction(value)

    if fraction == 0:

        raise ZeroDivisionError(
            "Cannot calculate reciprocal of zero."
        )

    return Fraction(
        fraction.denominator,
        fraction.numerator
    )


# =========================================================
# Simplify
# =========================================================

def simplify(value):
    """
Simplify the fraction.

Fraction simplifies automatically.

Examples
--------
simplify(2/4) -> 1/2
"""

    return to_fraction(value)