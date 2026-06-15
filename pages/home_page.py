from playwright.sync_api import Page, expect

from core.base_page import BasePage


class HomePage(BasePage):

    path = "/"
    title = "Task Management Board"

    def __init__(self, page: Page):
        super().__init__(page)

        self.tms_card = page.locator(".feature-card").filter(
            has_text="Система управления задачами"
        )

        self.open_tms_link = self.tms_card.get_by_role("link", name="Открыть")

    def open(self) -> None:
        self.goto(self.path)

    def verify_page_opened(self) -> None:
        super().verify_page_opened(self.path, self.title)
        expect(self.tms_card).to_be_visible()

    def open_tms_page(self):
        self.open_tms_link.click()
