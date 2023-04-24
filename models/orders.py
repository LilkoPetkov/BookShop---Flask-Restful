from datetime import datetime

from db import db
from models.enums import OrderStatus


class Order(db.Model):
    __tablename__ = 'orders'

    id = db.Column(db.Integer, primary_key=True)
    book_title = db.Column(db.String(100), nullable=False)
    book_author = db.Column(db.String(100), nullable=False)
    additional_request = db.Column(db.String(255), nullable=True)
    delivery_address = db.Column(db.String(255), nullable=True)
    price_to_pay = db.Column(db.Float, nullable=False)
    posted_on = db.Column(db.DateTime, default=datetime.utcnow(), nullable=False)
    status = db.Column(
        db.Enum(OrderStatus),
        default=OrderStatus.pending,
        nullable=False
    )
    payment_link = db.Column(db.String(1024), nullable=True)
    payment_session_id = db.Column(db.String(255), nullable=True)
    quantity = db.Column(db.Integer, nullable=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    buyer = db.relationship('User')
