from typing import AsyncGenerator

import pytest
from blacksheep import Application
from blacksheep.testing import TestClient
from src.api import build_api


@pytest.fixture(name="app", scope="session")
def create_app() -> Application:
    app: Application = build_api()
    return app


@pytest.fixture
async def test_client(app: Application) -> AsyncGenerator[TestClient, None]:
    await app.start()
    client: TestClient = TestClient(app)
    return client
