from datetime import datetime
from typing import Literal
from pydantic import BaseModel, Field


class WeatherForecast(BaseModel):
    dt: datetime = Field(alias="date")
    temperature_c: float
    summary: Literal[
        "Freezing",
        "Chilly",
        "Cool",
        "Mild",
        "Warm",
        "Balmy",
        "Hot",
        "Sweltering",
        "Scorching",
    ]
