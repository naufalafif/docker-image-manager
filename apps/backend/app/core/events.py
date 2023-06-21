from typing import Callable

from fastapi import FastAPI
from loguru import logger

from app.core.settings.app import AppSettings
from app.cache.events import connect_to_cache, close_cache_connection
from app.db.events import connect_to_db, close_db_connection


def create_start_app_handler(
    app: FastAPI,
    settings: AppSettings,
) -> Callable:  # type: ignore
    """
    This function creates a handler to start a FastAPI app by connecting to a cache and a database using
    the provided settings.

    :param app: FastAPI instance representing the application
    :type app: FastAPI
    :param settings: The `settings` parameter is an instance of the `AppSettings` class, which contains
    various settings and configurations for the FastAPI application. These settings can include things
    like database connection information, cache settings, and other application-specific configurations.
    The `create_start_app_handler` function uses these settings to connect
    :type settings: AppSettings
    :return: The function `create_start_app_handler` returns a callable function `start_app` that takes
    no arguments and returns `None`.
    """

    async def start_app() -> None:
        await connect_to_cache(app, settings)
        await connect_to_db(app, settings)

    return start_app


def create_stop_app_handler(app: FastAPI) -> Callable:  # type: ignore
    """
    This function creates a handler to stop a FastAPI application by closing database, cache, and labs
    connections.

    :param app: FastAPI instance representing the application
    :type app: FastAPI
    :return: The function `create_stop_app_handler` returns a coroutine function `stop_app` that takes
    no arguments and closes the database connection, cache connection, and labs.
    """

    @logger.catch
    async def stop_app() -> None:
        await close_db_connection(app)
        await close_cache_connection(app)

    return stop_app
