from schemas.application import Application


def test_application_schema():

    application = Application(
        applicant_name="John Doe",
        passport_number="AB123456",
        nationality="Bangladesh",
        purpose_of_visit="Tourism",
    )

    assert application.applicant_name == "John Doe"
    assert application.status == "draft"

    print("\nApplication Schema Test Passed")