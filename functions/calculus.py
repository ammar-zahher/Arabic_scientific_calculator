"""
=========================================================
File: calculus.py
Folder: functions
=========================================================

Basic calculus operations for the scientific calculator.

This file is independent of:

- Tokenizer
- Parser
- Expression Tree
- Evaluator
- Arabic language
- User Interface (UI)

Supported operations:

- Numerical Derivative
- Second Derivative
- Nth Derivative
- Definite Integral
- Trapezoidal Integration
- Simpson Integration
- Average Rate of Change

Note:
This file uses numerical methods.
It does not perform symbolic differentiation or integration.
=========================================================
"""

import math


# =========================================================
# Validation Helpers
# =========================================================

def _validate_function(function):
    """
    Check that the function input is callable.
    """

    if not callable(function):
        raise TypeError(
            "Function must be callable."
        )


def _validate_positive_integer(value, name):
    """
     Check that the value is a positive integer.
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
    Check that the calculation step is not zero.
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
Calculate the first derivative numerically.

Uses Central Difference:

    f'(x) ≈ [f(x+h) - f(x-h)] / (2h)

Parameters
----------
function:
    The function to be differentiated.

x:
    The point at which the derivative is calculated.

h:
    The approximation step.

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
Calculate the second derivative numerically.

Uses:

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
Calculate the nth derivative numerically.

Parameters
----------
function:
    The function.

x:
    The point of evaluation.

order:
    The order of the derivative.

h:
    The approximation step.

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

    # Numerical derivative using iteration
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
Calculate the definite integral numerically using
the Composite Trapezoidal Rule.

    ∫[a,b] f(x) dx

Parameters
----------
function:
    The function.

lower:
    The lower limit.

upper:
    The upper limit.

intervals:
    The number of intervals.

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
Calculate the integral using
Composite Trapezoidal Rule.

This function is separate from definite_integral
so that the Evaluator can later choose
the required integration method.
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
Calculate the integral using
Composite Simpson's Rule.

The number of intervals must be even.

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
Calculate the average rate of change:

    [f(x2) - f(x1)] / (x2 - x1)

Example
-------
f(x) = x²

From x=1 to x=3:

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