from marshmallow import Schema, fields, validate

from utils.validations import Validation

V = Validation()


class UserRequestBase(Schema):
    email = fields.Email(required=True, validate=validate.And(V.validate_email))
    password = fields.String(required=True, validate=validate.And(
        validate.Length(min=8, max=20), V.validate_password)
                             )


class OrderResponseBase(Schema):
    posted_on = fields.Str(required=True)
    book_title = fields.Str(required=True)
    book_author = fields.Str(required=True)
    delivery_address = fields.Str(required=True)
    price_to_pay = fields.Float(required=True)
    quantity = fields.Integer(required=True)
