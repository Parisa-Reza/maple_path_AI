import pytest

from repositories.application_repository import (
    ApplicationRepository,
)


@pytest.mark.asyncio
async def test_application_repository():

    repository = ApplicationRepository()

    application = {
        "applicant_name": "John Doe",
        "passport_number": "AB123456",
        "nationality": "Bangladesh",
        "purpose_of_visit": "Tourism",
        "status": "Draft",
    }

    print("\n========== CREATE ==========")

    created = await repository.create_application(application)

    print(created)

    application_id = created["id"].id

    print(f"\nApplication ID: {application_id}")

    print("\n========== READ ==========")

    retrieved = await repository.get_application(application_id)

    application = retrieved[0]

    print(application)

    assert application["applicant_name"] == "John Doe"

    print("\n========== UPDATE ==========")

    updated = await repository.update_application(
        application_id,
        {
            "status": "Approved"
        },
    )

    print(updated)

    retrieved = await repository.get_application(application_id)

    application = retrieved[0]

    assert application["status"] == "Approved"

    print("Application updated successfully.")

    print("\n========== DELETE ==========")

    await repository.delete_application(application_id)

    retrieved = await repository.get_application(application_id)

    print(retrieved)

    assert retrieved == []

    print("Application deleted successfully.")