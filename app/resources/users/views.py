from flask_restful import Resource, reqparse

from app.models import User

parser = reqparse.RequestParser()
parser.add_argument('useranme', type=str, required=True, help="Username is required")
parser.add_argument('password', type=str, required=True, help="Password is required")

class UserList(Resource):
    def get(self):
        """ Return all users """
        users = User.query.all()
        return {'users': list(map(lambda x: x.json(), users))}

    def post(self):
        """ Create new user """
        data = parser.parse_args()
        user = User(data['username'], data['password'])
        try:
            user.save()
        except:
            return {'message': 'Problem occured creating user'}, 500
        return {'message': 'User successfully created'}, 202
