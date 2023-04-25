from marshmallow import Schema, fields, validate


class OrderRequestSchema(Schema):
    book_title = fields.Str(required=True, validate=validate.Length(min=1, max=50))
    book_author = fields.Str(required=True, validate=validate.Length(min=1, max=50))
    delivery_address = fields.Str(required=True, validate=validate.Length(min=2, max=50))
    quantity = fields.Int(required=True, validate=validate.Range(min=1, max=1_000))
