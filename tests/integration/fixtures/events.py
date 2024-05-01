from typing import AsyncGenerator, Generator

import nats
import pytest
from src.application.common.events.event_bus import EventBus
from src.application.dinners.events.menu_create_handler import MenuCreateHandler
from src.infrastructure.event_bus.event_bus import EventBusImpl
from src.infrastructure.message_broker.interface import MessageBroker
from src.infrastructure.message_broker.message_broker import MessageBrokerImpl
from testcontainers.nats import NatsContainer


@pytest.fixture(name="nats_mq", scope="session")
def create_nats_container() -> Generator[NatsContainer, None, None]:
    with NatsContainer() as nats:
        yield nats


@pytest.fixture(name="message_broker", scope="session")
async def create_nats_message_broker(
    nats_mq: NatsContainer,
) -> AsyncGenerator[MessageBroker, None]:
    nats_conn = await nats.connect(nats_mq.nats_uri())
    yield MessageBrokerImpl(nats_conn)
    await nats_conn.close()


@pytest.fixture(name="event_bus", scope="session")
def create_event_bus(message_broker: MessageBroker) -> EventBus:
    return EventBusImpl(message_broker)


@pytest.fixture()
def menu_create_handler(event_bus: EventBus) -> MenuCreateHandler:
    return MenuCreateHandler(event_bus)
