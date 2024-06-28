import os

from pydantic_settings import BaseSettings


class Config(BaseSettings):
    postgresql_url: str = (
        f'postgresql+asyncpg://{os.environ["POSTGRES_USER"]}:{os.environ["POSTGRES_PASSWORD"]}@{os.environ["POSTGRES_HOST_NAME"]}/{os.environ["POSTGRES_DB"]}'
    )
