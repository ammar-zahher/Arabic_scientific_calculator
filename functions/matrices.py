"""
=========================================================
File: matrices.py
Folder: functions
=========================================================

عمليات المصفوفات للحاسبة العلمية.

تمثيل المصفوفة داخل Core:

    [
        [a, b],
        [c, d]
    ]

كل صف يمثل List مستقلة.

هذا الملف مستقل عن:

- Tokenizer
- Parser
- Expression Tree
- Evaluator
- اللغة العربية
- واجهة المستخدم

العمليات المدعومة:

- إنشاء المصفوفة
- معرفة الأبعاد
- الجمع
- الطرح
- ضرب المصفوفات
- الضرب بعدد
- Transpose
- Determinant
- Inverse
- Identity Matrix
=========================================================
"""


# =========================================================
# Validation
# =========================================================

def _validate_matrix(matrix):
    """
    التحقق من صحة تمثيل المصفوفة.

    المصفوفة يجب أن تكون:

    - List
    - غير فارغة
    - جميع الصفوف Lists
    - جميع الصفوف لها نفس الطول
    """

    if not isinstance(matrix, list):
        raise TypeError(
            "Matrix must be a list."
        )

    if not matrix:
        raise ValueError(
            "Matrix cannot be empty."
        )

    if not all(
        isinstance(row, list)
        for row in matrix
    ):
        raise TypeError(
            "Each matrix row must be a list."
        )

    columns = len(matrix[0])

    if columns == 0:
        raise ValueError(
            "Matrix rows cannot be empty."
        )

    if any(
        len(row) != columns
        for row in matrix
    ):
        raise ValueError(
            "All matrix rows must have the same length."
        )


# =========================================================
# Create Matrix
# =========================================================

def create_matrix(rows, columns, value=0):
    """
    إنشاء مصفوفة بالحجم المطلوب.

    Parameters
    ----------
    rows:
        عدد الصفوف.

    columns:
        عدد الأعمدة.

    value:
        القيمة الابتدائية لكل عنصر.

    Examples
    --------
    create_matrix(2, 3)

    [
        [0, 0, 0],
        [0, 0, 0]
    ]
    """

    if not isinstance(rows, int):
        raise TypeError(
            "Rows must be an integer."
        )

    if not isinstance(columns, int):
        raise TypeError(
            "Columns must be an integer."
        )

    if rows <= 0 or columns <= 0:
        raise ValueError(
            "Rows and columns must be positive."
        )

    return [
        [value for _ in range(columns)]
        for _ in range(rows)
    ]


# =========================================================
# Shape
# =========================================================

def matrix_shape(matrix):
    """
    إرجاع أبعاد المصفوفة.

    Returns
    -------
    tuple
        (rows, columns)

    Example
    -------
    matrix_shape([[1, 2], [3, 4]])
        -> (2, 2)
    """

    _validate_matrix(matrix)

    return (
        len(matrix),
        len(matrix[0])
    )


# =========================================================
# Addition
# =========================================================

def matrix_add(a, b):
    """
    جمع مصفوفتين.

    يجب أن تكون المصفوفتان بنفس الأبعاد.
    """

    _validate_matrix(a)
    _validate_matrix(b)

    if matrix_shape(a) != matrix_shape(b):
        raise ValueError(
            "Matrices must have the same dimensions."
        )

    rows, columns = matrix_shape(a)

    return [
        [
            a[i][j] + b[i][j]
            for j in range(columns)
        ]
        for i in range(rows)
    ]


# =========================================================
# Subtraction
# =========================================================

def matrix_subtract(a, b):
    """
    طرح المصفوفة b من المصفوفة a.
    """

    _validate_matrix(a)
    _validate_matrix(b)

    if matrix_shape(a) != matrix_shape(b):
        raise ValueError(
            "Matrices must have the same dimensions."
        )

    rows, columns = matrix_shape(a)

    return [
        [
            a[i][j] - b[i][j]
            for j in range(columns)
        ]
        for i in range(rows)
    ]


# =========================================================
# Matrix Multiplication
# =========================================================

def matrix_multiply(a, b):
    """
    ضرب مصفوفتين.

    إذا كانت:

        A = m × n
        B = n × p

    فالنتيجة:

        C = m × p
    """

    _validate_matrix(a)
    _validate_matrix(b)

    a_rows, a_columns = matrix_shape(a)
    b_rows, b_columns = matrix_shape(b)

    if a_columns != b_rows:
        raise ValueError(
            "Number of columns in the first matrix "
            "must equal number of rows in the second."
        )

    return [
        [
            sum(
                a[i][k] * b[k][j]
                for k in range(a_columns)
            )
            for j in range(b_columns)
        ]
        for i in range(a_rows)
    ]


# =========================================================
# Scalar Multiplication
# =========================================================

def matrix_scalar_multiply(matrix, scalar):
    """
    ضرب جميع عناصر المصفوفة في عدد.
    """

    _validate_matrix(matrix)

    rows, columns = matrix_shape(matrix)

    return [
        [
            matrix[i][j] * scalar
            for j in range(columns)
        ]
        for i in range(rows)
    ]


