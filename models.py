"""models.py ."""

# from flask_sqlalchemy import SQLAlchemy
from flask.ext.sqlalchemy import SQLAlchemy
db = SQLAlchemy()


class User(db.Model):
    """A very simple user model for the database."""

    __tablename__ = 'users'
    uid = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100))
    email = db.Column(db.String(100), unique=True)

    def __init__(self, username='', email=''):
        """Initialize and title case username."""
        self.username = username.title()
        self.email = email

    def __repr__(self):
        """String represenation of User showing only username."""
        return '<User %r>' % self.username
