
from schemas.interview import Interview


def test_interview_schema():

    print("\nCreating Interview...")

    interview = Interview(
        questions=[
            "Why do you want to visit Canada?"
        ],
        answers=[
            "For tourism."
        ],
        summary="Applicant answered confidently.",
    )

    print(interview)

    assert len(interview.questions) == 1
    assert interview.answers[0] == "For tourism."

    print("\nInterview Schema Test Passed.")