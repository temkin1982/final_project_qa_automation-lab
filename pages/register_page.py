from core.base_page import BasePage


from playwright.sync_api import Page, expect


class Register(BasePage):

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

    def verify_card_register_opened(self) -> None:
        super().verify_page_opened(self.path, self.title)
        expect(self.register_form).to_be_visible()
        expect(self.register_title).to_contain_text("Регистрация")

    def back_login_card(self):
        self.return_login_card.click()

    def register(self, name_user, email, password, password_confirm):
        self.name_user_input.fill(name_user)
        self.email_input.fill(email)
        self.password_input.fill(password)
        self.password_confirm_input.fill(password_confirm)

    def submit(self):
        self.register_button.click()

    def verify_register_success(self):
        expect(self.toast_message).to_have_text("Регистрация успешна!")

    def error_user_message(self):
        expect(self.toast_message).to_have_text("Username already taken")

    def error_email_message(self):
        expect(self.toast_message).to_have_text("Email already registered")

    def result_message(self, text):
        expect(self.toast_message).to_have_text(text)

    def verify_password_error(self):
        expect(self.password_error).to_be_visible()
