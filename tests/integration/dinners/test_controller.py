from blacksheep.testing import TestClient


async def test_get_dinners_wout_auth(test_client: TestClient) -> None:
    response = await test_client.get("/dinners")

    assert response.status == 401
