from PyQt5.QtWidgets import QApplication


class Application(QApplication):
    def __init__(self):
        QApplication.__init__(self, [])
        self.setStyle("Fusion")
        self.setQuitOnLastWindowClosed(False)
