from database.surreal import SurrealDBManager


class ApplicationRepository:
    """
    Repository responsible for CRUD operations
    on the application table.
    """

    def __init__(self):
        self.db = SurrealDBManager()

    async def create_application(self, application: dict):

        await self.db.connect()

        client = self.db.get_client()

        result = await client.create(
            "application",
            application,
        )

        await self.db.disconnect()

        return result

    async def get_application(self, application_id: str):

        await self.db.connect()

        client = self.db.get_client()

        result = await client.select(
            f"application:{application_id}"
        )

        await self.db.disconnect()

        return result

    async def update_application(self, application_id: str, data: dict):

        await self.db.connect()

        client = self.db.get_client()

        result = await client.merge(
            f"application:{application_id}",
            data,
        )

        await self.db.disconnect()

        return result


    async def delete_application(self, application_id: str):

        await self.db.connect()

        client = self.db.get_client()

        result = await client.delete(
            f"application:{application_id}"
        )

        await self.db.disconnect()

        return result