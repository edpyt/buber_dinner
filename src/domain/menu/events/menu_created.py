from dataclasses import dataclass
from typing import TypeVar

from src.domain.common.models.domain_event import DomainEvent

Menu = TypeVar("Menu")


@dataclass
class MenuCreated(DomainEvent):
    menu: Menu  # type: ignore
