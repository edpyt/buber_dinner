from blacksheep import Request
from guardpost import AuthenticationHandler, Identity


class BuberDinnerAuthHandler(AuthenticationHandler):
    def __init__(self) -> None:
        ...

    async def authenticate(self, context: Request) -> Identity | None:
        header_value = context.get_first_header(b"Authorization")

        if header_value:
            # FIXME: add real identity
            context.identity = Identity({"name": "test"}, "MOCK")
        else:
            context.identity = None

        return context.identity
