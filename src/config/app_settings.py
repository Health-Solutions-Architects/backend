from pydantic_settings import BaseSettings


class AppSettings(BaseSettings):
    postgres_database_url: str

    jwt_secret_key: str
    jwt_expiration: int
    jwt_algorithms: str

    redis_host: str
    redis_port: int
    redis_password: str

    session_key: str
