from flask import request
from flask_restful import Resource

from managers.auth import auth
from managers.order import OrderManager
from models import RoleType
from schemas.request_schems.orders import OrderRequestSchema
from utils.decorators import validate_schema, permission_required


class OrdersResource(Resource):
    @auth.login_required
    @permission_required(RoleType.client)
    @validate_schema(OrderRequestSchema)
    def post(self):
        data = request.get_json()
        data["price_to_pay"] = 18.95

        OrderManager.create_order(data)
