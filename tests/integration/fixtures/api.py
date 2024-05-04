import pytest
from blacksheep import Application, JSONContent
from blacksheep.testing import TestClient
from src.application.persistence.menu_repo import MenuRepository
from src.application.persistence.user_repo import UserRepository
from src.infrastructure.config.jwt import JWTConfig

from tests.integration.di import DIOverride, setup_test_di


@pytest.fixture
def di_overrides(
    jwt_config: JWTConfig, user_repo: UserRepository, menu_repo: MenuRepository,
) -> list[DIOverride]:
    return [
        DIOverride(jwt_config),
        DIOverride(user_repo, UserRepository),
        DIOverride(menu_repo, MenuRepository),
    ]


@pytest.fixture
def test_client(app: Application, di_overrides: list[DIOverride]) -> TestClient:
    setup_test_di(app, *di_overrides)
    return TestClient(app)


@pytest.fixture(name="token")
async def create_auth_token(test_client: TestClient) -> str:
    auth_response = await test_client.post(
        "/auth/register",
        content=JSONContent(
            {
                "first_name": "Amichai",
                "last_name": "Mantinband",
                "email": "amichai@mantinband.com",
                "password": "Amiko1232!",
            },
        ),
    )
    auth_response_data = await auth_response.json()
    return auth_response_data["token"]
