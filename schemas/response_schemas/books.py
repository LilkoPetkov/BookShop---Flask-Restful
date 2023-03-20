from marshmallow import Schema, fields


class BookResponseSchema(Schema):
    title = fields.Str(required=True)
    author = fields.Str(required=True)
    description = fields.Str(required=True)
    price = fields.Float(required=True)
