import os
import time

from blobbackup.util import HOME_PATH, HEARTBEAT_SECONDS

HEARTBEAT_PATH = os.path.join(HOME_PATH, "heartbeat.txt")


def heartbeat():
    with open(HEARTBEAT_PATH, "w") as f:
        f.write(str(time.time()))


def is_alive():
    if not os.path.exists(HEARTBEAT_PATH):
        return False
    try:
        with open(HEARTBEAT_PATH, "r") as f:
            delta_seconds = time.time() - float(f.read())
    except ValueError:
        heartbeat()
        return True
    return delta_seconds < (HEARTBEAT_SECONDS * 2)
