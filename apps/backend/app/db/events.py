from fastapi import FastAPI
from loguru import logger
from .client import SupabaseDB

from app.core.settings.app import AppSettings


async def connect_to_db(app: FastAPI, settings: AppSettings) -> None:
    """
    This function connects a FastAPI application to a PostgreSQL database using SupabaseDB.

    :param app: The `app` parameter is an instance of the `FastAPI` class, which represents the
    application being built
    :type app: FastAPI
    :param settings: The `settings` parameter is an instance of the `AppSettings` class, which contains
    various settings and configurations for the application. It is likely used to provide the necessary
    credentials and connection information for connecting to a PostgreSQL database
    :type settings: AppSettings
    """

    logger.info("Connecting to PostgreSQL")
    app.state.db = SupabaseDB.supabase
    logger.info("Connection established")


async def close_db_connection(app: FastAPI) -> None:
    """
    This function closes the connection to a database (specifically Supabase) and logs the action.

    :param app: FastAPI instance representing the application
    :type app: FastAPI
    """
    logger.info("Closing connection to database")
    # no closing needed for supabase

    logger.info("Connection closed")
