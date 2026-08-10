"""
=========================================================
File: tokenizer.py
Folder: core
=========================================================

The Tokenizer converts the mathematical expression into Tokens.

It does not perform calculations.

Supports:

Standard numbers

Scientific notation numbers

Operations

Parentheses

Functions

Constants

Variables
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



class Tokenizer:


    def __init__(self, expression: str):

        self.expression = expression

        self.position = 0

        self.length = len(expression)



    def tokenize(self) -> List[Token]:

        tokens = []


        while self.position < self.length:


            char = self.expression[self.position]


            # Ignore the spaces
            if char.isspace():

                self.position += 1
                continue



            # Casio symbols conversion
            if char == "×":

                char = "*"


            elif char == "÷":

                char = "/"



            # Read number
            if char.isdigit() or char == ".":

                tokens.append(
                    self._read_number()
                )

                continue



            # Read word
            if char.isalpha():

                tokens.append(
                    self._read_identifier()
                )

                continue



            # Operation
            if char in OPERATORS:

                tokens.append(
                    Token(
                        TokenType.OPERATOR,
                        char
                    )
                )

                self.position += 1

                continue



            # Open parenthesis
            if char == "(":

                tokens.append(
                    Token(
                        TokenType.LEFT_PAREN,
                        char
                    )
                )

                self.position += 1

                continue



            # Closing parenthesis
            if char == ")":

                tokens.append(
                    Token(
                        TokenType.RIGHT_PAREN,
                        char
                    )
                )

                self.position += 1

                continue



            # Comma
            if char == ",":

                tokens.append(
                    Token(
                        TokenType.COMMA,
                        char
                    )
                )

                self.position += 1

                continue



            raise ValueError(
                f"Unknown character: {char}"
            )



        tokens.append(
            Token(
                TokenType.EOF,
                None
            )
        )


        return tokens




    def _read_number(self) -> Token:
        """
Reading:

12
12.5
1E3
1.5E-3
"""

        start = self.position


        has_dot = False

        has_exp = False



        while self.position < self.length:


            char = self.expression[self.position]



            # number
            if char.isdigit():

                self.position += 1

                continue



            # Decimal point
            if char == ".":


                if has_dot:

                    raise ValueError(
                        "Invalid number"
                    )


                has_dot = True

                self.position += 1

                continue




            # powwer E

            if char in ("E", "e"):


                if has_exp:

                    raise ValueError(
                        "Invalid exponent"
                    )


                has_exp = True

                self.position += 1



                # Exponent sign

                if self.position < self.length:

                    if self.expression[self.position] in ("+", "-"):

                        self.position += 1


                continue




            break



        value = self.expression[start:self.position]


        return Token(
            TokenType.NUMBER,
            value
        )





    def _read_identifier(self) -> Token:


        start = self.position



        while self.position < self.length:


            char = self.expression[self.position]


            if not char.isalpha() and not char.isdigit():

                break


            self.position += 1



        value = self.expression[start:self.position]



        if is_function(value):

            return Token(
                TokenType.FUNCTION,
                value
            )



        if is_constant(value):

            return Token(
                TokenType.CONSTANT,
                value
            )



        if is_variable(value):

            return Token(
                TokenType.VARIABLE,
                value
            )



        raise ValueError(
            f"Unknown identifier: {value}"
        )
