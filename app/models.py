from db import db
from .common.utils import bcrypt

class Base(db.Model):
    __abstract__ = True

    id = db.Column(db.Integer, primary_key=True)
    created_date = db.Column(db.DateTime, default=db.func.current_timestamp())
    updated_date = db.Column(db.DateTime, default=db.func.current_timestamp())


class Todo(Base):
    __tablename__ = 'todos'

    name = db.Column(db.String(100), unique=True)
    description = db.Column(db.String(255), default='')
    slug = db.Column(db.String(100), unique=True)

    def __init__(self, name, description, slug):
        """ Initialize Todo """
        self.name = name
        self.description = description
        self.slug = slug

    @classmethod
    def get_by_slug(cls, slug):
        return cls.query.filter_by(slug=slug).first()

    def json(self):
        """ Return object as json """
        return {
            'slug': self.slug,
            'name': self.name,
            'description': self.description,
        }

    def save(self):
        """ Save todo to database """
        db.session.add(self)
        db.session.commit()

    def delete(self):
        """ Delete todo from the database """
        db.session.delete(self)
        db.session.commit()

    def __repr__(self):
        """ Return todo name which represents the todo object """
        return "<Todo: {}>".format(self.name)


class User(Base):
    __tablename__ = 'users'

    username = db.Column(db.String(100), unique=True, nullable=False)
    _password = db.Column(db.Binary(60), nullable=False)

    def __init__(self, username, password):
        self.username = username
        self._password = bcrypt.generate_password_hash(password)

    def json(self):
        return {
            'username': self.username,
            'password': self._password
        }

    def save(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_by_username(cls, username):
        return cls.query.filter_by(username).first()

    def __repr__(self):
        """ Return username which represetns user object """
        return "<User: {}".format(self.username)
