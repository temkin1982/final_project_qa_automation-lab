import pytest
from playwright.sync_api import Page

from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from pages.create_board_page import CreateBoardModal
from pages.register_page import Register
from pages.subscription_page import Subscription
from data.data_users import VALID_USERS


@pytest.fixture
def login(page: Page):
    email, password = VALID_USERS[0]
    login_page = LoginPage(page)
    login_page.open()
    login_page.verify_page_opened()
    login_page.login(email=email, password=password)
    return page


@pytest.fixture
def open_create_board(login):
    dashboard = DashboardPage(login)
    dashboard.create_board()

    create_board = CreateBoardModal(login)
    create_board.verify_board_modal_opened()
    return login


@pytest.fixture
def register(page: Page):
    login_page = LoginPage(page)
    login_page.open()
    login_page.verify_page_opened()
    login_page.click_register()

    new_user = Register(page)
    new_user.verify_card_register_opened()
    return page


@pytest.fixture
def subscription(page: Page):
    sub = Subscription(page)
    sub.open()
    sub.verify_subscription_opened()
    return page
