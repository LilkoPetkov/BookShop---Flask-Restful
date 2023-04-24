from marshmallow import Schema, fields


class OrderRequestSchema(Schema):
    book_title = fields.Str(required=True)
    book_author = fields.Str(required=True)
    delivery_address = fields.Str(required=True)
    quantity = fields.Int(required=True)
