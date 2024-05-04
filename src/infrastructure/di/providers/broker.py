from typing import AsyncGenerator

from dishka import Provider, Scope, provide
from nats import NATS

from src.application.common.events.event_bus import EventBus
from src.infrastructure.config.broker import BrokerConfig
from src.infrastructure.event_bus.event_bus import EventBusImpl
from src.infrastructure.message_broker.interface import MessageBroker
from src.infrastructure.message_broker.main import make_broker_connection
from src.infrastructure.message_broker.message_broker import MessageBrokerImpl


class BrokerProvider(Provider):
    event_bus = provide(EventBusImpl, provides=EventBus)
    message_broker = provide(
        MessageBrokerImpl,
        provides=MessageBroker,
        scope=Scope.REQUEST,
    )

    @provide
    async def nats_conn(self, broker_config: BrokerConfig) -> AsyncGenerator[NATS, None]:
        async with make_broker_connection(broker_config.full_url) as conn:
            yield conn
