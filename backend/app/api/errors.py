from fastapi import Request
from fastapi.responses import JSONResponse

async def internal_server_error_handler(
        request: Request,
        exc: Exception,
) -> JSONResponse:
    return JSONResponse(
        status_code=500,
        content={
            "error": "internal_server_error",
            "message": "An unexpected error occurred.",
        },
    )