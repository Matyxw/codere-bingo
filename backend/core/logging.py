import logging
import sys

from backend.core.config import settings


def configure_logging() -> None:
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s %(levelname)s %(name)s %(message)s",
        stream=sys.stdout,
    )
    if settings.app_env != "local":
        logging.getLogger("sqlalchemy.engine").setLevel(logging.WARNING)
