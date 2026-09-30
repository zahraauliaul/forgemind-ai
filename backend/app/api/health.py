import logging

from fastapi import FastAPI, APIRouter, Depends

from app.config import Settings, settings
from app.dependencies import get_settings
from app.schemas.health import HealthResponse

logger = logging.getLogger(__name__)

router = APIRouter(tags=["Health"])

@router.get("/health", response_model=HealthResponse)
def health_check(
    app_settings: Settings = Depends(get_settings)
) -> HealthResponse:
    logger.info("Health check requested")

    return HealthResponse(
        status="ok",
        service=settings.app_name,
        environment=settings.environment,
    )