
"""
=========================================================
File: parser.py
Folder: core
=========================================================

This file converts the list of Tokens into an Expression Tree.

The Parser does not perform any calculations.

Responsibilities:

Understanding the order of operations.

Applying precedence.

Applying associativity.

Handling Unary Operators.

Handling binary operations.

Handling functions.

Handling parentheses.

Supporting implicit multiplication.

Handling Factorials.

The Parser does not understand Arabic.
It only deals with the engine's internal language.

It uses Pratt / Precedence Climbing Parsing.
=========================================================
"""

from typing import List

from core.tokens import Token, TokenType
from core.operators import OPERATORS, Associativity
from core.precedence import Precedence

from core.expression_tree import (
    ExpressionTree,
    ExpressionNode,
    NumberNode,
    VariableNode,
    ConstantNode,
    UnaryOperationNode,
    BinaryOperationNode,
    FunctionNode,
)


class Parser:

    def __init__(self, tokens: List[Token]):

        self.tokens = tokens
        self.position = 0

    # =====================================================
    # Public API
    # =====================================================

    def parse(self) -> ExpressionTree:

        if not self.tokens:
            raise ValueError(
                "Cannot parse empty token list"
            )

        root = self._parse_expression(
            Precedence.LOWEST
        )

        current = self._current()

        if current.type != TokenType.EOF:

            raise ValueError(
                f"Unexpected token: {current}"
            )

        return ExpressionTree(
            root=root
        )

    # =====================================================
    # Expression Parsing
    # =====================================================

    def _parse_expression(
        self,
        min_precedence: int
    ) -> ExpressionNode:

        left = self._parse_prefix()

        while True:

            token = self._current()

            # =================================================
            # Factorial
            # =================================================

            if (
                token.type == TokenType.OPERATOR
                and token.value == "!"
            ):

                precedence = Precedence.FACTORIAL

                if precedence < min_precedence:
                    break

                self._advance()

                left = UnaryOperationNode(
                    operator="!",
                    operand=left
                )

                continue

            # =================================================
            # Binary Operator
            # =================================================

            if token.type == TokenType.OPERATOR:

                operator = token.value

                if operator == "!":
                    break

                operator_info = OPERATORS.get(operator)

                if operator_info is None:

                    raise ValueError(
                        f"Unknown operator: {operator}"
                    )

                precedence = operator_info.precedence

                if precedence < min_precedence:
                    break

                self._advance()

                # -------------------------------------------------
                # Left associative
                #
                # 2 - 3 - 4
                #
                # becomes:
                #
                # (2 - 3) - 4
                # -------------------------------------------------

                if (
                    operator_info.associativity
                    == Associativity.LEFT
                ):

                    next_min_precedence = (
                        int(precedence) + 1
                    )

                # -------------------------------------------------
                # Right associative
                #
                # 2 ^ 3 ^ 4
                #
                # becomes:
                #
                # 2 ^ (3 ^ 4)
                # -------------------------------------------------

                else:

                    next_min_precedence = int(
                        precedence
                    )

                right = self._parse_expression(
                    next_min_precedence
                )

                left = BinaryOperationNode(
                    operator=operator,
                    left=left,
                    right=right
                )

                continue

            # =================================================
            # Implicit Multiplication
            # =================================================

            if self._starts_implicit_multiplication(
                token
            ):

                precedence = Precedence.MUL_DIV_MOD

                if precedence < min_precedence:
                    break

                right = self._parse_expression(
                    int(precedence) + 1
                )

                left = BinaryOperationNode(
                    operator="*",
                    left=left,
                    right=right
                )

                continue

            break

        return left

    # =====================================================
    # Prefix Parsing
    # =====================================================

    def _parse_prefix(self) -> ExpressionNode:

        token = self._current()

        # =================================================
        # Number
        # =================================================

        if token.type == TokenType.NUMBER:

            self._advance()

            return NumberNode(
                value=token.value
            )

        # =================================================
        # Variable
        # =================================================

        if token.type == TokenType.VARIABLE:

            self._advance()

            return VariableNode(
                name=token.value
            )

        # =================================================
        # Constant
        # =================================================

        if token.type == TokenType.CONSTANT:

            self._advance()

            return ConstantNode(
                name=token.value
            )

        # =================================================
        # Function
        # =================================================

        if token.type == TokenType.FUNCTION:

            return self._parse_function()

        # =================================================
        # Unary + / -
        # =================================================

        if (
            token.type == TokenType.OPERATOR
            and token.value in ("+", "-")
        ):

            self._advance()

            # -------------------------------------------------
            # important:
            #
            # The power must be strictly greater than the signal.
            #
            # so:
            #
            # -2^2
            #
            # becomes:
            #
            # -(2^2)
            #
            # not:
            #
            # (-2)^2
            #
            # We use POWER here instead of UNARY.
            # -------------------------------------------------

            operand = self._parse_expression(
                Precedence.POWER
            )

            return UnaryOperationNode(
                operator=token.value,
                operand=operand
            )

        # =================================================
        # Parentheses
        # =================================================

        if token.type == TokenType.LEFT_PAREN:

            self._advance()

            expression = self._parse_expression(
                Precedence.LOWEST
            )

            self._expect(
                TokenType.RIGHT_PAREN
            )

            return expression

        raise ValueError(
            f"Unexpected token: {token}"
        )

    # =====================================================
    # Function Parsing
    # =====================================================

    def _parse_function(self) -> ExpressionNode:

        token = self._current()

        name = token.value

        self._advance()

        # =================================================
        # Function with parentheses
        # =================================================

        if (
            self._current().type
            == TokenType.LEFT_PAREN
        ):

            self._advance()

            arguments = []

            # -------------------------------------------------
            # FUNC()
            # -------------------------------------------------

            if (
                self._current().type
                == TokenType.RIGHT_PAREN
            ):

                self._advance()

                return FunctionNode(
                    name=name,
                    arguments=arguments
                )

            # -------------------------------------------------
            # First argument
            # -------------------------------------------------

            arguments.append(
                self._parse_expression(
                    Precedence.LOWEST
                )
            )

            # -------------------------------------------------
            # Additional arguments
            # -------------------------------------------------

            while (
                self._current().type
                == TokenType.COMMA
            ):

                self._advance()

                arguments.append(
                    self._parse_expression(
                        Precedence.LOWEST
                    )
                )

            self._expect(
                TokenType.RIGHT_PAREN
            )

            return FunctionNode(
                name=name,
                arguments=arguments
            )

        # =================================================
        # Function without parentheses
        # =================================================

        argument = self._parse_expression(
            Precedence.FUNCTION
        )

        return FunctionNode(
            name=name,
            arguments=[argument]
        )

    # =====================================================
    # Implicit Multiplication
    # =====================================================

    def _starts_implicit_multiplication(
        self,
        token: Token
    ) -> bool:
        """
        It determines whether the next Token will initiate an implicit multiplication process.

        Examples:

            2X
            2PI
            2SIN(30)
            3(4+5)
            (2+3)X

        becomes:

            2 * X
            2 * PI
            2 * SIN(30)
            3 * (4+5)
            (2+3) * X
        """

        return token.type in (
            TokenType.NUMBER,
            TokenType.VARIABLE,
            TokenType.CONSTANT,
            TokenType.FUNCTION,
            TokenType.LEFT_PAREN
        )

    # =====================================================
    # Token Helpers
    # =====================================================

    def _current(self) -> Token:

        if self.position >= len(self.tokens):

            raise ValueError(
                "Unexpected end of token stream"
            )

        return self.tokens[self.position]

    def _advance(self) -> Token:

        token = self._current()

        self.position += 1

        return token

    def _expect(
        self,
        token_type: TokenType
    ) -> Token:

        token = self._current()

        if token.type != token_type:

            raise ValueError(
                f"Expected {token_type.name}, "
                f"got {token.type.name}"
            )

        self.position += 1

        return token
