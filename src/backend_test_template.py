from backend import PathNotFound
import time


class BackendTestTemplate(object):
    def test_check_connection(self):
        self.assertTrue(self.backend.check_connection())

    def test_read(self):
        self.backend.write("exists", b"data")
        time.sleep(2)
        self.assertEqual(self.backend.read("exists"), b"data")

    def test_write(self):
        self.backend.write("write_path", b"data1")
        time.sleep(2)
        self.assertTrue(self.backend.exists("write_path"))
        self.assertEqual(b"data1", self.backend.read("write_path"))

        self.backend.write("write_path", b"data2")
        time.sleep(2)
        self.assertTrue(self.backend.exists("write_path"))
        self.assertTrue(b"data2", self.backend.read("write_path"))

    def test_ls(self):
        self.backend.makedirs("dir")
        time.sleep(2)
        self.backend.write("dir/file1", b"data1")
        self.backend.write("dir/file2", b"data2")
        time.sleep(2)
        self.assertEqual(set(self.backend.ls("dir")),
                         {"dir/file1", "dir/file2"})

    def test_exists(self):
        self.assertFalse(self.backend.exists("exists"))

        self.backend.write("exists", b"data")
        time.sleep(2)
        self.assertTrue(self.backend.exists("exists"))

    def test_rm(self):
        self.backend.write("exists", b"data")
        time.sleep(2)
        self.backend.rm("exists")
        time.sleep(2)
        self.assertFalse(self.backend.exists("exists"))