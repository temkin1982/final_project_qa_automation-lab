import allure
from utils.logger import logger
from api.http_client import HttpClient


class Tasks(HttpClient):
    """Tasks API client."""

    @allure.step("Get task with the board id: {board_id} and task id: {task_id}")
    def get_task(self, board_id, task_id):
        try:
            response = self.get(f"/boards/{board_id}/tasks/{task_id}")
            logger.info(
                f"Got task by board id: {board_id} and task id: {task_id}"
                f"status: {response.status_code}"
            )
            return response
        except Exception as error:
            logger.error(
                f"Failed to get board by board id: {board_id}, task by task id: {task_id}: {error}"
            )
            assert False, f"Request failed: {error}"

    @allure.step("Get task by query")
    def get_tasks_by_search(self, query):
        try:
            response = self.get(f"/tasks/search?q={query}")
            logger.info(
                f"Got task by use query: {query}, status: {response.status_code}"
            )
            return response
        except Exception as error:
            logger.error(f"Failed to get task by use query: {query} {error}")
            assert False, f"Request failed: {error}"

    @allure.step("Create task with board id: {board_id} and data")
    def create_task(self, board_id, data):
        try:
            response = self.post(f"/boards/{board_id}/tasks", data)
            logger.info(
                f"Success create task by board id: {board_id} and data: {data}"
                f"status: {response.status_code}"
            )
            return response
        except Exception as error:
            logger.error(
                f"Failed to create task with board id: {board_id} and data: {data}"
            )
            assert False, f"Request failed: {error}"

    @allure.step("Delete task with the board id: {board_id} and task id: {task_id}")
    def delete_task(self, board_id, task_id):
        try:
            response = self.delete(f"/boards/{board_id}/tasks/{task_id}")
            logger.info(
                f"Success delete task by use board id {board_id} and task id {task_id}"
                f"status: {response.status_code}"
            )
            return response
        except Exception as error:
            logger.error(
                f"Failed to delete task with board id: {board_id} and task id: {task_id}"
            )
            assert False, f"Request failed: {error}"
