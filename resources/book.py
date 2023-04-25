from flask import request
from flask_restful import Resource
from werkzeug.exceptions import BadRequest

from db import db
from managers.auth import auth
from managers.book import BookManager
from models import RoleType, Book
from schemas.request_schems.books import BookRequestSchema
from schemas.response_schemas.books import BookResponseSchema
from utils.decorators import validate_schema, permission_required


class BookResource(Resource):
    def get(self):
        books = Book.query.filter_by().all()

        return BookResponseSchema(many=True).dump(books)


class AddBookResource(Resource):
    @auth.login_required
    @permission_required(RoleType.book_manager)
    @validate_schema(BookRequestSchema)
    def post(self):
        data = request.get_json()
        book = BookManager.add_book(data)

        return BookResponseSchema().dump(book), 201


class BooksResource(Resource):
    @auth.login_required
    @permission_required(RoleType.book_manager)
    def delete(self, _id):
        book = Book.query.filter_by(id=_id).first()

        if book:
            book_name = book.title
            db.session.delete(book)
            db.session.commit()

            return {"message": f'{book_name} deleted successfully'}, 200
        raise BadRequest(f"Book with ID: {_id} does not exist in the catalogue")
