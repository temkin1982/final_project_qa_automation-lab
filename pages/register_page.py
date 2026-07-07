import allure
from playwright.sync_api import Page, expect

from core.base_page import BasePage


class Register(BasePage):
    """Registration page."""

    path = "/register"
    title = "Task Management Board"

    def __init__(self, page: Page):
        super().__init__(page)
        self.register_form = page.locator('[data-qa="register-form-container"]')
        self.register_title = page.locator('[data-qa="register-title"]')

        self.return_login_card = page.get_by_role("link", name="войдите в систему")

        self.name_user_input = page.locator('[data-qa="register-username-input"]')
        self.email_input = page.locator('[data-qa="register-email-input"]')
        self.password_input = page.locator('[data-qa="register-password-input"]')
        self.password_confirm_input = page.locator(
            '[data-qa="register-confirm-password-input"]'
        )

        self.register_button = page.locator('[data-qa="register-submit-button"]')

        self.toast_message = page.locator('[class="toast-message"]')
        self.password_error = page.get_by_text("Пароли не совпадают")

    @allure.step("Verify page is opened")
    def verify_card_register_opened(self) -> None:
        super().verify_page_opened(self.path, self.title)
        expect(self.register_form).to_be_visible()
        expect(self.register_title).to_contain_text("Регистрация")

    @allure.step("Click return to login card button")
    def back_login_card(self):
        self.return_login_card.click()

    @allure.step(
        "Register new user with: {name_user} {email} password and confirm password"
    )
    def register(self, name_user, email, password, password_confirm):
        self.name_user_input.fill(name_user)
        self.email_input.fill(email)
        self.password_input.fill(password)
        self.password_confirm_input.fill(password_confirm)

    @allure.step("Click register button")
    def submit(self):
        self.register_button.click()

    @allure.step("Verify register success message")
    def verify_register_success(self):
        expect(self.toast_message).to_have_text("Регистрация успешна!")

    @allure.step("Error message username already taken")
    def error_user_message(self):
        expect(self.toast_message).to_have_text("Username already taken")

    @allure.step("Error message email already registered")
    def error_email_message(self):
        expect(self.toast_message).to_have_text("Email already registered")

    @allure.step("Result message {text}")
    def result_message(self, text):
        expect(self.toast_message).to_have_text(text)

    @allure.step("Verify if password is error")
    def verify_password_error(self):
        expect(self.password_error).to_be_visible()
