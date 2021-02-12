from unittest import TestCase, main
from backend import PathNotFound
from gdrive_backend import GDriveBackend

from backend_test_template import BackendTestTemplate

import os
import warnings
import time


class GDriveBackendTest(TestCase, BackendTestTemplate):
    def setUp(self):
        warnings.filterwarnings("ignore",
                                category=ResourceWarning,
                                message="unclosed.*<ssl.SSLSocket.*>")
        self.backend = GDriveBackend(os.environ["BLOBBACKUP_GDRIVE_CRED_FILE"],
                                     os.environ["BLOBBACKUP_GDRIVE_FOLDER_ID"])

    def tearDown(self):
        self.backend.fs.writebytes("tmpdummy", b"dummy")
        time.sleep(2)
        self.backend.fs.removetree("")
        time.sleep(3)


if __name__ == "__main__":
    main()