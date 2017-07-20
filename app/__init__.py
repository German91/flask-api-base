from flask import Flask

# local imports
from .resources.todos import todos_api
from .resources.users import users_api
from instance.config import app_config
from db import db

def create_app(config_name):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(app_config[config_name])
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)

    # Register Blueprint
    app.register_blueprint(todos_api)
    app.register_blueprint(users_api)

    return app
