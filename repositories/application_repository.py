
from repositories.decorators import with_connection
from database.surreal import SurrealDBManager



class ApplicationRepository:
    def __init__(self):
        self.db = SurrealDBManager()

    @with_connection
    async def create_application(self, application: dict):
        client = self.db.get_client()
        return await client.create("application", application)

    @with_connection
    async def get_application(self, application_id: str):
        client = self.db.get_client()
        return await client.select(f"application:{application_id}")

    @with_connection
    async def update_application(self, application_id: str, data: dict):
        client = self.db.get_client()
        return await client.merge(f"application:{application_id}", data)

    @with_connection
    async def delete_application(self, application_id: str):
        client = self.db.get_client()
        return await client.delete(f"application:{application_id}")