# =========================================================
# Transpose
# =========================================================

def matrix_transpose(matrix):
    """
    حساب Transpose للمصفوفة.

    مثال:

        [1 2 3]
        [4 5 6]

    تصبح:

        [1 4]
        [2 5]
        [3 6]
    """

    _validate_matrix(matrix)

    return [
        list(column)
        for column in zip(*matrix)
    ]


# =========================================================
# Identity Matrix
# =========================================================

def identity_matrix(size):
    """
    إنشاء مصفوفة الوحدة.

    مثال:

        identity_matrix(3)

        [1 0 0]
        [0 1 0]
        [0 0 1]
    """

    if not isinstance(size, int):
        raise TypeError(
            "Size must be an integer."
        )

    if size <= 0:
        raise ValueError(
            "Size must be positive."
        )

    return [
        [
            1 if i == j else 0
            for j in range(size)
        ]
        for i in range(size)
    ]


# =========================================================
# Determinant
# =========================================================

def matrix_determinant(matrix):
    """
    حساب محدد المصفوفة.

    يدعم المصفوفات المربعة.

    يستخدم التوسع التكراري، وهو مناسب للأحجام
    الصغيرة التي تستهدفها الحاسبة العلمية.
    """

    _validate_matrix(matrix)

    rows, columns = matrix_shape(matrix)

    if rows != columns:
        raise ValueError(
            "Determinant requires a square matrix."
        )

    # 1 × 1

    if rows == 1:
        return matrix[0][0]

    # 2 × 2

    if rows == 2:

        return (
            matrix[0][0] * matrix[1][1]
            - matrix[0][1] * matrix[1][0]
        )

    determinant = 0

    for column in range(columns):

        minor = [
            [
                matrix[i][j]
                for j in range(columns)
                if j != column
            ]
            for i in range(1, rows)
        ]

        sign = (
            1
            if column % 2 == 0
            else -1
        )

        determinant += (
            sign
            * matrix[0][column]
            * matrix_determinant(minor)
        )

    return determinant


# =========================================================
# Inverse
# =========================================================

def matrix_inverse(matrix):
    """
    حساب معكوس المصفوفة.

    يستخدم طريقة Gauss-Jordan.

    يتم تنظيف أخطاء التقريب العشرية الصغيرة
    الناتجة عن عمليات float.

    Raises
    ------
    ValueError
        إذا كانت المصفوفة غير مربعة أو مفردة.
    """

    _validate_matrix(matrix)

    rows, columns = matrix_shape(matrix)

    if rows != columns:
        raise ValueError(
            "Inverse requires a square matrix."
        )

    size = rows

    # =====================================================
    # Create augmented matrix [A | I]
    # =====================================================

    augmented = [
        [
            float(matrix[i][j])
            for j in range(size)
        ]
        + [
            1.0 if i == j else 0.0
            for j in range(size)
        ]
        for i in range(size)
    ]

    # =====================================================
    # Gauss-Jordan elimination
    # =====================================================

    for column in range(size):

        # -------------------------------------------------
        # Find the best pivot
        # -------------------------------------------------

        pivot = column

        for row in range(
            column + 1,
            size
        ):

            if abs(
                augmented[row][column]
            ) > abs(
                augmented[pivot][column]
            ):
                pivot = row

        # -------------------------------------------------
        # Check for singular matrix
        # -------------------------------------------------

        if abs(
            augmented[pivot][column]
        ) < 1e-12:

            raise ValueError(
                "Matrix is singular and has no inverse."
            )

        # -------------------------------------------------
        # Swap rows if necessary
        # -------------------------------------------------

        if pivot != column:

            augmented[column], augmented[pivot] = (
                augmented[pivot],
                augmented[column]
            )

        # -------------------------------------------------
        # Normalize pivot row
        # -------------------------------------------------

        pivot_value = augmented[column][column]

        augmented[column] = [
            value / pivot_value
            for value in augmented[column]
        ]

        # -------------------------------------------------
        # Eliminate other rows
        # -------------------------------------------------

        for row in range(size):

            if row == column:
                continue

            factor = augmented[row][column]

            augmented[row] = [
                augmented[row][j]
                - factor * augmented[column][j]
                for j in range(2 * size)
            ]

    # =====================================================
    # Extract inverse matrix
    # =====================================================

    inverse = [
        row[size:]
        for row in augmented
    ]

    # =====================================================
    # Remove floating-point noise
    # =====================================================

    
    cleaned_inverse = []

    for row in inverse:

        cleaned_row = []

        for value in row:

            # قريب جدًا من عدد صحيح
            rounded_integer = round(value)

            if abs(value - rounded_integer) < 1e-12:
                value = float(rounded_integer)

            else:
                # تقريب محدود لإزالة أخطاء العمليات
                # العشرية مثل:
                #
                # 1.4999999999999998
                #
                # والتي يجب أن تكون:
                #
                # 1.5
                value = round(value, 12)

            # قريب جدًا من الصفر
            if abs(value) < 1e-12:
                value = 0.0

            cleaned_row.append(value)

        cleaned_inverse.append(cleaned_row)

    return cleaned_inverse