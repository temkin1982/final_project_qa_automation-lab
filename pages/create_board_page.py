import allure
from playwright.sync_api import Page, expect

from core.base_page import BasePage


class CreateBoardModal(BasePage):
    """Create board modal window."""

    def __init__(self, page: Page):
        super().__init__(page)

        self.close_model_button = page.locator('[data-qa="modal-close-button"]')
        self.title_input = page.locator('[data-qa="create-board-title-input"]')
        self.title_description_input = page.locator(
            '[data-qa="create-board-description-textarea"]'
        )
        self.checkbox = page.locator('[data-qa="create-board-public-checkbox"]')
        self.submit_button = page.locator('[data-qa="create-board-submit-button"]')
        self.cancel_button = page.locator('[data-qa="create-board-cancel-button"]')
        self.dashboard_title = page.locator('[data-qa="dashboard-title"]')
        self.create_board_title = page.locator('[class="modal-title text-gradient"]')
        self.toast_message = page.locator('[class="toast-message"]')

    @allure.step("Close model window")
    def close_model(self):
        self.close_model_button.click()

    @allure.step("Input title")
    def fill_title(self, title):
        self.title_input.fill(title)

    @allure.step("Input description")
    def fill_description_title(self, title):
        self.title_description_input.fill(title)

    @allure.step("Check checkbox")
    def check_checkbox(self):
        self.checkbox.check()

    @allure.step("Uncheck checkbox")
    def uncheck_checkbox(self):
        self.checkbox.uncheck()

    @allure.step("Verify checkbox is checked")
    def verify_checkbox(self):
        expect(self.checkbox).to_be_checked()

    @allure.step("Verify checkbox is not checked")
    def verify_uncheck_checkbox(self):
        expect(self.checkbox).not_to_be_checked()

    @allure.step("Click submit button")
    def submit(self):
        self.submit_button.click()

    @allure.step("Click cancel button")
    def cancel(self):
        self.cancel_button.click()

    @allure.step("Verify board modal is open")
    def verify_board_modal_opened(self):
        expect(self.create_board_title).to_have_text("Создать доску")

    @allure.step("Verify board modal is close")
    def verify_close_model(self):
        expect(self.dashboard_title).to_contain_text("Панель управления")

    @allure.step("Verify board modal is created")
    def verify_board_created(self):
        expect(self.toast_message).to_have_text("Доска успешно создана!")
