from datetime import datetime, timedelta
from random import randrange, choice

from clean_architecture_ddd.api.responses.weather_forecast import WeatherForecast


def get_weather_forecast() -> list[WeatherForecast]:
    today = datetime.now()
    weather = [
        WeatherForecast(
            date=timedelta(days=i) + today,
            temperature_c=randrange(-20, 55),
            summary=choice(
                (
                    "Freezing",
                    "Chilly",
                    "Cool",
                    "Mild",
                    "Warm",
                    "Balmy",
                    "Hot",
                    "Sweltering",
                    "Scorching",
                )
            ),
        )
        for i in range(1, 5)
    ]
    return weather
