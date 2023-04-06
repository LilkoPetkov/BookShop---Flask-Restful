from resources.auth import RegisterResource, LoginResource
from resources.book import BookResource
from resources.order import OrdersResource

routes = (
    (RegisterResource, "/register"),
    (LoginResource, "/login"),
    (OrdersResource, "/post-orders"),
    (BookResource, "/add-book")
)
