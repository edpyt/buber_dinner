from dataclasses import dataclass
from typing import TypeVar

from src.domain.common.models.domain_event import DomainEvent

TMenu = TypeVar("TMenu")


@dataclass
class MenuCreated(DomainEvent):
    menu: TMenu
