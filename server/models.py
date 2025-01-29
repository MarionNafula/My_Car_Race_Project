from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin

db = SQLAlchemy()

class Driver(db.Model, SerializerMixin):
    __tablename__ = 'drivers'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    team = db.Column(db.String(100), nullable=False)
    stats = db.relationship("Stat", backref="driver", lazy=True)

    serialize_rules = ('-stats.driver',)

class Circuit(db.Model, SerializerMixin):
    __tablename__ = 'circuits'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    location = db.Column(db.String(100), nullable=False)
    length = db.Column(db.Float, nullable=False)
    stats = db.relationship("Stat", backref="circuit", lazy=True)

    serialize_rules = ('-stats.circuit',)