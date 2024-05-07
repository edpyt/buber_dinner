from contextlib import asynccontextmanager
from typing import AsyncGenerator

import nats


@asynccontextmanager
async def make_broker_connection(conn_url: str) -> AsyncGenerator[nats.NATS, None]:
    conn = await nats.connect(conn_url)

    try:
        yield conn
    finally:
        await conn.close()
