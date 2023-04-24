from marshmallow import fields, validate

from schemas.response_schemas.base import UserRequestBase
from utils.validations import Validation

validation = Validation()


class UserRegisterRequestSchema(UserRequestBase):
    first_name = fields.String(required=True, validate=validate.Length(min=3, max=20))
    last_name = fields.String(required=True, validate=validate.Length(min=3, max=20))
    phone = fields.String(required=True, validate=validate.And(validation.phone_number_validation))


class UserLoginRequestSchema(UserRequestBase):
    pass
