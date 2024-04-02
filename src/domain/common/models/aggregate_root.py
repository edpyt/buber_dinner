from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Generic, Self

from .entity import Entity, TId


@dataclass
class AggregateRoot(Entity, ABC, Generic[TId]):
    @abstractmethod
    @classmethod
    def create(cls, *args, **kwargs) -> Self: ...
