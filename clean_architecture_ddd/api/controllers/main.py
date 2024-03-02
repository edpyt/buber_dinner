from blacksheep import Application

from clean_architecture_ddd.api.controllers.weather_forecast import (
    get_weather_forecast,
)


def setup_controllers(app: Application) -> None:
    app.router.add_get("/", get_weather_forecast)
