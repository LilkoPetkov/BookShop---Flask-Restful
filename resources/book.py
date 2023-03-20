from flask import request
from flask_restful import Resource

from managers.auth import auth
from managers.book import BookManager
from models import RoleType
from schemas.request_schems.books import BookRequestSchema
from utils.decorators import validate_schema, permission_required


class BookResource(Resource):
    @auth.login_required
    @permission_required(RoleType.client)
    @validate_schema(BookRequestSchema)
    def post(self):
        data = request.get_json()

        BookManager.add_book(data)

        # return BookResponseSchema().dump({"token": token})