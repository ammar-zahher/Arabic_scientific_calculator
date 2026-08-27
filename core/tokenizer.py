"""
=========================================================
File: tokenizer.py
Folder: core
=========================================================

تحويل التعبير الرياضي إلى Tokens.

هذا الملف لا يقوم بأي عملية حسابية.

يدعم:

- الأعداد الصحيحة
- الأعداد العشرية
- الأعداد العلمية مثل 1.5E-3
- العمليات الرياضية
- الأقواس
- الدوال
- الثوابت
- المتغيرات
- رموز Casio مثل × و ÷
- الاستثناءات المخصصة
=========================================================
"""

from typing import List

from core.tokens import Token, TokenType
from core.operators import OPERATORS

from core.keywords import (
    is_function,
    is_constant,
    is_variable,
)

from core.exceptions import (
    InvalidCharacterError,
    InvalidNumberError,
    UnknownIdentifierError,
)


class Tokenizer:

    def __init__(self, expression: str):

        self.expression = expression
        self.position = 0
        self.length = len(expression)


    # =====================================================
    # Tokenize
    # =====================================================

    def tokenize(self) -> List[Token]:

        tokens = []

        while self.position < self.length:

            char = self.expression[self.position]

            # =================================================
            # Spaces
            # =================================================

            if char.isspace():

                self.position += 1
                continue


            # =================================================
            # Casio multiplication symbol
            # =================================================

            if char == "×":

                tokens.append(
                    Token(
                        TokenType.OPERATOR,
                        "*"
                    )
                )

                self.position += 1
                continue


            # =================================================
            # Casio division symbol
            # =================================================

            if char == "÷":

                tokens.append(
                    Token(
                        TokenType.OPERATOR,
                        "/"
                    )
                )

                self.position += 1
                continue


            # =================================================
            # Number
            # =================================================

            if char.isdigit() or char == ".":

                tokens.append(
                    self._read_number()
                )

                continue


            # =================================================
            # Identifier
            # =================================================

            if char.isalpha():

                tokens.append(
                    self._read_identifier()
                )

                continue


            # =================================================
            # Operator
            # =================================================

            if char in OPERATORS:

                tokens.append(
                    Token(
                        TokenType.OPERATOR,
                        char
                    )
                )

                self.position += 1
                continue


            # =================================================
            # Left Parenthesis
            # =================================================

            if char == "(":

                tokens.append(
                    Token(
                        TokenType.LEFT_PAREN,
                        char
                    )
                )

                self.position += 1
                continue


            # =================================================
            # Right Parenthesis
            # =================================================

            if char == ")":

                tokens.append(
                    Token(
                        TokenType.RIGHT_PAREN,
                        char
                    )
                )

                self.position += 1
                continue


            # =================================================
            # Comma
            # =================================================

            if char == ",":

                tokens.append(
                    Token(
                        TokenType.COMMA,
                        char
                    )
                )

                self.position += 1
                continue


            # =================================================
            # Unknown Character
            # =================================================

            raise InvalidCharacterError(
                f"Unknown character: {char}"
            )


        # =====================================================
        # End Of Expression
        # =====================================================

        tokens.append(
            Token(
                TokenType.EOF,
                None
            )
        )

        return tokens


    # =====================================================
    # Read Number
    # =====================================================

    def _read_number(self) -> Token:
        """
        قراءة الأرقام.

        أمثلة صحيحة:

        12
        12.5
        .5
        100.
        1E3
        1.5E-3
        2E+5

        أمثلة خاطئة:

        .
        12.3.4
        1E
        1E+
        1E-
        1E2E3
        """

        start = self.position

        has_dot = False
        has_exp = False
        has_digit = False


        while self.position < self.length:

            char = self.expression[self.position]


            # =================================================
            # Digit
            # =================================================

            if char.isdigit():

                has_digit = True

                self.position += 1

                continue


            # =================================================
            # Decimal Point
            # =================================================

            if char == ".":

                if has_dot or has_exp:

                    raise InvalidNumberError(
                        "Invalid number"
                    )

                has_dot = True

                self.position += 1

                continue


            # =================================================
            # Scientific Notation
            # =================================================

            if char in ("E", "e"):

                # لا يمكن وجود E مرتين
                # ولا يمكن أن تأتي E بدون رقم قبلها

                if has_exp or not has_digit:

                    raise InvalidNumberError(
                        "Invalid exponent"
                    )

                has_exp = True

                self.position += 1


                # =============================================
                # Optional exponent sign
                # =============================================

                if (
                    self.position < self.length
                    and self.expression[self.position]
                    in ("+", "-")
                ):

                    self.position += 1


                # =============================================
                # يجب وجود رقم واحد على الأقل بعد E
                # =============================================

                exponent_start = self.position


                while (
                    self.position < self.length
                    and self.expression[
                        self.position
                    ].isdigit()
                ):

                    self.position += 1


                if self.position == exponent_start:

                    raise InvalidNumberError(
                        "Invalid exponent"
                    )

                continue


            # =================================================
            # End of Number
            # =================================================

            break


        value = self.expression[
            start:self.position
        ]


        # =====================================================
        # منع الرقم "."
        # =====================================================

        if not has_digit:

            raise InvalidNumberError(
                "Invalid number"
            )


        return Token(
            TokenType.NUMBER,
            value
        )


    # =====================================================
    # Read Identifier
    # =====================================================

    def _read_identifier(self) -> Token:

        start = self.position


        while self.position < self.length:

            char = self.expression[
                self.position
            ]

            if (
                not char.isalpha()
                and not char.isdigit()
                and char != "_"
            ):

                break

            self.position += 1


        value = self.expression[
            start:self.position
        ]


        # =====================================================
        # Function
        # =====================================================

        if is_function(value):

            return Token(
                TokenType.FUNCTION,
                value
            )


        # =====================================================
        # Constant
        # =====================================================

        if is_constant(value):

            return Token(
                TokenType.CONSTANT,
                value
            )


        # =====================================================
        # Variable
        # =====================================================

        if is_variable(value):

            return Token(
                TokenType.VARIABLE,
                value
            )


        # =====================================================
        # Unknown Identifier
        # =====================================================

        raise UnknownIdentifierError(
            f"Unknown identifier: {value}"
        )