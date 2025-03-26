from app import app, db
from models import Employee, Review, Onboarding
from datetime import datetime

# Create sample employees
employee1 = Employee(name="John Doe", hire_date=datetime(2021, 1, 15))
employee2 = Employee(name="Jane Smith", hire_date=datetime(2022, 3, 22))

# Add employees to session and commit to get their IDs
with app.app_context():
    db.session.add_all([employee1, employee2])
    db.session.commit()

    # Create sample reviews using the committed employee IDs
    review1 = Review(year=2021, summary="Excellent performance", employee=employee1)
    review2 = Review(year=2022, summary="Good performance", employee=employee1)
    review3 = Review(year=2022, summary="Outstanding performance", employee=employee2)

    # Create sample onboarding using the committed employee IDs
    onboarding1 = Onboarding(orientation=datetime(2021, 1, 20), forms_complete=True, employee=employee1)
    onboarding2 = Onboarding(orientation=datetime(2022, 3, 25), forms_complete=False, employee=employee2)

    # Add reviews and onboarding to session and commit
    db.session.add_all([review1, review2, review3, onboarding1, onboarding2])
    db.session.commit()

print("Seed data added successfully.")
