"""models.py ."""

# from flask_sqlalchemy import SQLAlchemy
from flask.ext.sqlalchemy import SQLAlchemy
db = SQLAlchemy()


class User(db.Model):
    """A very simple user model for the database."""

    __tablename__ = 'users'
    uid = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100), unique=True)

    def __init__(self, name='', email=''):
        """Initialize and title case name."""
        self.name = name.title()
        self.email = email

    def __repr__(self):
        """String represenation of User showing only name."""
        return '<User %r>' % self.name
