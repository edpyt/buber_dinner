from typing import AsyncGenerator, Generator

import nats
import pytest
from src.application.common.events.event_bus import EventBus
from src.application.dinners.events.menu_create_handler import MenuCreateHandler
from src.infrastructure.config.broker import BrokerConfig
from src.infrastructure.event_bus.event_bus import EventBusImpl
from src.infrastructure.message_broker.interface import MessageBroker
from src.infrastructure.message_broker.main import make_broker_connection
from src.infrastructure.message_broker.message_broker import MessageBrokerImpl
from testcontainers.nats import NatsContainer


@pytest.fixture(name="nats_container", scope="session")
async def create_nats_container() -> Generator[NatsContainer, None, None]:
    with NatsContainer() as nats_container:
        yield nats_container


@pytest.fixture(name="broker_config", scope="session")
def create_broker_config(nats_container: NatsContainer) -> BrokerConfig:
    host, port = nats_container.nats_host_and_port()
    return BrokerConfig(host=host, port=port)


@pytest.fixture(name="nats_conn")
async def connect_nats(nats_container: NatsContainer) -> AsyncGenerator[nats.NATS, None]:
    conn_url = nats_container.nats_uri()

    async with make_broker_connection(conn_url=conn_url) as conn:
        yield conn


@pytest.fixture(name="message_broker")
async def create_nats_message_broker(nats_conn: nats.NATS) -> MessageBroker:
    return MessageBrokerImpl(nats_conn)


@pytest.fixture(name="event_bus")
def create_event_bus(message_broker: MessageBroker) -> EventBus:
    return EventBusImpl(message_broker)


@pytest.fixture()
def menu_create_handler(event_bus: EventBus) -> MenuCreateHandler:
    return MenuCreateHandler(event_bus)
