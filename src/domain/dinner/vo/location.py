from src.domain.common.models.value_object import BaseValueObject


class Location(BaseValueObject):
    name: str
    address: str
    latitude: float
    longitude: float
