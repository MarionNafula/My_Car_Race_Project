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
    
# DRIVERS
class DriverResource(Resource):
    def get(self, id=None):
        if id:
            driver = Driver.query.get(id)
            return driver.to_dict() if driver else {"message": "Driver not found"}, 404
        return [driver.to_dict() for driver in Driver.query.all()], 200

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument("name", required=True)
        parser.add_argument("age", type=int, required=True)
        parser.add_argument("team", required=True)
        args = parser.parse_args()

        driver = Driver(name=args["name"], age=args["age"], team=args["team"])
        db.session.add(driver)
        db.session.commit()
        return driver.to_dict(), 201
    
# CIRCUITS
class CircuitResource(Resource):
    def get(self, id=None):
        if id:
            circuit = Circuit.query.get(id)
            return circuit.to_dict() if circuit else {"message": "Circuit not found"}, 404
        return [circuit.to_dict() for circuit in Circuit.query.all()], 200
    
# STATS
class StatResource(Resource):
    def get(self, id=None):
        if id:
            stat = Stat.query.get(id)
            return stat.to_dict() if stat else {"message": "Stat not found"}, 404
        return [stat.to_dict() for stat in Stat.query.all()], 200
