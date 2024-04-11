FROM python:3.11-slim-bullseye as build

WORKDIR /app/

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY ./pyproject.toml /app/
COPY ./src /app/src

FROM build as dev
RUN python -m pip install uv
RUN uv pip compile pyproject.toml -o requirements.txt
RUN uv pip install --no-cache \
                      --python $(which python3.11) \
                      -r requirements.txt

FROM build as migrations
RUN python -m pip install poetry
RUN poetry install --only db
