from schemas.assessment import Assessment


def test_assessment_schema():

    print("\nCreating Assessment...")

    assessment = Assessment(
        eligibility="Eligible",
        confidence=0.94,
        reasoning="Financial documents satisfy IRCC requirements.",
    )

    print(assessment)

    assert assessment.eligibility == "Eligible"
    assert assessment.confidence == 0.94

    print("\nAssessment Schema Test Passed.")