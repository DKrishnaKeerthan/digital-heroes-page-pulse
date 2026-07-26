# Digital Heroes – Page Pulse

A production-ready URL auditing service built with FastAPI for the Digital Heroes Software Development qualification task.

## Features

- URL validation
- Structured error responses
- Configurable caching
- Rate limiting per client
- Request timeouts
- Concurrency limits
- Structured logging with request IDs
- Automated test suite
- GitHub Actions CI

---

## Tech Stack

- Python 3.11
- FastAPI
- Pydantic
- Requests
- BeautifulSoup
- Pytest
- GitHub Actions

---

## Installation

Clone the repository:

```bash
git clone https://github.com/DKrishnaKeerthan/digital-heroes-page-pulse.git
cd digital-heroes-page-pulse
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate it (Windows):

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Run the API

```bash
uvicorn app.main:app --reload
```

The API runs at:

```
http://127.0.0.1:8000
```

---

# API Contract

## Health Check

### GET /

Returns the service status.

Example response:

```json
{
  "status": "running"
}
```

---

## URL Audit

### POST /audit

Request:

```json
{
  "url": "https://example.com"
}
```

Example Response:

```json
{
  "title": "...",
  "description": "...",
  "seo_score": 82
}
```

If the URL is invalid:

```json
{
  "error": "Invalid URL"
}
```

---

# Testing

Run all tests:

```bash
pytest
```

Current status:

- 5 tests passing

---

# Continuous Integration

GitHub Actions automatically:

- Installs dependencies
- Runs the test suite
- Validates every push to the main branch

---

# Environment Variables

Create a `.env` file.

Example:

```
CACHE_TTL=300
```

---

# Project Structure

```
app/
    routes/
    services/
    models/
    core/

tests/

docs/

.github/
```

---

# Deployment

Deployment URL:

_To be added after Render deployment._

---

# AI Usage

AI tools (ChatGPT) were used to:

- understand FastAPI best practices
- improve project structure
- review architecture
- help create tests
- improve documentation

All implementation decisions, debugging, testing, and final code review were completed manually.

---

Built for Digital Heroes Training Task.