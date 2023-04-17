from models import Book


def check_if_book(title, author):
    book = Book.query.filter_by(title=title, author=author).first()

    if book:
        return True
    return False
