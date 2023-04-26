from marshmallow import Schema, fields, validate


class OrderRequestSchema(Schema):
    book_title = fields.Str(required=True, validate=validate.Length(min=1, max=150))
    book_author = fields.Str(required=True, validate=validate.Length(min=1, max=150))
    delivery_address = fields.Str(required=True, validate=validate.Length(min=2, max=150))
    quantity = fields.Int(required=True, validate=validate.Range(min=1, max=1_000))
