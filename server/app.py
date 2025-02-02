from flask import Flask, request, jsonify
from flask_restful import Api, Resource
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
from flask_cors import CORS  # Optional: If you need CORS support
import os

# Initialize extensions (but don't bind them to an app yet)
db = SQLAlchemy()
migrate = Migrate()
bcrypt = Bcrypt()
jwt = JWTManager()

# Models
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)

class Driver(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    team = db.Column(db.String(100), nullable=False)
    age = db.Column(db.Integer, nullable=False)

class Circuit(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    location = db.Column(db.String(100), nullable=False)
    length = db.Column(db.Float, nullable=False)

def create_app():
    app = Flask(__name__)
    CORS(app)  # Enable CORS (Optional)

    # Database configuration
    app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv('DATABASE_URI', 'sqlite:///database.db')  # Default SQLite
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["JWT_SECRET_KEY"] = os.getenv('JWT_SECRET_KEY', 'your_secret_key')  # Change for production

    # Initialize extensions with app
    db.init_app(app)
    migrate.init_app(app, db)
    bcrypt.init_app(app)
    jwt.init_app(app)
    api = Api(app)

    # Authentication Routes
    @app.route('/register', methods=['POST'])
    def register():
        data = request.get_json()
        if not data or "username" not in data or "password" not in data:
            return jsonify({"error": "Missing username or password"}), 400

        hashed_password = bcrypt.generate_password_hash(data['password']).decode('utf-8')
        new_user = User(username=data['username'], password=hashed_password)

        try:
            db.session.add(new_user)
            db.session.commit()
            return jsonify({"message": "User registered successfully!"}), 201
        except Exception as e:
            db.session.rollback()
            return jsonify({"error": "Username already exists"}), 400

    @app.route('/login', methods=['POST'])
    def login():
        data = request.get_json()
        if not data or "username" not in data or "password" not in data:
            return jsonify({"error": "Missing username or password"}), 400

        user = User.query.filter_by(username=data['username']).first()
        if user and bcrypt.check_password_hash(user.password, data['password']):
            access_token = create_access_token(identity=user.id)
            return jsonify(access_token=access_token), 200
        return jsonify({"error": "Invalid credentials"}), 401

    @app.route('/protected', methods=['GET'])
    @jwt_required()
    def protected():
        current_user = get_jwt_identity()
        return jsonify({"message": f"Hello User {current_user}, you're authorized!"})

    # CRUD API Resources
    class DriverResource(Resource):
        def get(self, id=None):
            if id:
                driver = Driver.query.get(id)
                if driver:
                    return jsonify({"id": driver.id, "name": driver.name, "team": driver.team, "age": driver.age})
                return jsonify({"error": "Driver not found"}), 404
            drivers = Driver.query.all()
            return jsonify([{"id": d.id, "name": d.name, "team": d.team, "age": d.age} for d in drivers])

        def post(self):
            data = request.get_json()
            new_driver = Driver(name=data["name"], team=data["team"], age=data["age"])
            db.session.add(new_driver)
            db.session.commit()
            return jsonify({"message": "Driver added successfully!"})

        def put(self, id):
            data = request.get_json()
            driver = Driver.query.get(id)
            if driver:
                driver.name = data["name"]
                driver.team = data["team"]
                driver.age = data["age"]
                db.session.commit()
                return jsonify({"message": "Driver updated successfully!"})
            return jsonify({"error": "Driver not found"}), 404

        def delete(self, id):
            driver = Driver.query.get(id)
            if driver:
                db.session.delete(driver)
                db.session.commit()
                return jsonify({"message": "Driver deleted successfully!"})
            return jsonify({"error": "Driver not found"}), 404

    class CircuitResource(Resource):
        def get(self, id=None):
            if id:
                circuit = Circuit.query.get(id)
                if circuit:
                    return jsonify({"id": circuit.id, "name": circuit.name, "location": circuit.location, "length": circuit.length})
                return jsonify({"error": "Circuit not found"}), 404
            circuits = Circuit.query.all()
            return jsonify([{"id": c.id, "name": c.name, "location": c.location, "length": c.length} for c in circuits])

        def post(self):
            data = request.get_json()
            new_circuit = Circuit(name=data["name"], location=data["location"], length=data["length"])
            db.session.add(new_circuit)
            db.session.commit()
            return jsonify({"message": "Circuit added successfully!"})

        def put(self, id):
            data = request.get_json()
            circuit = Circuit.query.get(id)
            if circuit:
                circuit.name = data["name"]
                circuit.location = data["location"]
                circuit.length = data["length"]
                db.session.commit()
                return jsonify({"message": "Circuit updated successfully!"})
            return jsonify({"error": "Circuit not found"}), 404

        def delete(self, id):
            circuit = Circuit.query.get(id)
            if circuit:
                db.session.delete(circuit)
                db.session.commit()
                return jsonify({"message": "Circuit deleted successfully!"})
            return jsonify({"error": "Circuit not found"}), 404

    # Register API Routes
    api.add_resource(DriverResource, "/drivers", "/drivers/<int:id>")
    api.add_resource(CircuitResource, "/circuits", "/circuits/<int:id>")

    @app.route("/")
    def home():
        return "Welcome to the Car Race API!"

    return app

# Create `app` globally for Gunicorn
app = create_app()

if __name__ == "__main__":
    app.run(debug=True)
