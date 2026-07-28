from functools import wraps
def with_connection(method):
    @wraps(method)
    async def wrapper(self, *args, **kwargs):
        await self.db.connect()
        try:
            return await method(self, *args, **kwargs)
        finally:
            await self.db.disconnect()
    return wrapper