import allure
import requests
import pytest

from faker import Faker


@allure.epic("API Tests")
@allure.feature("Users")
@allure.title("Get user by id")
def test_get_user_by_id(api_client):
    response = api_client.get_user_by_id(1)
    assert response.status_code == 200
    data = response.json()
    assert data["email"] == "admin@example.com"
    assert data["username"] == "admin"


@allure.epic("API Tests")
@allure.feature("Users")
@allure.title("Get user without token")
def test_get_user_without_token():
    response = requests.get("http://localhost:8000/users/1", timeout=10)
    assert response.status_code == 401


@allure.epic("API Tests")
@allure.feature("Users")
@allure.title("Update user with user id")
def test_update_user(api_client, api_user_id):
    fake = Faker()

    update_user_name = fake.user_name()
    update_user_email = fake.email()

    body = {"username": update_user_name, "email": update_user_email}
    response = api_client.update_user(api_user_id, body)

    data = response.json()
    assert response.status_code == 200
    assert data["username"] == update_user_name
    assert data["email"] == update_user_email


@allure.epic("API Tests")
@allure.feature("Users")
@allure.title("Delete user with user id")
def test_delete_user_by_id(api_client, api_user_id):

    user_delete = api_client.delete_user(api_user_id)
    assert user_delete.status_code == 204

    response = api_client.get_user_by_id(api_user_id)
    assert response.status_code == 404


@allure.epic("API Tests")
@allure.feature("Users")
@allure.title("Update invalid value username")
@pytest.mark.parametrize(
    "user_name, expected_status",
    [
        ("ab", 422),
        ("a" * 51, 422),
    ],
)
def test_update_user_by_username(api_client, api_user_id, user_name, expected_status):
    body = {"username": user_name}
    response = api_client.update_user(api_user_id, body)

    assert response.status_code == expected_status


@allure.epic("API Tests")
@allure.feature("Users")
@allure.title("Update user with valid value")
def test_update_username_valid(api_client, api_user_id):
    fake = Faker()
    unique_name = fake.user_name()
    body = {"username": unique_name}

    response = api_client.update_user(api_user_id, body)
    assert response.status_code == 200
    assert response.json()["username"] == unique_name
