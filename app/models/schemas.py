from pydantic import BaseModel, HttpUrl


class AuditRequest(BaseModel):
    url: HttpUrl


class AuditResponse(BaseModel):
    url: str
    status_code: int
    response_time: float
    content_length: int | None