from core.base_page import BasePage

from playwright.sync_api import Page, expect


class LoginPage(BasePage):

    path = "/login"
    title = "Task Management Board"

    def __init__(self, page: Page):
        super().__init__(page)

        self.email = page.locator('[data-qa="login-email-input"]')
        self.password = page.locator('[data-qa="login-password-input"]')
        self.submit_button = page.locator('[data-qa="login-submit-button"]')
        self.login_form = page.locator('[data-qa="login-form"]')
        self.login_title = page.locator('[data-qa="login-title"]')
        self.toast_message = page.locator('[class="toast-message"]')

    def open(self) -> None:
        self.goto(self.path)

    def verify_page_opened(self) -> None:
        super().verify_page_opened(self.path, self.title)
        expect(self.login_form).to_be_visible()
        expect(self.login_title).to_contain_text("Вход в систему")

    def login(self, email, password):
        self.email.fill(email)
        self.password.fill(password)
        self.submit_button.click()

    def verify_error_message(self, text):
        expect(self.toast_message).to_have_text(text)
