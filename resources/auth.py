from flask_restful import Resource, Api
from flask import request

from app import db
from models.users import User
from schemas.request_schems.users import UserRegisterRequestSchema
from utils.decorators import validate_schema


class RegisterResource(Resource):
    @validate_schema(UserRegisterRequestSchema)
    def post(self):
        data = request.get_json()
        user = User(**data)

        db.session.add(user)
        db.session.commit()
