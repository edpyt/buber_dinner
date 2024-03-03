from blacksheep import Application

from src.api.docs.main import setup_docs
from src.infrastructure.di.main import build_application_container


def build_api() -> Application:
    di_container = build_application_container()
    app = Application(services=di_container, show_error_details=True)
    setup_app(app)
    return app


def setup_app(app: Application) -> None:
    # Before start
    setup_docs(app)
