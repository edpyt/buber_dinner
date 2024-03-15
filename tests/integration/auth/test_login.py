from typing import Callable, Coroutine

from blacksheep import JSONContent
from blacksheep.testing import TestClient
from src.domain.entities.user import User


async def test_login_user(
    test_client: TestClient,
    create_user_factory: Callable[[str, str, str, str], Coroutine[User, None, None]],
) -> None:
    await create_user_factory("test", "test", "amichai1@mantinband.com", "Amiko1232!")

    response = await test_client.post(
        "/auth/login",
        content=JSONContent(
            {
                "email": "amichai1@mantinband.com",
                "password": "Amiko1232!",
            },
        ),
    )

    assert response.status == 200
