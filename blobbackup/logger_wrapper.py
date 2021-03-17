import time


class LoggerWrapper(object):
    def __init__(self, logger):
        self.logger = logger

    def debug(self, message):
        self.logger.debug(message)

    def info(self, message):
        self.logger.info(message)
        time.sleep(0.5)
