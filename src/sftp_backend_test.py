from unittest import TestCase, main
from sftp_backend import SftpBackend

import os
import warnings
import uuid
import time


class SftpBackendTest(TestCase):
    def setUp(self):
        self.prefix = str(uuid.uuid1())
        warnings.filterwarnings("ignore",
                                category=ResourceWarning,
                                message="unclosed.*<ssl.SSLSocket.*>")
        self.backend = SftpBackend(os.environ["BLOBBACKUP_SFTP_HOST"],
                                   os.environ["BLOBBACKUP_SFTP_USER"],
                                   os.environ["BLOBBACKUP_SFTP_PREFIX"],
                                   rsa_path=os.environ["BLOBBACKUP_SFTP_RSA"])
        self.backend.makedirs(self.prefix)

    def tearDown(self):
        with self.backend._get_connection() as sftp:
            sftp.execute(f"rm -rf {self.backend.prefix}")

    def test_check_connection(self):
        self.assertTrue(self.backend.check_connection())

    def test_makedirs(self):
        self.backend.makedirs("test")
        self.assertTrue(self.backend.exists("test"))

    def test_round_trip(self):
        self.assertFalse(self.backend.exists("dir/test1"))
        self.assertFalse(self.backend.exists("dir/test2"))

        self.backend.write("dir/test1", b"test1")
        self.backend.write("dir/test2", b"test2")

        self.assertTrue(self.backend.exists("dir/test1"))
        self.assertTrue(self.backend.exists("dir/test2"))
        self.assertTrue(self.backend.ls("dir"), ["dir/test1", "dir/test2"])

        self.assertEqual(self.backend.read("dir/test1"), b"test1")
        self.assertEqual(self.backend.read("dir/test2"), b"test2")

        self.backend.rm("dir/test1")
        self.backend.rm("dir/test2")

        self.assertFalse(self.backend.exists('dir/test1'))
        self.assertFalse(self.backend.exists("dir/test2"))
        self.assertEqual(self.backend.ls("dir"), [])


if __name__ == "__main__":
    main()
