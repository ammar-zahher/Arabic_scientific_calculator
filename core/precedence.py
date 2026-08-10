"""
=========================================================
File: precedence.py
Folder: core
=========================================================

This file contains the order of operations in mathematical operations.

Having the order of operations in a separate file prevents the use of magic numbers and makes future modifications easier.
"""

from enum import IntEnum


class Precedence(IntEnum):
    """
    Priority of mathematical operations.

    The higher the value, the higher the priority given to executing the operation.
    """

    LOWEST = 0

    ADD_SUB = 10          # + -

    MUL_DIV_MOD = 20      # * / %

    POWER = 30            # ^

    UNARY = 40            # +x  -x

    FACTORIAL = 50        # !

    FUNCTION = 60         # sin() log() sqrt()

    ATOM = 100            # Number, Constant, Variable
