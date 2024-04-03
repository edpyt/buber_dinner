from dataclasses import dataclass
from datetime import datetime


@dataclass
class MenuResponse:
    id: str
    name: str
    description: str
    average_rating: float
    sections: list["MenuSectionResponse"]
    host_id: str
    dinner_ids: list[str]
    menu_review_ids: list[str]
    created_date_time: datetime
    updated_date_time: datetime


@dataclass
class MenuSectionResponse:
    id: str
    name: str
    description: str
    items: list["MenuItemResponse"]


@dataclass
class MenuItemResponse:
    id: str
    name: str
    description: str
