from typing import Generator

import pytest
from src.application.common.events.event_bus import EventBus
from src.application.dinners.events.menu_create_handler import MenuCreateHandler
from src.infrastructure.event_bus.event_bus import EventBusImpl
from testcontainers.nats import NatsContainer


@pytest.fixture(name="nats_mq", scope="session")
def create_nats_container() -> Generator[NatsContainer, None, None]:
    with NatsContainer() as nats:
        yield nats


@pytest.fixture(name="event_bus", scope="session")
def create_event_bus(nats_mq: NatsContainer) -> EventBus:
    return EventBusImpl(nats_mq)


@pytest.fixture()
def menu_create_handler(event_bus: EventBus) -> MenuCreateHandler:
    return MenuCreateHandler(event_bus)
