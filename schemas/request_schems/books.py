from marshmallow import Schema, fields, validate

from utils.validations import Validation

validation = Validation()


class BookRequestSchema(Schema):
    title = fields.Str(required=True, validate=validate.Length(min=2, max=100))
    author = fields.Str(required=True, validate=validate.Length(min=2, max=100))
    description = fields.Str(required=True, validate=validate.Length(min=10, max=1_500))
    price = fields.Float(required=True, validate=validate.Range(min=0.01, max=10_000_000))
    available_copies = fields.Str(required=False)
