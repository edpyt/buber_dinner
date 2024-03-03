import os

import uvicorn


def start_application() -> None:
    uvicorn.run(
        "clean_architecture_ddd.api.main:build_api",
        reload=bool(os.environ.get("APP_RELOAD", True)),
        factory=True,
    )


if __name__ == "__main__":
    start_application()
