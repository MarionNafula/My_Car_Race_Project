from app import app
from models import db, Circuit, Driver

with app.app_context():
    print("Creating tables...")
    db.drop_all()  # Drop all tables
    db.create_all()  # Ensure tables are created

    # Seeding data
    print("Seeding circuits...")
    circuit1 = Circuit(name="Monaco GP", location="Monaco", length=3.34)
    circuit2 = Circuit(name="Silverstone GP", location="UK", length=5.89)

    print("🚀 Seeding drivers...")
    driver1 = Driver(name="Lewis Hamilton", team="Mercedes", age=38)
    driver2 = Driver(name="Max Verstappen", team="Red Bull", age=26)

    # Add all to the session
    db.session.add_all([circuit1, circuit2, driver1, driver2])


    # Commit changes to database
    db.session.commit()
    print("✅ Seeding complete!")
