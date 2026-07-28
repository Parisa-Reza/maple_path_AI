from schemas.application import Application
from schemas.applicant import Applicant
from schemas.trip import Trip


def test_application():

    applicant = Applicant(
        name="John Doe",
        nationality="Bangladesh",
        passport_number="AB123456",
        occupation="Engineer",
        marital_status="Single"
    )

    trip = Trip(
        purpose="Tourism",
        travel_date="2026-08-01",
        duration_days=15,
        accommodation="Hotel"
    )

    application = Application(
        applicant=applicant,
        trip=trip
    )

    print(application)

    assert application.applicant.name == "John Doe"

    print("\nApplication Test Passed")