from flask_restful import Resource, abort, reqparse

class TodoList(Resource):
    def get(self):
        """ Return all todos """
        return 'todo list'
