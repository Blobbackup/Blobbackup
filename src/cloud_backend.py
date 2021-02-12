from backend import Backend, PathNotFound


class CloudBackend(Backend):
    def __init__(self, prefix=None):
        Backend.__init__(self)
        self.prefix = prefix

    def _get_prefixed_path(self, path):
        if self.prefix is None:
            return path
        return f"{self.prefix}/{path}"

    def _get_unprefixed_path(self, path):
        if self.prefix is None:
            return path
        prefix_len = len(self.prefix) + 1
        return path[prefix_len:]

    def makedirs(self, path):
        pass