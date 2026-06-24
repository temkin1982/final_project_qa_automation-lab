import pytest
from playwright.sync_api import Page

from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from data.data_users import VALID_USERS


@pytest.fixture
def login(page: Page):
    email, password = VALID_USERS[0]
    login_page = LoginPage(page)
    login_page.open()
    login_page.login(email=email, password=password)
    return page


@pytest.fixture
def open_create_board(login):
    dashboard = DashboardPage(login)
    dashboard.create_board()
    return login
