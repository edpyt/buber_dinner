from blacksheep import Application

from clean_architecture_ddd.api.controllers import setup_controllers
from clean_architecture_ddd.api.di import setup_di
from clean_architecture_ddd.api.docs.main import setup_docs


def build_api() -> Application:
    di_service = setup_di()
    app = Application(services=di_service, show_error_details=True)
    setup_docs(app)
    app.on_start(setup_app)
    return app


async def setup_app(app: Application) -> None:
    setup_controllers(app)
