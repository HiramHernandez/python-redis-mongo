from redis_om import get_redis_connection
from .config import settings

__all__ = ('redis',)

redis = get_redis_connection(
    host=settings.redis_host,
    port=settings.redis_port,
    decode_responses=True
)
