"""
=========================================================
File: statistics.py
Folder: functions
=========================================================

الدوال الإحصائية للحاسبة العلمية.

يدعم هذا الملف الإحصاء الوصفي الأساسي:

    mean
    median
    mode
    variance
    standard_deviation
    minimum
    maximum
    range_value
    sum_values

كما يدعم نوعي التباين:

    population
    sample

هذا الملف مستقل عن:

- Tokenizer
- Parser
- Expression Tree
- Evaluator
- اللغة العربية
- واجهة المستخدم

لا يقوم هذا الملف بتحليل التعبيرات الرياضية.
=========================================================
"""

from collections import Counter
import math


# =========================================================
# Validation
# =========================================================

def _validate_data(data):
    """
    التحقق من أن مجموعة البيانات صالحة.

    Parameters
    ----------
    data:
        مجموعة القيم الإحصائية.

    Raises
    ------
    ValueError
        إذا كانت البيانات فارغة.
    """

    if not data:
        raise ValueError(
            "Statistical data cannot be empty."
        )


# =========================================================
# Sum
# =========================================================

def sum_values(data):
    """
    حساب مجموع القيم.

    Examples
    --------
    sum_values([1, 2, 3]) -> 6
    """

    _validate_data(data)

    return sum(data)


# =========================================================
# Mean
# =========================================================

def mean(data):
    """
    حساب المتوسط الحسابي.

    mean = sum(x) / n

    Examples
    --------
    mean([1, 2, 3, 4, 5]) -> 3
    """

    _validate_data(data)

    return sum(data) / len(data)


# =========================================================
# Median
# =========================================================

def median(data):
    """
    حساب الوسيط.

    يتم ترتيب البيانات داخليًا دون تعديل القائمة
    الأصلية.

    Examples
    --------
    median([1, 3, 2]) -> 2
    median([1, 2, 3, 4]) -> 2.5
    """

    _validate_data(data)

    sorted_data = sorted(data)

    n = len(sorted_data)

    middle = n // 2

    if n % 2 == 1:

        return sorted_data[middle]

    return (
        sorted_data[middle - 1]
        + sorted_data[middle]
    ) / 2


# =========================================================
# Mode
# =========================================================

def mode(data):
    """
    حساب المنوال.

    إذا كان هناك أكثر من قيمة لها أعلى تكرار،
    يتم إرجاع جميع القيم المنوالية بترتيب تصاعدي.

    Returns
    -------
    list

    Examples
    --------
    mode([1, 2, 2, 3]) -> [2]

    mode([1, 1, 2, 2, 3]) -> [1, 2]
    """

    _validate_data(data)

    counts = Counter(data)

    highest_frequency = max(
        counts.values()
    )

    modes = [
        value
        for value, count in counts.items()
        if count == highest_frequency
    ]

    return sorted(modes)


# =========================================================
# Minimum
# =========================================================

def minimum(data):
    """
    إرجاع أصغر قيمة.

    Examples
    --------
    minimum([4, 1, 7, 2]) -> 1
    """

    _validate_data(data)

    return min(data)


# =========================================================
# Maximum
# =========================================================

def maximum(data):
    """
    إرجاع أكبر قيمة.

    Examples
    --------
    maximum([4, 1, 7, 2]) -> 7
    """

    _validate_data(data)

    return max(data)


# =========================================================
# Range
# =========================================================

def range_value(data):
    """
    حساب المدى.

    range = maximum - minimum

    Examples
    --------
    range_value([2, 5, 8]) -> 6
    """

    _validate_data(data)

    return maximum(data) - minimum(data)


# =========================================================
# Population Variance
# =========================================================

def population_variance(data):
    """
    حساب تباين المجتمع.

    σ² = Σ(x - μ)² / N

    Parameters
    ----------
    data:
        مجموعة البيانات.

    Returns
    -------
    float
        تباين المجتمع.
    """

    _validate_data(data)

    average = mean(data)

    return sum(
        (value - average) ** 2
        for value in data
    ) / len(data)


# =========================================================
# Sample Variance
# =========================================================

def sample_variance(data):
    """
    حساب تباين العينة.

    s² = Σ(x - x̄)² / (n - 1)

    Raises
    ------
    ValueError
        إذا كان عدد القيم أقل من 2.
    """

    _validate_data(data)

    if len(data) < 2:
        raise ValueError(
            "Sample variance requires at least two values."
        )

    average = mean(data)

    return sum(
        (value - average) ** 2
        for value in data
    ) / (len(data) - 1)


# =========================================================
# Population Standard Deviation
# =========================================================

def population_standard_deviation(data):
    """
    حساب الانحراف المعياري للمجتمع.

    σ = sqrt(σ²)
    """

    return math.sqrt(
        population_variance(data)
    )


# =========================================================
# Sample Standard Deviation
# =========================================================

def sample_standard_deviation(data):
    """
    حساب الانحراف المعياري للعينة.

    s = sqrt(s²)
    """

    return math.sqrt(
        sample_variance(data)
    )