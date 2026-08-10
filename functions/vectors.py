"""
=========================================================
File: vectors.py
Folder: functions
=========================================================

عمليات المتجهات للحاسبة العلمية.

تمثيل المتجه:

    [x, y, z]

هذا الملف مستقل عن:

- Tokenizer
- Parser
- Expression Tree
- Evaluator
- اللغة العربية
- واجهة المستخدم

العمليات المدعومة:

- إنشاء المتجه
- معرفة البعد
- جمع المتجهات
- طرح المتجهات
- الضرب بعدد
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
    التحقق من صحة المتجه.

    المتجه يجب أن يكون:

    - List
    - غير فارغ
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
    التحقق من أن متجهين لهما نفس البعد.
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
    إنشاء متجه.

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
    إرجاع بُعد المتجه.

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
    جمع متجهين.

    مثال:

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
    طرح المتجه b من المتجه a.

    مثال:

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
    ضرب المتجه في عدد.

    مثال:

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
    حساب طول المتجه.

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
    حساب الضرب النقطي.

    a · b = Σ(ai × bi)

    مثال:

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
    حساب الضرب الاتجاهي لمتجهين ثلاثيي الأبعاد.

        a × b

    يدعم المتجهات ذات البعد 3 فقط.

    مثال:

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
    حساب الزاوية بين متجهين بالراديان.

        cos(theta) = (a · b) / (|a| |b|)

    Returns
    -------
    float
        الزاوية بالراديان.

    Raises
    ------
    ValueError
        إذا كان أحد المتجهين متجهًا صفريًا.
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

    # بسبب أخطاء floating-point قد تظهر قيمة مثل:
    #
    # 1.0000000000000002
    #
    # بينما رياضيًا يجب أن تكون 1.
    #
    # لذلك نحصر القيمة داخل [-1, 1].

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
    حساب متجه الوحدة.

        u = v / |v|

    مثال:

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