from dataclasses import dataclass, field
from datetime import datetime
from typing import Self

from src.domain.common.models.aggregate_root import AggregateRoot
from src.domain.common.vo.average_rating import AverageRating
from src.domain.dinner.vo.dinner_id import DinnerId
from src.domain.host.vo.host_id import HostId
from src.domain.menu.vo.menu_id import MenuId
from src.domain.users.vo.user_id import UserId


@dataclass
class Host(AggregateRoot[HostId]):
    first_name: str
    last_name: str
    profile_image: str

    user_id: UserId
    average_rating: AverageRating = field(default_factory=AverageRating.create_new)

    _menu_ids: list[MenuId] = field(default_factory=list)
    _dinner_ids: list[DinnerId] = field(default_factory=list)

    created_date_time: datetime = field(default_factory=datetime.now)
    updated_date_time: datetime = field(default_factory=datetime.now)

    @classmethod
    def create(cls, first_name: str, last_name: str, profile_image: str, user_id: UserId) -> Self:
        return cls(
            id=HostId.create_unique(),
            first_name=first_name,
            last_name=last_name,
            profile_image=profile_image,
            user_id=user_id,
        )

    @property
    def menu_ids(self) -> tuple[MenuId, ...]:
        return tuple(self.menu_ids)

    @property
    def dinner_ids(self) -> tuple[DinnerId, ...]:
        return tuple(self._dinner_ids)
