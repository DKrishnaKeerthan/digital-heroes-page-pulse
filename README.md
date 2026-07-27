# Page Pulse API

Production-ready URL auditing API built with **FastAPI** for the **Digital Heroes Software Development (SDE) Training Task**.

**Live API:** https://digital-heroes-page-pulse-t4sg.onrender.com


**Swagger Documentation:** https://digital-heroes-page-pulse-t4sg.onrender.com/docs

---

## Features

- URL validation using Pydantic
- Configurable request timeout
- In-memory caching with configurable TTL
- Per-client rate limiting
- Concurrency limiting using semaphore
- Structured logging with unique request IDs
- Structured error responses
- SEO analysis
- Performance analysis
- Security header analysis
- FastAPI Swagger documentation
- Automated testing with pytest
- GitHub Actions Continuous Integration
- Live deployment on Render

---

# Project Structure

```
app/
│
├── main.py
├── cache.py
├── concurrency.py
├── config.py
├── logger.py
├── performance.py
├── rate_limit.py
├── security.py
└── seo.py

tests/
docs/
.github/workflows/
README.md
requirements.txt
```

---

# Installation

```bash
git clone https://github.com/DKrishnaKeerthan/digital-heroes-page-pulse

cd digital-heroes-page-pulse

python -m venv venv
```

Windows

```bash
venv\Scripts\activate
```

Linux / macOS

```bash
source venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the application

```bash
uvicorn app.main:app --reload
```

Open

```
http://127.0.0.1:8000/docs
```

---

# Configuration

Create a `.env` file.

Example

```
CACHE_TTL=300
RATE_LIMIT=2
MAX_CONCURRENT_REQUESTS=2
```

---

# API Endpoints

## GET /

Returns API status.

Example

```json
{
  "status":"running"
}
```

---

## POST /audit

Request

```json
{
  "url":"https://github.com"
}
```

Example Response

```json
{
  "request_id":"9b6d...",
  "url":"https://github.com",
  "status_code":200,
  "load_time":0.84,
  "title":"GitHub",
  "total_links":123,
  "total_images":21,
  "page_size_kb":512.33,
  "seo":{},
  "performance":{},
  "security":{},
  "cached":false
}
```

---

# Error Responses

The API returns structured JSON errors with a request ID for easier debugging.

| HTTP Status | Error | Description |
|-------------|-------|-------------|
|400|INVALID_URL|Unable to reach the provided URL|
|408|REQUEST_TIMEOUT|Website took too long to respond|
|429|RATE_LIMIT_EXCEEDED|Too many requests from the same client|
|500|INTERNAL_SERVER_ERROR|Unexpected server error|
|503|SERVER_BUSY|Maximum concurrent requests exceeded|

Example

```json
{
    "error":"RATE_LIMIT_EXCEEDED",
    "message":"Too many requests. Please try again later.",
    "request_id":"xxxxxxxx"
}
```

---
## Concurrency Control

The API uses a semaphore to limit the number of requests processed simultaneously.

If the maximum number of concurrent requests has already been reached, the API immediately returns:

HTTP Status: **503 Service Unavailable**

Example response:

```json
{
  "detail": {
    "error": "SERVER_BUSY",
    "message": "Too many concurrent requests",
    "request_id": "<uuid>"
  }
}
```

This protects the service from overload during traffic spikes.
# Caching

The application uses an in-memory cache to avoid repeatedly fetching the same webpage.

- First request fetches data from the target website.
- The response is cached for `CACHE_TTL` seconds.
- Subsequent requests for the same URL within the TTL are served directly from cache.

Example

First request

```json
"cached": false
```

Second request

```json
"cached": true
```

---

# Concurrency Control

The API limits the number of simultaneous audit requests using a semaphore.

If the maximum concurrent request limit is reached, the API immediately returns:

```
503 SERVER_BUSY
```

This prevents excessive resource consumption under heavy load.

---
### Testing Concurrency Limits

Swagger UI sends requests sequentially and cannot be used to test concurrency.

To test manually:

1. Start the server:

```bash
uvicorn app.main:app --reload --port 8001
```

2. Open multiple PowerShell windows.

3. Run the following command simultaneously in each window:

```powershell
Invoke-RestMethod `
-Method POST `
-Uri http://127.0.0.1:8001/audit `
-ContentType "application/json" `
-Body '{"url":"https://example.com"}'
```

If the configured semaphore limit is exceeded, additional requests receive:

```
503 SERVER_BUSY
```

If you receive:

```
Unable to connect to the remote server
```

ensure the FastAPI server is running and use the correct port (`8001` if started with `--port 8001`).
# Logging

Every request receives a unique request ID.

Logs include

- Incoming request
- URL being audited
- Completion status
- Response time
- Errors (if any)

Example

```
INFO Request 85e7902f...
INFO Completed 85e7902f...
```

---

# Running Tests

```bash
pytest
```

---

# Continuous Integration

GitHub Actions automatically runs the test suite on every push and pull request.

Workflow location

```
.github/workflows/ci.yml
```

---

# Documentation

Additional design documents are available in the `docs/` directory.

- Architecture
- Technology Decision Record
- Failure Mode Analysis
- Observability & Rollback Plan

---

# Deployment

The application is deployed on Render.

Live URL

```
https://digital-heroes-page-pulse-t4sg.onrender.com

```

Swagger

```
https://digital-heroes-page-pulse-t4sg.onrender.com/docs```

---

# Troubleshooting

## Port 8000 unavailable

If running

```bash
uvicorn app.main:app --reload
```

returns a socket permission error such as:

```
WinError 10013
```

start the server on another port:

```bash
uvicorn app.main:app --reload --port 8001
```

and open:

```
http://127.0.0.1:8001/docs
```

---

## Logging does not appear

Ensure the application is started with:

```bash
uvicorn app.main:app --reload --log-level info
```

If logs still do not appear, verify that:

- `from app.logger import logger` is imported in `main.py`
- Logging statements use `logger.info()`, `logger.error()`, or `logger.exception()`
- The application starts successfully before sending requests

---

## Cache always returns false

The first request is always fetched from the target website.

Repeat the **same URL** within the configured `CACHE_TTL` to receive:

```json
"cached": true
```

---

# AI Usage

ChatGPT was used to review FastAPI best practices, validate implementation ideas, improve documentation, and assist with troubleshooting during development.

All architectural decisions, debugging, feature implementation, testing, deployment, and final code were reviewed, modified, and verified manually before submission.

---

## Built for Digital Heroes Training Task