"""
=========================================================
File: fractions.py
Folder: functions
=========================================================

عمليات الكسور في الحاسبة العلمية.

هذا الملف مستقل عن:

- Tokenizer
- Parser
- Expression Tree
- Evaluator
- اللغة العربية
- واجهة المستخدم

يستخدم Fraction من مكتبة Python القياسية للحفاظ
على الدقة الحسابية للكسور.

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
    تحويل قيمة إلى Fraction.

    Parameters
    ----------
    value:
        عدد صحيح، Fraction، أو قيمة يمكن تحويلها
        إلى Fraction.

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
    إرجاع بسط الكسر.

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
    إرجاع مقام الكسر.

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
    جمع كسرين.

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
    طرح الكسر الثاني من الأول.

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
    ضرب كسرين.

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
    قسمة كسر على كسر.

    Raises
    ------
    ZeroDivisionError
        إذا كان المقسوم عليه صفرًا.
    """

    return to_fraction(a) / to_fraction(b)


# =========================================================
# Reciprocal
# =========================================================

def reciprocal(value):
    """
    حساب مقلوب الكسر.

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
    تبسيط الكسر.

    Fraction يقوم بالتبسيط تلقائيًا.

    Examples
    --------
    simplify(2/4) -> 1/2
    """

    return to_fraction(value)