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
admin@example.com / admin123
Admin
alice@example.com / admin123
Admin
bob@example.com / password123
charlie@example.com / password123
diana@example.com / password123
eve@example.com / password123
guest1@example.com / guest123
guest2@example.com / guest123
"""
# INVALID_USERS = [
#     ("adminexample.com", "admin123"),
#     ("admin@example", "admin123"),
#     ("", "admin123"),
#     ("admin@example.com", "")
# ]
