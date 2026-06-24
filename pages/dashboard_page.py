from playwright.sync_api import Page, expect

from core.base_page import BasePage


class DashboardPage(BasePage):

    path = "/dashboard"
    title = "Task Management Board"

    def __init__(self, page: Page):
        super().__init__(page)

        self.header_logo_button = page.locator('[data-qa="header-logo-link"]')
        self.home_menu_title = page.locator('[class="brand-subtitle"]')
        self.menu_home = page.locator('[data-qa="sidebar-home-link"]')
        self.menu_boards = page.locator('[data-qa="sidebar-boards-link"]')
        self.menu_tasks = page.locator('[data-qa="sidebar-tasks-link"]')
        self.menu_admin = page.locator('[data-qa="sidebar-admin-link"]')

        self.username = page.locator('[data-qa="header-username"]')
        self.user_menu_button = page.locator('[data-qa="header-user-info"]')
        self.logout_button = page.locator('[data-qa="header-logout-button"]')

        self.dashboard_title = page.locator('[data-qa="dashboard-title"]')
        self.create_board_button = page.locator(
            '[data-qa="dashboard-create-board-button"]'
        )
        self.create_board_title = page.locator('[class="modal-title text-gradient"]')

    def verify_page_opened(self) -> None:
        super().verify_page_opened(self.path, self.title)
        expect(self.dashboard_title).to_contain_text("Панель управления")

    def verify_username(self, username):
        expect(self.username).to_contain_text(username)

    def go_back_home_menu(self):
        self.header_logo_button.click()

    def logout(self):
        self.user_menu_button.click()
        self.logout_button.click()

    def go_to_home_menu(self):
        self.menu_home.click()

    def go_to_boards(self):
        self.menu_boards.click()

    def go_to_tasks(self):
        self.menu_tasks.click()

    def go_to_admin_panel(self):
        self.menu_admin.click()

    def create_board(self):
        self.create_board_button.click()

    def verify_board_modal_opened(self):
        expect(self.create_board_title).to_have_text("Создать доску")
