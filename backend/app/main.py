"""
Adaptive AI Workbench
Main application entry point.
"""

from fastapi import FastAPI

from app.api.router import api_router
from app.core.settings import settings
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

from app.core.exceptions import (AuthenticationError, EmailAlreadyExistsError)

from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi

app = FastAPI(
    title=settings.PROJECT_NAME,
    description="Cloud-native adaptive multi-agent AI platform",
    version=settings.VERSION,
)

def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema

    openapi_schema = get_openapi(
        title=app.title,
        version=app.version,
        description=app.description,
        routes=app.routes,
    )

    openapi_schema["components"]["securitySchemes"] = {
        "BearerAuth": {
            "type": "http",
            "scheme": "bearer",
            "bearerFormat": "JWT",
        }
    }

    app.openapi_schema = openapi_schema
    return app.openapi_schema


app.openapi = custom_openapi

app.include_router(api_router)

@app.exception_handler(EmailAlreadyExistsError)
async def email_exists_handler(
    request: Request,
    exc: EmailAlreadyExistsError,
):
    return JSONResponse(
        status_code=400,
        content={
            "detail": str(exc),
        },
    )


@app.exception_handler(AuthenticationError)
async def authentication_handler(
    request: Request,
    exc: AuthenticationError,
):
    return JSONResponse(
        status_code=401,
        content={
            "detail": str(exc),
        },
    )

@app.get(
    "/",
    tags=["System"]
)
def root():
    return {
        "project": settings.PROJECT_NAME,
        "status": "Running",
        "version": settings.VERSION,
    }