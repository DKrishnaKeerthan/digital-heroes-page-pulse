# Digital Heroes - Page Pulse

## Overview
Production-grade URL audit service built with FastAPI.

## Features
- URL validation
- Configurable caching
- Rate limiting
- Structured logging
- Request IDs
- Concurrency limits
- Request timeouts
- Structured error responses

## Installation

git clone ...

pip install -r requirements.txt

## Run

uvicorn app.main:app --reload

## API

GET /

Returns service status.

POST /audit

Request

{
  "url": "https://example.com"
}

Response

{
  ...
}

## Tests

pytest

## Environment Variables

CACHE_TTL=300

RATE_LIMIT=...

## CI

GitHub Actions automatically runs tests.

## Live Demo

(Add Render URL after deployment)

Built for Digital Heroes Training Task