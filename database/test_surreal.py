import pytest

from database.surreal import SurrealDBManager


@pytest.mark.asyncio
async def test_database_connection():
   

    db = SurrealDBManager()

    print("Connecting to SurrealDB...")
    await db.connect()

    print("Connection established successfully.")

    client = db.get_client()

    print("Checking client instance...")
    assert client is not None

    print("Client object exists.")

    print("Closing connection...")
    await db.disconnect()

    print("Connection closed successfully.")

    