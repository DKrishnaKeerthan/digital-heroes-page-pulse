from fastapi.responses import HTMLResponse
from app.logger import logger
from app.concurrency import semaphore
from fastapi import FastAPI, HTTPException, Request
from app.rate_limit import allow_request
from app.cache import get_cache, set_cache
from app.config import settings
from bs4 import BeautifulSoup
from pydantic import BaseModel, AnyHttpUrl
from app.seo import analyze_seo
from app.performance import performance_rating
from app.security import analyze_security
import requests
import time
import uuid
app = FastAPI(
    title="Page Pulse API",
    description="Website auditing API built for the Digital Heroes Training Task.",
    version="1.0.0",
)

logger.info("=== Page Pulse application started ===")
logger.info("Logger is working")
@app.get("/", response_class=HTMLResponse)
def root():
    return """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <title>Page Pulse API</title>
        <style>
            body{
                font-family:Arial, sans-serif;
                max-width:800px;
                margin:50px auto;
                padding:20px;
                background:#f7f7f7;
                color:#333;
            }
            h1{
                color:#2563eb;
            }
            .card{
                background:white;
                padding:25px;
                border-radius:10px;
                box-shadow:0 2px 8px rgba(0,0,0,.08);
            }
            footer{
                margin-top:40px;
                font-size:14px;
                color:#666;
            }
            a{
                color:#2563eb;
                text-decoration:none;
            }
        </style>
    </head>

    <body>

    <div class="card">

        <h1>Page Pulse API</h1>

        <p><strong>Status:</strong> ✅ Running</p>

        <h3>Available Endpoints</h3>

        <ul>
            <li><a href="/docs">Swagger Documentation</a></li>
            <li><strong>POST</strong> /audit</li>
        </ul>

        <p>
        Page Pulse is a FastAPI-based website auditing service that analyzes
        webpage metadata, performance, SEO, and basic security information.
        </p>

        <footer>
            Built for
            <a href="https://digitalheroesco.com" target="_blank">
                Digital Heroes Training Task
            </a>
        </footer>

    </div>

    </body>
    </html>
    """

class URLRequest(BaseModel):
    url: AnyHttpUrl


@app.post("/audit")
def audit_url(payload: URLRequest, request: Request):
    logger.info("audit endpoint reached")
    logger.info("Entered audit_url()")

    request_id = str(uuid.uuid4())

    logger.info(f"Request {request_id} | URL={payload.url}")

    client_ip = request.client.host if request.client else "unknown"
    

    allowed = allow_request(client_ip, settings.RATE_LIMIT)

    

    if not allowed:
        raise HTTPException(
            status_code=429,
            detail={
                "error": "RATE_LIMIT_EXCEEDED",
                "message": "Too many requests. Please try again later.",
                "request_id": request_id
            }
        )
    cached = get_cache(str(payload.url), settings.CACHE_TTL)
    if cached:
        cached["cached"] = True
        return cached
    if not semaphore.acquire(blocking=False):
        raise HTTPException(
            status_code=503,
            detail={
                "error": "SERVER_BUSY",
                "message": "Too many concurrent requests",
                "request_id": request_id
            }
        )

    try:
        start_time = time.time()
        time.sleep(5)
        response = requests.get(
            str(payload.url),
            timeout=5,
            allow_redirects=True
        )

        load_time = round(time.time() - start_time, 3)

        soup = BeautifulSoup(response.text, "html.parser")

        # Page title
        title = None
        if soup.title and soup.title.string:
            title = soup.title.string.strip()

        # Basic metrics
        total_links = len(soup.find_all("a"))
        total_images = len(soup.find_all("img"))
        page_size_kb = round(len(response.content) / 1024, 2)

         # Call helper modules
        seo_data = analyze_seo(soup)
        performance_data = performance_rating(load_time)
        security_data = analyze_security(response)

        result = {
            "request_id": request_id,
            "url": str(payload.url),
            "status_code": response.status_code,
            "load_time": load_time,
            "title": title,
            "total_links": total_links,
            "total_images": total_images,
            "page_size_kb": page_size_kb,
            "seo": seo_data,
            "performance": performance_data,
            "security": security_data,
            "cached": False
        }

        set_cache(str(payload.url), result.copy(), settings.CACHE_TTL)
        logger.info(
            f"Completed {request_id} | "
            f"Status={response.status_code} | "
            f"Load={load_time}s"
        )
        return result

    except requests.exceptions.Timeout:
        logger.error(f"{request_id} Timeout")
        
        raise HTTPException(
            
            status_code=408,
            detail={
                "error": "REQUEST_TIMEOUT",
                "message": "Website took too long to respond",
                "request_id": request_id
            }
        
        )

    except requests.exceptions.RequestException:
        logger.error(f"{request_id} Invalid URL")

        raise HTTPException(
            status_code=400,
            detail={
                "error": "INVALID_URL",
                "message": "Unable to reach the provided URL",
                "request_id": request_id
            }
        )

    except Exception as e:
        logger.exception(f"{request_id} Internal Error")

        raise HTTPException(
            status_code=500,
            detail={
                "error": "INTERNAL_SERVER_ERROR",
                "message": str(e),
                "request_id": request_id
            }
        )
    finally:
        semaphore.release()