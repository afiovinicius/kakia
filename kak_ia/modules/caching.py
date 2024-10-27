import redis.asyncio as aioredis

from kak_ia.core.config import settings


class Caching:
    def __init__(self):
        self.redis_client = aioredis.from_url(settings.REDIS_URL)

    async def get(self, key: str) -> str | None:
        try:
            value = await self.redis_client.get(key)
            return value.decode() if value else None
        except aioredis.RedisError as e:
            print(f"Erro ao obter chave {key}: {e}")
            return None

    async def set(self, key: str, value: str):
        try:
            result = await self.redis_client.set(key, value)
            return result
        except aioredis.RedisError as e:
            print(f"Erro ao definir chave {key}: {e}")
            return False
