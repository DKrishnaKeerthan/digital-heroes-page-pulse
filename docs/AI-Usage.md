# Technology Decision Record

## FastAPI

Chosen because:

- High performance
- Automatic OpenAPI generation
- Strong validation using Pydantic

Rejected:

Flask

Reason:

Requires additional libraries for validation and API documentation.

---

## Redis

Chosen because:

- Extremely fast
- Native TTL support
- Ideal for caching and rate limiting

Rejected:

In-memory Python dictionary

Reason:

Does not scale across multiple servers.

---

## Celery

Chosen because:

- Mature task queue
- Retry support
- Distributed workers

Rejected:

Threading

Reason:

Threads do not scale well for production workloads.

---

## PostgreSQL

Chosen because:

- Reliable
- ACID compliant
- Excellent indexing

Rejected:

SQLite

Reason:

Not suitable for concurrent production workloads.