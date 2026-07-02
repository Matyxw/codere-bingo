from typing import Optional

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_env: str = "local"
    database_url: Optional[str] = None
    secret_key: Optional[str] = None
    qr_issuer: str = "Codere Bingo"
    default_max_cartones: int = 6
    default_min_cartones: int = 1
    web_print_url: Optional[str] = None
    web_print_token: Optional[str] = None
    audit_retention_days: int = 365
    cors_origins: str = "*"
    jwt_access_ttl: int = 30
    jwt_refresh_ttl: int = 1440

    model_config = {"env_file": ".env", "env_file_encoding": "utf-8"}


settings = Settings()
