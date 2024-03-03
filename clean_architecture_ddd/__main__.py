from typing import TypeVar

import uvicorn

T = TypeVar("T")


def start_application(app: T) -> None:
    uvicorn.run(app)


if __name__ ==  "__main__":
    from clean_architecture_ddd.api.main import build_api

    app = build_api()
    start_application(app)
