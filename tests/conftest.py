import asyncio

import pytest


@pytest.fixture(scope="session")
def anyio_backend():
    return "asyncio"


# BUG: without this i have error, wth......
@pytest.fixture(scope="session")
def event_loop():
    """
    Creates an instance of the default event loop for the test session.
    """
    policy = asyncio.get_event_loop_policy()
    loop = policy.new_event_loop()
    yield loop
    loop.close()
