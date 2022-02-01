import subprocess

from blobbackup.util import RESTIC_PATH, get_restic_env, get_password_from_keyring
from blobbackup.config import config
from blobbackup.api import get_computer

if __name__ == "__main__":
    email = config["meta"]["email"]
    password = get_password_from_keyring()
    computer_id = config["meta"]["computer_id"]
    computer = get_computer(email, password, computer_id)
    subprocess.run(
        [RESTIC_PATH, "stats", "--mode", "raw-data"],
        env=get_restic_env(computer, password),
    )
