import logging

from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

from app.config import settings
from app.schemas.health import HealthResponse
from app.logging_config import configure_logging
from app.api.health import router as health_router
from app.api.errors import internal_server_error_handler

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

app.add_exception_handler(
    Exception,
    internal_server_error_handler,
)

app.include_router(health_router)