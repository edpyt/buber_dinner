from blacksheep import JSONContent
from blacksheep.testing import TestClient


async def test_login_user(test_client: TestClient) -> None:
    response = await test_client.post(
        "/auth/login",
        content=JSONContent({
            "email": "amichai@mantinband.com",
            "password": "Amiko1232!",
        }),
    )

    assert response.status == 200
