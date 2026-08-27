"""
=========================================================
File: statistics.py
Folder: functions
=========================================================

Statistical functions for the scientific calculator.

This file supports basic descriptive statistics:

    mean
    median
    mode
    variance
    standard_deviation
    minimum
    maximum
    range_value
    sum_values

It also supports both types of variance:

    population
    sample

This file is independent of:

- Tokenizer
- Parser
- Expression Tree
- Evaluator
- Arabic language
- User Interface (UI)

This file does not parse mathematical expressions.
=========================================================
"""

from collections import Counter
import math


# =========================================================
# Validation
# =========================================================

def _validate_data(data):
    """
Verify that the dataset is valid.

Parameters
----------
data:
    The set of statistical values.

Raises
------
ValueError
    If the data is empty.
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
Calculate the sum of values.

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
Calculate the arithmetic mean.

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
Calculate the median.

The data is sorted internally without modifying the original
list.

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
Calculate the mode.

If there is more than one value with the highest frequency,
all modal values are returned in ascending order.

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
Return the minimum value.

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
Return the maximum value.

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
Calculate the range.

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
Calculate the population variance.

σ² = Σ(x - μ)² / N

Parameters
----------
data:
    The dataset.

Returns
-------
float
    The population variance.
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
Calculate the sample variance.

s² = Σ(x - x̄)² / (n - 1)

Raises
------
ValueError
    If the number of values is less than 2.
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
Calculate the population standard deviation.

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
Calculate the sample standard deviation.

s = sqrt(s²)
"""

    return math.sqrt(
        sample_variance(data)
    )