from models import RoleType
from tests.base import TestRESTApiBase, generate_token
from tests.factory import UserFactory


class TestLoginRequired(TestRESTApiBase):
    def test_authentication_is_required(self):
        all_guarded_urls = [
            ("POST", "/post-order"),
            ("GET", "/books"),
            ("GET", "/all-orders"),
            ("GET", "/process-order/10"),
            ("GET", "/reject-order/10"),
            ("GET", "/my-orders"),
            ("DELETE", "/books/12")
        ]

        for method, url in all_guarded_urls:
            if method == "GET":
                res = self.client.get(url)
            elif method == "POST":
                res = self.client.post(url)
            elif method == "PUT":
                res = self.client.put(url)
            elif method == "DELETE":
                res = self.client.delete(url)

        assert res.status_code == 401
        assert res.json == {"message": "Invalid or missing token"}


    def test_permission_required_post_order_requires_client(self):
        user = UserFactory(role=RoleType.book_manager)
        token = generate_token(user)
        headers = {"Authorization": f"Bearer {token}"}

        res = self.client.post("/post-order", headers=headers)

        assert res.status_code == 403
        assert res.json == {"message": "You do not have permission to access this resource"}

    def test_permission_required_delete_book_requires_admin_book_manager(self):
        user = UserFactory(role=RoleType.book_manager)
        token = generate_token(user)
        headers = {"Authorization": f"Bearer {token}"}

        res = self.client.delete("/books/2", headers=headers)

        assert res.status_code == 403
        assert res.json == {"message": "You do not have permission to access this resource"}

    def test_permission_required_delete_book_requires_admin_client(self):
        user = UserFactory(role=RoleType.client)
        token = generate_token(user)
        headers = {"Authorization": f"Bearer {token}"}

        res = self.client.delete("/books/3", headers=headers)

        assert res.status_code == 403
        assert res.json == {"message": "You do not have permission to access this resource"}

    def test_get_all_orders_requires_book_manager_client(self):
        user = UserFactory(role=RoleType.client)
        token = generate_token(user)
        headers = {"Authorization": f"Bearer {token}"}

        res = self.client.get("/all-orders", headers=headers)

        assert res.status_code == 403
        assert res.json == {"message": "You do not have permission to access this resource"}

    def test_get_all_orders_requires_book_manager_admin(self):
        user = UserFactory(role=RoleType.client)
        token = generate_token(user)
        headers = {"Authorization": f"Bearer {token}"}

        res = self.client.get("/all-orders", headers=headers)

        assert res.status_code == 403
        assert res.json == {"message": "You do not have permission to access this resource"}

    def test_permission_required_to_approve_reject_orders_requires_book_manager(self):
        user = UserFactory(role=RoleType.admin)
        token = generate_token(user)
        headers = {"Authorization": f"Bearer {token}"}

        res = self.client.get("/process-order/10", headers=headers)

        assert res.status_code == 403
        assert res.json == {"message": "You do not have permission to access this resource"}

        res = self.client.get("/reject-order/10", headers=headers)

        assert res.status_code == 403
        assert res.json == {"message": "You do not have permission to access this resource"}