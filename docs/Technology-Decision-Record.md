# Technology Decision Record

## Objective

Select technologies that balance simplicity, maintainability, and production readiness.

| Component | Selected | Reason |
|-----------|----------|--------|
| API Framework | FastAPI | Automatic validation, OpenAPI documentation, async support |
| Validation | Pydantic | Native FastAPI integration |
| HTTP Client | Requests | Reliable and easy to use |
| HTML Parser | BeautifulSoup | Simple HTML parsing for metadata extraction |
| Testing | Pytest | Industry-standard Python testing framework |
| Deployment | Render | Reliable deployment after Railway build issues |

---

## Alternatives Considered

### Flask

Rejected because it requires additional libraries for validation and API documentation.

### httpx

Considered for asynchronous requests. I chose `requests` because it was sufficient for the current assignment scope. For production, I would migrate to `httpx` to improve concurrency.

### Railway

I initially attempted deployment on Railway, but encountered build issues with no usable logs. To ensure timely delivery, I deployed successfully on Render. This decision prioritized reliability and meeting the assignment deadline.