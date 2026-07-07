import allure
from playwright.sync_api import Page, expect

from core.base_page import BasePage


class HomePage(BasePage):
    """Home page of the automation lab."""

    path = "/"
    title = "Task Management Board"

    def __init__(self, page: Page):
        super().__init__(page)

        self.tmb_card_login = page.locator(".feature-card").filter(
            has_text="Система управления задачами"
        )

        self.open_card_login_link = self.tmb_card_login.get_by_role(
            "link", name="Открыть"
        )

        self.tmb_card_subscription = page.locator(".feature-card").filter(
            has_text="Форма подписки"
        )

        self.open_card_subscription_link = self.tmb_card_subscription.get_by_role(
            "link", name="Открыть"
        )

    @allure.step("Open home page")
    def open(self) -> None:
        self.goto(self.path)

    @allure.step("Verify page is opened")
    def verify_page_opened(self) -> None:
        super().verify_page_opened(self.path, self.title)
        expect(self.tmb_card_login).to_be_visible()

    @allure.step("Open login card")
    def open_card_login_page(self):
        self.open_card_login_link.click()

    @allure.step("Open subscription card")
    def open_card_subscription_page(self):
        self.open_card_subscription_link.click()
