from blacksheep import Request
from guardpost import AuthenticationHandler, Identity


class BuberDinnerAuthHandler(AuthenticationHandler):
    def __init__(self) -> None:
        ...

    async def authenticate(self, context: Request) -> Identity | None:
        header_value = context.get_first_header(b"Authorization")

        if header_value:
            context.identity = Identity({"name": "Abobe"}, "MOCK")
        else:
            context.identity = None

        return context.identity
