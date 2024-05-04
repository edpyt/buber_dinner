import nats


async def make_broker_connection(conn_url: str) -> nats.NATS:
    return await nats.connect(conn_url)
