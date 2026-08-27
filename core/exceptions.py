"""
=========================================================
File: exceptions.py
Folder: core
=========================================================

Custom exceptions for the scientific calculator.

All calculator-specific exceptions inherit from:

    CalculatorError

This allows the rest of the application to handle
calculator errors separately from normal Python errors.

=========================================================
"""


# =========================================================
# Base Exception
# =========================================================

class CalculatorError(Exception):
    """
    Base exception for all calculator errors.
    """

    pass


# =========================================================
# Tokenizer Errors
# =========================================================

class TokenizerError(CalculatorError):
    """
    Base exception for tokenizer-related errors.
    """

    pass


class InvalidCharacterError(TokenizerError):
    """
    Raised when the tokenizer encounters an unsupported
    character.
    """

    pass


class InvalidNumberError(TokenizerError):
    """
    Raised when a number has an invalid format.

    Examples:

        1.2.3
        1E
        1E+
    """

    pass


class UnknownIdentifierError(TokenizerError):
    """
    Raised when an identifier is not a known function,
    constant, or variable.
    """

    pass


# =========================================================
# Parser Errors
# =========================================================

class ParserError(CalculatorError):
    """
    Base exception for parser-related errors.
    """

    pass


class UnexpectedTokenError(ParserError):
    """
    Raised when the parser receives a token that is not
    valid in the current position.
    """

    pass


class UnexpectedEndError(ParserError):
    """
    Raised when the expression ends unexpectedly.
    """

    pass


class InvalidExpressionError(ParserError):
    """
    Raised when the mathematical expression is invalid.
    """

    pass


# =========================================================
# Evaluation Errors
# =========================================================

class EvaluationError(CalculatorError):
    """
    Base exception for evaluation-related errors.
    """

    pass


class UndefinedVariableError(EvaluationError):
    """
    Raised when an expression uses a variable that does not
    have an assigned value.
    """

    pass


class UnknownConstantError(EvaluationError):
    """
    Raised when an unknown mathematical constant is used.
    """

    pass


class UnknownFunctionError(EvaluationError):
    """
    Raised when an unknown function is evaluated.
    """

    pass


class InvalidOperationError(EvaluationError):
    """
    Raised when an operation cannot be evaluated.
    """

    pass


class InvalidArgumentError(EvaluationError):
    """
    Raised when a function receives invalid arguments.
    """

    pass


# =========================================================
# Mathematical Errors
# =========================================================

class DivisionByZeroError(CalculatorError):
    """
    Raised when attempting to divide by zero.
    """

    pass


class DomainError(CalculatorError):
    """
    Raised when an operation is outside its mathematical
    domain.

    Examples:

        SQRT(-1)
        LOG10(0)
        ASIN(2)
    """

    pass