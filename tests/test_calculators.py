from src.calculators import BasicCalculator, Tokenizer, AdvancedCalculator
from src.operations import OperatorEnum, AddOperation, SubtractOperation, MultiplyOperation, DivideOperation
from src.operations import get_basic_operations, get_extended_operations
import pytest


@pytest.fixture
def basic_calculator():
    operations = get_basic_operations()
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


def test_tokenizer():
    # Test basic tokenization
    assert Tokenizer.tokenize('1 + 2') == ['1', '+', '2']

    assert Tokenizer.tokenize('1 + 4/2') == ['1', '+', '4', '/', '2']

    assert Tokenizer.tokenize('3 * (4 - 2)') == ['3', '*', '(', '4', '-', '2', ')']

    assert Tokenizer.tokenize('1.5 * 2.5') == ['1.5', '*', '2.5']


def test_tokenizer_sqrt():
    assert Tokenizer.tokenize('sqrt(9)') == ['sqrt', '(', '9', ')']


def test_tokenizer_log():
    assert Tokenizer.tokenize('log(8, 2)') == ['log', '(', '8', '2', ')']


def test_tokenizer_log_sqrt():
    assert Tokenizer.tokenize('2 ^ log(8, 2) + sqrt(9)') == ['2', '^', 'log', '(', '8', '2', ')', '+', 'sqrt', '(', '9', ')']


def test_tokenizer_nested_func():
    assert Tokenizer.tokenize('log(sqrt(64), (2*3))') == ['log', '(', 'sqrt', '(', '64', ')', '(', '2', '*', '3', ')', ')']


def test_get_ordering():
    # Test basic operators
    assert AdvancedCalculator._get_ordering(OperatorEnum.ADD.value) == 1
    assert AdvancedCalculator._get_ordering(OperatorEnum.SUBTRACT.value) == 1
    assert AdvancedCalculator._get_ordering(OperatorEnum.MULTIPLY.value) == 2
    assert AdvancedCalculator._get_ordering(OperatorEnum.DIVIDE.value) == 2

    # Test advanced operators
    assert AdvancedCalculator._get_ordering(OperatorEnum.POWER.value) == 3
    assert AdvancedCalculator._get_ordering(OperatorEnum.LOGARITHM.value) == 3
    assert AdvancedCalculator._get_ordering(OperatorEnum.SQUARE_ROOT.value) == 3

    # Test unknown operator
    assert AdvancedCalculator._get_ordering('unknown') == 0


def test_apply_operator():
    operations = get_extended_operations()

    # Test addition
    operand_stack = [2, 3]
    operator_stack = [OperatorEnum.ADD.value]
    AdvancedCalculator._apply_operator(operand_stack, operator_stack, operations)
    assert operand_stack == [5]

    # Test subtraction
    operand_stack = [5, 3]
    operator_stack = [OperatorEnum.SUBTRACT.value]
    AdvancedCalculator._apply_operator(operand_stack, operator_stack, operations)
    assert operand_stack == [2]

    # Test multiplication
    operand_stack = [2, 3]
    operator_stack = [OperatorEnum.MULTIPLY.value]
    AdvancedCalculator._apply_operator(operand_stack, operator_stack, operations)
    assert operand_stack == [6]

    # Test division
    operand_stack = [6, 3]
    operator_stack = [OperatorEnum.DIVIDE.value]
    AdvancedCalculator._apply_operator(operand_stack, operator_stack, operations)
    assert operand_stack == [2]

    # Test exponentiation
    operand_stack = [2, 3]
    operator_stack = [OperatorEnum.POWER.value]
    AdvancedCalculator._apply_operator(operand_stack, operator_stack, operations)
    assert operand_stack == [8]

    # Test logarithm
    operand_stack = [8, 2]
    operator_stack = [OperatorEnum.LOGARITHM.value]
    AdvancedCalculator._apply_operator(operand_stack, operator_stack, operations)
    assert operand_stack == [3]

    # Test square root
    operand_stack = [9]
    operator_stack = [OperatorEnum.SQUARE_ROOT.value]
    AdvancedCalculator._apply_operator(operand_stack, operator_stack, operations)
    assert operand_stack == [3]


def test_calculate():
    operations = get_extended_operations()
    calculator = AdvancedCalculator(operations, tokenizer_class=Tokenizer)

    # Test basic arithmetic operations
    assert calculator.calculate('2 + 3') == 5
    assert calculator.calculate('4 - 2') == 2
    assert calculator.calculate('2 * 3') == 6
    assert calculator.calculate('6 / 3') == 2

    # Test advanced operations
    assert calculator.calculate('2 ^ 3') == 8
    assert calculator.calculate('log(8, 2)') == 3
    assert calculator.calculate('sqrt(9)') == 3

    # Test combination of operations
    assert calculator.calculate('2 + 3 * 4') == 14
    assert calculator.calculate('(2 + 3) * 4') == 20
    assert calculator.calculate('2+3*4/2') == 8

    assert calculator.calculate('2 ^ 3 + sqrt(9)') == 11

    assert calculator.calculate('4 + 6/sqrt(9) - 5') == 1

    assert calculator.calculate('1 + (2 - (3 * 4))') == -9

    # Test complex expression
    assert calculator.calculate('2 + 3 * (4 - 2) / sqrt(9)') == 4


def test_calculate_negative_scenarios():
    operations = get_extended_operations()
    calculator = AdvancedCalculator(operations, tokenizer_class=Tokenizer)

    try:
        assert calculator.calculate('2 + + 3') == 5
    except IndexError as ex:
        pass

    try:
        assert calculator.calculate('2 /') == 5
    except IndexError as ex:
        pass

    try:
        assert calculator.calculate(' /2') == 5
    except IndexError as ex:
        pass

    try:
        assert calculator.calculate('sqrt') == 5
    except IndexError as ex:
        pass

    try:
        assert calculator.calculate('sqrt(') == 5
    except ValueError as ex:
        pass

    try:
        assert calculator.calculate('sqrt(1') == 5
    except ValueError as ex:
        pass

    assert True
