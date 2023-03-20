from marshmallow import Schema, fields


class BookRequestSchema(Schema):
    title = fields.Str(required=True)
    author = fields.Str(required=True)
    description = fields.Str(required=True)
    price = fields.Float(required=True)
    available_copies = fields.Str(required=False)
