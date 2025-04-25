from http import HTTPStatus

import pytest
from fastapi.testclient import TestClient

from fast_zero.app import app


@pytest.fixture
def client():
    return TestClient(app)


def test_root_deve_retornar_ok_e_ola_mundo(client):
    client = TestClient(app)

    response = client.get("/")

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {"message": "Hello World"}


def test_create_user(client):
    client = TestClient(app)

    response = client.post(
        "/users/",
        json={
            "username": "testuser",
            "password": "password",
            "email": "test@test.com",
        },
    )

    assert response.status_code == HTTPStatus.CREATED
    assert response.json() == {
        "username": "testuser",
        "email": "test@test.com",
        "id": 1,
    }
