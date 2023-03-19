import enum


class RoleType(enum.Enum):
    client = "client"
    book_manager = "manager"
    admin = "admin"


class OrderStatus(enum.Enum):
    processed = "Processed"
    pending = "Pending"
    rejected = "Rejected"
