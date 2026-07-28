from schemas.applicant import Applicant


def test_applicant_schema():

    print("\nCreating Applicant...")

    applicant = Applicant(
        name="John Doe",
        nationality="Bangladesh",
        passport_number="AB123456",
        occupation="Software Engineer",
        marital_status="Single",
    )

    print(applicant)

    assert applicant.name == "John Doe"
    assert applicant.passport_number == "AB123456"

    print("\nApplicant Schema Test Passed.")