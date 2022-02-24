import os
import sys
import hashlib
import base64
import platform
import pathlib

from Crypto.Protocol.KDF import PBKDF2
from Crypto.Hash import SHA256
from keyring import get_password, set_password, set_keyring
from PyQt6.QtGui import QPixmap


def is_windows():
    return sys.platform == "win32" or sys.platform == "win64"


def is_mac():
    return sys.platform == "darwin"


def is_arm():
    return "arm64" in platform.platform()


if is_windows():
    import keyring.backends.Windows
    import win32timezone

    set_keyring(keyring.backends.Windows.WinVaultKeyring())
elif is_mac():
    import keyring.backends.OS_X

    set_keyring(keyring.backends.OS_X.Keyring())

BASE_APP_URL = "https://app.blobbackup.com"
BASE_URL = "https://blobbackup.com"
B2_BUCKET = "blobbackup01"

HEARTBEAT_SECONDS = 1
BACKUP_STUCK_HOURS = 8


def get_asset(path):
    if getattr(sys, "frozen", False):
        bundle_dir = sys._MEIPASS
    else:
        bundle_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(bundle_dir, path)


LOGO_PATH = get_asset(os.path.join("img", "logo.png"))
LOGO_PADDED_PATH = get_asset(os.path.join("img", "logo_padded.png"))
CHECK_PATH = get_asset(os.path.join("img", "check.png"))
COMPUTER_PATH = get_asset(os.path.join("img", "computer.png"))
ARROW_PATH = get_asset(os.path.join("img", "arrow.png"))
CLOUD_PATH = get_asset(os.path.join("img", "cloud.png"))
FOLDER_PATH = get_asset(os.path.join("img", "folder.png"))

KEEP_ALIVE_PLIST_PATH = get_asset(os.path.join("misc", "com.blobbackup.plist"))
KEEP_ALIVE_PLIST_DEST_PATH = os.path.join(
    os.path.expanduser("~"), "Library", "LaunchAgents", "com.blobbackup.plist"
)

if is_windows():
    RESTIC_PATH = get_asset(os.path.join("bin", "blobbackup-win.exe"))
elif is_mac():
    if is_arm():
        RESTIC_PATH = get_asset(os.path.join("bin", "blobbackup-darwin-arm"))
    else:
        RESTIC_PATH = get_asset(os.path.join("bin", "blobbackup-darwin-amd"))

HOME_PATH = os.path.join(os.path.expanduser("~"), ".bb")
os.makedirs(HOME_PATH, exist_ok=True)

LOGS_PATH = os.path.join(HOME_PATH, "logs")
os.makedirs(LOGS_PATH, exist_ok=True)

CACHE_PATH = os.path.join(HOME_PATH, "cache")
os.makedirs(CACHE_PATH, exist_ok=True)

TMP_PATH = os.path.join(HOME_PATH, "tmp")
os.makedirs(TMP_PATH, exist_ok=True)

os.makedirs(os.path.dirname(KEEP_ALIVE_PLIST_DEST_PATH), exist_ok=True)

INCLUSIONS_FILE_PATH = os.path.join(HOME_PATH, "inclusions.txt")
EXCLUDIONS_FILE_PATH = os.path.join(HOME_PATH, "exclusions.txt")

CREATE_NO_WINDOW = 0x08000000


def hash_password(password, email):
    password_binary = password.encode("utf-8")
    email_binary = email.encode("utf-8")

    email_hashed_binary = hashlib.sha256(email_binary).digest()
    salt_binary = email_hashed_binary[:16]

    hash_binary = PBKDF2(
        password_binary, salt_binary, 32, 100000, hmac_hash_module=SHA256
    )
    hash = base64.b64encode(hash_binary).decode("ascii")
    return hash


def save_password_in_keyring(password):
    set_password("blobbackup", "account", password)


def get_password_from_keyring():
    return get_password("blobbackup", "account")


def get_pixmap(path, width, height):
    pixmap = QPixmap(path)
    pixmap = pixmap.scaled(width, height)
    return pixmap


def get_restic_init_command():
    return [RESTIC_PATH, "init"]


def get_restic_backup_command(max_upload_kibs, backup_connected_file_systems):
    env = [
        RESTIC_PATH,
        "backup",
        "--json",
        "--files-from",
        INCLUSIONS_FILE_PATH,
        "--iexclude-file",
        EXCLUDIONS_FILE_PATH,
        "--limit-upload",
        max_upload_kibs,
    ]
    if backup_connected_file_systems == "No":
        env += ["--one-file-system"]
    return env


def get_restic_unlock_command():
    return [RESTIC_PATH, "unlock"]


def get_restic_list_passwords_command():
    return [RESTIC_PATH, "key", "list", "--json"]


def get_restic_add_password_command(password_file):
    return [RESTIC_PATH, "key", "add", "--new-password-file", password_file]


def get_restic_delete_password_command(password_id):
    return [RESTIC_PATH, "key", "remove", password_id]


def get_restic_snapshots_command():
    return [RESTIC_PATH, "snapshots", "--json"]


def get_restic_ls_command(snapshot_id):
    return [RESTIC_PATH, "ls", snapshot_id]


def get_restic_restore_command(snapshot_id, target, paths):
    command = [RESTIC_PATH, "restore", "--target", target]
    includes = []
    for path in paths:
        includes.append("--include")
        includes.append(path)
    command += includes
    command.append(snapshot_id)
    return command


def get_restic_env(computer, password):
    env = {
        "RESTIC_PASSWORD": password,
        "RESTIC_REPOSITORY": f"b2:{B2_BUCKET}:{computer['uuid']}",
        "B2_ACCOUNT_KEY": computer["b2_application_key"],
        "B2_ACCOUNT_ID": computer["b2_key_id"],
        "RESTIC_CACHE_DIR": CACHE_PATH,
    }
    if is_windows():
        env.update(
            {
                "SYSTEMROOT": os.environ["SYSTEMROOT"],
                "TMP": TMP_PATH,
                "TEMP": TMP_PATH,
            }
        )
    elif is_mac():
        env.update(
            {
                "HOME": os.environ["HOME"],
                "TMPDIR": TMP_PATH,
            }
        )
    return env


def pretty_bytes(num, suffix="B"):
    for unit in ["", "K", "M", "G", "T", "P", "E", "Z"]:
        if abs(num) < 1024.0:
            return "%3.2f %s%s" % (num, unit, suffix)
        num /= 1024.0
    return "%.2f %s%s" % (num, "Y", suffix)


def posix_path(path):
    return pathlib.Path(path).as_posix()
