import logging
import sys
import os
import tempfile
import filecmp

from unittest import TestCase, main
from memory_backend import MemoryBackend
from repo2 import Repo, decrypt, compress, generate_key
from pathlib import Path

logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)


class Repo2Test(TestCase):
    def setUp(self):
        self.backend = MemoryBackend()
        self.repo = Repo(self.backend)

    def test_init(self):
        self.assertFalse(self.backend.exists("keys/master-key"))
        self.assertFalse(self.repo.is_initialized())
        self.repo.init(b"password")

        self.assertTrue(self.backend.exists("keys/master-key"))
        self.assertTrue(self.backend.exists("keys/sha-key"))
        self.assertTrue(self.backend.exists("keys/key-salt"))
        self.assertTrue(self.repo.is_initialized())

        master = self.repo._get_master_key(b"password")
        decrypt(self.backend.read("keys/sha-key"), master)

        key = generate_key(self.backend.read("keys/key-salt"), b"password")
        self.assertEqual(decrypt(self.backend.read("keys/master-key"), key),
                         master)

    def test_backup_format(self):
        self.repo.init(b"password")
        self.repo.backup(b"password", [os.path.abspath(".")])

        snapshot_ids = self.repo.get_snapshot_ids()
        self.assertEqual(len(snapshot_ids), 1)

        snapshot_id = snapshot_ids[0]
        self.assertEqual(len(snapshot_id), 19)

        snapshot_obj = self.repo.get_snapshot_obj(b"password", snapshot_id)
        self.assertIn("data_format_version", snapshot_obj)
        self.assertIn("snapshot", snapshot_obj)
        self.assertIn("chunks", snapshot_obj)

        self.assertIsInstance(snapshot_obj["data_format_version"], int)
        self.assertEqual(snapshot_obj["data_format_version"], 1)
        self.assertIsInstance(snapshot_obj["snapshot"], dict)
        self.assertIsInstance(snapshot_obj["chunks"], list)

        referenced_chunk_ids = set()
        for path, node in snapshot_obj["snapshot"].items():
            self.assertEqual(Path(path).as_posix(), path)
            self.assertIn("type", node)
            if node["type"] == "file":
                self.assertIn("mtime", node)
                self.assertIn("range", node)
                start, ostart, end, oend = node["range"]
                for i in range(start, end + 1):
                    referenced_chunk_ids.add(i)
                    chunk_hash = snapshot_obj["chunks"][i]
                    self.assertTrue(
                        self.backend.exists(f"chunks/{chunk_hash}"))
            elif node["type"] == "dir":
                self.assertIn("mtime", node)
        self.assertEqual(sorted(referenced_chunk_ids),
                         list(range(len(snapshot_obj["chunks"]))))

    def test_check_password(self):
        self.repo.init(b"password")
        self.assertFalse(self.repo.check_password(b"notpassword"))
        self.assertTrue(self.repo.check_password(b"password"))

    def test_round_trip(self):
        tempdir = tempfile.TemporaryDirectory().name
        self.repo.init(b"password")
        snapshot_id, _ = self.repo.backup(b"password", [os.path.abspath(".")])
        self.repo.restore(b"password", snapshot_id, tempdir)

        dir_paths = []
        for root, dirs, files in os.walk("."):
            for d in dirs:
                path = os.path.join(root, d)
                dir_paths.append(path)
            for f in files:
                path = os.path.join(root, f)
                dir_paths.append(path)
        restore_paths = []
        for root, dirs, files in os.walk(
                os.path.join(tempdir,
                             os.path.abspath(".")[1:])):
            for d in dirs:
                path = os.path.join(root, d)
                restore_paths.append(path)
            for f in files:
                path = os.path.join(root, f)
                restore_paths.append(path)
        dir_paths.sort()
        restore_paths.sort()

        self.assertEqual(len(dir_paths), len(restore_paths))
        for dir_path, restore_path in zip(dir_paths, restore_paths):
            self.assertEqual(os.path.basename(dir_path),
                             os.path.basename(restore_path))
            self.assertEqual(os.path.isfile(dir_path),
                             os.path.isfile(restore_path))
            if os.path.isfile(dir_path):
                self.assertTrue(filecmp.cmp(dir_path, restore_path))
            print(os.path.basename(restore_path), "OK")

    def test_files_encrypted(self):
        self.repo.init(b"password")
        self.repo.backup(b"password", [os.path.abspath(".")])
        for path, data in self.backend.files.items():
            entropy = len(compress(data)) / len(data)
            self.assertGreater(entropy, 0.9)
            print(f"{path} entropy: {entropy} OK")


if __name__ == "__main__":
    main()