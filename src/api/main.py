from blacksheep import Application

from src.api.di import setup_api_di
from src.api.docs.main import setup_docs
from src.infrastructure.di.main import build_application_container


def build_api() -> Application:
    """Build BlackSheep application method"""

    di_container = build_application_container()
    setup_api_di(di_container)
    app = Application(services=di_container, show_error_details=True)
    setup_app(app)
    return app


def setup_app(app: Application) -> None:
    """Before start application method"""

    setup_docs(app)
