from typing import Optional

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_env: str = "local"
    database_url: str
    secret_key: str
    qr_issuer: str = "Codere Bingo"
    default_min_cartones: int = 1
    default_max_cartones: int = 6
    cors_origins: str = "*"
    web_print_url: Optional[str] = None
    web_print_token: Optional[str] = None
    audit_retention_days: int = 365
    jwt_access_ttl: int = 30
    jwt_refresh_ttl: int = 60 * 24

    model_config = {"env_file": ".env", "env_file_encoding": "utf-8"}


settings = Settings()
