from blacksheep import Application


def setup_middlewares(app: Application, *middlewares: tuple) -> None:
    app.middlewares = list(middlewares)
