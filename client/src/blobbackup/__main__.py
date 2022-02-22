import os
import sys

from blobbackup.application import Application
from blobbackup.logindialog import LoginDialog
from blobbackup.welcomedialog import WelcomeDialog
from blobbackup.mainwindow import MainWindow
from blobbackup.systemtrayicon import SystemTrayIcon
from blobbackup.config import config
from blobbackup.heartbeat import is_alive
from blobbackup.logger import get_logger


def main():
    logger = get_logger()

    if not is_alive():
        logger.info("application started")
        init_application_properties()
        application = Application()

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
        main_window.show()

        tray = SystemTrayIcon(main_window)
        tray.setVisible(True)

        application.exec()
    else:
        logger.info("application already running")


def client_initialized():
    return config["meta"].getboolean("initialized")


def init_application_properties():
    os.environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "1"


if __name__ == "__main__":
    main()
