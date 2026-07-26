import time

_cache = {}

def get_cache(key: str, ttl: int):
    item = _cache.get(key)
    if not item:
        return None

    created_at, value = item
    if time.time() - created_at > ttl:
        del _cache[key]
        return None

    return value

def set_cache(key: str, value, ttl: int):
    _cache[key] = (time.time(), value)