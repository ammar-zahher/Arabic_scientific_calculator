"""
=========================================================
File: equations.py
Folder: functions
=========================================================

Solving mathematical equations for the scientific calculator.

This file is responsible solely for equation-solving algorithms.

Independent of:

- Tokenizer
- Parser
- Expression Tree
- Evaluator
- Arabic language
- User Interface (UI)

And does not use:

    eval()

=========================================================

Supported operations:

1. Linear equations
2. Quadratic equations
3. Bisection method
4. Newton-Raphson method
5. Secant method

=========================================================

Important Notes
---------------------------------------------------------

Text expressions such as:

    "س^2 + 3س - 4"

are not parsed here.

Converting a text expression into an Expression Tree
is the responsibility of the Core.

Afterward, the Evaluator can convert
the expression into an evaluable function,
and then pass it to the algorithms in this file.

=========================================================
"""

import cmath
import math


# =========================================================
# Constants
# =========================================================

DEFAULT_TOLERANCE = 1e-10
DEFAULT_MAX_ITERATIONS = 1000
ZERO_TOLERANCE = 1e-12


# =========================================================
# Validation Helpers
# =========================================================

def _validate_number(value, name):
    """
Validate that the value is a number.

Supports:

- int
- float
- complex
"""

    if not isinstance(
        value,
        (int, float, complex)
    ):
        raise TypeError(
            f"{name} must be a number."
        )


def _validate_real_number(value, name):
    """
Validate that the value is a real number.

Used in numerical algorithms that operate
on the real number line.
"""

    if not isinstance(
        value,
        (int, float)
    ):
        raise TypeError(
            f"{name} must be a real number."
        )


def _validate_positive_integer(value, name):
    """
    Validate that the value is a positive integer.
    """

    if not isinstance(value, int):
        raise TypeError(
            f"{name} must be an integer."
        )

    if value <= 0:
        raise ValueError(
            f"{name} must be positive."
        )


def _validate_tolerance(tolerance):
    """
    Validate the tolerance value.
    """

    if not isinstance(
        tolerance,
        (int, float)
    ):
        raise TypeError(
            "Tolerance must be a real number."
        )

    if not math.isfinite(tolerance):
        raise ValueError(
            "Tolerance must be finite."
        )

    if tolerance <= 0:
        raise ValueError(
            "Tolerance must be positive."
        )


# =========================================================
# Numeric Cleaning
# =========================================================

def _clean_number(
    value,
    tolerance=ZERO_TOLERANCE
):
    """
Clean floating-point errors.

Examples:

    1.9999999999999998
        -> 2.0

    0.000000000000001
        -> 0.0

If a complex number has a very small imaginary part,
it is removed.
"""

    if isinstance(value, complex):

        real = value.real
        imaginary = value.imag

        if abs(real) < tolerance:
            real = 0.0

        if abs(imaginary) < tolerance:
            imaginary = 0.0

        if imaginary == 0.0:
            value = real
        else:
            value = complex(
                real,
                imaginary
            )

    if isinstance(
        value,
        (int, float)
    ):

        if not math.isfinite(value):
            return value

        if abs(value) < tolerance:
            return 0.0

        nearest_integer = round(value)

        if abs(
            value - nearest_integer
        ) < tolerance:

            return float(
                nearest_integer
            )

    return value


def _clean_roots(roots):
    """
    Clean a set of roots.
    """

    return tuple(
        _clean_number(root)
        for root in roots
    )


# =========================================================
# Linear Equation
# =========================================================

def solve_linear(a, b):
    """
Solving the equation:

    ax + b = 0

Cases:

    a != 0
        There is a single solution.

    a == 0 and b != 0
        There is no solution.

    a == 0 and b == 0
        There are infinite solutions.

Returns
-------
tuple
    The roots.

Examples
--------
solve_linear(2, 4)

    -> (-2.0,)

solve_linear(0, 4)

    -> ()

solve_linear(0, 0)

    -> ValueError
"""
    _validate_number(a, "a")
    _validate_number(b, "b")

    # -----------------------------------------------------
    # Infinite solutions
    # -----------------------------------------------------

    if a == 0 and b == 0:

        raise ValueError(
            "Equation has infinitely many solutions."
        )

    # -----------------------------------------------------
    # No solution
    # -----------------------------------------------------

    if a == 0:

        return ()

    # -----------------------------------------------------
    # Unique solution
    # -----------------------------------------------------

    root = -b / a

    return (
        _clean_number(root),
    )


# =========================================================
# Quadratic Equation
# =========================================================

