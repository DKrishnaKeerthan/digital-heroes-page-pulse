from fastapi import APIRouter

from app.models.schemas import AuditRequest, AuditResponse
from app.services.auditor import audit_url


router = APIRouter()


@router.post("/audit", response_model=AuditResponse)
async def create_audit(request: AuditRequest):

    result = await audit_url(
        str(request.url)
    )

    return result