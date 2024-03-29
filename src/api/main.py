from blacksheep import Application

from src.api.auth.handler import BuberDinnerAuthHandler
from src.api.di import setup_api_di
from src.api.docs.main import setup_docs
from src.api.middleware import ErrorHandlingMiddleware
from src.infrastructure.di.main import build_application_container
from src.infrastructure.log.main import configure_logging


def build_api() -> Application:
    """Build BlackSheep application"""

    di_container = build_application_container()
    setup_api_di(di_container)
    app = Application(services=di_container, show_error_details=True)
    setup_app(app)
    return app


def setup_app(app: Application) -> None:
    """Before start application"""

    configure_logging()

    setup_docs(app)
    app.middlewares = [ErrorHandlingMiddleware()]

    app.use_authentication().add(BuberDinnerAuthHandler())
    app.use_authorization()
