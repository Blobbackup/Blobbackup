from PyQt6.QtGui import QIcon
import sys

from PyQt6.QtWidgets import QSystemTrayIcon, QMenu

from blobbackup.util import LOGO_PADDED_PATH
from blobbackup._version import __version__


class SystemTrayIcon(QSystemTrayIcon):
    def __init__(self, main_window):
        QSystemTrayIcon.__init__(self)
        self.main_window = main_window
        self.setIcon(QIcon(LOGO_PADDED_PATH))
        self.initialize_context_menu()

    def initialize_context_menu(self):
        self.menu = QMenu()
        self.version_action = self.menu.addAction(f"Version {__version__}")
        self.version_action.setEnabled(False)
        self.open_action = self.menu.addAction("Open", self.show_main_window)
        self.settings_action = self.menu.addAction(
            "Settings", self.main_window.open_settings
        )
        self.quit_action = self.menu.addAction("Quit", sys.exit)
        self.setContextMenu(self.menu)

    def show_main_window(self):
        self.main_window.show()
        self.main_window.activateWindow()
        self.main_window.raise_()
