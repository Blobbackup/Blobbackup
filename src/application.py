from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *

import time
import sys
import os

from q_single_application import QSingleApplication
from main_window import MainWindow
from models import get_resource_path
from scheduler import Scheduler

from models import Settings


class Application:
    """
    Taken from https://gist.github.com/hogelog/5338905
    """
    def __init__(self):
        self.app = QSingleApplication("BlobBackup", sys.argv)
        self.app.setQuitOnLastWindowClosed(False)
        self.app.setStyle("Fusion")
        self.window = MainWindow(self)
        self.scheduler = Scheduler(self.app)

        self.show_minimize_message = not Settings.get_param("minimize")

        self.app.start_backup.connect(self.window.go_backup)

        if self.app.isRunning():
            QMessageBox.warning(
                None, "BlobBackup already running",
                "An instance of BlobBackup is already running. Check your status bar."
            )
            sys.exit()

        menu = QMenu()
        window_action = menu.addAction("BlobBackup")
        window_action.triggered.connect(self.show_window)
        quit_action = menu.addAction("Exit")

        quit_action.triggered.connect(self.quit_action)

        self.tray = QSystemTrayIcon()
        self.tray.setIcon(QIcon(get_resource_path("images/logo.ico")))
        self.tray.setContextMenu(menu)
        self.tray.show()
        self.tray.setToolTip("BlobBackup")

        self.tray.activated.connect(self.tray_activated)

        self.show_window()

    def tray_activated(self, reason):
        if reason == QSystemTrayIcon.DoubleClick:
            self.show_window()

    def quit_action(self):
        reply = QMessageBox.question(
            self.window, "Exit BlobBackup?",
            "Are you sure you want to exit? Your scheduled backups will not take place.",
            QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            self.scheduler.shutdown()
            self.window.log_file_thread.terminate_gracefully()
            self.window.log_file_thread.terminate()
            sys.exit()

    def run(self):
        self.app.exec_()
        sys.exit()

    def show_window(self):
        self.window.show()
        self.window.activateWindow()
        self.window.raise_()

    def notify(self, message):
        self.tray.showMessage("BlobBackup", message)


if __name__ == "__main__":
    os.environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "1"
    os.environ["QT_MAC_WANTS_LAYER"] = "1"
    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling,
                              True)  #enable highdpi scaling
    QApplication.setAttribute(Qt.AA_UseHighDpiPixmaps,
                              True)  #use highdpi icons

    app = Application()
    app.run()