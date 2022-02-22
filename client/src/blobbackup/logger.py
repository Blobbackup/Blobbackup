import os
import logging
import datetime

from logging import FileHandler

from blobbackup.util import LOGS_PATH


def get_logger():
    formatter = logging.Formatter("%(asctime)s %(levelname)s %(message)s")

    handler = FileHandler(
        os.path.join(LOGS_PATH, f"general-{datetime.date.today()}.txt")
    )
    handler.setFormatter(formatter)

    logger = logging.getLogger("blobbackup")
    logger.setLevel(logging.DEBUG)

    if len(logger.handlers) == 0:
        logger.addHandler(handler)

    return logger
