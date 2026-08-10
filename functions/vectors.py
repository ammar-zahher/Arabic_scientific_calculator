"""
=========================================================
File: vectors.py
Folder: functions
=========================================================

Vector operations for the scientific calculator.

Vector representation:

    [x, y, z]

This file is independent of:

- Tokenizer
- Parser
- Expression Tree
- Evaluator
- Arabic language
- User Interface (UI)

Supported operations:

- Create Vector
- Get Dimension
- Vector Addition
- Vector Subtraction
- Scalar Multiplication
- Magnitude
- Dot Product
- Cross Product
- Angle Between Vectors
- Unit Vector
=========================================================
"""

import math


# =========================================================
# Validation
# =========================================================

def _validate_vector(vector):
    """
Validate the vector.

The vector must be:

- A list
- Non-empty
"""

    if not isinstance(vector, list):
        raise TypeError(
            "Vector must be a list."
        )

    if not vector:
        raise ValueError(
            "Vector cannot be empty."
        )


def _validate_same_dimension(a, b):
    """
    Verify that two vectors have the same dimension.
    """

    _validate_vector(a)
    _validate_vector(b)

    if len(a) != len(b):
        raise ValueError(
            "Vectors must have the same dimension."
        )


# =========================================================
# Create Vector
# =========================================================

def create_vector(*values):
    """
Create a vector.

Examples
--------
create_vector(1, 2, 3)

-> [1, 2, 3]
"""
    if not values:
        raise ValueError(
            "Vector cannot be empty."
        )

    return list(values)


# =========================================================
# Dimension
# =========================================================

def vector_dimension(vector):
    """
Return the dimension of the vector.

Examples
--------
vector_dimension([1, 2, 3])

-> 3
"""

    _validate_vector(vector)

    return len(vector)


# =========================================================
# Addition
# =========================================================

def vector_add(a, b):
    """
Add two vectors.

Example:

    [1, 2, 3] + [4, 5, 6]

    -> [5, 7, 9]
"""

    _validate_same_dimension(a, b)

    return [
        x + y
        for x, y in zip(a, b)
    ]


# =========================================================
# Subtraction
# =========================================================

def vector_subtract(a, b):
    """
Subtract vector b from vector a.

Example:

    [4, 5, 6] - [1, 2, 3]

    -> [3, 3, 3]
"""

    _validate_same_dimension(a, b)

    return [
        x - y
        for x, y in zip(a, b)
    ]


# =========================================================
# Scalar Multiplication
# =========================================================

def vector_scalar_multiply(vector, scalar):
    """
Multiply a vector by a scalar.

Example:

    3 × [1, 2, 3]

    -> [3, 6, 9]
"""

    _validate_vector(vector)

    return [
        value * scalar
        for value in vector
    ]


# =========================================================
# Magnitude
# =========================================================

def vector_magnitude(vector):
    """
Calculate the vector magnitude.

    |v| = sqrt(x1² + x2² + ... + xn²)

Example
-------
vector_magnitude([3, 4])

-> 5.0
"""

    _validate_vector(vector)

    return math.sqrt(
        sum(value ** 2 for value in vector)
    )


# =========================================================
# Dot Product
# =========================================================

def dot_product(a, b):
    """
Calculate the dot product.

    a · b = Σ(ai × bi)

Example:

    [1, 2, 3] · [4, 5, 6]

    = 32
"""

    _validate_same_dimension(a, b)

    return sum(
        x * y
        for x, y in zip(a, b)
    )


# =========================================================
# Cross Product
# =========================================================

def cross_product(a, b):
    """
Calculate the cross product of two 3-dimensional vectors.

    a × b

Supports 3-dimensional vectors only.

Example:

    [1, 0, 0] × [0, 1, 0]

    -> [0, 0, 1]
"""

    _validate_same_dimension(a, b)

    if len(a) != 3:
        raise ValueError(
            "Cross product requires 3-dimensional vectors."
        )

    ax, ay, az = a
    bx, by, bz = b

    return [
        ay * bz - az * by,
        az * bx - ax * bz,
        ax * by - ay * bx,
    ]


# =========================================================
# Angle Between Vectors
# =========================================================

def angle_between(a, b):
    """
Calculate the angle between two vectors in radians.

    cos(theta) = (a · b) / (|a| |b|)

Returns
-------
float
    The angle in radians.

Raises
------
ValueError
    If either vector is a zero vector.
"""

    _validate_same_dimension(a, b)

    magnitude_a = vector_magnitude(a)
    magnitude_b = vector_magnitude(b)

    if magnitude_a == 0 or magnitude_b == 0:
        raise ValueError(
            "Angle is undefined for a zero vector."
        )

    cosine = (
        dot_product(a, b)
        / (magnitude_a * magnitude_b)
    )

    # Due to floating-point errors, a value like this might appear:
    #
    # 1.0000000000000002
    #
    # While mathematically it should be 1.
    #
    # Therefore, we clamp the value within [-1, 1].
    cosine = max(
        -1.0,
        min(1.0, cosine)
    )

    return math.acos(cosine)


# =========================================================
# Unit Vector
# =========================================================

def unit_vector(vector):
    """
Calculate the unit vector.

    u = v / |v|

Example:

    [3, 4]

    -> [0.6, 0.8]
"""

    _validate_vector(vector)

    magnitude = vector_magnitude(vector)

    if magnitude == 0:
        raise ValueError(
            "Zero vector has no unit vector."
        )

    return [
        value / magnitude
        for value in vector
    ]