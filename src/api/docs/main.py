from blacksheep import Application
from blacksheep.server.openapi.v3 import OpenAPIHandler
from openapidocs.v3 import Info


def setup_docs(app: Application) -> None:
    docs = OpenAPIHandler(info=Info(title="Hello World!", version="0.0.1"))
    docs.bind_app(app)
