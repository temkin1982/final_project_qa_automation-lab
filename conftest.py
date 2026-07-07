import pytest
import allure
from faker import Faker

from playwright.sync_api import Page
from api.users_api import Users
from api.tasks_api import Tasks


from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from pages.create_board_page import CreateBoardModal
from pages.register_page import Register
from pages.subscription_page import Subscription
from data.data_users import VALID_USERS

BOARD_ID = 1


@pytest.fixture
@allure.title("Login with admin user email and password")
def login(page: Page):
    email, password = VALID_USERS[0]
    login_page = LoginPage(page)
    login_page.open()
    login_page.verify_page_opened()
    login_page.login(email=email, password=password)
    return page


@pytest.fixture
@allure.title("Open create board")
def open_create_board(login):
    dashboard = DashboardPage(login)
    dashboard.create_board()

    create_board = CreateBoardModal(login)
    create_board.verify_board_modal_opened()
    return login


@pytest.fixture
@allure.title("Open login page and navigate to register panel")
def register(page: Page):
    login_page = LoginPage(page)
    login_page.open()
    login_page.verify_page_opened()
    login_page.click_register()

    new_user = Register(page)
    new_user.verify_card_register_opened()
    return page


@pytest.fixture
@allure.title("Open subscription model")
def subscription(page: Page):
    sub = Subscription(page)
    sub.open()
    sub.verify_subscription_opened()
    return page


@pytest.fixture
@allure.title("Api client")
def api_client():
    return Users()


@pytest.fixture
@allure.title("Get api client ID")
def api_user_id(api_client):
    fake = Faker()

    user_name = fake.user_name()
    user_email = fake.email()
    password = "test123"

    body = {"username": user_name, "email": user_email, "password": password}

    new_user = api_client.register_user(body)
    assert new_user.status_code == 201

    login = api_client.login_user(user_email, password)
    data_login = login.json()
    token = data_login["access_token"]
    assert login.status_code == 200

    data_user = api_client.user_me(token).json()

    new_id = data_user["id"]

    return new_id


@pytest.fixture
@allure.title("Api tasks")
def api_tasks():
    return Tasks()


@pytest.fixture
@allure.title("Get api task ID")
def api_task_id(api_tasks):
    fake = Faker()

    title = fake.sentence()
    description = fake.text()

    body = {
        "title": title,
        "description": description,
        "status": "todo",
        "priority": "medium",
        "assignee_id": 0,
    }

    response = api_tasks.create_task(BOARD_ID, body)
    assert response.status_code == 201

    data_task = response.json()
    task_id = data_task["id"]

    return task_id
