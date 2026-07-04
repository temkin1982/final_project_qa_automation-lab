from api.http_client import HttpClient


class Tasks(HttpClient):
    """Create Tasks modal window."""

    def get_task(self, board_id, task_id):
        return self.get(f"/boards/{board_id}/tasks/{task_id}")

    def get_tasks_by_search(self, query):
        return self.get(f"/tasks/search?q={query}")

    def create_task(self, board_id, data):
        return self.post(f"/boards/{board_id}/tasks", data)

    def delete_task(self, board_id, task_id):
        return self.delete(f"/boards/{board_id}/tasks/{task_id}")
