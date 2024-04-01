from dataclasses import dataclass, field
from datetime import datetime

from src.domain.bill import Bill
from src.domain.common.models.aggregate_root import AggregateRoot
from src.domain.common.vo.average_rating import AverageRating
from src.domain.common.vo.rating import Rating
from src.domain.dinner import Dinner
from src.domain.guest.vo.guest_id import GuestId
from src.domain.users.vo.user_id import UserId


@dataclass
class Guest(AggregateRoot[GuestId]):
    first_name: str
    last_name: str
    profile_image: str

    average_rating: AverageRating
    user_id: UserId = field(default_factory=UserId.create_unique)

    _upcoming_dinner_ids: list[Dinner] = field(default_factory=list)
    _past_dinner_ids: list[Dinner] = field(default_factory=list)
    _bill_ids: list[Bill] = field(default_factory=list)
    # _menu_review_ids: list[MenuReview] = field(default_factory=list)  # noqa: ERA001
    _ratings: list[Rating] = field(default_factory=list)

    created_date_time: datetime = field(default_factory=datetime.utcnow)
    updated_date_time: datetime = field(default_factory=datetime.utcnow)

    @property
    def upcoming_dinner_ids(self) -> tuple[Dinner, ...]:
        return tuple(self._upcoming_dinner_ids)

    @property
    def past_dinner_ids(self) -> tuple[Dinner, ...]:
        return tuple(self._past_dinner_ids)

    @property
    def bill_ids(self) -> tuple[Bill, ...]:
        return tuple(self._bill_ids)

    # @property
    # def menu_review_ids(self) -> tuple[MenuReview, ...]:
        # return tuple(self._menu_review_ids)  # noqa: ERA001

    @property
    def ratings(self) -> tuple[Rating, ...]:
        return tuple(self._ratings)
