from flask_restful import Resource, reqparse
from models import db, Driver, Circuit, Stat, DriverCircuit
from flask import jsonify, make_response

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
            if driver:
                return make_response(jsonify(driver.to_dict()), 200)
            return make_response(jsonify({"message": "Driver not found"}), 404)

        drivers = Driver.query.all()
        drivers_list = [driver.to_dict() for driver in drivers]
        return make_response(jsonify({"drivers": drivers_list}), 200)

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument("name", required=True)
        parser.add_argument("age", type=int, required=True)
        parser.add_argument("team", required=True)
        args = parser.parse_args()

        driver = Driver(name=args["name"], age=args["age"], team=args["team"])
        db.session.add(driver)
        db.session.commit()
        return make_response(jsonify(driver.to_dict()), 201)
