from flask import Blueprint
from flask_restful import Api

from .views import UserList

users_api = Blueprint('users_api', __name__)
api = Api(users_api)

api.add_resource(UserList, '/api/v1/users', endpoint='users')
