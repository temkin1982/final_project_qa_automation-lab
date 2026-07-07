import allure
from playwright.sync_api import Page, expect

from core.base_page import BasePage


class Subscription(BasePage):
    """Subscription page."""

    path = "/automation-lab/subscription"
    title = "Task Management Board"

    def __init__(self, page: Page):

        super().__init__(page)

        self.subscription_form = page.locator('[data-testid="tariffs-section"]')
        self.subscription_title = page.locator('[class="subscription-title"]')
        self.return_button = page.get_by_role("link", name="Назад")

        self.period_section = page.locator('[data-testid="period-section"]')
        self.period_name = page.locator('[data-testid="period-section"]')

        self.tariffs_section = page.locator('[data-testid="tariffs-section"]')
        self.tariff_name = page.locator('[data-testid="tariffs-section"]')

        self.promo_label = page.locator('[data-testid="promo-section"]')
        self.promo_code = page.locator('[data-testid="promo-section"]')
        self.promo_input = page.locator('[data-testid="promo-input"]')
        self.button_promo_code = page.locator('[data-testid="promo-apply-btn"]')
        self.promo_message = page.locator('[data-testid="promo-message"]')

        self.payment_section = page.locator('[data-testid="payment-section"]')
        self.card_number_input = page.locator('[data-testid="card-number"]')
        self.card_expiry_input = page.locator('[data-testid="card-expiry"]')
        self.card_cvv_input = page.locator('[data-testid="card-cvv"]')

        self.summary_section = page.locator('[data-testid="summary-section"]')
        self.summary_title = page.locator('[class="summary-title"]')
        self.summary_button = page.locator('[data-testid="pay-button"]')

        self.card_errors = page.locator('[data-testid="card-errors"]')
        self.card_success = page.locator('[data-testid="success-modal"]')
        self.success_button = page.get_by_role("button", name="Отлично!")

    @allure.step("Open subscription page")
    def open(self) -> None:
        self.goto(self.path)

    @allure.step("Verify page is opened")
    def verify_subscription_opened(self) -> None:
        super().verify_page_opened(self.path, self.title)
        expect(self.subscription_form).to_be_visible()
        expect(self.subscription_title).to_have_text("Подключение подписки StreamVibe")

    @allure.step("Click return from subscription page button")
    def return_from_subscription_page(self):
        self.return_button.click()

    @allure.step("Select period: {user_period}")
    def click_period_section(self, user_period):
        expect(self.period_section).to_be_visible()
        period_switcher = self.page.locator(f'[data-testid="{user_period}"]')
        period_switcher.click()

    @allure.step("Verify text period: {text_period}")
    def verify_text_period(self, text_period):
        expect(self.period_name).to_contain_text(text_period)

    @allure.step("Select tariff: {tariff_section}")
    def click_tariffs_section(self, tariff_section):
        expect(self.tariffs_section).to_be_visible()
        tariffs_switcher = self.page.locator(f'[data-testid="{tariff_section}"]')
        tariffs_switcher.click()

    @allure.step("Verify text tariff: {tariff_name}")
    def verify_text_tariff(self, tariff_name):
        expect(self.tariff_name).to_contain_text(tariff_name)

    @allure.step("Input promo code with result: {code} and {res}")
    def input_promo_code(self, code, res):
        self.promo_input.fill(code)
        self.button_promo_code.click()
        expect(self.promo_message).to_have_text(res)

    @allure.step("Verify promo code section label")
    def verify_promo_section_label(self):
        expect(self.promo_code).to_be_visible()
        expect(self.promo_label).to_contain_text("Промокод")

    @allure.step("Input card number: {card_number} mm_yy: {mm_yy} cvv {cvv}")
    def card_input(self, card_number, mm_yy, cvv):
        expect(self.payment_section).to_be_visible()
        self.card_number_input.fill(card_number)
        self.card_expiry_input.fill(mm_yy)
        self.card_cvv_input.fill(cvv)

    @allure.step("Negative message for card result")
    def negative_card_message(self, error_message):
        expect(self.card_errors).to_contain_text(error_message)

    @allure.step("Positive message for card result")
    def positive_card_message_and_click(self, success_message):
        expect(self.card_success).to_contain_text(success_message)
        self.success_button.click()

    @allure.step("Verify summary section")
    def verify_summary_section(self):
        expect(self.summary_section).to_be_visible()
        expect(self.summary_title).to_have_text("Введи карту")

    @allure.step("Verify pay button is disabled")
    def verify_pay_button_is_disabled(self):
        expect(self.summary_button).to_be_disabled()

    @allure.step("Verify pay button is enabled")
    def verify_pay_button_is_enabled_and_click(self):
        expect(self.summary_button).to_be_enabled()
        self.summary_button.click()
