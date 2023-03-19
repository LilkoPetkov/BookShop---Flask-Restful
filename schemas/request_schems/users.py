from marshmallow import fields

from schemas.response_schemas.base import UserRequestBase


#  Data we expect to get from the request
class UserRegisterRequestSchema(UserRequestBase):
    first_name = fields.String(required=True)
    last_name = fields.String(required=True)
    phone = fields.String(required=True)
    card_holder_name = fields.String(required=True)
    cvv = fields.Integer(required=True)
    card_number = fields.Integer(required=True)


class UserLoginRequestSchema(UserRequestBase):
    pass
