"""
=========================================================
File: errors.py
Folder: core
=========================================================

Utilities for representing calculator errors.

This file does not define exception types.

Exception classes are defined in:

    core.exceptions

This module is responsible for storing and formatting
information about an error, such as:

- Error message
- Expression
- Error position
- Original exception

=========================================================
"""

from dataclasses import dataclass
from typing import Optional

from core.exceptions import CalculatorError


# =========================================================
# Calculator Error Information
# =========================================================

@dataclass(frozen=True)
class CalculatorErrorInfo:
    """
    Represents information about a calculator error.

    Parameters
    ----------
    message:
        Human-readable description of the error.

    expression:
        The original mathematical expression where the
        error occurred.

    position:
        Character position where the error occurred.

    exception:
        The original calculator exception, if available.
    """

    message: str

    expression: Optional[str] = None

    position: Optional[int] = None

    exception: Optional[CalculatorError] = None

    # =====================================================
    # Validation
    # =====================================================

    def __post_init__(self):

        if not isinstance(
            self.message,
            str
        ):
            raise TypeError(
                "Error message must be a string."
            )

        if (
            self.expression is not None
            and not isinstance(
                self.expression,
                str
            )
        ):
            raise TypeError(
                "Expression must be a string or None."
            )

        if (
            self.position is not None
            and not isinstance(
                self.position,
                int
            )
        ):
            raise TypeError(
                "Position must be an integer or None."
            )

        if (
            self.position is not None
            and self.position < 0
        ):
            raise ValueError(
                "Position cannot be negative."
            )

        if (
            self.expression is not None
            and self.position is not None
            and self.position >= len(
                self.expression
            )
        ):
            raise ValueError(
                "Position is outside the expression."
            )

        if (
            self.exception is not None
            and not isinstance(
                self.exception,
                CalculatorError
            )
        ):
            raise TypeError(
                "Exception must be a CalculatorError or None."
            )

    # =====================================================
    # Pointer
    # =====================================================

    def pointer(self) -> Optional[str]:
        """
        Return a pointer indicating the error position.

        Example:

            expression = "2+*3"
            position = 2

        Returns:

            "  ^"
        """

        if self.position is None:
            return None

        return " " * self.position + "^"

    # =====================================================
    # Format
    # =====================================================

    def format(self) -> str:
        """
        Format the error information as readable text.

        Examples
        --------

        Without expression:

            Division by zero.

        With expression and position:

            2+*3
              ^
            Unexpected token.
        """

        lines = []

        if self.expression is not None:

            lines.append(
                self.expression
            )

            if self.position is not None:

                lines.append(
                    self.pointer()
                )

        lines.append(
            self.message
        )

        return "\n".join(lines)

    # =====================================================
    # String Representation
    # =====================================================

    def __str__(self) -> str:
        """
        Return the formatted error.
        """

        return self.format()


# =========================================================
# Create Error Information
# =========================================================

def create_error(
    message: str,
    expression: Optional[str] = None,
    position: Optional[int] = None,
    exception: Optional[CalculatorError] = None,
) -> CalculatorErrorInfo:
    """
    Create and return CalculatorErrorInfo.

    This helper makes error creation consistent across
    Tokenizer, Parser, and Evaluator.
    """

    return CalculatorErrorInfo(
        message=message,
        expression=expression,
        position=position,
        exception=exception,
    )