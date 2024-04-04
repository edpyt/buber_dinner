from blacksheep import JSONContent
from blacksheep.testing import TestClient


async def test_create_menu(test_client: TestClient, token: str) -> None:
    response = await test_client.post(
        "/hosts/ef74363c-9eac-4631-8bb1-7fbdb6c4054e/menus",
        headers={"Authorization": f"Bearer {token}"},
        content=JSONContent(
            {
                "name": "First Menu",
                "description": "My First Menu!!",
                "sections": [
                    {
                        "name": "Appetizers",
                        "description": "Starters",
                        "items": [{"name": "Fried Pickles", "description": "Deep fried pickles"}],
                    },
                ],
            },
        ),
    )

    assert response.status == 200
