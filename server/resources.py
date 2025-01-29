from flask_restful import Resource, reqparse
from models import db, Driver, Circuit, Stat, DriverCircuit
from flask import jsonify

# Helper function for data validation
def validate_number(value):
    try:
        float(value)
        return value
    except ValueError:
        raise ValueError("Value must be a number")
