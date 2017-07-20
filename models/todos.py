from common.db import db
from common.models import Base

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
        """ Return todo name wich represents the todo object """
        return "<Todo: {}>".format(self.name)
