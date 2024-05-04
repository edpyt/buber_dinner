from blacksheep import Application

from src.api.auth.handler import BuberDinnerAuthHandler
from src.api.docs import setup_docs
from src.api.middleware import ErrorHandlingMiddleware
from src.infrastructure.log import configure_logging


def build_api() -> Application:
    """Build BlackSheep application"""

    app = Application(show_error_details=True)
    setup_app(app)

    return app


def setup_app(app: Application) -> None:
    """Before start application"""

    configure_logging()

    setup_docs(app)
    app.middlewares = [ErrorHandlingMiddleware()]

    app.use_authentication().add(BuberDinnerAuthHandler())
    app.use_authorization()
