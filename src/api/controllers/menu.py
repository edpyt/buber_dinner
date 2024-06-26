from dataclasses import asdict
from uuid import UUID

from adaptix import Retort
from blacksheep import FromJSON, Response, auth, ok
from blacksheep.server.controllers import APIController, post
from mediatr import Mediator

from src.application.common.mapper.interface import MainMapper
from src.contracts.menu.create_menu_request import CreateMenuRequest


class MenusController(APIController):
    _mapper: MainMapper
    _mediator: Mediator

    @classmethod
    def route(cls) -> str | None:
        return "hosts/{host_id}/menus"

    @auth()
    @post()
    async def create_menu(
        self,
        host_id: UUID,
        create_menu_request: FromJSON[CreateMenuRequest],
        retort: Retort,
    ) -> Response:
        """
        Create menu request.

        :param host_id: Host entity id
        :param input: CreateMenuRequest contract
        """

        create_menu_request = retort.load(
            {**asdict(create_menu_request.value), "host_id": str(host_id)},
            CreateMenuRequest,
        )
        command = self._mapper.menu.convert_create_menu_request_to_command(create_menu_request)
        result = await self._mediator.send(command)
        return ok(self._mapper.menu.convert_menu_result_to_response(result))
