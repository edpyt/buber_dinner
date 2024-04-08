from adaptix.conversion import coercer, get_converter

from src.application.common.mapper.interface import MenuMapper
from src.application.menu.commands.create_menu.command import (
    CreateMenuCommand,
    MenuItemCommand,
    MenuSectionCommand,
)
from src.contracts.menu.create_menu_request import CreateMenuRequest, MenuItem, MenuSection
from src.contracts.menu.menu_response import MenuItemResponse, MenuResponse, MenuSectionResponse
from src.domain.menu.menu import Menu

__convert_menu_item_to_command = get_converter(MenuItem, MenuItemCommand)
__convert_menu_section_to_command = get_converter(
    MenuSection,
    MenuSectionCommand,
    recipe=[
        coercer(
            list[MenuItem],
            list[MenuItemCommand],
            lambda menu_items: list(map(__convert_menu_item_to_command, menu_items)),
        ),
    ],
)


class MenuMapperImpl(MenuMapper):
    convert_create_menu_request_to_command = get_converter(
        CreateMenuRequest,
        CreateMenuCommand,
        recipe=[
            coercer(
                list[MenuSection],
                list[MenuSectionCommand],
                lambda menu_sections: list(
                    map(__convert_menu_section_to_command, menu_sections),
                ),
            ),
        ],
    )

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
