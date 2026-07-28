from schemas.document import Document


def test_document_schema():

    print("\nCreating Documents...")

    documents = Document(
        passport_file="passport.pdf",
        bank_statement="bank.pdf",
        employment_letter="employment.pdf",
        itinerary="itinerary.pdf",
    )

    print(documents)

    assert documents.passport_file == "passport.pdf"

    print("\nDocument Schema Test Passed.")