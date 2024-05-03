from typing import AsyncGenerator

import nats

from src.infrastructure.config.broker import BrokerConfig


async def make_broker_connection(config: BrokerConfig) -> AsyncGenerator[nats.NATS, None]:
    conn = await nats.connect(config.full_url)
    yield conn
    await conn.close()
