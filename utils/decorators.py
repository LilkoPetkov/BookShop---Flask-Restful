from flask import request
from werkzeug.exceptions import BadRequest


#  Decorator for validating schema data
def validate_schema(schema_name):
    def decorated_function(func):
        def wrapper(*args, **kwargs):
            schema = schema_name()
            data = request.get_json()
            errors = schema.validate(data)

            if not errors:
                return func(*args, **kwargs)
            raise BadRequest(errors)
        return wrapper
    return decorated_function
