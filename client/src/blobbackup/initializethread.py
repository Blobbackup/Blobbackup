import sys
import subprocess
import socket
import platform
import shutil

from PyQt6.QtCore import QThread, pyqtSignal

from blobbackup.api import create_new_computer
from blobbackup.config import config, save_config
from blobbackup.status import (
    save_last_backed_up,
    save_selected_files,
    save_current_status,
)
from blobbackup.util import (
    HOME_PATH,
    CREATE_NO_WINDOW,
    is_windows,
    is_mac,
    save_password_in_keyring,
    get_restic_env,
    get_restic_init_command,
    posix_path,
    initialize_keep_alive,
)

DEFAULT_MAC_INCLUSIONS = ",".join(["/"])
DEFAULT_MAC_EXCLUSIONS = ",".join(
    [
        "/Applications",
        "/Library",
        "/Private",
        "/System",
        "/bin",
        "/dev",
        "/etc",
        "/net",
        "/sbin",
        "/usr",
        "/home",
        "*.wab~",
        "*.vmc",
        "*.vhd",
        "*.vo1",
        "*.vo2",
        "*.vsv",
        "*.vud",
        "*.iso",
        "*.dmg",
        "*.sparseimage",
        "*.sys",
        "*.cab",
        "*.exe",
        "*.msi",
        "*.dll",
        "*.dl_",
        "*.wim",
        "*.ost",
        "*.o",
        "*.qtch",
        "*.log",
        "*.ithmb",
        "*.vmdk",
        "*.vmem",
        "*.vmsd",
        "*.vmsn",
        "*.vmx",
        "*.vmxf",
        "*.menudata",
        "*.appicon",
        "*.appinfo",
        "*.pva",
        "*.pvs",
        "*.pvi",
        "*.pvm",
        "*.fdd",
        "*.hds",
        "*.drk",
        "*.mem",
        "*.nvram",
        "*.hdd",
        posix_path(HOME_PATH),
    ]
)
DEFAULT_WIN_INCLUSIONS = ",".join(["C:/"])
DEFAULT_WIN_EXCLUSIONS = ",".join(
    [
        "C:/Windows",
        "C:/I386",
        "C:/RECYCLER",
        "C:/MSOCache",
        "C:/Program Files",
        "C:/Program Files (x86)",
        "C:/Users/All Users/Microsoft",
        "C:/Users/All Users/Microsoft Help",
        "*.wab~",
        "*.vmc",
        "*.vhd",
        "*.vo1",
        "*.vo2",
        "*.vsv",
        "*.vud",
        "*.iso",
        "*.dmg",
        "*.sparseimage",
        "*.sys",
        "*.cab",
        "*.exe",
        "*.msi",
        "*.dll",
        "*.dl_",
        "*.wim",
        "*.ost",
        "*.o",
        "*.qtch",
        "*.log",
        "*.ithmb",
        "*.vmdk",
        "*.vmem",
        "*.vmsd",
        "*.vmsn",
        "*.vmx",
        "*.vmxf",
        "*.menudata",
        "*.appicon",
        "*.appinfo",
        "*.pva",
        "*.pvs",
        "*.pvi",
        "*.pvm",
        "*.fdd",
        "*.hds",
        "*.drk",
        "*.mem",
        "*.nvram",
        "*.hdd",
        posix_path(HOME_PATH),
    ]
)


class InitializeThread(QThread):
    initialized = pyqtSignal()

    def __init__(self, email, password):
        QThread.__init__(self)
        self.email = email
        self.password = password

    def run(self):
        initialize_client(self.email, self.password)
        self.initialized.emit()


def get_computer_name():
    return socket.gethostname()


def initialize_client(email, password):
    computer = create_computer_or_die(email, password)
    create_restic_repo_or_die(computer, password)
    config["meta"]["initialized"] = "yes"
    config["meta"]["email"] = email
    config["meta"]["computer_id"] = str(computer["id"])
    config["general"]["computer_name"] = get_computer_name()
    config["general"]["backup_schedule"] = "Automatic"
    if is_windows():
        config["inclusions"]["paths"] = DEFAULT_WIN_INCLUSIONS
        config["exclusions"]["paths"] = DEFAULT_WIN_EXCLUSIONS
    elif is_mac():
        config["inclusions"]["paths"] = DEFAULT_MAC_INCLUSIONS
        config["exclusions"]["paths"] = DEFAULT_MAC_EXCLUSIONS
    save_config()
    save_password_in_keyring(password)
    save_last_backed_up("Creating your first backup. This window can be safely closed.")
    save_selected_files("0 files / 0 B")
    save_current_status("Idle")
    initialize_keep_alive()


def create_computer_or_die(email, password):
    computer_name = get_computer_name()
    operating_system = platform.platform()
    computer = create_new_computer(email, password, computer_name, operating_system)
    if computer == None:
        sys.exit()
    return computer


def create_restic_repo_or_die(computer, password):
    if is_windows():
        ret = subprocess.run(
            get_restic_init_command(),
            env=get_restic_env(computer, password),
            creationflags=CREATE_NO_WINDOW,
        )
    elif is_mac():
        ret = subprocess.run(
            get_restic_init_command(),
            env=get_restic_env(computer, password),
        )
    if ret.returncode != 0:
        sys.exit()
