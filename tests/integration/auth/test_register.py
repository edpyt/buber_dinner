import jwt
from blacksheep import JSONContent
from blacksheep.testing import TestClient


async def test_register_user(test_client: TestClient) -> None:
    response = await test_client.post(
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
    response_data = await response.json()
    decoded_jwt = jwt.decode(
        response_data["token"],
        "test-secret",
        algorithms=["HS256"],
    )

    assert response.status == 200
    assert decoded_jwt["given_name"] == "Amichai"
    assert decoded_jwt["family_name"] == "Mantinband"
