from api.http_client import HttpClient


class Users(HttpClient):
    """Create Users modal window."""

    def get_user_by_id(self, user_id):
        return self.get(f"/users/{user_id}")

    def register_user(self, data):
        return self.post("/auth/register", data)

    def login_user(self, email, password):
        data = {"email": email, "password": password}
        return self.post("/auth/login", data)

    def user_me(self, token):
        return self.get_with_token("/users/me", token)

    def update_user(self, user_id, data):
        return self.put(f"/users/{user_id}", data)

    def delete_user(self, user_id):
        return self.delete(f"/users/{user_id}")
