"""
=========================================================
File: trigonometry.py
Folder: functions
=========================================================

الدوال المثلثية للحاسبة العلمية.

الملف يدعم:

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

هذا الملف مستقل عن:

- Tokenizer
- Parser
- Expression Tree
- Evaluator
- اللغة العربية
- واجهة المستخدم
=========================================================
"""

import math

from settings.angle_mode import AngleMode


# =========================================================
# Angle Conversion
# =========================================================

def _to_radians(angle, mode):
    """
    تحويل زاوية من نظامها الحالي إلى Radians.

    Parameters
    ----------
    angle:
        قيمة الزاوية.

    mode:
        نظام الزاوية الحالي.

    Returns
    -------
    float
        الزاوية بوحدة Radians.
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
    تحويل زاوية من Radians إلى النظام المطلوب.

    Parameters
    ----------
    angle:
        الزاوية بوحدة Radians.

    mode:
        النظام المطلوب.

    Returns
    -------
    float
        الزاوية بالنظام المطلوب.
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
    حساب جيب الزاوية.

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
    حساب جيب تمام الزاوية.
    """

    radians = _to_radians(angle, mode)

    return math.cos(radians)


# =========================================================
# Tangent
# =========================================================

def tan(angle, mode=AngleMode.RAD):
    """
    حساب ظل الزاوية.
    """

    radians = _to_radians(angle, mode)

    return math.tan(radians)


# =========================================================
# Cotangent
# =========================================================

def cot(angle, mode=AngleMode.RAD):
    """
    حساب ظل تمام الزاوية.

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
    حساب القاطع.

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
    حساب قاطع التمام.

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
    حساب الدالة العكسية للجيب.

    النتيجة تعاد حسب نظام الزاوية المحدد.
    """

    radians = math.asin(value)

    return _from_radians(radians, mode)


# =========================================================
# Inverse Cosine
# =========================================================

def acos(value, mode=AngleMode.RAD):
    """
    حساب الدالة العكسية لجيب التمام.

    النتيجة تعاد حسب نظام الزاوية المحدد.
    """

    radians = math.acos(value)

    return _from_radians(radians, mode)


# =========================================================
# Inverse Tangent
# =========================================================

def atan(value, mode=AngleMode.RAD):
    """
    حساب الدالة العكسية للظل.

    النتيجة تعاد حسب نظام الزاوية المحدد.
    """

    radians = math.atan(value)

    return _from_radians(radians, mode)