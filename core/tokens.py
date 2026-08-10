"""
=========================================================
File: tokens.py
Folder: core
=========================================================

This file contains the definitions of all token types used
within the calculator engine.

This file is completely independent of:
- Arabic language
- User Interface (UI)
- Mathematical operations

It is simply a definition of tokens only.
"""

from dataclasses import dataclass
from enum import Enum, auto
from typing import Any


class TokenType(Enum):
    """
All types of tokens that the tokenizer can produce.
"""
    # ==========================
    # Values
    # ==========================
    NUMBER = auto()          # 12   5.6

    # ==========================
    # Operators
    # ==========================
    OPERATOR = auto()        # + - * / ^ %

    # ==========================
    # Functions
    # ==========================
    FUNCTION = auto()        # SIN LOG SQRT ...

    # ==========================
    # Constants
    # ==========================
    CONSTANT = auto()        # PI E I

    # ==========================
    # Variables
    # ==========================
    VARIABLE = auto()        # X Y A B ...

    # ==========================
    # Parentheses
    # ==========================
    LEFT_PAREN = auto()      # (
    RIGHT_PAREN = auto()     # )

    # ==========================
    # Separators
    # ==========================
    COMMA = auto()           # ,

    # ==========================
    # End Of Expression
    # ==========================
    EOF = auto()


@dataclass(frozen=True)
class Token:
    """
Represents a single token within a mathematical expression.

Examples:

    NUMBER     -> 25

    FUNCTION   -> SIN

    OPERATOR   -> +

    CONSTANT   -> PI
"""

    type: TokenType
    value: Any

    def __str__(self) -> str:
        return f"{self.type.name}({self.value})"

    def __repr__(self) -> str:
        return self.__str__()
