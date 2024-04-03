from uuid import UUID

from blacksheep import FromJSON, Response, ok
from blacksheep.server.controllers import APIController, post

from src.application.common.mapper.interface import Mapper
from src.contracts.menu.create_menu_request import CreateMenuRequest


class MenusController(APIController):
    @classmethod
    def route(cls) -> str | None:
        return "hosts/{host_id}/menus"

    @post()
    async def create_menu(
        self,
        host_id: UUID,
        create_menu_request: FromJSON[CreateMenuRequest],
        mapper: Mapper,
    ) -> Response:
        """
        Create menu request.

        :param host_id: Host entity id
        :param input: CreateMenuRequest contract
        """

        return ok(create_menu_request.value)
