from typing import Dict
from enum import Enum
from abc import ABC
from math import exp, log, sqrt, pow


class OperatorEnum(str, Enum):
    ADD = '+'
    SUBTRACT = '-'
    MULTIPLY = '*'
    DIVIDE = '/'
    POWER = "^"
    LOGARITHM = "log"
    SQUARE_ROOT = "sqrt"


class OperationBase(ABC):
    params_num: int = 2

    @classmethod
    def calculate(cls, num1: float, num2: float) -> float:
        pass


class AddOperation(OperationBase):
    @classmethod
    def calculate(cls, num1: float, num2: float) -> float:
        return num1 + num2


class SubtractOperation(OperationBase):
    @classmethod
    def calculate(cls, num1: float, num2: float) -> float:
        return num1 - num2


class MultiplyOperation(OperationBase):
    @classmethod
    def calculate(cls, num1: float, num2: float) -> float:
        return num1 * num2


class DivideOperation(OperationBase):
    @classmethod
    def calculate(cls, num1: float, num2: float) -> float:
        if num2 == 0:
            raise ValueError('Cannot divide by zero')
        return num1 / num2


class PowerOperation(OperationBase):
    @classmethod
    def calculate(cls, num1: float, num2: float) -> float:
        return pow(num1, num2)


class LogarithmOperation(OperationBase):
    @classmethod
    def calculate(cls, num: float, base: float) -> float:
        return log(num, base)


class SquareRootOperation(OperationBase):
    params_num: int = 1

    @classmethod
    def calculate(cls, num: float) -> float:
        return sqrt(num)


_basic_operations = {
    OperatorEnum.ADD:      AddOperation,
    OperatorEnum.SUBTRACT: SubtractOperation,
    OperatorEnum.MULTIPLY: MultiplyOperation,
    OperatorEnum.DIVIDE:   DivideOperation,
}

_extended_operations = {
    **_basic_operations,
    OperatorEnum.LOGARITHM:   LogarithmOperation,
    OperatorEnum.POWER:       PowerOperation,
    OperatorEnum.SQUARE_ROOT: SquareRootOperation,
}


def get_basic_operations() -> Dict:
    return _basic_operations


def get_extended_operations() -> Dict:
    return _extended_operations
