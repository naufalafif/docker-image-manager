from starlette.middleware.cors import CORSMiddleware
from starlette.exceptions import HTTPException
from fastapi.exceptions import RequestValidationError
from fastapi import FastAPI
import os
from dotenv import load_dotenv

load_dotenv("/root/.env")

from app.core.events import create_start_app_handler, create_stop_app_handler
from app.core.config import get_app_settings
from app.api.routes.api import router as api_router
from app.api.errors.validation_error import http422_error_handler
from app.api.errors.http_error import http_error_handler


env = os.environ.get("APP_ENV")


def get_application() -> FastAPI:
    settings = get_app_settings()
    settings.configure_logging()

    application = FastAPI(**settings.fastapi_kwargs)

    application.add_middleware(
        CORSMiddleware,
        allow_origins=settings.allowed_hosts,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    application.add_event_handler(
        "startup",
        create_start_app_handler(application, settings),
    )
    application.add_event_handler(
        "shutdown",
        create_stop_app_handler(application),
    )

    application.add_exception_handler(HTTPException, http_error_handler)
    application.add_exception_handler(RequestValidationError, http422_error_handler)

    application.include_router(api_router, prefix=settings.api_prefix)

    return application


app = get_application()
