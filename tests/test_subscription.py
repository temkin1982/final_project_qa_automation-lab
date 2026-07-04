import pytest
from playwright.sync_api import Page, expect

from pages.home_page import HomePage
from pages.subscription_page import Subscription

from data.data_card import (
    PERIOD,
    RES_PERIOD,
    TARIFF,
    RES_TARIFF,
    PROMO_CODE,
    RES_PROMO_CODE,
    VALID_CREDIT_CARDS,
    RES_VALID_CARDS,
    INVALID_CREDIT_CARDS,
    RES_INVALID_CARDS,
)


def test_open_home_page_and_login(page: Page):
    home_page = HomePage(page)
    home_page.open()
    home_page.verify_page_opened()
    home_page.open_card_subscription_page()

    sub_page = Subscription(page)
    sub_page.verify_subscription_opened()


def test_return_button(subscription):
    sub = Subscription(subscription)
    sub.return_from_subscription_page()
    expect(subscription).to_have_url("http://localhost:3000/automation-lab")


@pytest.mark.parametrize("period, expect_res", PERIOD, ids=RES_PERIOD)
def test_click_choice_period(subscription, period, expect_res):
    sub = Subscription(subscription)
    sub.click_period_section(period)
    sub.verify_text_period(expect_res)


@pytest.mark.parametrize("tariff, expect_res", TARIFF, ids=RES_TARIFF)
def test_click_tariff_choice(subscription, tariff, expect_res):
    sub = Subscription(subscription)
    sub.click_tariffs_section(tariff)
    sub.verify_text_tariff(expect_res)


@pytest.mark.parametrize(
    "period, tariff, promo_code, expect_res", PROMO_CODE, ids=RES_PROMO_CODE
)
def test_promo_code_valid_and_invalid(
    subscription, period, tariff, promo_code, expect_res
):
    sub = Subscription(subscription)
    sub.click_period_section(period)
    sub.click_tariffs_section(tariff)
    sub.verify_promo_section_label()
    sub.input_promo_code(promo_code, expect_res)


@pytest.mark.parametrize(
    "card_number, mm_yy, cvv, expect_res", VALID_CREDIT_CARDS, ids=RES_VALID_CARDS
)
def test_valid_credit_cards(subscription, card_number, mm_yy, cvv, expect_res):
    card = Subscription(subscription)
    card.verify_summary_section()
    card.verify_pay_button_is_disabled()
    card.card_input(card_number, mm_yy, cvv)
    card.verify_pay_button_is_enabled_and_click()
    card.positive_card_message_and_click(expect_res)
    card.verify_subscription_opened()


@pytest.mark.parametrize(
    "card_number, mm_yy, cvv, expect_res", INVALID_CREDIT_CARDS, ids=RES_INVALID_CARDS
)
def test_invalid_credit_cards(subscription, card_number, mm_yy, cvv, expect_res):
    card = Subscription(subscription)
    card.verify_summary_section()
    card.verify_pay_button_is_disabled()
    card.card_input(card_number, mm_yy, cvv)
    card.verify_pay_button_is_enabled_and_click()
    card.negative_card_message(expect_res)
    card.verify_subscription_opened()


def test_big_numbers_to_card(subscription):
    card = Subscription(subscription)
    card.verify_summary_section()
    card.verify_pay_button_is_disabled()
    card.card_input("1111 1111 1111 1111 1111 1111 1111 1111", "12_29", "1234")
    card.verify_pay_button_is_disabled()
