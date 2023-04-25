from models import RoleType
from tests.base import TestRESTApiBase, generate_token
from tests.factory import UserFactory, BookFactory


class TestBookSchema(TestRESTApiBase):
    def test_required_fields_raises_when_missing(self):
        user = UserFactory(role=RoleType.client)
        token = generate_token(user)
        headers = {"Authorization": f"Bearer {token}", "Content-Type": "application/json"}

        data = {}
        res = self.client.post("/post-order", headers=headers, json=data)

        assert res.status_code == 400
        assert res.json == {
            'message': {'book_author': ['Missing data for required field.'],
                        'book_title': ['Missing data for required field.'],
                        'delivery_address': ['Missing data for required field.'],
                        'quantity': ['Missing data for required field.']}
        }

    def test_book_delete_book_exists(self):
        user = UserFactory(role=RoleType.book_manager)
        book = BookFactory()
        token = generate_token(user)
        headers = {"Authorization": f"Bearer {token}", "Content-Type": "application/json"}

        res = self.client.delete(f"/books/{book.id}/delete", headers=headers)

        assert res.status_code == 200

    def test_book_delete_book_does_not_exist(self):
        user = UserFactory(role=RoleType.book_manager)
        book = BookFactory()
        token = generate_token(user)
        headers = {"Authorization": f"Bearer {token}", "Content-Type": "application/json"}

        res = self.client.delete(f"/books/2/delete", headers=headers)

        assert res.status_code == 400