def solve_quadratic(a, b, c):
    """
Solving the equation:

    ax² + bx + c = 0

using the quadratic formula:

    x = (-b ± √Δ) / 2a

where:

    Δ = b² - 4ac

Supported cases:

- Two distinct real roots.
- One repeated real root.
- Complex roots.
- Linear equation (first-degree).
- No solution.
- Infinite solutions.

Returns
-------
tuple
    The roots.

Examples
--------
solve_quadratic(1, -5, 6)

    -> (2.0, 3.0)

solve_quadratic(1, -4, 4)

    -> (2.0,)

solve_quadratic(1, 0, 1)

    -> (-1j, 1j)
"""

    _validate_number(a, "a")
    _validate_number(b, "b")
    _validate_number(c, "c")

    # =====================================================
    # Degenerate equation
    # =====================================================

    if a == 0:

        return solve_linear(
            b,
            c
        )

    # =====================================================
    # Discriminant
    # =====================================================

    discriminant = (
        b ** 2
        - 4 * a * c
    )

    # =====================================================
    # Real coefficients
    # =====================================================

    if not isinstance(
        discriminant,
        complex
    ):

        # -------------------------------------------------
        # Two distinct real roots
        # -------------------------------------------------

        if discriminant > 0:

            sqrt_discriminant = math.sqrt(
                discriminant
            )

            x1 = (
                -b - sqrt_discriminant
            ) / (2 * a)

            x2 = (
                -b + sqrt_discriminant
            ) / (2 * a)

            roots = [
                _clean_number(x1),
                _clean_number(x2),
            ]

            roots.sort()

            return tuple(roots)

        # -------------------------------------------------
        # Repeated real root
        # -------------------------------------------------

        if discriminant == 0:

            root = (
                -b
            ) / (2 * a)

            return (
                _clean_number(root),
            )

        # -------------------------------------------------
        # Negative discriminant
        # -------------------------------------------------

        sqrt_discriminant = cmath.sqrt(
            discriminant
        )

        x1 = (
            -b - sqrt_discriminant
        ) / (2 * a)

        x2 = (
            -b + sqrt_discriminant
        ) / (2 * a)

        roots = [
            _clean_number(x1),
            _clean_number(x2),
        ]

        #Sorting complex roots in a consistent order
        roots.sort(
            key=lambda value: (
                value.real,
                value.imag
            )
        )

        return tuple(roots)

    # =====================================================
    # Complex coefficients
    # =====================================================

    sqrt_discriminant = cmath.sqrt(
        discriminant
    )

    x1 = (
        -b - sqrt_discriminant
    ) / (2 * a)

    x2 = (
        -b + sqrt_discriminant
    ) / (2 * a)

    roots = _clean_roots(
        [x1, x2]
    )

    return roots


# =========================================================
# Bisection Method
# =========================================================

def bisection(
    function,
    lower,
    upper,
    tolerance=DEFAULT_TOLERANCE,
    max_iterations=DEFAULT_MAX_ITERATIONS
):
    """
Finding a root for:

    f(x) = 0

using the Bisection Method.

It is required that the function has opposite signs
at the interval endpoints.

That is:

    f(a) * f(b) < 0

or that one of the endpoints is a root.

Returns
-------
float
    The approximate root.
"""

    if not callable(function):

        raise TypeError(
            "Function must be callable."
        )

    _validate_real_number(
        lower,
        "lower"
    )

    _validate_real_number(
        upper,
        "upper"
    )

    _validate_tolerance(
        tolerance
    )

    _validate_positive_integer(
        max_iterations,
        "max_iterations"
    )

    if lower >= upper:

        raise ValueError(
            "Lower bound must be less than upper bound."
        )

    f_lower = function(lower)
    f_upper = function(upper)

    _validate_real_number(
        f_lower,
        "function(lower)"
    )

    _validate_real_number(
        f_upper,
        "function(upper)"
    )

    # =====================================================
    # Endpoint roots
    # =====================================================

    if abs(f_lower) <= tolerance:

        return _clean_number(
            lower
        )

    if abs(f_upper) <= tolerance:

        return _clean_number(
            upper
        )

    # =====================================================
    # Check sign change
    # =====================================================

    if f_lower * f_upper > 0:

        raise ValueError(
            "Function must have opposite signs "
            "at the interval endpoints."
        )

    # =====================================================
    # Iteration
    # =====================================================

    for _ in range(
        max_iterations
    ):

        midpoint = (
            lower + upper
        ) / 2

        f_midpoint = function(
            midpoint
        )

        _validate_real_number(
            f_midpoint,
            "function(midpoint)"
        )

        # -------------------------------------------------
        # Function convergence
        # -------------------------------------------------

        if abs(
            f_midpoint
        ) <= tolerance:

            return _clean_number(
                midpoint
            )

        # -------------------------------------------------
        # Interval convergence
        # -------------------------------------------------

        if (
            abs(upper - lower)
            <= tolerance
        ):

            return _clean_number(
                midpoint
            )

        # -------------------------------------------------
        # Keep the interval containing the root
        # -------------------------------------------------

        if f_lower * f_midpoint < 0:

            upper = midpoint
            f_upper = f_midpoint

        else:

            lower = midpoint
            f_lower = f_midpoint

    raise ValueError(
        "Bisection method did not converge "
        "within max_iterations."
    )


