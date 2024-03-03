from blacksheep import Application

from src.api.docs.main import setup_docs


def build_api() -> Application:
    app = Application(show_error_details=True)
    setup_app(app)
    return app


def setup_app(app: Application) -> None:
    # Before start
    setup_docs(app)
