from blacksheep import Application
from mediatr import Mediator

from src.api.di import setup_api_di
from src.api.docs.main import setup_docs
from src.api.middleware import ErrorHandlingMiddleware, setup_middlewares
from src.infrastructure.di.main import build_application_container
from src.infrastructure.log.main import configure_logging


def build_api() -> Application:
    """Build BlackSheep application"""

    di_container = build_application_container()
    setup_api_di(di_container)
    di_container.resolve(Mediator)
    app = Application(services=di_container, show_error_details=True)
    setup_app(app)
    return app


def setup_app(app: Application) -> None:
    """Before start application"""

    configure_logging()

    setup_docs(app)
    setup_middlewares(app, ErrorHandlingMiddleware())
