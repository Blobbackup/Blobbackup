import os

from configparser import ConfigParser

from blobbackup.util import HOME_PATH, BASE_APP_URL

CONFIG_PATH = os.path.join(HOME_PATH, "config.ini")

config = ConfigParser()


def load_config():
    config.read(CONFIG_PATH)


def save_config():
    with open(CONFIG_PATH, "w") as f:
        config.write(f)


def add_new_variables():
    updated = False
    if "server" not in config["meta"]:
        config["meta"]["server"] = BASE_APP_URL
        updated = True
    if "max_upload_kibs" not in config["general"]:
        config["general"]["max_upload_kibs"] = "0"
        updated = True
    if "backup_connected_files_systems" not in config["general"]:
        config["general"]["backup_connected_file_systems"] = "No"
        updated = True
    if updated:
        save_config()


if not os.path.exists(CONFIG_PATH):
    config["meta"] = {}
    config["meta"]["initialized"] = "no"
    config["meta"]["email"] = ""
    config["meta"]["computer_id"] = ""
    config["meta"]["server"] = BASE_APP_URL

    config["general"] = {}
    config["general"]["computer_name"] = ""
    config["general"]["backup_schedule"] = ""
    config["general"]["max_upload_kibs"] = "0"
    config["general"]["backup_connected_file_systems"] = "No"

    config["inclusions"] = {}
    config["inclusions"]["paths"] = ""

    config["exclusions"] = {}
    config["exclusions"]["paths"] = ""
    save_config()
else:
    load_config()
    add_new_variables()
