from flask_restful import Resource, abort, reqparse
from slugify import slugify

from models.todos import Todo

parser = reqparse.RequestParser()
parser.add_argument('name', type=str, required=True, help='Todo name is required', location='json')
parser.add_argument('description', type=str, location='json')

class TodoList(Resource):
    def get(self):
        """ Return all todos """
        todos = Todo.query.all()
        return {'todos': list(map(lambda x: x.json(), todos))}, 200

    def post(self):
        """ Create new todo """
        data = parser.parse_args()
        slug = slugify(data['name'])
        todo = Todo(data['name'], data['description'], slug)
        try:
            todo.save()
        except:
            return {'message': 'A problem occured creating todo item'}, 500
        return {'message': 'Todo item successfully created'}, 202


class TodoItem(Resource):
    def get(self, slug):
        """ Get todo item by id """
        todo = Todo.get_by_slug(slug)
        if todo:
            return todo.json(), 200
        return {'message': 'Todo item not found'}, 404

    def put(self, slug):
        """ Update a todo item """
        data = parser.parse_args()
        todo = Todo.get_by_slug(slug)
        if todo:
            todo.name = data['name']
            todo.description = data['description']
            todo.slug = create_slug(todo.name)
            todo.save()
            return {'message': 'Todo item successfully updated'}, 200
        return {'message': 'Todo item not found'}, 404

    def delete(self, slug):
        """ Delete a todo item """
        todo = Todo.get_by_slug(slug)
        if todo:
            todo.delete()
            return {'message', 'Todo item successfully removed'}, 200
        return {'message': 'Todo item not found'}, 404
