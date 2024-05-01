from dataclasses import dataclass

from src.domain.common.models.domain_event import DomainEvent
from src.domain.menu.menu import Menu


@dataclass
class MenuCreated(DomainEvent):
    menu: Menu
