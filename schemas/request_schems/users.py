from marshmallow import fields, validate

from schemas.response_schemas.base import UserRequestBase
from utils.validations import Validation

validation = Validation()


class UserRegisterRequestSchema(UserRequestBase):
    first_name = fields.String(required=True, validate=validate.Length(min=3, max=20))
    last_name = fields.String(required=True, validate=validate.Length(min=3, max=20))
    phone = fields.String(required=True, validate=validate.And(validation.phone_number_validation))
    card_holder_name = fields.String(required=True, validate=validate.Length(min=3, max=20))
    cvv = fields.Integer(required=True, validate=validate.And(validation.validate_cvv))
    card_number = fields.String(required=True, validate=validate.Length(min=16, max=19))


class UserLoginRequestSchema(UserRequestBase):
    pass
