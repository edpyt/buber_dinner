from blacksheep import auth
from blacksheep.server.controllers import APIController, get


class DinnerController(APIController):
    @classmethod
    def route(cls) -> str:
        return "dinners"

    @classmethod
    def version(cls) -> str:
        return "v1"

    @auth()
    @get("/")
    def list_dinners(self) -> list[str]:
        """Gets a list of dinners"""

        return self.ok([])
