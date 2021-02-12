from PySide2.QtCore import QThread, Signal
from validator import Validator

class CommandThread(QThread):
    result = Signal(object)

    def __init__(self, function, arguments):
        QThread.__init__(self)
        self.function = function
        self.arguments = arguments

    def run(self):
        self.result.emit(self.function(self.arguments))


def config_worker(args):
    fs = args["fs"]
    args = args["args"]
    return Validator.validate(fs, args)
