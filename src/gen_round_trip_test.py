import unittest

from fs.osfs import OSFS
from fake_file_gen import FakeFileGen
from repo import Repo, get_paths

from memory_backend import MemoryBackend
from local_backend import LocalBackend
from aws_backend import AwsBackend
from gcp_backend import GcpBackend
from azure_backend import AzureBackend
from b2_backend import B2Backend
from sftp_backend import SftpBackend

from multiprocessing.pool import ThreadPool

import time
import os
import shutil
import warnings
import sys
import uuid


class GenRoundTripTest(unittest.TestCase):
    backend_type = "memory"
    nb_files = 50

    def setUp(self):
        warnings.filterwarnings("ignore",
                                category=ResourceWarning,
                                message="unclosed.*<ssl.SSLSocket.*>")
        self.prefix = str(uuid.uuid1())
        os.makedirs("tmp-files")
        self.fs = OSFS("tmp-files")
        self.gen = FakeFileGen(self.fs)
        self.gen.generate("/backup-from", self.nb_files)
        if self.backend_type == "memory":
            self.backend = MemoryBackend()
        if self.backend_type == "local":
            os.makedirs("tmp")
            self.backend = LocalBackend("tmp")
        if self.backend_type == "aws":
            self.backend = AwsBackend(
                "AKIAJ3EE6F33OHJFQDUA",
                "lkZIydI8MW1ipZHXIqYYEim5yGMRfQ4pke0o3bjQ", "bloobs-test",
                self.prefix)
        if self.backend_type == "gcp":
            self.backend = GcpBackend("creds/gcp.json", "bloobs-test",
                                      "bloobs-test", self.prefix)
        if self.backend_type == "azure":
            self.backend = AzureBackend(
                "DefaultEndpointsProtocol=https;AccountName=bimbastorageaccount;AccountKey=4roC08MX3p4d2dhR3fRFvMPC6hNb1mr+l16LxG7wjLb2iPRdme910zn/xByyxHyi3GPJc1YL542g8QBonq+RuA==;EndpointSuffix=core.windows.net",
                "bloobs-test", self.prefix)
        if self.backend_type == "b2":
            self.backend = B2Backend("000dc39ac8e3c600000000002",
                                     "K000lUsA6BBgjNrStKhkutV8TQicRo0",
                                     "bloobs-test", self.prefix)
        if self.backend_type == "sftp":
            self.backend = SftpBackend("35.202.113.38",
                                       "blobbackup",
                                       self.prefix,
                                       rsa_path="creds/sftp_id_rsa")
            self.backend.makedirs(self.prefix)

    def tearDown(self):
        shutil.rmtree("tmp-files")
        if self.backend_type == "local":
            shutil.rmtree("tmp")
        elif self.backend_type == "sftp":
            with self.backend._get_connection() as sftp:
                sftp.execute(f"rm -rf {self.backend.prefix}")
        else:
            for path in self.backend.ls(self.prefix):
                self.backend.rm(path)

    def verify(self, backup_dir, restore_dir):
        original_paths, _ = sorted(get_paths(backup_dir))
        restore_paths, _ = sorted(get_paths(f"{restore_dir}/{backup_dir[1:]}"))
        restore_path_len = len(restore_dir)
        for original_path, restore_path in zip(original_paths, restore_paths):
            restore_path_trun = restore_path[restore_path_len:]
            self.assertEqual(restore_path_trun, original_path)
            self.assertEqual(self.fs.isfile(original_path),
                             self.fs.isfile(restore_path))
            if self.fs.isfile(original_path):
                self.assertEqual(self.fs.readbytes(original_path),
                                 self.fs.readbytes(restore_path))

    def _test_round_trip(self, variable=False):
        self.repo = Repo(self.backend, enable_variable=variable)
        self.repo.init(b"password")
        first_before = time.time()
        snapshot_id, _ = self.repo.backup(
            b"password", [os.path.abspath("tmp-files/backup-from")])
        first_delta = time.time() - first_before
        print(f"First backup: {first_delta} seconds")

        self.repo.restore(b"password", snapshot_id, "tmp-files/restore1")
        self.verify("tmp-files/backup-from", "tmp-files/restore1")

        second_before = time.time()
        snapshot_id, _ = self.repo.backup(
            b"password", [os.path.abspath("tmp-files/backup-from")])
        second_delta = time.time() - second_before
        print(f"Second backup: {second_delta} seconds")

        self.assertLess(second_delta, first_delta)
        self.repo.restore(b"password", snapshot_id, "tmp-files/restore2")
        self.verify("tmp-files/backup-from", "tmp-files/restore2")

    def test_round_trip_fixed(self):
        self._test_round_trip(variable=False)

    def test_round_trip_variable(self):
        self._test_round_trip(variable=True)


if __name__ == "__main__":
    if len(sys.argv) > 2:
        GenRoundTripTest.backend_type = sys.argv.pop()
        GenRoundTripTest.nb_files = int(sys.argv.pop())
    unittest.main()