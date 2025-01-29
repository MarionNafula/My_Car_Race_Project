from app import db, app
from models import Driver, Circuit, Stat

with app.app_context():
    db.create_all()

    drivers = [Driver(name="Lewis Hamilton", age=36, team="Mercedes"), Driver(name="Max Verstappen", age=25, team="Red Bull")]
    circuits = [Circuit(name="Monaco GP", location="Monaco", length=3.34), Circuit(name="Silverstone", location="UK", length=5.89)]

    db.session.add_all(drivers + circuits)
    db.session.commit()

    print("Database seeded!")