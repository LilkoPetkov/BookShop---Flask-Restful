from random import randint, uniform


import factory

from db import db
from models import User, RoleType, Order, Book


class BaseFactory(factory.Factory):
    @classmethod
    def create(cls, **kwargs):
        object = super().create(**kwargs)
        db.session.add(object)
        db.session.commit()
        return object


class UserFactory(BaseFactory):
    class Meta:
        model = User

    id = factory.Sequence(lambda n: n)
    first_name = factory.Faker("first_name")
    last_name = factory.Faker("last_name")
    email = factory.Faker("email")
    phone = str(randint(100000, 200000))
    password = factory.Faker("password")
    role = RoleType.client


class OrderFactory(BaseFactory):
    class Meta:
        model = Order

    id = factory.Sequence(lambda n: n)
    book_title = "Test1"
    book_author = "Test2"
    price_to_pay = str(uniform(1.5, 150.0))
    user_id = 2


class BookFactory(BaseFactory):
    class Meta:
        model = Book

    id = factory.Sequence(lambda n: n)
    title = "Test1"
    author = "Test2"
    price = str(uniform(1.5, 150.0))
    description = "Test"
