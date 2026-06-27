import pytest

from pages.register_page import Register
from pages.dashboard_page import DashboardPage
from pages.login_page import LoginPage

from data.data_users import UNIQ_USER, RES_USER_UNIQ


from faker import Faker


@pytest.mark.reg1
def test_register(register):
    fake = Faker()
    fake_user = fake.user_name()
    fake_email = fake.email()

    user = Register(register)
    user.register(fake_user, fake_email, "test1234", "test1234")
    user.submit()
    user.verify_register_success()


@pytest.mark.reg2
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


@pytest.mark.reg3
def test_error_password(register):
    fake = Faker()
    fake_user = fake.user_name()
    fake_email = fake.email()

    user = Register(register)
    user.register(fake_user, fake_email, "test1234", "test123")
    user.submit()
    user.verify_password_error()


@pytest.mark.reg4
def test_error_minlength_3_for_user(register):
    fake = Faker()
    fake_email = fake.email()

    user = Register(register)
    user.register("ab", fake_email, "test1234", "test1234")
    user.submit()
    user.verify_card_register_opened()


@pytest.mark.reg5
def test_error_email(register):
    user = Register(register)
    user.register("abc", "admingmail.com", "test1234", "test1234")
    user.submit()
    user.verify_card_register_opened()


@pytest.mark.reg6
def test_error_minlength_6_for_user_password(register):
    fake = Faker()
    fake_user = fake.user_name()
    fake_email = fake.email()

    user = Register(register)
    user.register(fake_user, fake_email, "test1", "test1")
    user.submit()
    user.verify_card_register_opened()


@pytest.mark.reg7
def test_minlength_6_for_user_password(register):
    fake = Faker()
    fake_user = fake.user_name()
    fake_email = fake.email()

    user = Register(register)
    user.register(fake_user, fake_email, "test12", "test12")
    user.submit()
    user.verify_register_success()


@pytest.mark.reg8
@pytest.mark.parametrize(
    "user, email, password, confirm_password, res", UNIQ_USER, ids=RES_USER_UNIQ
)
def test_uniq_user(register, user, email, password, confirm_password, res):
    uniq_user = Register(register)
    uniq_user.register(user, email, password, confirm_password)
    uniq_user.submit()
    uniq_user.result_message(res)
