from werkzeug.exceptions import BadRequest

from db import db
from models import Book
from utils.check_if_book import check_if_book


class BookManager:
    @staticmethod
    def add_book(book_data):
        book = Book(**book_data)

        if check_if_book(
            book_data["title"],
            book_data["author"],
        ):
            raise BadRequest(f"{book_data['title']} already exists in the catalogue")

        db.session.add(book)
        db.session.commit()

        return book
