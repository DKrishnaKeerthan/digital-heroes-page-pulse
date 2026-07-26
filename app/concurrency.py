from threading import BoundedSemaphore
from app.config import settings

semaphore = BoundedSemaphore(settings.MAX_CONCURRENT_REQUESTS)