# =========================================================
# Newton-Raphson Method
# =========================================================

def newton_raphson(
    function,
    derivative,
    initial_guess,
    tolerance=DEFAULT_TOLERANCE,
    max_iterations=100
):

    if not callable(function):

        raise TypeError(
            "Function must be callable."
        )

    if not callable(derivative):

        raise TypeError(
            "Derivative must be callable."
        )

    _validate_real_number(
        initial_guess,
        "initial_guess"
    )

    _validate_tolerance(
        tolerance
    )

    _validate_positive_integer(
        max_iterations,
        "max_iterations"
    )

    x = float(initial_guess)

    for _ in range(
        max_iterations
    ):

        function_value = function(x)
        derivative_value = derivative(x)

        _validate_real_number(
            function_value,
            "function(x)"
        )

        _validate_real_number(
            derivative_value,
            "derivative(x)"
        )

        # -------------------------------------------------
        # Already converged
        # -------------------------------------------------

        if abs(
            function_value
        ) <= tolerance:

            return _clean_number(x)

        # -------------------------------------------------
        # Derivative too small
        # -------------------------------------------------

        if abs(
            derivative_value
        ) <= ZERO_TOLERANCE:

            raise ValueError(
                "Derivative is too close to zero. "
                "Newton-Raphson cannot continue."
            )

        # -------------------------------------------------
        # Newton step
        # -------------------------------------------------

        next_x = (
            x
            - function_value
            / derivative_value
        )

        if not math.isfinite(next_x):

            raise ValueError(
                "Newton-Raphson produced "
                "a non-finite value."
            )

        # -------------------------------------------------
        # Step convergence
        # -------------------------------------------------

        if abs(
            next_x - x
        ) <= tolerance:

            next_value = function(next_x)

            if abs(
                next_value
            ) <= tolerance:

                return _clean_number(
                    next_x
                )

        x = next_x

    raise ValueError(
        "Newton-Raphson did not converge "
        "within max_iterations."
    )


# =========================================================
# Secant Method
# =========================================================

def secant(
    function,
    x0,
    x1,
    tolerance=DEFAULT_TOLERANCE,
    max_iterations=100
):
    """
Finding a root using the Secant Method.

This method does not require explicitly providing the derivative.

Formula:

    x(n+1)
    =
    x(n)
    -
    f(x_n) * (x_n - x(n-1))
    --------------------------------
    f(x_n) - f(x(n-1))

Parameters
----------
function:
    The function.

x0:
    The first initial guess.

x1:
    The second initial guess.

tolerance:
    The tolerance (accuracy) for the solution.

max_iterations:
    Maximum number of iterations.
"""
    if not callable(function):

        raise TypeError(
            "Function must be callable."
        )

    _validate_real_number(
        x0,
        "x0"
    )

    _validate_real_number(
        x1,
        "x1"
    )

    _validate_tolerance(
        tolerance
    )

    _validate_positive_integer(
        max_iterations,
        "max_iterations"
    )

    if x0 == x1:

        raise ValueError(
            "x0 and x1 must be different."
        )

    f0 = function(x0)
    f1 = function(x1)

    _validate_real_number(
        f0,
        "function(x0)"
    )

    _validate_real_number(
        f1,
        "function(x1)"
    )

    for _ in range(
        max_iterations
    ):

        # -------------------------------------------------
        # Endpoint convergence
        # -------------------------------------------------

        if abs(f0) <= tolerance:

            return _clean_number(x0)

        if abs(f1) <= tolerance:

            return _clean_number(x1)

        denominator = f1 - f0

        if abs(
            denominator
        ) <= ZERO_TOLERANCE:

            raise ValueError(
                "Secant method encountered "
                "a near-zero denominator."
            )

        # -------------------------------------------------
        # Secant step
        # -------------------------------------------------

        x2 = (
            x1
            - f1 * (x1 - x0)
            / denominator
        )

        if not math.isfinite(x2):

            raise ValueError(
                "Secant method produced "
                "a non-finite value."
            )

        f2 = function(x2)

        _validate_real_number(
            f2,
            "function(x2)"
        )

        # -------------------------------------------------
        # Convergence
        # -------------------------------------------------

        if abs(f2) <= tolerance:

            return _clean_number(x2)

        if abs(
            x2 - x1
        ) <= tolerance:

            if abs(f2) <= tolerance:

                return _clean_number(x2)

        # -------------------------------------------------
        # Move forward
        # -------------------------------------------------

        x0, f0 = x1, f1
        x1, f1 = x2, f2

    raise ValueError(
        "Secant method did not converge "
        "within max_iterations."
    )