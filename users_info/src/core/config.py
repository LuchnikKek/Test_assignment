from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict

ROOT_PATH: Path = Path(__file__).parent.parent.parent.parent
ENV_FILEPATH: Path = ROOT_PATH / ".env"


class PostgresSettings(BaseSettings):
    """Конфигурация PostgreSQL."""

    user: str
    password: str
    host: str
    port: int
    database: str

    model_config = SettingsConfigDict(
        env_file=ENV_FILEPATH, env_file_encoding="utf-8", extra="ignore", env_prefix="USERS_PG_"
    )

    @property
    def dsn(self):
        """Строка, содержащая DSN для подключения."""
        return f"postgresql+asyncpg://{self.user}:{self.password}@{self.host}:{self.port}/{self.database}"


class ApiSettings(BaseSettings):
    """Конфигурация API."""

    port: int

    model_config = SettingsConfigDict(
        env_file=ENV_FILEPATH, env_file_encoding="utf-8", extra="ignore", env_prefix="USERS_API_"
    )


class Settings(BaseSettings):
    postgres: PostgresSettings = PostgresSettings()
    api: ApiSettings = ApiSettings()

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")


settings = Settings()