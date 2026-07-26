from fastapi import HTTPException


def invalid_url_error():

    raise HTTPException(
        status_code=400,
        detail={
            "code": "INVALID_URL",
            "message": "Please provide a valid HTTP/HTTPS URL"
        }
    )