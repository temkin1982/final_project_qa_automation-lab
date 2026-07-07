import allure
import pytest

from faker import Faker

from pages.register_page import Register
from pages.dashboard_page import DashboardPage
from pages.login_page import LoginPage

from data.data_users import UNIQ_USER, RES_USER_UNIQ


@allure.epic("UI Tests")
@allure.feature("Register new user")
@allure.title("Register user")
def test_register(register):
    fake = Faker()
    fake_user = fake.user_name()
    fake_email = fake.email()

    user = Register(register)
    user.register(fake_user, fake_email, "test1234", "test1234")
    user.submit()
    user.verify_register_success()


@allure.epic("UI Tests")
@allure.feature("Register new user")
@allure.title("Create a new user and login with new user and email")
def test_register_and_login(register):
    fake = Faker()
    fake_user = fake.user_name()
    fake_email = fake.email()

    user = Register(register)
    user.register(fake_user, fake_email, "test1234", "test1234")
    user.submit()
    user.verify_register_success()

    dashboard = DashboardPage(register)
    dashboard.verify_page_opened()
    dashboard.logout()

    user_login = LoginPage(register)
    user_login.login(fake_email, "test1234")
    dashboard.verify_page_opened()


@allure.epic("UI Tests")
@allure.feature("Register new user")
@allure.title("Create new user with error password")
def test_error_password(register):
    fake = Faker()
    fake_user = fake.user_name()
    fake_email = fake.email()

    user = Register(register)
    user.register(fake_user, fake_email, "test1234", "test123")
    user.submit()
    user.verify_password_error()


@allure.epic("UI Tests")
@allure.feature("Register new user")
@allure.title("User with under minimum length")
def test_error_minlength_3_for_user(register):
    fake = Faker()
    fake_email = fake.email()

    user = Register(register)
    user.register("ab", fake_email, "test1234", "test1234")
    user.submit()
    user.verify_card_register_opened()


@allure.epic("UI Tests")
@allure.feature("Register new user")
@allure.title("User with invalid email")
def test_error_email(register):
    user = Register(register)
    invalid_email = "admingmail.com"
    user.register("abc", invalid_email, "test1234", "test1234")
    user.submit()
    user.verify_card_register_opened()


@allure.epic("UI Tests")
@allure.feature("Register new user")
@allure.title("User with invalid password")
def test_error_minlength_6_for_user_password(register):
    fake = Faker()
    fake_user = fake.user_name()
    fake_email = fake.email()

    user = Register(register)
    user.register(fake_user, fake_email, "test1", "test1")
    user.submit()
    user.verify_card_register_opened()


@allure.epic("UI Tests")
@allure.feature("Register new user")
@allure.title("User register with valid password")
def test_minlength_6_for_user_password(register):
    fake = Faker()
    fake_user = fake.user_name()
    fake_email = fake.email()

    user = Register(register)
    user.register(fake_user, fake_email, "test12", "test12")
    user.submit()
    user.verify_register_success()


@allure.epic("UI Tests")
@allure.feature("Register new user")
@allure.title("Create new user with uniq user: {user}")
@pytest.mark.parametrize(
    "user, email, password, confirm_password, res", UNIQ_USER, ids=RES_USER_UNIQ
)
def test_uniq_user(register, user, email, password, confirm_password, res):
    uniq_user = Register(register)
    uniq_user.register(user, email, password, confirm_password)
    uniq_user.submit()
    uniq_user.result_message(res)
