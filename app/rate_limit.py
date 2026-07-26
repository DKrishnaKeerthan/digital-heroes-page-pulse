# app/rate_limit.py
import time
from collections import defaultdict, deque
from threading import Lock

_requests = defaultdict(deque)
_lock = Lock()

def allow_request(client_id: str, limit: int, window_seconds: int = 60) -> bool:
    now = time.time()
    with _lock:
        timestamps = _requests[client_id]

        while timestamps and now - timestamps[0] > window_seconds:
            timestamps.popleft()

        if len(timestamps) >= limit:
            return False

        timestamps.append(now)
        return True