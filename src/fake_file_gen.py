import random
import os
from fs.osfs import OSFS

MIN_FILE_SIZE = 1
MAX_FILE_SIZE = 2**22

MIN_FILES_PER_DIR = 0
MAX_FILES_PER_DIR = 32

MIN_DIRS_PER_DIR = 0
MAX_DIRS_PER_DIR = 8

MAX_DEPTH = 8


class FakeFileGen(object):
    def __init__(self, fs=None):
        if fs is None:
            fs = OSFS(".")
        self.fs = fs
        self.total_size = 0

    def gen_random_file(self, num_files):
        file_size = random.randint(MIN_FILE_SIZE, MAX_FILE_SIZE)
        file_name = f"file-{num_files}"
        random_bytes = os.urandom(file_size)
        return file_name, random_bytes

    def gen_random_recursive(self, path, num_files, max_files, depth):
        if depth > MAX_DEPTH:
            return num_files
        files_per_dir = random.randint(MIN_FILES_PER_DIR, MAX_FILES_PER_DIR)
        for _ in range(files_per_dir):
            if num_files >= max_files:
                return num_files
            file_name, random_bytes = self.gen_random_file(num_files)
            self.total_size += len(random_bytes) // 1024 // 1024
            self.fs.writebytes(f"{path}/{file_name}", random_bytes)
            print(f"Generating: {num_files} / {max_files} ({self.total_size:,} MB)")
            num_files += 1
        dirs_per_dir = random.randint(MIN_DIRS_PER_DIR, MAX_DIRS_PER_DIR)
        for _ in range(dirs_per_dir):
            if num_files >= max_files:
                return num_files
            file_name = f"dir-{num_files}"
            file_path = f"{path}/{file_name}"
            self.fs.makedirs(file_path)
            num_files += 1
            print(f"Generating: {num_files} / {max_files} ({self.total_size:,} MB)")
            num_files = self.gen_random_recursive(file_path, num_files,
                                                  max_files, depth + 1)
        return num_files

    def generate(self, generate_dir, max_files):
        self.fs.makedirs(generate_dir)
        self.total_size = 0
        self.gen_random_recursive(generate_dir, 0, max_files, 0)