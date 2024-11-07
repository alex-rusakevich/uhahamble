import pickle
from functools import wraps
from typing import Callable, Optional

from uhahamble.bot.config import REDIS_PREFIX, redis


def cached(function: Optional[Callable] = None, ttl_sec: int = 500):
    assert callable(function) or function is None

    def _decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            # Generate the cache key from the function's arguments.
            key_parts = [func.__name__] + list(args)
            key = REDIS_PREFIX + ":" + ("-".join(key_parts))
            result = redis.get(key)

            if result is None:
                # Run the function and cache the result for next time.
                value = func(*args, **kwargs)
                value_pickled = pickle.dumps(value)
                redis.set(key, value_pickled)
            else:
                # Skip the function entirely and use the cached value instead.
                value = pickle.loads(result)

            return value

        return wrapper

    return _decorator(function) if callable(function) else _decorator
