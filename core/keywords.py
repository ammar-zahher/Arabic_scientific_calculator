FUNCTIONS = {
    # Trigonometry
    "SIN",
    "COS",
    "TAN",
    "COT",
    "SEC",
    "CSC",

    # Inverse trigonometry
    "ASIN",
    "ACOS",
    "ATAN",

    # Hyperbolic
    "SINH",
    "COSH",
    "TANH",

    # Logarithms
    "LOG10",
    "LN",

    # Powers / Roots
    "SQRT",
    "CBRT",

    # Absolute / sign
    "ABS",

    # Combinatorics
    "FACT",
    "FUNC",
}
CONSTANTS = {
    "PI",
    "E",
    "I",
}
VARIABLES = {
    "X",
    "Y",
}
def is_function(value: str) -> bool:
    return value in FUNCTIONS


def is_constant(value: str) -> bool:
    return value in CONSTANTS


def is_variable(value: str) -> bool:
    return value in VARIABLES