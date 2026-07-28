import pytest

from repositories.knowledge_repository import (
    KnowledgeRepository,
)


@pytest.mark.asyncio
async def test_store_and_get_chunk():

    repository = KnowledgeRepository()

    chunk = {
        "title": "Visitor Visa",
        "content": (
            "Applicants must demonstrate that "
            "they will leave Canada before their "
            "authorized stay expires."
        ),
        "source": "IRCC",
    }

    print("\n========== STORE CHUNK ==========")

    created = await repository.store_chunk(chunk)

    print(created)

    chunk_id = created["id"].id

    print(f"\nChunk ID: {chunk_id}")

    print("\n========== GET CHUNK ==========")

    retrieved = await repository.get_chunk(chunk_id)

    print(retrieved)

    assert len(retrieved) == 1

    knowledge = retrieved[0]

    assert knowledge["title"] == "Visitor Visa"
    assert knowledge["source"] == "IRCC"

    print("\nKnowledge chunk retrieved successfully.")