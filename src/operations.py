from enum import Enum
from abc import ABC
# from math import exp, log, sqrt


class OperatorEnum(str, Enum):
    ADD = '+'
    SUBTRACT = '-'
    MULTIPLY = '*'
    DIVIDE = '/'


class OperationBase(ABC):
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
