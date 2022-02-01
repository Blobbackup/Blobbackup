import os

from configparser import ConfigParser

from blobbackup.util import HOME_PATH

CONFIG_PATH = os.path.join(HOME_PATH, "config.ini")

config = ConfigParser()


def load_config():
    config.read(CONFIG_PATH)


def save_config():
    with open(CONFIG_PATH, "w") as f:
        config.write(f)


if not os.path.exists(CONFIG_PATH):
    config["meta"] = {}
    config["meta"]["initialized"] = "no"
    config["meta"]["email"] = ""
    config["meta"]["computer_id"] = ""

    config["general"] = {}
    config["general"]["computer_name"] = ""
    config["general"]["backup_schedule"] = ""

    config["inclusions"] = {}
    config["inclusions"]["paths"] = ""

    config["exclusions"] = {}
    config["exclusions"]["paths"] = ""
    save_config()
else:
    load_config()
