from typing import AsyncGenerator

import pytest
from blacksheep import Application
from blacksheep.testing import TestClient
from src.api import build_api
from src.infrastructure.config.jwt import JWTConfig

from tests.integration.di import setup_test_di


@pytest.fixture(scope="session")
def jwt_config() -> JWTConfig:
    return JWTConfig(jwt_secret="test-secret", expiry_minutes=0)  # noqa: S106


@pytest.fixture(name="app", scope="session")
def create_app(jwt_config: JWTConfig) -> Application:
    app: Application = build_api()
    setup_test_di(app, jwt_config)
    return app


@pytest.fixture
async def test_client(app: Application) -> AsyncGenerator[TestClient, None]:
    await app.start()
    client: TestClient = TestClient(app)
    return client
