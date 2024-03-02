from clean_architecture_ddd.api.di.dishka import DishkaDI
from clean_architecture_ddd.infrastructure.di import setup_container


def setup_di() -> DishkaDI:
    container = setup_container()
    return DishkaDI(container)
