"""
=========================================================
File: calculus.py
Folder: functions
=========================================================

العمليات الأساسية في التفاضل والتكامل للحاسبة العلمية.

هذا الملف مستقل عن:

- Tokenizer
- Parser
- Expression Tree
- Evaluator
- اللغة العربية
- واجهة المستخدم

العمليات المدعومة:

- Numerical Derivative
- Second Derivative
- Nth Derivative
- Definite Integral
- Trapezoidal Integration
- Simpson Integration
- Average Rate of Change

ملاحظة:
هذا الملف يستخدم الحساب العددي (Numerical Methods).
لا يقوم بالتفاضل أو التكامل الرمزي.
=========================================================
"""

import math


# =========================================================
# Validation Helpers
# =========================================================

def _validate_function(function):
    """
    التحقق من أن المدخل Function قابل للاستدعاء.
    """

    if not callable(function):
        raise TypeError(
            "Function must be callable."
        )


def _validate_positive_integer(value, name):
    """
    التحقق من أن القيمة عدد صحيح موجب.
    """

    if not isinstance(value, int):
        raise TypeError(
            f"{name} must be an integer."
        )

    if value <= 0:
        raise ValueError(
            f"{name} must be positive."
        )


def _validate_nonzero_step(step):
    """
    التحقق من أن خطوة الحساب ليست صفرًا.
    """

    if step == 0:
        raise ValueError(
            "Step cannot be zero."
        )


# =========================================================
# Numerical Derivative
# =========================================================

def derivative(function, x, h=1e-5):
    """
    حساب المشتقة الأولى عدديًا.

    يستخدم Central Difference:

        f'(x) ≈ [f(x+h) - f(x-h)] / (2h)

    Parameters
    ----------
    function:
        الدالة المراد اشتقاقها.

    x:
        النقطة التي نحسب عندها المشتقة.

    h:
        خطوة التقريب.

    Example
    -------
    derivative(lambda x: x**2, 3)

    -> approximately 6
    """

    _validate_function(function)

    if h == 0:
        raise ValueError(
            "Step h cannot be zero."
        )

    return (
        function(x + h)
        - function(x - h)
    ) / (2 * h)


# =========================================================
# Second Derivative
# =========================================================

def second_derivative(function, x, h=1e-4):
    """
    حساب المشتقة الثانية عدديًا.

    يستخدم:

        f''(x) ≈
        [f(x+h) - 2f(x) + f(x-h)] / h²
    """

    _validate_function(function)

    if h == 0:
        raise ValueError(
            "Step h cannot be zero."
        )

    return (
        function(x + h)
        - 2 * function(x)
        + function(x - h)
    ) / (h ** 2)


# =========================================================
# Nth Derivative
# =========================================================

def nth_derivative(function, x, order, h=1e-4):
    """
    حساب المشتقة من الرتبة n عدديًا.

    Parameters
    ----------
    function:
        الدالة.

    x:
        نقطة التقييم.

    order:
        رتبة المشتقة.

    h:
        خطوة التقريب.

    Example
    -------
    nth_derivative(lambda x: x**3, 2, 2)

    -> approximately 12
    """

    _validate_function(function)

    _validate_positive_integer(
        order,
        "Order"
    )

    if h == 0:
        raise ValueError(
            "Step h cannot be zero."
        )

    # مشتقة عددية باستخدام تكرار
    # Central Difference.

    current_function = function

    for _ in range(order):

        previous_function = current_function

        def current_function(x_value, f=previous_function):
            return (
                f(x_value + h)
                - f(x_value - h)
            ) / (2 * h)

    return current_function(x)


# =========================================================
# Definite Integral
# =========================================================

def definite_integral(
    function,
    lower,
    upper,
    intervals=1000
):
    """
    حساب التكامل المحدد عدديًا باستخدام
    Composite Trapezoidal Rule.

        ∫[a,b] f(x) dx

    Parameters
    ----------
    function:
        الدالة.

    lower:
        الحد السفلي.

    upper:
        الحد العلوي.

    intervals:
        عدد الفواصل.

    Example
    -------
    definite_integral(
        lambda x: x,
        0,
        2
    )

    -> approximately 2
    """

    _validate_function(function)

    _validate_positive_integer(
        intervals,
        "Intervals"
    )

    if lower == upper:
        return 0.0

    step = (
        upper - lower
    ) / intervals

    total = (
        function(lower)
        + function(upper)
    ) / 2

    for i in range(1, intervals):

        x = lower + i * step

        total += function(x)

    return total * step


# =========================================================
# Trapezoidal Integration
# =========================================================

def trapezoidal_integral(
    function,
    lower,
    upper,
    intervals=1000
):
    """
    حساب التكامل باستخدام
    Composite Trapezoidal Rule.

    هذه الدالة منفصلة عن definite_integral
    حتى يستطيع Evaluator لاحقًا اختيار
    طريقة التكامل المطلوبة.
    """

    return definite_integral(
        function,
        lower,
        upper,
        intervals
    )


# =========================================================
# Simpson Integration
# =========================================================

def simpson_integral(
    function,
    lower,
    upper,
    intervals=1000
):
    """
    حساب التكامل باستخدام
    Composite Simpson's Rule.

    يجب أن يكون عدد الفواصل زوجيًا.

        ∫[a,b] f(x) dx
    """

    _validate_function(function)

    _validate_positive_integer(
        intervals,
        "Intervals"
    )

    if intervals % 2 != 0:
        raise ValueError(
            "Simpson integration requires "
            "an even number of intervals."
        )

    if lower == upper:
        return 0.0

    step = (
        upper - lower
    ) / intervals

    total = (
        function(lower)
        + function(upper)
    )

    for i in range(1, intervals):

        x = lower + i * step

        if i % 2 == 0:
            total += 2 * function(x)
        else:
            total += 4 * function(x)

    return (
        total * step / 3
    )


# =========================================================
# Average Rate of Change
# =========================================================

def average_rate_of_change(
    function,
    x1,
    x2
):
    """
    حساب معدل التغير المتوسط:

        [f(x2) - f(x1)] / (x2 - x1)

    Example
    -------
    f(x) = x²

    من x=1 إلى x=3:

        (9 - 1) / (3 - 1)

        = 4
    """

    _validate_function(function)

    if x1 == x2:
        raise ValueError(
            "x1 and x2 cannot be equal."
        )

    return (
        function(x2)
        - function(x1)
    ) / (x2 - x1)