from pydantic_settings import BaseSettings


class AppSettings(BaseSettings):
    postgres_database_url: str
