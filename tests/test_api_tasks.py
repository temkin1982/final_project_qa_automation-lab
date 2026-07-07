import allure
import pytest

from faker import Faker

BOARD_ID = 1


@allure.epic("API Tests")
@allure.feature("Tasks")
@allure.title("Create task")
def test_create_task(api_tasks):

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

    data = response.json()
    assert data["board_id"] == BOARD_ID
    assert data["title"] == title
    assert data["description"] == description


@allure.epic("API Tests")
@allure.feature("Tasks")
@allure.title("Search tasks by query")
def test_search_tasks(api_tasks):
    response = api_tasks.get_tasks_by_search("task")
    assert response.status_code == 200

    data = response.json()
    assert isinstance(data, list)
    assert len(data) > 0


@allure.epic("API Tests")
@allure.feature("Tasks")
@allure.title("Delete task by id")
def test_delete_task(api_tasks, api_task_id):

    response_after_delete = api_tasks.delete_task(BOARD_ID, api_task_id)
    assert response_after_delete.status_code == 204

    check_after_delete = api_tasks.get_task(BOARD_ID, api_task_id)
    assert check_after_delete.status_code == 404


@allure.epic("API Tests")
@allure.feature("Tasks")
@allure.title("Create task with valid title and invalid title")
@pytest.mark.parametrize(
    "title, expected_status",
    [
        ("", 422),
        ("A", 201),
        ("Normal task title", 201),
        ("A" * 200, 201),
        ("A" * 201, 422),
    ],
)
def test_create_tasks_valid_and_invalid_title(api_tasks, title, expected_status):
    fake = Faker()

    description = fake.text()

    body = {
        "title": title,
        "description": description,
        "status": "todo",
        "priority": "medium",
        "assignee_id": 0,
    }
    response = api_tasks.create_task(BOARD_ID, body)
    assert response.status_code == expected_status
