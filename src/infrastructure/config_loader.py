from pathlib import Path

import tomllib


def read_toml(path: Path) -> dict:
    f = path.open("rb")
    toml_data: dict = tomllib.load(f)
    return toml_data
