from abc import ABC
from dataclasses import dataclass
from typing import Generic

from .entity import Entity, TId


@dataclass
class AggregateRoot(Entity, ABC, Generic[TId]):
    ...
