from app import create_app, db
from models import Circuit, Driver

app = create_app()

with app.app_context():
    print("Dropping all tables...")
    db.drop_all()
    db.create_all()

    # Seed data
    print("Seeding circuits...")
    circuit1 = Circuit(name="Monaco GP", location="Monaco", length=3.34)
    circuit2 = Circuit(name="Silverstone GP", location="UK", length=5.89)

    print("Seeding drivers...")
    driver1 = Driver(name="Lewis Hamilton", team="Mercedes", age=38)
    driver2 = Driver(name="Max Verstappen", team="Red Bull", age=26)

    # Commit to database
    db.session.add_all([circuit1, circuit2, driver1, driver2])
    db.session.commit()

    print("✅ Seeding complete!")
