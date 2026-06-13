import pytest
from playwright.sync_api import Page

from pages.login_page import LoginPage


@pytest.mark.test1
def test_open_login_page(page: Page):
    login_page = LoginPage(page)

    login_page.open()
    login_page.verify_page_opened()
