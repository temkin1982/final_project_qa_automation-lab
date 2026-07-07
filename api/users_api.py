import allure
from utils.logger import logger
from api.http_client import HttpClient


class Users(HttpClient):
    """Users API client."""

    @allure.step("Get user by id: {user_id}")
    def get_user_by_id(self, user_id):
        try:
            response = self.get(f"/users/{user_id}")
            logger.info(f"Got user {user_id}, status: {response.status_code}")
            return response
        except Exception as error:
            logger.error(f"Failed to get user {user_id}: {error}")
            assert False, f"Request failed: {error}"

    @allure.step("Register user")
    def register_user(self, data):
        try:
            response = self.post("/auth/register", data)
            logger.info(
                f"Got data register user {data}, status: {response.status_code}"
            )
            return response
        except Exception as error:
            logger.error(f"Failed to get data {data}: {error}")
            assert False, f"Request failed: {error}"

    @allure.step("Login user with email: {email} and password")
    def login_user(self, email, password):
        try:
            data = {"email": email, "password": password}
            response = self.post("/auth/login", data)
            logger.info(f"Login user with {data}, status: {response.status_code}")
            return response
        except Exception as error:
            logger.error(f"Failed to login with data {data}: {error}")
            assert False, f"Request failed: {error}"

    @allure.step("Get token by user")
    def user_me(self, token):
        try:
            response = self.get_with_token("/users/me", token)
            logger.info(f"Success to get token, status {response.status_code}")
            return response
        except Exception as error:
            logger.error(f"Failed to get token {error}")
            assert False, f"Request failed: {error}"

    @allure.step("Update user with the user id: {user_id} and data")
    def update_user(self, user_id, data):
        try:
            response = self.put(f"/users/{user_id}", data)
            logger.info(
                f"Success update by user id {user_id} status: {response.status_code}"
            )
            return response
        except Exception as error:
            logger.error(f"Failed to update with user id: {user_id}")
            assert False, f"Request failed: {error}"

    @allure.step("Delete user with user id: {user_id}")
    def delete_user(self, user_id):
        try:
            response = self.delete(f"/users/{user_id}")
            logger.info(
                f"Success to delete user with user id: {user_id}"
                f"status: {response.status_code}"
            )
            return response
        except Exception as error:
            logger.error(f"Failed to delete with user id: {user_id}")
            assert False, f"Request failed: {error}"
