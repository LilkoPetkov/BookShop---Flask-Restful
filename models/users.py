from db import db
from models.enums import RoleType


class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(20), nullable=False)
    last_name = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(120), nullable=False, unique=True)
    phone = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(255), nullable=False)
    role = db.Column(
        db.Enum(RoleType),
        default=RoleType.client,
        nullable=False,
    )
    card_holder_name = db.Column(db.String(255), nullable=False)
    cvv = db.Column(db.Integer(), nullable=False)
    card_number = db.Column(db.Integer(), nullable=False)


