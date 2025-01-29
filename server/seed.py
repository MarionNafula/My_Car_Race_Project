from app import app
from models import db, Circuit

with app.app_context():
    print("Creating tables...")
    db.create_all()  # Ensure tables are created

    # Seeding data
    print("Seeding circuits...")
    monaco = Circuit(name="Monaco GP", location="Monaco", length=3.34)

    db.session.add(monaco)
    db.session.commit()
    print("Seeding complete!")
