import logging

from fastapi import FastAPI

from app.config import settings
from app.logging_config import configure_logging
from app.schemas.health import HealthResponse

configure_logging()

logger = logging.getLogger(__name__)

app = FastAPI(
    title=settings.app_name,
    description=(
        "Manufacturing Knowledge & Operations"
        "Intelligence Assistant"
    ),
    version="0.1.0",
)

@app.get("/health", response_model=HealthResponse)
def health_check():
    return HealthResponse(
        status="ok",
        service=settings.app_name,
        environment=settings.environment,
    )