from dataclasses import dataclass, field
from datetime import datetime
from typing import Self

from src.domain.common.models.aggregate_root import AggregateRoot
from src.domain.common.vo.average_rating import AverageRating
from src.domain.dinner.vo.dinner_id import DinnerId
from src.domain.host.vo.host_id import HostId
from src.domain.menu.entities.menu_section import MenuSection
from src.domain.menu.events.menu_created import MenuCreated
from src.domain.menu.vo.menu_id import MenuId
from src.domain.menu_review.vo.menu_review_id import MenuReviewId


@dataclass
class Menu(AggregateRoot[MenuId]):
    name: str
    description: str
    average_rating: AverageRating
    host_id: HostId

    _sections: list[MenuSection] = field(default_factory=list)
    _dinner_ids: list[DinnerId] = field(default_factory=list)
    _menu_review_ids: list[MenuReviewId] = field(default_factory=list)

    created_date_time: datetime = field(default_factory=datetime.now)
    updated_date_time: datetime = field(default_factory=datetime.now)

    @classmethod
    def create(
        cls,
        name: str,
        description: str,
        host_id: HostId,
        sections: list[MenuSection] | None = None,
    ) -> Self:
        if sections is None:
            sections = []
        menu = cls(
            id=MenuId.create_unique(),
            name=name,
            description=description,
            average_rating=AverageRating.create_new(),
            host_id=host_id,
            _sections=sections,
        )

        menu.add_domain_event(MenuCreated(menu))

        return menu

    @property
    def sections(self) -> tuple[MenuSection, ...]:
        return tuple(self._sections)

    @property
    def dinner_ids(self) -> tuple[DinnerId, ...]:
        return tuple(self._dinner_ids)

    @property
    def menu_review_ids(self) -> tuple[MenuReviewId, ...]:
        return tuple(self._menu_review_ids)
