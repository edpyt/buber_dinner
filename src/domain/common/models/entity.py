from abc import ABC
from dataclasses import dataclass
from typing import Generic, TypeVar

TId = TypeVar("TId")


@dataclass
class Entity(ABC, Generic[TId]):
    id: TId
