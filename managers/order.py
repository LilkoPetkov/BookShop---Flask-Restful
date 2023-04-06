from werkzeug.exceptions import BadRequest

from db import db
from managers.auth import auth
from models import Order, Book
from services.SES import SESservice
from utils.logs import aws_logs


class OrderManager:
    @staticmethod
    def create_order(order_data):
        current_user = auth.current_user()
        current_user_email = current_user.email
        order_data["user_id"] = current_user.id
        order = Order(**order_data)
        order_id = order.id

        requested_title = order_data["book_title"]
        requested_author = order_data["book_author"]

        find_book_by_title = Book.query.filter_by(title=requested_title).first()

        if find_book_by_title:
            find_book_by_author = Book.query.filter_by(author=requested_author).first()
            if find_book_by_author:
                order_data["price_to_pay"] = find_book_by_title.price

                SES = SESservice(current_user_email, order_id)
                # Required only for sandbox accounts, for production SES.send_email() is enough.
                if not SES.is_verified():
                    res = dict(SES.verify_email())

                    with open(aws_logs, "a") as f:
                        f.write(str(res) + "\n")

                else:
                    SES.send_email()

                # current_user["shopping_basket"] = 'book_title': find_book_by_title.title
                # To Do: to get the shopping cart to accept objects
                db.session.add(order)
                db.session.commit()

                return order
            raise BadRequest("Book does not exist")
        raise BadRequest("The book does not exist")

