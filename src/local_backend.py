from os import makedirs, walk, remove
from os.path import join, exists, dirname
from backend import Backend

from retry import retry

TRIES = 3
DELAY = 1


class LocalBackend(Backend):
    def __init__(self, root_path):
        self.root_path = root_path

    @retry((OSError, FileNotFoundError), tries=TRIES, delay=DELAY)
    def makedirs(self, path):
        if not exists(join(self.root_path, path)):
            makedirs(join(self.root_path, path))

    @retry((OSError, FileNotFoundError), tries=TRIES, delay=DELAY)
    def read(self, path):
        with open(join(self.root_path, path), "rb") as f:
            return f.read()

    @retry((OSError, FileNotFoundError), tries=TRIES, delay=DELAY)
    def write(self, path, data):
        if not exists(dirname(join(self.root_path, path))):
            makedirs(dirname(join(self.root_path, path)))
        with open(join(self.root_path, path), "wb") as f:
            f.write(data)

    @retry((OSError, FileNotFoundError), tries=TRIES, delay=DELAY)
    def ls(self, path):
        paths = []
        for root, _, files in walk(join(self.root_path, path)):
            for f in files:
                full_path = join(root, f)
                paths.append(full_path)
        return paths

    @retry((OSError, FileNotFoundError), tries=TRIES, delay=DELAY)
    def exists(self, path):
        return exists(join(self.root_path, path))

    @retry((OSError, FileNotFoundError), tries=TRIES, delay=DELAY)
    def rm(self, path):
        remove(join(self.root_path, path))
