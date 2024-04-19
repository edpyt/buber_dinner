import os
from pathlib import Path

import tomllib


def read_toml(path: Path | None = None) -> dict:
    if path is None:
        path = Path(os.getenv("BUBER_DINNER_CONFIG_PATH", "./config_dist/config.toml"))
    f = path.open("rb")
    toml_data: dict = tomllib.load(f)
    return toml_data
