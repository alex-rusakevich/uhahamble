import pickle
from functools import wraps
from logging import getLogger
from typing import Callable, Optional

from uhahamble.bot.config import NO_CACHE, REDIS_PREFIX, redis

logger = getLogger(__name__)


def cached(function: Optional[Callable] = None, ttl_sec: int = 500):
    assert callable(function) or function is None

    def _decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            # Generate the cache key from the function's arguments.
            key_parts = [func.__name__] + list(args)
            key = REDIS_PREFIX + ":" + ("-".join(key_parts))
            result = redis.get(key)

            if NO_CACHE or result is None:
                # Run the function and cache the result for next time.
                logger.debug(f"Cache miss for '{key}', cache disabled: {NO_CACHE}")

                value = func(*args, **kwargs)
                value_pickled = pickle.dumps(value)
                redis.set(key, value_pickled)
            else:
                # Skip the function entirely and use the cached value instead.
                logger.debug(f"Cache hit for '{key}'")

                value = pickle.loads(result)

            return value

        return wrapper

    return _decorator(function) if callable(function) else _decorator
