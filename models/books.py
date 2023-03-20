from datetime import datetime

from db import db


class Book(db.Model):
    __tablename__ = 'books'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    author = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String, nullable=False)
    price = db.Column(db.Float, nullable=False)
    posted_on = db.Column(db.DateTime, default=datetime.utcnow(), nullable=False)
    available_copies = db.Column(db.Integer, default=5)
