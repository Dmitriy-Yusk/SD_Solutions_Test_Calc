from src.operations import DivideOperation


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
