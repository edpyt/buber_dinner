from dataclasses import dataclass
from datetime import datetime


@dataclass
class MenuResponse:
    id: str
    name: str
    description: str
    average_rating: float
    sections: tuple["MenuSectionResponse", ...]
    host_id: str
    dinner_ids: tuple[str, ...]
    menu_review_ids: tuple[str, ...]
    created_date_time: datetime
    updated_date_time: datetime


@dataclass
class MenuSectionResponse:
    id: str
    name: str
    description: str
    items: tuple["MenuItemResponse", ...]


@dataclass
class MenuItemResponse:
    id: str
    name: str
    description: str
