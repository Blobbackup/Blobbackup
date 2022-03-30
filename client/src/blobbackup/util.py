import os
import sys
import hashlib
import base64
import platform
import pathlib
import subprocess
import shutil
import tempfile
import stat

from Crypto.Protocol.KDF import PBKDF2
from Crypto.Hash import SHA256
from keyring import get_password, set_password, set_keyring
from PyQt6.QtGui import QPixmap
from blobbackup._version import __version__


def is_windows():
    return sys.platform == "win32" or sys.platform == "win64"


def is_mac():
    return sys.platform == "darwin"


def is_arm():
    return "arm64" in platform.platform()


def make_executable(path):
    st = os.stat(path)
    os.chmod(path, st.st_mode | stat.S_IEXEC)


if is_windows():
    import keyring.backends.Windows
    import win32timezone

    set_keyring(keyring.backends.Windows.WinVaultKeyring())
elif is_mac():
    import keyring.backends.OS_X

    set_keyring(keyring.backends.OS_X.Keyring())

BASE_APP_URL = "https://app.blobbackup.com"
BASE_URL = "https://blobbackup.com"
PRIVACY_URL = BASE_URL + "/privacy"
SUPPORT_URL = BASE_URL + "/support"
TERMS_URL = BASE_URL + "/terms"
GUIDE_URL = BASE_URL + "/support/how-to-grant-full-disk-access-on-mac"

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
FULL_DISK_SCREENSHOT_PATH = get_asset(os.path.join("img", "full_disk_screenshot.png"))

KEEP_ALIVE_PLIST_PATH = get_asset(os.path.join("misc", "com.blobbackup.plist"))
KEEP_ALIVE_PLIST_DEST_PATH = os.path.join(
    os.path.expanduser("~"), "Library", "LaunchAgents", "com.blobbackup.plist"
)
UPDATER_PLIST_PATH = get_asset(os.path.join("misc", "com.blobbackup.updater.plist"))
UPDATER_PLIST_DEST_PATH = os.path.join(
    os.path.expanduser("~"), "Library", "LaunchAgents", "com.blobbackup.updater.plist"
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

MAC_UPDATER_PATH = get_asset(os.path.join("misc", "blobbackup-updater.sh"))
MAC_UPDATER_DEST_PATH = os.path.join(HOME_PATH, "blobbackup-updater.sh")

WIN_UPDATER_PATH = get_asset(os.path.join("misc", "blobbackup-updater.exe"))
WIN_UPDATER_DEST_PATH = os.path.join(HOME_PATH, "blobbackup-updater.exe")

VERSION_FILE_PATH = os.path.join(HOME_PATH, "version.txt")
with open(VERSION_FILE_PATH, "w") as f:
    f.write(__version__)

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
    if is_mac() and backup_connected_file_systems == "No":
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
        "RESTIC_REPOSITORY": f"b2:{computer['b2_bucket_name']}:{computer['uuid']}",
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


def load_scripts():
    load_keep_alive_script()
    load_updater_script()


def load_updater_script():
    if is_windows():
        load_updater_script_win()
    elif is_mac():
        load_updater_script_mac()


def load_keep_alive_script():
    if is_windows():
        load_keep_alive_script_win()
    elif is_mac():
        load_keep_alive_script_mac()


def load_keep_alive_script_win():
    remove_windows_task("com.blobbackup.login")
    add_windows_task(
        "com.blobbackup",
        [
            "schtasks",
            "/create",
            "/tr",
            "C:/Program Files (x86)/blobbackup/blobbackup-win32.exe --open-minimized",
            "/sc",
            "HOURLY",
            "/rl",
            "HIGHEST",
            "/f",
        ],
    )


def load_updater_script_win():
    shutil.copyfile(WIN_UPDATER_PATH, WIN_UPDATER_DEST_PATH)
    add_windows_task(
        "com.blobbackup.updater",
        [
            "schtasks",
            "/create",
            "/tr",
            WIN_UPDATER_DEST_PATH,
            "/sc",
            "HOURLY",
            "/rl",
            "HIGHEST",
            "/f",
        ],
    )


def add_windows_task(name, command):
    subprocess.run(
        command + ["/tn", name],
        creationflags=CREATE_NO_WINDOW,
    )
    ret = subprocess.run(
        [
            "schtasks",
            "/query",
            "/xml",
            "/tn",
            name,
        ],
        creationflags=CREATE_NO_WINDOW,
        stdout=subprocess.PIPE,
    )
    xml_content = ret.stdout.decode("utf-8")
    xml_content = xml_content.replace(
        "<DisallowStartIfOnBatteries>true</DisallowStartIfOnBatteries>",
        "<DisallowStartIfOnBatteries>false</DisallowStartIfOnBatteries>",
    )
    with tempfile.TemporaryDirectory() as root:
        xml_file = os.path.join(root, "task.xml")
        with open(xml_file, "w") as f:
            f.write(xml_content)
        ret = subprocess.run(
            [
                "schtasks",
                "/create",
                "/xml",
                xml_file,
                "/f",
                "/tn",
                name,
            ],
            creationflags=CREATE_NO_WINDOW,
        )


def remove_windows_task(name):
    subprocess.run(
        ["schtasks", "/delete", "/tn", name, "/f"],
        creationflags=CREATE_NO_WINDOW,
    )


def load_keep_alive_script_mac():
    shutil.copyfile(KEEP_ALIVE_PLIST_PATH, KEEP_ALIVE_PLIST_DEST_PATH)
    subprocess.run(["launchctl", "unload", KEEP_ALIVE_PLIST_DEST_PATH])
    subprocess.run(["launchctl", "load", KEEP_ALIVE_PLIST_DEST_PATH])


def load_updater_script_mac():
    shutil.copyfile(MAC_UPDATER_PATH, MAC_UPDATER_DEST_PATH)
    make_executable(MAC_UPDATER_DEST_PATH)
    shutil.copyfile(UPDATER_PLIST_PATH, UPDATER_PLIST_DEST_PATH)
    subprocess.run(["launchctl", "unload", UPDATER_PLIST_DEST_PATH])
    subprocess.run(["launchctl", "load", UPDATER_PLIST_DEST_PATH])


def full_disk_access():
    try:
        with open("/Library/Preferences/com.apple.TimeMachine.plist", "rb") as f:
            _ = f.read(1)
    except PermissionError:
        return False
    return True
