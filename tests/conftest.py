import pytest
from fastapi import FastAPI
from starlette.testclient import TestClient

import logging
from src.main import app as orig_app


@pytest.fixture
def app() -> FastAPI:
    testing_app = orig_app

    return testing_app


@pytest.fixture
def client(app: FastAPI) -> TestClient:
    return TestClient(app)


def pytest_configure(config):
    pass
