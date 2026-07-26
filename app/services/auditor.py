import time
import httpx


async def audit_url(url: str):

    start_time = time.time()

    async with httpx.AsyncClient() as client:

        response = await client.get(
            url,
            timeout=10
        )

    end_time = time.time()

    return {
        "url": url,
        "status_code": response.status_code,
        "response_time": round(end_time - start_time, 3),
        "content_length": len(response.content)
    }