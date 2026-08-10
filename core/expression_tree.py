"""
=========================================================
File: expression_tree.py
Folder: core
=========================================================

"""

from dataclasses import dataclass
from typing import List


# =========================================================
# Base Node
# =========================================================

class ExpressionNode:
    pass


# =========================================================
# Number Node
# =========================================================

@dataclass(frozen=True)
class NumberNode(ExpressionNode):
    value: str


# =========================================================
# Variable Node
# =========================================================

@dataclass(frozen=True)
class VariableNode(ExpressionNode):

    name: str


# =========================================================
# Constant Node
# =========================================================

@dataclass(frozen=True)
class ConstantNode(ExpressionNode):

    name: str


# =========================================================
# Unary Operation Node
# =========================================================

@dataclass(frozen=True)
class UnaryOperationNode(ExpressionNode):

    operator: str
    operand: ExpressionNode


# =========================================================
# Binary Operation Node
# =========================================================

@dataclass(frozen=True)
class BinaryOperationNode(ExpressionNode):
    operator: str
    left: ExpressionNode
    right: ExpressionNode


# =========================================================
# Function Node
# =========================================================

@dataclass(frozen=True)
class FunctionNode(ExpressionNode):

    name: str
    arguments: List[ExpressionNode]


# =========================================================
# Expression Tree
# =========================================================

@dataclass(frozen=True)
class ExpressionTree:

    root: ExpressionNode
