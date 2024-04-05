from uuid import UUID

from adaptix import Retort
from blacksheep import FromJSON, Response, ok
from blacksheep.server.controllers import APIController, post

from src.application.common.mapper.interface import Mapper
from src.contracts.menu.create_menu_request import CreateMenuRequest


class MenusController(APIController):
    _mapper: Mapper
    _retort: Retort

    @classmethod
    def route(cls) -> str | None:
        return "hosts/{host_id}/menus"

    @post()
    async def create_menu(
        self,
        host_id: UUID,
        create_menu_request: FromJSON,
    ) -> Response:
        """
        Create menu request.

        :param host_id: Host entity id
        :param input: CreateMenuRequest contract
        """

        create_menu_request = self._retort.load(
            create_menu_request.value,
            CreateMenuRequest,
        )
        command = self._mapper.convert_create_menu_request_to_command(create_menu_request)
        return ok(command)
