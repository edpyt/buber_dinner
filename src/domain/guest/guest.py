from dataclasses import dataclass, field
from datetime import datetime
from typing import Self

from src.domain.bill import Bill
from src.domain.common.models.aggregate_root import AggregateRoot
from src.domain.common.vo.average_rating import AverageRating
from src.domain.common.vo.rating import Rating
from src.domain.dinner import Dinner
from src.domain.guest.vo.guest_id import GuestId
from src.domain.menu_review.menu_review import MenuReview
from src.domain.users.vo.user_id import UserId


@dataclass
class Guest(AggregateRoot[GuestId]):
    first_name: str
    last_name: str
    profile_image: str

    average_rating: AverageRating
    user_id: UserId

    _upcoming_dinner_ids: list[Dinner] = field(default_factory=list)
    _past_dinner_ids: list[Dinner] = field(default_factory=list)
    _bill_ids: list[Bill] = field(default_factory=list)
    _menu_review_ids: list[MenuReview] = field(default_factory=list)
    _ratings: list[Rating] = field(default_factory=list)

    created_date_time: datetime = field(default_factory=datetime.now)
    updated_date_time: datetime = field(default_factory=datetime.now)

    @classmethod
    def create(
        cls,
        first_name: str,
        last_name: str,
        profile_image: str,
        average_rating: AverageRating,
        user_id: UserId,
    ) -> Self:
        return cls(
            id=GuestId.create_unique(),
            first_name=first_name,
            last_name=last_name,
            profile_image=profile_image,
            average_rating=average_rating,
            user_id=user_id,
        )

    @property
    def upcoming_dinner_ids(self) -> tuple[Dinner, ...]:
        return tuple(self._upcoming_dinner_ids)

    @property
    def past_dinner_ids(self) -> tuple[Dinner, ...]:
        return tuple(self._past_dinner_ids)

    @property
    def bill_ids(self) -> tuple[Bill, ...]:
        return tuple(self._bill_ids)

    @property
    def menu_review_ids(self) -> tuple[MenuReview, ...]:
        return tuple(self._menu_review_ids)

    @property
    def ratings(self) -> tuple[Rating, ...]:
        return tuple(self._ratings)
