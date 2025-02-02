# CAR RACE AP

This is a backend API for managing car races, drivers, and circuits. It is built using Flask and provides endpoints for user authentication and CRUD operations on drivers and circuits.

## Features
- User registration and login with JWT authentication
-  CRUD operations for drivers and circuits
- CORS support

## Requirements

- Python 3.8+
- Flask
- Flask-RESTful
- Flask-SQLAlchemy
- Flask-Migrate
- Flask-Bcrypt
- Flask-JWT-Extended
- Flask-Cors
- Gunicorn

## Installation

1. Clone the repository:
`git clone git@github.com:MarionNafula/My_Car_Race_Project.git`
`cd car-race-api`

2. Create and activate a virtual environment:
`python3 -m venv venv`
`source venv/bin/activate`

3. Install the dependencies:
`pip install -r requirements.txt`

4. Set up the environment variables:
Create a .env file in the root directory and add the following:

`DATABASE_URI=your_database_uri`
`JWT_SECRET_KEY=your_secret_key`

5. Run the database migrations:
`flask db upgrade`

## Running the Application
1. Start the Flask development server:
`flask run `

2. Alternatively, you can run the application using Gunicorn:
`gunicorn -w 4 app:app`

## API Endpoints
### Authentication
- POST /register: Register a new user
- POST /login: Login and get a JWT token

### Protected Route
- GET /protected: Access a protected route (requires JWT token)

### Drivers
- GET /drivers: Get all drivers
- GET /drivers/<id>: Get a driver by ID
- POST /drivers: Add a new driver
- PUT /drivers/<id>: Update a driver by ID
- DELETE /drivers/<id>: Delete a driver by ID

### Circuits
- GET /circuits: Get all circuits
- GET /circuits/<id>: Get a circuit by ID
- POST /circuits: Add a new circuit
- PUT /circuits/<id>: Update a circuit by ID
- DELETE /circuits/<id>: Delete a circuit by ID


## License
This project is licensed under the MIT License.

