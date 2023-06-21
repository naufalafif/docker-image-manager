import logging

from pydantic import SecretStr

from app.core.settings.app import AppSettings


class TestAppSettings(AppSettings):
    debug: bool = True

    title: str = "Test FastAPI example application"

    logging_level: int = logging.DEBUG

    supabase_url: str = "https://test"
    supabase_apikey: str = "https://test"
