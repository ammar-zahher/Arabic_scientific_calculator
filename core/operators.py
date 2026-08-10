"""
=========================================================
File: operators.py
Folder: core
=========================================================

"""

from dataclasses import dataclass
from enum import Enum
from typing import Dict

from core.precedence import Precedence


class Associativity(Enum):

    LEFT = "LEFT"
    RIGHT = "RIGHT"


@dataclass(frozen=True)
class Operator:

    symbol: str
    precedence: Precedence
    associativity: Associativity
    operands: int


OPERATORS: Dict[str, Operator] = {

    "+": Operator(
        symbol="+",
        precedence=Precedence.ADD_SUB,
        associativity=Associativity.LEFT,
        operands=2
    ),

    "-": Operator(
        symbol="-",
        precedence=Precedence.ADD_SUB,
        associativity=Associativity.LEFT,
        operands=2
    ),

    "*": Operator(
        symbol="*",
        precedence=Precedence.MUL_DIV_MOD,
        associativity=Associativity.LEFT,
        operands=2
    ),

    "/": Operator(
        symbol="/",
        precedence=Precedence.MUL_DIV_MOD,
        associativity=Associativity.LEFT,
        operands=2
    ),

    "%": Operator(
        symbol="%",
        precedence=Precedence.MUL_DIV_MOD,
        associativity=Associativity.LEFT,
        operands=2
    ),

    "^": Operator(
        symbol="^",
        precedence=Precedence.POWER,
        associativity=Associativity.RIGHT,
        operands=2
    ),

    "!": Operator(
        symbol="!",
        precedence=Precedence.FACTORIAL,
        associativity=Associativity.LEFT,
        operands=1
    ),
}
