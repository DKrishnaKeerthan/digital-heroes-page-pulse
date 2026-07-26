from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    REQUEST_TIMEOUT: int = 10
    CACHE_TTL: int = 300
    MAX_CONCURRENT_REQUESTS: int = 10
    RATE_LIMIT: int = 2

    class Config:
        env_file = ".env"


settings = Settings()