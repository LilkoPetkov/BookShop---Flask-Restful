from flask import Flask
from flask_migrate import Migrate
from flask_restful import Api

from db import db
from resources.routes import routes

app = Flask(__name__)
#  DevelopmentConfig is coming from the config.py file as a class for the dev environment
app.config.from_object("config.DevelopmentConfig")

api = Api(app)
migrate = Migrate(app, db)

with app.app_context():
    db.init_app(app)

[api.add_resource(*route) for route in routes]

if __name__ == "__main__":
    app.run()

#  Books table -> no relation to any users, it should be visible by anyone
#  Users table -> connected to orders
