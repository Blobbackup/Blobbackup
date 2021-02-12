TEST_CONNECTION_DATA = b"connection"
TEST_CONNECTION_PATH = "connection"


class PathNotFound(Exception):
    pass


class Backend(object):
    def __init__(self):
        pass

    def check_connection(self):
        try:
            self.write(TEST_CONNECTION_PATH, TEST_CONNECTION_DATA)
            assert self.read(TEST_CONNECTION_PATH) == TEST_CONNECTION_DATA
            self.rm(TEST_CONNECTION_PATH)
            return True
        except:
            return False

    def makedirs(self, path):
        raise NotImplementedError()

    def read(self, path):
        raise NotImplementedError()

    def write(self, path, data):
        raise NotImplementedError()

    def ls(self, path):
        raise NotImplementedError()

    def exists(self, path):
        raise NotImplementedError()

    def rm(self, path):
        raise NotImplementedError()
