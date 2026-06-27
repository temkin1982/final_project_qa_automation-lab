from faker import Faker

fake = Faker()
fake_user = fake.user_name()
fake_email = fake.email()


VALID_USERS = [
    (
        "admin@example.com",
        "admin123",
    ),
    ("diana@example.com", "password123"),
    ("bob@example.com", "password123"),
    ("charlie@example.com", "password123"),
]

VALID_RES = [
    "Test admin VALID",
    "Test diana_01 VALID",
    "Test user_bob VALID",
    "Test user_charlie VALID",
]

INVALID_USERS = [
    (
        "admin12345@example.com",
        "admin123",
        "Пользователь с таким email не найден в системе",
    ),
    (
        "admin987@example.com",
        "admin123",
        "Пользователь с таким email не найден в системе",
    ),
    ("alice@example.com", "admin1233434", "Неверный пароль"),
    (
        "guest1@example.com",
        "admin1232323",
        "Неверный пароль",
    ),
]

INVALID_RES = [
    "User with this email is not found in the system",
    "User with this email is not found in the system",
    "Wrong password",
    "Wrong password",
]
"""
nado dobavit Faker
"""
UNIQ_USER = [
    (
        fake_user,
        fake_email,
        "admin1982",
        "admin1982",
        "Регистрация успешна!",
    ),
    (
        fake_user,
        "admin19821@gmail.com",
        "admin1982",
        "admin1982",
        "Username already taken",
    ),
    (
        "admin198216",
        fake_email,
        "admin1982",
        "admin1982",
        "Email already registered",
    ),
]
RES_USER_UNIQ = ["REGISTER PASS", "UNIQ USER PASS", "UNIQ EMAIL PASS"]
