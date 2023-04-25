from unittest.mock import patch

from managers.book import BookManager
from models import RoleType, Order
from services.SES import SESservice
from services.STRP import PaymentSession
from tests.base import TestRESTApiBase, generate_token
from tests.factory import UserFactory, OrderFactory


class TestOrderSchema(TestRESTApiBase):
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

    def test_quantity_is_zero_or_less_than_zero_raises(self):
        user = UserFactory(role=RoleType.client)
        token = generate_token(user)
        headers = {"Authorization": f"Bearer {token}", "Content-Type": "application/json"}

        data = {"book_author": "Test", "book_title": "Test Test", "delivery_address": "test"}

        # Test with negative
        data["quantity"] = -1
        res = self.client.post("/post-order", headers=headers, json=data)

        assert res.status_code == 400
        assert res.json == {
            'message': {'quantity': ['Must be greater than or equal to 1 and less than or '
                                     'equal to 1000.']}
        }

        # Test with zero
        data["quantity"] = 0
        res = self.client.post("/post-order", headers=headers, json=data)

        assert res.status_code == 400
        assert res.json == {
            'message': {'quantity': ['Must be greater than or equal to 1 and less than or '
                                     'equal to 1000.']}
        }


class TestOrder(TestRESTApiBase):
    @patch.object(SESservice, "send_email")
    def test_create_order(self, mock_ses_send_email):
        orders = Order.query.all()
        assert len(orders) == 0

        # Book does not exist
        user = UserFactory(role=RoleType.client)
        token = generate_token(user)
        headers = {"Authorization": f"Bearer {token}", "Content-Type": "application/json"}

        data = {"book_author": "Test", "book_title": "Test Test", "delivery_address": "test", "quantity": 2}

        res = self.client.post("/post-order", headers=headers, json=data)

        assert res.status_code == 400

        # Book exists, different author
        BookManager.add_book(
            {
                "title": "The Great Gatsby",
                "author": "F. Scott FitzgeraDD",
                "description": "Testiing the description test.",
                "price": 22.99
            }
        )

        headers = {"Authorization": f"Bearer {token}", "Content-Type": "application/json"}

        data = {"book_author": "F. Scott Fitzgerald", "book_title": "The Great Gatsby", "delivery_address": "test",
                "quantity": 2}

        res = self.client.post("/post-order", headers=headers, json=data)

        assert res.status_code == 400

        # Book Exists, same author / Successfully added

        BookManager.add_book(
            {
                "title": "The Great GatsbyY",
                "author": "F. Scott FitzgeraDD",
                "description": "Testing the description test.",
                "price": 22.99
            }
        )

        headers = {"Authorization": f"Bearer {token}", "Content-Type": "application/json"}

        data = {"book_author": "F. Scott FitzgeraDD", "book_title": "The Great GatsbyY", "delivery_address": "test",
                "quantity": 2}

        res = self.client.post("/post-order", headers=headers, json=data)

        assert res.status_code == 201

        orders = Order.query.all()
        assert len(orders) == 1
        assert res.json["price_to_pay"] == 22.99
        assert res.json["book_author"] == "F. Scott FitzgeraDD"
        assert res.json["delivery_address"] == "test"

    @patch.object(PaymentSession, "check_payment_processed", return_value="test")
    def test_approve_order(self, mock_stripe_payment_session):
        # Book does not exist, mocked payment checkout
        user = UserFactory(role=RoleType.admin)
        user.id = 2
        order = OrderFactory()
        token = generate_token(user)
        headers = {
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json"
        }

        res = self.client.get(f"/process-order/{order.id}", headers=headers)

        assert res.status_code == 400

    @patch.object(PaymentSession, "check_payment_processed", return_value="test")
    def test_reject_order(self, mock_stripe_payment_session):
        # Book does not exist, mocked payment checkout
        user = UserFactory(role=RoleType.admin)
        user.id = 2
        order = OrderFactory()
        token = generate_token(user)
        headers = {
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json"
        }

        res = self.client.get(f"/process-order/{order.id}", headers=headers)

        assert res.status_code == 400

    def test_get_all_user_orders(self):
        user = UserFactory(role=RoleType.client)
        user.id = 2
        [OrderFactory() for _ in range(3)]
        token = generate_token(user)
        headers = {
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json"
        }

        res = self.client.get("/my-orders", headers=headers)

        assert res.status_code == 200
        assert len(res.json) == 3
