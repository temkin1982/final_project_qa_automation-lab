import allure
import pytest
from playwright.sync_api import Page, expect

from pages.home_page import HomePage
from pages.login_page import LoginPage
from data.data_users import VALID_USERS, INVALID_USERS, VALID_RES, INVALID_RES


@allure.epic("UI Tests")
@allure.feature("Authentication")
@allure.title("Open home page and login")
def test_open_home_page_and_login(page: Page):
    home_page = HomePage(page)
    home_page.open()
    home_page.verify_page_opened()
    home_page.open_card_login_page()

    login_page = LoginPage(page)
    login_page.verify_page_opened()


@allure.epic("UI Tests")
@allure.feature("Authentication")
@allure.title("Open login page")
def test_open_login_page(page: Page):
    login_page = LoginPage(page)

    login_page.open()
    login_page.verify_page_opened()


@allure.epic("UI Tests")
@allure.feature("Authentication")
@allure.title("Login with valid users password and email: {email}")
@pytest.mark.parametrize("email, password", VALID_USERS, ids=VALID_RES)
def test_successful_login(page, email, password):
    user_login = LoginPage(page)
    user_login.open()
    user_login.login(email, password)
    expect(page).to_have_url("http://localhost:3000/dashboard")


@allure.epic("UI Tests")
@allure.feature("Authentication")
@allure.title("Login with invalid users password and email: {email}")
@pytest.mark.parametrize(
    "email, password, expected_error", INVALID_USERS, ids=INVALID_RES
)
def test_find_error(page, email, password, expected_error):
    user_error_login = LoginPage(page)
    user_error_login.open()
    user_error_login.login(email, password)
    user_error_login.verify_error_message(expected_error)
