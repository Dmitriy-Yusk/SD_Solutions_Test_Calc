from typing import Dict
from src.operations import OperationBase, OperatorEnum


class BasicCalculator:
    def __init__(self, operations: Dict[OperatorEnum, OperationBase]):
        self._operations = operations

    def calculate(self, operand1: float, operand2: float, operator: OperatorEnum) -> float:
        if operator in self._operations:
            operation = self._operations[operator]
            return operation.calculate(operand1, operand2)
        else:
            raise ValueError(f"Unsupported operator: {operator}")
