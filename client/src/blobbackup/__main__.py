import os
import sys
import argparse

from blobbackup.application import Application
from blobbackup.requestfulldiskdialog import RequestFullDiskDialog
from blobbackup.logindialog import LoginDialog
from blobbackup.welcomedialog import WelcomeDialog
from blobbackup.mainwindow import MainWindow
from blobbackup.systemtrayicon import SystemTrayIcon
from blobbackup.config import config, save_config
from blobbackup.heartbeat import is_alive
from blobbackup.logger import get_logger
from blobbackup.util import is_mac, load_scripts, full_disk_access


def main():
    logger = get_logger()
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--open-minimized",
        dest="open_minimized",
        action="store_true",
        default=False,
    )
    parser.add_argument(
        "--set-server",
        dest="server",
        default=None,
    )
    args = parser.parse_args()

    if args.server:
        config["meta"]["server"] = args.server
        save_config()
        sys.exit()

    if not is_alive():
        logger.info("Application started.")
        init_application_properties()
        application = Application()

        if is_mac() and not full_disk_access():
            request_dialog = RequestFullDiskDialog()
            request_dialog.exec()
            sys.exit()

        first_time = False
        if not client_initialized():
            first_time = True

            login_dialog = LoginDialog()
            login_successful = login_dialog.exec()
            if not login_successful:
                sys.exit()

            welcome_dialog = WelcomeDialog(login_dialog.email, login_dialog.password)
            accepted_terms = welcome_dialog.exec()
            if not accepted_terms:
                sys.exit()

        main_window = MainWindow(first_time)
        try:
            load_scripts()
        except PermissionError:
            logger.error("Failed to load scripts because of permission error.")
        if not args.open_minimized:
            main_window.show()

        tray = SystemTrayIcon(main_window)
        tray.setVisible(True)

        application.exec()
    else:
        logger.info("Application not started (already running).")


def client_initialized():
    return config["meta"].getboolean("initialized")


def init_application_properties():
    os.environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "1"


if __name__ == "__main__":
    main()
