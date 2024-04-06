from typing import Any

from adaptix import Retort
from adaptix.conversion import coercer, get_converter

from src.application.authentication.commands.register.command import RegisterCommand
from src.application.authentication.queries.login.query import LoginQuery
from src.application.common.mapper.interface import Mapper
from src.application.menu.commands.create_menu.command import (
    CreateMenuCommand,
    MenuItemCommand,
    MenuSectionCommand,
)
from src.application.services.authentication.common.result import AuthenticationResult
from src.contracts.authentication.authentication_response import AuthenticationResponse
from src.contracts.authentication.login_request import LoginRequest
from src.contracts.authentication.register_request import RegisterRequest
from src.contracts.menu.create_menu_request import CreateMenuRequest, MenuItem, MenuSection
from src.contracts.menu.menu_response import MenuItemResponse, MenuResponse, MenuSectionResponse
from src.domain.menu.menu import Menu


class MapperImpl(Mapper):
    def __init__(self, retort: Retort) -> None:
        self._retort = retort

        self.convert_register_request_to_command = get_converter(  # type: ignore[method-assign]
            RegisterRequest,
            RegisterCommand,
        )
        self.convert_login_request_to_query = get_converter(  # type: ignore[method-assign]
            LoginRequest,
            LoginQuery,
        )

        convert_menu_item_to_command = get_converter(MenuItem, MenuItemCommand)
        convert_menu_section_to_command = get_converter(
            MenuSection,
            MenuSectionCommand,
            recipe=[
                coercer(
                    list[MenuItem],
                    list[MenuItemCommand],
                    lambda menu_items: list(map(convert_menu_item_to_command, menu_items)),
                ),
            ],
        )
        self.convert_create_menu_request_to_command = get_converter(  # type: ignore[method-assign]
            CreateMenuRequest,
            CreateMenuCommand,
            recipe=[
                coercer(
                    list[MenuSection],
                    list[MenuSectionCommand],
                    lambda menu_sections: list(
                        map(convert_menu_section_to_command, menu_sections),
                    ),
                ),
            ],
        )

    def convert_auth_result_to_response(self, src: AuthenticationResult) -> AuthenticationResponse:
        auth_result_data = self._convert_to_flatten_dict(self._retort.dump(src))
        auth_response: AuthenticationResponse = self._retort.load(
            auth_result_data,
            AuthenticationResponse,
        )
        return auth_response

    def convert_menu_result_to_response(self, src: Menu) -> MenuResponse:
        return MenuResponse(
            id=str(src.id.value),
            name=src.name,
            description=src.description,
            average_rating=src.average_rating.value,
            sections=tuple(
                MenuSectionResponse(
                    id=str(section.id.value),
                    name=section.name,
                    description=section.description,
                    items=tuple(
                        MenuItemResponse(
                            id=str(item.id.value),
                            name=item.name,
                            description=item.description,
                        )
                        for item in section.items
                    ),
                )
                for section in src.sections
            ),
            host_id=str(src.host_id.value),
            dinner_ids=tuple(str(id_.value) for id_ in src.dinner_ids),
            menu_review_ids=tuple(str(id_.value) for id_ in src.menu_review_ids),
            created_date_time=src.created_date_time,
            updated_date_time=src.updated_date_time,
        )

    @staticmethod
    def _convert_to_flatten_dict(nest_dict: dict[str, dict | Any]) -> dict[str, Any]:
        def convert_to_dict(n_dict: dict[str, dict | Any]) -> dict[str, Any]:
            res = {}
            for key, item in n_dict.items():
                if isinstance(item, dict):
                    res.update(convert_to_dict(item))
                else:
                    res[key] = item
            return res

        return convert_to_dict(nest_dict)
