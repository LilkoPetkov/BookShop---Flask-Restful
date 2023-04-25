from werkzeug.exceptions import BadRequest

from db import db
from managers.auth import auth
from models import Order, Book, OrderStatus
from services.SES import SESservice
from services.STRP import PaymentSession


class OrderManager:
    @staticmethod
    def create_order(order_data):
        current_user = auth.current_user()
        requested_title = order_data["book_title"]
        requested_author = order_data["book_author"]
        find_book_by_title = Book.query.filter_by(title=requested_title).first()
        current_user_email = current_user.email
        order = Order(**order_data)

        if find_book_by_title:
            order.price_to_pay = find_book_by_title.price
            P = PaymentSession()
            payment_session = P.create_payment_session(
                current_user.first_name + current_user.last_name,
                int(order.price_to_pay * 100),
                order_data["quantity"],
            )
            order.user_id = current_user.id
            order.payment_link = payment_session["url"]
            order.payment_session_id = payment_session["id"]

        # current_user_email = current_user.email
        # order = Order(**order_data)
        # order_id = order.id

        if find_book_by_title:
            if find_book_by_title.author == requested_author:
                SES = SESservice(current_user_email)
                # Required only for sandbox accounts, for production SES.send_email() is enough.
                if not SES.is_verified():
                    SES.verify_email()
                else:
                    SES.send_email()

                db.session.add(order)
                db.session.commit()

                return order
            raise BadRequest("Book does not exist")
        raise BadRequest("The book does not exist")

    @staticmethod
    def get_all_user_orders():
        current_user = auth.current_user()
        all_user_orders = Order.query.filter_by(user_id=current_user.id).all()

        return all_user_orders

    @staticmethod
    def _get_all_orders():
        all_orders = Order.query.filter_by().all()

        return all_orders

    @staticmethod
    def _validate_order(order_id):
        order = Order.query.filter_by(id=order_id).first()
        session_id = order.payment_session_id

        if not order:
            raise BadRequest("Order with such ID does not exist")
        if order.status != OrderStatus.pending:
            raise BadRequest("Cannot change status. Order is already processed")
        if PaymentSession().check_payment_processed(session_id) != "paid":
            raise BadRequest("The order is not paid still. It cannot be processed.")

    @staticmethod
    def approve_order(order_id):
        OrderManager._validate_order(order_id)

        Order.query.filter_by(id=order_id).update({"status": OrderStatus.processed})
        db.session.commit()

    @staticmethod
    def reject_order(order_id):
        OrderManager._validate_order(order_id)
        order = Order.query.filter_by(id=order_id).first()
        session_id = order.payment_session_id

        Order.query.filter_by(id=order_id).update({"status": OrderStatus.rejected})

        if PaymentSession().check_payment_processed(session_id) == "paid":
            raise BadRequest("The payment has been processed already, the order cannot be rejected.")

        db.session.commit()
