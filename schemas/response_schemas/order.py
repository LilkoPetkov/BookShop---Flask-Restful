from marshmallow import Schema, fields

from schemas.response_schemas.base import OrderResponseBase


class OrderResponseSchema(OrderResponseBase):
    payment_link = fields.Str(required=False)


class ClientOrderResponseSchema(OrderResponseBase):
    pass
