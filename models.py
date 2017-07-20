from db import db

class Base(db.Model):
    __abstract__ = True

    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    created_date = db.Column(db.DateTime, default=db.func.now())
    updated_date = db.Column(db.DateTime, default=db.func.now(), onupdate=db.func.now())


class Todo(Base):
    __tablename__ = 'todos'

    name = db.Column(db.String(100))
    description = db.Column(db.String(255), default='')


    def __init__(self, name, description):
        """ Initialize Todo """
        self.name = name
        self.description = description

    def json(self):
        """ Return object as json """
        return {
            'id': self.id,
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
