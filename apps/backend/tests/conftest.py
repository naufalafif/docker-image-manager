from os import environ
import pytest
import pytest_asyncio
from asgi_lifespan import LifespanManager
from fastapi import FastAPI
from httpx import AsyncClient

environ["APP_ENV"] = "test"


pytest.register_assert_rewrite("pytest_asyncio.plugin")


@pytest.fixture
def app() -> FastAPI:
    from app.main import get_application  # local import for testing purpose

    return get_application()


@pytest_asyncio.fixture
async def initialized_app(app: FastAPI) -> FastAPI:
    async with LifespanManager(app):
        # app.state.pool = await FakeAsyncPGPool.create_pool(app.state.pool)
        yield app


@pytest_asyncio.fixture
async def client(initialized_app: FastAPI) -> AsyncClient:
    async with AsyncClient(
        app=initialized_app,
        base_url="http://testserver",
        headers={"Content-Type": "application/json"},
    ) as client:
        yield client


@pytest.fixture
def authorized_client(
    client: AsyncClient, token: str, authorization_prefix: str
) -> AsyncClient:
    client.headers = {
        "Authorization": f"{authorization_prefix} {token}",
        **client.headers,
    }
    return client
