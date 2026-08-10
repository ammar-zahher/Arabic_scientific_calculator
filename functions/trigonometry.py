"""
=========================================================
File: trigonometry.py
Folder: functions
=========================================================

Trigonometric functions for the scientific calculator.

This file supports:

Trigonometric:
    SIN
    COS
    TAN
    COT
    SEC
    CSC

Inverse Trigonometric:
    ASIN
    ACOS
    ATAN

Angle Modes:
    DEG
    RAD
    GRAD

This file is independent of:

- Tokenizer
- Parser
- Expression Tree
- Evaluator
- Arabic language
- User Interface (UI)
=========================================================
"""

import math

from settings.angle_mode import AngleMode


# =========================================================
# Angle Conversion
# =========================================================

def _to_radians(angle, mode):
    """
Convert an angle from its current system to Radians.

Parameters
----------
angle:
    The value of the angle.

mode:
    The current angle system.

Returns
-------
float
    The angle in Radians.
"""

    if mode == AngleMode.RAD:
        return angle

    if mode == AngleMode.DEG:
        return math.radians(angle)

    if mode == AngleMode.GRAD:
        return angle * math.pi / 200

    raise ValueError(
        f"Unsupported angle mode: {mode}"
    )


def _from_radians(angle, mode):
    """
Convert an angle from Radians to the desired system.

Parameters
----------
angle:
    The angle in Radians.

mode:
    The target system.

Returns
-------
float
    The angle in the target system.
"""

    if mode == AngleMode.RAD:
        return angle

    if mode == AngleMode.DEG:
        return math.degrees(angle)

    if mode == AngleMode.GRAD:
        return angle * 200 / math.pi

    raise ValueError(
        f"Unsupported angle mode: {mode}"
    )


# =========================================================
# Sine
# =========================================================

def sin(angle, mode=AngleMode.RAD):
    """
Calculate the sine.

Examples
--------
sin(90, DEG) -> 1
sin(pi / 2, RAD) -> 1
sin(100, GRAD) -> 1
"""

    radians = _to_radians(angle, mode)

    return math.sin(radians)


# =========================================================
# Cosine
# =========================================================

def cos(angle, mode=AngleMode.RAD):
    """
    Calculate the cosine.
    """

    radians = _to_radians(angle, mode)

    return math.cos(radians)


# =========================================================
# Tangent
# =========================================================

def tan(angle, mode=AngleMode.RAD):
    """
    Calculate the tangent.
    """

    radians = _to_radians(angle, mode)

    return math.tan(radians)


# =========================================================
# Cotangent
# =========================================================

def cot(angle, mode=AngleMode.RAD):
    """
Calculate the cotangent.

cot(x) = 1 / tan(x)
"""

    radians = _to_radians(angle, mode)

    tangent = math.tan(radians)

    if math.isclose(tangent, 0.0, abs_tol=1e-15):
        raise ValueError(
            "Cotangent is undefined for this angle."
        )

    return 1 / tangent


# =========================================================
# Secant
# =========================================================

def sec(angle, mode=AngleMode.RAD):
    """
Calculate the secant.

sec(x) = 1 / cos(x)
"""

    radians = _to_radians(angle, mode)

    cosine = math.cos(radians)

    if math.isclose(cosine, 0.0, abs_tol=1e-15):
        raise ValueError(
            "Secant is undefined for this angle."
        )

    return 1 / cosine


# =========================================================
# Cosecant
# =========================================================

def csc(angle, mode=AngleMode.RAD):
    """
Calculate the cosecant.

csc(x) = 1 / sin(x)
"""

    radians = _to_radians(angle, mode)

    sine = math.sin(radians)

    if math.isclose(sine, 0.0, abs_tol=1e-15):
        raise ValueError(
            "Cosecant is undefined for this angle."
        )

    return 1 / sine


# =========================================================
# Inverse Sine
# =========================================================

def asin(value, mode=AngleMode.RAD):
    """
Calculate the inverse sine function.

The result is returned according to the specified angle system.
"""

    radians = math.asin(value)

    return _from_radians(radians, mode)


# =========================================================
# Inverse Cosine
# =========================================================

def acos(value, mode=AngleMode.RAD):
    """
Calculate the inverse cosine function.

The result is returned according to the specified angle system.
"""

    radians = math.acos(value)

    return _from_radians(radians, mode)


# =========================================================
# Inverse Tangent
# =========================================================

def atan(value, mode=AngleMode.RAD):
    """
Calculate the inverse tangent function.

The result is returned according to the specified angle system.
"""

    radians = math.atan(value)

    return _from_radians(radians, mode)