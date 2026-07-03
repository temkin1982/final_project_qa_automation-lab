PERIOD = [
    ("period-1", "1 месяц"),
    ("period-3", "3 месяца"),
    ("period-12", "12 месяцев"),
]

RES_PERIOD = ["TEST= 1 month PASS", "TEST=  3 month PASS", "TEST= 12 month PASS"]


TARIFF = [
    ("tariff-basic", "Базовый"),
    ("tariff-premium", "Премиум"),
    ("tariff-family", "Семейный"),
]

RES_TARIFF = [
    "TEST= tariff-basic PASS",
    "TEST= tariff-premium PASS",
    "TEST= tariff-family PASS",
]

PROMO_CODE = [
    ("period-1", "tariff-premium", "WELCOME10", "Промокод истек 31.12.2024"),
    ("period-3", "tariff-basic", "FAMILY300", "Промокод истек 30.06.2024"),
    ("period-12", "tariff-family", "SUMMER25", "Промокод истек 31.08.2024"),
    ("period-3", "tariff-premium", "BASIC199", "Промокод только для: Базовый"),
    (
        "period-1",
        "tariff-basic",
        "BASIC199",
        "Промокод применён: Специальная цена 199₷/мес на Базовый тариф",
    ),
    (
        "period-12",
        "tariff-family",
        "ALWAYS",
        "Промокод применён: Скидка 15% для для всех тарифов",
    ),
]

RES_PROMO_CODE = [
    "TEST NEGATIVE = PASS",
    "TEST NEGATIVE = PASS",
    "TEST NEGATIVE = PASS",
    "TEST NEGATIVE = PASS",
    "TEST POSITIVE = PASS",
    "TEST POSITIVE = PASS",
]

VALID_CREDIT_CARDS = [
    (
        "4111 1111 1111 1111",
        "1229",
        "123",
        "Успешно!",
    ),
    (
        "5555 5555 5555 4444",
        "1229",
        "234",
        "Успешно!",
    ),
    (
        "3782 822463 10005",
        "1229",
        "1234",
        "Успешно!",
    ),
]

RES_VALID_CARDS = [
    "tc-01-Critical PASS",
    "tc-02-Critical PASS",
    "tc-03-Critical PASS",
]

INVALID_CREDIT_CARDS = [
    (
        "4000 0000 0000 0002",
        "1229",
        "123",
        "Карта отклонена. Попробуйте другую карту",
    ),
    (
        "4000 0000 0000 9995",
        "1229",
        "123",
        "Недостаточно средств на карте",
    ),
]

RES_INVALID_CARDS = [
    "tc-01-Major PASS",
    "tc-02-Major PASS",
]
