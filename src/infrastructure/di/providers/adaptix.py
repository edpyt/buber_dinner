from dishka import Provider, Scope, provide

from src.infrastructure.converter.retort import setup_retort


class AdaptixProvider(Provider):
    retort = provide(setup_retort, scope=Scope.REQUEST)
