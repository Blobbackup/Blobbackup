from unittest import TestCase, main

from repo import Repo, AlreadyInitialized
from memory_backend import MemoryBackend
from models import BLOBBACKUP_DIR

import os
import sys
import uuid
import tempfile
import time


def readbytes(path):
    with open(path, "rb") as f:
        return f.read()


def writebytes(path, data):
    with open(path, "wb") as f:
        f.write(data)


class RepoTest(TestCase):
    def setUp(self):
        self.backend = MemoryBackend()
        self.repo = Repo(self.backend)

    def test_init(self):
        self.assertFalse(self.repo.is_initialized())
        self.assertFalse(self.backend.exists("keys/master"))
        self.assertFalse(self.backend.exists("keys/salt"))

        self.repo.init(b"password")

        self.assertTrue(self.repo.is_initialized())
        self.assertTrue(self.backend.exists("keys/master"))
        self.assertTrue(self.backend.exists("keys/salt"))

        self.assertFalse(self.repo.check_password(b"password1"))
        self.assertTrue(self.repo.check_password(b"password"))

        with self.assertRaises(AlreadyInitialized):
            self.repo.init(b"password")

    def test_snapshot_round_trip(self):
        self.repo.init(b"password")
        master_key = self.repo._get_master_key(b"password")
        self.repo._save_snapshot(master_key, {"test": "test"}, "test")
        self.assertEqual(self.repo.get_snapshot_obj(b"password", "test"),
                         {"test": "test"})

    def test_get_snapshot_ids(self):
        self.repo.init(b"password")
        master_key = self.repo._get_master_key(b"password")
        self.repo._save_snapshot(master_key, {"test": "test"}, "snapshot1")
        self.repo._save_snapshot(master_key, {"test": "test"}, "snapshot2")
        self.assertEqual(self.repo.get_snapshot_ids(),
                         ["snapshot1", "snapshot2"])

    def test_get_prefix_paths_single(self):
        self.assertEqual(
            self.repo._get_prefix_paths_single("/dir1/dir2/file1"),
            ["/dir1/dir2", "/dir1", "/"])

    def test_gen_blobs_fixed(self):
        path = f"{tempfile.gettempdir()}/tmp"
        self.repo.blob_size = 100
        with open(path, "wb") as f:
            f.write(b"0" * (self.repo.blob_size * 5 + 20))
        expected = [b"0" * self.repo.blob_size] * 5 + [b"0" * 20]
        blobs = list(self.repo._gen_blobs_fixed(path))
        self.assertEqual(expected, blobs)
        with open(path, "rb") as f:
            data = f.read()
        self.assertEqual(data, b"".join(blobs))

    def test_gen_blobs_buz(self):
        path = f"{tempfile.gettempdir()}/tmp"
        self.repo.blob_size = 100
        with open(path, "wb") as f:
            f.write(b"0" * (self.repo.blob_size * 5 + 20))
        blobs = list(self.repo._gen_blobs_buz(path))
        with open(path, "rb") as f:
            data = f.read()
        self.assertEqual(data, b"".join(blobs))

    def test_get_blob_size(self):
        self.repo.init(b"password")
        self.backend.write("blobs/blob1", b"test")
        self.backend.write("blobs/blob2", b"test")
        self.assertEqual(self.repo._get_blob_set(), {"blob1", "blob2"})

    def test_round_trip_prune(self):
        if sys.platform == "win32" or sys.platform == "win64":
            return
        inner_folder = str(uuid.uuid1())
        temp_dir_path = f"{tempfile.gettempdir()}/{inner_folder}"
        os.makedirs(f"{temp_dir_path}/dir1")
        os.makedirs(f"{temp_dir_path}/dir2")
        writebytes(f"{temp_dir_path}/dir1/file1", b"file1")
        writebytes(f"{temp_dir_path}/dir1/file2", b"file2")
        writebytes(f"{temp_dir_path}/dir2/file3", b"file3")
        writebytes(f"{temp_dir_path}/dir2/file4", b"file4")
        writebytes(f"{temp_dir_path}/dir2/exclude_file1", b"exclude_file1")
        writebytes(f"{temp_dir_path}/dir2/exclude_file2", b"exclude_file2")
        writebytes(f"{temp_dir_path}/file5", b"file5")

        self.repo.init(b"password")
        self.repo.backup(b"password", [temp_dir_path],
                         exclude_rules={f"{temp_dir_path}/dir2/exclude*"})

        snapshot_id = os.path.basename(self.backend.ls("snapshots")[0])
        snapshot = self.repo.get_snapshot_obj(b"password", snapshot_id)
        snapshot_paths = {(node["path"], node["type"]) for node in snapshot}

        dir_paths = set(self.repo._get_prefix_paths_single(temp_dir_path))
        dir_paths.add(temp_dir_path)
        dir_paths.update([f"{temp_dir_path}/dir1", f"{temp_dir_path}/dir2"])
        file_paths = {
            f"{temp_dir_path}/dir1/file1", f"{temp_dir_path}/dir1/file2",
            f"{temp_dir_path}/dir2/file3", f"{temp_dir_path}/dir2/file4",
            f"{temp_dir_path}/file5"
        }
        expected_snapshot_paths = set()
        expected_snapshot_paths.update([(path, "dir") for path in dir_paths])
        expected_snapshot_paths.update([(path, "file") for path in file_paths])

        self.assertEqual(snapshot_paths, expected_snapshot_paths)

        temp_restore_path = f"{tempfile.gettempdir()}/{uuid.uuid1()}"
        self.repo.restore(b"password",
                          snapshot_id,
                          temp_restore_path,
                          restore_paths={
                              f"{temp_dir_path}/file5",
                              f"{temp_dir_path}/dir1/file1"
                          })
        self.assertEqual(
            readbytes(f"{temp_restore_path}/{temp_dir_path}/file5"), b"file5")
        self.assertEqual(
            readbytes(f"{temp_restore_path}/{temp_dir_path}/dir1/file1"),
            b"file1")
        self.assertEqual(
            len(os.listdir(f"{temp_restore_path}/{temp_dir_path}")), 2)

        time.sleep(1)
        self.repo.backup(b"password", [f"{temp_dir_path}/dir1"])
        self.repo.delete(snapshot_id)
        self.repo.prune(b"password")

        self.assertEqual(len(self.backend.ls("snapshots")), 1)
        self.assertEqual(len(self.backend.ls("blobs")), 2)


if __name__ == "__main__":
    main()