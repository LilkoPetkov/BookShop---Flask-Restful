from db import db
from models import Book


class BookManager:
    @staticmethod
    def add_book(book_data):
        book = Book(**book_data)

        db.session.add(book)
        db.session.commit()

        return book
