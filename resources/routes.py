from resources.auth import RegisterResource, LoginResource
from resources.book import BookResource, BooksResource
from resources.order import OrdersResource, ManagerOrdersResource, OrderProcessResource, OrderRejectResource, \
    UserOrdersResource

routes = (
    (RegisterResource, "/register"),
    (LoginResource, "/login"),
    (OrdersResource, "/post-order"),
    (BookResource, "/books"),
    (ManagerOrdersResource, "/all-orders"),
    (OrderProcessResource, "/process-order/<int:_id>"),
    (OrderRejectResource, "/reject-order/<int:_id>"),
    (UserOrdersResource, "/my-orders"),
    (BooksResource, "/books/<int:_id>"),
)
