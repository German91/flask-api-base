from flask_restful import Resource, abort, reqparse

from models import Todo

class TodoList(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('name', type=str, required=True, help='Todo name is required')
    parser.add_argument('description', type=str)

    def get(self):
        """ Return all todos """
        todos = Todo.query.all()
        return {'todos': list(map(lambda x: x.json(), todos))}, 200

    def post(self):
        """ Create new todo """
        data = TodoList.parser.parse_args()
        todo = Todo(data['name'], data['description'])
        try:
            todo.save()
        except:
            return {'message': 'A problem occured creating todo item'}, 500
        return {'message': '{} successfully created'.format(data['name'])}, 202


class TodoItem(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('id', type=int, required=True, help='Todo id is required')

    def get(self, todo_id):
        """ Get todo item by id """
        todo = Todo.query.filter_by(id=todo_id).first()
        if todo:
            return todo.json(), 200
        return {'message': 'Todo item with id {} does not exists'.format(self.todo_id)}

    def delete(self, todo_id):
        """ Delete a todo item """
        todo = Todo.query.filter_by(id=todo_id).first()
        if todo:
            todo.delete()
            return {'message', 'Todo item successfully removed'}, 200
        return {'message': 'Todo item not found'}, 400
