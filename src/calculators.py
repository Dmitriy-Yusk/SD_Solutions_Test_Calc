from typing import Dict
import re

from src.operations import OperationBase, OperatorEnum


class BasicCalculator:
    def __init__(self, operations: Dict[OperatorEnum, OperationBase]):
        self._operations = operations

    def calculate(self, operand1: float, operand2: float, operator: OperatorEnum) -> float:
        if operator in self._operations:
            operation = self._operations[operator]
            return operation.calculate(operand1, operand2)
        else:
            raise ValueError(f'Unsupported operator: {operator}')


class Tokenizer:
    @staticmethod
    def tokenize(expression: str):
        pattern = re.compile(r'\d*\.?\d+|[()+\-*/^]|(?:log|sqrt)')
        tokens = re.findall(pattern, expression)

        if len(tokens) < 1:
            raise ValueError(f'Nothing to calculate in expression: {expression}')

        return tokens


class AdvancedCalculator:
    def __init__(self, operations: Dict[OperatorEnum, OperationBase], tokenizer_class: Tokenizer):
        self._operations = operations
        self._tokenizer_class = tokenizer_class

    def calculate(self, expression: str) -> float:
        tokens = self._tokenizer_class.tokenize(expression)
        operand_stack = []
        operator_stack = []

        for token in tokens:
            if token == "(":
                operator_stack.append(token)
            elif token == ")":
                while operator_stack and operator_stack[-1] != "(":
                    self._apply_operator(operand_stack, operator_stack, self._operations)
                operator_stack.pop()  # Pop the open parenthesis
            elif token in self._operations:
                while operator_stack and operator_stack[-1] in self._operations and self._get_ordering(operator_stack[-1]) >= self._get_ordering(token):
                    self._apply_operator(operand_stack, operator_stack, self._operations)
                operator_stack.append(token)
            else:
                operand_stack.append(float(token))

        if len(operator_stack) < 1 < len(operand_stack):
            raise ValueError("Invalid operator")

        while operator_stack:
            self._apply_operator(operand_stack, operator_stack, self._operations)

        return operand_stack[0]

    @staticmethod
    def _get_ordering(operator: str):
        # Define the ordering of operators
        ordering = {
            OperatorEnum.ADD.value:         1,
            OperatorEnum.SUBTRACT.value:    1,
            OperatorEnum.MULTIPLY.value:    2,
            OperatorEnum.DIVIDE.value:      2,
            OperatorEnum.POWER.value:       3,
            OperatorEnum.LOGARITHM.value:   3,
            OperatorEnum.SQUARE_ROOT.value: 3
        }

        return ordering.get(operator, 0)

    @staticmethod
    def _apply_operator(operand_stack, operator_stack, operations):
        operator = operator_stack.pop()
        if operator in operations:
            operation = operations[operator]

            operand2 = operand_stack.pop()

            if operation.params_num > 1:
                operand1 = operand_stack.pop()
                result = operation.calculate(operand1, operand2)
            else:
                operand1 = operand2
                result = operation.calculate(operand1)

            operand_stack.append(result)
        else:
            raise ValueError("Invalid operator")
