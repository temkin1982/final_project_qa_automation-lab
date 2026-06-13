from core.base_page import BasePage

from playwright.sync_api import Page, expect


class LoginPage(BasePage):

    path = "/login"
    title = "Task Management Board"

    def __init__(self, page: Page):
        super().__init__(page)

        self.email = page.locator('[id="id-input-login-email-input"]')
        self.password = page.locator('[id="id-input-login-password-input"]')
        self.submit_button = page.locator('[data-qa="login-submit-button"]')
        self.register_link = page.locator('[href="/register"]')
        self.login_form = page.locator('[data-qa="login-form"]')
        self.login_title = page.locator('[data-qa="login-title"]')

    def open(self) -> None:
        self.goto(self.path)

    def verify_page_opened(self) -> None:
        super().verify_page_opened(self.path, self.title)
        expect(self.login_form).to_be_visible()
        expect(self.login_title).to_contain_text("Вход в систему")
