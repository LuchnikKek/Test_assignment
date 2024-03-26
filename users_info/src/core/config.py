from pydantic_settings import BaseSettings, SettingsConfigDict

from src.core.constants import ENV_FILEPATH


class DatabaseSettings(BaseSettings):
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


class LoggerSettings(BaseSettings):
    level: str
    format: str
    default_handlers: list
    level_console: str
    level_handlers: str
    level_unicorn_errors: str
    level_unicorn_access: str
    level_root: str

    model_config = SettingsConfigDict(env_prefix="USERS_LOG_", env_file=ENV_FILEPATH, extra="ignore")


class Settings(BaseSettings):
    database: DatabaseSettings = DatabaseSettings()
    api: ApiSettings = ApiSettings()
    logger: LoggerSettings = LoggerSettings()

    debug: bool

    model_config = SettingsConfigDict(env_file=ENV_FILEPATH, extra="ignore")


settings = Settings()
