import os

from flask import Flask
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager

# local imports
from resources.todos.routes import todos_api
from instance.config import app_config
from db import db

# Configuration
app = Flask(__name__, instance_relative_config=True)
app.config.from_object(app_config[os.getenv('APP_SETTINGS')])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

migrate = Migrate(app, db)

# Manager commands
manager = Manager(app)
manager.add_command('db', MigrateCommand)

# Register Blueprint
app.register_blueprint(todos_api)
