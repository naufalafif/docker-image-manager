from fastapi import FastAPI
from redis import asyncio as aioredis, Redis

from app.core.settings.app import AppSettings


async def connect_to_cache(app: FastAPI, settings: AppSettings):
    """
    This function connects a FastAPI application to a Redis cache using the provided settings.

    :param app: The `app` parameter is an instance of the `FastAPI` class, which represents the
    application that is being created
    :type app: FastAPI
    :param settings: The `settings` parameter is an instance of the `AppSettings` class, which contains
    various settings for the FastAPI application, including the Redis URL. The Redis URL is used to
    connect to a Redis server, which is a popular in-memory data store used for caching and other
    purposes. The `
    :type settings: AppSettings
    """
    app.state.redis: Redis = aioredis.from_url(
        settings.redis_url, encoding="utf8", decode_responses=True
    )


async def close_cache_connection(app: FastAPI):
    """
    This is an asynchronous function that closes the connection to a Redis cache in a FastAPI
    application.

    :param app: The `app` parameter is of type `FastAPI`, which is the main application instance created
    using the `FastAPI` framework. It is used to access the application's state and configuration, as
    well as to register routes and middleware
    :type app: FastAPI
    """
    app_redis: Redis = app.state.redis
    await app_redis.close()
