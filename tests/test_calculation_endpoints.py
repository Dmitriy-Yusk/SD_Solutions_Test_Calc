from starlette.testclient import TestClient
from src.operations import OperatorEnum, AddOperation, SubtractOperation, MultiplyOperation, DivideOperation


def test_calculate_addition(client: TestClient):
    params = {
        'operand1': 2,
        'operand2': 3,
        'operator': OperatorEnum.ADD.value
    }
    response = client.get('/api/v1/calculate', params=params)

    assert response.status_code == 200
    assert response.json() == {'result': 5.0}


def test_calculate_subtraction(client: TestClient):
    params = {
        'operand1': 5,
        'operand2': 3,
        'operator': OperatorEnum.SUBTRACT.value
    }
    response = client.get('/api/v1/calculate', params=params)

    assert response.status_code == 200
    assert response.json() == {'result': 2}


def test_calculate_multiplication(client: TestClient):
    params = {
        'operand1': 2,
        'operand2': 3,
        'operator': OperatorEnum.MULTIPLY.value
    }
    response = client.get('/api/v1/calculate', params=params)
    assert response.status_code == 200
    assert response.json() == {'result': 6}


def test_calculate_division(client: TestClient):
    params = {
        'operand1': 6,
        'operand2': 3,
        'operator': OperatorEnum.DIVIDE.value
    }
    response = client.get('/api/v1/calculate', params=params)

    assert response.status_code == 200
    assert response.json() == {'result': 2}


def test_calculate_division_by_zero(client: TestClient):
    params = {
        'operand1': 6,
        'operand2': 0,
        'operator': OperatorEnum.DIVIDE.value
    }
    response = client.get('/api/v1/calculate', params=params)

    assert response.status_code == 400
    assert response.json() == {'detail': 'Cannot divide by zero'}
