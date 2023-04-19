from marshmallow import Schema, fields, validate

from utils.validations import Validation

V = Validation()


class UserRequestBase(Schema):
    email = fields.Email(required=True, validate=validate.And(V.validate_email))
    password = fields.String(required=True, validate=validate.And(
        validate.Length(min=8, max=20), V.validate_password)
                             )
