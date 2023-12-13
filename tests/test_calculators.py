from src.calculators import BasicCalculator
from src.operations import OperatorEnum, AddOperation, SubtractOperation, MultiplyOperation, DivideOperation
import pytest


@pytest.fixture
def basic_calculator():
    operations = {
        OperatorEnum.ADD: AddOperation,
        OperatorEnum.SUBTRACT: SubtractOperation,
        OperatorEnum.MULTIPLY: MultiplyOperation,
        OperatorEnum.DIVIDE: DivideOperation,
    }
    return BasicCalculator(operations=operations)


def test_basic_addition(basic_calculator):
    result = basic_calculator.calculate(2, 3, OperatorEnum.ADD)
    assert result == 5


def test_basic_subtraction(basic_calculator):
    result = basic_calculator.calculate(5, 3, OperatorEnum.SUBTRACT)
    assert result == 2


def test_basic_multiplication(basic_calculator):
    result = basic_calculator.calculate(2, 3, OperatorEnum.MULTIPLY)
    assert result == 6


def test_basic_division(basic_calculator):
    result = basic_calculator.calculate(6, 3, OperatorEnum.DIVIDE)
    assert result == 2


def test_basic_division_by_zero(basic_calculator):
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        basic_calculator.calculate(5, 0, OperatorEnum.DIVIDE)

