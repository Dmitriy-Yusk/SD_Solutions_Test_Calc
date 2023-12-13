from math import exp, log, sqrt
from src.operations import DivideOperation, LogarithmOperation, PowerOperation, SquareRootOperation


def test_division():
    num1 = 4
    num2 = 2
    standard = num1 / num2

    res = DivideOperation.calculate(num1, num2)

    assert standard == res


def test_division_by_zero():
    num1 = 4
    num2 = 0

    eq = False

    try:
        res = DivideOperation.calculate(num1, num2)
    except ValueError as ex:
    # except ZeroDivisionError as ex:
        eq = True

    assert eq


def test_power_operation():
    result = PowerOperation.calculate(2, 3)
    assert result == pow(2, 3)


def test_logarithm_operation():
    result = LogarithmOperation.calculate(8, 2)
    assert result == log(8, 2)


def test_square_root_operation():
    result = SquareRootOperation.calculate(9)
    assert result == sqrt(9)
