from flask import request
from flask_restful import Resource

from managers.auth import auth
from managers.order import OrderManager
from models import RoleType, Order
from schemas.request_schems.orders import OrderRequestSchema
from schemas.response_schemas.order import OrderResponseSchema, ClientOrderResponseSchema
from utils.decorators import validate_schema, permission_required


class OrdersResource(Resource):
    @auth.login_required
    @permission_required(RoleType.client)
    @validate_schema(OrderRequestSchema)
    def post(self):
        data = request.get_json()
        order = OrderManager.create_order(data)

        return OrderResponseSchema().dump(order), 201


class UserOrdersResource(Resource):
    @auth.login_required
    @permission_required(RoleType.client)
    def get(self):
        all_user_orders = OrderManager.get_all_user_orders()

        return ClientOrderResponseSchema(many=True).dump(all_user_orders), 200


class ManagerOrdersResource(Resource):
    @auth.login_required
    @permission_required(RoleType.admin)
    def get(self):
        all_orders = OrderManager._get_all_orders()

        return OrderResponseSchema(many=True).dump(all_orders), 200


class OrderProcessResource(Resource):
    @auth.login_required
    @permission_required(RoleType.admin)
    def get(self, _id):
        order = Order.query.filter_by(id=_id).first()
        OrderManager.approve_order(_id)

        return {"message": f"Order {order.id} successfully processed"}, 200


class OrderRejectResource(Resource):
    @auth.login_required
    @permission_required(RoleType.admin)
    def get(self, _id):
        order = Order.query.filter_by(id=_id).first()
        OrderManager.reject_order(_id)

        return {"message": f"Order {order.id} successfully rejected"}, 200
