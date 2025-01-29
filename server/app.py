from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)
migrate = Migrate(app, db)

api = Api(app)

# Import resources
from resources import DriverResource, CircuitResource, StatResource, DriverCircuitResource

# Register API routes
api.add_resource(DriverResource, "/drivers", "/drivers/<int:id>")
api.add_resource(CircuitResource, "/circuits", "/circuits/<int:id>")
api.add_resource(StatResource, "/stats", "/stats/<int:id>")
api.add_resource(DriverCircuitResource, "/driver_circuits")

@app.route("/")
def home():
    return "Welcome to the Car Race API!"


if __name__ == "__main__":
    app.run(debug=True)