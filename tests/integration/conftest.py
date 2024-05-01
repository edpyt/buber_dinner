from typing import AsyncGenerator

import pytest
from blacksheep import Application
from src.api.main import build_api
from src.infrastructure.config.jwt import JWTConfig

from tests.integration.di import DIOverride, setup_test_di


@pytest.fixture(name="jwt_config", scope="session")
def create_jwt_config() -> JWTConfig:
    return JWTConfig(jwt_secret="test-secret", expiry_minutes=9999)


@pytest.fixture(name="app", scope="session")
async def create_app(jwt_config: JWTConfig) -> AsyncGenerator[Application, None]:
    app: Application = build_api()

    setup_test_di(app, DIOverride(jwt_config))

    await app.start()
    yield app
    await app.stop()
