from nats import NATS
from rodi import Container

from src.application.common.events.event_bus import EventBus
from src.infrastructure.config.config import Config
from src.infrastructure.event_bus.event_bus import EventBusImpl
from src.infrastructure.message_broker.interface import MessageBroker
from src.infrastructure.message_broker.main import make_broker_connection
from src.infrastructure.message_broker.message_broker import MessageBrokerImpl


async def setup_message_queue_di(container: Container, config: Config) -> None:
    try:
        nats_conn = await make_broker_connection(conn_url=config.broker_config.full_url)
    except:  # noqa: E722
        nats_conn = None

    setup_events_di(container)

    container.add_instance(nats_conn, NATS)
    container.add_transient(MessageBroker, MessageBrokerImpl)


def setup_events_di(container: Container) -> None:
    container.add_singleton(EventBus, EventBusImpl)
