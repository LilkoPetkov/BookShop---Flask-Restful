from marshmallow import Schema, fields


#  Data we expect to get from the request
class UserRegisterRequestSchema(Schema):
    first_name = fields.String(required=True)
    last_name = fields.String(required=True)
    email = fields.Email(required=True)
    phone = fields.String(required=True)
    password = fields.String(required=True)
    card_holder_name = fields.String(required=True)
    cvv = fields.Integer(required=True)
    card_number = fields.Integer(required=True)
