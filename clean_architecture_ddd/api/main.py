from blacksheep import Application

from clean_architecture_ddd.api.controllers import setup_controllers
from clean_architecture_ddd.api.docs.main import setup_docs


def build_api() -> Application:
    app = Application(show_error_details=True)
    setup_app(app)
    return app


def setup_app(app: Application) -> None:
    # Before start
    setup_docs(app)

    # On start
    app.on_start(setup_controllers)
