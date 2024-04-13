from datetime import datetime
from uuid import UUID

from clickhouse_sqlalchemy import types
from sqlalchemy.orm import Mapped, mapped_column

from src.application.menu.dto.average_rating import AverageRatingDTO
from src.infrastructure.persistence.db.types.dataclass import DataclassType

from .base import BaseCH


class Menu(BaseCH):
    __tablename__ = "menu"

    id: Mapped[UUID] = mapped_column(types.UUID, primary_key=True)
    name: Mapped[str] = mapped_column(types.String(length=100))
    description: Mapped[str] = mapped_column(types.String(length=100))
    average_rating: Mapped[AverageRatingDTO] = mapped_column(DataclassType(AverageRatingDTO))
    host_id: Mapped[UUID] = mapped_column(types.UUID)

    # TODO: sections, dinner_ids, menu_review_ids

    created_date_time: Mapped[datetime] = mapped_column(types.DateTime)
    updated_date_time: Mapped[datetime] = mapped_column(types.DateTime)
