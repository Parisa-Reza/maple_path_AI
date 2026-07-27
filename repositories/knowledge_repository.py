from database.surreal import SurrealDBManager


class KnowledgeRepository:
    """
    Repository responsible for storing and retrieving
    IRCC knowledge.
    """

    def __init__(self):
        self.db = SurrealDBManager()

    async def store_chunk(self, chunk: dict):

        await self.db.connect()

        client = self.db.get_client()

        result = await client.create(
            "knowledge",
            chunk,
        )

        await self.db.disconnect()

        return result

    async def get_chunk(self, chunk_id: str):

        await self.db.connect()

        client = self.db.get_client()

        result = await client.select(
            f"knowledge:{chunk_id}"
        )

        await self.db.disconnect()

        return result