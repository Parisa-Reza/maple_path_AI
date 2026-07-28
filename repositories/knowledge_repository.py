from database.surreal import SurrealDBManager
from repositories.decorators import with_connection


class KnowledgeRepository:
    """
    Repository responsible for storing and retrieving
    IRCC knowledge.
    """

    def __init__(self):
        self.db = SurrealDBManager()

    @with_connection
    async def store_chunk(self, chunk: dict):

        client = self.db.get_client()

        return await client.create(
            "knowledge",
            chunk,
        )

    @with_connection
    async def get_chunk(self, chunk_id: str):

        client = self.db.get_client()

        return await client.select(
            f"knowledge:{chunk_id}"
        )