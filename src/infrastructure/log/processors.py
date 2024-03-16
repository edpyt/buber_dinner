from typing import Callable

import structlog

ProcessorType = Callable[
    [
        structlog.types.WrappedLogger,
        str,
        structlog.types.EventDict,
    ],
    str | bytes,
]


def get_render_processor() -> ProcessorType:
    return structlog.dev.ConsoleRenderer(colors=True)
