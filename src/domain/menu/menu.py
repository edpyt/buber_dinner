from dataclasses import dataclass, field
from datetime import datetime
from typing import Self

from src.domain.common.models.aggregate_root import AggregateRoot
from src.domain.common.vo.average_rating import AverageRating
from src.domain.dinner.vo.dinner_id import DinnerId
from src.domain.host.vo.host_id import HostId
from src.domain.menu.entities.menu_section import MenuSection
from src.domain.menu.vo.menu_id import MenuId
from src.domain.menu_review.vo.menu_review_id import MenuReviewId


@dataclass
class Menu(AggregateRoot[MenuId]):
    name: str
    description: str
    average_rating: AverageRating
    host_id: HostId

    sections: list[MenuSection] = field(default_factory=list)
    dinner_ids: list[DinnerId] = field(default_factory=list)
    menu_review_ids: list[MenuReviewId] = field(default_factory=list)

    created_date_time: datetime = field(default_factory=datetime.now)
    updated_date_time: datetime = field(default_factory=datetime.now)

    @classmethod
    def create(cls, name: str, description: str, host_id: HostId) -> Self:
        return cls(
            id=MenuId.create_unique(),
            name=name,
            description=description,
            average_rating=AverageRating.create_new(),
            host_id=host_id,
        )
