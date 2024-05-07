from logging import Logger

from blacksheep import Application
from nats import NATS

from src.api.auth.handler import BuberDinnerAuthHandler
from src.api.docs import setup_docs
from src.api.middleware import ErrorHandlingMiddleware
from src.infrastructure.di import build_application_container
from src.infrastructure.log import configure_logging


def build_api() -> Application:
    """Build BlackSheep application"""

    app = Application(show_error_details=True)
    setup_app(app)

    app.on_start += on_start

    app.on_stop += on_stop
    app.on_stop += close_connections

    return app


def setup_app(app: Application) -> None:
    """Before start application"""

    configure_logging()

    setup_docs(app)
    app.middlewares = [ErrorHandlingMiddleware()]

    app.use_authentication().add(BuberDinnerAuthHandler())
    app.use_authorization()


async def on_start(app: Application) -> None:
    container = await build_application_container(app.services)
    logger = container.resolve(Logger)
    logger.info("Start buber_dinner application!")


async def on_stop(app: Application) -> None:
    logger = app.services.resolve(Logger)
    logger.info("Stop buber_dinner application.")


async def close_connections(app: Application) -> None:
    await app.services.resolve(NATS).close()
