import os

import logfire
import uvicorn


def start_application() -> None:
    logfire.configure()
    logfire.instrument_asyncpg()

    uvicorn.run(
        "src.api.main:build_api",
        reload=bool(os.environ.get("APP_RELOAD", True)),
        host="0.0.0.0",  # noqa: S104
        factory=True,
    )


if __name__ == "__main__":
    start_application()
