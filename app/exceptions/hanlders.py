from app.exceptions.tech_exceptions import DuplicateTechSlugException
from fastapi.responses import JSONResponse
from fastapi import Request, status

async def duplicate_tech_slug_handler(request: Request, exception: DuplicateTechSlugException):
    return JSONResponse(
        status_code = status.HTTP_409_CONFLICT,
        content = {
            "detail": exception.message
        }
    )