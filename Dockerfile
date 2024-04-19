FROM python:3.11-slim-bullseye as build

WORKDIR /app/

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY ./src /app/src
COPY ./requirements /app/requirements

RUN python -m pip install uv

FROM build as dev

RUN uv pip install --no-cache \
    --python $(which python3.11) \
    -r /app/requirements/dev.txt

FROM build as migrations
COPY ./alembic.ini /app/

RUN uv pip install --no-cache \
    --python $(which python3.11) \
    -r /app/requirements/migrations.txt
