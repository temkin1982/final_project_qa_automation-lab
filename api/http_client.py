import requests


class HttpClient:
    """Base class for all API pages."""

    def __init__(self):
        self.base_url = "http://localhost:8000"
        self.token = self._login()

    def _login(self):
        response = requests.post(
            f"{self.base_url}/auth/login",
            json={"email": "admin@example.com", "password": "admin123"},
            timeout=10,
        )
        return response.json()["access_token"]

    def get(self, endpoint):
        headers = {"Authorization": f"Bearer {self.token}"}
        return requests.get(f"{self.base_url}{endpoint}", headers=headers, timeout=10)

    def get_with_token(self, endpoint, token):
        headers = {"Authorization": f"Bearer {token}"}
        return requests.get(f"{self.base_url}{endpoint}", headers=headers, timeout=10)

    def post(self, endpoint, data):
        headers = {
            "Authorization": f"Bearer {self.token}",
            "accept": "application/json",
            "Content-Type": "application/json",
        }
        return requests.post(
            f"{self.base_url}{endpoint}", json=data, headers=headers, timeout=10
        )

    def put(self, endpoint, data):
        headers = {
            "Authorization": f"Bearer {self.token}",
            "accept": "application/json",
            "Content-Type": "application/json",
        }
        return requests.put(
            f"{self.base_url}{endpoint}", json=data, headers=headers, timeout=10
        )

    def delete(self, endpoint):
        headers = {"Authorization": f"Bearer {self.token}"}
        return requests.delete(
            f"{self.base_url}{endpoint}", headers=headers, timeout=10
        )
