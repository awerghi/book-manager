import logging
from pathlib import Path

from app.core.config import settings

LOG_DIR = Path(__file__).parent.parent / "logs"
LOG_DIR.mkdir(exist_ok=True)


def setup_logger():

    logging.basicConfig(
        level= settings.LOG_LEVEL,
        format = "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        handlers= [
            logging.FileHandler(LOG_DIR / "booknest.log"),
            logging.StreamHandler()
        ]
    )

    return logging.getLogger(__name__)

logger = setup_logger()