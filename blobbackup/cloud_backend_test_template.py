from blobbackup.backend_test_template import BackendTestTemplate
from blobbackup.backend import PathNotFound


class CloudBackendTestTemplate(BackendTestTemplate):
    def _tearDown(self):
        try:
            for key in self.backend.ls(""):
                self.backend.rm(key)
        except PathNotFound:
            pass

    def test_makedirs(self):
        self.backend.makedirs("does_not_matter")