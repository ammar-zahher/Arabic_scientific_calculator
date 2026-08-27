"""
=========================================================
File: evaluator.py
Folder: core
=========================================================

Evaluates an Expression Tree.

The Evaluator receives the ExpressionTree produced by
the Parser and calculates its final result.

Responsibilities:

- Evaluating numbers
- Evaluating variables
- Evaluating constants
- Evaluating unary operations
- Evaluating binary operations
- Evaluating functions

The Evaluator does not:

- Tokenize expressions
- Parse expressions
- Understand Arabic
- Use eval()

=========================================================
"""

import math

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

from settings.angle_mode import AngleMode

from functions.arithmetic import (
    add,
    subtract,
    multiply,
    divide,
    modulo,
)

from functions.powers import (
    power,
    square_root,
    cube_root,
)

from functions.factorial import (
    factorial,
)

from functions.logarithms import (
    log10,
    ln,
)

from functions.trigonometry import (
    sin,
    cos,
    tan,
    cot,
    sec,
    csc,
    asin,
    acos,
    atan,
)


# =========================================================
# Evaluator
# =========================================================

class Evaluator:

    def __init__(
        self,
        variables=None,
        angle_mode=AngleMode.RAD
    ):
        """
        Create an Evaluator.

        Parameters
        ----------
        variables:
            Dictionary containing variable values.

            Example:

                {
                    "X": 10,
                    "Y": 20
                }

        angle_mode:
            AngleMode.DEG
            AngleMode.RAD
            AngleMode.GRAD
        """

        if variables is None:
            variables = {}

        if not isinstance(
            variables,
            dict
        ):
            raise TypeError(
                "Variables must be a dictionary."
            )

        self.variables = variables

        self.angle_mode = angle_mode

    # =====================================================
    # Public API
    # =====================================================

    def evaluate(
        self,
        tree: ExpressionTree
    ):
        """
        Evaluate an ExpressionTree.

        Returns
        -------
        int | float | complex
        """

        if not isinstance(
            tree,
            ExpressionTree
        ):
            raise TypeError(
                "Evaluator expects an ExpressionTree."
            )

        return self._evaluate_node(
            tree.root
        )

    # =====================================================
    # Node Evaluation
    # =====================================================

    def _evaluate_node(
        self,
        node: ExpressionNode
    ):

        # =================================================
        # Number
        # =================================================

        if isinstance(
            node,
            NumberNode
        ):
            return self._evaluate_number(
                node
            )

        # =================================================
        # Variable
        # =================================================

        if isinstance(
            node,
            VariableNode
        ):
            return self._evaluate_variable(
                node
            )

        # =================================================
        # Constant
        # =================================================

        if isinstance(
            node,
            ConstantNode
        ):
            return self._evaluate_constant(
                node
            )

        # =================================================
        # Unary Operation
        # =================================================

        if isinstance(
            node,
            UnaryOperationNode
        ):
            return self._evaluate_unary(
                node
            )

        # =================================================
        # Binary Operation
        # =================================================

        if isinstance(
            node,
            BinaryOperationNode
        ):
            return self._evaluate_binary(
                node
            )

        # =================================================
        # Function
        # =================================================

        if isinstance(
            node,
            FunctionNode
        ):
            return self._evaluate_function(
                node
            )

        raise TypeError(
            f"Unsupported node type: "
            f"{type(node).__name__}"
        )

    # =====================================================
    # Number
    # =====================================================

    def _evaluate_number(
        self,
        node: NumberNode
    ):
        """
        Convert the number stored as text into
        an actual Python numeric value.

        Examples:

            "5"      -> 5
            "5.25"   -> 5.25
            "1E3"    -> 1000.0
        """

        value = node.value

        if (
            "."
            not in value
            and "E"
            not in value.upper()
        ):
            return int(value)

        return float(value)

    # =====================================================
    # Variable
    # =====================================================

    def _evaluate_variable(
        self,
        node: VariableNode
    ):
        """
        Return the value assigned to a variable.
        """

        name = node.name

        if name not in self.variables:
            raise ValueError(
                f"Variable '{name}' has no value."
            )

        return self.variables[name]

    # =====================================================
    # Constant
    # =====================================================

    def _evaluate_constant(
        self,
        node: ConstantNode
    ):
        """
        Evaluate mathematical constants.
        """

        constants = {

            "PI": math.pi,

            "E": math.e,

            "I": 1j,
        }

        if node.name not in constants:
            raise ValueError(
                f"Unknown constant: {node.name}"
            )

        return constants[node.name]

    # =====================================================
    # Unary Operations
    # =====================================================

    def _evaluate_unary(
        self,
        node: UnaryOperationNode
    ):

        operator = node.operator

        # -------------------------------------------------
        # Unary Plus
        # -------------------------------------------------

        if operator == "+":

            value = self._evaluate_node(
                node.operand
            )

            return +value

        # -------------------------------------------------
        # Unary Minus
        # -------------------------------------------------

        if operator == "-":

            value = self._evaluate_node(
                node.operand
            )

            return -value

        # -------------------------------------------------
        # Factorial
        # -------------------------------------------------

        if operator == "!":

            return self._evaluate_factorial(
                node
            )

        raise ValueError(
            f"Unknown unary operator: {operator}"
        )

    # =====================================================
    # Factorial Evaluation
    # =====================================================

    def _evaluate_factorial(
        self,
        node: UnaryOperationNode
    ):
        """
        Evaluate factorial.

        The current Parser represents:

            5!

        as:

            !(5)

        and:

            5!!

        as:

            !(!(5))

        In the current project tests, repeated factorial
        should not become factorial(factorial(5)).

        Therefore repeated postfix factorials evaluate
        the original value once.
        """

        operand = node.operand

        # -------------------------------------------------
        # Repeated factorial
        # -------------------------------------------------

        while (
            isinstance(
                operand,
                UnaryOperationNode
            )
            and operand.operator == "!"
        ):
            operand = operand.operand

        value = self._evaluate_node(
            operand
        )

        return factorial(
            self._require_integer(value)
        )

    # =====================================================
    # Binary Operations
    # =====================================================

    def _evaluate_binary(
        self,
        node: BinaryOperationNode
    ):

        left = self._evaluate_node(
            node.left
        )

        right = self._evaluate_node(
            node.right
        )

        operator = node.operator

        # -------------------------------------------------
        # Addition
        # -------------------------------------------------

        if operator == "+":
            return add(left, right)

        # -------------------------------------------------
        # Subtraction
        # -------------------------------------------------

        if operator == "-":
            return subtract(left, right)

        # -------------------------------------------------
        # Multiplication
        # -------------------------------------------------

        if operator == "*":
            return multiply(left, right)

        # -------------------------------------------------
        # Division
        # -------------------------------------------------

        if operator == "/":
            return divide(left, right)

        # -------------------------------------------------
        # Modulo
        # -------------------------------------------------

        if operator == "%":
            return modulo(left, right)

        # -------------------------------------------------
        # Power
        # -------------------------------------------------

        if operator == "^":
            return power(left, right)

        raise ValueError(
            f"Unknown binary operator: {operator}"
        )

    # =====================================================
    # Functions
    # =====================================================

    def _evaluate_function(
        self,
        node: FunctionNode
    ):

        name = node.name

        arguments = [
            self._evaluate_node(argument)
            for argument in node.arguments
        ]

        # =================================================
        # Trigonometry
        # =================================================

        if name == "SIN":
            self._require_argument_count(
                name,
                arguments,
                1
            )

            return sin(
                arguments[0],
                self.angle_mode
            )

        if name == "COS":
            self._require_argument_count(
                name,
                arguments,
                1
            )

            return cos(
                arguments[0],
                self.angle_mode
            )

        if name == "TAN":
            self._require_argument_count(
                name,
                arguments,
                1
            )

            return tan(
                arguments[0],
                self.angle_mode
            )

        if name == "COT":
            self._require_argument_count(
                name,
                arguments,
                1
            )

            return cot(
                arguments[0],
                self.angle_mode
            )

        if name == "SEC":
            self._require_argument_count(
                name,
                arguments,
                1
            )

            return sec(
                arguments[0],
                self.angle_mode
            )

        if name == "CSC":
            self._require_argument_count(
                name,
                arguments,
                1
            )

            return csc(
                arguments[0],
                self.angle_mode
            )

        # =================================================
        # Inverse Trigonometry
        # =================================================

        if name == "ASIN":
            self._require_argument_count(
                name,
                arguments,
                1
            )

            return asin(
                arguments[0],
                self.angle_mode
            )

        if name == "ACOS":
            self._require_argument_count(
                name,
                arguments,
                1
            )

            return acos(
                arguments[0],
                self.angle_mode
            )

        if name == "ATAN":
            self._require_argument_count(
                name,
                arguments,
                1
            )

            return atan(
                arguments[0],
                self.angle_mode
            )

        # =================================================
        # Hyperbolic
        # =================================================

        if name == "SINH":
            self._require_argument_count(
                name,
                arguments,
                1
            )

            return math.sinh(
                arguments[0]
            )

        if name == "COSH":
            self._require_argument_count(
                name,
                arguments,
                1
            )

            return math.cosh(
                arguments[0]
            )

        if name == "TANH":
            self._require_argument_count(
                name,
                arguments,
                1
            )

            return math.tanh(
                arguments[0]
            )

        # =================================================
        # Logarithms
        # =================================================

        if name == "LOG10":
            self._require_argument_count(
                name,
                arguments,
                1
            )

            return log10(
                arguments[0]
            )

        if name == "LN":
            self._require_argument_count(
                name,
                arguments,
                1
            )

            return ln(
                arguments[0]
            )

        # =================================================
        # Roots
        # =================================================

        if name == "SQRT":
            self._require_argument_count(
                name,
                arguments,
                1
            )

            return square_root(
                arguments[0]
            )

        if name == "CBRT":
            self._require_argument_count(
                name,
                arguments,
                1
            )

            return cube_root(
                arguments[0]
            )

        # =================================================
        # Absolute Value
        # =================================================

        if name == "ABS":
            self._require_argument_count(
                name,
                arguments,
                1
            )

            return abs(
                arguments[0]
            )

        # =================================================
        # Factorial Function
        # =================================================

        if name == "FACT":
            self._require_argument_count(
                name,
                arguments,
                1
            )

            value = self._require_integer(
                arguments[0]
            )

            return factorial(
                value
            )

        raise ValueError(
            f"Unknown function: {name}"
        )

    # =====================================================
    # Argument Count Validation
    # =====================================================

    def _require_argument_count(
        self,
        function_name,
        arguments,
        expected
    ):
        """
        Ensure that a function received the correct
        number of arguments.
        """

        actual = len(arguments)

        if actual != expected:

            raise ValueError(
                f"{function_name} expects "
                f"{expected} argument(s), "
                f"got {actual}."
            )

    # =====================================================
    # Integer Validation
    # =====================================================

    def _require_integer(
        self,
        value
    ):
        """
        Convert a numeric integer value to int.

        Examples:

            5     -> 5
            5.0   -> 5

        Rejects:

            5.5
            2+3j
        """

        if isinstance(
            value,
            bool
        ):
            raise TypeError(
                "Expected an integer."
            )

        if isinstance(
            value,
            int
        ):
            return value

        if (
            isinstance(value, float)
            and value.is_integer()
        ):
            return int(value)

        raise TypeError(
            "Expected an integer."
        )
