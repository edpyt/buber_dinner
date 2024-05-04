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

    app.on_start += setup_di
    app.on_stop += close_connections

    return app


def setup_app(app: Application) -> None:
    """Before start application"""

    configure_logging()

    setup_docs(app)
    app.middlewares = [ErrorHandlingMiddleware()]

    app.use_authentication().add(BuberDinnerAuthHandler())
    app.use_authorization()


async def setup_di(app: Application) -> None:
    await build_application_container(app.services)


async def close_connections(app: Application) -> None:
    await app.services.resolve(NATS).close()
