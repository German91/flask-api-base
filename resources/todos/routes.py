from flask import Blueprint
from flask_restful import Api

from .views import TodoList, TodoItem

todos_api = Blueprint('todos_api', __name__)
api = Api(todos_api)

api.add_resource(TodoList, '/api/v1/todos', endpoint='todos')
api.add_resource(TodoItem, '/api/v1/todos/<slug>', endpoint='todo')
