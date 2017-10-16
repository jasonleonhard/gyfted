"""NEW models.py ."""
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.secret_key = "development-key"
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # True
app.config['TEMPLATES_AUTO_RELOAD'] = True
app.debug = True

db = SQLAlchemy(app)
db.init_app(app)
db.create_all()


class Ticket(db.Model):
    """A very simple ticket model for the database.

    Offerer, Requester and Deliver are fields for now.
    May later use relation like has-many belongs-to.
    """

    __tablename__ = 'tickets'
    tid = db.Column(db.Integer, primary_key=True)

    item = db.Column(db.String(100))
    deliverer = db.Column(db.String(100))

    gyfter = db.Column(db.String(100))
    pickup_address = db.Column(db.String(100))
    pickup_time = db.Column(db.String(100))
    pickup_date = db.Column(db.String(100))

    requester = db.Column(db.String(100))
    dropoff_address = db.Column(db.String(100))
    dropoff_time = db.Column(db.String(100))
    dropoff_date = db.Column(db.String(100))

    created = db.Column(db.DateTime)
    hidden = db.Column(db.Boolean)
    status = db.Column(db.String(100))

    def __init__(self, item, deliverer, gyfter, pickup_address, pickup_time,
                 pickup_date, requester, dropoff_address, dropoff_time,
                 dropoff_date):
        """Initialize each field. Sections include: by, from, to, other"""
        self.item = item
        self.deliverer = deliverer

        self.gyfter = gyfter
        self.pickup_address = pickup_address
        self.pickup_time = pickup_time
        self.pickup_date = pickup_date

        self.requester = requester
        self.dropoff_address = dropoff_address
        self.dropoff_time = dropoff_time
        self.dropoff_date = dropoff_date

        self.created = datetime.utcnow()
        self.hidden = False
        self.status = 'ready'

    def __repr__(self):
        """String represenation of User showing only username and id."""
        return '<Ticket %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s> ' % (self.tid, self.item, self.deliverer, self.gyfter, self.pickup_address, self.pickup_time, self.pickup_date, self.requester, self.dropoff_address, self.dropoff_time, self.dropoff_date, self.created, self.hidden, self.status)
