from blacksheep import JSONContent
from blacksheep.testing import TestClient


async def test_register_user(test_client: TestClient) -> None:
    response = await test_client.post(
        "/auth/login",
        content=JSONContent({
            "first_name": "Amichai",
            "last_name": "Mantinband",
            "email": "amichai@mantinband.com",
            "password": "Amiko1232!",
        }),
    )

    assert response.status == 200
