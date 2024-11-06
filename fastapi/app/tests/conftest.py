from typing import Generator, List

import pytest
from fastapi.testclient import TestClient

from app.main import app


@pytest.fixture(scope="module")
def test_data() -> List:
    inputs = [
        {
            "fixed acidity": 5.9,
            "volatile acidity": 0.645,
            "citric acid": 0.12,
            "residual sugar": 2.0,
            "chlorides": 0.075,
            "free sulfur dioxide": 32.0,
            "total sulfur dioxide": 44.0,
            "sulphates": 0.71,
            "alcohol": 10.2,
        },
        {
            "fixed acidity": 8.5,
            "volatile acidity": 0.28,
            "citric acid": 0.56,
            "residual sugar": 1.8,
            "chlorides": 0.092,
            "free sulfur dioxide": 35.0,
            "total sulfur dioxide": 103.0,
            "sulphates": 0.75,
            "alcohol": 10.5,
        },
    ]

    return inputs


@pytest.fixture()
def client() -> Generator:
    with TestClient(app) as _client:
        yield _client
        app.dependency_overrides = {}
