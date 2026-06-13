from playwright.sync_api import Page, expect


class BasePage:

    def __init__(self, page: Page):
        self.page = page
        self.domain = "http://localhost:3000"

    def goto(self, url: str) -> None:
        self.page.goto(f"{self.domain}{url}")

    def verify_page_opened(self, url: str, title: str) -> None:
        expect(self.page).to_have_url(f"{self.domain}{url}")
        expect(self.page).to_have_title(title)


# # РОДИТЕЛЬ — общие вещи для всех страниц
# class BasePage:
#     def __init__(self, page):
#         self.page = page
#         self.domain = 'http://localhost:3000'

#     def goto(self, url):
#         self.page.goto(f'{self.domain}{url}')


# # РЕБЁНОК — наследует от BasePage (в скобках!)
# class LoginPage(BasePage):  # ← (BasePage) = "я беру всё от BasePage"
#     def __init__(self, page):
#         super().__init__(page)  # ← вызываем __init__ родителя

#         # Свои локаторы только для Login
#         self.email_input = page.get_by_placeholder("Email")
#         self.login_button = page.get_by_role("button", name="Войти")

#     def login(self, email, password):
#         self.email_input.fill(email)
#         self.login_button.click()
