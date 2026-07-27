import os

from dotenv import load_dotenv
from surrealdb import AsyncSurreal


load_dotenv()


class SurrealDBManager:
    """
    Handles connection to SurrealDB.

    Responsibility:
    - Connect
    - Authenticate
    - Select namespace/database
    - Disconnect

    Nothing else.
    """

    def __init__(self):
        self.client = AsyncSurreal(os.getenv("SURREAL_URL"))

    async def connect(self):
        await self.client.signin(
            {
                "username": os.getenv("SURREAL_USERNAME"),
                "password": os.getenv("SURREAL_PASSWORD"),
            }
        )

        await self.client.use(
            os.getenv("SURREAL_NAMESPACE"),
            os.getenv("SURREAL_DATABASE"),
        )

    async def disconnect(self):
        await self.client.close()

    def get_client(self):
        return self.client