from blobbackup.backend import Backend


class MemoryBackend(Backend):
    def __init__(self):
        self.files = {}

    def makedirs(self, path):
        pass

    def read(self, path):
        return self.files[path]

    def write(self, path, data):
        self.files[path] = data

    def ls(self, path):
        paths = []
        for key in self.files:
            if path in key:
                paths.append(key)
        return paths

    def exists(self, path):
        return path in self.files

    def rm(self, path):
        del self.files[path]
