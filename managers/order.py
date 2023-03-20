from db import db
from managers.auth import auth
from models import Order, Book


class OrderManager:
    @staticmethod
    def create_order(order_data):
        current_user = auth.current_user()
        order_data["user_id"] = current_user.id
        order = Order(**order_data)

        requested_title = order_data["book_title"]
        requested_author = order_data["book_author"]

        find_book_by_title = Book.query.filter_by(title=requested_title).first()

        if find_book_by_title:
            find_book_by_author = Book.query.filter_by(author=requested_author).first()
            if find_book_by_author:
                order_data["price_to_pay"] = find_book_by_title.price
                # current_user["shopping_basket"] = 'book_title': find_book_by_title.title
                # To Do: to get the shopping cart to accept objects
                db.session.add(order)
                db.session.commit()
            else:
                return "The book does not exist"
        else:
            return "The book does not exist"

