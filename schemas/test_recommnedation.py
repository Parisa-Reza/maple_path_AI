from schemas.recommendation import Recommendation


def test_recommendation_schema():

    print("\nCreating Recommendation...")

    recommendation = Recommendation(
        decision="Approve",
        reason="Applicant satisfies visitor visa requirements.",
        reviewer="AI",
    )

    print(recommendation)

    assert recommendation.decision == "Approve"

    print("\nRecommendation Schema Test Passed.")